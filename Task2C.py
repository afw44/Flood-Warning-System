from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import station_namelookup, sorted_by_key,polyfit
from floodsystem.flood import stations_highest_rel_level
import datetime
import pprint
import matplotlib.pyplot as plt


stations = build_station_list()
update_water_levels(stations)

print()
print('Stations with highest relative level:')
pprint.pp(stations_highest_rel_level(stations,10))
print()

"""Calls and displays the highest relative level function from flood.py - afw44"""
