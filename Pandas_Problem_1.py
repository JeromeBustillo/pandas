import pandas as pd
data = pd.read_csv('cars.csv')
x = data.iloc[:5,:]
y = data.iloc[-5:,:]
