import datetime
from io import StringIO

import pandas as pd
import psycopg2
import psycopg2.extras
# from sqlalchemy import create_engine
import yfinance as yf


# df = yf.download('MMM', period='6mo')

# df = yf.download("MMM", start="2022-04-11", end="2022-04-17")

# engine = create_engine('postgresql://postgres:syncmaster@localhost/test_db')

# conn = psycopg2.connect(dbname='test_db', user='postgres',
#                       password='syncmaster', host='localhost')
# cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
# cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(dbname='SP500', user='postgres',
#                          password='syncmaster', host='localhost')
#         print("Connection to PostgreSQL DB successful")
#         return conn
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         # sys.exit(1)

def query_delete_duplicates(ticket, row):
    return f"""
        DELETE FROM {ticket} WHERE ctid NOT IN (SELECT max(ctid) FROM {ticket} GROUP BY {row});
        """


class Database:

    def __init__(self, dbname):
        self.dbname = dbname
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(dbname=dbname, user='postgres',  # dbname='SP500'
                                         password='syncmaster', host='localhost')
            print("Connection to PostgreSQL DB successful")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.NamedTupleCursor)

    def connector(self):
        return self.conn

    def cursor(self):
        return self.cursor

    def execute(self, query):
        self.cursor.execute(query)

    def __del__(self):
        self.conn.close()
        print('Connection closed')


class Tables(Database):

    def __int__(self, dbname):
        super().cursor()

    def fetch_one(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"The error '{error}' occurred")
        self.cursor.close()

    def fetch_all(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"The error '{error}' occurred")
        self.cursor.close()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            if len(self.conn.notices) != 0:
                print(self.conn.notices)
            if len(self.cursor.statusmessage) != 0:
                print(self.cursor.statusmessage)
            print("Query executed successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"The error '{error}' occurred")
        self.cursor.close()

    def copy_from_stringio(self, df, table):
        """
        Here we are going save the dataframe in memory
        and use copy_from() to copy it to the table
        """
        # save dataframe to an in memory buffer
        buffer = StringIO()
        df.to_csv(buffer, header=False)
        buffer.seek(0)
        try:
            self.cursor.copy_from(buffer, f"{table}", sep=",")
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:

            print(f"The error '{error}' occurred")
            self.conn.rollback()
            self.cursor.close()
            return 1
        print("Copy from stringio to DB done")
        self.cursor.close()


# db = Database()
# db.connector()
# with Database() as db:
#     db.connector()
#     db.cursor()

db = Tables('SP500')
#
# print(tikers.fetch_one('SELECT max(date) FROM "mmm_1d"')[0])

# print(db.execute_query(query_delete_duplicates("mmm_1d", 'date')))
last_date_raw = db.fetch_one(f'SELECT max(date) FROM "mmm_1d"')


# conn.read_query_one1('SELECT max(Date) FROM mmm')

# class Ticket:


# cursor = conn.cursor()


def dl_data_yf_period(ticket, start_time, end_time, timeframe: str = '1d'):
    '''
    :param ticket: from Yahoo Finance
    :param start_time: Date start
    :param end_time: Date end
    :param timeframe: valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    :return: pandas dataframe
    '''
    data = None
    try:
        data = yf.download(ticket, start=start_time,
                           end=end_time, interval=timeframe)
        return data
    except Exception as error:
        print(f"The error '{error}' occurred")


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


def execute_query55(connection, query):
    # connection.autocommit = True
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    try:
        cursor.execute(query)
        connection.commit()
        print(connection.notices)
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
    cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
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


def volume_price_level_calc(pd_df):
    '''
    Функция находит уровень цен (минимальная цена и максимальная)
    в котором находится наибольший проторгованный объем.
    :param pd_df: На входе pandas dataframe.
    :return: На выходе: два числа float - минимум и максимум цен, которые образуют в дальнейшем уровень цен.
    '''
    #  Делаем копию dataframe
    pd_df = pd_df.copy()
    #  Создаем новый столбец 'Price Groups', в котором все цены будут поделены на группы (количество групп: bins=30)
    pd_df['Price Groups'] = pd.cut(pd_df['Close'], bins=30)
    #  Группируем новую таблицу по столбцу 'Price Groups', при этом суммируем и объединяем все объемы по 'Price Groups'
    pd_df = pd_df.groupby(['Price Groups'])['Volume'].sum().reset_index()
    # Сортируем новую таблицу по столбцу 'Volume', наибольшие объемы вверху таблицы
    sorted_pd_df = pd_df.sort_values(by='Volume', ascending=False)
    #  Делаем табличку short с тремя верхними диапазонами, которые имеют самые большие объемы
    short = sorted_pd_df.head(3)
    #  Выбираем нижнюю и верхнюю границы этих трех диапазонов цен
    maxprice = short['Price Groups'].max()
    minprice = short['Price Groups'].min()
    return minprice.left, maxprice.right


def dl_new_data_to_db(symbols_to_dl, symbols_in_db, date_from, date_to, tf='d1'):
    for symbol in symbols_to_dl:
        if symbol + '_' + tf not in symbols_in_db:
            print(f'Символа {symbol}_{tf}, нет в базе данных, скачиваем...')
            df = dl_data_yf_period(symbol, date_from, date_to, tf)
            print(f'Создаем таблицу {symbol}_{tf}...')
            execute_query(conn, query_create_table(symbol + '_' + tf))
            print(f'Заполняем таблицу данными {symbol}_{tf}...')
            copy_from_stringio(conn, df, symbol + '_' + tf)
        else:
            print(
                f'Символ {symbol}_{tf} присутствует в базе, нужно обновление БД, а не загрузка')


def dl_and_add_to_db(symbols_to_dl, symbols_in_db, date_from, date_to, tf='d1'):
    for symbol in symbols_to_dl:
        if tf == 'd1':
            print(f' Проверяем последнюю запись в базе по {symbol}_{tf}...')
            last_date_raw = read_query_one(
                conn, f'SELECT max(date) FROM "{symbol}+_+{tf}"')
            last_date = last_date_raw[0].date()
            if last_date != datetime.date.today() and last_date != datetime.date.today() - datetime.timedelta(days=1):
                print(
                    f'База данных {symbol}_{tf} содержит последнюю запись от {last_date}')
                print(
                    f'Скачиваем данные с {last_date} по {datetime.date.today()}... ')
                df_d = dl_data_yf_period(
                    symbol, last_date, datetime.date.today())
                print(f'Загружаем полученные данные по {symbol}_{tf} в БД...')
                copy_from_stringio(conn, df_d, symbol + '_' + tf)
                print(f'Удаляем возможные дубли в базе {symbol}_{tf}')
                execute_query(conn, query_delete_duplicates(
                    symbol + '_' + tf, 'date'))

# def dl_data_from_yahoo_to_db(symbols_to_dl, symbols_in_db, date_from, date_to, tf='d1'):
#     for symbol in symbols_to_dl:
#         if symbol+'_'+tf not in symbols_in_db:
#             print(f'Символа {symbol}_{tf}, нет в базе данных, скачиваем...')
#             df = dl_data_yf_period(symbol, date_from, date_to, tf)
#             print(f'Создаем таблицу {symbol}_{tf}...')
#             execute_query(conn, query_create_table(symbol+'_'+tf))
#             print(f'Заполняем таблицу данными {symbol}_{tf}...')
#             copy_from_stringio(conn, df, symbol+'_'+tf)
#         else:
#             print(f'Символ {symbol}_{tf} присутствует в базе, проверяем последнюю запись в базе...')
#             last_date_raw = read_query_one(conn, f'SELECT max(date) FROM "{symbol}+_+{tf}"')
#             last_date = last_date_raw[0].date()
#             if last_date != datetime.date.today() and last_date != datetime.date.today() - datetime.timedelta(days=1):
#                 if last_date is not None:
#                     print(f'База данных {symbol} содержит последнюю запись от {last_date}')
#                     #  days_plus_one_from_db = last_date[0] + datetime.timedelta(days=1) # если грузим повторно в рабочий день, то день с заврашний)
#                     print(f'Скачиваем данные с {last_date} по {datetime.date.today()}... ')
#                     df_d = dl_data_yf_period(symbol, last_date, datetime.date.today())
#                     print(f'Загружаем полученные данные по {symbol} в БД...')
#                     copy_from_stringio(conn, df_d, symbol)
#                     print(f'Удаляем возможные дубли в базе {symbol}')
#                     execute_query(conn, query_delete_duplicates(symbol, 'date'))
#                 else:
#                     print(f'База данных {symbol} существует, но она пустая! Пробуем скачать данные еще раз...')
#                     df = yf.download(symbol, period='6mo')
#                     print(f'Заполняем таблицу данными {symbol}...')
#                     copy_from_stringio(conn, df, symbol)
#                     last_date = read_query_one(conn, f'SELECT max(date) FROM {symbol}')
#                     if last_date is not None:
#                         print(f'Кажется, база заполнилась)')
#                     else:
#                         print(f'Какие-то проблемы с загрузкой {symbol}')
#                         problem_with_data_load.append(symbol)
#             else:
#                 print(f'База данных {symbol} содержит последнюю запись от {last_date}')
#                 print(f'Данные {symbol} в БД актуальны и не требуют загрузки')


# if __name__ == '__main__':
# dic1 = {'DISH': ['2022-05-06', '2022-05-09', '2022-05-11', '2022-05-12'], 'DLTR': ['2022-05-18', '2022-05-26']}
# for key, value in dic1.items():
#     dic1[key] = [dic1[key], [1,2] ]
#
# for key, value in dic1.items():
#     print(key, value[1])


# for item in somelist:
# somelist2 = [f'"{i}"' for i in somelist]
# for item in somelist:
#     somelist2.append(f'"x-{item}"')
#
# for i in somelist2:
#     print(i)
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

# print(read_query_one(conn, 'SELECT max(Date) FROM mmm'))
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
# data = yf.download(tickers="IBM", start='2022-04-20', end='2022-04-21', interval="5m")
# data = dl_data_yf_period("IBM", '2022-04-20', '2022-04-21', '5m')
# data = data.query("Volume != 0")
# ticket = 'ibm_5m'
# from_date = '2022-04-20'
# data = read_query_all(conn, f"""select * from "{ticket}" where date > '{from_date}'""")
# ---------------

# data = data.copy()
# data['Price Groups'] = pd.qcut(data['Close'], q=2, precision=0)
# data['Price Groups'] = pd.qcut(data['Close'], [0, 0.25, 0.5, 0.75, 1])
# data['Price Groups'] = pd.cut(data['Close'], bins=30)

# data = data.groupby(['Price Groups'])['Volume'].sum().reset_index()
# data = data.groupby(['Price Groups'])['Volume']

# sorted_df = data.sort_values(by='Volume', ascending=False)

# print(sorted_df[['Volume', 'Price Groups']])
# short = sorted_df.head(3)

# maxprice = short['Price Groups'].max()
# minprice = short['Price Groups'].min()
# print(minprice.left, maxprice.right)

# ----------------------
#     print(volume_price_level_calc(data))

# sorted_df['Volumes'].plot(kind='hist')
# plt.show()

# sorted_df = data.sort_values(by='Volume', ascending=False)
# print(data)
# print(data[['Volume', 'Price Groups']])
# print(short)
# print(sorted_df.dtypes)

# print(minprice, maxprice)

# ----------------------------
# df = data.groupby(['Volume'])['Close'].sum()
# df['Volume'](by=df['Close'])
# print(data[['Close', 'Volume', 'Price Groups']])
# df['Close'].plot(kind='hist')
# maxclose = df.head()['Close'].max()
# minclose = df.head()['Close'].min()
# print(minclose, maxclose)
# plt.show()
# ---------------


# -------------
#     df = data.groupby(['Volume'])['Close'].sum().reset_index()
#     print(df.head(3))
#     df['Close'].plot(kind='hist')
#     maxclose = df.head()['Close'].max()
#     minclose = df.head()['Close'].min()
#     print(minclose, maxclose)
#     #plt.show()
# -----------


# sorted_df = data.sort_values(by='Close', ascending=False)
# print(data.dtypes)
# print(sorted_df[['High', 'Low', 'Close', 'Volume']])

# -------------
# data.plot(x="Close", y=["Volume"], kind="scatter")
# plt.show()
# -------------
# cursor.close()
# conn.close()
# if __name__ == '__main__':
#     pass
