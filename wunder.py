import requests

'''
Post to backend API /vouchers endpoint
'''

def post_vouchers(vouchers):
    # loop through list and convert (unless easier to convert to JSON beforehand)
    # post request to /credit-voucher/create
    # request format:
        # "description": "Tanken|dd.MM.yyyy|reservationId"
        # "customerId": int
        # "value": 500
    # create fuel_log_<date>.txt and pass today
    # append successes and failures to fuel_log_<date>.txt:
        # print("Voucher 'creditVoucherId' successfully created for customer 'customerId'.")
        # print("Voucher not created successfully for customer 'customerId'.")
    pass
