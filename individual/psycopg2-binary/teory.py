import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="aziz2",
    user="postgres",
    password="8659"
)
# try:
#     # пытаемся подключиться к базе данных
#     conn = psycopg2.connect(dbname='aziz2', user='postgres', password='8659', host='localhost')
#     # conn = psycopg2.connect('postgresql://user:password@host:port/database_name')
# except:
#     # в случае сбоя подключения будет выведено сообщение в STDOUT
#     print('Can`t establish connection to database')


# выполнить SQL-запросы с помощью объекта cursor
# получение объекта курсора
cursor = conn.cursor()


# Получаем список всех пользователей
# cursor.execute('SELECT * FROM users')
# all_users = cursor.fetchall()

# print(all_users)

# for row in all_users:
#     print(row)




# вставлять данные в базу данных с помощью метода execute() и метода commit()
# cursor.execute("INSERT INTO users (id, name, email) VALUES (2, 'Big Ben', 'Ben@example.com');")
# conn.commit()









cursor.close() # закрываем курсор
conn.close() # закрываем соединение


# with conn.cursor as curs:
#     curs.execute('SELECT * FROM users')
#     all_users = curs.fetchall()