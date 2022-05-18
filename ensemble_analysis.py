#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:30:10 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew
import seaborn as sns

###################################
### load data and collect stats ###
###################################

# 25 rms
ice_vol_25rms_25fdim = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)
ice_vol_25rms_50fdim = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0)
ice_vol_25rms_75fdim = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0)
ice_vol_25rms_10fdim = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)
# mean over 1000 years
ice_vol_25rms_25fdim['mean'] = ice_vol_25rms_25fdim.mean(axis=1)
ice_vol_25rms_50fdim['mean'] = ice_vol_25rms_50fdim.mean(axis=1)
ice_vol_25rms_75fdim['mean'] = ice_vol_25rms_75fdim.mean(axis=1)
ice_vol_25rms_10fdim['mean'] = ice_vol_25rms_10fdim.mean(axis=1)

# data through 500 years
ice_vol_25rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_25rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_25rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_25rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,500))
# mean over 500 years
ice_vol_25rms_25fdim_500['mean'] = ice_vol_25rms_25fdim_500.mean(axis=1)
ice_vol_25rms_50fdim_500['mean'] = ice_vol_25rms_50fdim_500.mean(axis=1)
ice_vol_25rms_75fdim_500['mean'] = ice_vol_25rms_75fdim_500.mean(axis=1)
ice_vol_25rms_10fdim_500['mean'] = ice_vol_25rms_10fdim_500.mean(axis=1)

# data through last 250 years
ice_vol_25rms_25fdim_750 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_25rms_50fdim_750 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_25rms_75fdim_750 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_25rms_10fdim_750 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,750))
# mean over 250 years
ice_vol_25rms_25fdim_750['mean'] = ice_vol_25rms_25fdim_750.mean(axis=1)
ice_vol_25rms_50fdim_750['mean'] = ice_vol_25rms_50fdim_750.mean(axis=1)
ice_vol_25rms_75fdim_750['mean'] = ice_vol_25rms_75fdim_750.mean(axis=1)
ice_vol_25rms_10fdim_750['mean'] = ice_vol_25rms_10fdim_750.mean(axis=1)

# data through last 100 years
ice_vol_25rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_25rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_25rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_25rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,900))
# mean over 100 years
ice_vol_25rms_25fdim_900['mean'] = ice_vol_25rms_25fdim_900.mean(axis=1)
ice_vol_25rms_50fdim_900['mean'] = ice_vol_25rms_50fdim_900.mean(axis=1)
ice_vol_25rms_75fdim_900['mean'] = ice_vol_25rms_75fdim_900.mean(axis=1)
ice_vol_25rms_10fdim_900['mean'] = ice_vol_25rms_10fdim_900.mean(axis=1)

#mean over last 50 years
ice_vol_25rms_25fdim_950 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_25rms_50fdim_950 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_25rms_75fdim_950 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_25rms_10fdim_950 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,950))
# mean over 50 years
ice_vol_25rms_25fdim_950['mean'] = ice_vol_25rms_25fdim_900.mean(axis=1)
ice_vol_25rms_50fdim_950['mean'] = ice_vol_25rms_50fdim_900.mean(axis=1)
ice_vol_25rms_75fdim_950['mean'] = ice_vol_25rms_75fdim_900.mean(axis=1)
ice_vol_25rms_10fdim_950['mean'] = ice_vol_25rms_10fdim_900.mean(axis=1)




# 50 rms
ice_vol_50rms_25fdim = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0)
ice_vol_50rms_50fdim = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0)
ice_vol_50rms_75fdim = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0)
ice_vol_50rms_10fdim = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0)
# mean over 1000 years
ice_vol_50rms_25fdim['mean'] = ice_vol_50rms_25fdim.mean(axis=1)
ice_vol_50rms_50fdim['mean'] = ice_vol_50rms_50fdim.mean(axis=1)
ice_vol_50rms_75fdim['mean'] = ice_vol_50rms_75fdim.mean(axis=1)
ice_vol_50rms_10fdim['mean'] = ice_vol_50rms_10fdim.mean(axis=1)

# data through 500 years
ice_vol_50rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_50rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_50rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,500))
ice_vol_50rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,500))
# mean over 500 years
ice_vol_50rms_25fdim_500['mean'] = ice_vol_50rms_25fdim_500.mean(axis=1)
ice_vol_50rms_50fdim_500['mean'] = ice_vol_50rms_50fdim_500.mean(axis=1)
ice_vol_50rms_75fdim_500['mean'] = ice_vol_50rms_75fdim_500.mean(axis=1)
ice_vol_50rms_10fdim_500['mean'] = ice_vol_50rms_10fdim_500.mean(axis=1)

# data through last 250 years
ice_vol_50rms_25fdim_750 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_50rms_50fdim_750 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_50rms_75fdim_750 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,750))
ice_vol_50rms_10fdim_750 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,750))
# mean over 250 years
ice_vol_50rms_25fdim_750['mean'] = ice_vol_50rms_25fdim_750.mean(axis=1)
ice_vol_50rms_50fdim_750['mean'] = ice_vol_50rms_50fdim_750.mean(axis=1)
ice_vol_50rms_75fdim_750['mean'] = ice_vol_50rms_75fdim_750.mean(axis=1)
ice_vol_50rms_10fdim_750['mean'] = ice_vol_50rms_10fdim_750.mean(axis=1)

# data through last 100 years
ice_vol_50rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_50rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_50rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,900))
ice_vol_50rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,900))
# mean over 100 years
ice_vol_50rms_25fdim_900['mean'] = ice_vol_50rms_25fdim_900.mean(axis=1)
ice_vol_50rms_50fdim_900['mean'] = ice_vol_50rms_50fdim_900.mean(axis=1)
ice_vol_50rms_75fdim_900['mean'] = ice_vol_50rms_75fdim_900.mean(axis=1)
ice_vol_50rms_10fdim_900['mean'] = ice_vol_50rms_10fdim_900.mean(axis=1)

#mean over last 50 years
ice_vol_50rms_25fdim_950 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_50rms_50fdim_950 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_50rms_75fdim_950 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,950))
ice_vol_50rms_10fdim_950 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,950))
# mean over 50 years
ice_vol_50rms_25fdim_950['mean'] = ice_vol_50rms_25fdim_900.mean(axis=1)
ice_vol_50rms_50fdim_950['mean'] = ice_vol_50rms_50fdim_900.mean(axis=1)
ice_vol_50rms_75fdim_950['mean'] = ice_vol_50rms_75fdim_900.mean(axis=1)
ice_vol_50rms_10fdim_950['mean'] = ice_vol_50rms_10fdim_900.mean(axis=1)




# 75 rms
ice_vol_75rms_25fdim = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0)
ice_vol_75rms_50fdim = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0)
ice_vol_75rms_75fdim = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0)
ice_vol_75rms_10fdim = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0)
# mean over 1000 years
ice_vol_75rms_25fdim['mean'] = ice_vol_75rms_25fdim.mean(axis=1)
ice_vol_75rms_50fdim['mean'] = ice_vol_75rms_50fdim.mean(axis=1)
ice_vol_75rms_75fdim['mean'] = ice_vol_75rms_75fdim.mean(axis=1)
ice_vol_75rms_10fdim['mean'] = ice_vol_75rms_10fdim.mean(axis=1)

# 100 rms
ice_vol_100rms_25fdim = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0)
ice_vol_100rms_50fdim = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0)
ice_vol_100rms_75fdim = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0)
ice_vol_100rms_10fdim = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0)
# mean over 1000 years
ice_vol_100rms_25fdim['mean'] = ice_vol_100rms_25fdim.mean(axis=1)
ice_vol_100rms_50fdim['mean'] = ice_vol_100rms_50fdim.mean(axis=1)
ice_vol_100rms_75fdim['mean'] = ice_vol_100rms_75fdim.mean(axis=1)
ice_vol_100rms_10fdim['mean'] = ice_vol_100rms_10fdim.mean(axis=1)


###################################
############## plot ###############
###################################

### through 1000 years ###
plt.figure()
sns.kdeplot(data=ice_vol_25rms_25fdim)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim over 1000 years')
plt.legend([],[], frameon=False) 
# 25 rms .50 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_50fdim)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.50 fdim over 1000 years')
plt.legend([],[], frameon=False) 
# 25 rms .75 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_75fdim)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.75 fdim over 1000 years')
plt.legend([],[], frameon=False) 
# 25 rms 1.0 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_10fdim)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 1.0 fdim over 1000 years')
plt.legend([],[], frameon=False) 


### last 500 years ###
# 25 rms .25 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_25fdim_500)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim through last 500 years')
plt.legend([],[], frameon=False) 
# 25 rms .25 fdim - mean 
# plt.figure()
# sns.kdeplot(data=ice_vol_25rms_25fdim_500['mean'])
# plt.xlabel('volume (m^3)')
# plt.title('gaussian KDE for 25 rms, 0.25 fdim through first 500 years - mean')
# plt.legend([],[], frameon=False)

# 25 rms .50 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_50fdim_500)
plt.xlabel('volume change (m^3)')
plt.title('gaussian KDE for 25 rms, 0.50 fdim through last 500 years')
plt.legend([],[], frameon=False)
# # 25 rms 5.0 fdim - mean 
# plt.figure()
# sns.kdeplot(data=ice_vol_25rms_50fdim_500['mean'])
# plt.xlabel('volume (m^3)')
# plt.title('gaussian KDE for 25 rms, 0.50 fdim through first 500 years - mean')
# plt.legend([],[], frameon=False)

# 25 rms .75 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_75fdim_500)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.75 fdim through last 500 years')
plt.legend([],[], frameon=False)
# # 25 rms .75 fdim - mean 
# plt.figure()
# sns.kdeplot(data=ice_vol_25rms_75fdim_500['mean'])
# plt.xlabel('volume (m^3)')
# plt.title('gaussian KDE for 25 rms, 0.75 fdim through first 500 years - mean')
# plt.legend([],[], frameon=False)

# 25 rms 1.0 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_10fdim_500)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 1.0 fdim through last 500 years')
plt.legend([],[], frameon=False)
# # 25 rms 1.0 fdim - mean 
# plt.figure()
# sns.kdeplot(data=ice_vol_25rms_10fdim_500['mean'])
# plt.xlabel('volume (m^3)')
# plt.title('gaussian KDE for 25 rms, 1.0 fdim through first 500 years - mean')
# plt.legend([],[], frameon=False)


### last 250 years ###
# 25 rms .25 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_25fdim_750)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim through last 250 years')
plt.legend([],[], frameon=False) 
# 25 rms .50 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_50fdim_750)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.50 fdim through last 250 years')
plt.legend([],[], frameon=False) 
# 25 rms .75 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_75fdim_750)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.75 fdim through last 250 years')
plt.legend([],[], frameon=False) 
# 25 rms 1.0 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_10fdim_750)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 1.0 fdim through last 250 years')
plt.legend([],[], frameon=False) 


### last 100 years ###
# 25 rms .25 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_25fdim_900)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim through last 100 years')
plt.legend([],[], frameon=False) 
# 25 rms .50 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_50fdim_900)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.50 fdim through last 100 years')
plt.legend([],[], frameon=False) 
# 25 rms .75 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_75fdim_900)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.75 fdim through last 100 years')
plt.legend([],[], frameon=False) 
# 25 rms 1.0 fdim
plt.figure()
sns.kdeplot(data=ice_vol_25rms_10fdim_900)
plt.xlabel('volume (m^3)')
plt.title('gaussian KDE for 25 rms, 1.0 fdim through last 100 years')
plt.legend([],[], frameon=False) 


### 25 rms all fdim, last 50 years ###
# set up plot matrix
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex = True, sharey=True)
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip(axs,fdims):
    ax.text(0.25,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
sns.kdeplot(data=ice_vol_25rms_25fdim_950, ax = ax1, legend = False,color='seagreen')
sns.kdeplot(data=ice_vol_25rms_50fdim_950, ax = ax2, legend = False,color='seagreen')
sns.kdeplot(data=ice_vol_25rms_75fdim_950, ax = ax3, legend = False,color='seagreen')
sns.kdeplot(data=ice_vol_25rms_10fdim_950, ax = ax4, legend = False,color='seagreen')
plt.xlabel('volume (m^3)')


###################################
###### ice volume over time #######
###################################

### 25 rms ###
# set up plot matrix
plt.title('Ice Volume Over Time - 25 rms, all fdim')
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex = True, sharey=True)
plt.legend([],[], frameon=False)
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip(axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# 25 rms 0.25 fdim
# plt.figure()
ice_vol_25rms_25fdim.plot(ax = ax1)
# plt.title('Ice Volume Over Time - 25 rms, 0.25 fdim')
# plt.xlabel('Time (years)')
# plt.ylabel('volume (m^3)')
# plt.legend([],[], frameon=False) 

# 25 rms 0.50 fdim 
# plt.figure()
ice_vol_25rms_50fdim.plot(ax = ax2)
# plt.title('Ice Volume Over Time - 25 rms, 0.50 fdim')
# plt.xlabel('Time (years)')
# plt.ylabel('volume (m^3)')
# plt.legend([],[], frameon=False) 

# 25 rms 0.75 fdim
# plt.figure()
ice_vol_25rms_75fdim.plot(ax = ax3)
# plt.title('Ice Volume Over Time - 25 rms, 0.75 fdim')
# plt.xlabel('Time (years)')
# plt.ylabel('volume (m^3)')
# plt.legend([],[], frameon=False) 

# 25 rms 1.0 fdim 
# plt.figure()
ice_vol_25rms_10fdim.plot(ax = ax4)
# plt.title('Ice Volume Over Time - 25 rms, 1.0 fdim')
# plt.xlabel('Time (years)')
# plt.ylabel('volume (m^3)')
# plt.legend([],[], frameon=False) 


### 50 rms ###

# 50 rms 0.25 fdim
plt.figure()
ice_vol_50rms_25fdim.plot()
plt.title('Ice Volume Over Time - 50 rms, 0.25 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 50 rms 0.50 fdim 
plt.figure()
ice_vol_50rms_50fdim.plot()
plt.title('Ice Volume Over Time - 50 rms, 0.50 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 50 rms 0.75 fdim
plt.figure()
ice_vol_50rms_75fdim.plot()
plt.title('Ice Volume Over Time - 50 rms, 0.75 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 50 rms 1.0 fdim 
plt.figure()
ice_vol_50rms_10fdim.plot()
plt.title('Ice Volume Over Time - 50 rms, 1.0 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 


### 75 rms ###

# 75 rms 0.25 fdim
plt.figure()
ice_vol_75rms_25fdim.plot()
plt.title('Ice Volume Over Time - 75 rms, 0.25 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 75 rms 0.50 fdim 
plt.figure()
ice_vol_75rms_50fdim.plot()
plt.title('Ice Volume Over Time - 75 rms, 0.50 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 75 rms 0.75 fdim
plt.figure()
ice_vol_75rms_75fdim.plot()
plt.title('Ice Volume Over Time - 75 rms, 0.75 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 75 rms 1.0 fdim 
plt.figure()
ice_vol_75rms_10fdim.plot()
plt.title('Ice Volume Over Time - 75 rms, 1.0 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 


### 100 rms ###

# 100 rms 0.25 fdim
plt.figure()
ice_vol_100rms_25fdim.plot()
plt.title('Ice Volume Over Time - 100 rms, 0.25 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 100 rms 0.50 fdim 
plt.figure()
ice_vol_100rms_50fdim.plot()
plt.title('Ice Volume Over Time - 100 rms, 0.50 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 100 rms 0.75 fdim
plt.figure()
ice_vol_100rms_75fdim.plot()
plt.title('Ice Volume Over Time - 100 rms, 0.75 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 

# 100 rms 1.0 fdim 
plt.figure()
ice_vol_100rms_10fdim.plot()
plt.title('Ice Volume Over Time - 100 rms, 1.0 fdim')
plt.xlabel('Time (years)')
plt.ylabel('volume (m^3)')
plt.legend([],[], frameon=False) 



