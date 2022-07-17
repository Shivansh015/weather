import requests, json
apikey= "e0714df0b81404fa8be5e43fe6f0f6a4"
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input("Enter the city: ")
completeURL= baseURL+ cityName+ "&appid=" + apikey
response= requests.get(completeURL)
data= response.json()

print("Current Temperature(in °C) : ",round(data["main"]["temp"]-273.15,2))
print("Minimum Temperature(in °C) : ",round(data["main"]["temp_min"]-273.15,2))
print("Maximum Temperature(in °C) : ",round(data["main"]["temp_max"]-273.15,2))
print("Humidity(in %) : ",round(data["main"]["humidity"],2))
print("Wind Speed(in km/hr) : ",round(data["wind"]["speed"]*3.6,0))
print("Country(Two-letter Abbreviation) : ",(data["sys"]["country"]))

