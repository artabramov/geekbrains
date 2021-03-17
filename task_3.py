import json


def load_dict(users_file: str, hobbies_file: str):
    data_in = []

    for file_link in users_file, hobbies_file:
        f = open(file_link, 'r', encoding='utf-8')
        data_in.append(f.read().split('\n'))
        f.close()

    len_1, len_2 = len(data_in[0]), len(data_in[1])
    if len_1 < len_2:
        return 1

    elif len_1 > len_2:
        data_in[1] = data_in[1] + [None] * (len_1 - len_2)

    return dict(zip(data_in[0], data_in[1]))


def save_json(data_out: dict, json_file: str):
    with open(json_file, 'w') as f:
        json.dump(data_out, f)


def load_json(json_file: str):
    with open(json_file, 'r') as f:
        return json.load(f)


save_data = load_dict('c:/_delete/users.csv', 'c:/_delete/hobby.csv')
if save_data != 1:
    save_json(save_data, 'c:/_delete/output.csv')
    load_data = load_json('c:/_delete/output.csv')
    print(load_data)
