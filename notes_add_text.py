from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="茶馆" rel="nofollow" href="/notes/茶馆"><img alt="茶馆" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1418521248l/23823879._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="知道分子" rel="nofollow" href="/notes/知道分子"><img alt="知道分子" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582771993l/33232097._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Liars' Club" rel="nofollow" href="/notes/liars-club"><img alt="The Liars' Club" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1499665766l/14241._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI" rel="nofollow" href="/notes/the-worlds-i-see"><img alt="The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1682738725l/144405196._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="万箭穿心" rel="nofollow" href="/notes/万箭穿心"><img alt="万箭穿心" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1498711160l/35535004._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="六個說謊的大學生" rel="nofollow" href="/notes/六个说谎的大学生"><img alt="六個說謊的大學生" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650611803l/60860351._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="一百年，许多人，许多事：杨苡口述自传" rel="nofollow" href="/notes/一百年"><img alt="一百年，许多人，许多事：杨苡口述自传" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1674822624l/87636035._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Nexus: A Brief History of Information Networks from the Stone Age to AI" rel="nofollow" href="/notes/nexus"><img alt="Nexus: A Brief History of Information Networks from the Stone Age to AI" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1709986452l/204927599._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="How To: Absurd Scientific Advice for Common Real-World Problems" rel="nofollow" href="/notes/how-to"><img alt="How To: Absurd Scientific Advice for Common Real-World Problems" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1550145086l/43852758._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Wild: From Lost to Found on the Pacific Crest Trail" rel="nofollow" href="/notes/wild"><img alt="Wild: From Lost to Found on the Pacific Crest Trail" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1453189881l/12262741._SY75_.jpg" /></a></div>

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
