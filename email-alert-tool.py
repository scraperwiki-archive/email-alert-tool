import os
import json
import sqlite3
import smtplib

def open_json_and_convert_to_dictionary():
    if os.path.isfile('metadata.json') == True:
        json_string = open('metadata.json').read()
        json_out = json.loads(json_string)
        print "Opening JSON file"
        return json_out
    else: 
        print "No Json file found. Write one, and then maybe we'll think about sending you some email updates. Maybe"
        exit()

def get_current_count_in_sqlite():
    Connection = sqlite3.connect('scraperwiki.sqlite')
    Cursor = Connection.cursor()
    Cursor.execute('SELECT count(*) FROM swdata')
    Count = Cursor.fetchone()
    return Count

def compare_contents_of_file():
    config = open_json_and_convert_to_dictionary()
    Count = get_current_count_in_sqlite()
    print config['count']
    print Count
    if config['count'] < Count:
       send_report()
    else:
        exit()

def send_report():
    FROM_USER = "noreply@scraperwiki.com"
    subject = "There are updated rows"
    json_file = open_json_and_convert_to_dictionary()
    recipient = json_file['recipient']
    headers = [
       "From: " + FROM_USER,
       "Subject: " + subject,
       "To: " + recipient,
       "MIME-Version: 1.0",
       "Content-Type: text/html"]
    body = "Please check your dataset"
    headers = "\r\n".join(headers)
    server = smtplib.SMTP('localhost', 25)
    server.ehlo()
    server.sendmail(FROM_USER, recipient, headers + "\r\n\r\n" + body)
    server.close()

def main():
    get_current_count_in_sqlite()
    compare_contents_of_file()

if __name__ == '__main__':
    main()
