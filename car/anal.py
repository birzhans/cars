import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pd.set_option("display.max_colwidth", -1)

path = os.getcwd()
data_csv = pd.read_csv(
    os.path.abspath(os.path.join(path, os.pardir)) + "/cars/dataset.csv", sep=";"
)


class Data:
    def __init__(self, data):
        self.data = data

    def describe(self):
        return self.data.describe()


data = Data(data_csv)
