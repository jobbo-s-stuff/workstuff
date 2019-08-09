import simplejson
import psycopg2
from psycopg2.extras import RealDictCursor

timeStart = ''
timeEnd = ''

'''
Creates connection to db, queries and joins required car, reservation data and dumps it into json
'''


# TODO: check whether easier to go for "IN cars.licenceplate" based on json results in addition to timeframe
def db_query():
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="database")
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    car_res = "SELECT cars.carid, cars.licenceplate, cars.vehicletypeid, " \
              "reservations.reservationid, reservations.carid, reservations.customerid, reservations.starttime, " \
              "reservations.endtime, reservations.startbatterylevel, reservations.endbatterylevel, " \
              "FROM reservations INNER JOIN cars ON reservations.carid = cars.carid  " \
              "WHERE reservations.starttime BETWEEN " + "'" + timeStart + "'" + " and " + "'" + timeEnd + "'" + \
              " and startbatterylevel <= 25  and endbatterylevel >= 84 and isdev = 0 and drivendistance != 0;"
    cursor.execute(car_res)

    print(simplejson.dumps(cursor.fetchall(), indent=2))

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
