#Hawkathon 2017

import sqlite3

conn = sqlite3.connect('afflictionID.db')  # define connection
c = conn.cursor()  # start cursor



def create_table():
    """Create a table with specified number of columns"""
    c.execute('CREATE TABLE IF NOT EXISTS quickfix(species text, affliction text, immediate_Treatment text, long_term_treatment text)')
        

def data_entry():
    """reads data from text file"""
    file_data = [line.split('\t') for line in open('animal treatments.txt' , 'r').readlines()]
    c.executemany("INSERT INTO quickfix (species, affliction, immediate_Treatment, long_term_treatment) VALUES (?, ?, ?, ?);", file_data)
    conn.commit()
        

def read_from_db(animal):
    """pull data at column where species = animal"""
    try:
        c.execute('SELECT * FROM quickfix WHERE species = "{}"'.format(animal))  #populate cursor with value as tuple
        for row in c.fetchall():
            return row
    except:
        raise ValueError('{} is not a valid animal'.format(animal))


def main():
    
    create_table()

    data_entry()

    print(read_from_db("Snake"))
    
    c.close()
main()
