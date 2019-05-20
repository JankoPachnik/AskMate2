from flask import Flask, render_template, request, redirect

import data_manager_answers
import data_manager_questions
import data_manager_comment
import data_manager_operations

app = Flask(__name__)


app.config['UPLOADED_PHOTOS_DEST'] = 'ask-mate-python/static/images'


@app.route('/')
def main_page():
    newest_question = data_manager_questions.newest_question()
    best_question = data_manager_questions.best_questions()
    return render_template("index.html", newest_question=newest_question, best_question=best_question)


@app.route('/list')
def list_of_questions():
    questions = data_manager_questions.get_questions()
    return render_template('list.html', questions=questions)


@app.route('/list/sorted/by_date')
def sorted_by_date():
    questions = data_manager_questions.sort_time()
    return render_template('list.html', questions=questions)

#tet

@app.route('/list/sorted/by_vote')
def sorted_by_vote():
    questions = data_manager_questions.sort_vote()
    return render_template('list.html', questions=questions)


@app.route('/show_question/<id>')       #dodanie wyswietlania commentarzy
def show_question(id):
    data_manager_questions.question_view_count_increase(id)
    question_one = data_manager_questions.one_question(id)
    answers = data_manager_answers.get_answers_to_question(id)
    comments = data_manager_comment.get_comment_to_answer(id)
    return render_template("show_question.html", questions=question_one, answers=answers, comments=comments, id=id)


@app.route('/add_comment/<id>', methods=['GET', 'POST'])
def add_comment(id):
    data = request.form
    if request.method == 'POST':
        data_manager_comment.add_comment(data, id)
        question_id = data_manager_operations.get_question_id(id)
        return redirect('/show_question/' + question_id)     #trzea naprawic id
    return render_template('add_comment.html', id=id)


@app.route('/question/<id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        data_manager_answers.add_answer(request.form, id)
        return redirect('/show_question/' + id)
    return render_template('answer.html', id=id)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    return render_template("add.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.form
    if request.method == 'POST':
        data_manager_questions.new_question(data)
    else:
        return render_template('add.html')
    return redirect('/list')


@app.route('/question/<question_id>/delete')  # delete question
def route_delete_question(question_id):
    data_manager_questions.delete_question_element(question_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/delete/<question_id>')  # delete answer
def route_delete_answer(answer_id, question_id):
    data_manager_answers.delete_answer_element(answer_id)
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
    return render_template('edit.html', questions=questions)


if __name__ == '__main__':
    app.debug = True
    app.run()