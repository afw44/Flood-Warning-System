import pytest
import pprint
import numpy as np
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

inconsistent_stations = inconsistent_typical_range_stations(build_station_list(use_cache=True))
"""Fetches inconsistent stations from the relevant function in station.py - afw44 """

inconsistent_station_names = sorted([station.name for station in inconsistent_stations])
""" Produces alphabetised list of station names from the list of MonitoringClass objects - afw44 """

print('Stations with inconsistent range data:')
pprint.pp(inconsistent_station_names)
"""Displays station names - afw44 """





