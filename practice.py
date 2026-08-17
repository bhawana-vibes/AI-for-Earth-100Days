#import numpy as np
#rain_data = np.array([12,25,5,40])
#high_rain = rain_data[rain_data>20]
#print(high_rain)
#print("avg rain" , np.mean(rain_data))
#print("high rain" , np.max(rain_data))

#import numpy as np
#solar_eng = np.array([15,8,22])
#print("low engery:" ,np.min(solar_eng))
#hot_rays = solar_eng *2
#print(hot_rays)

import numpy as np
city_temps = np.array([
    [30, 32, 34],
    [25, 27, 26]
])
print("avg temps:" , np.mean(city_temps))
print("high temps:" , np.max(city_temps))
#high_temps= ([city_temps>30])
print(city_temps[city_temps>30])
