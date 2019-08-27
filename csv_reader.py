import csv
from fuel_class import FuelEvent
from datetime import datetime


def clean_read_fuel_events(in_filename):
    fuel_events = []  # list that holds fuel_event objects
    with open(in_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            date_time_str = row[0] + ' ' + row[1] + ':00'  # merge date and time columns
            date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')  # reformat date_time
            clean_date_time = datetime.strftime(date_time_obj, '%Y-%m-%d %H:%M:%S')
            licence_plate = row[2].replace(" ", "")  # removes blanks from licence plates
            plate_fallback = row[3]

            if plate_fallback != '':
                licence_plate = plate_fallback

            fuel_events.append(FuelEvent(licence_plate, plate_fallback, date_time_obj))  # create list per object
            print(row)

        return sorted(fuel_events, key=lambda x: x.date_time, reverse=False)  # sorts fuel_events by time


def get_min_time(events):
    print('Earliest event is ' + str(events[0].date_time))
    return events[0].date_time  # returns first listed date_time


def get_max_time(events):
    print('Latest event is ' + str(events[-1].date_time))
    return events[-1].date_time  # returns last listed date_time


def get_plates(events):
    licence_plates = []
    for e in events:
        licence_plates.append(e.licence_plate)  # adds licence_plates to list for query
        print(e)
    return licence_plates
