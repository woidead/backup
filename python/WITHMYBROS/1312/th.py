import psycopg2
params = 'host = localhost dbname = clientshop user = postgres password=8659'
con = psycopg2.connect(params)
thirdint = (input('Напишите ID товаров которых надо купить через прбел'))
x = thirdint.split()
name = []
for i in range(0, len(x)):
    query2 = f"select * from products WHERE id = {x[i]};"
    cur = con.cursor()
    cur.execute(query2)
    viv = cur.fetchall()
    for row in viv:
                name.append(row[1])
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2], "сом")
                print("Количество =", row[3], "сом", "\n") 
for new in name:
    print(new)




con.commit()
cur.close()
con.close()
con.close()