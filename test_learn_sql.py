from io import StringIO
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd
from psycopg2 import OperationalError
import datetime
import time

# df = yf.download('MMM', period='6mo')

# df = yf.download("MMM", start="2022-04-11", end="2022-04-17")

# engine = create_engine('postgresql://postgres:syncmaster@localhost/test_db')

conn = psycopg2.connect(dbname='test_db', user='postgres',
                        password='syncmaster', host='localhost')
# cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


# cursor = conn.cursor()


def dl_data_yf_period(ticket, start_time, end_time):
    data = None
    try:
        data = yf.download(ticket, start=start_time, end=end_time)
        return data
    except Exception as error:
        print(f"The error '{error}' occurred")


def query_delete_duplicates(ticket, row):
    return f"""
        DELETE FROM {ticket} WHERE ctid NOT IN (SELECT max(ctid) FROM {ticket} GROUP BY {row});
        """


def query_create_table(table_name):
    return f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    Date timestamp,
    Open double precision,
    High double precision,
    Low double precision,
    Close double precision,
    "Adj Close" double precision,
    Volume bigint
    )
    """


query_get_list_of_tables = '''
    SELECT tablename
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog' AND
    schemaname != 'information_schema';
'''


def execute_query(connection, query):
    # connection.autocommit = True
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    try:
        cursor.execute(query)
        conn.commit()
        print(conn.notices)
        print(cursor.statusmessage)
        print("Query executed successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"The error '{error}' occurred")
    cursor.close()


def read_query_all(connection, query):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"The error '{error}' occurred")
    cursor.close()


def read_query_one(connection, query):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"The error '{error}' occurred")
    cursor.close()


# cursor.execute(query_create_table('mmm'))
# conn.commit()


def copy_from_stringio(conn, df, table):
    """
    Here we are going save the dataframe in memory
    and use copy_from() to copy it to the table
    """
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, header=False)
    buffer.seek(0)

    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:

        print(f"The error '{error}' occurred")
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()


somelist = ['mmm', 'ddd', 'bbb']
somelist2 = []

if __name__ == '__main__':
    #for item in somelist:
    #somelist2 = [f'"{i}"' for i in somelist]
    for item in somelist:
        somelist2.append(f'"x-{item}"')

    for i in somelist2:
        print(i)
    # execute_query(conn, query_create_table('mmm'))
    # cursor.execute('SELECT * FROM MMM')
    # cursor.execute('SELECT max(Date) FROM mmm;')
    # execute_query(conn, 'SELECT date FROM MMM')
    # records = cursor.fetchall()
    # records = cursor.fetchone()

    # d = datetime.datetime.today() + datetime.timedelta(days=1)
    # df.to_sql("MMM", engine, if_exists='replace')
    # for row in records:
    #     print(f'{row.date}, {row.volume}')

    # copy_from_stringio(conn, df, 'mmm')  # working

    # last_date = read_query_one(conn, 'SELECT max(Date) FROM mmm')
    # last_date_and_one = last_date
    # if last_date[0] != None:

    #    print(last_date[0])
    # df = dl_data_yf_period('mmm', last_date[0], datetime.datetime.today())
    # read_query_all(conn, query_delete_duplicates('mmm', 'date'))
    # copy_from_stringio(conn, df, 'mmm')

    # cursor.copy_from(buffer, 'MMM', sep=",")
    # cursor.copy_expert(sql, file=buffer)

    # print(records[0])
    # print(records[0] + datetime.timedelta(days=1))
    # days_plus_one_from_db = records[0] + datetime.timedelta(days=1)
    # print(days_plus_one_from_db)
    # print(datetime.datetime.today())

    # execute_query(conn, query_delete_duplicates('mmm', 'date'))
    # execute_query(conn, query_create_table('mmm'))

    # df = dl_data_yf_period('MMM', '2022-04-15', datetime.datetime.today())

    cursor.close()
    conn.close()
