import mysql.connector


def user_db():

    config = {
        'host': 'localhost',
        'database' : 'fuel_station',
        'user' : 'root',
        'password' : '123456789',
    }

    return config


def connectdb():

    config = user_db()
    try:

        connection = mysql.connector.connect(**config)

        if connection.is_connected:

            return connection
        
    except mysql.connector.Error:
        
        print(f'error{mysql.connector.Error}')
        
        return None            


def log_register(msg,datetime):

    connection = connectdb()

    if connection:
        try:

            cursor = connection.cursor()

            query = 'INSERT INTO logs (message, msg_date) VALUES (%s, %s);'
            cursor.execute(query, (msg, datetime))
            
            connection.commit()

        except mysql.connector.Error:

            print(f'Error al realizar la query: {mysql.connector.Error}')

        finally:

            if connection.is_connected():

                cursor.close()
                connection.close()    


def ccaa_register(ccaa_code,datetime):

    connection = connectdb()

    if connection:
        try:

            cursor = connection.cursor()

            query = 'INSERT INTO ccaa_register (location_id, msg_date) VALUES (%s, %s);'
            cursor.execute(query, (ccaa_code, datetime))
            
            connection.commit()

        except mysql.connector.Error:

            print(f'Error al realizar la query: {mysql.connector.Error}')

        finally:

            if connection.is_connected():

                cursor.close()
                connection.close()  
