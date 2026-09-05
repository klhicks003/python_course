### CSC-121 Python Programming Assignment Week 2

| Week | Learning | Link | Assignment Details |
|---|---|---|---|
| 2 | Git and GitHub | | First GitHub Push - repo scaffolding, branch -> PR -> merge cycle, `assignment/` folder and files added to the repo. |

<br><br><br>

## Week 2 - Getting the File System Ready

*No design doc applies yet.*

### Overview (from the client)
> "Let's make sure git and github are working correctly.
> We should branch, commit, push, PR, and merge. That's the workflow for every feature
> from here on."

### Plan - Business Requirements
- Documented repo structure before feature work starts
- Full branch -> PR -> merge cycle demonstrated once
- `main` stays clean - no direct commits
- Create a new folder at the root of the repo named "assignment"
- Create a file named `book_tracker.py` in assignment folder
- Create a file named `assignment_overview.md` in assignment folder
- Create a new folder under `assignment` called `design_docs`
- Create a file name `working_design.md` in assignment/design_docs


```
csc_121/
├── readme.md                 
├── license                   
├── pyproject.toml            
├── requirements.txt          
├── .vscode/                  
├── src/
├── tests/
... (add folder structure below to repo)
└── assignment/     
    ├── design_docs/
    │   └── working_design.md
    ├── assignment_overview.md
    ├── book_tracker.py
    └── ...                   
```

### Code
- Create a new branch called `assignment_setup`
- Make file/folder additions
- Add the files to staging (either through vscode or terminal)
- Create a commit message and commit changes
- Publish/push branch to GitHub


### Build - Pull Request (PR) Check on GitHub
- Create a PR on GitHub
- Check that the branch is seen and a PR is 

### Test - Manual
- [ ] Folders and files are seen in GitHub

### Deliverables
- [ ] GitHub link to PR
- [ ] All folders and files created and uploaded
- [ ] Update the root level readme.md to fix the git command error in the section Working through a module

---