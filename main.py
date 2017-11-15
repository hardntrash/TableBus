# encoding=utf8
import sqlite3
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('testDB.db')
c = conn.cursor()

c.execute('PRAGMA TABLE_INFO (busTable)')
columns = c.fetchall()
bus_stops = []
k = 2
while k != columns.__len__():
    bus_stops.append(columns[k][1])
    k += 1


def add_stop():
    name_stop = raw_input("Название остановки\n")
    c.execute("ALTER TABLE busTable ADD COLUMN '%s' TEXT " % name_stop)
    conn.commit()


def view_all_bus():
    c.execute('SELECT * FROM busTable')
    rows = c.fetchall()
    view__bus = {}
    i = 0
    j = 2
    while i != rows.__len__():
        view__bus["Маршрут: "] = rows[i][1]
        while j != rows[i].__len__():
            if str(rows[i][j]) != "None":
                view__bus[str(bus_stops[j - 2]) + ": "] = (rows[i][j])
            j += 1
        for item in view__bus:
            print "%s %s" % (item, view__bus[item])
        view__bus.clear()
        print('\n')
        i += 1
        j = 2


view_all_bus()
now = datetime.datetime.now()
print("Время: %s" % now.strftime("%H:%M")
)
# add_stop()
c.close()
conn.close()
