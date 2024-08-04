import sqlite3

global conn


def init_db():
    global conn
    conn = sqlite3.connect('curse.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS "CURSES" ("id" INTEGER, "curse" TEXT, PRIMARY KEY("id" 
    AUTOINCREMENT))''')


def get_curses():
    global conn
    cursess = []
    rows = conn.execute("select curse from CURSES")
    for row in rows:
        cursess.append(row[0])

    return cursess
