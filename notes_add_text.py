from bs4 import BeautifulSoup

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="看见" rel="nofollow" href="/notes/看见"><img alt="看见" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408458884l/18458655._SX98_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Thinking In Systems: A Primer" rel="nofollow" href="/notes/thinking-in-systems"><img alt="Thinking In Systems: A Primer" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1390169859l/3828902._SX98_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Enlightenment now: The Case for Reason, Science, Humanism and Progress" rel="nofollow" href="/notes/enlightenment-now"><img alt="Enlightenment now: The Case for Reason, Science, Humanism and Progress" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1518557146l/38526454._SX98_.jpg" /></a></div>
'''

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

# Print the modified HTML
print(soup)
