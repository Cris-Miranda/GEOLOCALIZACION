# Importamos el modulo time
import time
from geopy.geocoders import Nominatim
# Generamos un objeto de la clase Nominatim
geolocator = Nominatim()
# Creamos una lista de lugares a buscar
places = ["Mexico", "Buenos Aires Argentina", "175 5th Avenue NYC"]
# Utilizamos la funcion geocode del objeto para obtener la longitud y latitud de cada lugar
for x in places:
    location = geolocator.geocode(x,timeout=10)
# Imprimimos la informacion obtenida
    print("lugar: "+x+", coordenadas: "+str(location.latitude)+","+str(location.longitude))
    time.sleep(1)