import requests

def get_osrm_route(start_lat, start_lon, end_lat, end_lon):
    """
    Fetch route data from the OSRM API.
    :param start_lat: Starting latitude
    :param start_lon: Starting longitude
    :param end_lat: Ending latitude
    :param end_lon: Ending longitude
    :return: Optimized route data as a dictionary
    """
    url = f"http://router.project-osrm.org/route/v1/driving/{start_lon},{start_lat};{end_lon},{end_lat}?overview=full"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == "Ok":
            route = data["routes"][0]
            return {
                "distance_km": route["distance"] / 1000,  # meters to km
                "duration_min": route["duration"] / 60,   # seconds to minutes
                "geometry": route["geometry"],           # Polyline geometry for the route
            }
        else:
            raise Exception(f"Error in OSRM response: {data['code']}")
    else:
        raise Exception(f"Error fetching route data: {response.status_code}")
