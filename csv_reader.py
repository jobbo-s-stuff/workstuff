import os
from csv_convert import CSVToJson


def convert():
    csv_convert = CSVToJson()
    csv_file = open('./testdata/example.csv')

    json_output = csv_convert.start(csv_file, ['date', 'time', 'licencePlate', 'additionalInfo', 'Amount', 'grossPrice'])


