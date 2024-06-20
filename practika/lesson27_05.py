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
            number_part_qua = "SELECT * FROM `team` WHERE number_part > 5"
            cursor.execute(number_part_qua)
            result = cursor.fetchall()
            for i in result:
                if not result:
                    print('does not exist')
                else:
                    print(i)



    except Exception as e:
        print('An error ')
        print(e)        

    finally:
        connection.close()

except Exception as ex:
    print ("connection rufus")
    print (ex)    
    