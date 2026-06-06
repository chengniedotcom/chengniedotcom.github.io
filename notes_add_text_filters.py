#!/usr/bin/env python3
"""
Combined script to:
1. Parse Goodreads widget HTML and add new books to notes.md
2. Skip books that already exist in notes.md
3. Update all book divs with data-year and data-rating attributes from _notes/ files
"""

import os
import re
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup


# =============================================================================
# PASTE YOUR GOODREADS WIDGET HTML HERE
# =============================================================================
html = r'''
    <div class="gr_grid_book_container"><a title="大话方言" rel="nofollow" href="https://www.goodreads.com/book/show/40276751"><img alt="大话方言" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1527816684l/40276751._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="赶时间的人：一个外卖员的诗" rel="nofollow" href="https://www.goodreads.com/book/show/125366678"><img alt="赶时间的人：一个外卖员的诗" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1682143860l/125366678._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Heartburn" rel="nofollow" href="https://www.goodreads.com/book/show/225343.Heartburn"><img alt="Heartburn" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386647458l/225343._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Artificial Intelligence: A Guide for Thinking Humans" rel="nofollow" href="https://www.goodreads.com/book/show/43565360-artificial-intelligence"><img alt="Artificial Intelligence: A Guide for Thinking Humans" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1559680391l/43565360._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="For the Love of the Grind" rel="nofollow" href="https://www.goodreads.com/book/show/240019711-for-the-love-of-the-grind"><img alt="For the Love of the Grind" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1757018636l/240019711._SY75_.jpg" /></a></div>
'''
# =============================================================================


def get_short_title(title):
    """Return the title up to the first subtitle separator (colon, comma, parens, brackets, or spaced hyphen)."""
    return re.split(r'[:(,\[]|\s+-\s+', title)[0].strip()


def get_slug_from_title(title):
    """Generate URL slug from book title."""
    title_core = get_short_title(title)
    slug = re.sub(r'[^\w\s-]', '', title_core.lower())
    slug = re.sub(r'\s+', '-', slug)
    return slug


def get_existing_slugs(notes_md_path):
    """Extract all existing book slugs from notes.md."""
    with open(notes_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all href="/notes/slug" patterns
    slugs = set(re.findall(r'href="/notes/([^"]+)"', content))
    # URL decode the slugs for proper matching
    return {urllib.parse.unquote(s) for s in slugs}


def parse_and_format_html(html, existing_slugs):
    """Parse Goodreads HTML and format for notes.md, skipping existing books."""
    if not html.strip():
        return '', [], []

    # Fix JavaScript-style escaped closing tags (e.g. <\/a> → </a>)
    html = html.replace('\\/', '/')

    pattern = re.compile(r'_(SX|SY)\d+_.jpg')
    soup = BeautifulSoup(html, 'html.parser')

    new_books = []
    skipped_books = []

    for a_tag in soup.find_all('a'):
        title_original = a_tag.get('title', '')
        slug = get_slug_from_title(title_original)

        # Check if book already exists
        if slug in existing_slugs:
            skipped_books.append(title_original)
            # Remove this book's container from soup
            container = a_tag.find_parent('div', class_='gr_grid_book_container')
            if container:
                container.decompose()
            continue

        new_books.append(title_original)
        title_before_colon = get_short_title(title_original)

        a_tag['href'] = f"/notes/{slug}"
        a_tag['style'] = 'color: black; font-size: 10px;'

        img_tag = a_tag.img
        if img_tag:
            a_tag.clear()
            a_tag.append(img_tag)
            a_tag.append(' ')
            a_tag.append(title_before_colon)

    # Replace image size for all remaining images
    for img_tag in soup.find_all('img'):
        src = img_tag.get('src', '')
        img_tag['src'] = pattern.sub('_SX98_.jpg', src)

    # Generate formatted HTML
    formatted_html = ''
    for div in soup.find_all('div', class_='gr_grid_book_container'):
        formatted_html += '    ' + str(div) + '\n'

    return formatted_html, new_books, skipped_books


def add_books_to_notes(notes_md_path, formatted_html):
    """Insert new books at the beginning of the grid container."""
    with open(notes_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    container_start = content.find('<div class="gr_grid_container">')
    if container_start == -1:
        print("ERROR: Could not find grid container in notes.md")
        return False

    container_start += len('<div class="gr_grid_container">\n')
    updated_content = content[:container_start] + formatted_html + content[container_start:]

    with open(notes_md_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True


def extract_metadata_from_notes(notes_dir):
    """Extract year and rating from all _notes/ files."""
    metadata = {}

    for note_file in notes_dir.glob('*.md'):
        slug = note_file.stem

        with open(note_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract date from front matter
        date_match = re.search(r'^date:\s*(\d{4})-\d{2}-\d{2}', content, re.MULTILINE)
        year = date_match.group(1) if date_match else None

        # Extract rating from "Recommend: X/10" line
        rating_match = re.search(r'Recommend:\s*(\d+)/10', content)
        rating = int(rating_match.group(1)) if rating_match else None

        metadata[slug] = (year, rating)

    return metadata


def update_data_attributes(notes_md_path, metadata):
    """Update book divs with data-year and data-rating attributes."""
    with open(notes_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match book container divs (with or without existing data attributes)
    pattern = r'<div class="gr_grid_book_container"(?: data-year="\d+")?(?:\s*data-rating="\d+")?>'

    def replace_with_data(match):
        # Find the href in the following content to get the slug
        start = match.end()
        href_match = re.search(r'href="/notes/([^"]+)"', content[start:start+500])
        if not href_match:
            return match.group(0)

        slug = urllib.parse.unquote(href_match.group(1))
        year, rating = metadata.get(slug, (None, None))

        # Build data attributes
        data_attrs = []
        if year:
            data_attrs.append(f'data-year="{year}"')
        if rating:
            data_attrs.append(f'data-rating="{rating}"')

        if data_attrs:
            return f'<div class="gr_grid_book_container" {" ".join(data_attrs)}>'
        else:
            return '<div class="gr_grid_book_container">'

    # Process each div individually to get context
    result = []
    last_end = 0
    for match in re.finditer(pattern, content):
        result.append(content[last_end:match.start()])

        # Get the slug from href after this div
        search_area = content[match.end():match.end()+500]
        href_match = re.search(r'href="/notes/([^"]+)"', search_area)

        if href_match:
            slug = urllib.parse.unquote(href_match.group(1))
            year, rating = metadata.get(slug, (None, None))

            data_attrs = []
            if year:
                data_attrs.append(f'data-year="{year}"')
            if rating:
                data_attrs.append(f'data-rating="{rating}"')

            if data_attrs:
                result.append(f'<div class="gr_grid_book_container" {" ".join(data_attrs)}>')
            else:
                result.append('<div class="gr_grid_book_container">')
        else:
            result.append(match.group(0))

        last_end = match.end()

    result.append(content[last_end:])
    updated_content = ''.join(result)

    with open(notes_md_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True


REQUIRED_CSS_RULES = """\
.gr_grid_container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.gr_grid_book_container {
    width: 108px;
    overflow: hidden;
}

.gr_grid_book_container a {
    display: block;
    line-height: 1.2;
}

.gr_grid_book_container img {
    display: block;
    width: 100%;
    height: 145px;
    object-fit: cover;
}"""

def update_filter_buttons(notes_md_path):
    """Regenerate static filter buttons from current data-year values in notes.md."""
    with open(notes_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    years = sorted(set(re.findall(r'data-year="(\d+)"', content)), key=int, reverse=True)
    recent_years = [y for y in years if int(y) > 2021]
    has_older = any(int(y) <= 2021 for y in years)

    lines = ['<div class="filter-container" id="yearFilter">']
    lines.append('  <button class="filter-btn active" data-filter="all">All</button>')
    lines.append('  <button class="filter-btn" data-filter="recommended">★ 9+</button>')
    for year in recent_years:
        lines.append(f'  <button class="filter-btn" data-filter="{year}">{year}</button>')
    if has_older:
        lines.append('  <button class="filter-btn" data-filter="older">≤ 2021</button>')
    lines.append('  <span class="book-count"></span>')
    lines.append('</div>')
    new_block = '\n'.join(lines)

    updated = re.sub(
        r'<div class="filter-container" id="yearFilter">.*?</div>',
        new_block,
        content,
        count=1,
        flags=re.DOTALL,
    )

    if updated == content:
        return False

    with open(notes_md_path, 'w', encoding='utf-8') as f:
        f.write(updated)
    return True


def ensure_css(notes_md_path):
    """Ensure CSS rules are present for flex layout, gaps, and aligned title baseline."""
    with open(notes_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'display: flex' in content and 'object-fit: cover' in content:
        return False  # already present

    # Insert before closing </style>
    updated = content.replace('</style>', REQUIRED_CSS_RULES + '\n</style>', 1)
    with open(notes_md_path, 'w', encoding='utf-8') as f:
        f.write(updated)
    return True


def find_missing_notes(notes_dir, existing_slugs):
    """Find _notes/ files that are not included in notes.md."""
    missing = []

    for note_file in notes_dir.glob('*.md'):
        slug = note_file.stem
        if slug not in existing_slugs:
            # Get the title from the file for better display
            with open(note_file, 'r', encoding='utf-8') as f:
                content = f.read()
            title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else slug
            missing.append((slug, title, note_file.name))

    return missing


def main():
    script_dir = Path(__file__).parent
    notes_md_path = script_dir / '_pages' / 'notes.md'
    notes_dir = script_dir / '_notes'

    print("=" * 60)
    print("NOTES.MD UPDATE SCRIPT")
    print("=" * 60)

    # Step 1: Get existing slugs
    existing_slugs = get_existing_slugs(notes_md_path)
    print(f"\nFound {len(existing_slugs)} existing books in notes.md")

    # Step 2: Parse and add new books (if HTML provided)
    if html.strip():
        print("\n--- Processing new books from HTML ---")
        formatted_html, new_books, skipped_books = parse_and_format_html(html, existing_slugs)

        if skipped_books:
            print(f"\nSkipped {len(skipped_books)} existing books:")
            for title in skipped_books:
                print(f"  - {title}")

        if new_books:
            print(f"\nAdding {len(new_books)} new books:")
            for title in new_books:
                print(f"  + {title}")

            if add_books_to_notes(notes_md_path, formatted_html):
                print("\nSuccessfully added new books to notes.md!")
        else:
            print("\nNo new books to add.")
    else:
        print("\nNo HTML provided - skipping book addition step.")

    # Step 3: Extract metadata from _notes/ files
    print("\n--- Updating data attributes ---")
    metadata = extract_metadata_from_notes(notes_dir)
    print(f"Found metadata for {len(metadata)} note files")

    # Count stats
    years = {}
    highly_recommended = 0
    for slug, (year, rating) in metadata.items():
        if year:
            years[year] = years.get(year, 0) + 1
        if rating and rating >= 9:
            highly_recommended += 1

    print("\nBooks by year:")
    for year in sorted(years.keys(), reverse=True):
        print(f"  {year}: {years[year]} books")
    print(f"\nHighly recommended (9+): {highly_recommended} books")

    # Step 4: Update data attributes
    if update_data_attributes(notes_md_path, metadata):
        print(f"\nSuccessfully updated data attributes in notes.md!")

    # Step 5: Find notes files not in notes.md
    print("\n--- Checking for missing notes ---")
    existing_slugs = get_existing_slugs(notes_md_path)
    missing_notes = find_missing_notes(notes_dir, existing_slugs)
    if missing_notes:
        print(f"\nFound {len(missing_notes)} note files NOT in notes.md:")
        for slug, title, filename in sorted(missing_notes, key=lambda x: x[1]):
            print(f"  ! {filename} ({title})")
    else:
        print("\nAll note files are included in notes.md!")

    # Step 6: Ensure display:block CSS is present for tight title wrapping
    print("\n--- Checking CSS ---")
    if ensure_css(notes_md_path):
        print("Added missing display:block CSS rules to notes.md.")
    else:
        print("CSS rules already present.")

    # Step 7: Update static filter buttons to match current years
    print("\n--- Updating filter buttons ---")
    if update_filter_buttons(notes_md_path):
        print("Updated filter buttons in notes.md.")
    else:
        print("Filter buttons already up to date.")

    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)


if __name__ == '__main__':
    main()
