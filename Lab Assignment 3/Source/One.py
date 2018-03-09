#Importing packages
import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
x_axis = []
y_axis = []
# Loading data
with open('temp.csv') as f:
    csvfile = csv.reader(f, delimiter=',')
    next(csvfile)
    for line in csvfile:
        temp = float(line[0])
        relative_humidity = float(line[1])
        wind = float(line[2])
        precipitation = float(line[3])
        area = 1 if float(line[4]) > 0 else 0
        x_axis.append([temp, relative_humidity, wind, precipitation])
        y_axis.append(area)
# Creating numpy array
np_x = np.array(x_axis)
np_y = np.array(y_axis)
#LDA
model = LinearDiscriminantAnalysis()
model.fit(np_x, np_y)
# Hot weather prediction
tetemp = 40; relative_humidity = 90; wind = 2 ; precipitation = 0.9
print("Weather: temperature [%f] in Celsius, relative humidity [%f] of percent, \n wind speed [%f] in km/h, and  precipitation [%f] in mm/m2" % (temp, relative_humidity, wind,  precipitation))
if model.predict([[temp, relative_humidity, wind,  precipitation]])[0]:
    print("There will be hot weather conditions")
else:
    print("Normal weather conditions")
#Cold weather prediction
tetemp =4 ; relative_humidity = 10; wind = 15 ; precipitation = 30
print("\nWeather: temperature [%f] in Celsius, relative humidity [%f] of percent, wind speed [%f] in km/h,\n and  precipitation [%f] in mm/m2" % (temp, relative_humidity, wind,  precipitation))
if model.predict([[temp, relative_humidity, wind,  precipitation]])[0]:
    print("There will be cold weather, Health Advisory: Do not go out")
else:
    print("Normal weather conditions")