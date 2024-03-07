from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import station_namelookup, sorted_by_key,polyfit
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold, stations_highest_rel_level, towns_by_highest_rel_level
import datetime
import pprint
import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation

stations = build_station_list()
update_water_levels(stations)

class teststation:
    def __init__(self,name,latest_level,trange,town,coord):
        self.name=name
        self.latest_level=latest_level
        self.typical_range=trange
        self.town=town
        self.coord=coord
    
    def typical_range_consistent(self):

        if self.typical_range == None:
            return False
        
        elif self.typical_range[0] == None or self.typical_range[1] == None: 
            return False
        
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        
        else: return True


    def relative_water_level(self):
        if self.typical_range_consistent() and type(self.latest_level) == float:
            if self.latest_level >= 0:
                """Checks that water level data is as expected - afw44"""

                return (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        else:
            #print('Bad water level data')
            return None
    """Returns the current *relative* level at the station - afw44 """




























def test_relative_water_level():
    assert teststation("A",25.0,(0,5),"dummytown",(0,0)).relative_water_level()==5.0
    assert teststation("B",0.0,(0,10),"dummytown",(0,0)).relative_water_level()==0.0
    assert teststation("D",18.0,(15,21),"dummytown",(0,0)).relative_water_level()==0.5
    assert teststation("C",5.0,(12,5),"dummytown",(0,0)).relative_water_level()==None
    assert teststation("E",15.0,None,"dummytown",(0,0)).relative_water_level()==None
    assert teststation("F",15005.0,(5,15),"dummytown",(0,0)).relative_water_level()==1500

def test_stations_highest_rel_level():
    test_stations = [teststation("A",25.0,(0,5),"dummytown",(0,0)),
                    teststation("B",0.0,(0,10),"dummytown",(0,0)),
                    teststation("C",18.0,(15,21),"dummytown",(0,0)),
                    teststation("D",15005.0,(5,15),"dummytown",(0,0)),
                    teststation("E",3.5,(3,3.00001),"dummytown",(0,0))]
    d = stations_highest_rel_level(test_stations,2)
    assert d == [('A', 5.0),('D', 1500.0)]

def test_stations_level_over_threshold():
    test_stations = [teststation("A",25.0,(0,5),"dummytown",(0,0)),
                    teststation("B",0.0,(0,10),"dummytown",(0,0)),
                    teststation("C",18.0,(15,21),"dummytown",(0,0)),
                    teststation("D",15005.0,(5,15),"dummytown",(0,0)),
                    teststation("E",3.5,(3,3.00001),"dummytown",(0,0))]
    e = stations_level_over_threshold(test_stations,10)
    assert e == [('D', 1500.0),('E', 50000.0)]

def test_towns_by_highest_rel_level():
    test_stations = [teststation("A",25.0,(0,5),"Alpha",(0,0)),
                    teststation("B",0.0,(0,10),"Beta",(0,0)),
                    teststation("C",18.0,(15,21),"Gamma",(0,0)),
                    teststation("D",15005.0,(5,15),"Delta",(0,0)),
                    teststation("E",3.5,(3,3.00001),"Epsilon",(0,0))]
    
    f = towns_by_highest_rel_level(test_stations)
    assert f[0] == ['Beta', 0.0, 1,(0,0)]
    assert f[3] == ['Delta', 1500.0, 1,(0,0)]