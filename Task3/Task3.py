import json
import sys


def get_json(file_path): # берем данные из json
    with open(file_path, 'r') as file:
        return json.load(file)

def upload_json(file_path, data): # закачиваем данные в json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def fill_values(tests, values_dict): #чекаем и заполняем занч
    for test in tests:
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test: # мини рекурсия, для проверки и заполнения
            fill_values(test['values'], values_dict)
    return tests

if __name__ == '__main__':
    values_path, tests_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]
    values = get_json(values_path)
    tests = get_json(tests_path)
    # мини табл для поиска по id
    values_dict = {value['id']: value['value'] for value in values['values']}
    tests['tests'] = fill_values(tests['tests'], values_dict)
    upload_json(report_path, tests)
