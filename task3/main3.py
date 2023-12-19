import argparse
import json

parser = argparse.ArgumentParser(description='Filling new file')
parser.add_argument('tests_path', type=str, help='path to the file with tests')
parser.add_argument('values_path', type=str, help='path to the file with values')
args = parser.parse_args()

with open(args.tests_path, 'r') as file:
    tests = json.load(file)
with open(args.values_path, 'r') as file1:
    values = json.load(file1)

report = tests
print(tests['tests'])

def setvals(a: dict, b: dict) -> dict:
    for test in a:
        for value in b['values']:
            if test['id'] == value['id']:
                test['value'] = value['value']
                print(test['value'])
        if test.keys().__contains__('values'):
            setvals(test['values'], b)

setvals(tests['tests'], values)
print(tests['tests'])

report = {'tests': tests['tests']}

with open('report.json', 'w') as file2:
    json.dump(report, file2, indent=2)


