import csv_reader
import connect


def main():
    csv_reader.convert()
    # merge date/time
    # take min/max timestamps for endTime (/reservations)
    connect.db_query()
    # match plates from db_query() with plates from convert()
    # check against timestamps
    # convert to API consumable
    # loop: wunder.post_vouchers


def time_frame():
    pass
    # this checks output_json for highest and lowest timestamp


def plate_match():
    pass
    # this matches plates from query to plates from output_json


def res_match():
    pass
    # this matches reservations start/end to specific fueling events


def voucher_convert():
    pass
    # this converts json to loopable payloads for post_vouchers


if __name__ == '__main__':
    main()
