import psycopg2
import os

TABLE_NAME = 'pos_rate_hist'


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
    )
    return conn


def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        curr TEXT,
        rate TEXT,
        rdate TEXT);
    ''')
    conn.commit()
    cur.close()
    conn.close()


def proc_rate_hist(curr, rate, date):
    save_rate_hist(curr, rate, date)
    hist = get_rate_hist(curr)
    return hist


def save_rate_hist(curr, rate, date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'''
    INSERT INTO {TABLE_NAME} (curr, rate, rdate)
    VALUES (%s, %s, %s);
    ''', (curr, rate, date))
    conn.commit()
    cur.close()
    conn.close()


def get_rate_hist(curr):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'''
    SELECT curr, rate, rdate FROM {TABLE_NAME}
        WHERE curr = '{curr}' order by rdate;
    ''')
    hist = cur.fetchall()
    cur.close()
    conn.close()
    return hist
