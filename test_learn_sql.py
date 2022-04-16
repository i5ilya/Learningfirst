from io import StringIO
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd
from psycopg2 import OperationalError

#df = yf.download('MMM', period='1mo')

# engine = create_engine('postgresql://postgres:syncmaster@localhost/test_db')

conn = psycopg2.connect(dbname='test_db', user='postgres',
                        password='syncmaster', host='localhost')
#cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)


# cursor = conn.cursor()


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


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"The error '{error}' occurred")


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


if __name__ == '__main__':
    execute_query(conn, query_create_table('mmm'))
    #cursor.execute('SELECT * FROM MMM')
    execute_query(conn, 'SELECT date FROM MMM')
    #records = cursor.fetchall()
    # df.to_sql("MMM", engine, if_exists='replace')
    # for row in records:
    #     print(f'{row.date}, {row.volume}')
    #copy_from_stringio(conn, df, 'mmm')  # working
    # cursor.copy_from(buffer, 'MMM', sep=",")
    # cursor.copy_expert(sql, file=buffer)
    #print(records)
    # conn.commit()
    # cursor.close()
    # conn.close()
