import pprint
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key  # noqa


def station_distance(station, p):

    r = 6371
    """Radius of earth in km - afw44 """

    [lon1,lat1,lon2,lat2] = (np.array([station.coord[0], station.coord[1], p[0],p[1]])*np.pi/180).tolist()
    """Fetches coordinates and converts them to raidans"""

    a = np.sin((lon2 - lon1)/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin((lat2 - lat1)/2)**2
    d = 2 * r * np.arcsin(np.sqrt(a))
    """Computes distance in km between input coordinates - afw44 """

    return np.round(d,3)


def stations_by_distance(stations, p):
    """Reads in a list of MonitoringStation objects and a coordinate, 

    then returns a (stationname, distance from p) list sorted by distance - afw44"""

    names = [station.name for station in stations]
    """Makes list of labels for every station in the list - afw44 """

    distances = [station_distance(station, p) for station in stations]
    """Makes list of distances for every station - afw44 """

    for d in distances:
        assert 0 <= d < 20000
    """Checks distances are within a reasonable range, ie non-negative and less than half circumference of earth - afw44 """

    station_distance_tuples = [(names[i],distances[i]) for i in range(len(names))]
    """Makes list of (name, distance from p) tuples - afw44 """

    return sorted_by_key(station_distance_tuples,1)



def rivers_by_station_number(stations, N):
    """Reads in a list of MonitoringStation objects and returns the N rivers with the most stations

    Output is a list of (River name, # of stations) tuples - afw44 """

    stations_by_river_dict = stations_by_river(stations)

    """Fetches dictionary of rivers ---> stations on river, from the stations_by_river function - afw44 """

    sorted_river_lengths = sorted_by_key([(river,len(stations_by_river_dict[river])) 
                          for river in rivers_with_station(stations)],1)
    
    """Builds list of tuples. River station count is list length of output from dictionary.
    .util function sorts ascending by number of stations. - afw44 """

    for rivertup in sorted_river_lengths:
        assert 1 <= rivertup[1]
        """Checks there are no rivers listed with no stations - afw44 """

        assert len(rivertup) == 2 and type(rivertup) == tuple
        """Checks the output is in the right format - afw44 """

        assert rivertup[1] == int(rivertup[1])
        """Checks there are no no-integer number of rivers - afw44"""

    assert len(sorted_river_lengths) >= N
    """Checks that there are more than N rivers represented - afw44 """

    return sorted_river_lengths[-N:]
    """Only returns the final N entries in the sorted list - afw44 """



def stations_within_radius(stations,r,centre):

    stations_howfar = [(station.name,station_distance(station,centre)) for station in stations]

    "Obtains the distance of each station from input"
    correct_stations=[]
    "Empty list where stations will be added"
    for i in stations_howfar:
        if i[1] < r:
            correct_stations.append(i)
    "Only adds station to list if its distance to the input is less than r"
    return correct_stations


def rivers_with_station(stations):
    rivers = [station.river for station in stations]
    "Makes lists of the rivers for every station in the list"
    list_of_rivers=[]
    "Empty list where rivers will be added"
    for n in rivers:
        list_of_rivers.append(n) if n not in list_of_rivers else list_of_rivers
        list_of_rivers.sort()
    "River is added only if it is not present on the list, preventing duplicates"
    return list_of_rivers


def stations_by_river(stations):
    random_dictionary = {}
    for a in stations:
        stations_in_river = []
        for b in stations:
            if b.river == a.river:
                stations_in_river.append(b.name)
            stations_in_river.sort()
    
        random_dictionary.update({a.river: stations_in_river})
    return random_dictionary

    """Makes lists of names and corresponding rivers for every station in the list, then converts the two lists into a dictionary"""



