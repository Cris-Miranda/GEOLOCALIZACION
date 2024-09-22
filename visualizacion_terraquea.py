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

