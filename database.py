#Functions for Reading, Writing and creating tables in database
import sqlite3
import time
import datetime


def connect():
    try:
        conn = sqlite3.connect("./HNPosts.db")
        return conn
    except:
        print("ERROR CONNECTING TO DATABASES")

def createTable(name):
    # The structure of the table is Rank, Title, Time
    try:
        conn = connect()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS scrape_%s (rank INTEGER, title TEXT, time );" % (name))
        conn.commit()
        return True
    except:
        return False

def write(name,data):
    #Data is list of lists where inner lists is rank, title, time
    try:
        conn = connect()
        c = conn.cursor()
        c.executemany("INSERT INTO scrape_%s (rank, title, time) VALUES(?,?,?);" % (name), data)
        conn.commit()
        return True
    except:
        return False

def read(name,rank):
    #Returns a row with rank rank
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM scrape_%s WHERE rank=?" % (name), tuple([rank]))
    rows = c.fetchall()
    return rows[0]

def tableExists(name):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scrape_%s';" % (name))
    x = c.fetchone()
    return x != None
