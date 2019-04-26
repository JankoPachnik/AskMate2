import csv


def import_data(filename):  # import csv data
    with open(filename, "r") as file:
        imported_data = csv.DictReader(file)
        data = list(imported_data)
        return data


def write_file(dict_list, filename):
    keys = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
    if filename == 'ask-mate-python/sample_data/answer.csv':
        keys = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(dict_list)
