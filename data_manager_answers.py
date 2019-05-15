import uuid
from datetime import datetime

import db_connection


def get_all_answers():
    sql_query = """SELECT * FROM answer;"""
    a_list = db_connection.sql_data(sql_query, "read")
    return a_list


def add_answer(form_data, id):
    answer_id = str(uuid.uuid4())
    new_answer = [answer_id, datetime.now(), 0, id, form_data['answer'], None]
    sql_query = """INSERT INTO answer (ID, submission_time, vote_number, question_id, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_answer)


def get_answers_to_question(id_from_question):
    sql_query = """SELECT * FROM answer WHERE question_id = %s;"""
    answers = db_connection.sql_data(sql_query, "read", id_from_question)
    return answers


def delete_answers_element(element_id):
    pass
