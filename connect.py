import psycopg2
from psycopg2.extras import RealDictCursor
import program

min_fuel_time = ''
max_fuel_time = ''
licence_plates = []

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
    # TODO: pass list as string
    car_res = "SELECT cars.carid, cars.licenceplate, cars.vehicletypeid, " \
              "reservations.reservationid, reservations.carid, reservations.customerid, reservations.starttime, " \
              "reservations.endtime, reservations.startbatterylevel, reservations.endbatterylevel, " \
              "FROM reservations INNER JOIN cars ON reservations.carid = cars.carid  " \
              "WHERE reservations.endtime >= " + "'" + minFuelTime + "'" + " and reservations.starttime <=" + "'" + maxFuelTime + "'" + \
              " and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0" \
              " and cars.licenceplate IN" + licencePlates([]) + ";"
    cursor.execute(car_res)

    # TODO: don't dump as json, store in list instead


    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
