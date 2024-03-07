import pprint
from floodsystem.geo import stations_by_distance, station_distance, rivers_by_station_number
from floodsystem.utils import station_namelookup
from floodsystem.stationdata import build_station_list
import numpy as np


station_list = build_station_list(use_cache = True)
"""Fetches list of MonitoringStation objects - afw44 """

print('10 Rivers with most Monitoring Stations:')
pprint.pp(rivers_by_station_number(station_list,10))


