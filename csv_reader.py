import csv
from fuel_class import FuelEvent
import datetime


def clean_read_fuel_events(in_filename):
    fuel_events = []
    with open(in_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # parse row wnd format data
            date_time_str = row[0] + '_' + row[1]
            date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
            clean_date_time = datetime.datetime.strftime(date_time_obj, '%Y-%m-%d %H:%M')
            licence_plate = row[2]
            plate_fallback = row[3]

            if plate_fallback != '':
                licence_plate = plate_fallback

            # append FuelEvent obj to list
            fuel_events.append(FuelEvent(licence_plate, plate_fallback, clean_date_time))

            return fuel_events
