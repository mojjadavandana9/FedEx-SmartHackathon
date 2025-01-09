class EmissionModel:
    def calculate_emissions(self, distance_km, fuel_efficiency_l_per_km, emission_factor):
        """
        Calculate emissions for a route.
        :param distance_km: Distance of the route in kilometers
        :param fuel_efficiency_l_per_km: Fuel consumption in liters per km
        :param emission_factor: Emissions per liter of fuel (kg CO₂)
        :return: Total emissions (kg CO₂)
        """
        return distance_km * fuel_efficiency_l_per_km * emission_factor
