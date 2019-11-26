import pandas as pd
data = pd.read_csv('cars.csv')
a = data.iloc[:5,::2]
b = data[data['Model']=='Mazda RX4']
c = data[data['Model']=='Camaro Z28'].loc[:,['Model','cyl']]
d1 = data[data['Model']=='Mazda RX4 Wag'].loc[:,['Model','cyl','gear']]
d2 = data[data['Model']=='Ford Pantera L'].loc[:,['Model','cyl','gear']]
d3 = data[data['Model']=='Honda Civic'].loc[:,['Model','cyl','gear']]

