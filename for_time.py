from datetime import datetime

import data_manager

data = datetime.now()
data = str(data)
print(type(data))
print(data)

last_id = data_manager.get_questions()
last_id = last_id[-1]['id']
print(type(last_id))
print(last_id)
