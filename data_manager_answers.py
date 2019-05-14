import db_connection
import connection
import uuid
from datetime import datetime


def get_all_answers():
    a_list = db_connection.answer_data()

    return a_list


def add_answer(form_data, id):
    answers = connection.import_data('ask-mate-python/sample_data/answer.csv')
    new_answer = {
        'id': uuid.uuid4(),
        'submission_time': datetime.now(),
        'vote_number': 0,
        'question_id': id,
        'message': form_data['answer'],
        'image': None
    }
    answers.append(new_answer)
    connection.write_file(answers, 'ask-mate-python/sample_data/answer.csv')


def get_answers_to_question(id):
    id = id
    answers = get_all_answers()
    filtered_answers = []
    for answer in answers:
        if answer['question_id'] == id:
            filtered_answers.append(answer)
    return filtered_answers

