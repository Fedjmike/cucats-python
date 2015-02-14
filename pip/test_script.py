# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 19:01:08 2015

@author: Daniel

This is a script to test the module.
"""

import cucats
from cucats import *

def between(city1,city2):
    lat = (coordinates(city1)[0] + coordinates(city2)[0])/2
    lon = (coordinates(city1)[1] + coordinates(city2)[1])/2
    return(city(lat, lon))



cucats.city_ex.check(between)
