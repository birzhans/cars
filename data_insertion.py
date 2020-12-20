import pandas

data = pandas.read_csv("cars.csv")
l = data.shape[0]


def av_p(p):
    a = 0
    try:
        a = int(p)
    except:
        pass
    return a


for i in range(1000):
    row = data.loc[i, :]
    _, created = Car.objects.get_or_create(
        id=i,
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
        custom_clearanced=True if "Да" == row[12] else False,
        price=int(row[13]),
        average_price=av_p(row[14]),
        link=row[15],
        fuel_type=row[16],
        price_difference_percent=row[17],
    )
