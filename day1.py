city_name = "New Delhi"
temperature = 35.5
air_quality_index = 185
is_hazardous = False
print(city_name)
print(temperature)
print(air_quality_index)
print(is_hazardous)

if air_quality_index > 150:
    print("alert! not good air . please wear a mask")
else:
    print("air is a good ")

print("\n=== weekly climate log=== ")
weekly_aqi = [85,95,100,203,259]
total_aqi = 0
for aqi in weekly_aqi:
    if aqi > 150:
        print("poor air quality" , aqi)
    else:
        print("modrate air quality" , aqi)
    total_aqi = total_aqi+aqi

avrage_aqi = total_aqi / len(weekly_aqi)
print(avrage_aqi)

