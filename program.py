import csv_reader
import connect
import wunder


def main():
    csv_reader.convert()
    csv_to_db()
    connect.db_query()  # pass timestamps, endtime between earliest and latest fuel timestamp, use lambda,
                        # pass licence plates collection

    # select reservatons that match licence plate and fueltimestamp falls between start and end time
    # convert to API consumable
    wunder.post_vouchers()


def csv_to_db():
    # TODO: probably easier to pass directly from csv_reader to connect
    # check csv_reader's output for min and max fuel timestamp
    # grab licence plates from csv_reader's output
    # pass to connect
    pass


def res_match():
    # loop through connect output, compare with csv_reader output
        # match reservation where:
            # licencePlate identical
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
