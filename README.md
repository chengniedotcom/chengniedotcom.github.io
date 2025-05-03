# Github pages for chengnie.com. 

It's based on [Academic pages](https://github.com/academicpages/academicpages.github.io)

## Check to-update items

1. Tracked in Apple Reminders. 
2. Keep changes in UPDATES.md

## Update Research

1. Change the status of each paper: add updated links, add review progress
2. Add new papers I had worked on
3. Update ORCID
4. Google Scholar
5. Iowa State Page through PRR


## Update teaching

1. The survey in Canvas has the enrollment and response of each section for the evaluation
2. [PRR](https://ivy-prr.bus.iastate.edu/update/login?return=true&) has the average GPA, then I don't have to calculate it manually as in the notes. 

## Duplicate Research and Teaching into the about.md pace

1. It is easier to view everything on this single about me page. 
2. Now the _includes/research-include.html and _includes/teaching-include.html are used to incorparte research and teaching into the about.md page. 


## Update Notes

1. Retrieve books I read in this [link](https://www.goodreads.com/user/edit?format=html&tab=widgets#_=_). Select "Date Read" and "desc" to pick the most recently read books. For an older book, retrieve it from the local _notes_processed.html file. When adding a read book, remember to "Edit Activity" to 1) give the start and end time; 2) add this to my read list. 
    
    1. In case it does not work, I can manually edit a link:  a) the book link shows when I visit the book in goodreads; b) The picture link shows when I click on the book cover and open the cover picture in a new tab.
    2. Paste the html section to notes_add_text.py and use only the books I haven't added yet. 
    3. For books not in goodreads, I can use "抑郁的力量" as a template. I need to download the cover pictures myself. 
    <!-- 4. Paste the output back to _pages/notes.md -->
    <!-- 3. Replace the href link with my summary links like /notes/乡土中国, so that the click would lead to my notes. 
    4. To add text and adjust the width of the book title, run notes_add_text.py -->


## Update Marathon map

1. Update marathon.tsv 
2. Run ``python marathon.py`` to update marathon/map.html automatically
~~ 3. Update _pages/marathon.html by adding the new record of Marahon in the html table. Convert the tsv to html table using this [tool](https://wtools.io/convert-tsv-to-html-table) ~~
<!-- 3. Update _pages/marathon.html by adding the new record of Marahon in the html table. marathon.py output the table in html format.  -->


## Some special considerations


1. Remove "$" in notes so that they won't be interpreted as math fonts. 




## Update latest update date

<!-- 1. Update _includes/footer.html -->


## Verfiy the updates before committing the changes to github

1. Preview markdown in vs code
2. Verify locally using ``bundle exec jekyll serve --trace``

```

    # Method 2024_05_06 (replicate the same process on macm1 on 2024_06_19 in China):
    github copilot account and github personal account cannot co-exist in vs code. Therefore, I log into school copilot account in vs code and github ssh to commit the changes in iMac. 
    - set up ssh to github using chengniedotcom account. 
        - pbcopy < ~/.ssh/id_rsa.pub
        - paste it to github.com -> Settings -> Add SSH key -> paste the key
        - Verify it works in terminal: ssh -T git@github.com
        - Update the repo from HTTPS to SSH: git remote set-url origin git@github.com:chengniedotcom/chengniedotcom.github.io.git
        - git remote -v
        - git branch. It looks that I did not have dev branch. That is OK since things are backuped in Dropbox. 
        - git commit -m "2024_05_06 update"
            - Because I had conflicted changes (added pptx in web interface, then update the local repo. I need to merge the changes) git pull --no-rebase origin master
            - Also for merge: git pull origin master

        - git status
        - git add --all
        - git commit -m """
        - git push origin master

    # Method 1: in vs code. No need for the dev branch. 
    Commit the change with Source Control view
    Git: Push
    # Method 2: or in terminal
    cd '/Users/chengnie/Dropbox/public/chengniedotcom.github.io'
    bundle exec jekyll serve --trace
    git status
    git add --all
    git commit -m """
    git checkout master
    git merge dev
    git push
    git checkout dev

```

# History

Updates tracked in (UPDATES.md)[/UPDATES.md]

