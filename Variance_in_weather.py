import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
# Project start
print(london_data.head())
print(len(london_data))
temp = london_data["TemperatureC"]
average_temp = np.average(temp)
print("The average temperature is ",average_temp)
temperature_var = np.var(temp)
print("The temperature variance is ",temperature_var)
temperature_standard_deviation = np.std(temp)
print("The temperature standard deviation is",temperature_standard_deviation)
june = london_data.loc[london_data["month"]==6]["TemperatureC"]
july = london_data.loc[london_data["month"]==7]["TemperatureC"]
print("The mean of june is ",np.mean(june)," and mean of july is ",np.mean(july))
print("The std of june is ",np.std(june)," and std of july is ",np.std(july))
for i in range(1,13):
  month = london_data.loc[london_data["month"]==i]["TemperatureC"]
  print("The mean temperature in month ",i," is ",np.mean(month))
  print("The std temperature in month ",i," is ",np.std(month))