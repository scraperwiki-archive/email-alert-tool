import requests
import os
import json
import sqlite3
import smtplib

def open_json_and_convert_to_dictionary():
    if os.path.isfile('metadata.json') == True:
        json_string = open('metadata.json').read()
        json_out = json.loads(json_string)
        return json_out
    else: 
        print "No Json file found. Write one, and then maybe we'll think about sending you some email updates. Maybe"
        exit(1)

def compare_contents_of_file():
    config = open_json_and_convert_to_dictionary()
    Count = get_count_from_endpoint()
    if config['count'] != Count:
       subject = 'Database Change'
       message = 'Some rows have been changed in your database.'
       send_report(subject, message)
    else:
       return
    config['count']=Count
    json.dump(config, open("metadata.json", "w"))

def get_count_from_endpoint():
    config_file = open_json_and_convert_to_dictionary()
    dataset = config_file['dataset']
    view = config_file['view']
    if dataset == None or view == None:
        print 'You must specify the SQL endpoint'
        exit()
    request = requests.get('https://premium.scraperwiki.com/%s/%s/sql/?q=select count(*) from swdata;' % (dataset, view))
    endpoint_json = request.json()
    endpoint_json = endpoint_json[0]
    endpoint_count = endpoint_json['count(*)']
    if endpoint_count == 0:
        print 'No fields were found'
        subject = "Your SQL endpoint is teh borked"
        message = "No rows were found in your endpoint"
        send_report(subject, message)
    return endpoint_count

def send_report(subject, message):
    FROM_USER = "noreply@scraperwiki.com"
    json_file = open_json_and_convert_to_dictionary()
    recipient = json_file['recipient']
    headers = [
       "From: " + FROM_USER,
       "Subject: " + subject,
       "To: " + recipient,
       "MIME-Version: 1.0",
       "Content-Type: text/html"]
    body = message
    headers = "\r\n".join(headers)
    server = smtplib.SMTP('localhost', 25)
    server.ehlo()
    server.sendmail(FROM_USER, recipient, headers + "\r\n\r\n" + body)
    server.close()

def main():
    compare_contents_of_file()

if __name__ == '__main__':
    main()
