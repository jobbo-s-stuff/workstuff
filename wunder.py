import requests
import os
from requests.auth import HTTPBasicAuth


def post_vouchers(query_result):
    url = "https://url"
    headers = {'x-api-key': 'key', 'Content-Type': 'application/x-www-form-urlencoded'}
    log_file = get_log_file()

    for row in query_result:
        data = '{"description": "Tanken|' + str(row['starttime']) + '| ' + str(
            row['reservationid']) + '", "customerId":' + str(row['customerid']) + ', "value": 500}'
        req = requests.post(url, data=data, headers=headers)  # post for each dictionary
        print(req.status_code, req.reason, req.content)
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(str(req.content))  # adds to log file

    return url


def get_log_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'example_log.txt')
