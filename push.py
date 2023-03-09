#/bin/python3

# Purpuse to simulate CI/CD workflow in Git and ussing git and git-server
# Mark Snyder Juniper Networks msnyder@juniper.net
# dependencies python3 , git-core

#       Simulates a group of developers that are coding.  Files are writen and checked into a local git repo. 
#       File screation is also random with house keeping for cleanup to minimize too many files.
#       Contents of files are also randomized to emulate changes. 
#       Git brancehes are created
#       Git braches are randomaly checked out
#       Random branches resently checked out are merged upstream unless master

import os
import time
import random
userlist = ['Marcus', 'Harold', 'Nate', 'Mark', 'Teddy', 'Krystle', 'Jose']
branches = ['master','dev', 'test']
filenames = ['markdown.md', 'index.php', 'data.json']
jsonfake = ['key:pair','username:password', 'host:IP', 'file:data']
words =['house','red','horseshoe','snake','micro','cat','dog','barn','pink','seven','jake','alice','vault','crystal','boss','fluffy','alpha','beta','cup','glass','one','two','five','six']
message=['" typo "', '"changed font"', '"bug 534"', '"fixed error 404"', '"bad syntax"', '"fixed table"', '"wrong var called"', '"nightly build"']


def build():
    print('----Starting build function')
    buildusersandgroup()
    buildfiles()
    destroyfiles()
    
def buildusersandgroup():
    print('---Starting build user and groups function')
    cmd='sudo addgroup dev'
    os.system(cmd)
    for auser in ruser():
        cmd='sudo adduser '+ userlist
        os.system(cmd)

def buildfiles():
    print('----Starting buildfiles function')
    return

def gprint(gcmd):
    print('      Git command >>>> ',gcmd)

def buildbranch(branches):
    print('----Starting buildbranch fucntion')
    for branch in branches:
        gcmd='git branch '+ branch
        gprint(gcmd)
        os.system(gcmd)

    # needed for upstream git-server as branceh does not exist
    # git push --set-upstream origin test
    # git push --set-upstream origin dev

def whereaminow():
    print('---- Startig what branch am i im function. Current branch =', end = ' ')
    gcmd='git branch'
    gprint(gcmd)
    os.system(gcmd)
    print()

def whoami():
    print('----Starting what git user is active function.  User is = ')
    auser=random.choice(userlist)
    print('      ',auser)
    return(auser)

def whereshouldigo():
    print('----Starting changing branch function.  Branch will be changed to = ', end = ' ')
    branch=random.choice(branches)
    print('      ',branch)
    gcmd='git checkout '+ branch
    gprint(gcmd)
    os.system(gcmd)
    print()
    return(branch)

def branchmerges(branch):
    print('----Starting branch merge function. File changed for merge is = ', end = ' ')
    for filez in filenames:
        gadd(filez)
    commit()
    push()
    print('current branch >> ',branch)
    if branch == 'test': 
        for filez in filenames:
            gadd(filez)
        commit()
        push()
        gcmd='git checkout dev'
        gprint(gcmd)
        os.system(gcmd)
        for filez in filenames:
            gadd(filez)
        gcmd='git merge test -m '+ random.choice(message)
        gprint(gcmd)
        os.system(gcmd)

    if branch =='dev': 
        for filez in filenames:
            gadd(filez)
        commit()
        push()
        gcmd='git checkout master'
        gprint(gcmd)
        os.system(gcmd)
        for filez in filenames:
            gadd(filez)        
        print()
        gcmd='git merge dev -m '+ random.choice(message)
        gprint(gcmd)
        os.system(gcmd)
        print()

    if branch =='master':
        for filez in filenames:
            gadd(filez)
        commit()
        push()
        return(branch)

def fileopen(filename):
    print('----Starting opening and modifying files function. File being modified = ', filename)
    fh0=open(filename,'a')
    file=filename
    aword=random.choice(words)
    print("writing the word", aword, "to file ", filename ,"\n")
    fh0.write(aword+"\n")
    fh0.close() 
    return(file)   

def gadd(filename):
    print('----Starting git add function. Adding file = ', filename)
    file=filename
    gcmd='git add '+file
    gprint(gcmd+' only messages on error, so nothing is good')
    os.system(gcmd)
    print(':-)')
    print()
    return(file)

def commit():
    print('----Starting git commit function. File to be commited = ')
    amessage=random.choice(message)
    gcmd='git commit -m '+ amessage
    gprint(gcmd)
    os.system(gcmd)
    print()
    return[amessage]

def push():
    print('----Starting push function. ')
    gcmd='git push -f'
    gprint(gcmd)
    os.system(gcmd)
    print()

def deletenclean():
    # git reset --merge
    print('----Starting delete and clean function' )
    gcmd='git rm -r *'
    gprint(gcmd)
    os.system(gcmd)
    gcmd='git commit -m "delete-all"'
    gprint(gcmd)
    os.system(gcmd)
    push()
    for branch in branches:
        gcmd='git checkout '+ branch
        gprint(gcmd)
        os.system(gcmd)
        gcmd='git rm -r *'
        gprint(gcmd)
        os.system(gcmd)
        gcmd='git commit -m "delete-all"'
        gprint(gcmd)
        os.system(gcmd)
        push()
    print()

selection=input('select 1 for norm, 2 for clean')

if selection == '2'  :
    deletenclean()

if selection == '1'  :
    loop = 'y'
    while loop == 'y':
        #build()
        #buildbranch(branches)
        print()
        whereaminow()
        who=whoami()
        branch=whereshouldigo()
        print('Changing to branch >>',branch)

        if branch != 'master':
            #fileandamessage=commit(gadd(fileopen(random.choice(filenames))))
            filename=fileopen(random.choice(filenames))
            gadd(filename)
            commit()
            push()
            branchmerges(branch)
        if branch == 'master':
            #fileandamessage=commit(gadd(fileopen(random.choice(filenames))))
            filename=fileopen(random.choice(filenames))
            gadd(filename)
            commit()
            push()
if selection == '3'  :        
    gadd(fileopen(random.choice(filenames)))