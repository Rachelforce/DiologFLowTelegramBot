import json


def is_in_list(new_user, data):
    for user in data:
        if user['id'] == new_user['id']:
            return True
    else:
        return False


def user_save(new_user):
    with open("..\\users.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
    if not is_in_list(new_user, data):
        data.append(new_user)
    with open("..\\users.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)