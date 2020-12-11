import csv
from car.models import *

with open("dataset.csv") as f:
    reader = csv.reader(f, sep="\t")
    next(reader)
    c = 0
    while c < 5:
        for row in reader:
            print(row)
            # _, created = Car.objects.get_or_create(
            #     id=c,
            #     brand=row[0],
            #     model=row[1],
            #     year=int(row[2]),
            #     city=row[3],
            #     body_type=row[4],
            #     engine_volume=round(float(row[5]), 1),
            #     mileage=int(row[6]),
            #     gear_type=row[7],
            #     steering_wheel=row[8],
            #     color=row[9],
            #     wheel_drive=row[10],
            #     custom_clearanced=True if "TRUE" == row[11] else False,
            #     price=int(row[12]),
            #     average_price=int(row[13]),
            #     link=row[14],
            #     fuel_type=row[15],
            # )
