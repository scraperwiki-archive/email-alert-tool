import sqlite3
import random
import os

table_definition = "CREATE TABLE swdata (main TEXT)"

def create_file():
    file = open('scraperwiki.sqlite', 'w+')
    file.close()

def create_table_in_database():
    Connection = sqlite3.connect('scraperwiki.sqlite')
    Cursor = Connection.cursor()
    Cursor.execute(table_definition)
    Cursor.close()

def create_list_of_random_values():
    value_list = []
    for x in range(0, 100):
        value_list.append(str(random.random()))
    return value_list

def insert_random_values_into_database():
    value_list = create_list_of_random_values()
    for item in value_list:
        Connection = sqlite3.connect('scraperwiki.sqlite', isolation_level=None)
        Cursor = Connection.cursor()
        print item
        Cursor.execute("INSERT INTO swdata VALUES ( ?)", [item])
        #Cursor.commit()

def main():
    create_file()
    create_table_in_database()
    create_list_of_random_values()
    insert_random_values_into_database()

if __name__ == '__main__':
    main()
