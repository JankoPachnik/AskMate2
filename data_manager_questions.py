import connection
import data_manager_operations


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
