import psycopg2
params = 'host = localhost dbname = clientshop user = postgres password=8659'
con = psycopg2.connect(params)
cur = con.cursor()


firstint = int(input("""
                                                                                    Добро Пожаловать в продуктовый магазин WOIDEAD 
                                                                                            Для продолжения нажмите 1
"""))
if firstint == 2:
    secondint = int(input("""
    Вы вошли как работник
    Какое действие вы хотите провести?
    1. Действия с товаром
    2. Действия с Клиентской базой
    3. Действия с базой закaзов
    4. Действия с базой работников
    """))


    if secondint == 1:
        thirdint = int(input(""" 
        1. Добавить позицию
        2. Изменить название
        3. Изменить количество
        4. Изменить цену
        5. Удалить позицию
        """))
        if thirdint == 1:
            query3 = f"select max(id) from products;"
            cur.execute(query3)
            viv = cur.fetchone()
            for row in viv:
                print()
                print('Последнее id: ',row)
            inid = int(input('id нового товара: '))
            inname = input('Название нового товара: ')
            inprice = int(input('Стоимость нового товара: '))
            incount = int(input("Количество нового товара: "))
            query = f"insert into products values({inid}, '{inname}', {inprice}, {incount})"
            cur.execute(query)
            query2 = f"select * from products where id = {inid};"
            cur.execute(query2)
            print('Добавлены строчки')
            viv = cur.fetchall()
            for row in viv:
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2])
                print("Количество на складе =", row[3], "\n")
            con.commit()
            cur.close()
            con.close()
            con.close()
        elif thirdint == 2:
            inid = int(input('ID товара которого надо изменить название:'))
            query3 = f"select * from products where id = {inid};"
            cur.execute(query3)
            viv = cur.fetchone()
            print()
            print('Название редактируемой строки:',viv[1])
            inname  = input('Новое название: ')
            query = f"UPDATE products set name = '{inname}' where id = {inid};"
            query2 = f"select * from products;"
            cur.execute(query)
            cur.execute(query2)
            print('Обновленная таблица')
            viva = cur.fetchall()
            for row in viva:
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2])
                print("Количество на складе =", row[3], "\n")
            con.commit()
            cur.close()
            con.close()
            con.close()


        elif thirdint == 3:
            inid = int(input('ID товара которого надо изменить количество:'))
            query3 = f"select * from products where id = {inid};"
            cur.execute(query3)
            viv = cur.fetchone()
            print()
            print('Название редактируемой строки:',viv[1], 'и количество', viv[3])
            incount  = input('Актуальное количество: ')
            query = f"UPDATE products set count = {incount} where id = {inid};"
            query2 = f"select * from products where id = {inid};"
            cur.execute(query)
            cur.execute(query2)
            print('Обновленная таблица')
            viva = cur.fetchall()
            for row in viva:
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2])
                print("Количество на складе =", row[3], "\n")
            con.commit()
            cur.close()
            con.close()
            con.close()
        elif thirdint == 4:
            inid = int(input('ID товара которого надо изменить цену:'))
            query3 = f"select * from products where id = {inid};"
            cur.execute(query3)
            viv = cur.fetchone()
            print()
            print('Название редактируемой строки:',viv[1], 'и цена', viv[2])
            inprice  = input('Актуальная цена: ')
            query = f"UPDATE products set count = {inprice} where id = {inid};"
            query2 = f"select * from products where id = {inid};"
            cur.execute(query)
            cur.execute(query2)
            print('Обновленная таблица')
            viva = cur.fetchall()
            for row in viva:
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2])
                print("Количество на складе =", row[3], "\n")
            con.commit()
            cur.close()
            con.close()
            con.close()
        elif thirdint == 5:
            inid = int(input('ID товара которого надо удалить:'))
            query = f"delete from products where id = {inid};"
            cur.execute(query)
            print()
            print('Обновленная таблица')
            query2 = f"select * from products;"
            cur.execute(query2)
            viv = cur.fetchall()
            for row in viv:
                print()
                print("Id =", row[0], )
                print("Название товара =", row[1])
                print("Цена =", row[2])
                print("Количество на складе =", row[3], "\n")
            cur.execute(query2)
            con.commit()
            cur.close()
            con.close()
            con.close()


    elif secondint == 2:
        thirdint = int(input("""
        1. Добавить данные
        2. Редактировать данные
        3. Удалить данные
        """))
        if thirdint == 1:
            query3 = f"select max(id) from clients;"
            cur.execute(query3)
            viv = cur.fetchone()
            for row in viv:
                print('Последнее id:',row)
            inid = int(input('id клиента: '))
            inname = input('Имя клиента: ')
            insur = input('Фамилия клиента: ')
            innumber = int(input("Моб. номер клиента: "))
            query = f"insert into clients values({inid}, '{inname}', '{insur}', {innumber})"
            cur.execute(query)
            con.commit()

            print()
            print('Добавлены строчки')
            query2 = f"select * from clients where id = {inid};"
            cur.execute(query2)
            viva = cur.fetchall()
            for row in viva:
                print()
                print("Id =", row[0])
                print("Имя =", row[1])
                print("Фамилия =", row[2])
                print("Моб. номер =", row[3], "\n")
        elif thirdint == 2:

            fourth = int(input("""
            Изменить какие данные?
            1. id
            2. Имя
            3. Фамилия
            4. Моб. телефон
            """))

            if fourth == 1:
                inid = int(input('ID человека которого надо изменить ID:'))
                query3 = f"select * from clients where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и имя', viv[1])
                innewid  = input('Новое имя: ')
                query = f"UPDATE clients set id = {innewid} where id = {inid};"
                query2 = f"select * from clients where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Моб. номер =", row[3], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
            if fourth == 2:
                inid = int(input('ID человека которого надо изменить Имя:'))
                query3 = f"select * from clients where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id:',viv[0], 'и имя:', viv[1])
                innewname  = input('Новое имя: ')
                query = f"UPDATE clients set name = '{innewname}' where id = {inid};"
                query2 = f"select * from clients where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Моб. номер =", row[3], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 3:
                inid = int(input('ID человека которого надо изменить Фамилию:'))
                query3 = f"select * from clients where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и имя', viv[1])
                innewsurname  = input('Новая фамилия: ')
                query = f"UPDATE clients set surname = '{innewsurname}' where id = {inid};"
                query2 = f"select * from clients where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Моб. номер =", row[3], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 4:
                inid = int(input('ID человека которого надо изменить ID:'))
                query3 = f"select * from clients where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print(f'Редактируемая данные: id = {viv[0]} имя = {viv[1]},  моб. номер = {viv[3]}')
                innewnumber  = input('Новый номер: ')
                query = f"UPDATE clients set number = {innewnumber} where id = {inid};"
                query2 = f"select * from clients where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Моб. номер =", row[3], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
        
        elif thirdint == 3:
            inid = int(input('ID клиента которого надо удалить:'))
            query = f"delete from clients where id = {inid};"
            cur.execute(query)
            print()
            print('Обновленная таблица')
            query2 = f"select * from clients;"
            cur.execute(query2)
            viv = cur.fetchall()
            for row in viv:
                print()
                print("Id =", row[0], )
                print("Имя клиента =", row[1])
                print("Фамилия клиента =", row[2])
                print("Моб. номер =", row[3], "\n")
            cur.execute(query2)
            con.commit()
            cur.close()
            con.close()
            con.close()



        
    elif secondint == 3:
        thirdint = int(input("""
        1. Добавить данные
        2. Редактировать данные
        3. Удалить данные
        """))
        if thirdint == 1:
            query3 = f"select max(id) from orders;"
            cur.execute(query3)
            viv = cur.fetchone()
            for row in viv:
                print('Последнее id:',row)
            inid = int(input('id заказа: '))
            inname = input('Имя клиента: ')
            insur = input('Фамилия клиента: ')
            infprice = int(input("Полная стоимость всех заказов: "))
            infcount = int(input("Общее количество купленных товаров: "))
            intime = input('Время покупки: ')
            query = f"insert into orders values({inid}, '{inname}', '{insur}', {infprice}, {infcount},'{intime}')"
            cur.execute(query)
            con.commit()

            print()
            print('Добавлены строчки')
            query2 = f"select * from orders where id = {inid};"
            cur.execute(query2)
            viva = cur.fetchall()
            for row in viva:
                print()
                print("Id =", row[0])
                print("Имя =", row[1])
                print("Фамилия =", row[2])
                print("Полная стоимость всех заказов =", row[3])
                print("Общее количество купленных товаров =", row[4])
                print("Время покупки =", row[5], "\n")
        elif thirdint == 2:

            fourth = int(input("""
            Изменить какие данные?
            1. id
            2. Имя
            3. Фамилия
            4. Полная стоимость всех заказов
            5. Общее количество купленных товаров
            """))

            if fourth == 1:
                inid = int(input('ID заказа которого надо изменить ID:'))
                query3 = f"select * from orders where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и имя покупателя', viv[1])
                innewid  = input('Новое id: ')
                query = f"UPDATE orders set id = {innewid} where id = {inid};"
                query2 = f"select * from orders where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Полная стоимость всех заказов =", row[3])
                    print("Общее количество купленных товаров =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
            if fourth == 2:
                inid = int(input('ID заказа которого надо изменить Имя:'))
                query3 = f"select * from orders where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id:', viv[0], 'и имя:', viv[1])
                innewname  = input('Новое имя: ')
                query = f"UPDATE orders set client_name = '{innewname}' where id = {inid};"
                query2 = f"select * from orders where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Полная стоимость всех заказов =", row[3])
                    print("Общее количество купленных товаров =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 3:
                inid = int(input('ID заказа которого надо изменить Фамилию:'))
                query3 = f"select * from orders where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и фамилия', viv[2])
                innewsurname  = input('Новая фамилия: ')
                query = f"UPDATE orders set client_surname = '{innewsurname}' where id = {inid};"
                query2 = f"select * from orders where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Полная стоимость всех заказов =", row[3])
                    print("Общее количество купленных товаров =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 4:
                inid = int(input('ID человека которого надо изменить полная стоимость всех заказов:'))
                query3 = f"select * from orders where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print(f'Редактируемая данные: id = {viv[0]} имя = {viv[1]},  Полная стоимость всех заказов = {viv[3]}')
                innewfprice  = input('Полная стоимость всех заказов: ')
                query = f"UPDATE orders set full_price = {innewfprice} where id = {inid};"
                query2 = f"select * from orders where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Полная стоимость всех заказов =", row[3])
                    print("Общее количество купленных товаров =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
            if fourth == 5:
                inid = int(input('ID человека которого надо общее количество купленных товаров:'))
                query3 = f"select * from orders where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print(f'Редактируемая данные: id = {viv[0]} имя = {viv[1]},  oбщее количество купленных товаров = {viv[4]}')
                innewfcount  = input('Полная стоимость всех заказов: ')
                query = f"UPDATE orders set full_count = {innewfcount} where id = {inid};"
                query2 = f"select * from orders where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0], )
                    print("Имя клиента =", row[1])
                    print("Фамилия клиента =", row[2])
                    print("Полная стоимость всех заказов =", row[3])
                    print("Общее количество купленных товаров =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
        
        elif thirdint == 3:
            inid = int(input('ID заказа которого надо удалить:'))
            query = f"delete from orders where id = {inid};"
            cur.execute(query)
            print()
            print('Обновленная таблица')
            query2 = f"select * from orders;"
            cur.execute(query2)
            viv = cur.fetchall()
            for row in viv:
                print()
                print("Id =", row[0], )
                print("Имя клиента =", row[1])
                print("Фамилия клиента =", row[2])
                print("Полная стоимость всех заказов =", row[3])
                print("Общее количество купленных товаров =", row[4], "\n")
            cur.execute(query2)
            con.commit()
            cur.close()
            con.close()
            con.close()

        
    
    elif secondint == 4:
        thirdint = int(input("""
        1. Добавить данные
        2. Редактировать данные
        3. Удалить данные
        """))
        if thirdint == 1:
                query3 = f"select max(id) from workers;"
                cur.execute(query3)
                viv = cur.fetchone()
                for row in viv:
                    print('Последнее id:',row)
                inid = int(input('id работника: '))
                inname = input('Имя работника: ')
                insurname = input('Фамилия работника: ')
                insolary = int(input('Зарплата работника: '))
                intwtime = int(input('Время работы за этот месяц: '))
                
                query = f"insert into workers values({inid}, '{inname}','{insurname}',{insolary}, {intwtime})"
                cur.execute(query)
                con.commit()
                print()
                print('Добавлены строчки')
                query2 = f"select * from workers where id = {inid};"
                cur.execute(query2)
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
        elif thirdint == 2:
    
            fourth = int(input("""
            Изменить какие данные?
            1. id
            2. Имя
            3. Фамилия
            4. Зарплата работника 
            5. Время работы за этот месяц
            """))

            if fourth == 1:
                inid = int(input('ID работника которого надо изменить ID:'))
                query3 = f"select * from workers where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и имя работника', viv[1])
                innewid  = input('Новое id: ')
                query = f"UPDATE workers set id = {innewid} where id = {inid};"
                query2 = f"select * from workers where id = {innewid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
            if fourth == 2:
                inid = int(input('ID работника которого надо изменить Имя:'))
                query3 = f"select * from workers where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id:', viv[0], 'и имя:', viv[1])
                innewname  = input('Новое имя: ')
                query = f"UPDATE workers set name = '{innewname}' where id = {inid};"
                query2 = f"select * from workers where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 3:
                inid = int(input('ID работника которого надо изменить Фамилию:'))
                query3 = f"select * from workers where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print('Редактируемая данные: id',viv[0], 'и фамилия', viv[2])
                innewsurname  = input('Новая фамилия: ')
                query = f"UPDATE workers set surname = '{innewsurname}' where id = {inid};"
                query2 = f"select * from workers where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()


            if fourth == 4:
                inid = int(input('ID человека которого надо изменить Зарплата работника:'))
                query3 = f"select * from workers where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print(f'Редактируемая данные: id = {viv[0]} имя = {viv[1]},  Зарплата работника = {viv[3]}')
                innewsalary  = input('Зарплата работника: ')
                query = f"UPDATE workers set solary = {innewsalary} where id = {inid};"
                query2 = f"select * from workers where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
            if fourth == 5:
                inid = int(input('ID человека которого надо изменить Время работы за этот месяц:'))
                query3 = f"select * from workers where id = {inid};"
                cur.execute(query3)
                viv = cur.fetchone()
                print()
                print(f'Редактируемая данные: id = {viv[0]} имя = {viv[1]},  Время работы за этот месяц = {viv[4]}')
                innewwtime  = input('Время работы за этот месяц: ')
                query = f"UPDATE workers set work_time = {innewwtime} where id = {inid};"
                query2 = f"select * from workers where id = {inid};"
                cur.execute(query)
                cur.execute(query2)
                print('Обновленные данные')
                viva = cur.fetchall()
                for row in viva:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                con.commit()
                cur.close()
                con.close()
                con.close()
        elif thirdint == 3:
                inid = int(input('ID работника которого надо удалить:'))
                query = f"delete from workers where id = {inid};"
                cur.execute(query)
                print()
                print('Обновленная таблица')
                query2 = f"select * from workers;"
                cur.execute(query2)
                viv = cur.fetchall()
                for row in viv:
                    print()
                    print("Id =", row[0])
                    print("Имя =", row[1])
                    print("Фамилия =", row[2])
                    print("Зарплата работника =", row[3])
                    print("Время работы за этот месяц =", row[4], "\n")
                cur.execute(query2)
                con.commit()
                cur.close()
                con.close()
                con.close()


elif firstint == 1:
    secondint = int(input("""
    1.Начать покупку
    2.Посмотреть ассортимент
    3.Завершить
    """))
    if secondint == 2:
        query = f"select * from products;"
        cur.execute(query)
        viva = cur.fetchall()
        for row in viva:
            print()
            print("Id =", row[0], )
            print("Название товара =", row[1])
            print("Цена =", row[2], "сом")
            print("Количество =", row[3], "\n")
        con.commit()
        cur.close()
        con.close()
        con.close()
    if secondint == 1:
        query = f"select * from products;"
        cur.execute(query)
        viva = cur.fetchall()
        for row in viva:
            print()
            print("Id =", row[0], )
            print("Название товара =", row[1])
            print("Цена =", row[2], "сом")
            print("Количество =", row[3], "сом", "\n")
        thirdint = int(input('Напишите ID товаров которых надо купить через прбел'))
        while thirdint != 0:
            thirdint = int(input('Напишите ID товаров которых надо купить через пробел или все'))
            busket = []
            busket.append(thirdint)
            
        # query2 = f"select * from products where id = ;"
        # cur.execute(query2)
        viva = cur.fetchall()
        
        # busket = thirdint.split()
        name = []
        price = []
        for i in range(0, len(busket)):
            query2 = f"select * from products WHERE id = {busket[i]};"
            cur = con.cursor()
            cur.execute(query2)
            viv = cur.fetchall()
            for row in viv:

                name.append(row[1])
            print(name)
                




        con.commit()
        cur.close()
        con.close()
        con.close()

else:
    print()
    print('запустите код и напишите правильно 1')

