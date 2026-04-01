#!/usr/bin/env python3
"""
Script to extract year and rating from _notes/ files and update notes.md
with data attributes for filtering.
"""

import os
import re
from pathlib import Path

def extract_metadata_from_note(filepath):
    """Extract year and rating from a note file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract date from front matter
    date_match = re.search(r'^date:\s*(\d{4})-\d{2}-\d{2}', content, re.MULTILINE)
    year = date_match.group(1) if date_match else None

    # Extract rating from "Recommend: X/10" line
    rating_match = re.search(r'Recommend:\s*(\d+)/10', content)
    rating = int(rating_match.group(1)) if rating_match else None

    return year, rating

def get_slug_from_filepath(filepath):
    """Get the slug (URL path) from the filepath."""
    # The slug is typically the filename without .md
    return Path(filepath).stem

def main():
    notes_dir = Path('_notes')
    notes_page = Path('_pages/notes.md')

    # Build mapping of slug -> (year, rating)
    metadata = {}
    for note_file in notes_dir.glob('*.md'):
        slug = get_slug_from_filepath(note_file)
        year, rating = extract_metadata_from_note(note_file)
        metadata[slug] = (year, rating)
        print(f"  {slug}: year={year}, rating={rating}")

    print(f"\nFound {len(metadata)} notes with metadata")

    # Count books by year
    years = {}
    for slug, (year, rating) in metadata.items():
        if year:
            years[year] = years.get(year, 0) + 1
    print("\nBooks by year:")
    for year in sorted(years.keys(), reverse=True):
        print(f"  {year}: {years[year]} books")

    # Count highly recommended (9+)
    highly_recommended = sum(1 for _, (_, r) in metadata.items() if r and r >= 9)
    print(f"\nHighly recommended (9+): {highly_recommended} books")

    # Read notes.md
    with open(notes_page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match book container divs
    # <div class="gr_grid_book_container"><a href="/notes/slug" ...
    pattern = r'(<div class="gr_grid_book_container">)(<a href="/notes/([^"]+)")'

    def replace_with_data(match):
        div_open = match.group(1)
        anchor = match.group(2)
        slug = match.group(3)

        # URL decode the slug for matching
        import urllib.parse
        decoded_slug = urllib.parse.unquote(slug)

        year, rating = metadata.get(decoded_slug, (None, None))

        # Build data attributes
        data_attrs = []
        if year:
            data_attrs.append(f'data-year="{year}"')
        if rating:
            data_attrs.append(f'data-rating="{rating}"')

        if data_attrs:
            # Insert data attributes into the div
            return f'<div class="gr_grid_book_container" {" ".join(data_attrs)}>{anchor}'
        else:
            return match.group(0)

    updated_content = re.sub(pattern, replace_with_data, content)

    # Count how many were updated
    original_divs = len(re.findall(r'<div class="gr_grid_book_container">', content))
    updated_divs = len(re.findall(r'<div class="gr_grid_book_container" data-', updated_content))
    print(f"\nUpdated {updated_divs}/{original_divs} book divs with data attributes")

    # Write back
    with open(notes_page, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"\nUpdated {notes_page}")

if __name__ == '__main__':
    main()
