
import pprint
import numpy as np
import matplotlib.pyplot as plt
from .utils import polyfit
from datetime import datetime
import geopandas


def plot_water_levels(station, dates, levels):

    for index,level in enumerate(levels):        
        if level>3*station.typical_range[1]:
            #print('Anomaly',dates[index],level)
            levels.pop(index)
            dates.pop(index)
    """ Removes readings that are anomalously large - afw44 """

    for index,level in enumerate(levels):
        if abs(level-levels[index-1]) > 0.05:
            #print('Anomaly',dates[index],level)
            levels.pop(index)
            dates.pop(index)
    """ Removes readings that are discontinuous - afw44 """

    plt.plot(dates,levels,color = 'black')

    """Plots unfiltered data - afw44"""

    plt.plot([dates[0],dates[-1]], station.typical_range[0]*np.array([1,1]),
             c='r', linewidth = 2, linestyle = 'dashed', zorder = 0)
    plt.plot([dates[0],dates[-1]], station.typical_range[1]*np.array([1,1]),
             c='g', linewidth = 2, linestyle = 'dashed', zorder = 0)

    """Adds lower and upper typical range values as dashed lines on the plot - afw44"""

    plt.ylabel('River Depth / m')
    plt.xlabel('Time')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    """Formatting above - afw44"""

    return


def plot_water_level_with_fit(station, dates, levels, p):

    for index,level in enumerate(levels):        
        if level>3*station.typical_range[1]:
            #print('Anomaly',dates[index],level)
            levels.pop(index)
            dates.pop(index)
    """ Removes readings that are anomalously large - afw44 """

    for index,level in enumerate(levels):
        if abs(level-levels[index-1]) > 0.05:
            #print('Anomaly',dates[index],level)
                levels.pop(index)
                dates.pop(index)
    """ Removes readings that are discontinuous - afw44 """

    plt.plot(dates,levels,linewidth = 0.5,color = 'grey')

    """Adds unfitted data in the background for context - afw44"""

    dates = [date.timestamp() for date in dates]

    """Converts dates to timestamp for fitting - afw44"""

    (poly, offset) = polyfit(dates,levels,p)

    """Finds returns a fitting polynomial, and the required time offset - afw44"""

    dates = (np.array([dates]) - np.ones(len(dates))*offset)[0]

    """Reduces dates by offset to smallest values for poly function - afw44 """

    levels = poly(dates)

    """Performs the polynomial fitting with the smaller dates - afw44"""

    dates = [datetime.fromtimestamp(date) 
             for date in (np.array([dates]) + np.ones(len(dates))*offset)[0]]
    
    """Returns dates to original values, and converts back to datetime - afw44"""
    
    plt.plot(dates,levels,linewidth=2,color ='black')

    """Plots dates against levels - afw44"""

    plt.plot([dates[0],dates[-1]], station.typical_range[0]*np.array([1,1]),
             c='r', linewidth = 2, linestyle = 'dashed', zorder = 0)
    plt.plot([dates[0],dates[-1]], station.typical_range[1]*np.array([1,1]),
             c='g', linewidth = 2, linestyle = 'dashed', zorder = 0)
    
    """Adds lower and upper typical range values as dashed lines on the plot - afw44"""

    plt.ylabel('River Depth / m')
    plt.xlabel('Time')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    """Formatting above - afw44"""
    
    return


def mapplot(townrisk_floats):

    world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
    ax = world[world.name == 'United Kingdom'].plot(color='white', edgecolor='black')

    plt.plot(ax=ax, color='red')
    colours = ['b','g','y','r']

    for town in townrisk_floats:
        plt.scatter(town[3],town[2],color = colours[int(town[1])],
                    s = 50*(town[1]+0.5),edgecolors='black',alpha = (0.3*(town[1]) + 0.1))
    """Plots stations on a map of the UK, with colour corresponding to risk type - afw44 """
