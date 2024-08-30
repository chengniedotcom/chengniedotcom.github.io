from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="多谈谈问题：单读33" rel="nofollow" href="/notes/多谈谈问题"><img alt="多谈谈问题：单读33" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1690644936l/154010981._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Best Strangers in the World: Stories from a Life Spent Listening" rel="nofollow" href="/notes/the-best-strangers-in-the-world"><img alt="The Best Strangers in the World: Stories from a Life Spent Listening" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1675646603l/61357874._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="我在北京送快递" rel="nofollow" href="/notes/我在北京送快递"><img alt="我在北京送快递" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1681956009l/125918046._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Endure: Mind, Body, and the Curiously Elastic Limits of Human Performance" rel="nofollow" href="/notes/endure"><img alt="Endure: Mind, Body, and the Curiously Elastic Limits of Human Performance" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1533053130l/41014339._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="I Don't Want to Talk About It: Overcoming the Secret Legacy of Male Depression" rel="nofollow" href="/notes/i-dont-want-to-talk-about-it"><img alt="I Don't Want to Talk About It: Overcoming the Secret Legacy of Male Depression" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1424410383l/236765._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Infectious Generosity: The Ultimate Idea Worth Spreading" rel="nofollow" href="/notes/infectious-generosity"><img alt="Infectious Generosity: The Ultimate Idea Worth Spreading" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1697950377l/178332355._SY75_.jpg" /></a></div>

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
