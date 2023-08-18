import psycopg
import re

# Connect to the database
try:
   conn = psycopg.connect(
       dbname   = 'ed',
       user     = 'ed',
       host     = 'ada.hpc.stlawu.edu',
       password = open('../../.pgpass').readline().strip())
except psycopg.Error as e:
   print("Error: unable to connect to the database")
   print(e)
   exit()

conn.autocommit = True
cur = conn.cursor()

for user in open('users.txt'):
    user = user.strip()
    cmd1 = f'DROP ROLE IF EXISTS {user};'
    cmd2 = f"""CREATE ROLE {user} LOGIN PASSWORD '{user}'
               VALID UNTIL 'infinity'
               NOSUPERUSER INHERIT CREATEDB NOCREATEROLE NOREPLICATION;"""
    cmd2 = re.sub('\\s+', ' ', cmd2)
    cmd3 = f'DROP DATABASE IF EXISTS {user};'
    cmd4 = f"CREATE DATABASE {user};"
    cmd5 = f"REVOKE CONNECT ON DATABASE {user} FROM PUBLIC;"
    cmd6 = f"GRANT CONNECT ON DATABASE {user} TO {user};"
    try:
        # print(cmd1)
        # print(cmd2)
        # print(cmd3)
        # print(cmd4)
        # print(cmd5)
        # print(cmd6)
        cur.execute(cmd1)
        cur.execute(cmd2)
        cur.execute(cmd3)
        cur.execute(cmd4)
        cur.execute(cmd5)
        cur.execute(cmd6)
        # cur.commit()  # not running within a transaction
    except psycopg.Error as e:
        print(f'Error: create role {user.strip()}. {e}')

cur.close()
conn.close()
