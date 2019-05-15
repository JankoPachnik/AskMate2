import db_connection


#def delete_element(element_type, element_id):          #to trzeba zrobic od nowa


def sorting_questions(descending):
    if descending:
        sql_query = """SELECT * FROM question ORDER BY vote_number DESC ;"""
    else:
        sql_query = """SELECT * FROM question ORDER BY vote_number ASC ;"""
    questions = db_connection.sql_data(sql_query, "read")
    return questions
