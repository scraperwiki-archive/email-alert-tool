import os
import json
import sqlite3
import smtplib

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
    Count = Cursor.execute('SELECT count(*) FROM swdata')
    return Count

def compare_contents_of_file():
    json_file = open_json_and_convert_to_dictionary()
    Count = get_current_count_in_sqlite()
    if json_file['count'] < Count:
       send_report()
    else:
        exit()

def send_report():
    FROM_EMAIL = "noreply@scraperwiki.com"
    subject = "There are updated rows"
    json_file = open_json_and_convert()
    recipient = json_file['recipient']
    headers = [
       "From: " + FROM_USER,
       "Subject: " + subject,
       "To: " + recipient,
       "MIME-Version: 1.0",
       "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    server = smtplib.SMTP('localhost', 25)
    server.ehlo()
    server.sendmail(FROM_USER, recipient, headers + "\r\n\r\n" + body)
    server.close()

def main():
    get_current_count_in_sqlite()
    compare_contents_of_file

if __name__ == '__main__':
    main()
