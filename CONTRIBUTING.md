# How to contribute

Fork

## New features

1. Create a new branch from `develop`. That new branch's name must start with `feature_`
   
    `$ git checkout develop`
    
    `$ git checkout -b feature_name`

2. Always write (in english) a clear log messages for your commits. One line comments are prefered.
  
     `$ git commit -m "An english comment with a clear messaget about thtis commit`
     
3. Open a pull request using the Github web page
  
     `$ git commit -m "An english comment with a clear messaget abou thtis commit`
 
 3. Or if you are a repo member, you can merge `feature_` into `develop`.
     
     1. Merge with develop
       
        `$ git checkout develop`
     
        `$ git merge feature_name`
    
     2. Solve the conflits (if any).
     
     3. Delete the feature branch:
     
        `$ git branch -d feature_name`
     
     4. Push changes
