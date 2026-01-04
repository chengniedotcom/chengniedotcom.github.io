import re
import os
from bs4 import BeautifulSoup


# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Private Revolutions: Four Women Face China's New Social Order" rel="nofollow" href="https://www.goodreads.com/book/show/200158232-private-revolutions"><img alt="Private Revolutions: Four Women Face China's New Social Order" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1711403676l/200158232._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Hands-On Large Language Models: Language Understanding and Generation" rel="nofollow" href="https://www.goodreads.com/book/show/210408850-hands-on-large-language-models"><img alt="Hands-On Large Language Models: Language Understanding and Generation" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1718922029l/210408850._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="大江大海：一九四九" rel="nofollow" href="https://www.goodreads.com/book/show/6902548"><img alt="大江大海：一九四九" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1253724411l/6902548._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Last Black Unicorn" rel="nofollow" href="https://www.goodreads.com/book/show/34974310-the-last-black-unicorn"><img alt="The Last Black Unicorn" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1508059685l/34974310._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Grief Is for People" rel="nofollow" href="https://www.goodreads.com/book/show/127282631-grief-is-for-people"><img alt="Grief Is for People" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1689777641l/127282631._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Last Words" rel="nofollow" href="https://www.goodreads.com/book/show/6713071-last-words"><img alt="Last Words" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442633404l/6713071._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Essentialism: The Disciplined Pursuit of Less" rel="nofollow" href="https://www.goodreads.com/book/show/19776547-essentialism"><img alt="Essentialism: The Disciplined Pursuit of Less" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1755208457l/19776547._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Rape of Nanking: The Forgotten Holocaust of World War II" rel="nofollow" href="https://www.goodreads.com/book/show/95784.The_Rape_of_Nanking"><img alt="The Rape of Nanking: The Forgotten Holocaust of World War II" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348687411l/95784._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Wu: The Chinese Empress Who Schemed, Seduced and Murdered Her Way to Become a Living God" rel="nofollow" href="https://www.goodreads.com/book/show/900793.Wu"><img alt="Wu: The Chinese Empress Who Schemed, Seduced and Murdered Her Way to Become a Living God" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1349045240l/900793._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Make Time: How to Focus on What Matters Every Day" rel="nofollow" href="https://www.goodreads.com/book/show/37880811-make-time"><img alt="Make Time: How to Focus on What Matters Every Day" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1524067121l/37880811._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="We Did Ok, Kid: A Memoir" rel="nofollow" href="https://www.goodreads.com/book/show/228676790-we-did-ok-kid"><img alt="We Did Ok, Kid: A Memoir" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1741022660l/228676790._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Running Ground: A Father, a Son, and the Simplest of Sports" rel="nofollow" href="https://www.goodreads.com/book/show/224082600-the-running-ground"><img alt="The Running Ground: A Father, a Son, and the Simplest of Sports" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1743475609l/224082600._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Empress Dowager Cixi: The Concubine Who Launched Modern China" rel="nofollow" href="https://www.goodreads.com/book/show/17857634-empress-dowager-cixi"><img alt="Empress Dowager Cixi: The Concubine Who Launched Modern China" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367929789l/17857634._SX50_.jpg" /></a></div>
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
