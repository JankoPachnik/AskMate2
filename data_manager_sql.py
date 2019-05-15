def data_transformation(data_from_sql):
    FIRST_INDEX = 0
    keys = data_from_sql[FIRST_INDEX]
    if "submission_time" not in keys:
        if len(keys) == 6:
            keys = ("id", "submission_time", "vote_number", "question_id", "message", "image")
        else:
            keys = ("id", "submission_time", "view_number", "vote_number", "title", "message", "image")

    trans_data = []

    for list_of_data in data_from_sql:
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = list_of_data[i]
        trans_data.append(new_dict)

    if len(trans_data) == 1:
        trans_data2 = trans_data[0]
        return trans_data2

    trans_data.pop(FIRST_INDEX)
    return trans_data
