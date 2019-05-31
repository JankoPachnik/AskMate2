#!/usr/bin/env


from flask import Flask, render_template, request, redirect, session, escape
import flask_login
from data_manager import data_manager_questions, data_manager_comment, data_manager_answers, data_manager_operations, data_manager_user_operations

app = Flask(__name__)

app.config['UPLOADED_PHOTOS_DEST'] = 'ask-mate-python/static/images'
app.secret_key = 'ptaki lataja kluczem'

login_manager = flask_login.LoginManager()

login_manager.init_app(app)


@app.route('/')
def main_page():
    login = None
    if 'username' in session:
        login = session['username']
    newest_questions = data_manager_questions.newest_questions()
    return render_template("index.html", newest_questions=newest_questions, login=login)


@app.route('/list')
def list_of_questions():
    questions = data_manager_questions.get_questions()
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('list.html', questions=questions, login=login)


@app.route('/list/sorted/by_date')
def sorted_by_date():
    questions = data_manager_questions.sort_time()
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('list.html', questions=questions, login=login)


@app.route('/list/sorted/by_view')
def sorted_by_view():
    questions = data_manager_questions.sort_view()
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('list.html', questions=questions, login=login)


@app.route('/list/sorted/by_vote')
def sorted_by_vote():
    questions = data_manager_questions.sort_vote()
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('list.html', questions=questions, login=login)


@app.route('/show_question/<id>')       #dodanie wyswietlania commentarzy
def show_question(id):
    data_manager_questions.question_view_count_increase(id)
    question_one = data_manager_questions.one_question(id)
    answers = data_manager_answers.get_answers_to_question(id)
    comments = data_manager_comment.get_comment_to_answer(id)
    login = None
    if 'username' in session:
        login = session['username']
    return render_template("show_question.html", question=question_one, answers=answers, comments=comments, id=id, login=login)


@app.route('/add_comment/<id>', methods=['GET', 'POST'])
def add_comment(id):
    data = request.form
    login = None
    if 'username' in session:
        login = session['username']
    if request.method == 'POST':
        data_manager_comment.add_comment(data, id, session['username'])
        question_id = data_manager_operations.get_question_id(id)
        return redirect('/show_question/' + question_id)     #trzea naprawic id
    return render_template('add_comment.html', id=id, login=login)


@app.route('/question/<id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        if "username" in session:
            data_manager_answers.add_answer(request.form, id, session["username"])
            return redirect('/show_question/' + id)
        else:
            data_manager_answers.add_answer(request.form, id)
            return redirect('/show_question/' + id)
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('answer.html', id=id, login=login)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add_question', methods=['GET', 'POST'])
def add():
    data = request.form
    if request.method == 'POST':
        if 'username' in session:
            data_manager_questions.new_question(data, session['username'])
        else:
            data_manager_questions.new_question(data)
    else:
        login = None
        if 'username' in session:
            login = session['username']
        return render_template('add.html', login=login)
    return redirect('/list')


@app.route('/question/<question_id>/delete')  # delete question
def route_delete_question(question_id):
    data_manager_questions.delete_question_element(question_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/delete/<question_id>')  # delete answer
def route_delete_answer(answer_id, question_id):
    data_manager_answers.delete_answer_element(answer_id)
    return redirect('/show_question/' + question_id)


@app.route('/comment/<comment_id>/delete/<question_id>')  # delete comment
def route_delete_comment(comment_id, question_id):
    data_manager_comment.delete_comment_element(comment_id)
    return redirect('/show_question/' + question_id)


@app.route('/list/<id>/down', methods=['GET', 'POST'])
def vote_system_minus(id):
    data_manager_questions.vote_questions_minus(id)
    return redirect('/list')


@app.route('/list/<id>/up', methods=['GET', 'POST'])
def vote_system_plus(id):
    data_manager_questions.vote_questions_plus(id)
    return redirect('/list')


@app.route('/answer/<answer_id>/vote-down/<question_id>', methods=['GET', 'POST'])
def vote_ask_minus(answer_id, question_id):
    data_manager_answers.vote_answers_minus(answer_id)
    return redirect('/show_question/' + question_id)


@app.route('/answer/<answer_id>/vote-up/<question_id>', methods=['GET', 'POST'])
def vote_ask_plus(answer_id, question_id):
    data_manager_answers.vote_answers_plus(answer_id)
    return redirect('/show_question/' + question_id)


@app.route('/show_question/<id>/edit', methods=['POST', 'GET'])
def route_question_edit(id):
    questions = data_manager_questions.one_question(id)
    data = request.form
    if request.method == 'POST':
        data_manager_questions.update_question(id, data)
        return redirect('/show_question/' + id)
    login = None
    if 'username' in session:
        login = session['username']
    return render_template('edit.html', questions=questions, login=login)


@app.route('/add-tag/<tag_id>/new/<question_id>', methods=['POST', 'GET'])
def add_new_tag(tag_id, question_id, tag_name):
    data_manager_questions.add_new_tag(tag_id, question_id, tag_name)
    return render_template('/show_question/' + question_id)


@app.route('/add-tag/<tag_id>/new/<question_id>', methods=['POST', 'GET'])
def add_tag(tag_id, question_id):
    data_manager_questions.add_tag(tag_id, question_id)
    return render_template('/show_question/' + question_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect('/my_page')
    else:
        if request.method == 'POST':
            data = request.form
            if data_manager_user_operations.verify_login(data):
                return render_template("login.html", message="Oops login or password is not correct")
            else:
                session['username'] = request.form['username']
                return redirect('/my_page')
    return render_template("login.html")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username')
    session.pop('email')
    session.pop('reputation')
    return redirect('/login')


@app.route('/register', methods=['POST', 'GET'])
def register():
    data = request.form
    if request.method == 'POST':
        if data_manager_user_operations.verify_credentials(data):
            return render_template("register.html", message=data_manager_user_operations.verify_credentials(data))
        else:
            data_manager_user_operations.register(data)
            session['username'] = request.form['username']
            session['email'] = request.form['email']
            return redirect('/my_page')
    return render_template("register.html")


@app.route('/my_page')
def my_page():
    if 'username' in session:
        data_manager_user_operations.reputation_update(session['username'])
        info = data_manager_user_operations.get_email_and_reputation(session['username'])
        session['email'] = info[0]['user_email']
        session['reputation'] = info[0]['user_reputation']
        user_questions = data_manager_questions.get_questions_to_user(session["username"])
        return render_template("my_page_extend.html", username=session['username'], email=session['email'], reputation=session['reputation'], user_questions=user_questions)
    return redirect("login.html")


@app.route('/my_page/answers')
def my_page_answers():
    if 'username' in session:
        user_answers = data_manager_answers.get_answers_to_user(session["username"])
        return render_template("my_page_extend_answers.html", username=session['username'], email=session['email'], reputation=session['reputation'], user_answers=user_answers)
    return redirect("login.html")


@app.route('/ranking')
def ranking():
    users_info = data_manager_user_operations.get_user_info()
    login = None
    if 'username' in session:
        login = session['username']
    return render_template("ranking.html", users_info=users_info, login=login)


@app.route('/my_page/comment')
def my_page_comment():
    if 'username' in session:
        user_comments = data_manager_comment.get_comment_to_user(session["username"])
        return render_template("my_page_extend_comments.html", username=session['username'], email=session['email'], reputation=session['reputation'], user_comments=user_comments)
    return redirect("login.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
