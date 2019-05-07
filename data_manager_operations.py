import connection
import data_manager_questions


def delete_element(element_type, element_id):
    # delete file if exists
    data = connection.import_data(f'ask-mate-python/sample_data/{element_type}.csv')
    try:
        deleted_element_img_path = [element['image'] for element in data if element['id'] == element_id][0]
        file_name = deleted_element_img_path.split("/")[1]
    except IndexError:
        pass

    # delete element
    updated_data = [data_element for data_element in data if data_element['id'] != element_id]
    connection.write_file(updated_data, f'ask-mate-python/sample_data/{element_type}.csv')

    if element_type == "question":
        answers = connection.import_data('ask-mate-python/sample_data/answer.csv')

        # delete answer's image
        img_paths_of_deleted_answers = [answer['image'] for answer in answers if answer['question_id'] == element_id]

        # delete answer
        updated_answers = [answer for answer in answers if answer['question_id'] != element_id]
        connection.write_file(updated_answers, 'ask-mate-python/sample_data/answer.csv')


def sorting_questions(filter, descending):
    questions = data_manager_questions.get_questions()
    sorting_key = 'vote_number'
    if filter == "by_date":
        sorting_key = 'submission_time'
    return sorted(questions, key=lambda i: i[sorting_key], reverse=descending)


def checker(type):
    questions = data_manager_questions.get_questions()
    if type == 'submission_time':
        return True if questions[0][type] < questions[-1][type] else False
    else:
        return True if int(questions[0][type]) < int(questions[-1][type]) else False


def question_view_count_increase(id):
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            question['view_number'] = str(int(question['view_number']) + 1)
    connection.write_file(questions, 'ask-mate-python/sample_data/question.csv')


def update_image(file_type, filename, id):
    data = connection.import_data(f"ask-mate-python/sample_data/{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['image'] = '/static/images/' + filename
    connection.write_file(data, f"ask-mate-python/sample_data/{file_type}.csv")