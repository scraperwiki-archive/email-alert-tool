#!/usr/bin/env python

import os
import sys
import json
import argparse
import scraperwiki

def open_json_and_convert_to_dictionary():
    if os.path.isfile('metadata1.json') == True:
        json_string = open('metadata1.json').read()
        json_out = json.loads(json_string)
        return json_out
    else: 
        print "No Json file found. Write one, and then maybe we'll think about sending you some email updates. Maybe"
        exit(1)

def update_json_file():
    config = open_json_and_convert_to_dictionary()
    config['recipient'] = sys.argv[1]
    scraperwiki.sqlite.save_var("recipient", sys.argv[1])
    config['url'] = sys.argv[2]
    scraperwiki.sqlite.save_var("url", sys.argv[2])
    config['tablename'] = sys.argv[3]
    scraperwiki.sqlite.save_var("tablename", sys.argv[3])
    json.dump(config, open("metadata1.json", "w"))


def main():
    update_json_file()

if __name__ == '__main__':
   if len(sys.argv) == 4:
       main()
   else: 
       "Not enough arguments."
       exit() 
