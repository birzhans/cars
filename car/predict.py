import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv("cars.csv")
data.drop(["Ссылка"], axis=1, inplace=True)
data["Бренд"] = pd.factorize(data["Бренд"])[0]
data["Модель"] = pd.factorize(data["Модель"])[0]
data["Город"] = pd.factorize(data["Город"])[0]
data["Кузов"] = pd.factorize(data["Кузов"])[0]
data["Руль"] = pd.factorize(data["Руль"])[0]
data["Цвет"] = pd.factorize(data["Цвет"])[0]
data["Привод"] = pd.factorize(data["Привод"])[0]
data["Растаможен в Казахстане"] = pd.factorize(data["Растаможен в Казахстане"])[0]
data["Вид топлива"] = pd.factorize(data["Вид топлива"])[0]
data["Коробка передач"] = pd.factorize(data["Коробка передач"])[0]

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(data.iloc[::])

data.iloc[::] = imputer.transform(data.iloc[::])

y = data["Цена"]
data.drop(["Цена"], axis=1, inplace=True)
# data.drop(["Средння цена"], axis=1, inplace=True)
X = data[::]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=50
)


from sklearn.linear_model import LinearRegression

# Create model
linreg = LinearRegression()
linreg.fit(X_train, y_train)

x = linreg.predict([X_test.iloc[0]])
# print([X_test.iloc[0]])
print(y_test.iloc[0])
print(x)
# print(X_test)

# Calculate our y hat (how our model performs against the test data held off)
# y_hat_test1 = linreg.predict(X_test)

# from sklearn.metrics import mean_squared_error, mean_absolute_error

# test_mae1 = mean_absolute_error(y_test, y_hat_test1)

# print(test_mae1)