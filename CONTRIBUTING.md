## 1. Fork the repository (done only once)

## 2. Clone the forked repo (done only once)
Open a terminal and run the below commands in your desired directory
*Replace `USERNAME` with your username*
```
git clone https://github.com/USERNAME/congenial-spoon.git
cd congenial-spoon
```

## 3. Adding remote (done only once)
    
- Run the below command
        
    ```
    git remote -v
    ```

    Output would be
    ```
    origin https://github.com/USERNAME/Android-Development.git (fetch)```
    origin https://github.com/USERNAME/Android-Development.git (push)
    ```

    `origin` refers to the repository on your account

- Adding another remote
    
    ```
    git remote add rakesh https://github.com/RakeshSeervi/congenial-spoon.git
    ```

    `rakesh` would now refer to the repository to which you want to contribute to

## 4. Workflow (everytime you work on a new feature or fix a bug)

- **Sync it**
  
    Always keep your local copy of the repository updated with the original repository. 

    **Before making any changes and/or in an appropriate interval**, run the following commands carefully to update your local repository. 

    - Fetch all remote repositories and delete any deleted remote branches
        ```
        git fetch --all --prune
        ```
    - Switch to `main` branch
        ```
        git checkout main
        ```
    - Reset local `main` branch to match `rakesh` repository's `main` branch
        ```
        git reset --hard upstream/main
        ```
    - Push changes to your forked repository
        ```
        git push origin
        ```
        doing this keeps the main branch of your forked repository in sync with the original repository

- **Final steps**
  - Create a new branch
  
    **Everytime you work on a new feature or fix a bug**, please create seperate branch using the command and keep your main branch clean and most
stable version of your project (i.e. synced with remote branch). 

    Command to create and switch to a new branch

    *Replace `BRANCH_NAME` with a meaningful name*
    ```
    git checkout -b BRANCH_NAME
    ```
  - Make the desired changes 
    
    Follow the instructions in [README.md](<../main/README.md>) to set up and get the project running and then proceed with your changes
    
  - To add the changes to the branch
    ```
    git add .
    ```
    to add specific files
    ```
    git add file1 file2 ...
    ```

  - Commit your changes
    ```
    git commit -m 'relevant message'
    ```
  - Push your awesome work to your remote repository
    ```
    git push -u origin <BRANCH NAME>
    ```
  - Create a pull request
  
    Finally, go to your repository on github, switch to the desired branch and click on **compare and pull request**. 

    Then add a title and description to your pull request that explains your precious effort.
