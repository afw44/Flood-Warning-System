import pprint
from floodsystem.geo import stations_by_distance, station_distance
from floodsystem.utils import station_namelookup
from floodsystem.stationdata import build_station_list
import numpy as np



p = (52.2053, 0.1218)
"""Coordinate from which to evaluate distances - afw44 """

station_list = build_station_list(use_cache = True)
"""Fetches list of MonitoringStation objects - afw44 """

sorted_station_tuples = stations_by_distance(station_list,p)
"""Fetches list of sorted (name, distance) tuples - afw44 """

sorted_station_tuples = [(station_tup[0], station_namelookup(station_list, station_tup[0]).town, station_tup[1])
                         for station_tup in sorted_station_tuples]
"""Looks up each station based on name, then creates a (name,town,distance) tuple - afw44 """

print('\nClosest 10 stations:')
pprint.pp(sorted_station_tuples[:10])

print('\nFurthest 10 stations:')
pprint.pp(sorted_station_tuples[-10:])





