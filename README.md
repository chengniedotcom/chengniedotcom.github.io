# Github pages for chengnie.com. 

It's based on [Academic pages](https://github.com/academicpages/academicpages.github.io)

## Check to-update items

1. Tracked in Notion App. 

## Update Research

1. Change the status of each paper: add updated link, add review progress
2. Add new papers I had worked on


## Update Marathon map

1. Update marathon.tsv 
2. Run marathonmap.py in python 3.8 environment to update marathonmap/map.html
3. Update _pages/marathonmap.html by adding the new record of Marahon in the html table. Convert the tsv to html table using this [tool](https://wtools.io/convert-tsv-to-html-table)


## Update teaching

1. The survey in Canvas has the enrollment and response of each section for the evaluation
2. Maybe future PRR has the average GPA, then I don't have to calculate it manually as in the notes. 


## Update Notes

1. Retrieve books I read in this [link](https://www.goodreads.com/user/edit?format=html&tab=widgets#_=_). Select "Date Read" and "desc" to pick the most recently read books. 
2. Paste the html section to _pages/notes.md and keep only books I haven't added yet. 
3. Replace the link with my summary links, so that the click would lead to my notes. 
4. I can use width of SX147(changed to SX98 on July 1, 2022) to adjust the width of the container and the cover picture


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