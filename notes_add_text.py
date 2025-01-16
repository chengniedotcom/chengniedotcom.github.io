from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Hillbilly Elegy: A Memoir of a Family and Culture in Crisis" rel="nofollow" href="/notes/hillbilly-elegy"><img alt="Hillbilly Elegy: A Memoir of a Family and Culture in Crisis" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1463569814l/27161156._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Know My Name" rel="nofollow" href="/notes/know-my-name"><img alt="Know My Name" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1567612158l/50196744._SX50_SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Coming Wave: Technology, Power, and the Twenty-first Century's Greatest Dilemma" rel="nofollow" href="/notes/the-coming-wave"><img alt="The Coming Wave: Technology, Power, and the Twenty-first Century's Greatest Dilemma" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1685351813l/90590134._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Open Book" rel="nofollow" href="/notes/open-book"><img alt="Open Book" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1575562439l/41571753._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Brain on Fire: My Month of Madness" rel="nofollow" href="/notes/brain-on-fire"><img alt="Brain on Fire: My Month of Madness" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1667594294l/63221207._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="From Darkness to Sight: A Journey from Hardship to Healing" rel="nofollow" href="/notes/from-darkness-to-sight"><img alt="From Darkness to Sight: A Journey from Hardship to Healing" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1450655219l/25834321._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="This is Going to Hurt: Secret Diaries of a Junior Doctor" rel="nofollow" href="/notes/this-is-going-to-hurt"><img alt="This is Going to Hurt: Secret Diaries of a Junior Doctor" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1498340278l/35510008._SY75_.jpg" /></a></div>
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
