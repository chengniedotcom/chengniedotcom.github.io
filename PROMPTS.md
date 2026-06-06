2026_06_06
----------

> can you make sure that when I run marathon.py, the USA States Progress is also updated in the marathon.html?
> The USA progress map look ugly, can you give me a few options that look more realistic like a map of various states? I want to select the best
> Update and push the changes to main. 


2026_05_07
----------
> Update txt2md.py so that add the /notes/ link to the top of @~/Dropbox/public/chengniedotcom.github.io/CHANGELOG.md

> --- Checking for missing notes --- considered the version of notes.md before the update, but @/Users/chengnie/Library/CloudStorage/Dropbox/public/chengniedotcom.github.io/notes_add_text_filters.py updated the notes.md file as well. Can you update the python file so that checking missing notes is for the updated version of notes.md?

> @/Users/chengnie/Library/CloudStorage/Dropbox/public/chengniedotcom.github.io/notes_add_text_filters.py when retriving the titile tag like "女皇武则天 (易中天中华史 15) (Chinese Edition)", we should keep only the text before - and ( as the title, or else, the notes/ link would be too long. 

> For these three books. Can you follow the notes.md to add the information for them?

  ! dear-friend.md (Dear Friend - by Yiyun Li)
  ! fear-and-trembling.md (Fear and Trembling - by Søren Kierkegaard and Alastair Hannay)
  ! the-country-of-the-blind.md (The Country Of The Blind - by Andrew Leland)

> Deep Learning for Finance in the notes page shows the title in two lines. Can you reduce the gap between the two lines so that the text (title) of each book are compact. 

  > Update this  line-height: to 0.2 since I don't see the difference. 

> I use @/Users/chengnie/Library/CloudStorage/Dropbox/public/chengniedotcom.github.io/notes_add_text_filters.py to update the notes.md. However, I want update: 1) Some of the book titles are quite long. When it is long, I want to keep only the part of the title that is before any special characters like comma, hyphen, parenthesis and so on. so the notes/ link and the title displayed in notes.md should be the short version. 

>  are there some good visualization to show the 7 abott world marjor marathons and the time when running these          
  marathons? I have running time recorded in a tsv file. 

> Update @marathon.py 1) London runing time was updated; 2) include the update of world majors to marathon.html; 3) add a visualization of the full table to marathon.html

> commit the changes for all files and push to repository

> Study the first row of books in https://chengnie.com/notes/. Deep Learning for Finance has a big gap between the first line of Deep Learning for and the second row for Finance. Can you make these two lines close to each other for all books that need to wrap the text for long titles

>  is it possible to keep the title text to be on the same horizontal line for the same row of books? I know the cover  
  might have different height when we restrict them to be the same width. Please keep css and the python file updated   
  as well.

> how come there are some empty spaces in the notes page. And I want maybe a small gap between books so that not all    
  books are connected to each other 

> what happened to the filters for different years and ratings in previous versions in the notes page.  

2026_04_01
----------

> Update the website to remove the page views in all pages
> Update notes_add_text_filters.py and the site so that 1) after running notes_add_text_filters.py, it will add the books to new year like 2026; 2) it should have different years in a dropdown menu

> In Chinese blog like: @http://localhost:4000/cn/review2025/, When I click on Cn of the breadcrumb at the top "Home / Cn / 我的 2025 年度回顾", it has error. Can you fix it so that clicking on Cn (change it to CN) would lead to 中文博客@http://localhost:4000/cn/blog/。
> https://chengnie.com/notes/ does not show the book cover of "身后无一物“ but the local site http://localhost:4000/notes shows the book cover picture correcly. Fix it. 
> Filters of the mobile end for the notes page does not show the different years. Update and push the changes to main. 