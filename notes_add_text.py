from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''

    <div class="gr_grid_book_container"><a title="Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values (Phaedrus, #1)" rel="nofollow" href="/notes/zen"><img alt="Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1410136019l/629._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Long Story Short: The Only Storytelling Guide You'll Ever Need" rel="nofollow" href="/notes/long-story-short"><img alt="Long Story Short: The Only Storytelling Guide You'll Ever Need" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435219716l/25241947._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Mindreader: The New Science of Deciphering What People Really Think, What They Really Want, and Who They Really Are" rel="nofollow" href="/notes/mindreader"><img alt="Mindreader: The New Science of Deciphering What People Really Think, What They Really Want, and Who They Really Are" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654782809l/59900650._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="A Therapeutic Journey: Lessons from The School of Life" rel="nofollow" href="/notes/a-therapeutic-journey"><img alt="A Therapeutic Journey: Lessons from The School of Life" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1699484033l/176849725._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Normal People" rel="nofollow" href="/notes/normal-people"><img alt="Normal People" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571423190l/41057294._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Total Recall: My Unbelievably True Life Story" rel="nofollow" href="/notes/total-recall"><img alt="Total Recall: My Unbelievably True Life Story" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1344398356l/14546626._SX50_.jpg" /></a></div>

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
