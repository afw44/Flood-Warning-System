from floodsystem.plot import mapplot
from floodsystem.utils import risktypedict_from_cache, riskleveldict_from_cache
import matplotlib.pyplot as plt
import numpy as np


def run():

    #update_risk_caches(build_station_list())

    townrisk_floats = np.genfromtxt('risk_cache_floats.txt',delimiter=',')

    mapplot(townrisk_floats)

    plt.title('England Station Risks')

    risktype_dictionary = risktypedict_from_cache()
    risklevel_dictionary = riskleveldict_from_cache()

    plt.show()


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()

