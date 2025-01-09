import requests

def get_traffic_data(lat, lon):
    """
    Fetch real-time traffic data for a given latitude and longitude.
    :param lat: Latitude
    :param lon: Longitude
    :return: Traffic information as a dictionary
    """
    api_key = "YOUR_TOMTOM_API_KEY"
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "current_speed": data["flowSegmentData"]["currentSpeed"],
            "free_flow_speed": data["flowSegmentData"]["freeFlowSpeed"],
            "traffic_level": data["flowSegmentData"]["currentTravelTime"] / data["flowSegmentData"]["freeFlowTravelTime"]
        }
    else:
        raise Exception(f"Error fetching traffic data: {response.status_code}")
