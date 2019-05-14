import connection
import data_manager_operations
import uuid
import datetime


def get_questions():
    q_list = connection.import_data('ask-mate-python/sample_data/question.csv')
    return q_list


def one_question(id):
    questions = get_questions()
    for question in questions:
        if question['id'] == id:
            return question


def update_question(id, title, description, file_type):
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            question['title'] = title
            question['message'] = description
    connection.write_file(questions, f"ask-mate-python/sample_data/{file_type}.csv")


def newest_question():
    new_question = []
    sorted_questions = data_manager_operations.sorting_questions("by_date", True)
    new_question.append(sorted_questions[0])
    return new_question


def question_view_count_increase(id):
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            question['view_number'] = str(int(question['view_number']) + 1)
    connection.write_file(questions, 'ask-mate-python/sample_data/question.csv')


def new_question(request):
    data = datetime.now()
    data = str(data)

    new_question = {
        'id': uuid.uuid4(),
        'submission_time': data,
        'view_number': 0,
        'vote_number': 0,
        'title': request.form['title'],
        'message': request.form["message"],
        'image': None
    }
    new_data = get_questions()
    new_data.append(new_question)
    return new_data

