# s3knock
Amazon S3 bucket name and permission discovery tool. 

Usage: python s3knock.py wordlist term position  
Example: python s3knock.py wordlist.txt tumblr 1

Position options are 1 or 2, where 1 is term[wordlist] and 2 is [wordlist]term 

Requirements: python, beautifulsoup4, lxml, urllib2, cookielib, random, sys
