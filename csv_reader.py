from csv_convert import CSVToJson

'''
Opens csv from path, reads it and converts it to json
'''


def convert():
    csv_convert = CSVToJson()
    csv_file = open('./testdata/example.csv')
    print('Parsing CSV...')
    json_output = csv_convert.start(csv_file, ['date',
                                               'time',
                                               'licencePlate',
                                               'additionalInfo',
                                               'Amount',
                                               'grossPrice'])

    print('Converted to JSON.')
