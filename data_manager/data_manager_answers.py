from datetime import datetime

import db_connection


def get_all_answers():
    sql_query = """SELECT * FROM answer;""" #selecting list of dicts from sql
    a_list = db_connection.sql_data(sql_query, "read")
    return a_list


def add_answer(form_data, id):
    new_answer = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, id, form_data['message'], None)
    sql_query = """INSERT INTO answer (submission_time, vote_number, question_id, message, image) 
    VALUES (%s, %s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_answer)


def get_answers_to_question(id_from_question):
    sql_query = """SELECT * FROM answer WHERE question_id = %s ORDER BY id ASC;"""
    answers = db_connection.sql_data(sql_query, "read", id_from_question)
    return answers


def delete_answer_element(element_id):  #usuwanie commentarzy do odpowiedzi
    sql_query_answer = """DELETE FROM answer WHERE id = %s;"""
    db_connection.sql_data(sql_query_answer, "write", element_id)
    sql_query_comment = """DELETE FROM comment WHERE answer_id = %s;"""
    db_connection.sql_data(sql_query_comment, "write", element_id)


def vote_answers_plus(id):
    sql_update = """UPDATE answer
                SET vote_number = vote_number + 1
                WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)


def vote_answers_minus(id):
    sql_update = """UPDATE answer
                SET vote_number = vote_number - 1
                WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)
