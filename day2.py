cities_data  = [
    {"city":"new delhi" , "aqi":85 , "temperature":37.5,
      "city":"mumbai" , "aqi":95 , "temperature":34.5,
      "city":"goa" , "aqi":90 , "temperature":38.5,
      "city":"kolkata" , "aqi":202 , "temperature":32.5,
      "city":"pune" , "aqi":100 , "temperature":36.5
    }
]
def air_health(city_name , aqi_value):
    if aqi_value >200:
        status = "poor quality(high risk)"
    elif aqi_value >100:
        status = "moderate quality (cauation)"
    else:
        status = "good / heathly"
    return f"City: {city_name:10} | AQI: {aqi_value:<4} | Status: {status}"

print("=== Multi-City Air Quality Report ===\n")

for data in cities_data:
    report = air_health(data["city"], data["aqi"])
    print(report)

highest_aqi = 0
most_polluted_city = ""
total_temp = 0
for data in cities_data:
   total_temp += data["temperature"]
   if data["aqi"] > highest_aqi:
        highest_aqi = data["aqi"]
        most_polluted_city = data["city"]
avg_temp = total_temp / len(cities_data)

print("\n=== Climate Analytics Summary ===")
print(f"🔥 Most Polluted City: {most_polluted_city} (AQI: {highest_aqi})")
print(f"🌡️ Average Temperature across all cities: {avg_temp:.2f} °C")
        
