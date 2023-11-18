import random
from multiprocessing import connection
import psycopg2
connect = psycopg2.connect(
    host = '127.0.0.1',
    database = 'ww',
    user = 'postgres',
    password = '8659', 
    port = '5432'
    
)
print('хуйня работает')

cursor = connect.cursor()
for i in range(1, 8):
    x = random.randint(10, 30)
    cursor.execute(f"update products set productcount = {x}  where id = {i}")
    connect.commit()
connect.set_client_encoding('UTF8')
cursor.close()
connect.close()
print (connect.encoding)
