
import psycopg2.extras
import psycopg2

hostname = 'localhost'
database = 'password_project'
username = 'postgres'
pas = 'richy'
port = 5432
conn = None

a=[]
try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pas,
                port = port) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('SELECT * FROM RIC')
            a=cur.fetchall():
            print(a)

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
