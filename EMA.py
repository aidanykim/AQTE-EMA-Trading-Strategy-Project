import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#Reading CSVs
read_data = input("Enter preferred CSV file: ")
DATA_df = pd.read_csv(read_data + "_StockData.csv")

#EMA Model for DATA
#n = 20
DATA_20_sum = 0

for i in range(0, 20):
    DATA_20_sum += DATA_df.iloc[i,1];

sma_20 = DATA_20_sum / 20
mult_20 = (2 / (21))

DATA_EMA_list = [1 for i in DATA_df.iloc[:,0]]

DATA_EMA_list[21] = (DATA_df.ilco[21,1] - sma_20) * mult_20 + sma_20

for i in range(22, len(DATA_EMA_list)):
  DATA_EMA_list[i] = (DATA_df.ilco[i,1] - DATA_EMA_list[i - 1]) * mult_20 + DATA_EMA_list[i - 1]


#n = 50
#TODO: Just copy the 20 model later (or make a new model that reads prefered n values?) Just plot n = 20 for now.

#DATA_50_sum = 0
#
#for i in range(len(DATA_head_50)):
#    DATA_50_sum += DATA_head_50[i]
#
#sma_50 = DATA_50_sum / 50
#mult_50 = (2 / (51))

#Plots
#Plot Share Prices
x1 = range(len(DATA_df["Dates"]))
y1 =DATA_df[["PX_LAST"]]

plt.plot(x1, y1, label=read_data + "Price")
plt.xlabel("Dates")
plt.ylabel("Price")
plt.title(read_data + "Price over time (n = 7 days)")
plt.legend()
plt.show()
#Plot EMA
x1 = range(len(DATA_df["Dates"]))
y1 =DATA_df[["PX_LAST"]]

plt.plot(x1, y1, label= read_data + "Momentum")
plt.xlabel("Dates")
plt.ylabel("Price")
plt.title(read_data + "Momentum over time (n = 7 days)")
plt.legend()
plt.show()

