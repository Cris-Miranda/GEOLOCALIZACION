from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
# Latitud y longitud de varios puntos de interes
lat = [19.4326009, -34.9964962, 38.89511]
lon = [-99.1333415, -64.9672816, -77.03637]
# Inicializamos las dimenciones de la figura
plt.figure (figsize = (16, 12))
#distribucion de lineascosteras
eq_map =Basemap(projection='robin',
                lon_0 = 0,
                resolution = "h",
                area_thresh = 1000.0,
                llcrnrlon = -136.25,
                llcrnrlat = 56,
                urcrnrlon = -134.25,
                urcrnrlat = 57.75)
# Dibujamos las lineas costeras y los paises
eq_map.drawcoastlines()
eq_map.drawcountries()
# Dibujamos los meridianos y paralelos
eq_map.fillcontinents(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
# Dibujamos cada uno de los puntos usando zip
for lon, lat in zip(lon, lat):
# Creamos un objeto de la clase eq_map
    x,y = eq_map(lon, lat)
# Dibujamos un circulo color rojo 
    eq_map.plot(x, y, "r", markersize = 17, alpha = 0.8)
    
    
