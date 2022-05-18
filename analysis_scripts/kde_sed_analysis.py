#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:53:45 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
import seaborn as sns


###################################
### load data and collect stats ###
###################################

### control ###
ctrl_SED = pd.read_csv('ice_vol_1000yr_control_case.csv', index_col=0)


######## 25 rms ########

### 25 rms 0.25 fdim ###
### low ###
ls_25r_25f = pd.read_csv('low_sed_25r_25f.csv', index_col=0)
ls_25r_25f_1 = ls_25r_25f.loc[0:100]
ls_25r_25f_2 = ls_25r_25f.loc[100:200]
ls_25r_25f_3 = ls_25r_25f.loc[200:300]
ls_25r_25f_4 = ls_25r_25f.loc[300:400]
ls_25r_25f_5 = ls_25r_25f.loc[400:500]
ls_25r_25f_6 = ls_25r_25f.loc[500:600]
ls_25r_25f_7 = ls_25r_25f.loc[600:700]
ls_25r_25f_8 = ls_25r_25f.loc[700:800]
ls_25r_25f_9 = ls_25r_25f.loc[800:900]
ls_25r_25f_10 = ls_25r_25f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_25r_25f_1 = np.mean(ls_25r_25f_1)
lsiv_25r_25f_2 = np.mean(ls_25r_25f_2)
lsiv_25r_25f_3 = np.mean(ls_25r_25f_3)
lsiv_25r_25f_4 = np.mean(ls_25r_25f_4)
lsiv_25r_25f_5 = np.mean(ls_25r_25f_5)
lsiv_25r_25f_6 = np.mean(ls_25r_25f_6)
lsiv_25r_25f_7 = np.mean(ls_25r_25f_7)
lsiv_25r_25f_8 = np.mean(ls_25r_25f_8)
lsiv_25r_25f_9 = np.mean(ls_25r_25f_9)
lsiv_25r_25f_10 = np.mean(ls_25r_25f_10)
# build df 
lsiv_25r_25f_tot = np.array([lsiv_25r_25f_1, lsiv_25r_25f_2, lsiv_25r_25f_3, lsiv_25r_25f_4, 
                                        lsiv_25r_25f_5, lsiv_25r_25f_6, lsiv_25r_25f_7, lsiv_25r_25f_8,
                                        lsiv_25r_25f_9, lsiv_25r_25f_10])
lsiv_25r_25f_tot = lsiv_25r_25f_tot.transpose() # switch rows and columns 

### med ###
ms_25r_25f = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)
ms_25r_25f_1 = ms_25r_25f.loc[0:100]
ms_25r_25f_2 = ms_25r_25f.loc[100:200]
ms_25r_25f_3 = ms_25r_25f.loc[200:300]
ms_25r_25f_4 = ms_25r_25f.loc[300:400]
ms_25r_25f_5 = ms_25r_25f.loc[400:500]
ms_25r_25f_6 = ms_25r_25f.loc[500:600]
ms_25r_25f_7 = ms_25r_25f.loc[600:700]
ms_25r_25f_8 = ms_25r_25f.loc[700:800]
ms_25r_25f_9 = ms_25r_25f.loc[800:900]
ms_25r_25f_10 = ms_25r_25f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_25r_25f_1 = np.mean(ms_25r_25f_1)
msiv_25r_25f_2 = np.mean(ms_25r_25f_2)
msiv_25r_25f_3 = np.mean(ms_25r_25f_3)
msiv_25r_25f_4 = np.mean(ms_25r_25f_4)
msiv_25r_25f_5 = np.mean(ms_25r_25f_5)
msiv_25r_25f_6 = np.mean(ms_25r_25f_6)
msiv_25r_25f_7 = np.mean(ms_25r_25f_7)
msiv_25r_25f_8 = np.mean(ms_25r_25f_8)
msiv_25r_25f_9 = np.mean(ms_25r_25f_9)
msiv_25r_25f_10 = np.mean(ms_25r_25f_10)
# build df 
msiv_25r_25f_tot = np.array([msiv_25r_25f_1, msiv_25r_25f_2, msiv_25r_25f_3, msiv_25r_25f_4, 
                                        msiv_25r_25f_5, msiv_25r_25f_6, msiv_25r_25f_7, msiv_25r_25f_8,
                                        msiv_25r_25f_9, msiv_25r_25f_10])
msiv_25r_25f_tot = msiv_25r_25f_tot.transpose() # switch rows and columns

### high ###
hs_25r_25f = pd.read_csv('high_sed_25r_25f.csv', index_col=0)
hs_25r_25f_1 = hs_25r_25f.loc[0:100]
hs_25r_25f_2 = hs_25r_25f.loc[100:200]
hs_25r_25f_3 = hs_25r_25f.loc[200:300]
hs_25r_25f_4 = hs_25r_25f.loc[300:400]
hs_25r_25f_5 = hs_25r_25f.loc[400:500]
hs_25r_25f_6 = hs_25r_25f.loc[500:600]
hs_25r_25f_7 = hs_25r_25f.loc[600:700]
hs_25r_25f_8 = hs_25r_25f.loc[700:800]
hs_25r_25f_9 = hs_25r_25f.loc[800:900]
hs_25r_25f_10 = hs_25r_25f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_25r_25f_1 = np.mean(hs_25r_25f_1)
hsiv_25r_25f_2 = np.mean(hs_25r_25f_2)
hsiv_25r_25f_3 = np.mean(hs_25r_25f_3)
hsiv_25r_25f_4 = np.mean(hs_25r_25f_4)
hsiv_25r_25f_5 = np.mean(hs_25r_25f_5)
hsiv_25r_25f_6 = np.mean(hs_25r_25f_6)
hsiv_25r_25f_7 = np.mean(hs_25r_25f_7)
hsiv_25r_25f_8 = np.mean(hs_25r_25f_8)
hsiv_25r_25f_9 = np.mean(hs_25r_25f_9)
hsiv_25r_25f_10 = np.mean(hs_25r_25f_10)
# build df 
hsiv_25r_25f_tot = np.array([hsiv_25r_25f_1, hsiv_25r_25f_2, hsiv_25r_25f_3, hsiv_25r_25f_4, 
                                        hsiv_25r_25f_5, hsiv_25r_25f_6, hsiv_25r_25f_7, hsiv_25r_25f_8,
                                        hsiv_25r_25f_9, hsiv_25r_25f_10])
hsiv_25r_25f_tot = hsiv_25r_25f_tot.transpose() # switch rows and columns

### 25 rms 0.50 fdim ###
ls_25r_50f = pd.read_csv('low_sed_25r_50f.csv', index_col=0)
ls_25r_50f_1 = ls_25r_50f.loc[0:100]
ls_25r_50f_2 = ls_25r_50f.loc[100:200]
ls_25r_50f_3 = ls_25r_50f.loc[200:300]
ls_25r_50f_4 = ls_25r_50f.loc[300:400]
ls_25r_50f_5 = ls_25r_50f.loc[400:500]
ls_25r_50f_6 = ls_25r_50f.loc[500:600]
ls_25r_50f_7 = ls_25r_50f.loc[600:700]
ls_25r_50f_8 = ls_25r_50f.loc[700:800]
ls_25r_50f_9 = ls_25r_50f.loc[800:900]
ls_25r_50f_10 = ls_25r_50f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_25r_50f_1 = np.mean(ls_25r_50f_1)
lsiv_25r_50f_2 = np.mean(ls_25r_50f_2)
lsiv_25r_50f_3 = np.mean(ls_25r_50f_3)
lsiv_25r_50f_4 = np.mean(ls_25r_50f_4)
lsiv_25r_50f_5 = np.mean(ls_25r_50f_5)
lsiv_25r_50f_6 = np.mean(ls_25r_50f_6)
lsiv_25r_50f_7 = np.mean(ls_25r_50f_7)
lsiv_25r_50f_8 = np.mean(ls_25r_50f_8)
lsiv_25r_50f_9 = np.mean(ls_25r_50f_9)
lsiv_25r_50f_10 = np.mean(ls_25r_50f_10)
# build df 
lsiv_25r_50f_tot = np.array([lsiv_25r_50f_1, lsiv_25r_50f_2, lsiv_25r_50f_3, lsiv_25r_50f_4, 
                                        lsiv_25r_50f_5, lsiv_25r_50f_6, lsiv_25r_50f_7, lsiv_25r_50f_8,
                                        lsiv_25r_50f_9, lsiv_25r_50f_10])
lsiv_25r_50f_tot = lsiv_25r_50f_tot.transpose() # switch rows and columns

# med
ms_25r_50f = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0)
ms_25r_50f_1 = ms_25r_50f.loc[0:100]
ms_25r_50f_2 = ms_25r_50f.loc[100:200]
ms_25r_50f_3 = ms_25r_50f.loc[200:300]
ms_25r_50f_4 = ms_25r_50f.loc[300:400]
ms_25r_50f_5 = ms_25r_50f.loc[400:500]
ms_25r_50f_6 = ms_25r_50f.loc[500:600]
ms_25r_50f_7 = ms_25r_50f.loc[600:700]
ms_25r_50f_8 = ms_25r_50f.loc[700:800]
ms_25r_50f_9 = ms_25r_50f.loc[800:900]
ms_25r_50f_10 = ms_25r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_25r_50f_1 = np.mean(ms_25r_50f_1)
msiv_25r_50f_2 = np.mean(ms_25r_50f_2)
msiv_25r_50f_3 = np.mean(ms_25r_50f_3)
msiv_25r_50f_4 = np.mean(ms_25r_50f_4)
msiv_25r_50f_5 = np.mean(ms_25r_50f_5)
msiv_25r_50f_6 = np.mean(ms_25r_50f_6)
msiv_25r_50f_7 = np.mean(ms_25r_50f_7)
msiv_25r_50f_8 = np.mean(ms_25r_50f_8)
msiv_25r_50f_9 = np.mean(ms_25r_50f_9)
msiv_25r_50f_10 = np.mean(ms_25r_50f_10)
# build df 
msiv_25r_50f_tot = np.array([msiv_25r_50f_1, msiv_25r_50f_2, msiv_25r_50f_3, msiv_25r_50f_4, 
                                        msiv_25r_50f_5, msiv_25r_50f_6, msiv_25r_50f_7, msiv_25r_50f_8,
                                        msiv_25r_50f_9, msiv_25r_50f_10])
msiv_25r_50f_tot = msiv_25r_50f_tot.transpose() # switch rows and columns

# high
hs_25r_50f = pd.read_csv('high_sed_25r_50f.csv', index_col=0)
hs_25r_50f_1 = hs_25r_50f.loc[0:100]
hs_25r_50f_2 = hs_25r_50f.loc[100:200]
hs_25r_50f_3 = hs_25r_50f.loc[200:300]
hs_25r_50f_4 = hs_25r_50f.loc[300:400]
hs_25r_50f_5 = hs_25r_50f.loc[400:500]
hs_25r_50f_6 = hs_25r_50f.loc[500:600]
hs_25r_50f_7 = hs_25r_50f.loc[600:700]
hs_25r_50f_8 = hs_25r_50f.loc[700:800]
hs_25r_50f_9 = hs_25r_50f.loc[800:900]
hs_25r_50f_10 = hs_25r_50f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_25r_50f_1 = np.mean(hs_25r_50f_1)
hsiv_25r_50f_2 = np.mean(hs_25r_50f_2)
hsiv_25r_50f_3 = np.mean(hs_25r_50f_3)
hsiv_25r_50f_4 = np.mean(hs_25r_50f_4)
hsiv_25r_50f_5 = np.mean(hs_25r_50f_5)
hsiv_25r_50f_6 = np.mean(hs_25r_50f_6)
hsiv_25r_50f_7 = np.mean(hs_25r_50f_7)
hsiv_25r_50f_8 = np.mean(hs_25r_50f_8)
hsiv_25r_50f_9 = np.mean(hs_25r_50f_9)
hsiv_25r_50f_10 = np.mean(hs_25r_50f_10)
# build df 
hsiv_25r_50f_tot = np.array([hsiv_25r_50f_1, hsiv_25r_50f_2, hsiv_25r_50f_3, hsiv_25r_50f_4, 
                                        hsiv_25r_50f_5, hsiv_25r_50f_6, hsiv_25r_50f_7, hsiv_25r_50f_8,
                                        hsiv_25r_50f_9, hsiv_25r_50f_10])
hsiv_25r_50f_tot = hsiv_25r_50f_tot.transpose() # switch rows and columns


### 25 rms 0.75 fdim ###
### low ###
ls_25r_75f = pd.read_csv('low_sed_25r_75f.csv', index_col=0)
ls_25r_75f_1 = ls_25r_75f.loc[0:100]
ls_25r_75f_2 = ls_25r_75f.loc[100:200]
ls_25r_75f_3 = ls_25r_75f.loc[200:300]
ls_25r_75f_4 = ls_25r_75f.loc[300:400]
ls_25r_75f_5 = ls_25r_75f.loc[400:500]
ls_25r_75f_6 = ls_25r_75f.loc[500:600]
ls_25r_75f_7 = ls_25r_75f.loc[600:700]
ls_25r_75f_8 = ls_25r_75f.loc[700:800]
ls_25r_75f_9 = ls_25r_75f.loc[800:900]
ls_25r_75f_10 = ls_25r_75f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_25r_75f_1 = np.mean(ls_25r_75f_1)
lsiv_25r_75f_2 = np.mean(ls_25r_75f_2)
lsiv_25r_75f_3 = np.mean(ls_25r_75f_3)
lsiv_25r_75f_4 = np.mean(ls_25r_75f_4)
lsiv_25r_75f_5 = np.mean(ls_25r_75f_5)
lsiv_25r_75f_6 = np.mean(ls_25r_75f_6)
lsiv_25r_75f_7 = np.mean(ls_25r_75f_7)
lsiv_25r_75f_8 = np.mean(ls_25r_75f_8)
lsiv_25r_75f_9 = np.mean(ls_25r_75f_9)
lsiv_25r_75f_10 = np.mean(ls_25r_75f_10)
# build df 
lsiv_25r_75f_tot = np.array([lsiv_25r_75f_1, lsiv_25r_75f_2, lsiv_25r_75f_3, lsiv_25r_75f_4, 
                                        lsiv_25r_75f_5, lsiv_25r_75f_6, lsiv_25r_75f_7, lsiv_25r_75f_8,
                                        lsiv_25r_75f_9, lsiv_25r_75f_10])
lsiv_25r_75f_tot = lsiv_25r_75f_tot.transpose() # switch rows and columns 

### med ###
ms_25r_75f = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0)
ms_25r_75f_1 = ms_25r_75f.loc[0:100]
ms_25r_75f_2 = ms_25r_75f.loc[100:200]
ms_25r_75f_3 = ms_25r_75f.loc[200:300]
ms_25r_75f_4 = ms_25r_75f.loc[300:400]
ms_25r_75f_5 = ms_25r_75f.loc[400:500]
ms_25r_75f_6 = ms_25r_75f.loc[500:600]
ms_25r_75f_7 = ms_25r_75f.loc[600:700]
ms_25r_75f_8 = ms_25r_75f.loc[700:800]
ms_25r_75f_9 = ms_25r_75f.loc[800:900]
ms_25r_75f_10 = ms_25r_75f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_25r_75f_1 = np.mean(ms_25r_75f_1)
msiv_25r_75f_2 = np.mean(ms_25r_75f_2)
msiv_25r_75f_3 = np.mean(ms_25r_75f_3)
msiv_25r_75f_4 = np.mean(ms_25r_75f_4)
msiv_25r_75f_5 = np.mean(ms_25r_75f_5)
msiv_25r_75f_6 = np.mean(ms_25r_75f_6)
msiv_25r_75f_7 = np.mean(ms_25r_75f_7)
msiv_25r_75f_8 = np.mean(ms_25r_75f_8)
msiv_25r_75f_9 = np.mean(ms_25r_75f_9)
msiv_25r_75f_10 = np.mean(ms_25r_75f_10)
# build df 
msiv_25r_75f_tot = np.array([msiv_25r_75f_1, msiv_25r_75f_2, msiv_25r_75f_3, msiv_25r_75f_4, 
                                        msiv_25r_75f_5, msiv_25r_75f_6, msiv_25r_75f_7, msiv_25r_75f_8,
                                        msiv_25r_75f_9, msiv_25r_75f_10])
msiv_25r_75f_tot = msiv_25r_75f_tot.transpose() # switch rows and columns

### high ###
hs_25r_75f = pd.read_csv('high_sed_25r_75f.csv', index_col=0)
hs_25r_75f_1 = hs_25r_75f.loc[0:100]
hs_25r_75f_2 = hs_25r_75f.loc[100:200]
hs_25r_75f_3 = hs_25r_75f.loc[200:300]
hs_25r_75f_4 = hs_25r_75f.loc[300:400]
hs_25r_75f_5 = hs_25r_75f.loc[400:500]
hs_25r_75f_6 = hs_25r_75f.loc[500:600]
hs_25r_75f_7 = hs_25r_75f.loc[600:700]
hs_25r_75f_8 = hs_25r_75f.loc[700:800]
hs_25r_75f_9 = hs_25r_75f.loc[800:900]
hs_25r_75f_10 = hs_25r_75f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_25r_75f_1 = np.mean(hs_25r_75f_1)
hsiv_25r_75f_2 = np.mean(hs_25r_75f_2)
hsiv_25r_75f_3 = np.mean(hs_25r_75f_3)
hsiv_25r_75f_4 = np.mean(hs_25r_75f_4)
hsiv_25r_75f_5 = np.mean(hs_25r_75f_5)
hsiv_25r_75f_6 = np.mean(hs_25r_75f_6)
hsiv_25r_75f_7 = np.mean(hs_25r_75f_7)
hsiv_25r_75f_8 = np.mean(hs_25r_75f_8)
hsiv_25r_75f_9 = np.mean(hs_25r_75f_9)
hsiv_25r_75f_10 = np.mean(hs_25r_75f_10)
# build df 
hsiv_25r_75f_tot = np.array([hsiv_25r_75f_1, hsiv_25r_75f_2, hsiv_25r_75f_3, hsiv_25r_75f_4, 
                                        hsiv_25r_75f_5, hsiv_25r_75f_6, hsiv_25r_75f_7, hsiv_25r_75f_8,
                                        hsiv_25r_75f_9, hsiv_25r_75f_10])
hsiv_25r_75f_tot = hsiv_25r_75f_tot.transpose() # switch rows and columns


### 25 rms 1.0 fdim ###
### low ###
ls_25r_10f = pd.read_csv('low_sed_25r_10f.csv', index_col=0)
ls_25r_10f_1 = ls_25r_10f.loc[0:100]
ls_25r_10f_2 = ls_25r_10f.loc[100:200]
ls_25r_10f_3 = ls_25r_10f.loc[200:300]
ls_25r_10f_4 = ls_25r_10f.loc[300:400]
ls_25r_10f_5 = ls_25r_10f.loc[400:500]
ls_25r_10f_6 = ls_25r_10f.loc[500:600]
ls_25r_10f_7 = ls_25r_10f.loc[600:700]
ls_25r_10f_8 = ls_25r_10f.loc[700:800]
ls_25r_10f_9 = ls_25r_10f.loc[800:900]
ls_25r_10f_10 = ls_25r_10f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_25r_10f_1 = np.mean(ls_25r_10f_1)
lsiv_25r_10f_2 = np.mean(ls_25r_10f_2)
lsiv_25r_10f_3 = np.mean(ls_25r_10f_3)
lsiv_25r_10f_4 = np.mean(ls_25r_10f_4)
lsiv_25r_10f_5 = np.mean(ls_25r_10f_5)
lsiv_25r_10f_6 = np.mean(ls_25r_10f_6)
lsiv_25r_10f_7 = np.mean(ls_25r_10f_7)
lsiv_25r_10f_8 = np.mean(ls_25r_10f_8)
lsiv_25r_10f_9 = np.mean(ls_25r_10f_9)
lsiv_25r_10f_10 = np.mean(ls_25r_10f_10)
# build df 
lsiv_25r_10f_tot = np.array([lsiv_25r_10f_1, lsiv_25r_10f_2, lsiv_25r_10f_3, lsiv_25r_10f_4, 
                                        lsiv_25r_10f_5, lsiv_25r_10f_6, lsiv_25r_10f_7, lsiv_25r_10f_8,
                                        lsiv_25r_10f_9, lsiv_25r_10f_10])
lsiv_25r_10f_tot = lsiv_25r_10f_tot.transpose() # switch rows and columns 

### med ###
ms_25r_10f = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)
ms_25r_10f_1 = ms_25r_10f.loc[0:100]
ms_25r_10f_2 = ms_25r_10f.loc[100:200]
ms_25r_10f_3 = ms_25r_10f.loc[200:300]
ms_25r_10f_4 = ms_25r_10f.loc[300:400]
ms_25r_10f_5 = ms_25r_10f.loc[400:500]
ms_25r_10f_6 = ms_25r_10f.loc[500:600]
ms_25r_10f_7 = ms_25r_10f.loc[600:700]
ms_25r_10f_8 = ms_25r_10f.loc[700:800]
ms_25r_10f_9 = ms_25r_10f.loc[800:900]
ms_25r_10f_10 = ms_25r_10f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_25r_10f_1 = np.mean(ms_25r_10f_1)
msiv_25r_10f_2 = np.mean(ms_25r_10f_2)
msiv_25r_10f_3 = np.mean(ms_25r_10f_3)
msiv_25r_10f_4 = np.mean(ms_25r_10f_4)
msiv_25r_10f_5 = np.mean(ms_25r_10f_5)
msiv_25r_10f_6 = np.mean(ms_25r_10f_6)
msiv_25r_10f_7 = np.mean(ms_25r_10f_7)
msiv_25r_10f_8 = np.mean(ms_25r_10f_8)
msiv_25r_10f_9 = np.mean(ms_25r_10f_9)
msiv_25r_10f_10 = np.mean(ms_25r_10f_10)
# build df 
msiv_25r_10f_tot = np.array([msiv_25r_10f_1, msiv_25r_10f_2, msiv_25r_10f_3, msiv_25r_10f_4, 
                                        msiv_25r_10f_5, msiv_25r_10f_6, msiv_25r_10f_7, msiv_25r_10f_8,
                                        msiv_25r_10f_9, msiv_25r_10f_10])
msiv_25r_10f_tot = msiv_25r_10f_tot.transpose() # switch rows and columns

### high ###
hs_25r_10f = pd.read_csv('high_sed_25r_10f.csv', index_col=0)
hs_25r_10f_1 = hs_25r_10f.loc[0:100]
hs_25r_10f_2 = hs_25r_10f.loc[100:200]
hs_25r_10f_3 = hs_25r_10f.loc[200:300]
hs_25r_10f_4 = hs_25r_10f.loc[300:400]
hs_25r_10f_5 = hs_25r_10f.loc[400:500]
hs_25r_10f_6 = hs_25r_10f.loc[500:600]
hs_25r_10f_7 = hs_25r_10f.loc[600:700]
hs_25r_10f_8 = hs_25r_10f.loc[700:800]
hs_25r_10f_9 = hs_25r_10f.loc[800:900]
hs_25r_10f_10 = hs_25r_10f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_25r_10f_1 = np.mean(hs_25r_10f_1)
hsiv_25r_10f_2 = np.mean(hs_25r_10f_2)
hsiv_25r_10f_3 = np.mean(hs_25r_10f_3)
hsiv_25r_10f_4 = np.mean(hs_25r_10f_4)
hsiv_25r_10f_5 = np.mean(hs_25r_10f_5)
hsiv_25r_10f_6 = np.mean(hs_25r_10f_6)
hsiv_25r_10f_7 = np.mean(hs_25r_10f_7)
hsiv_25r_10f_8 = np.mean(hs_25r_10f_8)
hsiv_25r_10f_9 = np.mean(hs_25r_10f_9)
hsiv_25r_10f_10 = np.mean(hs_25r_10f_10)
# build df 
hsiv_25r_10f_tot = np.array([hsiv_25r_10f_1, hsiv_25r_10f_2, hsiv_25r_10f_3, hsiv_25r_10f_4, 
                                        hsiv_25r_10f_5, hsiv_25r_10f_6, hsiv_25r_10f_7, hsiv_25r_10f_8,
                                        hsiv_25r_10f_9, hsiv_25r_10f_10])
hsiv_25r_10f_tot = hsiv_25r_10f_tot.transpose() # switch rows and columns




######## 50 rms ########

### 50 rms 0.25 fdim ###
### low ###
ls_50r_25f = pd.read_csv('low_sed_50r_25f.csv', index_col=0)
ls_50r_25f_1 = ls_50r_25f.loc[0:100]
ls_50r_25f_2 = ls_50r_25f.loc[100:200]
ls_50r_25f_3 = ls_50r_25f.loc[200:300]
ls_50r_25f_4 = ls_50r_25f.loc[300:400]
ls_50r_25f_5 = ls_50r_25f.loc[400:500]
ls_50r_25f_6 = ls_50r_25f.loc[500:600]
ls_50r_25f_7 = ls_50r_25f.loc[600:700]
ls_50r_25f_8 = ls_50r_25f.loc[700:800]
ls_50r_25f_9 = ls_50r_25f.loc[800:900]
ls_50r_25f_10 = ls_50r_25f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_50r_25f_1 = np.mean(ls_50r_25f_1)
lsiv_50r_25f_2 = np.mean(ls_50r_25f_2)
lsiv_50r_25f_3 = np.mean(ls_50r_25f_3)
lsiv_50r_25f_4 = np.mean(ls_50r_25f_4)
lsiv_50r_25f_5 = np.mean(ls_50r_25f_5)
lsiv_50r_25f_6 = np.mean(ls_50r_25f_6)
lsiv_50r_25f_7 = np.mean(ls_50r_25f_7)
lsiv_50r_25f_8 = np.mean(ls_50r_25f_8)
lsiv_50r_25f_9 = np.mean(ls_50r_25f_9)
lsiv_50r_25f_10 = np.mean(ls_50r_25f_10)
# build df 
lsiv_50r_25f_tot = np.array([lsiv_50r_25f_1, lsiv_50r_25f_2, lsiv_50r_25f_3, lsiv_50r_25f_4, 
                                        lsiv_50r_25f_5, lsiv_50r_25f_6, lsiv_50r_25f_7, lsiv_50r_25f_8,
                                        lsiv_50r_25f_9, lsiv_50r_25f_10])
lsiv_50r_25f_tot = lsiv_50r_25f_tot.transpose() # switch rows and columns 

### med ###
ms_50r_25f = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0)
ms_50r_25f_1 = ms_50r_25f.loc[0:100]
ms_50r_25f_2 = ms_50r_25f.loc[100:200]
ms_50r_25f_3 = ms_50r_25f.loc[200:300]
ms_50r_25f_4 = ms_50r_25f.loc[300:400]
ms_50r_25f_5 = ms_50r_25f.loc[400:500]
ms_50r_25f_6 = ms_50r_25f.loc[500:600]
ms_50r_25f_7 = ms_50r_25f.loc[600:700]
ms_50r_25f_8 = ms_50r_25f.loc[700:800]
ms_50r_25f_9 = ms_50r_25f.loc[800:900]
ms_50r_25f_10 = ms_50r_25f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_50r_25f_1 = np.mean(ms_50r_25f_1)
msiv_50r_25f_2 = np.mean(ms_50r_25f_2)
msiv_50r_25f_3 = np.mean(ms_50r_25f_3)
msiv_50r_25f_4 = np.mean(ms_50r_25f_4)
msiv_50r_25f_5 = np.mean(ms_50r_25f_5)
msiv_50r_25f_6 = np.mean(ms_50r_25f_6)
msiv_50r_25f_7 = np.mean(ms_50r_25f_7)
msiv_50r_25f_8 = np.mean(ms_50r_25f_8)
msiv_50r_25f_9 = np.mean(ms_50r_25f_9)
msiv_50r_25f_10 = np.mean(ms_50r_25f_10)
# build df 
msiv_50r_25f_tot = np.array([msiv_50r_25f_1, msiv_50r_25f_2, msiv_50r_25f_3, msiv_50r_25f_4, 
                                        msiv_50r_25f_5, msiv_50r_25f_6, msiv_50r_25f_7, msiv_50r_25f_8,
                                        msiv_50r_25f_9, msiv_50r_25f_10])
msiv_50r_25f_tot = msiv_50r_25f_tot.transpose() # switch rows and columns

### high ###
hs_50r_25f = pd.read_csv('high_sed_50r_25f.csv', index_col=0)
hs_50r_25f_1 = hs_50r_25f.loc[0:100]
hs_50r_25f_2 = hs_50r_25f.loc[100:200]
hs_50r_25f_3 = hs_50r_25f.loc[200:300]
hs_50r_25f_4 = hs_50r_25f.loc[300:400]
hs_50r_25f_5 = hs_50r_25f.loc[400:500]
hs_50r_25f_6 = hs_50r_25f.loc[500:600]
hs_50r_25f_7 = hs_50r_25f.loc[600:700]
hs_50r_25f_8 = hs_50r_25f.loc[700:800]
hs_50r_25f_9 = hs_50r_25f.loc[800:900]
hs_50r_25f_10 = hs_50r_25f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_50r_25f_1 = np.mean(hs_50r_25f_1)
hsiv_50r_25f_2 = np.mean(hs_50r_25f_2)
hsiv_50r_25f_3 = np.mean(hs_50r_25f_3)
hsiv_50r_25f_4 = np.mean(hs_50r_25f_4)
hsiv_50r_25f_5 = np.mean(hs_50r_25f_5)
hsiv_50r_25f_6 = np.mean(hs_50r_25f_6)
hsiv_50r_25f_7 = np.mean(hs_50r_25f_7)
hsiv_50r_25f_8 = np.mean(hs_50r_25f_8)
hsiv_50r_25f_9 = np.mean(hs_50r_25f_9)
hsiv_50r_25f_10 = np.mean(hs_50r_25f_10)
# build df 
hsiv_50r_25f_tot = np.array([hsiv_50r_25f_1, hsiv_50r_25f_2, hsiv_50r_25f_3, hsiv_50r_25f_4, 
                                        hsiv_50r_25f_5, hsiv_50r_25f_6, hsiv_50r_25f_7, hsiv_50r_25f_8,
                                        hsiv_50r_25f_9, hsiv_50r_25f_10])
hsiv_50r_25f_tot = hsiv_50r_25f_tot.transpose() # switch rows and columns

### 50 rms 0.50 fdim ###
ls_50r_50f = pd.read_csv('low_sed_50r_50f.csv', index_col=0)
ls_50r_50f_1 = ls_50r_50f.loc[0:100]
ls_50r_50f_2 = ls_50r_50f.loc[100:200]
ls_50r_50f_3 = ls_50r_50f.loc[200:300]
ls_50r_50f_4 = ls_50r_50f.loc[300:400]
ls_50r_50f_5 = ls_50r_50f.loc[400:500]
ls_50r_50f_6 = ls_50r_50f.loc[500:600]
ls_50r_50f_7 = ls_50r_50f.loc[600:700]
ls_50r_50f_8 = ls_50r_50f.loc[700:800]
ls_50r_50f_9 = ls_50r_50f.loc[800:900]
ls_50r_50f_10 = ls_50r_50f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_50r_50f_1 = np.mean(ls_50r_50f_1)
lsiv_50r_50f_2 = np.mean(ls_50r_50f_2)
lsiv_50r_50f_3 = np.mean(ls_50r_50f_3)
lsiv_50r_50f_4 = np.mean(ls_50r_50f_4)
lsiv_50r_50f_5 = np.mean(ls_50r_50f_5)
lsiv_50r_50f_6 = np.mean(ls_50r_50f_6)
lsiv_50r_50f_7 = np.mean(ls_50r_50f_7)
lsiv_50r_50f_8 = np.mean(ls_50r_50f_8)
lsiv_50r_50f_9 = np.mean(ls_50r_50f_9)
lsiv_50r_50f_10 = np.mean(ls_50r_50f_10)
# build df 
lsiv_50r_50f_tot = np.array([lsiv_50r_50f_1, lsiv_50r_50f_2, lsiv_50r_50f_3, lsiv_50r_50f_4, 
                                        lsiv_50r_50f_5, lsiv_50r_50f_6, lsiv_50r_50f_7, lsiv_50r_50f_8,
                                        lsiv_50r_50f_9, lsiv_50r_50f_10])
lsiv_50r_50f_tot = lsiv_50r_50f_tot.transpose() # switch rows and columns

# med
ms_50r_50f = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0)
ms_50r_50f_1 = ms_50r_50f.loc[0:100]
ms_50r_50f_2 = ms_50r_50f.loc[100:200]
ms_50r_50f_3 = ms_50r_50f.loc[200:300]
ms_50r_50f_4 = ms_50r_50f.loc[300:400]
ms_50r_50f_5 = ms_50r_50f.loc[400:500]
ms_50r_50f_6 = ms_50r_50f.loc[500:600]
ms_50r_50f_7 = ms_50r_50f.loc[600:700]
ms_50r_50f_8 = ms_50r_50f.loc[700:800]
ms_50r_50f_9 = ms_50r_50f.loc[800:900]
ms_50r_50f_10 = ms_50r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_50r_50f_1 = np.mean(ms_50r_50f_1)
msiv_50r_50f_2 = np.mean(ms_50r_50f_2)
msiv_50r_50f_3 = np.mean(ms_50r_50f_3)
msiv_50r_50f_4 = np.mean(ms_50r_50f_4)
msiv_50r_50f_5 = np.mean(ms_50r_50f_5)
msiv_50r_50f_6 = np.mean(ms_50r_50f_6)
msiv_50r_50f_7 = np.mean(ms_50r_50f_7)
msiv_50r_50f_8 = np.mean(ms_50r_50f_8)
msiv_50r_50f_9 = np.mean(ms_50r_50f_9)
msiv_50r_50f_10 = np.mean(ms_50r_50f_10)
# build df 
msiv_50r_50f_tot = np.array([msiv_50r_50f_1, msiv_50r_50f_2, msiv_50r_50f_3, msiv_50r_50f_4, 
                                        msiv_50r_50f_5, msiv_50r_50f_6, msiv_50r_50f_7, msiv_50r_50f_8,
                                        msiv_50r_50f_9, msiv_50r_50f_10])
msiv_50r_50f_tot = msiv_50r_50f_tot.transpose() # switch rows and columns

# high
hs_50r_50f = pd.read_csv('high_sed_50r_50f.csv', index_col=0)
hs_50r_50f_1 = hs_50r_50f.loc[0:100]
hs_50r_50f_2 = hs_50r_50f.loc[100:200]
hs_50r_50f_3 = hs_50r_50f.loc[200:300]
hs_50r_50f_4 = hs_50r_50f.loc[300:400]
hs_50r_50f_5 = hs_50r_50f.loc[400:500]
hs_50r_50f_6 = hs_50r_50f.loc[500:600]
hs_50r_50f_7 = hs_50r_50f.loc[600:700]
hs_50r_50f_8 = hs_50r_50f.loc[700:800]
hs_50r_50f_9 = hs_50r_50f.loc[800:900]
hs_50r_50f_10 = hs_50r_50f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_50r_50f_1 = np.mean(hs_50r_50f_1)
hsiv_50r_50f_2 = np.mean(hs_50r_50f_2)
hsiv_50r_50f_3 = np.mean(hs_50r_50f_3)
hsiv_50r_50f_4 = np.mean(hs_50r_50f_4)
hsiv_50r_50f_5 = np.mean(hs_50r_50f_5)
hsiv_50r_50f_6 = np.mean(hs_50r_50f_6)
hsiv_50r_50f_7 = np.mean(hs_50r_50f_7)
hsiv_50r_50f_8 = np.mean(hs_50r_50f_8)
hsiv_50r_50f_9 = np.mean(hs_50r_50f_9)
hsiv_50r_50f_10 = np.mean(hs_50r_50f_10)
# build df 
hsiv_50r_50f_tot = np.array([hsiv_50r_50f_1, hsiv_50r_50f_2, hsiv_50r_50f_3, hsiv_50r_50f_4, 
                                        hsiv_50r_50f_5, hsiv_50r_50f_6, hsiv_50r_50f_7, hsiv_50r_50f_8,
                                        hsiv_50r_50f_9, hsiv_50r_50f_10])
hsiv_50r_50f_tot = hsiv_50r_50f_tot.transpose() # switch rows and columns


### 50 rms 0.75 fdim ###
### low ###
ls_50r_75f = pd.read_csv('low_sed_50r_75f.csv', index_col=0)
ls_50r_75f_1 = ls_50r_75f.loc[0:100]
ls_50r_75f_2 = ls_50r_75f.loc[100:200]
ls_50r_75f_3 = ls_50r_75f.loc[200:300]
ls_50r_75f_4 = ls_50r_75f.loc[300:400]
ls_50r_75f_5 = ls_50r_75f.loc[400:500]
ls_50r_75f_6 = ls_50r_75f.loc[500:600]
ls_50r_75f_7 = ls_50r_75f.loc[600:700]
ls_50r_75f_8 = ls_50r_75f.loc[700:800]
ls_50r_75f_9 = ls_50r_75f.loc[800:900]
ls_50r_75f_10 = ls_50r_75f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_50r_75f_1 = np.mean(ls_50r_75f_1)
lsiv_50r_75f_2 = np.mean(ls_50r_75f_2)
lsiv_50r_75f_3 = np.mean(ls_50r_75f_3)
lsiv_50r_75f_4 = np.mean(ls_50r_75f_4)
lsiv_50r_75f_5 = np.mean(ls_50r_75f_5)
lsiv_50r_75f_6 = np.mean(ls_50r_75f_6)
lsiv_50r_75f_7 = np.mean(ls_50r_75f_7)
lsiv_50r_75f_8 = np.mean(ls_50r_75f_8)
lsiv_50r_75f_9 = np.mean(ls_50r_75f_9)
lsiv_50r_75f_10 = np.mean(ls_50r_75f_10)
# build df 
lsiv_50r_75f_tot = np.array([lsiv_50r_75f_1, lsiv_50r_75f_2, lsiv_50r_75f_3, lsiv_50r_75f_4, 
                                        lsiv_50r_75f_5, lsiv_50r_75f_6, lsiv_50r_75f_7, lsiv_50r_75f_8,
                                        lsiv_50r_75f_9, lsiv_50r_75f_10])
lsiv_50r_75f_tot = lsiv_50r_75f_tot.transpose() # switch rows and columns 

### med ###
ms_50r_75f = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0)
ms_50r_75f_1 = ms_50r_75f.loc[0:100]
ms_50r_75f_2 = ms_50r_75f.loc[100:200]
ms_50r_75f_3 = ms_50r_75f.loc[200:300]
ms_50r_75f_4 = ms_50r_75f.loc[300:400]
ms_50r_75f_5 = ms_50r_75f.loc[400:500]
ms_50r_75f_6 = ms_50r_75f.loc[500:600]
ms_50r_75f_7 = ms_50r_75f.loc[600:700]
ms_50r_75f_8 = ms_50r_75f.loc[700:800]
ms_50r_75f_9 = ms_50r_75f.loc[800:900]
ms_50r_75f_10 = ms_50r_75f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_50r_75f_1 = np.mean(ms_50r_75f_1)
msiv_50r_75f_2 = np.mean(ms_50r_75f_2)
msiv_50r_75f_3 = np.mean(ms_50r_75f_3)
msiv_50r_75f_4 = np.mean(ms_50r_75f_4)
msiv_50r_75f_5 = np.mean(ms_50r_75f_5)
msiv_50r_75f_6 = np.mean(ms_50r_75f_6)
msiv_50r_75f_7 = np.mean(ms_50r_75f_7)
msiv_50r_75f_8 = np.mean(ms_50r_75f_8)
msiv_50r_75f_9 = np.mean(ms_50r_75f_9)
msiv_50r_75f_10 = np.mean(ms_50r_75f_10)
# build df 
msiv_50r_75f_tot = np.array([msiv_50r_75f_1, msiv_50r_75f_2, msiv_50r_75f_3, msiv_50r_75f_4, 
                                        msiv_50r_75f_5, msiv_50r_75f_6, msiv_50r_75f_7, msiv_50r_75f_8,
                                        msiv_50r_75f_9, msiv_50r_75f_10])
msiv_50r_75f_tot = msiv_50r_75f_tot.transpose() # switch rows and columns

### high ###
hs_50r_75f = pd.read_csv('high_sed_50r_75f.csv', index_col=0)
hs_50r_75f_1 = hs_50r_75f.loc[0:100]
hs_50r_75f_2 = hs_50r_75f.loc[100:200]
hs_50r_75f_3 = hs_50r_75f.loc[200:300]
hs_50r_75f_4 = hs_50r_75f.loc[300:400]
hs_50r_75f_5 = hs_50r_75f.loc[400:500]
hs_50r_75f_6 = hs_50r_75f.loc[500:600]
hs_50r_75f_7 = hs_50r_75f.loc[600:700]
hs_50r_75f_8 = hs_50r_75f.loc[700:800]
hs_50r_75f_9 = hs_50r_75f.loc[800:900]
hs_50r_75f_10 = hs_50r_75f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_50r_75f_1 = np.mean(hs_50r_75f_1)
hsiv_50r_75f_2 = np.mean(hs_50r_75f_2)
hsiv_50r_75f_3 = np.mean(hs_50r_75f_3)
hsiv_50r_75f_4 = np.mean(hs_50r_75f_4)
hsiv_50r_75f_5 = np.mean(hs_50r_75f_5)
hsiv_50r_75f_6 = np.mean(hs_50r_75f_6)
hsiv_50r_75f_7 = np.mean(hs_50r_75f_7)
hsiv_50r_75f_8 = np.mean(hs_50r_75f_8)
hsiv_50r_75f_9 = np.mean(hs_50r_75f_9)
hsiv_50r_75f_10 = np.mean(hs_50r_75f_10)
# build df 
hsiv_50r_75f_tot = np.array([hsiv_50r_75f_1, hsiv_50r_75f_2, hsiv_50r_75f_3, hsiv_50r_75f_4, 
                                        hsiv_50r_75f_5, hsiv_50r_75f_6, hsiv_50r_75f_7, hsiv_50r_75f_8,
                                        hsiv_50r_75f_9, hsiv_50r_75f_10])
hsiv_50r_75f_tot = hsiv_50r_75f_tot.transpose() # switch rows and columns


### 50 rms 1.0 fdim ###
### low ###
ls_50r_10f = pd.read_csv('low_sed_50r_10f.csv', index_col=0)
ls_50r_10f_1 = ls_50r_10f.loc[0:100]
ls_50r_10f_2 = ls_50r_10f.loc[100:200]
ls_50r_10f_3 = ls_50r_10f.loc[200:300]
ls_50r_10f_4 = ls_50r_10f.loc[300:400]
ls_50r_10f_5 = ls_50r_10f.loc[400:500]
ls_50r_10f_6 = ls_50r_10f.loc[500:600]
ls_50r_10f_7 = ls_50r_10f.loc[600:700]
ls_50r_10f_8 = ls_50r_10f.loc[700:800]
ls_50r_10f_9 = ls_50r_10f.loc[800:900]
ls_50r_10f_10 = ls_50r_10f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_50r_10f_1 = np.mean(ls_50r_10f_1)
lsiv_50r_10f_2 = np.mean(ls_50r_10f_2)
lsiv_50r_10f_3 = np.mean(ls_50r_10f_3)
lsiv_50r_10f_4 = np.mean(ls_50r_10f_4)
lsiv_50r_10f_5 = np.mean(ls_50r_10f_5)
lsiv_50r_10f_6 = np.mean(ls_50r_10f_6)
lsiv_50r_10f_7 = np.mean(ls_50r_10f_7)
lsiv_50r_10f_8 = np.mean(ls_50r_10f_8)
lsiv_50r_10f_9 = np.mean(ls_50r_10f_9)
lsiv_50r_10f_10 = np.mean(ls_50r_10f_10)
# build df 
lsiv_50r_10f_tot = np.array([lsiv_50r_10f_1, lsiv_50r_10f_2, lsiv_50r_10f_3, lsiv_50r_10f_4, 
                                        lsiv_50r_10f_5, lsiv_50r_10f_6, lsiv_50r_10f_7, lsiv_50r_10f_8,
                                        lsiv_50r_10f_9, lsiv_50r_10f_10])
lsiv_50r_10f_tot = lsiv_50r_10f_tot.transpose() # switch rows and columns 

### med ###
ms_50r_10f = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0)
ms_50r_10f_1 = ms_50r_10f.loc[0:100]
ms_50r_10f_2 = ms_50r_10f.loc[100:200]
ms_50r_10f_3 = ms_50r_10f.loc[200:300]
ms_50r_10f_4 = ms_50r_10f.loc[300:400]
ms_50r_10f_5 = ms_50r_10f.loc[400:500]
ms_50r_10f_6 = ms_50r_10f.loc[500:600]
ms_50r_10f_7 = ms_50r_10f.loc[600:700]
ms_50r_10f_8 = ms_50r_10f.loc[700:800]
ms_50r_10f_9 = ms_50r_10f.loc[800:900]
ms_50r_10f_10 = ms_50r_10f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_50r_10f_1 = np.mean(ms_50r_10f_1)
msiv_50r_10f_2 = np.mean(ms_50r_10f_2)
msiv_50r_10f_3 = np.mean(ms_50r_10f_3)
msiv_50r_10f_4 = np.mean(ms_50r_10f_4)
msiv_50r_10f_5 = np.mean(ms_50r_10f_5)
msiv_50r_10f_6 = np.mean(ms_50r_10f_6)
msiv_50r_10f_7 = np.mean(ms_50r_10f_7)
msiv_50r_10f_8 = np.mean(ms_50r_10f_8)
msiv_50r_10f_9 = np.mean(ms_50r_10f_9)
msiv_50r_10f_10 = np.mean(ms_50r_10f_10)
# build df 
msiv_50r_10f_tot = np.array([msiv_50r_10f_1, msiv_50r_10f_2, msiv_50r_10f_3, msiv_50r_10f_4, 
                                        msiv_50r_10f_5, msiv_50r_10f_6, msiv_50r_10f_7, msiv_50r_10f_8,
                                        msiv_50r_10f_9, msiv_50r_10f_10])
msiv_50r_10f_tot = msiv_50r_10f_tot.transpose() # switch rows and columns

### high ###
hs_50r_10f = pd.read_csv('high_sed_50r_10f.csv', index_col=0)
hs_50r_10f_1 = hs_50r_10f.loc[0:100]
hs_50r_10f_2 = hs_50r_10f.loc[100:200]
hs_50r_10f_3 = hs_50r_10f.loc[200:300]
hs_50r_10f_4 = hs_50r_10f.loc[300:400]
hs_50r_10f_5 = hs_50r_10f.loc[400:500]
hs_50r_10f_6 = hs_50r_10f.loc[500:600]
hs_50r_10f_7 = hs_50r_10f.loc[600:700]
hs_50r_10f_8 = hs_50r_10f.loc[700:800]
hs_50r_10f_9 = hs_50r_10f.loc[800:900]
hs_50r_10f_10 = hs_50r_10f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_50r_10f_1 = np.mean(hs_50r_10f_1)
hsiv_50r_10f_2 = np.mean(hs_50r_10f_2)
hsiv_50r_10f_3 = np.mean(hs_50r_10f_3)
hsiv_50r_10f_4 = np.mean(hs_50r_10f_4)
hsiv_50r_10f_5 = np.mean(hs_50r_10f_5)
hsiv_50r_10f_6 = np.mean(hs_50r_10f_6)
hsiv_50r_10f_7 = np.mean(hs_50r_10f_7)
hsiv_50r_10f_8 = np.mean(hs_50r_10f_8)
hsiv_50r_10f_9 = np.mean(hs_50r_10f_9)
hsiv_50r_10f_10 = np.mean(hs_50r_10f_10)
# build df 
hsiv_50r_10f_tot = np.array([hsiv_50r_10f_1, hsiv_50r_10f_2, hsiv_50r_10f_3, hsiv_50r_10f_4, 
                                        hsiv_50r_10f_5, hsiv_50r_10f_6, hsiv_50r_10f_7, hsiv_50r_10f_8,
                                        hsiv_50r_10f_9, hsiv_50r_10f_10])
hsiv_50r_10f_tot = hsiv_50r_10f_tot.transpose() # switch rows and columns




######## 75 rms ########

### 75 rms 0.25 fdim ###
### low ###
ls_75r_25f = pd.read_csv('low_sed_75r_25f.csv', index_col=0)
ls_75r_25f_1 = ls_75r_25f.loc[0:100]
ls_75r_25f_2 = ls_75r_25f.loc[100:200]
ls_75r_25f_3 = ls_75r_25f.loc[200:300]
ls_75r_25f_4 = ls_75r_25f.loc[300:400]
ls_75r_25f_5 = ls_75r_25f.loc[400:500]
ls_75r_25f_6 = ls_75r_25f.loc[500:600]
ls_75r_25f_7 = ls_75r_25f.loc[600:700]
ls_75r_25f_8 = ls_75r_25f.loc[700:800]
ls_75r_25f_9 = ls_75r_25f.loc[800:900]
ls_75r_25f_10 = ls_75r_25f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_75r_25f_1 = np.mean(ls_75r_25f_1)
lsiv_75r_25f_2 = np.mean(ls_75r_25f_2)
lsiv_75r_25f_3 = np.mean(ls_75r_25f_3)
lsiv_75r_25f_4 = np.mean(ls_75r_25f_4)
lsiv_75r_25f_5 = np.mean(ls_75r_25f_5)
lsiv_75r_25f_6 = np.mean(ls_75r_25f_6)
lsiv_75r_25f_7 = np.mean(ls_75r_25f_7)
lsiv_75r_25f_8 = np.mean(ls_75r_25f_8)
lsiv_75r_25f_9 = np.mean(ls_75r_25f_9)
lsiv_75r_25f_10 = np.mean(ls_75r_25f_10)
# build df 
lsiv_75r_25f_tot = np.array([lsiv_75r_25f_1, lsiv_75r_25f_2, lsiv_75r_25f_3, lsiv_75r_25f_4, 
                                        lsiv_75r_25f_5, lsiv_75r_25f_6, lsiv_75r_25f_7, lsiv_75r_25f_8,
                                        lsiv_75r_25f_9, lsiv_75r_25f_10])
lsiv_75r_25f_tot = lsiv_75r_25f_tot.transpose() # switch rows and columns 

### med ###
ms_75r_25f = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0)
ms_75r_25f_1 = ms_75r_25f.loc[0:100]
ms_75r_25f_2 = ms_75r_25f.loc[100:200]
ms_75r_25f_3 = ms_75r_25f.loc[200:300]
ms_75r_25f_4 = ms_75r_25f.loc[300:400]
ms_75r_25f_5 = ms_75r_25f.loc[400:500]
ms_75r_25f_6 = ms_75r_25f.loc[500:600]
ms_75r_25f_7 = ms_75r_25f.loc[600:700]
ms_75r_25f_8 = ms_75r_25f.loc[700:800]
ms_75r_25f_9 = ms_75r_25f.loc[800:900]
ms_75r_25f_10 = ms_75r_25f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_75r_25f_1 = np.mean(ms_75r_25f_1)
msiv_75r_25f_2 = np.mean(ms_75r_25f_2)
msiv_75r_25f_3 = np.mean(ms_75r_25f_3)
msiv_75r_25f_4 = np.mean(ms_75r_25f_4)
msiv_75r_25f_5 = np.mean(ms_75r_25f_5)
msiv_75r_25f_6 = np.mean(ms_75r_25f_6)
msiv_75r_25f_7 = np.mean(ms_75r_25f_7)
msiv_75r_25f_8 = np.mean(ms_75r_25f_8)
msiv_75r_25f_9 = np.mean(ms_75r_25f_9)
msiv_75r_25f_10 = np.mean(ms_75r_25f_10)
# build df 
msiv_75r_25f_tot = np.array([msiv_75r_25f_1, msiv_75r_25f_2, msiv_75r_25f_3, msiv_75r_25f_4, 
                                        msiv_75r_25f_5, msiv_75r_25f_6, msiv_75r_25f_7, msiv_75r_25f_8,
                                        msiv_75r_25f_9, msiv_75r_25f_10])
msiv_75r_25f_tot = msiv_75r_25f_tot.transpose() # switch rows and columns

### high ###
hs_75r_25f = pd.read_csv('high_sed_75r_25f.csv', index_col=0)
hs_75r_25f_1 = hs_75r_25f.loc[0:100]
hs_75r_25f_2 = hs_75r_25f.loc[100:200]
hs_75r_25f_3 = hs_75r_25f.loc[200:300]
hs_75r_25f_4 = hs_75r_25f.loc[300:400]
hs_75r_25f_5 = hs_75r_25f.loc[400:500]
hs_75r_25f_6 = hs_75r_25f.loc[500:600]
hs_75r_25f_7 = hs_75r_25f.loc[600:700]
hs_75r_25f_8 = hs_75r_25f.loc[700:800]
hs_75r_25f_9 = hs_75r_25f.loc[800:900]
hs_75r_25f_10 = hs_75r_25f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_75r_25f_1 = np.mean(hs_75r_25f_1)
hsiv_75r_25f_2 = np.mean(hs_75r_25f_2)
hsiv_75r_25f_3 = np.mean(hs_75r_25f_3)
hsiv_75r_25f_4 = np.mean(hs_75r_25f_4)
hsiv_75r_25f_5 = np.mean(hs_75r_25f_5)
hsiv_75r_25f_6 = np.mean(hs_75r_25f_6)
hsiv_75r_25f_7 = np.mean(hs_75r_25f_7)
hsiv_75r_25f_8 = np.mean(hs_75r_25f_8)
hsiv_75r_25f_9 = np.mean(hs_75r_25f_9)
hsiv_75r_25f_10 = np.mean(hs_75r_25f_10)
# build df 
hsiv_75r_25f_tot = np.array([hsiv_75r_25f_1, hsiv_75r_25f_2, hsiv_75r_25f_3, hsiv_75r_25f_4, 
                                        hsiv_75r_25f_5, hsiv_75r_25f_6, hsiv_75r_25f_7, hsiv_75r_25f_8,
                                        hsiv_75r_25f_9, hsiv_75r_25f_10])
hsiv_75r_25f_tot = hsiv_75r_25f_tot.transpose() # switch rows and columns


### 75 rms 0.50 fdim ###
ls_75r_50f = pd.read_csv('low_sed_75r_50f.csv', index_col=0)
ls_75r_50f_1 = ls_75r_50f.loc[0:100]
ls_75r_50f_2 = ls_75r_50f.loc[100:200]
ls_75r_50f_3 = ls_75r_50f.loc[200:300]
ls_75r_50f_4 = ls_75r_50f.loc[300:400]
ls_75r_50f_5 = ls_75r_50f.loc[400:500]
ls_75r_50f_6 = ls_75r_50f.loc[500:600]
ls_75r_50f_7 = ls_75r_50f.loc[600:700]
ls_75r_50f_8 = ls_75r_50f.loc[700:800]
ls_75r_50f_9 = ls_75r_50f.loc[800:900]
ls_75r_50f_10 = ls_75r_50f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_75r_50f_1 = np.mean(ls_75r_50f_1)
lsiv_75r_50f_2 = np.mean(ls_75r_50f_2)
lsiv_75r_50f_3 = np.mean(ls_75r_50f_3)
lsiv_75r_50f_4 = np.mean(ls_75r_50f_4)
lsiv_75r_50f_5 = np.mean(ls_75r_50f_5)
lsiv_75r_50f_6 = np.mean(ls_75r_50f_6)
lsiv_75r_50f_7 = np.mean(ls_75r_50f_7)
lsiv_75r_50f_8 = np.mean(ls_75r_50f_8)
lsiv_75r_50f_9 = np.mean(ls_75r_50f_9)
lsiv_75r_50f_10 = np.mean(ls_75r_50f_10)
# build df 
lsiv_75r_50f_tot = np.array([lsiv_75r_50f_1, lsiv_75r_50f_2, lsiv_75r_50f_3, lsiv_75r_50f_4, 
                                        lsiv_75r_50f_5, lsiv_75r_50f_6, lsiv_75r_50f_7, lsiv_75r_50f_8,
                                        lsiv_75r_50f_9, lsiv_75r_50f_10])
lsiv_75r_50f_tot = lsiv_75r_50f_tot.transpose() # switch rows and columns

# med
ms_75r_50f = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0)
# ms_75r_50f = ms_75r_50f.iloc[:,:10]
ms_75r_50f_1 = ms_75r_50f.loc[0:100]
ms_75r_50f_2 = ms_75r_50f.loc[100:200]
ms_75r_50f_3 = ms_75r_50f.loc[200:300]
ms_75r_50f_4 = ms_75r_50f.loc[300:400]
ms_75r_50f_5 = ms_75r_50f.loc[400:500]
ms_75r_50f_6 = ms_75r_50f.loc[500:600]
ms_75r_50f_7 = ms_75r_50f.loc[600:700]
ms_75r_50f_8 = ms_75r_50f.loc[700:800]
ms_75r_50f_9 = ms_75r_50f.loc[800:900]
ms_75r_50f_10 = ms_75r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_75r_50f_1 = np.mean(ms_75r_50f_1)
msiv_75r_50f_2 = np.mean(ms_75r_50f_2)
msiv_75r_50f_3 = np.mean(ms_75r_50f_3)
msiv_75r_50f_4 = np.mean(ms_75r_50f_4)
msiv_75r_50f_5 = np.mean(ms_75r_50f_5)
msiv_75r_50f_6 = np.mean(ms_75r_50f_6)
msiv_75r_50f_7 = np.mean(ms_75r_50f_7)
msiv_75r_50f_8 = np.mean(ms_75r_50f_8)
msiv_75r_50f_9 = np.mean(ms_75r_50f_9)
msiv_75r_50f_10 = np.mean(ms_75r_50f_10)
# build df 
msiv_75r_50f_tot = np.array([msiv_75r_50f_1, msiv_75r_50f_2, msiv_75r_50f_3, msiv_75r_50f_4, 
                                        msiv_75r_50f_5, msiv_75r_50f_6, msiv_75r_50f_7, msiv_75r_50f_8,
                                        msiv_75r_50f_9, msiv_75r_50f_10])
msiv_75r_50f_tot = msiv_75r_50f_tot.transpose() # switch rows and columns

# med reduced - 10-members
msl_75r_50f = ms_75r_50f.iloc[:,:10]
msl_75r_50f_1 = msl_75r_50f.loc[0:100]
msl_75r_50f_2 = msl_75r_50f.loc[100:200]
msl_75r_50f_3 = msl_75r_50f.loc[200:300]
msl_75r_50f_4 = msl_75r_50f.loc[300:400]
msl_75r_50f_5 = msl_75r_50f.loc[400:500]
msl_75r_50f_6 = msl_75r_50f.loc[500:600]
msl_75r_50f_7 = msl_75r_50f.loc[600:700]
msl_75r_50f_8 = msl_75r_50f.loc[700:800]
msl_75r_50f_9 = msl_75r_50f.loc[800:900]
msl_75r_50f_10 = msl_75r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msliv_75r_50f_1 = np.mean(msl_75r_50f_1)
msliv_75r_50f_2 = np.mean(msl_75r_50f_2)
msliv_75r_50f_3 = np.mean(msl_75r_50f_3)
msliv_75r_50f_4 = np.mean(msl_75r_50f_4)
msliv_75r_50f_5 = np.mean(msl_75r_50f_5)
msliv_75r_50f_6 = np.mean(msl_75r_50f_6)
msliv_75r_50f_7 = np.mean(msl_75r_50f_7)
msliv_75r_50f_8 = np.mean(msl_75r_50f_8)
msliv_75r_50f_9 = np.mean(msl_75r_50f_9)
msliv_75r_50f_10 = np.mean(msl_75r_50f_10)
# build df 
msliv_75r_50f_tot = np.array([msliv_75r_50f_1, msliv_75r_50f_2, msliv_75r_50f_3, msliv_75r_50f_4, 
                                        msliv_75r_50f_5, msliv_75r_50f_6, msliv_75r_50f_7, msliv_75r_50f_8,
                                        msliv_75r_50f_9, msliv_75r_50f_10])
msliv_75r_50f_tot = msliv_75r_50f_tot.transpose() # switch rows and columns

# high
hs_75r_50f = pd.read_csv('high_sed_75r_50f.csv', index_col=0)
hs_75r_50f_1 = hs_75r_50f.loc[0:100]
hs_75r_50f_2 = hs_75r_50f.loc[100:200]
hs_75r_50f_3 = hs_75r_50f.loc[200:300]
hs_75r_50f_4 = hs_75r_50f.loc[300:400]
hs_75r_50f_5 = hs_75r_50f.loc[400:500]
hs_75r_50f_6 = hs_75r_50f.loc[500:600]
hs_75r_50f_7 = hs_75r_50f.loc[600:700]
hs_75r_50f_8 = hs_75r_50f.loc[700:800]
hs_75r_50f_9 = hs_75r_50f.loc[800:900]
hs_75r_50f_10 = hs_75r_50f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_75r_50f_1 = np.mean(hs_75r_50f_1)
hsiv_75r_50f_2 = np.mean(hs_75r_50f_2)
hsiv_75r_50f_3 = np.mean(hs_75r_50f_3)
hsiv_75r_50f_4 = np.mean(hs_75r_50f_4)
hsiv_75r_50f_5 = np.mean(hs_75r_50f_5)
hsiv_75r_50f_6 = np.mean(hs_75r_50f_6)
hsiv_75r_50f_7 = np.mean(hs_75r_50f_7)
hsiv_75r_50f_8 = np.mean(hs_75r_50f_8)
hsiv_75r_50f_9 = np.mean(hs_75r_50f_9)
hsiv_75r_50f_10 = np.mean(hs_75r_50f_10)
# build df 
hsiv_75r_50f_tot = np.array([hsiv_75r_50f_1, hsiv_75r_50f_2, hsiv_75r_50f_3, hsiv_75r_50f_4, 
                                        hsiv_75r_50f_5, hsiv_75r_50f_6, hsiv_75r_50f_7, hsiv_75r_50f_8,
                                        hsiv_75r_50f_9, hsiv_75r_50f_10])
hsiv_75r_50f_tot = hsiv_75r_50f_tot.transpose() # switch rows and columns


### 75 rms 0.75 fdim ###
### low ###
ls_75r_75f = pd.read_csv('low_sed_75r_75f.csv', index_col=0)
ls_75r_75f_1 = ls_75r_75f.loc[0:100]
ls_75r_75f_2 = ls_75r_75f.loc[100:200]
ls_75r_75f_3 = ls_75r_75f.loc[200:300]
ls_75r_75f_4 = ls_75r_75f.loc[300:400]
ls_75r_75f_5 = ls_75r_75f.loc[400:500]
ls_75r_75f_6 = ls_75r_75f.loc[500:600]
ls_75r_75f_7 = ls_75r_75f.loc[600:700]
ls_75r_75f_8 = ls_75r_75f.loc[700:800]
ls_75r_75f_9 = ls_75r_75f.loc[800:900]
ls_75r_75f_10 = ls_75r_75f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_75r_75f_1 = np.mean(ls_75r_75f_1)
lsiv_75r_75f_2 = np.mean(ls_75r_75f_2)
lsiv_75r_75f_3 = np.mean(ls_75r_75f_3)
lsiv_75r_75f_4 = np.mean(ls_75r_75f_4)
lsiv_75r_75f_5 = np.mean(ls_75r_75f_5)
lsiv_75r_75f_6 = np.mean(ls_75r_75f_6)
lsiv_75r_75f_7 = np.mean(ls_75r_75f_7)
lsiv_75r_75f_8 = np.mean(ls_75r_75f_8)
lsiv_75r_75f_9 = np.mean(ls_75r_75f_9)
lsiv_75r_75f_10 = np.mean(ls_75r_75f_10)
# build df 
lsiv_75r_75f_tot = np.array([lsiv_75r_75f_1, lsiv_75r_75f_2, lsiv_75r_75f_3, lsiv_75r_75f_4, 
                                        lsiv_75r_75f_5, lsiv_75r_75f_6, lsiv_75r_75f_7, lsiv_75r_75f_8,
                                        lsiv_75r_75f_9, lsiv_75r_75f_10])
lsiv_75r_75f_tot = lsiv_75r_75f_tot.transpose() # switch rows and columns 

### med ###
ms_75r_75f = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0)
ms_75r_75f_1 = ms_75r_75f.loc[0:100]
ms_75r_75f_2 = ms_75r_75f.loc[100:200]
ms_75r_75f_3 = ms_75r_75f.loc[200:300]
ms_75r_75f_4 = ms_75r_75f.loc[300:400]
ms_75r_75f_5 = ms_75r_75f.loc[400:500]
ms_75r_75f_6 = ms_75r_75f.loc[500:600]
ms_75r_75f_7 = ms_75r_75f.loc[600:700]
ms_75r_75f_8 = ms_75r_75f.loc[700:800]
ms_75r_75f_9 = ms_75r_75f.loc[800:900]
ms_75r_75f_10 = ms_75r_75f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_75r_75f_1 = np.mean(ms_75r_75f_1)
msiv_75r_75f_2 = np.mean(ms_75r_75f_2)
msiv_75r_75f_3 = np.mean(ms_75r_75f_3)
msiv_75r_75f_4 = np.mean(ms_75r_75f_4)
msiv_75r_75f_5 = np.mean(ms_75r_75f_5)
msiv_75r_75f_6 = np.mean(ms_75r_75f_6)
msiv_75r_75f_7 = np.mean(ms_75r_75f_7)
msiv_75r_75f_8 = np.mean(ms_75r_75f_8)
msiv_75r_75f_9 = np.mean(ms_75r_75f_9)
msiv_75r_75f_10 = np.mean(ms_75r_75f_10)
# build df 
msiv_75r_75f_tot = np.array([msiv_75r_75f_1, msiv_75r_75f_2, msiv_75r_75f_3, msiv_75r_75f_4, 
                                        msiv_75r_75f_5, msiv_75r_75f_6, msiv_75r_75f_7, msiv_75r_75f_8,
                                        msiv_75r_75f_9, msiv_75r_75f_10])
msiv_75r_75f_tot = msiv_75r_75f_tot.transpose() # switch rows and columns

### high ###
hs_75r_75f = pd.read_csv('high_sed_75r_75f.csv', index_col=0)
hs_75r_75f_1 = hs_75r_75f.loc[0:100]
hs_75r_75f_2 = hs_75r_75f.loc[100:200]
hs_75r_75f_3 = hs_75r_75f.loc[200:300]
hs_75r_75f_4 = hs_75r_75f.loc[300:400]
hs_75r_75f_5 = hs_75r_75f.loc[400:500]
hs_75r_75f_6 = hs_75r_75f.loc[500:600]
hs_75r_75f_7 = hs_75r_75f.loc[600:700]
hs_75r_75f_8 = hs_75r_75f.loc[700:800]
hs_75r_75f_9 = hs_75r_75f.loc[800:900]
hs_75r_75f_10 = hs_75r_75f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_75r_75f_1 = np.mean(hs_75r_75f_1)
hsiv_75r_75f_2 = np.mean(hs_75r_75f_2)
hsiv_75r_75f_3 = np.mean(hs_75r_75f_3)
hsiv_75r_75f_4 = np.mean(hs_75r_75f_4)
hsiv_75r_75f_5 = np.mean(hs_75r_75f_5)
hsiv_75r_75f_6 = np.mean(hs_75r_75f_6)
hsiv_75r_75f_7 = np.mean(hs_75r_75f_7)
hsiv_75r_75f_8 = np.mean(hs_75r_75f_8)
hsiv_75r_75f_9 = np.mean(hs_75r_75f_9)
hsiv_75r_75f_10 = np.mean(hs_75r_75f_10)
# build df 
hsiv_75r_75f_tot = np.array([hsiv_75r_75f_1, hsiv_75r_75f_2, hsiv_75r_75f_3, hsiv_75r_75f_4, 
                                        hsiv_75r_75f_5, hsiv_75r_75f_6, hsiv_75r_75f_7, hsiv_75r_75f_8,
                                        hsiv_75r_75f_9, hsiv_75r_75f_10])
hsiv_75r_75f_tot = hsiv_75r_75f_tot.transpose() # switch rows and columns


### 75 rms 1.0 fdim ###
### low ###
ls_75r_10f = pd.read_csv('low_sed_75r_10f.csv', index_col=0)
ls_75r_10f_1 = ls_75r_10f.loc[0:100]
ls_75r_10f_2 = ls_75r_10f.loc[100:200]
ls_75r_10f_3 = ls_75r_10f.loc[200:300]
ls_75r_10f_4 = ls_75r_10f.loc[300:400]
ls_75r_10f_5 = ls_75r_10f.loc[400:500]
ls_75r_10f_6 = ls_75r_10f.loc[500:600]
ls_75r_10f_7 = ls_75r_10f.loc[600:700]
ls_75r_10f_8 = ls_75r_10f.loc[700:800]
ls_75r_10f_9 = ls_75r_10f.loc[800:900]
ls_75r_10f_10 = ls_75r_10f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_75r_10f_1 = np.mean(ls_75r_10f_1)
lsiv_75r_10f_2 = np.mean(ls_75r_10f_2)
lsiv_75r_10f_3 = np.mean(ls_75r_10f_3)
lsiv_75r_10f_4 = np.mean(ls_75r_10f_4)
lsiv_75r_10f_5 = np.mean(ls_75r_10f_5)
lsiv_75r_10f_6 = np.mean(ls_75r_10f_6)
lsiv_75r_10f_7 = np.mean(ls_75r_10f_7)
lsiv_75r_10f_8 = np.mean(ls_75r_10f_8)
lsiv_75r_10f_9 = np.mean(ls_75r_10f_9)
lsiv_75r_10f_10 = np.mean(ls_75r_10f_10)
# build df 
lsiv_75r_10f_tot = np.array([lsiv_75r_10f_1, lsiv_75r_10f_2, lsiv_75r_10f_3, lsiv_75r_10f_4, 
                                        lsiv_75r_10f_5, lsiv_75r_10f_6, lsiv_75r_10f_7, lsiv_75r_10f_8,
                                        lsiv_75r_10f_9, lsiv_75r_10f_10])
lsiv_75r_10f_tot = lsiv_75r_10f_tot.transpose() # switch rows and columns 

### med ###
ms_75r_10f = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0)
ms_75r_10f_1 = ms_75r_10f.loc[0:100]
ms_75r_10f_2 = ms_75r_10f.loc[100:200]
ms_75r_10f_3 = ms_75r_10f.loc[200:300]
ms_75r_10f_4 = ms_75r_10f.loc[300:400]
ms_75r_10f_5 = ms_75r_10f.loc[400:500]
ms_75r_10f_6 = ms_75r_10f.loc[500:600]
ms_75r_10f_7 = ms_75r_10f.loc[600:700]
ms_75r_10f_8 = ms_75r_10f.loc[700:800]
ms_75r_10f_9 = ms_75r_10f.loc[800:900]
ms_75r_10f_10 = ms_75r_10f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_75r_10f_1 = np.mean(ms_75r_10f_1)
msiv_75r_10f_2 = np.mean(ms_75r_10f_2)
msiv_75r_10f_3 = np.mean(ms_75r_10f_3)
msiv_75r_10f_4 = np.mean(ms_75r_10f_4)
msiv_75r_10f_5 = np.mean(ms_75r_10f_5)
msiv_75r_10f_6 = np.mean(ms_75r_10f_6)
msiv_75r_10f_7 = np.mean(ms_75r_10f_7)
msiv_75r_10f_8 = np.mean(ms_75r_10f_8)
msiv_75r_10f_9 = np.mean(ms_75r_10f_9)
msiv_75r_10f_10 = np.mean(ms_75r_10f_10)
# build df 
msiv_75r_10f_tot = np.array([msiv_75r_10f_1, msiv_75r_10f_2, msiv_75r_10f_3, msiv_75r_10f_4, 
                                        msiv_75r_10f_5, msiv_75r_10f_6, msiv_75r_10f_7, msiv_75r_10f_8,
                                        msiv_75r_10f_9, msiv_75r_10f_10])
msiv_75r_10f_tot = msiv_75r_10f_tot.transpose() # switch rows and columns

### high ###
hs_75r_10f = pd.read_csv('high_sed_75r_10f.csv', index_col=0)
hs_75r_10f_1 = hs_75r_10f.loc[0:100]
hs_75r_10f_2 = hs_75r_10f.loc[100:200]
hs_75r_10f_3 = hs_75r_10f.loc[200:300]
hs_75r_10f_4 = hs_75r_10f.loc[300:400]
hs_75r_10f_5 = hs_75r_10f.loc[400:500]
hs_75r_10f_6 = hs_75r_10f.loc[500:600]
hs_75r_10f_7 = hs_75r_10f.loc[600:700]
hs_75r_10f_8 = hs_75r_10f.loc[700:800]
hs_75r_10f_9 = hs_75r_10f.loc[800:900]
hs_75r_10f_10 = hs_75r_10f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_75r_10f_1 = np.mean(hs_75r_10f_1)
hsiv_75r_10f_2 = np.mean(hs_75r_10f_2)
hsiv_75r_10f_3 = np.mean(hs_75r_10f_3)
hsiv_75r_10f_4 = np.mean(hs_75r_10f_4)
hsiv_75r_10f_5 = np.mean(hs_75r_10f_5)
hsiv_75r_10f_6 = np.mean(hs_75r_10f_6)
hsiv_75r_10f_7 = np.mean(hs_75r_10f_7)
hsiv_75r_10f_8 = np.mean(hs_75r_10f_8)
hsiv_75r_10f_9 = np.mean(hs_75r_10f_9)
hsiv_75r_10f_10 = np.mean(hs_75r_10f_10)
# build df 
hsiv_75r_10f_tot = np.array([hsiv_75r_10f_1, hsiv_75r_10f_2, hsiv_75r_10f_3, hsiv_75r_10f_4, 
                                        hsiv_75r_10f_5, hsiv_75r_10f_6, hsiv_75r_10f_7, hsiv_75r_10f_8,
                                        hsiv_75r_10f_9, hsiv_75r_10f_10])
hsiv_75r_10f_tot = hsiv_75r_10f_tot.transpose() # switch rows and columns



######## 100 rms ########

### 100 rms 0.25 fdim ###
### low ###
ls_100r_25f = pd.read_csv('low_sed_100r_25f.csv', index_col=0)
ls_100r_25f_1 = ls_100r_25f.loc[0:100]
ls_100r_25f_2 = ls_100r_25f.loc[100:200]
ls_100r_25f_3 = ls_100r_25f.loc[200:300]
ls_100r_25f_4 = ls_100r_25f.loc[300:400]
ls_100r_25f_5 = ls_100r_25f.loc[400:500]
ls_100r_25f_6 = ls_100r_25f.loc[500:600]
ls_100r_25f_7 = ls_100r_25f.loc[600:700]
ls_100r_25f_8 = ls_100r_25f.loc[700:800]
ls_100r_25f_9 = ls_100r_25f.loc[800:900]
ls_100r_25f_10 = ls_100r_25f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_100r_25f_1 = np.mean(ls_100r_25f_1)
lsiv_100r_25f_2 = np.mean(ls_100r_25f_2)
lsiv_100r_25f_3 = np.mean(ls_100r_25f_3)
lsiv_100r_25f_4 = np.mean(ls_100r_25f_4)
lsiv_100r_25f_5 = np.mean(ls_100r_25f_5)
lsiv_100r_25f_6 = np.mean(ls_100r_25f_6)
lsiv_100r_25f_7 = np.mean(ls_100r_25f_7)
lsiv_100r_25f_8 = np.mean(ls_100r_25f_8)
lsiv_100r_25f_9 = np.mean(ls_100r_25f_9)
lsiv_100r_25f_10 = np.mean(ls_100r_25f_10)
# build df 
lsiv_100r_25f_tot = np.array([lsiv_100r_25f_1, lsiv_100r_25f_2, lsiv_100r_25f_3, lsiv_100r_25f_4, 
                                        lsiv_100r_25f_5, lsiv_100r_25f_6, lsiv_100r_25f_7, lsiv_100r_25f_8,
                                        lsiv_100r_25f_9, lsiv_100r_25f_10])
lsiv_100r_25f_tot = lsiv_100r_25f_tot.transpose() # switch rows and columns 

### med ###
ms_100r_25f = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0)
ms_100r_25f_1 = ms_100r_25f.loc[0:100]
ms_100r_25f_2 = ms_100r_25f.loc[100:200]
ms_100r_25f_3 = ms_100r_25f.loc[200:300]
ms_100r_25f_4 = ms_100r_25f.loc[300:400]
ms_100r_25f_5 = ms_100r_25f.loc[400:500]
ms_100r_25f_6 = ms_100r_25f.loc[500:600]
ms_100r_25f_7 = ms_100r_25f.loc[600:700]
ms_100r_25f_8 = ms_100r_25f.loc[700:800]
ms_100r_25f_9 = ms_100r_25f.loc[800:900]
ms_100r_25f_10 = ms_100r_25f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_100r_25f_1 = np.mean(ms_100r_25f_1)
msiv_100r_25f_2 = np.mean(ms_100r_25f_2)
msiv_100r_25f_3 = np.mean(ms_100r_25f_3)
msiv_100r_25f_4 = np.mean(ms_100r_25f_4)
msiv_100r_25f_5 = np.mean(ms_100r_25f_5)
msiv_100r_25f_6 = np.mean(ms_100r_25f_6)
msiv_100r_25f_7 = np.mean(ms_100r_25f_7)
msiv_100r_25f_8 = np.mean(ms_100r_25f_8)
msiv_100r_25f_9 = np.mean(ms_100r_25f_9)
msiv_100r_25f_10 = np.mean(ms_100r_25f_10)
# build df 
msiv_100r_25f_tot = np.array([msiv_100r_25f_1, msiv_100r_25f_2, msiv_100r_25f_3, msiv_100r_25f_4, 
                                        msiv_100r_25f_5, msiv_100r_25f_6, msiv_100r_25f_7, msiv_100r_25f_8,
                                        msiv_100r_25f_9, msiv_100r_25f_10])
msiv_100r_25f_tot = msiv_100r_25f_tot.transpose() # switch rows and columns

### med reduced - 10-members
msl_100r_25f = ms_100r_25f.iloc[:,:10]
msl_100r_25f_1 = msl_100r_25f.loc[0:100]
msl_100r_25f_2 = msl_100r_25f.loc[100:200]
msl_100r_25f_3 = msl_100r_25f.loc[200:300]
msl_100r_25f_4 = msl_100r_25f.loc[300:400]
msl_100r_25f_5 = msl_100r_25f.loc[400:500]
msl_100r_25f_6 = msl_100r_25f.loc[500:600]
msl_100r_25f_7 = msl_100r_25f.loc[600:700]
msl_100r_25f_8 = msl_100r_25f.loc[700:800]
msl_100r_25f_9 = msl_100r_25f.loc[800:900]
msl_100r_25f_10 = msl_100r_25f.loc[900:1000]
# get mean, iv = ice vol mean
msliv_100r_25f_1 = np.mean(msl_100r_25f_1)
msliv_100r_25f_2 = np.mean(msl_100r_25f_2)
msliv_100r_25f_3 = np.mean(msl_100r_25f_3)
msliv_100r_25f_4 = np.mean(msl_100r_25f_4)
msliv_100r_25f_5 = np.mean(msl_100r_25f_5)
msliv_100r_25f_6 = np.mean(msl_100r_25f_6)
msliv_100r_25f_7 = np.mean(msl_100r_25f_7)
msliv_100r_25f_8 = np.mean(msl_100r_25f_8)
msliv_100r_25f_9 = np.mean(msl_100r_25f_9)
msliv_100r_25f_10 = np.mean(msl_100r_25f_10)
# build df 
msliv_100r_25f_tot = np.array([msliv_100r_25f_1, msliv_100r_25f_2, msliv_100r_25f_3, msliv_100r_25f_4, 
                                        msliv_100r_25f_5, msliv_100r_25f_6, msliv_100r_25f_7, msliv_100r_25f_8,
                                        msliv_100r_25f_9, msliv_100r_25f_10])
msliv_100r_25f_tot = msliv_100r_25f_tot.transpose() # switch rows and columns

### high ###
hs_100r_25f = pd.read_csv('high_sed_100r_25f.csv', index_col=0)
hs_100r_25f_1 = hs_100r_25f.loc[0:100]
hs_100r_25f_2 = hs_100r_25f.loc[100:200]
hs_100r_25f_3 = hs_100r_25f.loc[200:300]
hs_100r_25f_4 = hs_100r_25f.loc[300:400]
hs_100r_25f_5 = hs_100r_25f.loc[400:500]
hs_100r_25f_6 = hs_100r_25f.loc[500:600]
hs_100r_25f_7 = hs_100r_25f.loc[600:700]
hs_100r_25f_8 = hs_100r_25f.loc[700:800]
hs_100r_25f_9 = hs_100r_25f.loc[800:900]
hs_100r_25f_10 = hs_100r_25f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_100r_25f_1 = np.mean(hs_100r_25f_1)
hsiv_100r_25f_2 = np.mean(hs_100r_25f_2)
hsiv_100r_25f_3 = np.mean(hs_100r_25f_3)
hsiv_100r_25f_4 = np.mean(hs_100r_25f_4)
hsiv_100r_25f_5 = np.mean(hs_100r_25f_5)
hsiv_100r_25f_6 = np.mean(hs_100r_25f_6)
hsiv_100r_25f_7 = np.mean(hs_100r_25f_7)
hsiv_100r_25f_8 = np.mean(hs_100r_25f_8)
hsiv_100r_25f_9 = np.mean(hs_100r_25f_9)
hsiv_100r_25f_10 = np.mean(hs_100r_25f_10)
# build df 
hsiv_100r_25f_tot = np.array([hsiv_100r_25f_1, hsiv_100r_25f_2, hsiv_100r_25f_3, hsiv_100r_25f_4, 
                                        hsiv_100r_25f_5, hsiv_100r_25f_6, hsiv_100r_25f_7, hsiv_100r_25f_8,
                                        hsiv_100r_25f_9, hsiv_100r_25f_10])
hsiv_100r_25f_tot = hsiv_100r_25f_tot.transpose() # switch rows and columns


### 100 rms 0.50 fdim ###
ls_100r_50f = pd.read_csv('low_sed_100r_50f.csv', index_col=0)
ls_100r_50f_1 = ls_100r_50f.loc[0:100]
ls_100r_50f_2 = ls_100r_50f.loc[100:200]
ls_100r_50f_3 = ls_100r_50f.loc[200:300]
ls_100r_50f_4 = ls_100r_50f.loc[300:400]
ls_100r_50f_5 = ls_100r_50f.loc[400:500]
ls_100r_50f_6 = ls_100r_50f.loc[500:600]
ls_100r_50f_7 = ls_100r_50f.loc[600:700]
ls_100r_50f_8 = ls_100r_50f.loc[700:800]
ls_100r_50f_9 = ls_100r_50f.loc[800:900]
ls_100r_50f_10 = ls_100r_50f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_100r_50f_1 = np.mean(ls_100r_50f_1)
lsiv_100r_50f_2 = np.mean(ls_100r_50f_2)
lsiv_100r_50f_3 = np.mean(ls_100r_50f_3)
lsiv_100r_50f_4 = np.mean(ls_100r_50f_4)
lsiv_100r_50f_5 = np.mean(ls_100r_50f_5)
lsiv_100r_50f_6 = np.mean(ls_100r_50f_6)
lsiv_100r_50f_7 = np.mean(ls_100r_50f_7)
lsiv_100r_50f_8 = np.mean(ls_100r_50f_8)
lsiv_100r_50f_9 = np.mean(ls_100r_50f_9)
lsiv_100r_50f_10 = np.mean(ls_100r_50f_10)
# build df 
lsiv_100r_50f_tot = np.array([lsiv_100r_50f_1, lsiv_100r_50f_2, lsiv_100r_50f_3, lsiv_100r_50f_4, 
                                        lsiv_100r_50f_5, lsiv_100r_50f_6, lsiv_100r_50f_7, lsiv_100r_50f_8,
                                        lsiv_100r_50f_9, lsiv_100r_50f_10])
lsiv_100r_50f_tot = lsiv_100r_50f_tot.transpose() # switch rows and columns

# med
ms_100r_50f = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0)
ms_100r_50f_1 = ms_100r_50f.loc[0:100]
ms_100r_50f_2 = ms_100r_50f.loc[100:200]
ms_100r_50f_3 = ms_100r_50f.loc[200:300]
ms_100r_50f_4 = ms_100r_50f.loc[300:400]
ms_100r_50f_5 = ms_100r_50f.loc[400:500]
ms_100r_50f_6 = ms_100r_50f.loc[500:600]
ms_100r_50f_7 = ms_100r_50f.loc[600:700]
ms_100r_50f_8 = ms_100r_50f.loc[700:800]
ms_100r_50f_9 = ms_100r_50f.loc[800:900]
ms_100r_50f_10 = ms_100r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_100r_50f_1 = np.mean(ms_100r_50f_1)
msiv_100r_50f_2 = np.mean(ms_100r_50f_2)
msiv_100r_50f_3 = np.mean(ms_100r_50f_3)
msiv_100r_50f_4 = np.mean(ms_100r_50f_4)
msiv_100r_50f_5 = np.mean(ms_100r_50f_5)
msiv_100r_50f_6 = np.mean(ms_100r_50f_6)
msiv_100r_50f_7 = np.mean(ms_100r_50f_7)
msiv_100r_50f_8 = np.mean(ms_100r_50f_8)
msiv_100r_50f_9 = np.mean(ms_100r_50f_9)
msiv_100r_50f_10 = np.mean(ms_100r_50f_10)
# build df 
msiv_100r_50f_tot = np.array([msiv_100r_50f_1, msiv_100r_50f_2, msiv_100r_50f_3, msiv_100r_50f_4, 
                                        msiv_100r_50f_5, msiv_100r_50f_6, msiv_100r_50f_7, msiv_100r_50f_8,
                                        msiv_100r_50f_9, msiv_100r_50f_10])
msiv_100r_50f_tot = msiv_100r_50f_tot.transpose() # switch rows and columns

### med - 10-members
msl_100r_50f = ms_100r_50f.iloc[:,:10]
msl_100r_50f_1 = msl_100r_50f.loc[0:100]
msl_100r_50f_2 = msl_100r_50f.loc[100:200]
msl_100r_50f_3 = msl_100r_50f.loc[200:300]
msl_100r_50f_4 = msl_100r_50f.loc[300:400]
msl_100r_50f_5 = msl_100r_50f.loc[400:500]
msl_100r_50f_6 = msl_100r_50f.loc[500:600]
msl_100r_50f_7 = msl_100r_50f.loc[600:700]
msl_100r_50f_8 = msl_100r_50f.loc[700:800]
msl_100r_50f_9 = msl_100r_50f.loc[800:900]
msl_100r_50f_10 = msl_100r_50f.loc[900:1000]
# get mean, iv = ice vol mean
msliv_100r_50f_1 = np.mean(msl_100r_50f_1)
msliv_100r_50f_2 = np.mean(msl_100r_50f_2)
msliv_100r_50f_3 = np.mean(msl_100r_50f_3)
msliv_100r_50f_4 = np.mean(msl_100r_50f_4)
msliv_100r_50f_5 = np.mean(msl_100r_50f_5)
msliv_100r_50f_6 = np.mean(msl_100r_50f_6)
msliv_100r_50f_7 = np.mean(msl_100r_50f_7)
msliv_100r_50f_8 = np.mean(msl_100r_50f_8)
msliv_100r_50f_9 = np.mean(msl_100r_50f_9)
msliv_100r_50f_10 = np.mean(msl_100r_50f_10)
# build df 
msliv_100r_50f_tot = np.array([msliv_100r_50f_1, msliv_100r_50f_2, msliv_100r_50f_3, msliv_100r_50f_4, 
                                        msliv_100r_50f_5, msliv_100r_50f_6, msliv_100r_50f_7, msliv_100r_50f_8,
                                        msliv_100r_50f_9, msliv_100r_50f_10])
msliv_100r_50f_tot = msliv_100r_50f_tot.transpose() # switch rows and columns

# high
hs_100r_50f = pd.read_csv('high_sed_100r_50f.csv', index_col=0)
hs_100r_50f_1 = hs_100r_50f.loc[0:100]
hs_100r_50f_2 = hs_100r_50f.loc[100:200]
hs_100r_50f_3 = hs_100r_50f.loc[200:300]
hs_100r_50f_4 = hs_100r_50f.loc[300:400]
hs_100r_50f_5 = hs_100r_50f.loc[400:500]
hs_100r_50f_6 = hs_100r_50f.loc[500:600]
hs_100r_50f_7 = hs_100r_50f.loc[600:700]
hs_100r_50f_8 = hs_100r_50f.loc[700:800]
hs_100r_50f_9 = hs_100r_50f.loc[800:900]
hs_100r_50f_10 = hs_100r_50f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_100r_50f_1 = np.mean(hs_100r_50f_1)
hsiv_100r_50f_2 = np.mean(hs_100r_50f_2)
hsiv_100r_50f_3 = np.mean(hs_100r_50f_3)
hsiv_100r_50f_4 = np.mean(hs_100r_50f_4)
hsiv_100r_50f_5 = np.mean(hs_100r_50f_5)
hsiv_100r_50f_6 = np.mean(hs_100r_50f_6)
hsiv_100r_50f_7 = np.mean(hs_100r_50f_7)
hsiv_100r_50f_8 = np.mean(hs_100r_50f_8)
hsiv_100r_50f_9 = np.mean(hs_100r_50f_9)
hsiv_100r_50f_10 = np.mean(hs_100r_50f_10)
# build df 
hsiv_100r_50f_tot = np.array([hsiv_100r_50f_1, hsiv_100r_50f_2, hsiv_100r_50f_3, hsiv_100r_50f_4, 
                                        hsiv_100r_50f_5, hsiv_100r_50f_6, hsiv_100r_50f_7, hsiv_100r_50f_8,
                                        hsiv_100r_50f_9, hsiv_100r_50f_10])
hsiv_100r_50f_tot = hsiv_100r_50f_tot.transpose() # switch rows and columns


### 100 rms 0.75 fdim ###
### low ###
ls_100r_75f = pd.read_csv('low_sed_100r_75f.csv', index_col=0)
ls_100r_75f_1 = ls_100r_75f.loc[0:100]
ls_100r_75f_2 = ls_100r_75f.loc[100:200]
ls_100r_75f_3 = ls_100r_75f.loc[200:300]
ls_100r_75f_4 = ls_100r_75f.loc[300:400]
ls_100r_75f_5 = ls_100r_75f.loc[400:500]
ls_100r_75f_6 = ls_100r_75f.loc[500:600]
ls_100r_75f_7 = ls_100r_75f.loc[600:700]
ls_100r_75f_8 = ls_100r_75f.loc[700:800]
ls_100r_75f_9 = ls_100r_75f.loc[800:900]
ls_100r_75f_10 = ls_100r_75f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_100r_75f_1 = np.mean(ls_100r_75f_1)
lsiv_100r_75f_2 = np.mean(ls_100r_75f_2)
lsiv_100r_75f_3 = np.mean(ls_100r_75f_3)
lsiv_100r_75f_4 = np.mean(ls_100r_75f_4)
lsiv_100r_75f_5 = np.mean(ls_100r_75f_5)
lsiv_100r_75f_6 = np.mean(ls_100r_75f_6)
lsiv_100r_75f_7 = np.mean(ls_100r_75f_7)
lsiv_100r_75f_8 = np.mean(ls_100r_75f_8)
lsiv_100r_75f_9 = np.mean(ls_100r_75f_9)
lsiv_100r_75f_10 = np.mean(ls_100r_75f_10)
# build df 
lsiv_100r_75f_tot = np.array([lsiv_100r_75f_1, lsiv_100r_75f_2, lsiv_100r_75f_3, lsiv_100r_75f_4, 
                                        lsiv_100r_75f_5, lsiv_100r_75f_6, lsiv_100r_75f_7, lsiv_100r_75f_8,
                                        lsiv_100r_75f_9, lsiv_100r_75f_10])
lsiv_100r_75f_tot = lsiv_100r_75f_tot.transpose() # switch rows and columns 

### med ###
ms_100r_75f = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0)
ms_100r_75f_1 = ms_100r_75f.loc[0:100]
ms_100r_75f_2 = ms_100r_75f.loc[100:200]
ms_100r_75f_3 = ms_100r_75f.loc[200:300]
ms_100r_75f_4 = ms_100r_75f.loc[300:400]
ms_100r_75f_5 = ms_100r_75f.loc[400:500]
ms_100r_75f_6 = ms_100r_75f.loc[500:600]
ms_100r_75f_7 = ms_100r_75f.loc[600:700]
ms_100r_75f_8 = ms_100r_75f.loc[700:800]
ms_100r_75f_9 = ms_100r_75f.loc[800:900]
ms_100r_75f_10 = ms_100r_75f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_100r_75f_1 = np.mean(ms_100r_75f_1)
msiv_100r_75f_2 = np.mean(ms_100r_75f_2)
msiv_100r_75f_3 = np.mean(ms_100r_75f_3)
msiv_100r_75f_4 = np.mean(ms_100r_75f_4)
msiv_100r_75f_5 = np.mean(ms_100r_75f_5)
msiv_100r_75f_6 = np.mean(ms_100r_75f_6)
msiv_100r_75f_7 = np.mean(ms_100r_75f_7)
msiv_100r_75f_8 = np.mean(ms_100r_75f_8)
msiv_100r_75f_9 = np.mean(ms_100r_75f_9)
msiv_100r_75f_10 = np.mean(ms_100r_75f_10)
# build df 
msiv_100r_75f_tot = np.array([msiv_100r_75f_1, msiv_100r_75f_2, msiv_100r_75f_3, msiv_100r_75f_4, 
                                        msiv_100r_75f_5, msiv_100r_75f_6, msiv_100r_75f_7, msiv_100r_75f_8,
                                        msiv_100r_75f_9, msiv_100r_75f_10])
msiv_100r_75f_tot = msiv_100r_75f_tot.transpose() # switch rows and columns

### high ###
hs_100r_75f = pd.read_csv('high_sed_100r_75f.csv', index_col=0)
hs_100r_75f_1 = hs_100r_75f.loc[0:100]
hs_100r_75f_2 = hs_100r_75f.loc[100:200]
hs_100r_75f_3 = hs_100r_75f.loc[200:300]
hs_100r_75f_4 = hs_100r_75f.loc[300:400]
hs_100r_75f_5 = hs_100r_75f.loc[400:500]
hs_100r_75f_6 = hs_100r_75f.loc[500:600]
hs_100r_75f_7 = hs_100r_75f.loc[600:700]
hs_100r_75f_8 = hs_100r_75f.loc[700:800]
hs_100r_75f_9 = hs_100r_75f.loc[800:900]
hs_100r_75f_10 = hs_100r_75f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_100r_75f_1 = np.mean(hs_100r_75f_1)
hsiv_100r_75f_2 = np.mean(hs_100r_75f_2)
hsiv_100r_75f_3 = np.mean(hs_100r_75f_3)
hsiv_100r_75f_4 = np.mean(hs_100r_75f_4)
hsiv_100r_75f_5 = np.mean(hs_100r_75f_5)
hsiv_100r_75f_6 = np.mean(hs_100r_75f_6)
hsiv_100r_75f_7 = np.mean(hs_100r_75f_7)
hsiv_100r_75f_8 = np.mean(hs_100r_75f_8)
hsiv_100r_75f_9 = np.mean(hs_100r_75f_9)
hsiv_100r_75f_10 = np.mean(hs_100r_75f_10)
# build df 
hsiv_100r_75f_tot = np.array([hsiv_100r_75f_1, hsiv_100r_75f_2, hsiv_100r_75f_3, hsiv_100r_75f_4, 
                                        hsiv_100r_75f_5, hsiv_100r_75f_6, hsiv_100r_75f_7, hsiv_100r_75f_8,
                                        hsiv_100r_75f_9, hsiv_100r_75f_10])
hsiv_100r_75f_tot = hsiv_100r_75f_tot.transpose() # switch rows and columns


### 100 rms 1.0 fdim ###
### low ###
ls_100r_10f = pd.read_csv('low_sed_100r_10f.csv', index_col=0)
ls_100r_10f_1 = ls_100r_10f.loc[0:100]
ls_100r_10f_2 = ls_100r_10f.loc[100:200]
ls_100r_10f_3 = ls_100r_10f.loc[200:300]
ls_100r_10f_4 = ls_100r_10f.loc[300:400]
ls_100r_10f_5 = ls_100r_10f.loc[400:500]
ls_100r_10f_6 = ls_100r_10f.loc[500:600]
ls_100r_10f_7 = ls_100r_10f.loc[600:700]
ls_100r_10f_8 = ls_100r_10f.loc[700:800]
ls_100r_10f_9 = ls_100r_10f.loc[800:900]
ls_100r_10f_10 = ls_100r_10f.loc[900:1000]
# get mean, iv = ice vol mean
lsiv_100r_10f_1 = np.mean(ls_100r_10f_1)
lsiv_100r_10f_2 = np.mean(ls_100r_10f_2)
lsiv_100r_10f_3 = np.mean(ls_100r_10f_3)
lsiv_100r_10f_4 = np.mean(ls_100r_10f_4)
lsiv_100r_10f_5 = np.mean(ls_100r_10f_5)
lsiv_100r_10f_6 = np.mean(ls_100r_10f_6)
lsiv_100r_10f_7 = np.mean(ls_100r_10f_7)
lsiv_100r_10f_8 = np.mean(ls_100r_10f_8)
lsiv_100r_10f_9 = np.mean(ls_100r_10f_9)
lsiv_100r_10f_10 = np.mean(ls_100r_10f_10)
# build df 
lsiv_100r_10f_tot = np.array([lsiv_100r_10f_1, lsiv_100r_10f_2, lsiv_100r_10f_3, lsiv_100r_10f_4, 
                                        lsiv_100r_10f_5, lsiv_100r_10f_6, lsiv_100r_10f_7, lsiv_100r_10f_8,
                                        lsiv_100r_10f_9, lsiv_100r_10f_10])
lsiv_100r_10f_tot = lsiv_100r_10f_tot.transpose() # switch rows and columns 

### med ###
ms_100r_10f = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0)
ms_100r_10f_1 = ms_100r_10f.loc[0:100]
ms_100r_10f_2 = ms_100r_10f.loc[100:200]
ms_100r_10f_3 = ms_100r_10f.loc[200:300]
ms_100r_10f_4 = ms_100r_10f.loc[300:400]
ms_100r_10f_5 = ms_100r_10f.loc[400:500]
ms_100r_10f_6 = ms_100r_10f.loc[500:600]
ms_100r_10f_7 = ms_100r_10f.loc[600:700]
ms_100r_10f_8 = ms_100r_10f.loc[700:800]
ms_100r_10f_9 = ms_100r_10f.loc[800:900]
ms_100r_10f_10 = ms_100r_10f.loc[900:1000]
# get mean, iv = ice vol mean
msiv_100r_10f_1 = np.mean(ms_100r_10f_1)
msiv_100r_10f_2 = np.mean(ms_100r_10f_2)
msiv_100r_10f_3 = np.mean(ms_100r_10f_3)
msiv_100r_10f_4 = np.mean(ms_100r_10f_4)
msiv_100r_10f_5 = np.mean(ms_100r_10f_5)
msiv_100r_10f_6 = np.mean(ms_100r_10f_6)
msiv_100r_10f_7 = np.mean(ms_100r_10f_7)
msiv_100r_10f_8 = np.mean(ms_100r_10f_8)
msiv_100r_10f_9 = np.mean(ms_100r_10f_9)
msiv_100r_10f_10 = np.mean(ms_100r_10f_10)
# build df 
msiv_100r_10f_tot = np.array([msiv_100r_10f_1, msiv_100r_10f_2, msiv_100r_10f_3, msiv_100r_10f_4, 
                                        msiv_100r_10f_5, msiv_100r_10f_6, msiv_100r_10f_7, msiv_100r_10f_8,
                                        msiv_100r_10f_9, msiv_100r_10f_10])
msiv_100r_10f_tot = msiv_100r_10f_tot.transpose() # switch rows and columns

### high ###
hs_100r_10f = pd.read_csv('high_sed_100r_10f.csv', index_col=0)
hs_100r_10f_1 = hs_100r_10f.loc[0:100]
hs_100r_10f_2 = hs_100r_10f.loc[100:200]
hs_100r_10f_3 = hs_100r_10f.loc[200:300]
hs_100r_10f_4 = hs_100r_10f.loc[300:400]
hs_100r_10f_5 = hs_100r_10f.loc[400:500]
hs_100r_10f_6 = hs_100r_10f.loc[500:600]
hs_100r_10f_7 = hs_100r_10f.loc[600:700]
hs_100r_10f_8 = hs_100r_10f.loc[700:800]
hs_100r_10f_9 = hs_100r_10f.loc[800:900]
hs_100r_10f_10 = hs_100r_10f.loc[900:1000]
# get mean, iv = ice vol mean
hsiv_100r_10f_1 = np.mean(hs_100r_10f_1)
hsiv_100r_10f_2 = np.mean(hs_100r_10f_2)
hsiv_100r_10f_3 = np.mean(hs_100r_10f_3)
hsiv_100r_10f_4 = np.mean(hs_100r_10f_4)
hsiv_100r_10f_5 = np.mean(hs_100r_10f_5)
hsiv_100r_10f_6 = np.mean(hs_100r_10f_6)
hsiv_100r_10f_7 = np.mean(hs_100r_10f_7)
hsiv_100r_10f_8 = np.mean(hs_100r_10f_8)
hsiv_100r_10f_9 = np.mean(hs_100r_10f_9)
hsiv_100r_10f_10 = np.mean(hs_100r_10f_10)
# build df 
hsiv_100r_10f_tot = np.array([hsiv_100r_10f_1, hsiv_100r_10f_2, hsiv_100r_10f_3, hsiv_100r_10f_4, 
                                        hsiv_100r_10f_5, hsiv_100r_10f_6, hsiv_100r_10f_7, hsiv_100r_10f_8,
                                        hsiv_100r_10f_9, hsiv_100r_10f_10])
hsiv_100r_10f_tot = hsiv_100r_10f_tot.transpose() # switch rows and columns


###################################
####### plot across rms ###########
###################################

sns_years_lbl = ['0-100 years','100-200','200-300','300-400','400-500','500-600','600-700','700-800','800-900','900-1000']

#plt.tight_layout

#### 25 rms ####

### 25 rms 0.25 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 25 rms 0.25 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_25r_25f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_25r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_25r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,1.0e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_25r_25f_all_sed.png", dpi=800)


### 25 rms 0.50 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 25 rms 0.50 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_25r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_25r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_25r_50f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,1.2e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_25r_50f_all_sed.png", dpi=800)


### 25 rms 0.75 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 25 rms 0.75 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_25r_75f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_25r_75f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_25r_75f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,1.2e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_25r_75f_all_sed.png", dpi=800)


### 25 rms 1.0 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 25 rms 1.0 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_25r_10f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_25r_10f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_25r_10f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,1.2e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_25r_10f_all_sed.png", dpi=800)



#### 50 rms ####

### 50 rms 0.25 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 50 rms 0.25 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_50r_25f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_50r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_50r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_50r_25f_all_sed.png", dpi=800)


### 50 rms 0.50 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 50 rms 0.50 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_50r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_50r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_50r_50f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_50r_50f_all_sed.png", dpi=800)


### 50 rms 0.75 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 50 rms 0.75 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_50r_75f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_50r_75f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_50r_75f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_50r_75f_all_sed.png", dpi=800)


### 50 rms 1.0 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 50 rms 1.0 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_50r_10f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_50r_10f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_50r_10f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_50r_10f_all_sed.png", dpi=800)



#### 75 rms ####

### 75 rms 0.25 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 75 rms 0.25 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_75r_25f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_75r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_75r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_75r_25f_all_sed.png", dpi=800)

### 75 rms 0.50 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(3,1,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 75 rms 0.50 fdim (10-members)', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
rcParams['figure.figsize'] = 8, 8
sns.kdeplot(data=lsiv_75r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_75r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_75r_50f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.8e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_75r_50f_all_sed.png", dpi=800)


### 75 rms 0.75 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 75 rms 0.75 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_75r_75f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_75r_75f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_75r_75f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_75r_75f_all_sed.png", dpi=800)


### 75 rms 1.0 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 75 rms 1.0 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_75r_10f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_75r_10f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_75r_10f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_75r_10f_all_sed.png", dpi=800)




#### 100 rms ####

### 100 rms 0.25 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 100 rms 0.25 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_100r_25f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_100r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_100r_25f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_100r_25f_all_sed.png", dpi=800)

### 100 rms 0.50 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 100 rms 0.50 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_100r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_100r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_100r_50f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.8e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_100r_50f_all_sed.png", dpi=800)


### 100 rms 0.75 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 100 rms 0.75 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_100r_75f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_100r_75f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_100r_75f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_100r_75f_all_sed.png", dpi=800)


### 100 rms 1.0 fdim plot ###
fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 100 rms 1.0 fdim', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=lsiv_100r_10f_tot, fill=True, ls='-', lw=2, palette = "crest", label='low sed', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msiv_100r_10f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = 'med sed', ax = ax2)
sns.kdeplot(data = hsiv_100r_10f_tot, fill=None, ls= '-.', lw = 2, palette = "crest", label = 'high sed', ax = ax3)
for ax in (ax1,ax2,ax3):
    ax.set(ylim=[0,0.7e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('low sed', pad=20)
ax2.set_title('med sed',pad=20)
ax3.set_title('high sed',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
ax3.get_legend().remove()
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("kde_100r_10f_all_sed.png", dpi=800)




########### comparing 10 vs 100 ensemble members #############

### 75 rms 0.50 fdim plot ###
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 75 rms 0.50 fdim (10 vs. 100-members, medium sed)', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
rcParams['figure.figsize'] = 8, 8
sns.kdeplot(data=msiv_75r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='100-members', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msliv_75r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = '10-members', ax = ax2)
for ax in (ax1,ax2):
    ax.set(xlim=[0,3.5e8],ylim=[0,0.6e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('100-members', pad=20)
ax2.set_title('10-members',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
fig.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(0.75, 0.75))
plt.savefig("kde_75r_50f_all_sed_10vs100mems.png", dpi=800)

### 100 rms 0.25 fdim plot ###
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,sharey=True)
fig.subplots_adjust(top=0.8)
fig.suptitle('Gaussian KDE of Ice Volume - 100 rms 0.50 fdim (10 vs. 100-members, medium sed)', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
rcParams['figure.figsize'] = 8, 8
sns.kdeplot(data=msiv_100r_50f_tot, fill=True, ls='-', lw=2, palette = "crest", label='100-members', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
sns.kdeplot(data = msliv_100r_50f_tot, fill=None, ls= '--', lw = 2, palette = "crest", label = '10-members', ax = ax2)
for ax in (ax1,ax2):
    ax.set(xlim=[0,3.5e8],ylim=[0,0.6e-7])
fig.subplots_adjust(bottom=0.2)
ax1.set_title('100-members', pad=20)
ax2.set_title('10-members',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
fig.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
legend = fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center right', bbox_to_anchor=(0.95, 0.75))
plt.savefig("kde_100r_50f_all_sed_10vs100mems.png", dpi=800)

def export_legend(legend, filename="legend.png"):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi=800, bbox_inches=bbox)

export_legend(legend)
plt.show()

