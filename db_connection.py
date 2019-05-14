import psycopg2


def main():
    try:
        # setup connection string
        user_name = "***"
        password = "***"
        host = "***"
        database_name = "***"

        # this string describes all info for psycopg2 to connect to the database
        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
        print("Connection string: " + connect_str)

        # connection describes and maintaines a connection to the database
        # to get a connection you can call the connect function of psycopg2
        connection = psycopg2.connect(connect_str)

        # set autocommit option, to do every query when we call it
        connection.autocommit = True

        # create a psycopg2 (client side) cursor that can execute queries
        # to get a cursor you can call the cursor function of a connection
        cursor = connection.cursor()

        # removing the test table if it already exists
        cursor.execute("DROP TABLE IF EXISTS test;")

        # pass data to fill a query placeholders and let Psycopg perform
        # the correct execution (no more SQL injections!) is when you pass the values in a second
        #   paremeter to the execute function
        #cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "First row"))
        #cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "Second row"))

        # query the database and obtain data as Python objects
        cursor.execute("SELECT * FROM answer;")
        data = cursor.fetchall()
        print(data)

        # close communication with the database
        cursor.close()

        return data

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        # checks first whether the connection has been created successfully
        if 'connection' in locals():
            connection.close()


if __name__ == '__main__':
    main()