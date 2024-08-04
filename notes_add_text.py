from bs4 import BeautifulSoup
import re

# Sample HTML input
html = '''
    <div class="gr_grid_book_container"><a title="Outlive: The Science and Art of Longevity" rel="nofollow" href="/notes/outlive"><img alt="Outlive: The Science and Art of Longevity" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1697230662l/199680637._SX50_SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="我的前半生：全本(九项奥斯卡金像奖电影《末代皇帝》原著，全本首次精装升级。本书以（灰皮本）为底本，国内众多名家匠心审阅修订，纠正以往版本二百三十六个错误知识点，唯一为自己做传的中国最后一位皇帝) (Chinese Edition)" rel="nofollow" href="/notes/我的前半生"><img alt="我的前半生：全本(九项奥斯卡金像奖电影《末代皇帝》原著，全本首次精装升级。本书以（灰皮本）为底本，国内众多名家匠心审阅修订，纠正以往版本二百三十六个错误知识点，唯一为自己做传的中国最后一位皇帝)" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1593075279l/54260356._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="许三观卖血记" rel="nofollow" href="/notes/许三观卖血记"><img alt="许三观卖血记" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451517651l/28404509._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="皮囊" rel="nofollow" href="/notes/皮囊"><img alt="皮囊" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1447789192l/27847873._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="一句顶一万句" rel="nofollow" href="/notes/一句顶一万句"><img alt="一句顶一万句" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1664127164l/19200550._SX50_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="How to Know a Person: The Art of Seeing Others Deeply and Being Deeply Seen" rel="nofollow" href="/notes/how-to-know-a-person"><img alt="How to Know a Person: The Art of Seeing Others Deeply and Being Deeply Seen" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1684815605l/112974860._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Kitchen Confidential: Adventures in the Culinary Underbelly" rel="nofollow" href="/notes/kitchen-confidential"><img alt="Kitchen Confidential: Adventures in the Culinary Underbelly" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1433739086l/33313._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Dictator's Handbook: Why Bad Behavior Is Almost Always Good Politics" rel="nofollow" href="/notes/the-dictatators-handbook"><img alt="The Dictator's Handbook: Why Bad Behavior Is Almost Always Good Politics" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1697577841l/200088563._SY75_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="The Sense of Style: The Thinking Person's Guide to Writing in the 21st Century" rel="nofollow" href="/notes/sense-of-style"><img alt="The Sense of Style: The Thinking Person's Guide to Writing in the 21st Century" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1396671354l/20821371._SX98_.jpg" /></a></div>
    <div class="gr_grid_book_container"><a title="Moonwalking with Einstein: The Art and Science of Remembering Everything" rel="nofollow" href="/notes/moonwalking-with-einstein"><img alt="Moonwalking with Einstein: The Art and Science of Remembering Everything" border="0" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630575238l/6346975._SX98_.jpg" /></a></div>

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
