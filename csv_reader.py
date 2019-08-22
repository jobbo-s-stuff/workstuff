import csv
from fuel_class import FuelEvent
from datetime import datetime


def clean_read_fuel_events(in_filename):
    fuel_events = []
    with open(in_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            # parse row and format data
            date_time_str = row[0] + ' ' + row[1] + ':00'
            date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
            licence_plate = row[2].replace(" ", "")
            plate_fallback = row[3]

            if plate_fallback != '':
                print("Replacing plate " + licence_plate + " with fallback " + plate_fallback + "...")
                licence_plate = plate_fallback

            # append FuelEvent obj to list
            fuel_events.append(FuelEvent(licence_plate, plate_fallback, date_time_obj))

        print("Datetime converted.")
        return sorted(fuel_events, key=lambda x: x.date_time, reverse=False)


def get_min_time(events):
    print("Earliest event is {}".format(events[0].date_time))
    return events[0].date_time


def get_max_time(events):
    print("Latest event is {}".format(events[-1].date_time))
    return events[-1].date_time


def get_plates(events):
    licence_plates = []
    for e in events:
        licence_plates.append(e.licence_plate)
    print("List contains the following licence plates:")
    print(licence_plates)
    return licence_plates
