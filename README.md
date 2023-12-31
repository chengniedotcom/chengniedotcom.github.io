# Github pages for chengnie.com. 

It's based on [Academic pages](https://github.com/academicpages/academicpages.github.io)

## Check to-update items

1. Tracked in Notion App and Apple Reminders. 

## Update Research

1. Change the status of each paper: add updated links, add review progress
2. Add new papers I had worked on


## Update Marathon map

1. Update marathon.tsv 
2. Run ``python marathon.py`` to update marathon/map.html
~~ 3. Update _pages/marathon.html by adding the new record of Marahon in the html table. Convert the tsv to html table using this [tool](https://wtools.io/convert-tsv-to-html-table) ~~
3. Update _pages/marathon.html by adding the new record of Marahon in the html table. marathon.py output the table in html format. 


## Update teaching

1. The survey in Canvas has the enrollment and response of each section for the evaluation
2. [PRR](ivy-prr.bus.iastate.edu) has the average GPA, then I don't have to calculate it manually as in the notes. 


## Update Notes

1. Retrieve books I read in this [link](https://www.goodreads.com/user/edit?format=html&tab=widgets#_=_). Select "Date Read" and "desc" to pick the most recently read books. For an older book, retrieve it from the local _notes_processed.html file. When adding a read book, remember to "Edit Activity" to 1) give the start and end time; 2) add this to my read list. 
    
    1. In case it does not work, I can manually edit a link. The picture link shows when I click on the book cover and open the cover picture in a new tab. 
    2. Paste the html section to notes_add_text.py and use only the books I haven't added yet. 
    3. Replace the href link with my summary links like /notes/乡土中国, so that the click would lead to my notes. 
    4. To add text and adjust the width of the book title, run notes_add_text.py
    5. Paste the output back to _pages/notes.md



## Update latest update date

1. Update _includes/footer.html


## Verfiy the updates before committing the changes to github

1. Preview markdown in vs code
2. Verify locally using ``bundle exec jekyll serve --trace``

```

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

