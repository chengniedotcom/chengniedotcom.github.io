from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="奇特的一生" rel="nofollow" href="/notes/奇特的一生"><img alt="奇特的一生" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442383414l/26570751._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Woman in Me" rel="nofollow" href="/notes/the-woman-in-me"><img alt="The Woman in Me" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1697216267l/199661496._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Be Useful: Seven Tools for Life" rel="nofollow" href="/notes/be-useful"><img alt="Be Useful: Seven Tools for Life" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1685351182l/125063314._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Las Vegas Madam: The Escorts, The Clients, The Truth" rel="nofollow" href="/notes/the-las-vegas-madam"><img alt="The Las Vegas Madam: The Escorts, The Clients, The Truth" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1443924433l/26861308._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Beautiful World, Where Are You" rel="nofollow" href="/notes/beautiful-world-where-are-you"><img alt="Beautiful World, Where Are You" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1672783505l/75555793._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Ignorance: How it drives science" rel="nofollow" href="/notes/ignorance"><img alt="Ignorance: How it drives science" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1333421651l/13574594._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="SPIKE" rel="nofollow" href="/notes/spike"><img alt="SPIKE" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1634634955l/57971393._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Elon Musk" rel="nofollow" href="/notes/elon-musk"><img alt="Elon Musk" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1692288251l/122765395._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Coddling of the American Mind: How Good Intentions and Bad Ideas Are Setting Up a Generation for Failure" rel="nofollow" href="/notes/the-coddling-of-the-american-mind"><img alt="The Coddling of the American Mind: How Good Intentions and Bad Ideas Are Setting Up a Generation for Failure" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1513836885l/36556202._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Why Is Sex Fun? The Evolution of Human Sexuality (Science Masters)" rel="nofollow" href="/notes/why-is-sex-fun"><img alt="Why Is Sex Fun? The Evolution of Human Sexuality" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1431354333l/1991._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Guns, Germs, and Steel: The Fates of Human Societies" rel="nofollow" href="/notes/guns-germs-and-steel"><img alt="Guns, Germs, and Steel: The Fates of Human Societies" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1453215833l/1842._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="价值：我对投资的思考" rel="nofollow" href="/notes/价值"><img alt="价值：我对投资的思考" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1599406665l/55247953._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Lessons in Chemistry" rel="nofollow" href="/notes/lessons-in-chemistry"><img alt="Lessons in Chemistry" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1649650192l/58735074._SY75_.jpg" /></a> </div>
    <div class="gr_grid_book_container"><a title="Rationality" rel="nofollow" href="/notes/rationality"><img alt="Rationality" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1618510588l/56224080._SY75_.jpg" /></a> </div>
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
