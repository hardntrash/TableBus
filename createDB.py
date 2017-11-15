#encoding=utf8
import sqlite3
import sys

reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('testDB.db')

c = conn.cursor()

c.execute('''CREATE TABLE busTable (id INTEGER PRIMARY KEY AUTOINCREMENT, numberBus INTEGER)''')

c.close()
conn.close()