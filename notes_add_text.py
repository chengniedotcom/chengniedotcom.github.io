from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Cognitive Behavioral Therapy Made Simple: 10 Strategies for Managing Anxiety, Depression, Anger, Panic, and Worry" rel="nofollow" href="/notes/cognitive-behavioral-hterapy-made-simple"><img alt="Cognitive Behavioral Therapy Made Simple: 10 Strategies for Managing Anxiety, Depression, Anger, Panic, and Worry" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546428492l/43440823._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="How to Be Perfect: The Correct Answer to Every Moral Question" rel="nofollow" href="/notes/how-to-be-perfect"><img alt="How to Be Perfect: The Correct Answer to Every Moral Question" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1642042986l/58484901._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Story of My Life" rel="nofollow" href="/notes/the-story-of-my-life"><img alt="The Story of My Life" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320429331l/821611._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Unbroken: A World War II Story of Survival, Resilience and Redemption" rel="nofollow" href="/notes/unbroken"><img alt="Unbroken: A World War II Story of Survival, Resilience and Redemption" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327861115l/8664353._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Friends, Lovers, and the Big Terrible Thing" rel="nofollow" href="/notes/friends-lovers-and-the-big-terrible-thing"><img alt="Friends, Lovers, and the Big Terrible Thing" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1699634140l/59641216._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Why Nations Fail: The Origins of Power, Prosperity, and Poverty" rel="nofollow" href="/notes/why-nations-fail"><img alt="Why Nations Fail: The Origins of Power, Prosperity, and Poverty" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348987396l/12158480._SY75_.jpg" /></a></div>
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
