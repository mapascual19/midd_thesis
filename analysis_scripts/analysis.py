#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:46:40 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
#import seaborn

### read csv ###
ice_vol_25rms_10fdim = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)
ice_vol_25rms_25fdim = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)

#plot 
plt.hist(ice_vol_25rms_25fdim, log=True) # makes basic histogram, bins=[1000000, 3000000, 5000000, 7000000]
plt.hist(ice_vol_25rms_10fdim, log=True) # makes basic histogram, bins=[1000000, 3000000, 5000000, 7000000]

# ice_vol_data[['Trial3','Trial4']].plot()
# plt.xlabel('time (years)')
# plt.ylabel('ice volume (m^3)')
# plt.title('Ice Volume Trials 3 and 4 for 100 rms 0.50 fdim')

##########################
### first plot attempt ###
##########################
# time = ice_vol_data_75rms_75fdim['Index']

# ice_vol_data_75rms_75fdim.plot(kind = 'scatter',
#         x = time,
#         y = 'Trial0',
#         color = 'green')
# ice_vol_data_75rms_75fdim.plot(kind = 'scatter',
#         x = time,
#         y = 'Trial1',
#         color = 'blue')
# plt.show
##########################
##########################

#X = []
#Y = [100]

#a = np.loadtxt('ice_vol_data_75rms_75fdim.csv')

# with open('ice_vol_data.txt', 'r') as datafile:
#       plotting = csv.reader(datafile, delimiter=',')
#       for ROWS in plotting: 
#           X.append(float(ROWS[0]))

# # plt.plot(X,Y)
# # plt.title('sed_surface at time t')
# # plt.xlabel('time')
# # plt.ylabel('sed_surface')


# # Michael's scratch work

# y_surf = np.array(X)
# x_vals = np.arange(0,len(y_surf),1)
# plt.plot(x_vals, y_surf)
# plt.ylabel('sed_surface (m)')
# plt.xlabel('number of points along glacier (?)')
