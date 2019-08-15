import csv
from fuel_class import FuelEvent
import datetime


# TODO: print progress
# do fucking regular lists instead of this shit
def read_fuel_csv(in_filename, out_filename):
    with open(in_filename, 'r', encoding='utf-8') as fin, open(out_filename, 'w', encoding='utf-8') as fout:
        r = csv.reader(fin)
        w = csv.writer(fout)

        next(r, None)
        w.writerow(['date_time', 'licence_plate', 'plate_fallback'])

        r = csv.reader(fin)
        for row in r:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            w.writerow(new_row)

    with open(out_filename, 'r', encoding='utf-8') as fout:
        r = csv.DictReader(fout)
        fuel_events = []
        for row in r:
            f = FuelEvent.create_from_dict(row)
            fuel_events.append(f)
            print(row)

    return fuel_events


def clean_fuel_events(events):
    for f in events:
        date_time_str = f.date_time + ':00'
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
        date_time_format = datetime.datetime.strftime(date_time_obj, '%Y-%m-%d %H:%M:%S')
        f.date_time = date_time_format

        if f.plate_fallback != '':
            setattr(f, 'licence_plate', f.plate_fallback)
        print(f.date_time, f.licence_plate, f.plate_fallback)

        # strip licence_plate of blanks
