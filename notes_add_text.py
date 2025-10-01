import re
import os
from bs4 import BeautifulSoup


# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Large Language Models Projects: Apply and Implement Strategies for Large Language Models" rel="nofollow" href="https://www.goodreads.com/book/show/214593430-large-language-models-projects"><img alt="Large Language Models Projects: Apply and Implement Strategies for Large Language Models" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1720584213l/214593430._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Memories, Dreams, Reflections" rel="nofollow" href="https://www.goodreads.com/book/show/612188.Memories_Dreams_Reflections"><img alt="Memories, Dreams, Reflections" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1751072457l/612188._SY75_.jpg" /></a></div>
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
