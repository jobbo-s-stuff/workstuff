import os
import csv_reader
import connect
import wunder


def main():
    in_filename = get_csv_in()
    out_filename = get_csv_out()
    events = csv_reader.clean_read_fuel_events(in_filename)
    #min_fuel_time = get_min_time(events)
    #max_fuel_time = get_max_time(events)
    #licence_plates = get_plates(events)
    #connect.db_query()  # pass timestamps, endtime between earliest and latest fuel timestamp, use lambda,
                        # pass licence plates collection

    # select reservatons that match licence plate and fueltimestamp falls between start and end time
    # convert to API consumable
    #wunder.post_vouchers()


def get_csv_in():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'testdata', 'example_input.csv')


def get_csv_out():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'testdata', 'example_output.csv')


def get_min_time(events):
    min_time = ''
    for e in events:
        if min_time == '':
            min_time = e.date_time
        elif e.date_time < min_time:
            min_time = e.date_time

    print(min_time)
    return min_time


def get_max_time(events):
    # determine maximum timestamp
    # return
    pass


def get_plates(events):
    # create licence plate array
    # return
    pass


def res_match():
    # loop through connect output, compare with csv_reader output
        # match reservation where:
            # licencePlate identical, ignore blank spaces
            # fuelTimeStamp >= startTime and <= endTime
    # pass reservationid, customerid, datetime to list for voucher_convert
    # TODO: maybe again use class (s. csv_reader todo)
    pass


def voucher_convert():
    # loop through list from res_match
    # convert to json
    # TODO: check whether easier and more sensible to convert in post method
    pass


if __name__ == '__main__':
    main()
