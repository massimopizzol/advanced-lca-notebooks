# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:50:12 2021

@author: GF20PZ
"""

#Projects backup
import bw2data
import bw2io
from bw2data.parameters import *
import brightway2 as bw


#Create an archive file IN YOUR ROOT (/C, or User)
bw2io.backup.backup_project_directory('AH_38') #The name of your project



#restore intital status of project on any machine
##(You have to give the right path)
bw2io.restore_project_directory('brightway2-project-AH_38_naturalgas_2_0711-backup.10-November-2022-01-36PM.tar.gz')


#This creates the project in brigthway.
