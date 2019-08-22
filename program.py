import os
import csv_reader
import connect
import wunder


def main():
    in_filename = get_csv_in()
    out_filename = get_csv_out()
    events = csv_reader.clean_read_fuel_events(in_filename)
    # for event in events:
    #     print(event)
    min_fuel_time = csv_reader.get_min_time(events)
    max_fuel_time = csv_reader.get_max_time(events)
    licence_plates = csv_reader.get_plates(events)
    query_result = connect.db_query(min_fuel_time, max_fuel_time, licence_plates) 
    # select reservatons that match licence plate and fueltimestamp falls between start and end time
    # convert to API consumable
    if len(query_result) > len(events):
        raise ValueError('Query result does not match tank events')
    else:
        wunder.post_vouchers(query_result)


def get_csv_in():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'testdata', 'example_input.csv')


def get_csv_out():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'testdata', 'example_output.csv')


if __name__ == '__main__':
    main()
