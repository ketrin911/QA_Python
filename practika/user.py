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
            

                user_nameAB = """
                    SELECT  * FROM user
                    WHERE `name` LIKE 'А%' OR
                    `name`  LIKE 'Б%' OR 
                    `name` LIKE '% А%' OR
                    `name`  LIKE '% Б%' AND YEAR(reg_date) = 2018;
                """
                cursor.execute(user_nameAB)
                result = cursor.fetchall()
                
                if result:
                    print (result)
                else:
                    print ("ошибка")     

                create_view = """
                SELECT  * FROM user
                    WHERE `name` LIKE 'А%' OR
                    `name`  LIKE 'Б%' OR 
                    `name` LIKE '% А%' OR
                    `name`  LIKE '% Б%' AND YEAR(reg_date) = 2018
                """
                cursor.execute(create_view)
                connection.commit()
                print('created ')




    except Exception as e:
        print('An error ')
        print(e)        

    finally:
        connection.close()

except Exception as ex:
    print ("connection rufus")
    print (ex)    
    