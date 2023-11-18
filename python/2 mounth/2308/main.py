from multiprocessing import connection
import psycopg2
connect = psycopg2.connect(
    host = '127.0.0.1',
    database = 'ww',
    user = 'postgres',
    password = '8659', 
    port = '5432'
    
)
print('d')
cursor = connect.cursor()
#query = 'create table class (id serial primary key, name text, class text);'
#cursor.execute(query)
#connect.commit()
#cursor.close()
#connect.close()
#cursor.execute ("insert into class (name, class) values('anna', '9a'), ('rostik', '12a')")
#connect.commit()
cursor.execute("select * from class")
connect.commit()
data = cursor.fetchall()
print (data)

#cursor.execute("update class set name = 'farruh' where id= 2")
#connect.commit()




cursor.execute("DELETE FROM class WHERE id=2")
connect.commit()

cursor.execute("select * from class")
connect.commit()
data = cursor.fetchall()
print (data)















cursor.close()
connect.close()