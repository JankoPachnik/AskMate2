from datetime import datetime

import db_connection


def add_comment(form_data, id):
    sql_read = """SELECT * FROM answer WHERE id = %s"""
    answer_row = db_connection.sql_data(sql_read, "read", id)
    for answer in answer_row:
        question_id = answer["question_id"]
    new_comment = (form_data['comment'], datetime.now(), 0, id, question_id)
    sql_query = """INSERT INTO comment (message, submission_time, edited_count, answer_id, question_id) 
    VALUES (%s, %s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_comment)


def get_comment_to_answer(id_from_answer):
    sql_query = """SELECT * FROM comment WHERE answer_id = %s;"""
    comments = db_connection.sql_data(sql_query, "read", id_from_answer)
    return comments


def delete_comment_element(element_id):
    sql_query_comment = """DELETE FROM comment WHERE id = %s;"""     #dunno if that works
    db_connection.sql_data(sql_query_comment, "write", element_id)



