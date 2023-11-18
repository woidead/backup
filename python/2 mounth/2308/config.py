from multiprocessing import connection
import psycopg2
connect = psycopg2.connect(
    host = '127.0.0.1',
    database = 'ww',
    user = 'postgres',
    password = '8659', 
    port = '5432'
    
)
print('добро пожаловать в магазин')
cursor = connect.cursor()

cursor.execute("select * from products")
connect.commit()
data = cursor.fetchall()
for i in data:
    print (i)


# x = input('что вы хотите купить? ')
# y = int(input('выберите количество '))
# cursor.execute(f"select price from products where productname = '{x}' ")
# connect.commit()
# data = cursor.fetchall()
# print (data)
# print(f'счет: Товар: {x}, количество: {y}, цена: {data}, общая сумма: {y} x {data}'  )



cursor.execute("update products set price = '66000' where id = 1;")
connect.commit()











cursor.close()
connect.close()