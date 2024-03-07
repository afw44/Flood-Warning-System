import pprint
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
import pprint
import numpy as np
from floodsystem.utils import sorted_by_key  # noqa

rivers_with_at_least_one_station = rivers_with_station(build_station_list(use_cache = True))
"Fetches all of the rivers that appear in the given data as a list - bhyw2"

print("\nNumber of rivers:",len(rivers_with_at_least_one_station))
"Prints the number of rivers that appear in the data - bhyw2"

print("\nFirst 10 rivers:",rivers_with_at_least_one_station[:10])
"Prints the first 10 rivers in alphabetical order - bhyw2"



River_finding = stations_by_river(build_station_list(use_cache = True))
"Creates dictionary from the data cache - bhyw2"

stations_in_cambridge = River_finding["River Cam"]
print('\nStations on the River Cam:')
pprint.pp(stations_in_cambridge)
"Displays list of stations on the River Cam - bhyw2"

stations_on_the_thames = River_finding["River Thames"]
print('\nStations on the River Thames:')
pprint.pp(stations_on_the_thames)
"Displays list of stations on the River Thames - bhyw2"

stations_on_aire = River_finding["River Aire"]
print('\nStations on the River Aire:')
pprint.pp(stations_on_aire)
"Displays list of stations on the River Aire - bhyw2"


