
from .utils import sorted_by_key
import numpy as np
from floodsystem.utils import station_namelookup, town_namelookup
from .utils import gradnow
from .stationdata import update_water_levels
import pprint
import datetime
from .datafetcher import fetch_measure_levels
from numpy import asarray
from numpy import savetxt


def stations_level_over_threshold(stations, tol):
    """Returns (name,relative_level) for stations whose relative level is above a tolerance - afw44"""
    return [(station.name,np.round(station.relative_water_level(),3)) 
                          for station in stations
                          if type(station.relative_water_level()) == float 
                          and station.relative_water_level() > tol]


def stations_highest_rel_level(stations, N):
    """Returns the N stations with the highest relative level - afw44"""
    return (sorted_by_key([(station.name, np.round(station.relative_water_level(),3)) 
                                for station in stations 
                                if type(station.relative_water_level()) == float],1)[-N-1:-1])


def towns_by_highest_rel_level(stations):
    town_names = []
    clean_stations = [station for station in stations if type(station.relative_water_level()) == float]
    """Only proceeds with stations that have floats as their relative level, rather than NoneType - afw44"""

    for station in clean_stations:
            if station.town not in town_names:
                town_names.append(station.town)
    """Builds list of unique town names - afw44"""
    
    ttups = []
    for town in town_names:
        stations_in_town  = town_namelookup(clean_stations,town) 
        town_average = np.average(np.array([station.relative_water_level() for station in stations_in_town]))
        """Gets average station level within a town - afw44"""

        ttups.append([town,town_average,len(stations_in_town),stations_in_town[0].coord])
        """Adds (name, average_level,number of stations in town, coordinates of town) to ttups - afw44"""
    
    ttups = sorted_by_key(ttups,1)
    """Sorts ttups by average level - afw44"""

    return(ttups)

"""Fetches all station relative levels, filters bad data, sorts stations by relative level - afw44"""


def update_risk_caches(stations):

    print('CACHE UPDATE INITIATED')
    print()
    update_water_levels(stations)
    print('WATER LEVELS UPDATED')
    print()
    sorted_towns = towns_by_highest_rel_level(stations)

    
    all_towns = []
    """Sets up array of stationdata to be sorted - afw44"""

    high_level = []
    """Sets up array of stationdata for further analysis than just level - afw44"""


    for ttup in sorted_towns:
        if ttup[1] < 0.5:
            all_towns.append([ttup[0],ttup[1],0,0,ttup[3][0],ttup[3][1]])
        elif ttup[1] < 1.5:
            all_towns.append([ttup[0],ttup[1],1,0,ttup[3][0],ttup[3][1]])
        else:
            high_level.append(ttup)

    """Categorises stations into: low risk (0->0.5), med risk (0.5->1.5), and passes rest into gradient analysis - afw44"""
    

    print('LOW AND MEDIUM RISKS ASSESSED')
    print()


    for ttup in high_level:
        stations_in_town = town_namelookup(stations, ttup[0])
        grads_in_town = []
        for station in stations_in_town:
            
            dates, levels = fetch_measure_levels(
                    station.measure_id, dt=datetime.timedelta(days = 1))
            
            """Fetches dates and levels - afw44 """

            dates = np.array([date.timestamp() for date in dates][-10:-1])
            levels = levels[-10:-1]

            """Slices only 10 most recent readings - afw44"""

            if len(dates) > 0:
                grads_in_town.append(gradnow(dates, levels,1))
                """Adds gradient at station to town gradients list - afw44"""
            else:
                grads_in_town.append(0)
                """Handles error cases - afw44"""
            
        ave_grad_in_town = np.average(np.array(grads_in_town))
        """Averages gradients in town - afw44"""

        high_subtowns = []

        if ave_grad_in_town > 0:
            high_subtowns.append([ttup[0],ttup[1],3,ave_grad_in_town,ttup[3][0],ttup[3][1]])
            print(f'Severe: {ttup[0]}, Rising')

        else:
            high_subtowns.append([ttup[0],ttup[1],2,ave_grad_in_town,ttup[3][0],ttup[3][1]])
            print(f'High: {ttup[0]}, Falling')
            
        """Decides whether high level stations are Severe or High risk, based on whether level is rising or falling - afw44"""

        high_subtowns = sorted_by_key(high_subtowns,3)
        """Sorts High/Severe risks by gradient not level - afw44"""

        for town in high_subtowns:
            all_towns.append(town)

    pprint.pp(all_towns)

    all_towns = np.array(all_towns)
    print(all_towns[:,3])

    all_towns[:,3] = all_towns[:,3] - (np.min(all_towns[:,3]))*np.ones(len(all_towns[:,3]))
    print(all_towns[:,3])
    """Normalises gradients to be only positive - afw44 """
    
    all_towns[:,3] = all_towns[:,3] / np.max(all_towns[:,3])
    print(all_towns[:,3])

    """Normalises gradients to range from 0->1 - afw44"""

    all_towns[:,3] *= all_towns[:,1]
    print(all_towns[:,3])

    """Multiplies level by rate at which the level is increasing to come up with a weighted risk measurement - afw44"""

    all_towns[:,3] = all_towns[:,3] - (np.min(all_towns[:,3]))*np.ones(len(all_towns[:,3]))
    print(all_towns[:,3])
    """Normalises risks to be only positive - afw44 """

    all_towns[:,3] /= (np.max(all_towns[:,3]))
    print(all_towns[:,3])
    """Again normalises risks to range from 0->1 - afw44"""
    
    sorted_by_key(all_towns,4)

    print(all_towns[:,3])
    townrisk_floats = np.array([[round(ttup[3],2),ttup[2],ttup[4],ttup[5]] for ttup in all_towns])
    townrisk_strings = np.array([ttup[0] for ttup in all_towns])
    
    townrisks = np.array([[ttup[0],round(ttup[3],2),ttup[2],ttup[4],ttup[5]] for ttup in all_towns])
    pprint.pp(townrisks)

    savetxt('risk_cache_floats.txt', townrisk_floats, delimiter=',')
    savetxt('risk_cache_strings.txt', townrisk_strings, delimiter=',',fmt = '%s')

    """Caches risk levels - afw44"""

    return townrisks

