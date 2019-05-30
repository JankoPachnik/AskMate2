import db_connection


def get_tags_to_question(question_id):
    sql_query = """SELECT name FROM tag INNER JOIN question_tag qt on tag.id = qt.tag_id 
    WHERE question_id = %s"""
    tags_to_question = db_connection.sql_data(sql_query, "read", (question_id, ))
    return tags_to_question


def new_tags(tags):
    tags = tags.split(',')
    sql_query = """INSERT INTO tag (name) VALUES (%s);"""
    db_connection.sql_data(sql_query, "write", (tags, ))
    pass
