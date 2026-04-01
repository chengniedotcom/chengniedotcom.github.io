## Someday maybe
x Add a sort function based on ranking in the book notes page
x Add the views count of different blog posts.
  > how to add a pageview count like in https://www.behind-the-enemy-lines.com/2026/03/taste-is-not-enough-reality-or-bust.html or for individual pages in the github pages?
  x setup hits.seeyoufarm.com
- selfish-gene.md went through a few lines
x disable showing the research and teaching tab since they are in front page
- Add social media tab
- 申请weibo 还有X账号
- link run.chengnie.com to cnie.us
- Upload and use Panos' idea to let github web, claude web take over
- ```Can you check the directory to see if the file names are correct. I used UPDATES.md as changelog. Can you suggest which file names I should change?```
- ```Can you suggest where I keep track of my prompts?```
- ```Compare my edited version with the origianl version and compile and update my writing style as a skill file```
- link check, picture check throughout the website. 
- Remove you may also enjoy section at the end. 
- Beautify the mobile site. 

# 2026

## Next

TODO- get a Chinese version toggle
- Remame files for usual pattern: CHANGELOG instead of update. Ask Claude
- load with Claude Web
- Streamline some other process (like loading notes and checking consistency)

/notes/beautiful-country
/notes/shot-ready
/notes/the-country-of-the-blind
/notes/sociopath
/notes/everything-is-tuberculosis
/notes/在难搞的日子笑出声来
/notes/the-house-of-my-mother
/notes/九诗心
/notes/the-book-of-sheen
/notes/要有光
/notes/dont-believe-everything-you-think
/notes/dear-friend
/notes/things-in-nature-merely-grow
/notes/陆犯焉识
/notes/房思琪的初恋乐园
/notes/美国华人史

English translation of some chinese posts. 


```
Is it possible to use python and goodreads API to retrieve the books I read, along with their ratings and other metadata, and then automatically update the notes.md file on my GitHub pages site following these steps that I used manullay?

1. Retrieve books I read in this [link](https://www.goodreads.com/user/edit?format=html&tab=widgets#_=_). Select "Date Read" and "desc" to pick the most recently read books. 
2. Paste the html section to notes_add_text.py and use only the books I haven't added yet. 
3. To add text and adjust the width of the book title, run notes_add_text.py -->
4. just run python notes_add_filters.py to update the data attributes.
```


## 2026_01_15: testing claude 
- import https://cnie.us/%E4%B8%BA%E4%BB%80%E4%B9%88

```

The Notes page has many books. I hope to offer a few buttons to display a subset of books:
- like books read in different years
- Highly recommended books (rated 9 or above by me)

TODO
- translate some of the posts
- some of the Chinese version I already have in my 公众号
_posts/en/2024-01-07-gww2023.md
_posts/en/2024-06-19-jiangnan2024.md
_posts/en/2025-01-01-letter2003.md

  1. English posts WITHOUT Chinese version (14 posts)
  ┌────────────┬───────────────────┬───────────────────────┐
  │    Date    │       File        │         Title         │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2021-12-31 │ review2021.md     │ My 2021 Annual Review │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2022-05-04 │ boston2022.md     │ Boston Marathon 2022  │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2022-12-11 │ talk.md           │ Talk                  │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2022-12-31 │ review2022.md     │ My 2022 Annual Review │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2023-01-23 │ maui2023.md       │ Maui 2023             │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2023-02-03 │ student-letter.md │ Student Letter        │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2023-03-03 │ moon-heart.md     │ Moon Heart            │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2023-04-20 │ boston2023.md     │ Boston Marathon 2023  │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2023-12-31 │ review2023.md     │ My 2023 Annual Review │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2024-08-30 │ how-do-i-read.md  │ How Do I Read         │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2024-09-08 │ mantra.md         │ Mantra                │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2025-01-16 │ review2024.md     │ My 2024 Annual Review │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2025-02-01 │ why-do-i-run.md   │ Why Do I Run          │
  ├────────────┼───────────────────┼───────────────────────┤
  │ 2025-10-06 │ web2025.md        │ Web 2025              │
  └────────────┴───────────────────┴───────────────────────┘
  我如何阅读
  我的座右铭
  我为什么跑步
  > The why-do-i-run.md post is translated to Chinses in https://mp.weixin.qq.com/s/nYzqDGexOwOHVvhKTH3l6g. Create a Chinese post @cn-why-do-i-run.md to pair with the English post based on the translated version. The post html is saved in @_wechat folder.
  > Can you do the same for two other posts? Their Chinese hmtl are saved in @_wechat folder. mantra.md and @how-do-i-read.md. Remember to keep the pictures in the Chinse post that I may not used in the English post. Also insert the link at the correct place following the English posts' style. 
  - where do claude save the picutres from the post?. files/pics folder. 
  - > Create an English and an Chinse blog post for @_wechat/我的2017：从5千米到马拉松.html. 

  2. Chinese posts WITHOUT English version (5 posts)
  ┌────────────┬──────────────────────┬────────────────┐
  │    Date    │         File         │     Title      │
  ├────────────┼──────────────────────┼────────────────┤
  │ 2020-09-12 │ cn-highschool2020.md │ 时光倒流二十年 │
  ├────────────┼──────────────────────┼────────────────┤
  │ 2023-10-11 │ cn-hust2023.md       │ HUST 2023      │
  ├────────────┼──────────────────────┼────────────────┤
  │ 2024-01-07 │ cn-gww2023.md        │ GWW 2023       │
  ├────────────┼──────────────────────┼────────────────┤
  │ 2024-06-19 │ cn-jiangnan2024.md   │ 江南 2024      │
  ├────────────┼──────────────────────┼────────────────┤
  │ 2025-01-01 │ cn-letter2003.md     │ Letter 2003    │
  └────────────┴──────────────────────┴────────────────┘
  Posts with both versions (3 posts):
  - why-write (2021-12-08)
  - chicago2025 (2025-10-18)
  - review2025 (2026-01-04)


```


```

Can you tranlsate shot-ready.md to Chinese for me? and Place the translated version to @'/Users/chengnie/Dropbox/5_creative/1_posts/cn_shot_ready.md. 

ultrathink
```
TODO: 身后无遗物 身后无遗物 cover not showing properly
TODO: add voice narration for some notes like this one: https://staycuriousmetabolism.substack.com/p/the-carb-loading-myth-is-finally?utm_source=podcast-email%2Csubstack&publication_id=2682303&post_id=182588963&utm_campaign=email-play-on-substack&utm_medium=email&r=fhcuy&triedRedirect=true
TODO: Home/ Cn/记一次吵架, click on cn is problematic
TODO: maybe add a toggle to switch between English and Chinese for notes that have both versions.
```


# 2025

## 2026_01_04

/notes/empress-dowager-cixi
/notes/the-running-ground
/notes/we-did-ok-kid
/notes/make-time
/notes/wu
/notes/the-rape-of-nanking
/notes/essentialism
/notes/last-words
/notes/grief-is-for-people
/notes/大江大海1949
/notes/the-last-black-unicorn
/notes/private-revolutions
/notes/hands-on-large-language-models

Kansas city marathon
Rocket city marathon

Teaching eval for 2025 summer, update in prr, and chengnie.com

Jiana paper submit to DSS


Crime Dynamics of Home-Sharing: Disentangling Temporal Effects and Policy Interventions
  by Jiana Meng; He Li; Cheng Nie; Chen Zhang


## 2025_10_31

Chicago Marathon 2025
Silver Comet Marathon 2025

/notes/the-year-of-magical-thinking
/notes/plato-and-a-platypus-walk-into-a-bar
/notes/never-finished
/notes/i-know-why-the-caged-bird-sings

add missing ones
/notes/magical-thinking
/notes/lust-and-wonder

identified not included txt files into notes.md



## 2025_10_06

The old notes page (with the grid layout of book covers) has been backed up as notes-old-backup.md in case you want to reference it later. The new organized page should now be live at /notes/ with a cleaner, more readable list format similar to your blog section.




## 2025_09_30
/notes/memories-dreams-reflections


## 2025_09_02


/notes/the-end-of-burnout
Add Marathon USA states map progess

## 2025_08_18

/notes/me-talk-pretty-one-day
/notes/mao
/notes/no-time-to-spare
/notes/sound-of-gravel
/notes/the-diary-of-a-young-girl



## 2025_06_01 
/notes/the-autobiography-of-malcolm-x
/notes/lust-and-wonder
/notes/chasing-daylight
/notes/never-enough
/notes/meditations-for-mortals


## 2025_05_01
/notes/the-molecule-of-more
/notes/mamas-boy
/notes/身后无遗物
/notes/the-third-gilmore-girl
/notes/the-next-day

Marathon
Garmin Marathon
update the layout of the blog page

## 2025_04_01

/notes/never-split-the-difference
/notes/dry
/notes/我用中文做了场梦

ISR zillow update from forthcoming to 2024 and page numbers

## 2025_03_02

/notes/猫鱼
/notes/wild-swans
/notes/source-code
/notes/世上为什么要有图书馆
/notes/抑郁的力量
/notes/我的母亲做保洁


/notes/抑郁的力量 showed my own saved picture and goodreads link (I submitted following perplexity's instructions)


## 2025_02_01

/notes/yes-please
/notes/is-everyone-hanging-out-without-me
/notes/running-with-scissors
/notes/the-anxious-generation
/notes/while-time-remains

Blog: why-do-i-run
Marathon tables add num
set read_time: false in _config.yml to disable the read time. 



## 2025_01_16

/notes/this-is-going-to-hurt
/notes/brain-on-fire
/notes/from-darkness-to-sight
/notes/open-book
/notes/know-my-name
/notes/hillbilly-elegy
/notes/the-coming-wave

Xiamen Marathon. (about, certificate, table)
那年的情书
New year summary
Teaching of Fall 2024

# 2024

## 2024_12_08
/notes/why-nations-fail
/notes/friends-lovers-and-the-big-terrible-thing
/notes/unbroken
/notes/the-story-of-my-life
/notes/how-to-be-perfect
/notes/cognitive-behavioral-hterapy-made-simple

Research
Submitted MS with Vijay Mookerjee
Rejected MS with Wei Chen
Round 2 with Bin Fang JAIS

## 2024_11_08
/notes/a-simpler-life
/notes/李锐口述往事
/notes/what-if
/notes/at-the-edge-of-empire
/notes/build-the-life-you-want
/notes/memoirs-of-a-geisha
/notes/the-vegetarian
/notes/我还能看到多少次满月升起

Old repo
/notes/age-of-ambition

Research 
Update paper title with Mingwen

## 2024_10_04
/notes/wild
/notes/how-to
/notes/一百年
/notes/nexus
/notes/六个说谎的大学生
/notes/万箭穿心
/notes/liars-club
/notes/the-worlds-i-see
/notes/知道分子
/notes/茶馆

Jiana paper submission
MISQ hotel strategy revising

Berlin Marathon

## 2024_09_10
Need to explain Annica, Sankara are my summary of the Vipassana Meditation. 
Adjust the NFT submission journal

## 2024_09_08
/blog/mantra
put Chen Wei's paper to top of the working paper list
update 江南创业史, picutres misplaced 

## 2024_09_04
Add the management science submission

## 2024_08_30

/notes/infectious-generosity
/notes/i-dont-want-to-talk-about-it
/notes/endure
/notes/我在北京送快递
/notes/the-best-strangers-in-the-world
/notes/多谈谈问题

Blog
2024_08_15_how_i_read

## 2024_08_04

Notes

/notes/the-dictatators-handbook
/notes/kitchen-confidential
/notes/how-to-know-a-person
/notes/一句顶一万句
/notes/皮囊
/notes/许三观卖血记
/notes/我的前半生
/notes/outlive
/notes/moonwalking-with-einstein
/notes/sense-of-style

Teaching

- 2024 spring

Marathon map 

- add WI

CV

## 2024_05 to 2024_06_19

Profile:
Add ORCID

Research:
Adjust working papers and papers under review. 

Blog:
江南创业史


## April & May

- 2024_05_06

### General

- Get research Teaching into the About page directly
- Update my profile picture taken: GOLD8617.jpg. Add my domain. Ask friends. 
- Get the blog and notes link below profile picture. 
    - Through "flickr" search in the directory, I found the places to update blog and notes into the profile page: 
        - author-profile.html
        - _config.yml
        - _utilities.scss
        - _variables.scss

### About

- associate professor

### Research

- DSS accepted
- Add Jiana Meng's MISQ submission
- Delete (2024) for working papers
- Delete conference papers and presentation. 
- update the volumne: 4\. Nie C, Zheng Z (Eric), Sarkar S (2024). [Firm Competitive Structure and Consumer Reaction in Search Advertising.](https://doi.org/10.17705/1jais.00835) _Journal of the Association for Information Systems_, (25:2), 442–462.
- Remember to add the big12 presentation slides. 2024big12.pptx. I uploaded from the web interface. 

### note

- /notes/罪与罚
- /notes/invention-and-innovation
- /notes/shoe-dog
- /notes/the-tender-bar


## Mar 17


1. update link for the 2024 link for JAIS paper. 
2. update notes for books. 

    2024 Feb
    /notes/eat-pray-love
    /notes/如何阅读一本书
    /notes/the-song-of-the-cell
    /notes/feel-good-productivity
    /notes/never-get-angry-again
    /notes/the-private-life-of-chairman-mao
    /notes/晚年周恩来
    /notes/finding-me
    /notes/yellowface
    /notes/the-gift-of-imperfection
3. update marathon to add tokyo marathon 2024