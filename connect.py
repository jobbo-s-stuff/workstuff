import simplejson
import psycopg2
from psycopg2.extras import RealDictCursor

minFuelTime = ''
maxFuelTime = ''
licencePlates = []

'''
Creates connection to db, queries and joins required car, reservation data and dumps it into json
'''


def db_query():
    print("Opening MILES db connection...")
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="database")
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    print("Querying reservations, cars...")
    car_res = "SELECT cars.carid, cars.licenceplate, cars.vehicletypeid, " \
              "reservations.reservationid, reservations.carid, reservations.customerid, reservations.starttime, " \
              "reservations.endtime, reservations.startbatterylevel, reservations.endbatterylevel, " \
              "FROM reservations INNER JOIN cars ON reservations.carid = cars.carid  " \
              "WHERE reservations.endtime >= " + "'" + minFuelTime + "'" + " and reservations.starttime <=" + "'" + maxFuelTime + "'" + \
              " and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0" \
              " and cars.licenceplate IN" + licencePlates([]) + ";"
    cursor.execute(car_res)

    # TODO: don't dump as json, store in list instead
    print(simplejson.dumps(cursor.fetchall(), indent=2))

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
