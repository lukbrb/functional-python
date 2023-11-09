import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y = 2015
max_record_15 = pd.read_csv("data/max_records_15.csv")
min_record_15 = pd.read_csv("data/min_records_15.csv")
max_0514 = pd.read_csv("data/max_0514.csv", index_col=0)
min_0514 = pd.read_csv("data/min_0514.csv", index_col=0)

plt.figure(figsize=(10, 10))

day_to_int = {day: num_day for day, num_day in zip(max_0514.index, list(range(366)))}
print(max_record_15)
days_max_records_15 = [day_to_int[day_rec] for day_rec in max_record_15.Day]
days_min_records_15 = [day_to_int[day_rec] for day_rec in min_record_15.Day]

plt.plot(max_0514.values, 
        c = 'red', 
        label ='Record High')

plt.plot(min_0514.values, 
        c = '#00FFFF', 
        label ='Record Low')

plt.scatter(days_max_records_15, 
            max_record_15['2015'].values, 
            c = 'black', 
            label = "Record Breaking High in "+ str(y))

plt.scatter(days_min_records_15, 
            min_record_15['2015'].values, 
            c = 'blue', 
            label = "Record Breaking Low in " + str(y))



plt.xlabel('Days of the year', fontsize=10)
plt.ylabel('Temperature (Celsius)', fontsize=10)
plt.title('Michigan Record Temperatures between 2005 and 2015', fontsize=15)

plt.gca().fill_between(range(len(max_0514)), 
                    np.array(max_0514.values.reshape(len(max_0514),)), 
                    np.array(min_0514.values.reshape(len(min_0514.values),)), 
                    facecolor='purple', alpha=0.1)

# DAYS = list(np.arange(0, 366, 14))
# axis = plt.axes()
# axis.set_xticks(DAYS)
# plt.xticks(fontsize=7)
# plt.yticks(fontsize=7)
# plt.legend(loc = (1.01,0.3), fontsize=10)
plt.show()