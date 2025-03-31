from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="我用中文做了场梦" rel="nofollow" href="https://www.goodreads.com/book/show/216363638"><img alt="我用中文做了场梦" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1720693359l/216363638._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Dry" rel="nofollow" href="https://www.goodreads.com/book/show/32370.Dry"><img alt="Dry" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442601868l/32370._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Never Split the Difference: Negotiating as if Your Life Depended on It" rel="nofollow" href="https://www.goodreads.com/book/show/123857637-never-split-the-difference"><img alt="Never Split the Difference: Negotiating as if Your Life Depended on It" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1680014152l/123857637._SY75_.jpg" /></a></div>
'''

pattern = re.compile(r'_(SX|SY)\d+_.jpg')
# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Modify the a tags
for a_tag in soup.find_all('a'):
    title_original = a_tag.get('title', '')
    title_before_colon = title_original.split(':')[0].strip() if ':' in title_original else title_original.strip()
    slug = re.sub(r'\s+', '-', title_before_colon.lower())
    a_tag['href'] = f"/notes/{slug}"
    style = 'color: black; font-size: 10px;'
    img_tag = a_tag.img
    a_tag.clear()
    print(a_tag)
    print("="*80)
    a_tag.append(img_tag)
    a_tag.append(' ')
    a_tag.append(slug)
    a_tag['style'] = style

for img_tag in soup.find_all('img'):
    # Change picture size
    img_tag['src'] = re.sub(pattern, '_SX98_.jpg', img_tag['src'])

# Print the modified HTML
print(soup)
