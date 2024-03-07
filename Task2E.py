from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import station_namelookup
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime
import pprint

stations = build_station_list()
update_water_levels(stations)

highest_stations = [tuple[0] for tuple in stations_highest_rel_level(stations,6)]

"""Returns names of highest 6 relative level stations - afw44"""

print('Stations with highest water level:')
pprint.pp(highest_stations)
print()

for index,name in enumerate(highest_stations):
        

        station = station_namelookup(build_station_list(use_cache = True),name)

        print(f"Plotting {station.name}")

        dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days = 5))
        """Fetches dates and levels for the station in a given timeperiod."""

        if len(dates) > 0:
                plt.subplot(2, 3, index+1)
                plot_water_levels(station, dates, levels)
        else:
                
                print('Bad data')


print("PLOTS COMPLETE")
plt.subplots_adjust(wspace=None, hspace=None)
plt.show()
