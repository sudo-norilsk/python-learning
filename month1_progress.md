#first day

    for vs Press Ctrl+Shift+V to open a live preview pane

## Tasks
- [x] LINUX SETUP COMMANDS 
- [] GIT
- [] 
- []       
installation faze:


prikazy

    tree - to display file tree
    htop
    which
    code
    . == sources: runs all the commands in the .bashrc file as if you typed them right into your terminal.
    pip	Installs packages (like requests, flask)
    echo 'alias pyenv="source ~/python-projects/venv/bin/activate"' >> ~/.bashrc, 

        echo ... generates the text:

            alias pyenv="source ~/python-projects/venv/bin/activate"

        >> ~/.bashrc takes that text and adds it to the end of the .bashrc file.

python3-venv: 

    Used to create isolated virtual environments:

    A virtual environment is an isolated Python environment that has its own:

        Python interpreter,

        Installed packages (via pip),

        Scripts and dependencies.

        So anything you install in that environment won’t affect your system-wide Python or other projects.

            # Setup virtual environment

                python3 -m venv venv: creating

                source venv/bin/activate: to activate created alias sub

                deactivate: to leave

                
    
GPG 

    (GNU Privacy Guard) is a tool used for cryptographic signing, encryption, and verification. It uses public-key cryptography to ensure the authenticity and integrity of files or 
    packages. When a company (like Microsoft) distributes software, they also provide a GPG key to let users verify that the package is genuine and hasn’t been tampered with.

APT can read only binary 

    🧭 What are APT sources?
    APT (Advanced Package Tool) is the system Ubuntu/Debian uses to install, update, and remove software.
    APT gets its packages from a list of software sources, also called repositories.

.md 
    
    is the file extension for Markdown files.

GIT

    git config --global user.name "Your Name"
    git config --global user.email "your.email@gmail.com"
    git init = it will start track git
    git clone https://github.com/username/project.git = to clone

    3. Stage changes for commit
    Adds your changed files to the staging area:
        git add .
    (adds everything in the current directory)  
    Or:
        git add filename.py

    Essential Git Commands Cheat Sheet

    Setup & Config                                              Command	What it does
        
            git config --global user.name "Name"	            Set your Git username globally
            git config --global user.email "email@example.com"	Set your Git email globally
            git init	Initialize a new Git repository

    Working with Repos                                          Command	What it does
        
            git clone <repo-url>	                            Copy a remote repo to your local machine
            git status	                                        Show changed files, staged files, and branch
            git add <file>	                                    Stage changes to be committed
            git add .	                                        Stage all changes in current directory
            git commit -m "message"	                            Commit staged changes with a message
            git log	                                            Show commit history

    Branches & Switching                                        Command	What it does

            git branch	                                        List local branches
            git branch <branch-name>	                        Create a new branch
            git checkout <branch-name>	                        Switch to a different branch
            git checkout -b <branch-name>	                    Create and switch to a new branch
            git branch -M main	                                Rename current branch to main

    Remote Repos & Syncing                                      Command	What it does
   
            git remote add origin <url>	                        Link your local repo to a remote repo
            git push -u origin main	                            Push your commits to the remote main branch (sets upstream)
            git push	                                        Push committed changes to remote branch
            git pull origin main	                            Fetch and merge changes from remote main branch

    Undo & Reset                                                Command	What it does
    
            git reset <file>	                                Unstage a file (remove from staging area)
            git checkout -- <file>	                            Discard local changes in a file (restore last commit)
            git revert <commit>	                                Create a new commit that undoes a past commit

    Other Useful Commands                                       Command	What it does
  
            git diff	                                        Show changes between working directory and last commit
            git stash	                                        Temporarily save uncommitted changes
            git stash pop	                                    Reapply stashed changes
            git remote -v	                                    Show remote repo URLs
    

    Workflow

            git add tells Git what changes to save.

            git commit saves those changes locally with a message.

            git push shares those changes with others on the remote repo.


            git push	        Local → Remote      	Uploads your local commits to the remote repository (e.g., GitHub). This shares your changes with others.	After you commit changes and want to update the remote repo with your work.

            git pull	        Remote → Local	        Downloads changes from the remote repository and merges them into your current local branch.	To update your local repo with others’ changes from the remote.