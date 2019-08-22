class FuelEvent:
    def __init__(self, licence_plate, plate_fallback, date_time):
        self.licence_plate = licence_plate
        self.plate_fallback = plate_fallback
        self.date_time = date_time

    def __str__(self):
        return "licence_plate:" + self.licence_plate + ", plate_fallback:" + self.plate_fallback + ", datetime:" + self.date_time.strftime(
            "%m/%d/%Y, %H:%M:%S")

    @staticmethod
    def create_from_dict(lookup):
        return FuelEvent(
            lookup['licence_plate'],
            lookup['plate_fallback'],
            lookup['date_time']
        )