from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="乡土中国" rel="nofollow" href="/notes/乡土中国"><img alt="乡土中国" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365606185l/17789435._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="為人民服務" rel="nofollow" href="/notes/为人民服务"><img alt="為人民服務" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1526265841l/40117150._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="情人" rel="nofollow" href="/notes/情人"><img alt="情人" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1566760739l/20319229._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="江村经济:中国农民的生活(博雅双语名家名作)(英汉对照)(图文版)" rel="nofollow" href="/notes/江村经济"><img alt="江村经济:中国农民的生活(博雅双语名家名作)(英汉对照)" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385086405l/18880682._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="王小波文集（全十卷）" rel="nofollow" href="/notes/王小波"><img alt="王小波文集（全十卷）" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1471818440l/31571755._SX50_.jpg" /></a></div>
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
