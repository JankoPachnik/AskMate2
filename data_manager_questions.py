import datetime

import db_connection


def get_questions():
    sql_query = """SELECT * FROM question ORDER BY id ASC;"""
    q_list = db_connection.sql_data(sql_query, "read")
    return q_list


def one_question(id_of_question):
    sql_query = """SELECT * FROM question WHERE id=%s;"""
    question = db_connection.sql_data(sql_query, "read", id_of_question)
    return question


def update_question(id, data):
    title = data['title']
    description = data['message']
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
    questions = db_connection.sql_data(sql_read, "read", id)
    for question in questions:
        number_to_increase = question["view_number"] + 1
    data = (number_to_increase, id)
    sql_update = """UPDATE question
        SET view_number = %s
        WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", data)


def new_question(request):
    data = datetime.datetime.now()
    question = (data, "0", "0", request['title'], request["message"], None)
    sql_query = """INSERT INTO question (submission_time, view_number, vote_number, title, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s);"""
    db_connection.sql_data(sql_query, "write", question)


def delete_question_element(element_id):
    sql_query_question = """DELETE FROM question WHERE id = %s;"""
    db_connection.sql_data(sql_query_question, "write", element_id)
    sql_query_answer = """DELETE FROM answer WHERE question_id = %s;"""
    db_connection.sql_data(sql_query_answer, "write", element_id)


def vote_questions_plus(id):
    sql_read = """SELECT * FROM question WHERE id = %s;"""
    questions = db_connection.sql_data(sql_read, "read", id)
    for question in questions:
        data = (question["vote_number"] + 1, id)
    sql_update = """UPDATE question
            SET vote_number = %s
            WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", data)


def vote_questions_minus(id):
    sql_read = """SELECT * FROM question WHERE id = %s;"""
    questions = db_connection.sql_data(sql_read, "read", id)
    for question in questions:
        data = (question["vote_number"] - 1, id)
    sql_update = """UPDATE question
                SET vote_number = %s
                WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", data)

