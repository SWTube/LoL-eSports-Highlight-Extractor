# Summary
## Git Branch
master < release < develop < feature<br>
hotfix
### Naming Convention
`feature-text-recognition`

### When to Push to `develop`?
When `feature` is complete, then report to PM, then push/merge the branch.<br>
Other members should then pull `develop` and update their individual `feature` branches

## Commit Message
* categories
    * [add] -> added new features
    * [fix] -> fixed errors such as syntax errors
    * [new] -> created new file
    * [remove] -> removed file
    * [rollback] -> removed changes
```
[category] - [simple message]

[detailed description]
why committed?
what was the bug issue?
include url to the issue tracker if there is one
``` 

## Coding Review
Weekly. Done via GitHub.

# Git
## Installation
https://git-scm.com/

## Basic Commands

|Purpose|Command|
|---|---|
|Create repo|`git init`|
|Add `<file-name>` into repo|`git add <file-name>`|
|Propose changes to repo|`git commit`|
|Check repo status|`git status`|
|Add `<branch-name>` to repo|`git branch <branch-name>`|
|Change current branch|`git checkout <branch-name>`|
|Merge `<branch-name>`|`git merge <branch-name>`|
|Create new directory `<dir-name>`|`mkdir <dir-name>`|
|Print `<file-name>`|`cat <file-name>`|
|Print what's inside current directory|`ls`|
|Move to directory `<dir-name>`|`cd <dir-name>`|

example work flow
* Create branch
* Checkout to temporary branch
* Create / add files
* Edit files
* Commit edited files to repo
* Checkout to original master branch
* Merge temporary branch to master branch
* Create branch
* ...

Vim Commands

|Purpose|Current Mode|Command|
|---|---|---|
|insert mode (starting from current position)|normal|`i`|
|insert mode (starting from next line)|normal|`o`|
|insert mode (starting after a character)|normal|`a`|
|normal mode (from insert or command mode)|write, command|`esc`|
|command mode|normal|(from normal mode)`:`|
|save|command|`w`|
|exit|command|`q`|

### Git Bash Prompt Example
```
SWTube@SWTube ~/git_tutorial
$ git init
Initialized empty Git repository in c:/Users/SWTube/git_tutorial/.git/

SWTube@SWTube ~/git_tutorial (master)
$ vim hello.py
```

* hello.py (master)
```python
print("Hello World")
```

```
SWTube@SWTube ~/git_tutorial (master)
$ cat hello.py
print("Hello World")

SWTube@SWTube ~/git_tutorial (master)
$ python hello.py
Hello World

SWTube@SWTube ~/git_tutorial (master)
$ git status
On branch master

Initial commit

Untracked files:
    (use "git add <file>..." to include in what will be committed)

        hello.py

nothing added to commit but untracked files present (use "git add" to track)

SWTube@SWTube ~/git_tutorial (master)
$ git add hello.py

SWTube@SWTube ~/git_tutorial (master)
$ git status
On branch master

Initial commit

Changes to be committed:
    (use "git rm --cached <file>..." to unstage)

        new file:   hello.py

SWTube@SWTube ~/git_tutorial (master)
$ git commit
```

Default would be using vim editor to add commit message.<br>
Use `i` to get to insert mode, and `:wq` to save and exit.
For example: `create "hello world" program`

```
$ git commit
[master (root-commit) 4204f1c] create "hello world" program
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py

SWTube@SWTube ~/git_tutorial (master)
$ git branch
  master

SWTube@SWTube ~/git_tutorial (master)
$ git branch hotfix

SWTube@SWTube ~/git_tutorial (master)
$ git branch
  hotfix
  master

SWTube@SWTube ~/git_tutorial (master)
$ git checkout hotfix
Switched to branch hotfix

SWTube@SWTube ~/git_tutorial (hotfix)
$ ls
hello.py

SWTube@SWTube ~/git_tutorial (hotfix)
$ vim hello.py
```

* hello.py (hotfix)
```python
print("Hello World")
print("Tell Your World")
```

```
SWTube@SWTube ~/git_tutorial (hotfix)
$ cat hello.py
print("Hello World")
print("Tell Your World")

SWTube@SWTube ~/git_tutorial (hotfix)
$ python hello.py
Hello World
Tell Your World

SWTube@SWTube ~/git_tutorial (hotfix)
$ git status
On branch hotfix
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified    hello.py

no changes added to commit (use "git add" and/or "git commit -a")

SWTube@SWTube ~/git_tutorial (hotfix)
$ git commit -am "added output 'Tell Your World'"
[hotfix 13d3028] added output 'Tell Your World'|
 1 file changed, 1 insertion(+)

SWTube@SWTube ~/git_tutorial (hotfix)
$ git status
On branch hotfix
nothing to commit, working directory clean

SWTube@SWTube ~/git_tutorial (hotfix)
$ git checkout master
Switched to branch 'master'

SWTube@SWTube ~/git_tutorial (master)
$ git status
On branch master
nothing to commit, working directory clean

SWTube@SWTube ~/git_tutorial (master)
$ ls
hello.py

SWTube@SWTube ~/git_tutorial (master)
$ cat hello.py
print("Hello World")

SWTube@SWTube ~/git_tutorial (master)
$ python hello.py
Hello World

SWTube@SWTube ~/git_tutorial (master)
$ git merge hotfix
Updating 4204f1c..13d3028
Fast-forward
 hello.py | 1
 1 file changed, 1 insertion(+)

SWTube@SWTube ~/git_tutorial (master)
$ ls
hello.py

SWTube@SWTube ~/git_tutorial (master)
$ cat hello.py
print("Hello World")
print("Tell Your World")

SWTube@SWTube ~/git_tutorial (master)
$ python hello.py
Hello World
Tell Your World
```

* hello.py (master)
```python
print("Hello World")
print("Tell Your World")
print("Tell His World")
```

```
SWTube@SWTube ~/git_tutorial (master)
$ python hello.py
Hello World
Tell Your World
Tell His World

SWTube@SWTube ~/git_tutorial (master)
$ git commit
On branch master
Changes not staged for commit:
    modified    hello.py

SWTube@SWTube ~/git_tutorial (master)
$ git commit -am "added output 'Tell His World'"
...

SWTube@SWTube ~/git_tutorial (master)
$ git checkout hotfix
...

SWTube@SWTube ~/git_tutorial (hotfix)
$ vim hello.py
```

* hello.py (hotfix)
```python
print("Hello World")
print("Tell Your World")
print("Tell Her World")
```

```
SWTube@SWTube ~/git_tutorial (hotfix)
$ git commit -am "added output 'Tell Her World'"
...

SWTube@SWTube ~/git_tutorial (hotfix)
$ touch .gitignore

SWTube@SWTube ~/git_tutorial (hotfix)
$ ls
hello.py

SWTube@SWTube ~/git_tutorial (hotfix)
$ ls -a
./  .gitignore  hello.py
```

https://www.gitignore.io/ <br>
Search Operating Systems, IDEs, Programming Language
<br>**Windows, Pycharm, Python**

Copy the details into `.gitignore` file

```
SWTube@SWTube ~/git_tutorial (hotfix)
$ git add .gitignore

SWTube@SWTube ~/git_tutorial (hotfix)
$ git commit -m "added ',gitignore' file"
```

# GitHub Collaboration
## Collaboration Tools
### Issue Tracker
* Board, Forum
* Used to issue anything concerning to project such as report bugs, suggest improvements
* Format
    * In-charge: Person in-charge of issues
    * Notification: @<name> format can notify specific team/person
    * Label: categorizes issues
    * Commit Reference: links automatically to the commit when commit hash is given
    * Milestone: Sets markers to group issues

### Wiki
Uses markdown

### Pull Request
When user forks the repo, and wants to merge his forked version to the original repo, the user files a "Pull Request"

### Code Review
Click commits from repo, choose a commit, use comments to the commit to do code reviews.

## Collaboration Rules
### Commit Measure
* Every commit should have only one purpose and meaning. Purpose should remain unique even though multiple files are edited. This includes bug fixes and new function additions.
* Fixed one file but has two purposes are prohibited. Fixing bugs and adding new functions should be separated.

### Commit Message
https://wiki.openstack.org/wiki/GitCommitMessages
```
[category] - [simple message]

[detailed description]
why committed?
what was the bug issue?
include url to the issue tracker if there is one
``` 

ex)
```
[fix] - fixed syntax error

syntax error found in parser.py, line 341
included missing colon(:) after for controlling expression
```

```
  commit 3114a97ba188895daff4a3d337b2c73855d4632d
  Author: [removed]
  Date:   Mon Jun 11 17:16:10 2012 +0100

    Update default policies for KVM guest PIT & RTC timers

    The default policies for the KVM guest PIT and RTC timers
    are not very good at maintaining reliable time in guest
    operating systems. In particular Windows 7 guests will
    often crash with the default KVM timer policies, and old
    Linux guests will have very bad time drift

    Set the PIT such that missed ticks are injected at the
    normal rate, ie they are delayed

    Set the RTC such that missed ticks are injected at a
    higher rate to "catch up"

    This corresponds to the following libvirt XML

      <clock offset='utc'>
        <timer name='pit' tickpolicy='delay'/>
        <timer name='rtc' tickpolicy='catchup'/>
      </clock>

    And the following KVM options

      -no-kvm-pit-reinjection
      -rtc base=utc,driftfix=slew

    This should provide a default configuration that works
    acceptably for most OS types. In the future this will
    likely need to be made configurable per-guest OS type.

    Closes-Bug: #1011848

    Change-Id: Iafb0e2192b5f3c05b6395ffdfa14f86a98ce3d1f
```

### Branch Naming
* new - to add new features
* test - to test something (library / distribution environment / experiment / etc)
* bug - to fix bugs

ex)
```
new/feat-foo
new/feat-bar
bug/critical-thing
test/awesome-new-library
```

### Tag, Version Naming
https://semver.org/lang/ko/
* Version x.y.z
    * x is increased when changes doesn't have compatibility
    * y is increased when new features are added but still has compatibility
    * z is increased when bug fixes occur but still has compatibility

## Collaboration Workflow
### `git-flow`
Using "A successful Git branching model" by Vincent Driessen

* `develop` branch
* `feature` branch
* `release` branch
* `master` branch
* `hotfix` branch

#### `develop` branch
* Only one `develop` branch can exist.
* Every development starts in this branch
* But changes doesn't directly commit to `develop` branch
* Only `feature`, `release`, `hotfix` branches can merge

#### `feature` branch
* Various can exist
* Based on `develop` branch, new features / bug fixes occur
* Each branch has single feature / purpose

example workflow
* `development` branch init
* various `feature`s are being developed
* finished `feature`s are merged to `development

#### `release` branch
* Only bug fixes
    * bug fixes should of course be merged to both `develop` and `release`
* Only comes from `develop` branch

example workflow
* `development` branch init
* various `feature`s are being developed
* finished `feature`s are merged to `development
* first releasable `release` branch merged from `develop` branch
* meanwhile, new `feature`s are continuously being developed and merged

#### `master` branch
* Only related with `release` and `hotfix`
* Just like `develop` branch, only merge commit is possible

#### `hotfix` branch
* When released code need bug hotfix
* hotfix is directly merged to `develop` and `master`

#### Sum Up
* `develop` branch init
* `feature` branch init based on `develop`
* `feature` branches start developing new features
* once development is done, pull request / merge branch to `development`
* when release schedule comes, init `release` branch based on `develop` branch
* focus on fixing bugs in `release` branch, merge fixes to `develop`
* when release schedule arrives, init `master` branch based on `release` branch, and release the program
* init `hotfix` when bugs are found in `master` branch, the released version
* merge `hotfix` into `develop` and `master`
