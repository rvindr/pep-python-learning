import requests
import json

base_url = "https://api.weatherapi.com/v1"
api_key = "6eb2a9a4b4b5467ba4d71355263101"
# query = "mumbai"
# res = requests.get(url=f"{base_url}/current.json?key={api_key}&q={query}")
# data = res.json()

# # print("Latitude",data['location']['lon'])
# # print("Longitude",data['location']['lat'])
# location = data.get("location")
# current = data.get("current")

# print("Latitude:",location.get("lat"))
# print("Longitude:",location.get("lon"))
# print("City:",location.get("name"))
# print("Waether Condition:",current.get("condition").get("text"))
# print("Wind speed:",current.get("wind_kph"))
# print("Humidity:",current.get("humidity"))


def get_weather(city):
    res = requests.get(url=f"{base_url}/current.json?key={api_key}&q={city}")
    print(f"{base_url}/current.json?key={api_key}&q={city}")
    if res.status_code==200:
        # data = res.json()
        # location = data.get("location")
        # current = data.get("current")
        # info = {
        # "Longitude":location.get("lon"),
        # "Latitude":location.get("lat"),
        # "City":location.get("name"),
        # "Condition":current.get("condition").get("text"),
        # "Wind speed":current.get("wind_kph"),
        # "Humidity":current.get("humidity"),
        # "Temp a":current.get("temp_c")

        # }
        
        # return info
        return res.json()
    return "Error occured"


# print(get_weather('delhi'))

def get_advisory(data):
    if data['Temp a'] > 35:
        print("Heat Alert")
    if data['Condition'].lower() == "rain":
        print("Carry Umbrella")
    if data["Wind speed"] > 40:
        print("Travel warning")
    if data["Temp a"] < 0:
        print("Cold")

# while True:
#     city = input("enter city name:\t")
#     if not city.strip():
#         continue
#     weather = get_weather(city)
#     print("-------Weather Details")
#     print(weather)
#     get_advisory(weather)
#     exit = input("Do you want to search more.\n Press y/n\n")
#     if exit.lower() == "n":
#         break


def save_json(weather):
    with open("data.json", "w") as file:
        json.dump(weather, file, indent=3)


save_json(get_weather("Delhi"))

# https://drive.google.com/drive/folders/1GfYuwmmb0Lq2uThuVNV5dPznJUBelzlL
