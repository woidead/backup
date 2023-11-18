import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="aziz2",
    user="postgres",
    password="8659"
)

cursor = conn.cursor()


def get_all_products():
    cursor.execute('SELECT * FROM market_base')
    all_product = cursor.fetchall()
    for row in all_product:
        print(f"'Продукт: {row[0]},   цена: {row[1]},  Количество: {row[2]}")

def post_product(amount, product_name):
    cursor.execute(f"SELECT quantity FROM market_base where name = '{product_name}'")
    total = cursor.fetchall()[0][0] - amount
    cursor.execute(f"UPDATE market_base set quantity = {total} where name = '{product_name}'")
    cursor.execute(f"SELECT * FROM market_base where name = '{product_name}'")
    new_data = cursor.fetchall()
    for row in new_data:
        print(row)
    conn.commit()



def new_products(amount, product_name):
    cursor.execute(f"SELECT quantity FROM market_base where name = '{product_name}'")
    total = cursor.fetchall()[0][0] + amount
    cursor.execute(f"UPDATE market_base set quantity = {total} where name = '{product_name}'")
    cursor.execute(f"SELECT * FROM market_base where name = '{product_name}'")
    new_data = cursor.fetchall()
    for row in new_data:
        print(row)
    conn.commit()    


# get_all_products()
# post_product(1, "apple")
# new_products(1, "apple")
cursor.close() # закрываем курсор
conn.close() # закрываем соединение



"""CREATE TABLE products(name VARCHAR (255), price SMALLINT NOT NULL, quantity SMALLINT NOT NULL);
   INSERT INTO products VALUES('apple', 70, 9);
   INSERT INTO products VALUES('carrots', 11, 8);
   INSERT INTO products VALUES('tomatoes', 12, 11);
"""