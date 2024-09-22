from geopy.geocoders import Nominatim

# Generamos un objeto de la clase Nominatim
geolocator = Nominatim(user_agent="nombre-de-mi-app-geolocator")

# Creamos una lista de lugares a buscar
places = ["Mexico", "Buenos Aires Argentina", "175 5th Avenue NYC"]

for place in places:
    location = geolocator.geocode(place)
    if location:
        print(f"Lugar: {place}, Coordenadas: {location.latitude}, {location.longitude}")
    else:
        print(f"Lugar: {place}, No se encontraron coordenadas.")
