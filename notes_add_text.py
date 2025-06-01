import re
import os
from bs4 import BeautifulSoup

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Meditations for Mortals: Four Weeks to Embrace Your Limitations and Make Time for What Counts" rel="nofollow" href="https://www.goodreads.com/book/show/218702903-meditations-for-mortals"><img alt="Meditations for Mortals: Four Weeks to Embrace Your Limitations and Make Time for What Counts" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1726043663l/218702903._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Never Enough: From Barista to Billionaire" rel="nofollow" href="https://www.goodreads.com/book/show/199348906-never-enough"><img alt="Never Enough: From Barista to Billionaire" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1699912269l/199348906._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Chasing Daylight: How My Forthcoming Death Transformed My Life" rel="nofollow" href="https://www.goodreads.com/book/show/580305.Chasing_Daylight"><img alt="Chasing Daylight: How My Forthcoming Death Transformed My Life" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1441169922l/580305._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Lust & Wonder" rel="nofollow" href="https://www.goodreads.com/book/show/25663652-lust-wonder"><img alt="Lust & Wonder" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1444932277l/25663652._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Autobiography of Malcolm X" rel="nofollow" href="https://www.goodreads.com/book/show/92057.The_Autobiography_of_Malcolm_X"><img alt="The Autobiography of Malcolm X" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1434682864l/92057._SY75_.jpg" /></a></div>
'''

pattern = re.compile(r'_(SX|SY)\d+_.jpg')
# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Modify the a tags
for a_tag in soup.find_all('a'):
    title_original = a_tag.get('title', '')
    title_before_colon = title_original.split(':')[0].strip() if ':' in title_original else title_original.strip()
    # Remove apostrophes and other special characters before creating the slug
    slug = re.sub(r'[^\w\s-]', '', title_before_colon.lower())
    slug = re.sub(r'\s+', '-', slug)
    a_tag['href'] = f"/notes/{slug}"
    style = 'color: black; font-size: 10px;'
    img_tag = a_tag.img
    a_tag.clear()
    print(a_tag)
    print("="*80)
    a_tag.append(img_tag)
    a_tag.append(' ')
    a_tag.append(title_before_colon)
    a_tag['style'] = style

# Replace image size for all images
for img_tag in soup.find_all('img'):
    src = img_tag.get('src', '')
    # Replace the image size to make it larger
    img_tag['src'] = pattern.sub('_SX98_.jpg', src)

# Generate the formatted HTML output
formatted_html = ''
for div in soup.find_all('div', class_='gr_grid_book_container'):
    formatted_html += '    ' + str(div) + '\n'

# Get the path to notes.md
notes_md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_pages', 'notes.md')

# Check if we should automatically update the file
if os.path.exists(notes_md_path):
    print('\nGenerated HTML:\n')
    print(formatted_html)
    
    # auto_update = input('\nDo you want to automatically update notes.md? (y/n): ')
    auto_update = 'y'
    
    if auto_update.lower() == 'y':
        with open(notes_md_path, 'r') as file:
            content = file.read()
        
        # Find the container div and insert our new content at the beginning
        container_start = content.find('<div class="gr_grid_container">')
        if container_start != -1:
            container_start += len('<div class="gr_grid_container">\n')
            updated_content = content[:container_start] + formatted_html + content[container_start:]
            
            with open(notes_md_path, 'w') as file:
                file.write(updated_content)
            
            print('Successfully updated notes.md!')
        else:
            print('Could not find the grid container in notes.md. Manual update required.')
    else:
        print('\nPlease manually copy the HTML above to your notes.md file.')
else:
    print('\nGenerated HTML (notes.md not found for automatic update):\n')
    print(formatted_html)
# Print the modified HTML
print(soup)
