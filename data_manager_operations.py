import db_connection


def get_question_id(answer_id):
    sql_query = """SELECT * FROM answer WHERE id = %s"""
    answers = db_connection.sql_data(sql_query, "read", answer_id)
    for answer in answers:
        question_id = str(answer['question_id'])
    return question_id


