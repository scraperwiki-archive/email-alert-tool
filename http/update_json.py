#!/usr/bin/env python

import os
import sys
import json
import argparse
import scraperwiki

def metadata_location():
    return "/home/tool/metadata.json"

def open_json_and_convert_to_dictionary():
    json_string = open(metadata_location()).read()
    return json.loads(json_string)

def update_json_file():
    config = open_json_and_convert_to_dictionary()
    _, config['recipient'], config['url'], config['tablename'] = sys.argv
    scraperwiki.sqlite.save_var("recipient", sys.argv[1])
    scraperwiki.sqlite.save_var("url", sys.argv[2])
    scraperwiki.sqlite.save_var("tablename", sys.argv[3])
    json.dump(config, open(metadata_location(), "w"))

def main():
    update_json_file()

if __name__ == '__main__':
   if len(sys.argv) == 4:
       print len(sys.argv)
       main()
   else: 
       print "Not enough arguments: email, url to SQL, tablename"
       exit() 
