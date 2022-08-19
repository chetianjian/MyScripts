import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf
import numpy as np
import pandas as pd
import datetime as dt
import tensorflow as tf
import pickle
import math
import re
import random
import matplotlib.pyplot as plt
import multiprocessing as mp

# import the relevant Keras modules
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.layers import LSTM
from keras.layers import Dropout


# Check if GPU computation is available.

class ActivateGPU(object):
    def __init__(self):
        self.is_available = bool(tf.config.list_physical_devices("GPU"))
        self.physical_device = tf.config.experimental.list_physical_devices("GPU")

    def check_device(self):
        print("Physical Devices:")
        for device in tf.config.list_physical_devices():
            print(device)

    def set_gpu(self):
        if self.is_available:
            print(f"GPU availability: {self.is_available}")
        try:
            tf.config.experimental.set_memory_growth(self.physical_device[0], True)
            print("Num GPUs: ", len(tf.config.experimental.list_physical_devices("GPU")))
            print("Set Memory Growth Successfully.")
        except:
            print("Invalid device or cannot modify virtual devices once initialized.")
        return "GPU initialization completed."

print(ActivateGPU().check_device())
print(ActivateGPU().set_gpu())

# Import the data
price_file = open("C:\\Users\\tianj\\Desktop\\" +
                 "Causis\\data\\股票行情及估值数据\\stock_price_standard_",
                 "rb")
st_file = open("C:\\Users\\tianj\\Desktop\\" +
               "Causis\\data\\股票行情及估值数据\\stock_st_standard_",
               "rb")
valuation_file = open("C:\\Users\\tianj\\Desktop\\" +
                  "Causis\\data\\股票行情及估值数据\\stock_valuation_standard_",
                  "rb")

price = pickle.load(price_file)
st = pickle.load(st_file)
valuation = pickle.load(valuation_file)

price = price.reset_index().rename(columns={"level_0": "code"}).rename(columns={"level_1": "item"})
price["code"] = list(map(lambda i: re.findall(pattern="[\d]{6}", string=i)[0], price["code"]))
price = price.set_index(["code", "item"]).T
price.index.name = "date"
print(price.head(3))

st = st.reset_index().rename(columns={"level_0": "code"}).rename(columns={"level_1": "item"})
st["code"] = list(map(lambda i: re.findall(pattern="[\d]{6}", string=i)[0], st["code"]))
st = st.set_index(["code", "item"]).T
st.index.name = "date"
print(st.head(3))

valuation = valuation.reset_index().rename(columns={"level_0": "code"}).rename(columns={"level_1": "item"})
valuation["code"] = list(map(lambda i: re.findall(pattern="[\d]{6}", string=i)[0], valuation["code"]))
valuation = valuation.set_index(["code", "item"]).T
valuation.index.name = "date"
print(valuation.head(3))

print(f"Identical underlying assets?     {list(price.stack().columns) == list(st.stack().columns) == list(valuation.stack().columns)}")
print(f"Identical time interval?     {list(price.index) == list(st.index) == list(valuation.index)}")

stock_codes, trading_dates = list(price.stack().columns), list(price.index)

def count_daily_underlyings(date):
    return len(set(map(lambda x: x if len(price.loc[date][x].dropna()) == 11 else None, stock_codes)) &
               set(map(lambda x: x if len(st.loc[date][x].dropna()) == 2 else None, stock_codes)) &
               set(map(lambda x: x if len(valuation.loc[date][x].dropna()) == 10 else None, stock_codes)))



daily_stock_count = list(map(count_daily_underlyings, trading_dates[0:40]))

print(daily_stock_count)


num_cores = int(mp.cpu_count())
print(f"Cores: {num_cores}")

pool = mp.Pool(num_cores)
results = [pool.apply_async(count_daily_underlyings, args=(date)) for date in trading_dates[0:40]]
print(len(results))
for i in results:
    print(i.get())