import os
import json
import sqlite3

def open_json_and_convert_to_dictionary():
    if os.path.isfile('metadata.json') == false:
        json_file = open('filemeta.json')
        json_file = json.dumps(json_file)
        return json_file
    else: 
        print "No Json file found. Write one, and then maybe we'll think about sending you some email updates. Maybe"
        exit()

def get_current_count_in_sqlite():
    Connection = sqlite3.connect('scraperwiki.sqlite')
    Cursor = Connection.cursor()
    Count = Cursor.execute('SELECT count(*) FROM dumptruck')
    return Count

def compare_contents_of_file():
    json_file = open_json_and_convert_to_dictionary():

