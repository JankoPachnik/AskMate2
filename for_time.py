from datetime import datetime

from data_manager import data_manager_questions

data = datetime.now()
data = str(data)
print(type(data))
print(data)

last_id = data_manager_questions.get_questions()
last_id = last_id[-1]['id']
print(type(last_id))
print(last_id)
