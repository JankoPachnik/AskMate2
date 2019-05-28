from datetime import datetime
from data_manager import data_manager_user_operations
import db_connection


def add_comment(form_data, id, username=None):
    sql_read = """SELECT * FROM answer WHERE id = %s"""
    answer_row = db_connection.sql_data(sql_read, "read", id)
    for answer in answer_row:
        question_id = answer["question_id"]
    user_id = data_manager_user_operations.check_user_id(username)
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    new_comment = (form_data['comment'], data, 0, id, question_id, user_id[0]['user_id'])
    sql_query = """INSERT INTO comment (message, submission_time, edited_count, answer_id, question_id, user_id) 
    VALUES (%s, %s, %s, %s, %s, %s)"""
    db_connection.sql_data(sql_query, "write", new_comment)


def get_comment_to_answer(question_id):
    sql_query = """SELECT * FROM comment WHERE question_id = %s;"""
    comments = db_connection.sql_data(sql_query, "read", question_id)
    return comments


def delete_comment_element(element_id):
    sql_query_comment = """DELETE FROM comment WHERE id = %s;"""     #dunno if that work
    db_connection.sql_data(sql_query_comment, "write", element_id)


def get_comment_to_user(username=None):
    user_id = data_manager_user_operations.check_user_id(username)
    sql_query = """SELECT * FROM comment WHERE user_id = %s"""
    user_comments = db_connection.sql_data(sql_query, "read", (user_id[0]['user_id'], ))
    return user_comments


