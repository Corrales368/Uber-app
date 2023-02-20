import math


def haversine(lat1, lon1, lat2, lon2):
    """
    Get the distance of two points with coordinates assuming a sphere
    """
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Distance angular between two points
    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2
    
    # Distance in a straight line between the two points
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth radius
    earth_radius = 6371  # Radius of earth in kilometers. Use 3956 for miles

    distance = c * earth_radius
    return distance
