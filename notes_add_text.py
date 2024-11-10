from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Age of Ambition: Chasing Fortune, Truth, and Faith in the New China" rel="nofollow" href="/notes/age-of-ambition"><img alt="Age of Ambition: Chasing Fortune, Truth, and Faith in the New China" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1418113377l/18490568._SX98_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="我还能看到多少次满月升起 (Chinese Edition)" rel="nofollow" href="/notes/我还能看到多少次满月升起"><img alt="我还能看到多少次满月升起" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1709646057l/209519263._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Vegetarian" rel="nofollow" href="/notes/the-vegetarian"><img alt="The Vegetarian" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1728661771l/25489025._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Memoirs of a Geisha" rel="nofollow" href="/notes/memoirs-of-a-geisha"><img alt="Memoirs of a Geisha" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1409595968l/929._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Build the Life You Want: The Art and Science of Getting Happier" rel="nofollow" href="/notes/build-the-life-you-want"><img alt="Build the Life You Want: The Art and Science of Getting Happier" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1692830209l/137978862._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="At the Edge of Empire: A Family's Reckoning with China" rel="nofollow" href="/notes/at-the-edge-of-empire"><img alt="At the Edge of Empire: A Family's Reckoning with China" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1705031856l/198137984._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="What If?: Serious Scientific Answers to Absurd Hypothetical Questions" rel="nofollow" href="/notes/what-if"><img alt="What If?: Serious Scientific Answers to Absurd Hypothetical Questions" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451351509l/21413662._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="李銳口述往事" rel="nofollow" href="/notes/李锐口述往事"><img alt="李銳口述往事" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1609682800l/56529025._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="A Simpler Life" rel="nofollow" href="/notes/a-simpler-life"><img alt="A Simpler Life" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639239014l/59692890._SX50_.jpg" /></a></div>
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
    print(a_tag)
    print("="*80)
    a_tag.append(img_tag)
    a_tag.append(' ')
    a_tag.append(text)
    a_tag['style'] = style

for img_tag in soup.find_all('img'):
    # Change picture size
    img_tag['src'] = re.sub(pattern, '_SX98_.jpg', img_tag['src'])


# Print the modified HTML
print(soup)
