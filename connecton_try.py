import pymysql
from test_connection import host, user, password, db_name


try:
    connection = pymysql.connect(
    host = host,
    port=3306,
    user = user,
    password = password,
    database = db_name,
)
    print('succesfull connection')
    print('')

    try:
        #cursor = connection.cursor()

        #create table
        '''with connection.cursor() as cursor:
            create_table_querry = "CREATE TABLE `name_table`(id int AUTO_INCREMENT," \
                                  " name VARCHAR(32), " \
                                  "password VARCHAR(32), " \
                                  "mail VARCHAR(32), PRIMARY KEY (id));"
            cursor.execute(create_table_querry)
            print('table created')'''
        ''

        #insert data
        '''with connection.cursor() as cursor:
            insert_querry = "INSERT INTO `name_table` (name, password, mail) VALUES ('Me', 'password', 'ubabuba');"
            cursor.execute(insert_querry)
            connection.commit()'''
        #select all data from table
        with connection.cursor() as cursor:
            select_all = "SELECT * FROM `name_table`"
            cursor.execute(select_all)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()
except Exception as ex:
    print('Connection...')
    print(ex)
