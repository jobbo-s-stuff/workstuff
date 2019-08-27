import psycopg2
from psycopg2.extras import RealDictCursor
import pprint
from datetime import datetime


def db_query(min_fuel_time, max_fuel_time, licence_plates):
    print("Opening MILES db connection...")
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="database")
    cursor = connection.cursor(cursor_factory=RealDictCursor)  # opens database connection
    print("Querying reservations, cars...")
    cursor.execute(
        "SELECT reservations.reservationid, reservations.customerid, reservations.starttime FROM reservations INNER JOIN cars ON reservations.carid = cars.carid WHERE reservations.endtime >= %s and reservations.starttime <= %s and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0 and cars.licenceplate IN %s;",
        (str(min_fuel_time), str(max_fuel_time), tuple(licence_plates),))  # executes query with variables passed in
    result = cursor.fetchall()  # grabs all results
    cursor.close()
    connection.close()
    pprint.pprint(result)  # makes results more readable
    print("PostgreSQL connection is closed")
    return result
