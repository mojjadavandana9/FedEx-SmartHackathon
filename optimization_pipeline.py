from apis.google_maps_api import get_route_data

class OptimizationPipeline:
    def get_optimized_route(self, start, end):
        """
        Fetch optimized route data.
        :param start: Starting location
        :param end: Ending location
        :return: Dictionary with route distance and duration
        """
        # Fetch route data from Google Maps API
        route_data = get_route_data(start, end)
        return route_data
