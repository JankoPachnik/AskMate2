import random
import string

import db_connection


def sorting_questions(descending):
    if descending:
        sql_query = """SELECT * FROM question ORDER BY vote_number DESC ;"""
    else:
        sql_query = """SELECT * FROM question ORDER BY vote_number ASC ;"""
    questions = db_connection.sql_data(sql_query, "read")
    return questions


def generate_user_id():
    unique_id = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(unique_id) for i in range(9))
    unique_id = str(unique_id)
    return unique_id
