import datetime
import db_connection
from data_manager import data_manager_user_operations


def get_questions():
    sql_query = """SELECT * FROM question ORDER BY id ASC;"""   #selecting lisr of dicts from sql
    q_list = db_connection.sql_data(sql_query, "read")
    print(q_list)
    return q_list


def get_questions_to_user(user_id):
    user_id = data_manager_user_operations.check_user_id(user_id)
    sql_query = """SELECT * FROM question WHERE user_id = %s ORDER BY id ASC"""
    user_questions = db_connection.sql_data(sql_query, "read", (user_id[0]['user_id'], ))
    return user_questions


def get_tags():
    sql_query = """SELECT * FROM tag ORDER BY id ASC;"""
    tags_list = db_connection.sql_data(sql_query, "read")
    return tags_list


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


def newest_questions():
    sql_query = """SELECT * FROM question ORDER BY submission_time DESC LIMIT 5;"""
    questions = db_connection.sql_data(sql_query, "read")
    return questions


def hottest_questions():
    sql_query = """SELECT * FROM question ORDER BY view_number DESC LIMIT 5"""
    questions = db_connection.sql_data(sql_query, "read")
    return questions


def question_view_count_increase(id):
    sql_update = """UPDATE question
        SET view_number = view_number + 1
        WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)


def new_question(request, username=None):
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = data_manager_user_operations.check_user_id(username)
    question = (data, "0", "0", request['title'], request["message"], None, username[0]['user_id'])
    sql_query = """INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    db_connection.sql_data(sql_query, "write", question)


def delete_question_element(element_id):
    sql_query_question = """DELETE FROM question WHERE id = %s;"""
    db_connection.sql_data(sql_query_question, "write", element_id)
    sql_query_answer = """DELETE FROM answer WHERE question_id = %s;"""
    db_connection.sql_data(sql_query_answer, "write", element_id)
    sql_query_comment = """DELETE FROM comment WHERE question_id = %s;"""
    db_connection.sql_data(sql_query_comment, "write", element_id)


def vote_questions_plus(id):
    sql_update = """UPDATE question
            SET vote_number = vote_number + 1
            WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)


def vote_questions_minus(id):
    sql_update = """UPDATE question
                SET vote_number = vote_number - 1
                WHERE id = %s;"""
    db_connection.sql_data(sql_update, "update", id)


def best_questions():
    sql_read = """SELECT * FROM question ORDER BY vote_number DESC LIMIT 1;"""
    question = db_connection.sql_data(sql_read, "read")
    return question


def sort_vote():
    sql_read = """SELECT * FROM question ORDER BY vote_number DESC"""
    questions = db_connection.sql_data(sql_read, "read")
    return questions


def sort_time():
    sql_read = """SELECT * FROM question ORDER BY submission_time DESC"""
    questions = db_connection.sql_data(sql_read, "read")
    return questions


def sort_view():
    sql_read = """SELECT * FROM question ORDER BY view_number DESC"""
    questions = db_connection.sql_data(sql_read, "read")
    return questions


def add_new_tag(question_id, tag_id, tag_name):
    new_tag = tag_name
    sql_query = """INSERT INTO tag (name) VALUES (%s);"""
    db_connection.sql_data(sql_query, "write", new_tag)

    tag = (question_id, tag_id)
    sql_query = """INSERT INTO question_tag (question_id, tag_id) VALUES (%s, %s);"""
    db_connection.sql_data(sql_query, "write", tag)


def add_tag(question_id, tag_id):
    tag = (question_id, tag_id)
    sql_query = """INSERT INTO question_tag (question_id, tag_id) VALUES (%s, %s);"""
    db_connection.sql_data(sql_query, "write", tag)