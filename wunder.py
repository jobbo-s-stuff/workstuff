import requests
from requests.auth import HTTPBasicAuth

# TODO: create fake data set for testing

# data = '{"description": "Test|16.08.2019|771", "customerId": "89", "value": "500"}'

def post_vouchers(query_result):
    url = "https://url/rest/credit-voucher/create"
    headers = {'x-api-key': 'key', 'Content-Type': 'application/x-www-form-urlencoded' }
    # req = requests.post(url, data=data, headers=headers)
    # print(req.status_code, req.reason, req._content)

    # loop through list and convert (unless easier to convert to JSON beforehand)
    for row in query_result:
        data = '{"description": "Tanken|' + row['starttime'] + '| ' + row['reservationid']+ ', "customerId":' + row['customerid'] + ', "value": "500"}'
        req = requests.post(url, data= data, headers = headers)
        print(req.status_code, req.reason, req._content) 

    # post request to /credit-voucher/create
    # request format:
    # "description": "Tanken|dd.MM.yyyy|reservationId"
    # "customerId": int
    # "value": 500
    # create fuel_log_<date>.txt and pass today
    # append successes and failures to fuel_log_<date>.txt:
    # print("Voucher 'creditVoucherId' successfully created for customer 'customerId'.")
    # print("Voucher not created successfully for customer 'customerId'.")
    return url