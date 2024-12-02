import pandas as pd
import numpy as np
import math

KO_df = pd.read_csv("KO_StockData.csv")
PEP_df = pd.read_csv("PEP_StockData.csv")

sma_20 = x / 20
mult_20 = (2 / (sma_20 + 1))

sma_50 = y / 50
mult_50 = (2 / (sma_50 + 1))
