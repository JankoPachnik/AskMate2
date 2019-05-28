import db_connection
import bcrypt


def register(data):
    credentials = (data["username"], data["email"], hash_password(data['password']))
    sql_query = """INSERT INTO credentials(user_login, user_email, user_password)
    VALUES (%s, %s, %s);"""
    db_connection.sql_data(sql_query, "write", credentials)


def verify_login(data):
    sql_query = """SELECT user_login, user_password FROM credentials WHERE user_login = %s"""
    login_and_password = db_connection.sql_data(sql_query, "read", (data["username"],))
    if login_and_password:
        if verify_password(data["password"], login_and_password[0]["user_password"]):
            return 0
        return 1
    return 1


def get_email_and_reputation(username=None):
    sql_query = """SELECT user_email, user_reputation FROM credentials WHERE user_login = %s"""
    info = db_connection.sql_data(sql_query, "read", (username, ))
    return info


def check_user_id(username):
    sql_query = """SELECT user_id FROM credentials WHERE user_login = %s"""
    user_id = db_connection.sql_data(sql_query, "read", (username, ))
    return user_id


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def verify_credentials(data):
    if verify_username(data["username"]):
        return "username taken"
    if verify_email(data["email"]):
        return "email taken"


def verify_username(data):
    sql_query = """SELECT user_id FROM credentials WHERE user_login = %s"""
    login_check = db_connection.sql_data(sql_query, "read", (data,))
    if login_check:
        return "login taken"
    return None


def verify_email(data):
    sql_query = """SELECT user_id FROM credentials WHERE user_email = %s"""
    email_check = db_connection.sql_data(sql_query, "read", (data,))
    if email_check:
        return "email taken"
    return None

