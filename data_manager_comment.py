from datetime import datetime

import db_connection


def add_comment(form_data, answer_id):
    new_comment = (form_data['comment'], datetime.now(), 0, answer_id, )
    sql_query = """INSERT INTO comment (message, submission_time, edited_count,  answer_id,) 
    VALUES (%s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_comment)


def get_comment_to_answer(id_from_answer):
    sql_query = """SELECT * FROM comment WHERE answer_id = %s;"""
    comments = db_connection.sql_data(sql_query, "read", id_from_answer)
    return comments


def delete_comment_element(element_id):
    sql_query_comment = """DELETE FROM comment WHERE id = %s;"""
    db_connection.sql_data(sql_query_comment, "write", element_id)



