def data_transformation(data_from_sql):
    if data_from_sql:
        if len(data_from_sql[0]) == 6:
            keys = ("id", "submission_time", "vote_number", "question_id", "message", "image")
        elif len(data_from_sql[0]) == 7:
            keys = ("id", "submission_time", "view_number", "vote_number", "title", "message", "image")
        elif len(data_from_sql[0]) == 2:
            keys = ("id", "name")

        trans_data = []
        for list_of_data in data_from_sql:
            new_dict = {}
            for i in range(len(keys)):
                new_dict[keys[i]] = list_of_data[i]
            trans_data.append(new_dict)
        return trans_data
    pass
