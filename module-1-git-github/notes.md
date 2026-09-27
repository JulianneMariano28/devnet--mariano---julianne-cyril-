# Module 1 — Git & GitHub

**Student:** Julianne Cyril S. Mariano
**Date:** 09/27/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

A git is a tool that help you manage you code. It helps you keep track of changes made to files, especially when working on a projects involving codes. Meanwhile, GitHub is a platform or a website where Git repositories can be stored online. Inside these repositories, you can store and share your projects.

---

## Key vocabulary (in your own words)

- repository: A folder-like space that contains projects and keep tracks of its files and changes using Git commands.
- commit: A saved version of changes that includes a message describing what was changed.
- branch: A seperate version or a repository-like of a projects without directly affecting the main branch.
- push / pull: Push sends your commit and changes to the local repository, while Pull gets the latest or most current changes from the remote repository and updates the local repository.
- pull request: A request sends to add the changes from one branch to another.
- merge conflict: A conflict that happense when Git finds different changes made to the same part of a file and cannot automatically decide which changes to keep.
---

## Walking through what I did

First, I set up my Git username and email. Then, I connected my local repository to my GitHub repository. I also checked remote status. After that, I created a new branch named "julianne". After making some progress, I added my changes, checked their status, created a commit with a message, and push the changes to my branch. Lastly, I did pull request on GitHub.

```
git config --global user "CyrilMariano"
git confi --global user.email "juliannecyril28mariano@gmail.com"
git remote add origin "(repo url)"
git remote -v
git switch -c julianne
git add .
git status
git commit -m "Initial Commit"
git push -u origin julianne
```

---

## A mistake I made (or one I want to avoid)

A mistake that I want to avoid is overlooking which branch I am currently working on before making a commit. My commit changes could end up in a different places or may affect the main branch.

---

## How this connects to something else

Version control or working in GitHub and Git connects to group projects because different members work on the same project. We usually used GitHub to our projects or activies in our two subjects and I can say it is helpful in terms of collaboration and keeping things organized.
