import sqlite3

def save_to_db(id, name, gpa, rank):
    conn = sqlite3.connect('STUDENT.sqlite')
    cur = conn.cursor()
    try:
        cur.executescript('''
            create table student (ID TEXT, Name TEXT, gpa number, rank TEXT)
        ''')
    except:
        pass
    conn.commit()
    conn.close()

if  __name__ == '__main__':
    save_to_db(13, 'Khoa', 8.0, 0)