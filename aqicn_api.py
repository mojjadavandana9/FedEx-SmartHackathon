import requests

def get_weather_data(lat, lon):
    """
    Fetch real-time weather and air quality data for a given location.
    :param lat: Latitude
    :param lon: Longitude
    :return: Weather and AQI data as a dictionary
    """
    api_key = "YOUR_AQICN_API_KEY"
    url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "ok":
            return {
                "aqi": data["data"]["aqi"],
                "temperature": data["data"]["iaqi"].get("t", {}).get("v", "N/A"),
                "humidity": data["data"]["iaqi"].get("h", {}).get("v", "N/A"),
            }
        else:
            raise Exception(f"Error in AQICN response: {data['data']}")
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")
