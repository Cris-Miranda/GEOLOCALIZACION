from geopy.distance import geodesic
from geopy.distance import great_circle

# Coordenadas de Washington D.C. (Estados Unidos) y Ciudad de México (México)
USA = (38.89511, -77.03637)  # Washington 
Mexico = (19.4326009, -99.1333415)  # Ciudad de México

# Calculamos la distancia con geodesic (reemplaza a vincenty)
print("Distancia entre México y Estados Unidos (geodesic): " + str(geodesic(USA, Mexico).miles))

# Calculamos la distancia con great_circle
print("Distancia entre México y Estados Unidos (great_circle): " + str(great_circle(USA, Mexico).miles))
