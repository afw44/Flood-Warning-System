import numpy as np
import floodsystem

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):

        if self.typical_range == None:
            return False
        
        elif self.typical_range[0] == None or self.typical_range[1] == None: 
            return False
        
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        
        else: return True

    """Truth test to check whether the range is not NoneType, and correctly ordered - afw44 """

    def relative_water_level(self):
        if self.typical_range_consistent() and type(self.latest_level) == float:
            if self.latest_level >= 0:
                """Checks that water level data is as expected - afw44"""

                return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        else:
            #print('Bad water level data')
            return None

    """Returns the current *relative* level at the station - afw44 """


def inconsistent_typical_range_stations(stations):

    """Builds list of bools for whether the range is consistent or not, then builds index list of (False bool) - afw44 """
    indices = [i for i, x in enumerate(
                [station.typical_range_consistent() for station in stations])
                  if x == False]
    """Returns stations at the 'False' indices - afw44 """

    inconsistent_stations = np.array(stations)[indices]

    for station in inconsistent_stations:
        if station.typical_range != None:
            assert sorted(station.typical_range) != station.typical_range
        else:
            assert station.typical_range == None
    """ Tests that every station in the list either has 'None' for their typical range, or has the range out of order - afw44 """

    return inconsistent_stations

