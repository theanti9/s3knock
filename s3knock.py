import urllib2,cookielib
import random
from sys import argv
from bs4 import BeautifulSoup

wordlist = argv[1]
base = str(argv[2])
position = argv[3]

lines = [line.rstrip('\n') for line in open(wordlist)]
length = len(lines)

class bcolors:
    public = '\033[92m'
    exists = '\033[93m'
    problem = '\033[91m'
    stop = '\033[0m'

for i in range(0, length):
    if position == '1':
        site = "http://" + base + lines[i] + ".s3.amazonaws.com/"
    else:
        site = "https://" + lines[i] + base + ".s3.amazonaws.com/"

    hdr1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}
    hdr2 = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.11 Chrome/23.0.1271.64 Safari/537.16',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}


    req = urllib2.Request(site, headers=random.choice([hdr1, hdr2]))

    try:
        page = urllib2.urlopen(req)
        xml = e.fp.read()
        soup = BeautifulSoup(xml, features='xml')
        print bcolors.public + '[*] found : ' + site + " Public! " + bcolors.stop
    except urllib2.HTTPError, e:
        xml = e.fp.read()
        soup = BeautifulSoup(xml, features='xml')
        for q in soup.find_all('Error'):
            if q.find('Code').text != 'NoSuchBucket':
                print bcolors.exists + '[*] found : ' + site + " " + q.find('Code').text + bcolors.stop
    except urllib2.URLError, e:
        print 'INFO: Invalid domain format. No DNS resolution.'

