import requests

#create questions
BASE_URL = 'http://127.0.0.1:8000/api/'

def create_user(data):
    url = BASE_URL + 'users/create-list/'
    response = requests.post(url, json=data)
    return response.json()

# data = {
#     "user_id": "123",
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "john_doe"
# }
# print(create_user(data))
    
def get_user(user_id):
    url = BASE_URL + 'users/update-delete/' + user_id + '/'
    response = requests.get(url)
    return response.json()

# print(get_user('123'))



def update_user(user_id, data):
    url = BASE_URL + 'users/update-delete/' + user_id + '/'
    response = requests.put(url, json=data)
    return response.json()

data = {
    "user_id": "123456", # "1234dert
    "first_name": "Johon",
    "last_name": "Doe",
    "username": "john_doe"
    }
print(update_user('123', data))   



def create_question(data):
    url = BASE_URL + 'questions/create/'
    response = requests.post(url, json=data)
    return response.json()
    
    
# data = {
#     "user": "21212",
#     "code": "1234dddddert",
#     "subject": "matem",
#     "description": "prosta",
#     "answers": "{'1':'a','2':'a','3':'a','4':'d'}",
#     "file": None,
#     "size": 4,
#     "start_time": "2024-02-09T02:01:43Z"
# }
# print(create_question(data))


