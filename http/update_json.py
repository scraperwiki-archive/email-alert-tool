import os
import sys
import json
import argparse

def open_json_and_convert_to_dictionary():
    if os.path.isfile('metadata1.json') == True:
        json_string = open('metadata1.json').read()
        json_out = json.loads(json_string)
        return json_out
    else: 
        print "No Json file found. Write one, and then maybe we'll think about sending you some email updates. Maybe"
        exit(1)

def update_json_file():
    config = {}
    config['table']="hello"
    json.dump(config, open("metadata1.json", "w"))


def main():
    update_json_file()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A tool for updating the configuration file used by the email-alert-tool")
    
    if len(sys.argv) == 5:
        main()
    else: 
        print 'Not enough arguments'
