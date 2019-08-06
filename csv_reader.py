import csv
import os
import json


def main():
    name = 'example-export-reduced'
    filename = get_data_file(name)
    load_file(filename)
    # query_data(data)


def get_data_file(name):
    data = []
    filename = os.path.abspath(os.path.join('.', 'testdata', name + '.csv'))

    return filename


def load_file(filename):
    #TODO fix output
    file = open(filename, 'r', newline='', encoding='utf-8')
    reader = csv.DictReader(file, fieldnames= ('date','time','licencePlate','additionalInfo','amount','grossPrice'))
    out = json.dumps([row for row in reader])
    print('Json parsed!')
    name = 'examplejson'
    file = open(os.path.abspath(os.path.join('.', 'testdata', name + '.json')),'w')
    file.write(out)
    print('Json saved!')


def query_data():
    pass


if __name__ == '__main__':
    main()