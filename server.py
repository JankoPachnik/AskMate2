from flask import Flask, render_template, request, redirect

import connection
import data_manager_answers
import data_manager_questions

# from flask_uploads import UploadSet, configure_uploads, IMAGES
app = Flask(__name__)

# photos = UploadSet('photos', IMAGES)


app.config['UPLOADED_PHOTOS_DEST'] = 'ask-mate-python/static/images'
# configure_uploads(app, photos)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/list')
def list_of_questions():
    questions = data_manager_questions.get_questions()
    return render_template('list.html', questions=questions)


@app.route('/list/sorted/by_date')
def sorted_by_date():
    value = data_manager_questions.checker('submission_time')
    questions = data_manager_questions.sorting_questions("by_date", value)
    connection.write_file(questions, 'ask-mate-python/sample_data/question.csv')
    return redirect("/list")


@app.route('/list/sorted/by_vote')
def sorted_by_vote():
    value = data_manager_questions.checker('vote_number')
    questions = data_manager_questions.sorting_questions("by_vote", value)
    connection.write_file(questions, 'ask-mate-python/sample_data/question.csv')
    return redirect('/list')


@app.route('/show_question/<id>')       #transfers id from list of questions
def show_question(id):
    #data_manager_questions.question_view_count_increase(id)
    question = data_manager_questions.one_question(id)
    answers = data_manager_answers.get_answers_to_question(id)
    return render_template("show_question.html", question=question, answers=answers, id=id)


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
    data_manager_questions.delete_element("question", question_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/delete/<question_id>')  # delete answer
def route_delete_answer(answer_id, question_id):
    data_manager_answers.delete_element("answer", answer_id)
    return redirect('/show_question/' + question_id)


'''@app.route('/list/<id>/down', methods=['GET', 'POST'])
def vote_system_minus(id):
    all_questions = data_manager_questions.get_questions()
    FIRST_INDEX = 0
    for question in all_questions:
        if id == question[FIRST_INDEX]:
            question[3] = int(question[3]) - 1
            data_manager_sql.write_questions(all_questions)
    return redirect('/list')


@app.route('/list/<id>/up', methods=['GET', 'POST'])
def vote_system_plus(id):
    all_answers = data_manager_questions.get_questions()
    for answer in all_answers:
        if id == answer['id']:
            answer['vote_number'] = int(answer['vote_number']) + 1
            connection.write_file(all_answers, 'ask-mate-python/sample_data/question.csv')
    return redirect('/list')'''


'''@app.route('/answer/<answer_id>/vote-down/<question_id>', methods=['GET', 'POST'])
def vote_ask_minus(answer_id, question_id):
    all_answers = data_manager_answers.get_all_answers()
    for answer in all_answers:
        if answer_id == answer['id']:
            answer['vote_number'] = int(answer['vote_number']) - 1
            connection.write_file(all_answers, 'ask-mate-python/sample_data/answer.csv')
    question_id = str(question_id)
    return redirect('/show_question/' + question_id)


@app.route('/answer/<answer_id>/vote-up/<question_id>', methods=['GET', 'POST'])
def vote_ask_plus(answer_id, question_id):
    all_answers = data_manager_answers.get_all_answers()
    for answer in all_answers:
        if answer_id == answer['id']:
            answer['vote_number'] = int(answer['vote_number']) + 1
            connection.write_file(all_answers, 'ask-mate-python/sample_data/answer.csv')
    question_id = str(question_id)
    return redirect('/show_question/' + question_id)'''


@app.route('/show_question/<id>/edit', methods=['POST', 'GET'])
def route_question_edit(id):
    edit = True
    action = '/show_question/' + id + '/edit'
    question = data_manager_answers.one_question(id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['message']
        data_manager_questions.update_question(id, title, description, "question")
        return redirect('/show_question/' + id)
    return render_template('edit.html', edit=edit, question=question, id=id, action=action)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        question_id = request.args.get('question_id', type=str)
        answer_id = request.args.get('answer_id', type=str)

        try:
            filename = photos.save(request.files['photo'])
        except:
            return redirect('/show_question/' + question_id)

        id = answer_id if answer_id else question_id
        file_type = "answer" if answer_id else "question"

        data_manager_questions.update_image(file_type, filename, id)
        return redirect('/show_question/' + question_id)


if __name__ == '__main__':
    app.debug = True
    app.run()