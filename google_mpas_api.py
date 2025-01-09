import requests

def get_route_data(start, end):
    """
    Fetch route data from Google Maps API.
    :param start: Starting location
    :param end: Ending location
    :return: Dictionary with route distance and duration
    """
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        route = data["routes"][0]
        distance = route["legs"][0]["distance"]["value"] / 1000  # meters to km
        duration = route["legs"][0]["duration"]["value"] / 60  # seconds to minutes
        return {"distance_km": distance, "duration_min": duration}
    else:
        raise Exception("Error fetching route data from Google Maps API")
