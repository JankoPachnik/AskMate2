import psycopg2


def answer_data():
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

        cursor.execute("SELECT * FROM answer;")
        data = cursor.fetchall()

        data = data_transformation(data)

        cursor.close()

        return data

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        # checks first whether the connection has been created successfully
        if 'connection' in locals():
            connection.close()


def question_data():
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

        cursor.execute("SELECT * FROM question;")
        data = cursor.fetchall()

        data = data_transformation(data)

        cursor.close()

        return data

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        # checks first whether the connection has been created successfully
        if 'connection' in locals():
            connection.close()


def data_transformation(data_from_sql):
    FIRST_INDEX = 0
    keys = data_from_sql[FIRST_INDEX]
    trans_data = []

    for list_of_data in data_from_sql:
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = list_of_data[i]
        trans_data.append(new_dict)

    trans_data.pop(FIRST_INDEX)
    return trans_data


#def write_answers():


#def write_questins():
