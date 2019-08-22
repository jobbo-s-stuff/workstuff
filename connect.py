import psycopg2
from psycopg2.extras import RealDictCursor

'''
Creates connection to db, queries and joins required car, reservation data and dumps it into json
'''
from datetime import datetime

def db_query(min_fuel_time, max_fuel_time, licence_plates):
    print("Opening MILES db connection...")
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="database")
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    print("Querying reservations, cars...")
    cursor.execute(
        "SELECT reservations.reservationid, reservations.customerid, reservations.starttime FROM reservations INNER JOIN cars ON reservations.carid = cars.carid WHERE reservations.endtime >= %s and reservations.starttime <= %s and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0 and cars.licenceplate IN %s;",
        (str(min_fuel_time), str(max_fuel_time), tuple(licence_plates),))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print(result)
    print("PostgreSQL connection is closed")
    return result
