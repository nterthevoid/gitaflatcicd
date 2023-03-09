# Purpuse to simulate CI/CD workflow in Git and ussing git and git-server

Work in progress ...


 Mark Snyder Juniper Networks msnyder@juniper.net
 dependencies python3 , git-core

       Simulates a group of developers that are coding.  Files are writen and checked into a local git repo. 
       File screation is also random with house keeping for cleanup to minimize too many files.
       Contents of files are also randomized to emulate changes. 
       Git brancehes are created
       Git braches are randomaly checked out
       Random branches resently checked out are merged upstream unless master
