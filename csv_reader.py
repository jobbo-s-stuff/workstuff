import csv
import os


def main():
    name = 'example-export'
    filename = get_data_file(name)
    load_file(filename)
    # query_data(data)


def get_data_file(name):
    data = []
    filename = os.path.abspath(os.path.join('.', 'testdata', name + '.csv'))

    if os.path.exists(filename):
        with open(filename) as file_in:
            for entry in file_in.readlines():
                data.append(entry.rstrip())

    return filename


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        data = csv.DictReader(fin)
        for row in data:
            print(row)


def query_data():
    pass


if __name__ == '__main__':
    main()