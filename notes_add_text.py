from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="抑郁的力量" rel="nofollow" href="/notes/抑郁的力量"><img alt="抑郁的力量" border="0" src="https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png" /></a></div>
    <div class="gr_grid_book_container"><a title="世上为什么要有图书馆" rel="nofollow" href="/notes/世上为什么要有图书馆"><img alt="世上为什么要有图书馆" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1704607915l/204353687._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Source Code: My Beginnings" rel="nofollow" href="/notes/source-code"><img alt="Source Code: My Beginnings" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1719004398l/213034913._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Wild Swans: Three Daughters of China" rel="nofollow" href="/notes/wild-wwans"><img alt="Wild Swans: Three Daughters of China" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440643710l/1848._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="猫鱼" rel="nofollow" href="/notes/猫鱼"><img alt="猫鱼" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1720526527l/216105320._SY75_.jpg" /></a></div>
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
