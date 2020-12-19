import pandas

data = pandas.read_csv("dataset.csv")
l = data.shape[0]


def av_p(p):
    a = 0
    try:
        a = int(p)
    except:
        pass
    return a


for i in range(11, l):
    row = data.loc[i, :]
    _, created = Car.objects.get_or_create(
        id=i,
        brand=row[0],
        model=row[1],
        year=int(row[2]),
        city=row[3],
        body_type=row[4],
        engine_volume=round(float(row[5]), 1),
        mileage=int(row[6]),
        gear_type=row[7],
        steering_wheel=row[8],
        color=row[9],
        wheel_drive=row[10],
        custom_clearanced=True if "Да" == row[11] else False,
        price=int(row[12]),
        average_price=av_p(row[13]),
        link=row[14],
        fuel_type=row[15],
    )
