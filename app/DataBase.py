import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    if conn is not None:
        try:
            sql = """ CREATE TABLE IF NOT EXISTS logs (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        user_id text,
                        user_name text,
                        group_name text,
                        date text,
                        raw_text text
                      ); """
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

def add_log(conn, user_id, user_name, group_name, date, raw_text):
    try:
        sql = ''' INSERT INTO logs (user_id, user_name, group_name, date, raw_text)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (user_id, user_name, group_name, date, raw_text))
        return cur.lastrowid
    except Error as e:
        print(e)

# def query_all_users(conn):
#     try:
#         cur = conn.cursor()
#         cur.execute('SELECT uid, language, user_id FROM users')
#         result = cur.fetchall()
#         if result!=[]:
#             return result
#         else:
#             return 0
#     except Error as e:
#         print(e)
#         return 0
# def query_user(conn, uid):
#     try:
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM users WHERE uid=?', (uid,))
#         result = cur.fetchall()
#         if result!=[]:
#             return result[0]
#         else:
#             return 0
#     except Error as e:
#         print(e)
#         return 'Fail'

# def query_all_targets(conn):
#     try:
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM targets')
#         result = cur.fetchall()
#         if result!=[]:
#             return result
#         else:
#             return 0
#     except Error as e:
#         print(e)
# 
# def query_target(conn, shortened_link):
#     try:
#         cur = conn.cursor()
#         cur.execute('SELECT target_link, counter FROM targets WHERE shortened_link=?', (shortened_link,))
#         result = cur.fetchall()
#         if result!=[]:
#             return result[0][0], result[0][1]
#         else:
#             return [0,0]
#     except Error as e:
#         print(e)
# 
# def query_target_by_link(conn, target_link):
#     try:
#         cur = conn.cursor()
#         cur.execute('SELECT shortened_link FROM targets WHERE target_link=?', (target_link,))
#         result = cur.fetchall()
#         if result!=[]:
#             return result[0][0]
#         else:
#             return 0
#     except Error as e:
#         print(e)
# 
# def edit_user(conn, uid, name=None, user_id=None, state=None):
#     if name!=None:
#         try:
#             cur = conn.cursor()
#             cur.execute('UPDATE users SET name=? WHERE uid=?', (name, uid,))
#             conn.commit()
#         except Error as e:
#             print(e)
#     if user_id!=None:
#         try:
#             cur = conn.cursor()
#             cur.execute('UPDATE users SET user_id=? WHERE uid=?', (user_id, uid,))
#             conn.commit()
#         except Error as e:
#             print(e)
#     if state!=None:
#         try:
#             cur = conn.cursor()
#             cur.execute('UPDATE users SET state=? WHERE uid=?', (state, uid,))
#             conn.commit()
#         except Error as e:
#             print(e)

# def edit_target(conn, shortened_link, counter):
#     try:
#         cur = conn.cursor()
#         cur.execute('UPDATE targets SET counter=? WHERE shortened_link=?', (counter, shortened_link,))
#         conn.commit()
#     except Error as e:
#         print(e)

# def delete_target(conn, shortened_link):
#     try:
#         cur = conn.cursor()
#         cur.execute('DELETE FROM targets WHERE shortened_link=?', (shortened_link,))
#         conn.commit()
#         return 1
#     except Error as e:
#         print(e)
#         return 0
