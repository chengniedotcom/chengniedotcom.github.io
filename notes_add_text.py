from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''

    <div class="gr_grid_book_container"><a title="Yellowface" rel="nofollow" href="/notes/yellowface"><img alt="Yellowface" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671336608l/62047984._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Finding Me" rel="nofollow" href="/notes/finding-me"><img alt="Finding Me" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650842995l/58687126._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="晚年周恩來" rel="nofollow" href="/notes/晚年周恩来"><img alt="晚年周恩來" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1677916824l/5786795._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Private Life of Chairman Mao" rel="nofollow" href="/notes/the-private-life-of-chairman-mao"><img alt="The Private Life of Chairman Mao" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320537867l/775647._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Never Get Angry Again: The Foolproof Way to Stay Calm and in Control in Any Conversation or Situation" rel="nofollow" href="/notes/never-get-angry-again"><img alt="Never Get Angry Again: The Foolproof Way to Stay Calm and in Control in Any Conversation or Situation" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1499695975l/34964946._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Feel-Good Productivity: How to Do More of What Matters to You" rel="nofollow" href="/notes/feel-good-productivity"><img alt="Feel-Good Productivity: How to Do More of What Matters to You" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1689695229l/142402923._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="如何阅读一本书" rel="nofollow" href="/notes/如何阅读一本书"><img alt="如何阅读一本书" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381142523l/18632797._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Eat, Pray, Love" rel="nofollow" href="/notes/eat-pray-love"><img alt="Eat, Pray, Love" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1503066414l/19501._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Song of the Cell: An Exploration of Medicine and the New Human" rel="nofollow" href="/notes/the-song-of-the-cell"><img alt="The Song of the Cell: An Exploration of Medicine and the New Human" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1666198162l/60321392._SY75_.jpg" /></a></div>
            <div class="gr_grid_book_container"><a title="The Gifts of Imperfection" rel="nofollow" href="/notes/the-gift-of-imperfection"><img alt="The Gifts of Imperfection" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1369092544l/7015403._SX98_.jpg" /></a></div>

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
