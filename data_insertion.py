import csv
from car.models import *

with open("dataset.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    c = 10001
    for row in reader:
        while c < 19000:
            _, created = Car.objects.get_or_create(
                id=c,
                brand=row[1],
                model=row[2],
                year=int(row[3]),
                city=row[4],
                body_type=row[5],
                engine_volume=round(float(row[6]), 1),
                mileage=int(row[7]),
                gear_type=row[8],
                steering_wheel=row[9],
                color=row[10],
                wheel_drive=row[11],
                custom_clearanced=True if "TRUE" == row[12] else False,
                price=int(row[13]),
                average_price=int(row[14]),
                link=row[15],
                fuel_type=row[16],
            )
            c += 1
