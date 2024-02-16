# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:55:04 2024

@author: pierre.jouannais
"""

# Importing ecoinvent with the ecoinvent_interface package
# See original sources for more info: 

# https://brightway.groups.io/g/updates/message/36
# https://stackoverflow.com/questions/77697351/brightway2-and-ecoinvent-3-10-unlinked-exchanges
# https://github.com/brightway-lca/ecoinvent_interface



from bw2data.parameters import *
import brightway2 as bw

import bw2data as bd
import bw2io as bi


from ecoinvent_interface import Settings, permanent_setting
permanent_setting("username", "xxx") # put your ecoinvent username instead of the xxx
permanent_setting("password", "xxx")  # put your ecoinvent password instead of the xxx


bd.projects.set_current("ecoinvent-3.10-cutoff") # your project

#This downloads and loads ecoinvent and the corresponding biosphere + the methods
bi.import_ecoinvent_release("3.10", "cutoff") # ask for the version 

Ecoinvent = bw.Database('ecoinvent-3.10-cutoff')


# Note that both ecoinvent and biosphere get assigned a name, and the biosphere name has changed (not "biosphere3" as used previously)
