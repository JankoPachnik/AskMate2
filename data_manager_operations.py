import db_connection


def sorting_questions(descending):  #we have to change that
    if descending:
        sql_query = """SELECT * FROM question ORDER BY vote_number DESC ;"""
    else:
        sql_query = """SELECT * FROM question ORDER BY vote_number ASC ;"""
    questions = db_connection.sql_data(sql_query, "read")
    return questions

