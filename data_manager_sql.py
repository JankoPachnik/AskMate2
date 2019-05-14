import psycopg2


def data_transformation(data_from_sql):
    FIRST_INDEX = 0
    keys = data_from_sql[FIRST_INDEX]
    trans_data = []

    for list_of_data in data_from_sql:
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = list_of_data[i]
        trans_data.append(new_dict)

    trans_data.pop(FIRST_INDEX)
    return trans_data


#def write_answers(data):


#def write_questins(data):