from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import station_namelookup
from floodsystem.flood import stations_highest_rel_level
import datetime
import pprint
import matplotlib.pyplot as plt

stations = build_station_list()
update_water_levels(stations)

highest_stations = [tuple[0] for tuple in stations_highest_rel_level(stations,6)]

"""Returns names for highest 6 relative level stations - afw44"""

print()
print('Stations with highest water level:')
pprint.pp(highest_stations)
print()

for index,name in enumerate(highest_stations):

        station = station_namelookup(build_station_list(use_cache = True),name)

        dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days = 5))
        """Fetches dates and levels for the station in a given timeperiod."""

        if len(dates) > 0:
                plt.subplot(2, 3, index+1)
                print(f"Plotting {station.name}")
                plot_water_level_with_fit(station, dates, levels,10)
        else:
                
                print(f'Bad data for {station.name}')


print("PLOTS COMPLETE")
plt.subplots_adjust(wspace=None, hspace=None)
plt.show()
