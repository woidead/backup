import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
params = 'host = localhost dbname = abik user = postgres password=8659'
con = psycopg2.connect(params)
cur = con.cursor()
# inid = int(input('id'))
# inname = input('name')
# insur = input('surname')
# inage = int(input('age'))
# ingen = input('gender')
# innat = input('nationality')
# query = f"insert into students values ({inid}, '{inname}', '{insur}', {inage}, '{ingen}', '{innat}')"
my_table    = pd.read_sql('select * from my-table-name', connection)
cur.execute(query)
con.commit()
cur.close()
con.close()
con.close()