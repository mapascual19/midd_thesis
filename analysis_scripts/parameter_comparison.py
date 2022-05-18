#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 00:12:59 2022

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
ice_vol_25rms_25fdim = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_25rms_50fdim = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_25rms_75fdim = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_25rms_10fdim = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,800))
## vol change
### 25 rms .25 fdim
vol_first_25rms_25fdim = ice_vol_25rms_25fdim.iloc[0,:]
vol_end_25rms_25fdim = ice_vol_25rms_25fdim.iloc[200,:]
vc_25rms_25fdim = np.subtract(vol_end_25rms_25fdim,vol_first_25rms_25fdim)
vc_25rms_25fdim_mean = np.mean(vc_25rms_25fdim)
vc_25rms_25fdim_skew = skew(vc_25rms_25fdim)
vc_25rms_25fdim_std = np.std(vc_25rms_25fdim)
### 25 rms .50 fdim
vol_first_25rms_50fdim = ice_vol_25rms_50fdim.iloc[0,:]
vol_end_25rms_50fdim = ice_vol_25rms_50fdim.iloc[200,:]
vc_25rms_50fdim = np.subtract(vol_end_25rms_50fdim,vol_first_25rms_50fdim)
vc_25rms_50fdim_mean = np.mean(vc_25rms_50fdim)
vc_25rms_50fdim_skew = skew(vc_25rms_50fdim)
vc_25rms_50fdim_std = np.std(vc_25rms_50fdim)
### 25 rms .75 fdim
vol_first_25rms_75fdim = ice_vol_25rms_75fdim.iloc[0,:]
vol_end_25rms_75fdim = ice_vol_25rms_75fdim.iloc[200,:]
vc_25rms_75fdim = np.subtract(vol_end_25rms_75fdim,vol_first_25rms_75fdim)
vc_25rms_75fdim_mean = np.mean(vc_25rms_75fdim)
vc_25rms_75fdim_skew = skew(vc_25rms_75fdim)
vc_25rms_75fdim_std = np.std(vc_25rms_75fdim)
### 25 rms 1.0 fdim
vol_first_25rms_10fdim = ice_vol_25rms_10fdim.iloc[0,:]
vol_end_25rms_10fdim = ice_vol_25rms_10fdim.iloc[200,:]
vc_25rms_10fdim = np.subtract(vol_end_25rms_10fdim,vol_first_25rms_10fdim)
vc_25rms_10fdim_mean = np.mean(vc_25rms_10fdim)
vc_25rms_10fdim_skew = skew(vc_25rms_10fdim)
vc_25rms_10fdim_std = np.std(vc_25rms_10fdim)


# 50 rms
ice_vol_50rms_25fdim = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_50rms_50fdim = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_50rms_75fdim = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_50rms_10fdim = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,800))
## vol change
### 50 rms .25 fdim
vol_first_50rms_25fdim = ice_vol_50rms_25fdim.iloc[0,:]
vol_end_50rms_25fdim = ice_vol_50rms_25fdim.iloc[200,:]
vc_50rms_25fdim = np.subtract(vol_end_50rms_25fdim,vol_first_50rms_25fdim)
vc_50rms_25fdim_mean = np.mean(vc_50rms_25fdim)
vc_50rms_25fdim_skew = skew(vc_50rms_25fdim)
vc_50rms_25fdim_std = np.std(vc_50rms_25fdim)
### 50 rms .50 fdim
vol_first_50rms_50fdim = ice_vol_50rms_50fdim.iloc[0,:]
vol_end_50rms_50fdim = ice_vol_50rms_50fdim.iloc[200,:]
vc_50rms_50fdim = np.subtract(vol_end_50rms_50fdim,vol_first_50rms_50fdim)
vc_50rms_50fdim_mean = np.mean(vc_50rms_50fdim)
vc_50rms_50fdim_skew = skew(vc_50rms_50fdim)
vc_50rms_50fdim_std = np.std(vc_50rms_50fdim)
### 50 rms .75 fdim
vol_first_50rms_75fdim = ice_vol_50rms_75fdim.iloc[0,:]
vol_end_50rms_75fdim = ice_vol_50rms_75fdim.iloc[200,:]
vc_50rms_75fdim = np.subtract(vol_end_50rms_75fdim,vol_first_50rms_75fdim)
vc_50rms_75fdim_mean = np.mean(vc_50rms_75fdim)
vc_50rms_75fdim_skew = skew(vc_50rms_75fdim)
vc_50rms_75fdim_std = np.std(vc_50rms_75fdim)
### 50 rms 1.0 fdim
vol_first_50rms_10fdim = ice_vol_50rms_10fdim.iloc[0,:]
vol_end_50rms_10fdim = ice_vol_50rms_10fdim.iloc[200,:]
vc_50rms_10fdim = np.subtract(vol_end_50rms_10fdim,vol_first_50rms_10fdim)
vc_50rms_10fdim_mean = np.mean(vc_50rms_10fdim)
vc_50rms_10fdim_skew = skew(vc_50rms_10fdim)
vc_50rms_10fdim_std = np.std(vc_50rms_10fdim)


# 75 rms
ice_vol_75rms_25fdim = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_75rms_50fdim = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_75rms_75fdim = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_75rms_10fdim = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,800))
## vol change
### 75 rms .25 fdim
vol_first_75rms_25fdim = ice_vol_75rms_25fdim.iloc[0,:]
vol_end_75rms_25fdim = ice_vol_75rms_25fdim.iloc[200,:]
vc_75rms_25fdim = np.subtract(vol_end_75rms_25fdim,vol_first_75rms_25fdim)
vc_75rms_25fdim_mean = np.mean(vc_75rms_25fdim)
vc_75rms_25fdim_skew = skew(vc_75rms_25fdim)
vc_75rms_25fdim_std = np.std(vc_75rms_25fdim)
### 75 rms .50 fdim
vol_first_75rms_50fdim = ice_vol_75rms_50fdim.iloc[0,:]
vol_end_75rms_50fdim = ice_vol_75rms_50fdim.iloc[200,:]
vc_75rms_50fdim = np.subtract(vol_end_75rms_50fdim,vol_first_75rms_50fdim)
vc_75rms_50fdim_mean = np.mean(vc_75rms_50fdim)
vc_75rms_50fdim_skew = skew(vc_75rms_50fdim)
vc_75rms_50fdim_std = np.std(vc_75rms_50fdim)
### 75 rms .75 fdim
vol_first_75rms_75fdim = ice_vol_75rms_75fdim.iloc[0,:]
vol_end_75rms_75fdim = ice_vol_75rms_75fdim.iloc[200,:]
vc_75rms_75fdim = np.subtract(vol_end_75rms_75fdim,vol_first_75rms_75fdim)
vc_75rms_75fdim_mean = np.mean(vc_75rms_75fdim)
vc_75rms_75fdim_skew = skew(vc_75rms_75fdim)
vc_75rms_75fdim_std = np.std(vc_75rms_75fdim)
### 75 rms 1.0 fdim
vol_first_75rms_10fdim = ice_vol_75rms_10fdim.iloc[0,:]
vol_end_75rms_10fdim = ice_vol_75rms_10fdim.iloc[200,:]
vc_75rms_10fdim = np.subtract(vol_end_75rms_10fdim,vol_first_75rms_10fdim)
vc_75rms_10fdim_mean = np.mean(vc_75rms_10fdim)
vc_75rms_10fdim_skew = skew(vc_75rms_10fdim)
vc_75rms_10fdim_std = np.std(vc_75rms_10fdim)


# 100 rms
ice_vol_100rms_25fdim = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_100rms_50fdim = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_100rms_75fdim = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,800))
ice_vol_100rms_10fdim = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,800))
## vol change
### 100 rms .25 fdim
vol_first_100rms_25fdim = ice_vol_100rms_25fdim.iloc[0,:]
vol_end_100rms_25fdim = ice_vol_100rms_25fdim.iloc[200,:]
vc_100rms_25fdim = np.subtract(vol_end_100rms_25fdim,vol_first_100rms_25fdim)
vc_100rms_25fdim_mean = np.mean(vc_100rms_25fdim)
vc_100rms_25fdim_skew = skew(vc_100rms_25fdim)
vc_100rms_25fdim_std = np.std(vc_100rms_25fdim)
### 100 rms .50 fdim
vol_first_100rms_50fdim = ice_vol_100rms_50fdim.iloc[0,:]
vol_end_100rms_50fdim = ice_vol_100rms_50fdim.iloc[200,:]
vc_100rms_50fdim = np.subtract(vol_end_100rms_50fdim,vol_first_100rms_50fdim)
vc_100rms_50fdim_mean = np.mean(vc_100rms_50fdim)
vc_100rms_50fdim_skew = skew(vc_100rms_50fdim)
vc_100rms_50fdim_std = np.std(vc_100rms_50fdim)
### 100 rms .75 fdim
vol_first_100rms_75fdim = ice_vol_100rms_75fdim.iloc[0,:]
vol_end_100rms_75fdim = ice_vol_100rms_75fdim.iloc[200,:]
vc_100rms_75fdim = np.subtract(vol_end_100rms_75fdim,vol_first_100rms_75fdim)
vc_100rms_75fdim_mean = np.mean(vc_100rms_75fdim)
vc_100rms_75fdim_skew = skew(vc_100rms_75fdim)
vc_100rms_75fdim_std = np.std(vc_100rms_75fdim)
### 100 rms 1.0 fdim
vol_first_100rms_10fdim = ice_vol_100rms_10fdim.iloc[0,:]
vol_end_100rms_10fdim = ice_vol_100rms_10fdim.iloc[200,:]
vc_100rms_10fdim = np.subtract(vol_end_100rms_10fdim,vol_first_100rms_10fdim)
vc_100rms_10fdim_mean = np.mean(vc_100rms_10fdim)
vc_100rms_10fdim_skew = skew(vc_100rms_10fdim)
vc_100rms_10fdim_std = np.std(vc_100rms_10fdim)


############ FROM REU #############

# structure:
# 1. load data
# 2. transpose 
# 3. convert km3 to m3
# 4. vol change + mean

### 25 rms ### 

### 25 rms .25 fdim
REU_vol_25rms_25fdim = pd.read_csv('25rms_25fdim_total_vs.csv', header=None)
REU_vol_25rms_25fdim = REU_vol_25rms_25fdim.transpose()
REU_vol_25rms_25fdim = REU_vol_25rms_25fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_25rms_25fdim = REU_vol_25rms_25fdim.iloc[0,:]
RVE_25rms_25fdim = REU_vol_25rms_25fdim.iloc[19,:]
RVC_25rms_25fdim = np.subtract(RVE_25rms_25fdim,RVF_25rms_25fdim)
RVC_25rms_25fdim_mean = np.mean(vc_25rms_25fdim)

### 25 rms .50 fdim
REU_vol_25rms_50fdim = pd.read_csv('25rms_50fdim_total_vs.csv', header=None)
REU_vol_25rms_50fdim = REU_vol_25rms_50fdim.transpose()
REU_vol_25rms_50fdim = REU_vol_25rms_50fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_25rms_50fdim = REU_vol_25rms_50fdim.iloc[0,:]
RVE_25rms_50fdim = REU_vol_25rms_50fdim.iloc[19,:]
RVC_25rms_50fdim = np.subtract(RVE_25rms_50fdim,RVF_25rms_50fdim)
RVC_25rms_50fdim_mean = np.mean(vc_25rms_50fdim)

### 25 rms .75 fdim
REU_vol_25rms_75fdim = pd.read_csv('25rms_75fdim_total_vs.csv', header=None)
REU_vol_25rms_75fdim = REU_vol_25rms_75fdim.transpose()
REU_vol_25rms_75fdim = REU_vol_25rms_75fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_25rms_75fdim = REU_vol_25rms_75fdim.iloc[0,:]
RVE_25rms_75fdim = REU_vol_25rms_75fdim.iloc[19,:]
RVC_25rms_75fdim = np.subtract(RVE_25rms_75fdim,RVF_25rms_75fdim)
RVC_25rms_75fdim_mean = np.mean(vc_25rms_75fdim)

### 25 rms 1.0 fdim
REU_vol_25rms_10fdim = pd.read_csv('25rms_10fdim_total_vs.csv', header=None)
REU_vol_25rms_10fdim = REU_vol_25rms_10fdim.transpose()
REU_vol_25rms_10fdim = REU_vol_25rms_10fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_25rms_10fdim = REU_vol_25rms_10fdim.iloc[0,:]
RVE_25rms_10fdim = REU_vol_25rms_10fdim.iloc[19,:]
RVC_25rms_10fdim = np.subtract(RVE_25rms_10fdim,RVF_25rms_10fdim)
RVC_25rms_10fdim_mean = np.mean(vc_25rms_10fdim)


### 50 rms ###

### 50 rms .25 fdim
REU_vol_50rms_25fdim = pd.read_csv('50rms_25fdim_total_vs.csv', header=None)
REU_vol_50rms_25fdim = REU_vol_50rms_25fdim.transpose()
REU_vol_50rms_25fdim = REU_vol_50rms_25fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_50rms_25fdim = REU_vol_50rms_25fdim.iloc[0,:]
RVE_50rms_25fdim = REU_vol_50rms_25fdim.iloc[19,:]
RVC_50rms_25fdim = np.subtract(RVE_50rms_25fdim,RVF_50rms_25fdim)
RVC_50rms_25fdim_mean = np.mean(vc_50rms_25fdim)

### 50 rms .50 fdim
REU_vol_50rms_50fdim = pd.read_csv('50rms_50fdim_total_vs.csv', header=None)
REU_vol_50rms_50fdim = REU_vol_50rms_50fdim.transpose()
REU_vol_50rms_50fdim = REU_vol_50rms_50fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_50rms_50fdim = REU_vol_50rms_50fdim.iloc[0,:]
RVE_50rms_50fdim = REU_vol_50rms_50fdim.iloc[19,:]
RVC_50rms_50fdim = np.subtract(RVE_50rms_50fdim,RVF_50rms_50fdim)
RVC_50rms_50fdim_mean = np.mean(vc_50rms_50fdim)

### 50 rms .75 fdim
REU_vol_50rms_75fdim = pd.read_csv('50rms_75fdim_total_vs.csv', header=None)
REU_vol_50rms_75fdim = REU_vol_50rms_75fdim.transpose()
REU_vol_50rms_75fdim = REU_vol_50rms_75fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_50rms_75fdim = REU_vol_50rms_75fdim.iloc[0,:]
RVE_50rms_75fdim = REU_vol_50rms_75fdim.iloc[19,:]
RVC_50rms_75fdim = np.subtract(RVE_50rms_75fdim,RVF_50rms_75fdim)
RVC_50rms_75fdim_mean = np.mean(vc_50rms_75fdim)

### 50 rms 1.0 fdim
REU_vol_50rms_10fdim = pd.read_csv('50rms_10fdim_total_vs.csv', header=None)
REU_vol_50rms_10fdim = REU_vol_50rms_10fdim.transpose()
REU_vol_50rms_10fdim = REU_vol_50rms_10fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_50rms_10fdim = REU_vol_50rms_10fdim.iloc[0,:]
RVE_50rms_10fdim = REU_vol_50rms_10fdim.iloc[19,:]
RVC_50rms_10fdim = np.subtract(RVE_50rms_10fdim,RVF_50rms_10fdim)
RVC_50rms_10fdim_mean = np.mean(vc_50rms_10fdim)


### 75 rms ###

### 75 rms .25 fdim
REU_vol_75rms_25fdim = pd.read_csv('75rms_25fdim_total_vs.csv', header=None)
REU_vol_75rms_25fdim = REU_vol_75rms_25fdim.transpose()
REU_vol_75rms_25fdim = REU_vol_75rms_25fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_75rms_25fdim = REU_vol_75rms_25fdim.iloc[0,:]
RVE_75rms_25fdim = REU_vol_75rms_25fdim.iloc[19,:]
RVC_75rms_25fdim = np.subtract(RVE_75rms_25fdim,RVF_75rms_25fdim)
RVC_75rms_25fdim_mean = np.mean(vc_75rms_25fdim)

### 75 rms .50 fdim
REU_vol_75rms_50fdim = pd.read_csv('75rms_50fdim_total_vs.csv', header=None)
REU_vol_75rms_50fdim = REU_vol_75rms_50fdim.transpose()
REU_vol_75rms_50fdim = REU_vol_75rms_50fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_75rms_50fdim = REU_vol_75rms_50fdim.iloc[0,:]
RVE_75rms_50fdim = REU_vol_75rms_50fdim.iloc[19,:]
RVC_75rms_50fdim = np.subtract(RVE_75rms_50fdim,RVF_75rms_50fdim)
RVC_75rms_50fdim_mean = np.mean(vc_75rms_50fdim)

### 75 rms .75 fdim
REU_vol_75rms_75fdim = pd.read_csv('75rms_75fdim_total_vs.csv', header=None)
REU_vol_75rms_75fdim = REU_vol_75rms_75fdim.transpose()
REU_vol_75rms_75fdim = REU_vol_75rms_75fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_75rms_75fdim = REU_vol_75rms_75fdim.iloc[0,:]
RVE_75rms_75fdim = REU_vol_75rms_75fdim.iloc[19,:]
RVC_75rms_75fdim = np.subtract(RVE_75rms_75fdim,RVF_75rms_75fdim)
RVC_75rms_75fdim_mean = np.mean(vc_75rms_75fdim)

### 75 rms 1.0 fdim
REU_vol_75rms_10fdim = pd.read_csv('75rms_10fdim_total_vs.csv', header=None)
REU_vol_75rms_10fdim = REU_vol_75rms_10fdim.transpose()
REU_vol_75rms_10fdim = REU_vol_75rms_10fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_75rms_10fdim = REU_vol_75rms_10fdim.iloc[0,:]
RVE_75rms_10fdim = REU_vol_75rms_10fdim.iloc[19,:]
RVC_75rms_10fdim = np.subtract(RVE_75rms_10fdim,RVF_75rms_10fdim)
RVC_75rms_10fdim_mean = np.mean(vc_75rms_10fdim)


### 100 rms ###

### 100 rms .25 fdim
REU_vol_100rms_25fdim = pd.read_csv('100rms_25fdim_total_vs.csv', header=None)
REU_vol_100rms_25fdim = REU_vol_100rms_25fdim.transpose()
REU_vol_100rms_25fdim = REU_vol_100rms_25fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_100rms_25fdim = REU_vol_100rms_25fdim.iloc[0,:]
RVE_100rms_25fdim = REU_vol_100rms_25fdim.iloc[19,:]
RVC_100rms_25fdim = np.subtract(RVE_100rms_25fdim,RVF_100rms_25fdim)
RVC_100rms_25fdim_mean = np.mean(vc_100rms_25fdim)

### 100 rms .50 fdim
REU_vol_100rms_50fdim = pd.read_csv('100rms_50fdim_total_vs.csv', header=None)
REU_vol_100rms_50fdim = REU_vol_100rms_50fdim.transpose()
REU_vol_100rms_50fdim = REU_vol_100rms_50fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_100rms_50fdim = REU_vol_100rms_50fdim.iloc[0,:]
RVE_100rms_50fdim = REU_vol_100rms_50fdim.iloc[19,:]
RVC_100rms_50fdim = np.subtract(RVE_100rms_50fdim,RVF_100rms_50fdim)
RVC_100rms_50fdim_mean = np.mean(vc_100rms_50fdim)

### 100 rms .75 fdim
REU_vol_100rms_75fdim = pd.read_csv('100rms_75fdim_total_vs.csv', header=None)
REU_vol_100rms_75fdim = REU_vol_100rms_75fdim.transpose()
REU_vol_100rms_75fdim = REU_vol_100rms_75fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_100rms_75fdim = REU_vol_100rms_75fdim.iloc[0,:]
RVE_100rms_75fdim = REU_vol_100rms_75fdim.iloc[19,:]
RVC_100rms_75fdim = np.subtract(RVE_100rms_75fdim,RVF_100rms_75fdim)
RVC_100rms_75fdim_mean = np.mean(vc_100rms_75fdim)

### 100 rms 1.0 fdim
REU_vol_100rms_10fdim = pd.read_csv('100rms_10fdim_total_vs.csv', header=None)
REU_vol_100rms_10fdim = REU_vol_100rms_10fdim.transpose()
REU_vol_100rms_10fdim = REU_vol_100rms_10fdim.multiply(1.0E-9, axis=1)
## vol change
RVF_100rms_10fdim = REU_vol_100rms_10fdim.iloc[0,:]
RVE_100rms_10fdim = REU_vol_100rms_10fdim.iloc[19,:]
RVC_100rms_10fdim = np.subtract(RVE_100rms_10fdim,RVF_100rms_10fdim)
RVC_100rms_10fdim_mean = np.mean(vc_100rms_10fdim)


###################################
############# plot ################
###################################

stats_xlabel = np.array(['25 rms','50 rms','75 rms','100 rms'])

### SED ### 
# .25 fdim mean
vc_25fdim_mean = np.array([vc_25rms_25fdim_mean, vc_50rms_25fdim_mean, vc_75rms_25fdim_mean, vc_100rms_25fdim_mean])
plt.figure()
plt.plot(stats_xlabel,vc_25fdim_mean,'r',marker='o')
plt.xlabel('topo. rms')
plt.title('mean volume change across rms - .25 fdim')

# .50 fdim mean
vc_50fdim_mean = np.array([vc_25rms_50fdim_mean, vc_50rms_50fdim_mean, vc_75rms_50fdim_mean, vc_100rms_50fdim_mean])
plt.figure()
plt.plot(stats_xlabel,vc_50fdim_mean,'b',marker='o')
plt.xlabel('topo. rms')
plt.title('mean volume change across rms - .50 fdim')

# .75 fdim mean
vc_75fdim_mean = np.array([vc_25rms_75fdim_mean, vc_50rms_75fdim_mean, vc_75rms_75fdim_mean, vc_100rms_75fdim_mean])
plt.figure()
plt.plot(stats_xlabel,vc_75fdim_mean,'g',marker='o')
plt.xlabel('topo. rms')
plt.title('mean volume change across rms - .75 fdim')

# 1.0 fdim mean
vc_10fdim_mean = np.array([vc_25rms_10fdim_mean, vc_50rms_10fdim_mean, vc_75rms_10fdim_mean, vc_100rms_10fdim_mean])
plt.figure()
plt.plot(stats_xlabel,vc_10fdim_mean,marker='o')
plt.xlabel('topo. rms')
plt.title('mean volume change across rms - 1.0 fdim')


### REU ###
RVC_25fdim_mean = np.array([RVC_25rms_25fdim_mean, RVC_50rms_25fdim_mean, RVC_75rms_25fdim_mean, RVC_100rms_25fdim_mean])
RVC_50fdim_mean = np.array([RVC_25rms_50fdim_mean, RVC_50rms_50fdim_mean, RVC_75rms_50fdim_mean, RVC_100rms_50fdim_mean])
RVC_75fdim_mean = np.array([RVC_25rms_75fdim_mean, RVC_50rms_75fdim_mean, RVC_75rms_75fdim_mean, RVC_100rms_75fdim_mean])
RVC_10fdim_mean = np.array([RVC_25rms_10fdim_mean, RVC_50rms_10fdim_mean, RVC_75rms_10fdim_mean, RVC_100rms_10fdim_mean])

# # 25 rms skew
# vc_25rms_skew = np.array([vc_25rms_25fdim_skew, vc_25rms_50fdim_skew, vc_25rms_75fdim_skew, vc_25rms_10fdim_skew])
# plt.plot(stats_xlabel,vc_25rms_skew,marker='o')
# plt.xlabel('topo. fdim')
# plt.title('skew volume change across fdim - 25rms')

# # 25 rms standard deviation
# vc_25rms_std = np.array([vc_25rms_25fdim_std, vc_25rms_50fdim_std, vc_25rms_75fdim_std, vc_25rms_10fdim_std])
# plt.plot(stats_xlabel,vc_25rms_std,marker='o')
# plt.xlabel('topo. fdim')
# plt.title('standard dev. volume change across fdim - 25rms')



###################################
######### gaussian kde ############
###################################

## use seaborn pkg
## smoothing with bw_method, bw_adjust (numerical value)

# 0.25-1.0 fdim mean -- SED
vc_fdim_mean_total = np.array([vc_25fdim_mean, vc_50fdim_mean, vc_75fdim_mean, vc_10fdim_mean])
plt.figure()
sns.kdeplot(data=vc_fdim_mean_total)
plt.xlabel('volume change (m^3)')
plt.title('gaussian KDE for 0.25-1.0 fdim mean - SED')
plt.legend(["0.25 fdim", "0.50 fdim", "0.75 fdim", "1.0 fdim"])
plt.savefig("SED_KDE_all_fdim.png", dpi=800)

# 0.25-1.0 fdim mean -- REU
RVC_fdim_mean_total = np.array([RVC_25fdim_mean, RVC_50fdim_mean, RVC_75fdim_mean, RVC_10fdim_mean])
plt.figure()
sns.kdeplot(data=RVC_fdim_mean_total)
plt.xlabel('volume change (m^3)')
plt.title('gaussian KDE for 0.25-1.0 fdim mean - REU')
plt.legend(["0.25 fdim", "0.50 fdim", "0.75 fdim", "1.0 fdim"])
plt.savefig("REU_KDE_all_fdim.png", dpi=800)


# 25rms-100rms mean -- SED
vc_25rms_mean = np.array([vc_25rms_25fdim_mean, vc_25rms_50fdim_mean, vc_25rms_75fdim_mean, vc_25rms_10fdim_mean])
vc_50rms_mean = np.array([vc_50rms_25fdim_mean, vc_50rms_50fdim_mean, vc_50rms_50fdim_mean, vc_50rms_10fdim_mean])
vc_75rms_mean = np.array([vc_75rms_25fdim_mean, vc_75rms_50fdim_mean, vc_75rms_75fdim_mean, vc_75rms_10fdim_mean])
vc_100rms_mean = np.array([vc_100rms_25fdim_mean, vc_100rms_50fdim_mean, vc_100rms_75fdim_mean, vc_100rms_10fdim_mean])
vc_rms_mean_total = np.array([vc_25rms_mean, vc_50rms_mean, vc_75rms_mean, vc_100rms_mean])
plt.figure()
sns.kdeplot(data=vc_rms_mean_total)
plt.xlabel('volume change (m^3)')
plt.title('gaussian KDE for 25-100 rms mean - SED')
plt.legend(["25 rms", "50 rms", "75 rms", "100 rms"])

# 25rms-100rms mean -- REU
RVC_25rms_mean = np.array([RVC_25rms_25fdim_mean, RVC_25rms_50fdim_mean, RVC_25rms_75fdim_mean, RVC_25rms_10fdim_mean])
RVC_50rms_mean = np.array([RVC_50rms_25fdim_mean, RVC_50rms_50fdim_mean, RVC_50rms_50fdim_mean, RVC_50rms_10fdim_mean])
RVC_75rms_mean = np.array([RVC_75rms_25fdim_mean, RVC_75rms_50fdim_mean, RVC_75rms_75fdim_mean, RVC_75rms_10fdim_mean])
RVC_100rms_mean = np.array([RVC_100rms_25fdim_mean, RVC_100rms_50fdim_mean, RVC_100rms_75fdim_mean, RVC_100rms_10fdim_mean])
RVC_rms_mean_total = np.array([RVC_25rms_mean, RVC_50rms_mean, RVC_75rms_mean, RVC_100rms_mean])
plt.figure()
sns.kdeplot(data=RVC_rms_mean_total)
plt.xlabel('volume change (m^3)')
plt.title('gaussian KDE for 25-100 rms mean - REU')
plt.legend(["25 rms", "50 rms", "75 rms", "100 rms"])






