import os
import csv_reader
import connect
import wunder
from psycopg2.extras import RealDictRow


def main():
    in_filename = get_csv_in()  # identify input csv
    events = csv_reader.clean_read_fuel_events(in_filename)  # cleans csv and returns rows as events
    print()
    print('CSV read. Continue? (Y/N)')
    step = input()
    if step == 'Y':
        min_fuel_time = csv_reader.get_min_time(events)  # returns earliest timestamp
        max_fuel_time = csv_reader.get_max_time(events)  # returns latest timestamp
    elif step == 'N':
        exit()
    print()
    print('Timeframe identified. Continue? (Y/N)')
    step = input()
    if step == 'Y':
        licence_plates = csv_reader.get_plates(events)  # finds and replaces plates with backup where necessary
    elif step == 'N':
        exit()
    print()
    print('Licence Plates corrected. Continue? (Y/N)')
    step = input()
    if step == 'Y':
        query_result = connect.db_query(min_fuel_time, max_fuel_time, licence_plates) # passes data to db query
        if len(query_result) > len(events): # in case of missing fuel events
            raise ValueError('Query result does not match fuel events')
    elif step == 'N':
        exit()
    print()
    print('Query data prepared. Continue? (Y/N)')
    if step == 'Y':
        # wunder.post_vouchers(query_result)  # loops through query results to create vouchers
        exit()
    elif step == 'N':
        exit()


def get_csv_in():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'export-cleaned.csv')


def get_csv_out():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'testdata', 'example_output.csv')


if __name__ == '__main__':
    main()
