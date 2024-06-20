import pymysql
import pymysql.cursors
from main_config_base import host, user, password, db_name

try:
    connection = pymysql.connect(
    host=host, 
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print ("succsess")
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            create_table_q = '''
            CREATE TABLE IF NOT EXISTS `team`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            team_name VARCHAR(255) NOT NULL,
            number_part INT CHECK (number_part <= 10));
            '''
            cursor.execute(create_table_q)
            print('table team created')

            insert_query = '''
            INSERT INTO `team` (id,team_name,number_part) VALUES
            (1,'kometa',7),
            (2,'zvezda',8),
            (3,'planeta ',5),
            (4,'iskra',10),
            (5,'krokodil',6),
            (6, 'zima',9),
            (7,'polet',7),
            (8,'uran ',3),
            (9,'samolet',9),
            (10,'pirozhok',8)
            '''
            cursor.execute(insert_query)
            connection.commit()
            print('table inserted')

            
            



    except Exception as e:
        print('An error ')
        print(e)        

    finally:
        connection.close()

except Exception as ex:
    print ("connection rufus")
    print (ex)    
