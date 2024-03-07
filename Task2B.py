
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold
import pprint


stations = build_station_list()
update_water_levels(stations)

print()
print('Stations whose relative level is over 0.8:')
pprint.pp(stations_level_over_threshold(stations, 0.8))
print()
print('Stations whose relative level is over 2.5:')
pprint.pp(stations_level_over_threshold(stations, 2.5))


"""Calls and displays the level threshold function from flood.py - afw44"""



