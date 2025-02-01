from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="While Time Remains: A North Korean Defector's Search for Freedom in America" rel="nofollow" href="/notes/while-time-remains"><img alt="While Time Remains: A North Korean Defector's Search for Freedom in America" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1676499199l/61273331._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Anxious Generation: How the Great Rewiring of Childhood Caused an Epidemic of Mental Illness" rel="nofollow" href="/notes/the-anxious-generation"><img alt="The Anxious Generation: How the Great Rewiring of Childhood Caused an Epidemic of Mental Illness" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1711573377l/171681821._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Running with Scissors" rel="nofollow" href="/notes/running-with-scissors"><img alt="Running with Scissors" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1690319656l/242006._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Is Everyone Hanging Out Without Me? (And Other Concerns)" rel="nofollow" href="/notes/is-everyone-hanging-out-without-me"><img alt="Is Everyone Hanging Out Without Me?" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1443264638l/10335308._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Yes Please" rel="nofollow" href="/notes/yes-please"><img alt="Yes Please" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1402815435l/20910157._SY75_.jpg" /></a></div>
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
