from floodsystem.plot import plot_list_of_stations
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
import pprint
import matplotlib.pyplot as plt


def run():
        stations = build_station_list()
        update_water_levels(stations)

        highest_stations = [tuple[0] for tuple in stations_highest_rel_level(stations,6)]
        """Returns names for highest 6 relative level stations - afw44"""

        plot_list_of_stations(highest_stations)
        """Plots above stations - afw44 """

if __name__ == "__main__":
    print("*** Task A: CUED Part IA Flood Warning System ***")
    run()


