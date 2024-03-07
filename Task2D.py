import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.utils import station_namelookup

def run():

    station = station_namelookup(build_station_list(),'Whaddon')

    # Fetch data over past 2 days
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=2))

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()

