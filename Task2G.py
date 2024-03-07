from floodsystem.plot import mapplot
from floodsystem.utils import risktypedict_from_cache, riskleveldict_from_cache
from floodsystem.flood import update_risk_caches
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import numpy as np

print()
#update_risk_caches(build_station_list())

townrisk_floats = np.genfromtxt('risk_cache_floats.txt',delimiter=',')

mapplot(townrisk_floats)

plt.title('England Station Risks')

risktype_dictionary = risktypedict_from_cache()
risklevel_dictionary = riskleveldict_from_cache()

plt.show()