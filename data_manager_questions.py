import datetime

import data_manager_operations
import db_connection


def get_questions():
    sql_query = """SELECT * FROM question;"""
    q_list = db_connection.sql_data(sql_query, "read")
    return q_list


def one_question(id_of_question):
    sql_query = """SELECT * FROM question WHERE id = %s;"""
    question = db_connection.sql_data(sql_query, "read", id_of_question)
    return question


def update_question(id, title, description):   #do zrobienia od nowa
    sql_query = """UPDATE question
        SET title = %s, message = %s
        WHERE id = %s;"""
    question = [title, description, id]
    db_connection.sql_data(sql_query, "update", question)


def newest_question():
    sql_query = """SELECT * FROM question ORDER BY submission_time DESC LIMIT 1;"""
    question = db_connection.sql_data(sql_query, "read")
    return question


def question_view_count_increase(id):
    sql_read = """SELECT * FROM question WHERE id = %s;"""
    question = db_connection.sql_data(sql_read, "read", id)
    question["id"] = int(question["id"]) + 1
    sql_update = """UPDATE question
        SET view_number = %s
        WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)


def new_question(request):
    data = datetime.datetime.now()
    data = str(data)
    id = str(data_manager_operations.generate_user_id())
    question = (id, data, "0", "0", request['title'], request["message"], "NULL")
    sql_query = """INSERT INTO question (ID, submission_time, view_number, vote_number, title, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    db_connection.sql_data(sql_query, "write", question)


def delete_question_element(element_id):
    '''
    kasuje tylko odpowiedz (opcja dodania też usó∑ania komentów)
    '''

