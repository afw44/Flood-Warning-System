from floodsystem.geo import stations_by_distance, station_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

global s_id, m_id, label, coord, trange, river, town

[s_id, m_id, label, coord, trange, river, town] = ["test-s-id","test-m-id","some station",
                                                   "some coord","some trange","River X","My Town"]

def test_rivers_by_station_number():

    stations = build_station_list()
    """Ensures that tests that run on whole dataset pass - afw44 """

    test_stations=[MonitoringStation(s_id, m_id, 'A', coord, trange, 'River1', town),
                   MonitoringStation(s_id, m_id, 'B', coord, trange, 'River1', town),
                   MonitoringStation(s_id, m_id, 'C', coord, trange, 'River2', town),
                   MonitoringStation(s_id, m_id, 'D', coord, trange, 'River2', town),
                   MonitoringStation(s_id, m_id, 'E', coord, trange, 'River2', town)] 
    
    c = rivers_by_station_number(test_stations,2)

    """Builds output list based on the input test stations above - afw44 """

    assert c[0] == ('River1',2)
    assert c[1] == ('River2',3)

    """Checks the output list is of the expected form - afw44 """

def test_stations_by_distance():

    test_stations=[MonitoringStation(s_id, m_id, 'A', (0,0), trange, river, town),
                   MonitoringStation(s_id, m_id, 'B', (-2,0), trange, river, town),
                   MonitoringStation(s_id, m_id, 'C', (-100,-100), trange, river, town)]
    
    """Produces test stations with increasing distance from (0,0) - afw44 """

    c = stations_by_distance(test_stations,(0,0))

    """Sorts stations with function being tested - afw44 """

    assert c[0][0] == 'A'
    assert c[1][0] == 'B'
    assert c[2][0] == 'C'

    """Checks the output list is in the expected order - afw44 """







def test_stations_within_radius():

    test_stations=[MonitoringStation(s_id, m_id, label,(1,1.0001), trange, river, town),
                   MonitoringStation(s_id, m_id, label, (30,40), trange, river, town),
                   MonitoringStation(s_id, m_id, label, (50,60), trange, river, town)]
    

    # Defines arbitrary parameters for testing stations - bhyw2
    
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    # Displays the arbitrary parameters in the same format as the dataset - bhyw2
    
    test_stations=[MonitoringStation(s_id, m_id, label,(1,1.0001), trange, river, town),
                   MonitoringStation(s_id, m_id, label, (30,40), trange, river, town),
                   MonitoringStation(s_id, m_id, label, (50,60), trange, river, town)]
    
    # Data set with 3 stations is created - bhyw2
    
    a = stations_within_radius(test_stations,1,(1,1))
    
    assert len(a)==1
    
    # Only one of the stations is within 1m of (1,1), so it should be the list should only have one item - bhyw2




def test_rivers_with_station():

    # Defines arbitrary parameters for testing stations - bhyw2
    
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    # Displays the arbitrary parameters in the same format as the dataset - bhyw2
    
    test_stations=[MonitoringStation(s_id, m_id, label, coord, trange, "A", town),
                   MonitoringStation(s_id, m_id, label, coord, trange, "B", town),
                   MonitoringStation(s_id, m_id, label, coord, trange, "A", town)]
    
    # Data set with 3 stations is created. Two are on river A and one is on river B - bhyw2
    
    b = rivers_with_station(test_stations)
    
    assert b == ["A","B"]
    
    # Rivers A and B are the only two that appear in the testing data set so when the function is applied the only two rivers are A and B (the duplicate A should not appear). The list has to be sorted alphabetically- bhy2


def test_stations_by_river():  
    # Defines arbitrary parameters for testing stations - bhyw2
    
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    # Displays the arbitrary parameters in the same format as the dataset - bhyw2
    
    test_stations=[MonitoringStation(s_id, m_id, "Gamma", coord, trange, "A", town),
                   MonitoringStation(s_id, m_id, "Delta", coord, trange, "B", town),
                   MonitoringStation(s_id, m_id, "Alpha", coord, trange, "A", town),
                   MonitoringStation(s_id, m_id, "Epsilon", coord, trange, "A", town),
                   MonitoringStation(s_id, m_id, "Beta", coord, trange, "B", town)] 
    
    # Data set with 5 stations is created, with stations Alpha, Gamma and Epsilon along river A and stations Beta and Delta along river B. - bhyw2
    
    c = stations_by_river(test_stations)

    # Dictionary with each river and the corresponding stations is created - bhyw2

    assert c["A"] == ['Alpha', 'Epsilon', 'Gamma']

    # This finds all stations on river A, which should be Alpha, Epsilon and Gamma (in alphabetical order) - bhyw2
    assert c["B"] == ['Beta', 'Delta']

    # This finds all stations on river B, which should be Beta and Delta (in alphabetical order) - bhyw2
