from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''

    <div class="gr_grid_book_container"><a title="The Tender Bar: A Memoir" rel="nofollow" href="/notes/the-tender-bar"><img alt="The Tender Bar: A Memoir" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348917147l/144977._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Invention and Innovation: A Brief History of Hype and Failure" rel="nofollow" href="/notes/invention-and-innovation"><img alt="Invention and Innovation: A Brief History of Hype and Failure" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660590317l/61102803._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="罪与罚" rel="nofollow" href="/notes/罪与罚"><img alt="罪与罚" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659913308l/61892246._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Shoe Dog: A Memoir by the Creator of Nike" rel="nofollow" href="/notes/shoe-dog"><img alt="Shoe Dog: A Memoir by the Creator of Nike" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1457284880l/27220736._SX98_.jpg" /></a></div>
'''

pattern = re.compile(r'_(SX|SY)\d+_.jpg')
# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Modify the a tags
for a_tag in soup.find_all('a'):
    href = a_tag['href']
    text = href.replace('/notes/', '').replace('-', ' ').title()
    style = 'color: black; font-size: 10px;'
    img_tag = a_tag.img
    a_tag.clear()
    a_tag.append(img_tag)
    a_tag.append(' ')
    a_tag.append(text)
    a_tag['style'] = style

for img_tag in soup.find_all('img'):
    # Change picture size
    img_tag['src'] = re.sub(pattern, '_SX98_.jpg', img_tag['src'])


# Print the modified HTML
print(soup)
