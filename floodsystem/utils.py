import numpy as np
import numpy as np
import numpy.polynomial.polynomial as P


def polyfit(dates, levels, p):
    offset = min(dates)
    dates = (np.array([dates]) - np.ones(len(dates))*offset)[0]
    poly = P.Polynomial.fit(dates,levels,p)
    
    return (poly,offset)


def gradnow(dates, levels,p):
    offset = min(dates)
    dates = (np.array([dates]) - np.ones(len(dates))*offset)[0]
    poly = P.Polynomial.fit(dates,levels,p)
    deriv = poly.deriv(m=1)
    grad_now = deriv(dates[-1])

    return grad_now

def rise_or_fall(levels):
    if np.average(np.array(levels[-10:-6])) < np.average(np.array(levels[-5:-1])):
        return True
    else:
        return False

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple"""

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)


def station_namelookup(station_list,name):

    indexlist = np.argwhere(np.array([station.name for station in station_list]) == name)

    """Looks up a MonitoringStation object from its name - afw44 """   

    if len(indexlist) > 1:
        if station_list[indexlist[0][0]].town == station_list[indexlist[1][0]].town:
            if station_list[indexlist[0][0]].river == station_list[indexlist[1][0]].river:
                print(station_list[indexlist[0][0]])
                print(station_list[indexlist[1][0]])
                assert False 

    """Verifies that if there are stations with the same name, they are not the same station - afw44"""
    
    return station_list[indexlist[0][0]]

def town_namelookup(station_list,name):

    indexlist = np.argwhere(np.array([station.town for station in station_list]) == name)

    """Looks up a MonitoringStation object from its name - afw44 """   
    stations_in_town = []  
    for index in indexlist:
        stations_in_town.append(station_list[index[0]])
    
    """Builds list of stations in a town - afw44"""

    return stations_in_town


def risktypedict_from_cache():

    townrisk_floats = np.genfromtxt('risk_cache_floats.txt',delimiter=',')
    townrisk_strings = np.genfromtxt('risk_cache_strings.txt',delimiter = '/',dtype ='str')
    
    risks = ['Low','Medium','High','Severe']

    """Takes the cached station names and station data, and generates a name:risktype dictionary - afw"""

    return dict([(townrisk_strings[index], risks[int(town[1])]) 
                 for index,town in enumerate(townrisk_floats)])
    

def riskleveldict_from_cache():

    townrisk_floats = np.genfromtxt('risk_cache_floats.txt',delimiter=',')
    townrisk_strings = np.genfromtxt('risk_cache_strings.txt',delimiter = '/',dtype ='str')
    
    risks = ['Low','Medium','High','Severe']

    """Takes the cached station names and station data, and generates a name:risklevel dictionary - afw"""

    return dict([(townrisk_strings[index], town[0]) for index,town in enumerate(townrisk_floats)])
    