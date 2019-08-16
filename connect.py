import psycopg2
from psycopg2.extras import RealDictCursor
import program

'''
Creates connection to db, queries and joins required car, reservation data and dumps it into json
'''


def db_query(min_fuel_time, max_fuel_time, licence_plates):
    print("Opening MILES db connection...")
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="hostname",
                                  port="port",
                                  database="database")
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    print("Querying reservations, cars...")
    cursor.execute("SELECT reservations.reservationid, reservations.customerid, reservations.starttime FROM reservations INNER JOIN cars ON reservations.carid = cars.carid WHERE reservations.endtime >= (%s) and reservations.starttime <= (%s)and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0 and cars.licenceplate IN ANY(%s);", min_fuel_time, max_fuel_time, licence_plates)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
    return result
