import urllib2,cookielib
import random
import signal
import sys
from sys import argv
from bs4 import BeautifulSoup

USAGE = """Usage:
python s3knock.py wordlist term position
Example: python s3knock.py wordlist.txt tumblr 1
"""

class bcolors:
    public = '\033[92m'
    exists = '\033[93m'
    problem = '\033[91m'
    stop = '\033[0m'

discovered = []

def main(wordlist, base, position):
    with open(wordlist) as wordlist_file:
        lines = [line.rstrip('\n') for line in wordlist_file]
    
    for line in lines:
        if position == 1:
            site = "http://%s%s.s3.amazonaws.com/" %  (base, line)
        else:
            site = "https://%s%s.s3.amazonaws.com/" % (line, base)
    
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
            print bcolors.public + '[*] found : ' + site + " Public! " + bcolors.stop
            discovered.append(site)
        except urllib2.HTTPError, e:
            xml = e.fp.read()
            soup = BeautifulSoup(xml, features='xml')
            for q in soup.find_all('Error'):
                if q.find('Code').text != 'NoSuchBucket':
                    print bcolors.exists + '[*] found : ' + site + " " + q.find('Code').text + bcolors.stop
        except urllib2.URLError, e:
            print 'INFO: Invalid domain format. No DNS resolution.'
    
    print_summary()
    
def print_summary():
    print ""
    if not discovered:
        print "No public sites found!"
        return

    print "Summary of public sites found: "
    for s in discovered:
        print s

def signal_handler(signal, frame):
    print "\nCtrl+C detected. Exiting..."
    print_summary()
    sys.exit(0)

if __name__ == '__main__':
    if len(argv) < 4:
        print "ERROR: Not enough arguments given"
        print USAGE
        sys.exit(1)
    
    wordlist = argv[1]
    base = argv[2]
    
    try:
        position = int(argv[3])
    except ValueError as e:
        print "ERROR: position argument not a number"
        sys.exit(1)
    signal.signal(signal.SIGINT, signal_handler)
    main(wordlist, base, position)