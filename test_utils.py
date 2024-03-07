"""Unit test for the utils module"""

import floodsystem.utils
from floodsystem.station import MonitoringStation
from floodsystem.utils import station_namelookup,town_namelookup
from floodsystem.stationdata import build_station_list
from floodsystem.utils import rise_or_fall,gradnow,polyfit


def test_rise_or_fall():
    test_levels1 = [1,2,3,4,5,6,7,8,9,10]
    test_levels2 = [10,9,8,7,6,5,4,3,2,1]

    assert rise_or_fall(test_levels1) == True
    assert rise_or_fall(test_levels2) == False

    """Checks rise_or_fall can distinguish a climbing flow from a descending one - afw44"""

def test_gradnow():
    dates = [1,2,3,4,5,6,7,8,9,10]

    test_levels1 = [1,2,3,4,5,6,7,8,9,10]
    test_levels2 = [1,2,3,4,5,6,7,8,9,11]
    test_levels3 = [10,9,8,7,6,5,4,3,2,1]

    assert gradnow(dates,test_levels1,4) > 0 
    assert gradnow(dates,test_levels2,4) > gradnow(dates,test_levels1,4)
    assert gradnow(dates,test_levels3,4) < 0

    """Checks gradnow can compare rates of ascent - afw44"""


def test_polyfit():
    dates1 = [100,101,102,103,104,105,106,107,108,109]
    dates2 = [0,1,2,3,4,5,6,7,8,9]

    levels = [0,1,2,3,4,5,6,7,8,9]

    poly,offset = polyfit(dates1,levels,2)
    assert round(poly(5.5 + offset),1) == offset + 5.5

    poly,offset = polyfit(dates2,levels,2)
    assert round(poly(5.5 + offset),1) == offset + 5.5

    """Checks polyfit can quadratically interpolate simple datasets, and handle offsets - afw44"""

    







global s_id, m_id, label, coord, trange, river, town

[s_id, m_id, label, coord, trange, river, town] = ["test-s-id","test-m-id","some station",
                                                   "some coord","some trange","River X","My Town"]

def test_station_namelookup():

    test_stations=[MonitoringStation(s_id, m_id, 'A', coord, trange, 'River1', town),
                MonitoringStation(s_id, m_id, 'B', coord, trange, 'River1', town),
                MonitoringStation(s_id, m_id, 'C', coord, trange, 'River2', town),
                MonitoringStation(s_id, m_id, 'D', coord, trange, 'River2', town),
                MonitoringStation(s_id, m_id, 'E', coord, trange, 'River2', town)] 

    test_names = ['A','B','C','D','E']

    assert station_namelookup(test_stations, 'A') == test_stations[0]
    assert station_namelookup(test_stations, 'C') == test_stations[2]
    
    """Checks the utility can successfully return a MonitoringStation object from a list, using its name as a key - afw44 """


def test_townname_lookup():
    stations = build_station_list()
    names = [station.name for station in town_namelookup(stations,'Cambridge')]

    assert names == ['Cambridge Jesus Lock','Bin Brook','Cambridge']

    """Checks utility can find all stations in a given town - afw44"""


def test_sort():
    """Test sort container by specific index"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2)
    assert list1[0] == b
    assert list1[1] == a
    assert list1[2] == c


def test_reverse_sort():
    """Test sort container by specific index (reverse)"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2, reverse=True)
    assert list1[0] == c
    assert list1[1] == a
    assert list1[2] == b



