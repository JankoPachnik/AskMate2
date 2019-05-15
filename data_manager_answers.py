from datetime import datetime

import db_connection


def get_all_answers():
    sql_query = """SELECT * FROM answer;"""
    a_list = db_connection.sql_data(sql_query, "read")
    return a_list


def add_answer(form_data, id):
    new_answer = (datetime.now(), 0, id, form_data['answer'], None)
    sql_query = """INSERT INTO answer (submission_time, vote_number, question_id, message, image) 
    VALUES (%s, %s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_answer)


def get_answers_to_question(id_from_question):
    sql_query = """SELECT * FROM answer WHERE question_id = %s;"""
    answers = db_connection.sql_data(sql_query, "read", id_from_question)
    return answers


def delete_answer_element(element_id):
    sql_query_answer = """DELETE FROM answer WHERE id = %s;"""
    db_connection.sql_data(sql_query_answer, "write", element_id)


def vote_answers_plus(id):
    sql_read = """SELECT * FROM answer WHERE id = %s;"""
    answers = db_connection.sql_data(sql_read, "read", id)
    for answer in answers:
        data = (answer["vote_number"] + 1, id)
    sql_update = """UPDATE answer
                SET vote_number = %s
                WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", data)


def vote_answers_minus(id):
    sql_read = """SELECT * FROM answer WHERE id = %s;"""
    answers = db_connection.sql_data(sql_read, "read", id)
    for answer in answers:
        data = (answer["vote_number"] - 1, id)
    sql_update = """UPDATE answer
                  SET vote_number = %s
                  WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", data)
