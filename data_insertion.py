import pandas

data = pandas.read_csv("dataset.csv")
l = data.shape[0]

for i in range(10):
    r = data.loc[i, :]
    row = row[0].split(";")
    _, created = Car.objects.get_or_create(
        id=row[0],
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
