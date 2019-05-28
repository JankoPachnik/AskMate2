import psycopg2
import psycopg2.extras


def sql_data(sql_query, operation_type, data=None):
    try:
        user_name = "aleksander"
        password = "Minotaur1"
        host = "localhost"
        database_name = "codecooler"

        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
        print("Connection string: " + connect_str)

        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()

        if operation_type == "read":
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(sql_query, data)
            data = cursor.fetchall()
            return data

        elif operation_type == "write":
            cursor.execute(sql_query, data)

        else:
            cursor.execute(sql_query, data)

        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        # checks first whether the connection has been created successfully
        if 'connection' in locals():
            connection.close()