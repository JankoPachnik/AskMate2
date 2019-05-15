import psycopg2

import data_manager_sql


def sql_data(sql_query, operation_type, data=None):
    try:
        user_name = "janek"
        password = ""
        host = "localhost"
        database_name = "AskMate"

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
            cursor.execute(sql_query, data)
            data = cursor.fetchall()
            data = data_manager_sql.data_transformation(data)
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