import pprint
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key  # noqa


stations_within_cambridge = stations_within_radius(build_station_list(use_cache = True), 10, (52.2053, 0.1218))
"Finds all stations within the radius of required coordinates on the given data - bhyw2"
pprint.pp(stations_within_cambridge)