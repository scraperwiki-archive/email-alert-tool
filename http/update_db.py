#!/usr/bin/env python

import sys
import scraperwiki

def update_db():
    scraperwiki.sqlite.save_var("recipient", sys.argv[1])
    scraperwiki.sqlite.save_var("url", sys.argv[2])
    scraperwiki.sqlite.save_var("tablename", sys.argv[3])

def main():
    update_db()

if __name__ == '__main__':
   if len(sys.argv) == 4:
       main()
   else: 
       print "Not enough arguments: email, url to SQL, tablename"
       exit() 
