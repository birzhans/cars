import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path = os.getcwd()
data = pd.read_csv(os.path.abspath(os.path.join(path, os.pardir)) + "/dataset.csv")


def describe():
    return data.describe()


print(describe())