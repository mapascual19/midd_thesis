#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:53:20 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


###################################
### load data and collect stats ###
###################################

####### control ########
ctrl_SED = pd.read_csv('ice_vol_1000yr_control_case.csv', index_col=0)


######## 25 rms ########

### 25 rms 0.25 fdim ###
# low
ls_25r_25f = pd.read_csv('low_sed_25r_25f.csv', index_col=0)
ls_25r_25f_q1 = ls_25r_25f.quantile(q=0.25, axis=1)
ls_25r_25f_q3 = ls_25r_25f.quantile(q=0.75, axis=1)
# med
ms_25r_25f = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)
# ms_25r_25f = ms_25r_25f.iloc[:,:10]
ms_25r_25f_q1 = ms_25r_25f.quantile(q=0.25, axis=1)
ms_25r_25f_q3 = ms_25r_25f.quantile(q=0.75, axis=1)
# high
hs_25r_25f = pd.read_csv('high_sed_25r_25f.csv', index_col=0)
hs_25r_25f_q1 = hs_25r_25f.quantile(q=0.25, axis=1)
hs_25r_25f_q3 = hs_25r_25f.quantile(q=0.75, axis=1)

### 25 rms 0.50 fdim ###
# low
ls_25r_50f = pd.read_csv('low_sed_25r_50f.csv', index_col=0)
ls_25r_50f_q1 = ls_25r_50f.quantile(q=0.25, axis=1)
ls_25r_50f_q3 = ls_25r_50f.quantile(q=0.75, axis=1)
# med
ms_25r_50f = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0)
# ms_25r_50f = ms_25r_50f.iloc[:,:10]
ms_25r_50f_q1 = ms_25r_50f.quantile(q=0.25, axis=1)
ms_25r_50f_q3 = ms_25r_50f.quantile(q=0.75, axis=1)
# high
hs_25r_50f = pd.read_csv('high_sed_25r_50f.csv', index_col=0)
hs_25r_50f_q1 = hs_25r_50f.quantile(q=0.25, axis=1)
hs_25r_50f_q3 = hs_25r_50f.quantile(q=0.75, axis=1)

### 25 rms 0.75 fdim ###
# low
ls_25r_75f = pd.read_csv('low_sed_25r_75f.csv', index_col=0)
ls_25r_75f_q1 = ls_25r_75f.quantile(q=0.25, axis=1)
ls_25r_75f_q3 = ls_25r_75f.quantile(q=0.75, axis=1)
# med
ms_25r_75f = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0)
# ms_25r_75f = ms_25r_75f.iloc[:,:10]
ms_25r_75f_q1 = ms_25r_75f.quantile(q=0.25, axis=1)
ms_25r_75f_q3 = ms_25r_75f.quantile(q=0.75, axis=1)
# high
hs_25r_75f = pd.read_csv('high_sed_25r_75f.csv', index_col=0)
hs_25r_75f_q1 = hs_25r_75f.quantile(q=0.25, axis=1)
hs_25r_75f_q3 = hs_25r_75f.quantile(q=0.75, axis=1)

### 25 rms 1.0 fdim ###
# low
ls_25r_10f = pd.read_csv('low_sed_25r_10f.csv', index_col=0)
ls_25r_10f_q1 = ls_25r_10f.quantile(q=0.25, axis=1)
ls_25r_10f_q3 = ls_25r_10f.quantile(q=0.75, axis=1)
# med
ms_25r_10f = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)
# ms_25r_10f = ms_25r_10f.iloc[:,:10]
ms_25r_10f_q1 = ms_25r_10f.quantile(q=0.25, axis=1)
ms_25r_10f_q3 = ms_25r_10f.quantile(q=0.75, axis=1)
# high
hs_25r_10f = pd.read_csv('high_sed_25r_10f.csv', index_col=0)
hs_25r_10f_q1 = hs_25r_10f.quantile(q=0.25, axis=1)
hs_25r_10f_q3 = hs_25r_10f.quantile(q=0.75, axis=1)



######## 50 rms ########

### 50 rms 0.25 fdim ###
# low
ls_50r_25f = pd.read_csv('low_sed_50r_25f.csv', index_col=0)
ls_50r_25f_q1 = ls_50r_25f.quantile(q=0.25, axis=1)
ls_50r_25f_q3 = ls_50r_25f.quantile(q=0.75, axis=1)
# med
ms_50r_25f = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0)
# ms_50r_25f = ms_50r_25f.iloc[:,:10]
ms_50r_25f_q1 = ms_50r_25f.quantile(q=0.25, axis=1)
ms_50r_25f_q3 = ms_50r_25f.quantile(q=0.75, axis=1)
# high
hs_50r_25f = pd.read_csv('high_sed_50r_25f.csv', index_col=0)
hs_50r_25f_q1 = hs_50r_25f.quantile(q=0.25, axis=1)
hs_50r_25f_q3 = hs_50r_25f.quantile(q=0.75, axis=1)

### 50 rms 0.50 fdim ###
# low
ls_50r_50f = pd.read_csv('low_sed_50r_50f.csv', index_col=0)
ls_50r_50f_q1 = ls_50r_50f.quantile(q=0.25, axis=1)
ls_50r_50f_q3 = ls_50r_50f.quantile(q=0.75, axis=1)
# med
ms_50r_50f = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0)
# ms_50r_50f = ms_50r_50f.iloc[:,:10]
ms_50r_50f_q1 = ms_50r_50f.quantile(q=0.25, axis=1)
ms_50r_50f_q3 = ms_50r_50f.quantile(q=0.75, axis=1)
# high
hs_50r_50f = pd.read_csv('high_sed_50r_50f.csv', index_col=0)
hs_50r_50f_q1 = hs_50r_50f.quantile(q=0.25, axis=1)
hs_50r_50f_q3 = hs_50r_50f.quantile(q=0.75, axis=1)

### 50 rms 0.75 fdim ###
# low
ls_50r_75f = pd.read_csv('low_sed_50r_75f.csv', index_col=0)
ls_50r_75f_q1 = ls_50r_75f.quantile(q=0.25, axis=1)
ls_50r_75f_q3 = ls_50r_75f.quantile(q=0.75, axis=1)
# med
ms_50r_75f = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0)
# ms_50r_75f = ms_50r_75f.iloc[:,:10]
ms_50r_75f_q1 = ms_50r_75f.quantile(q=0.25, axis=1)
ms_50r_75f_q3 = ms_50r_75f.quantile(q=0.75, axis=1)
# high
hs_50r_75f = pd.read_csv('high_sed_50r_75f.csv', index_col=0)
hs_50r_75f_q1 = hs_50r_75f.quantile(q=0.25, axis=1)
hs_50r_75f_q3 = hs_50r_75f.quantile(q=0.75, axis=1)

### 50 rms 1.0 fdim ###
# low
ls_50r_10f = pd.read_csv('low_sed_50r_10f.csv', index_col=0)
ls_50r_10f_q1 = ls_50r_10f.quantile(q=0.25, axis=1)
ls_50r_10f_q3 = ls_50r_10f.quantile(q=0.75, axis=1)
# med
ms_50r_10f = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0)
# ms_50r_10f = ms_50r_10f.iloc[:,:10]
ms_50r_10f_q1 = ms_50r_10f.quantile(q=0.25, axis=1)
ms_50r_10f_q3 = ms_50r_10f.quantile(q=0.75, axis=1)
# high
hs_50r_10f = pd.read_csv('high_sed_50r_10f.csv', index_col=0)
hs_50r_10f_q1 = hs_50r_10f.quantile(q=0.25, axis=1)
hs_50r_10f_q3 = hs_50r_10f.quantile(q=0.75, axis=1)



######## 75 rms ########

### 75 rms 0.25 fdim ###
# low
ls_75r_25f = pd.read_csv('low_sed_75r_25f.csv', index_col=0)
ls_75r_25f_q1 = ls_75r_25f.quantile(q=0.25, axis=1)
ls_75r_25f_q3 = ls_75r_25f.quantile(q=0.75, axis=1)
# med
ms_75r_25f = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0)
# ms_75r_25f = ms_75r_25f.iloc[:,:10]
ms_75r_25f_q1 = ms_75r_25f.quantile(q=0.25, axis=1)
ms_75r_25f_q3 = ms_75r_25f.quantile(q=0.75, axis=1)
# high
hs_75r_25f = pd.read_csv('high_sed_75r_25f.csv', index_col=0)
hs_75r_25f_q1 = hs_75r_25f.quantile(q=0.25, axis=1)
hs_75r_25f_q3 = hs_75r_25f.quantile(q=0.75, axis=1)

### 75 rms 0.50 fdim ###
# low
ls_75r_50f = pd.read_csv('low_sed_75r_50f.csv', index_col=0)
ls_75r_50f_q1 = ls_75r_50f.quantile(q=0.25, axis=1)
ls_75r_50f_q3 = ls_75r_50f.quantile(q=0.75, axis=1)
# med
ms_75r_50f = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0)
# ms_75r_50f = ms_75r_50f.iloc[:,:10]
ms_75r_50f_q1 = ms_75r_50f.quantile(q=0.25, axis=1)
ms_75r_50f_q3 = ms_75r_50f.quantile(q=0.75, axis=1)
# high
hs_75r_50f = pd.read_csv('high_sed_75r_50f.csv', index_col=0)
hs_75r_50f_q1 = hs_75r_50f.quantile(q=0.25, axis=1)
hs_75r_50f_q3 = hs_75r_50f.quantile(q=0.75, axis=1)

### 75 rms 0.75 fdim ###
# low
ls_75r_75f = pd.read_csv('low_sed_75r_75f.csv', index_col=0)
ls_75r_75f_q1 = ls_75r_75f.quantile(q=0.25, axis=1)
ls_75r_75f_q3 = ls_75r_75f.quantile(q=0.75, axis=1)
# med
ms_75r_75f = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0)
# ms_75r_75f = ms_75r_75f.iloc[:,:10]
ms_75r_75f_q1 = ms_75r_75f.quantile(q=0.25, axis=1)
ms_75r_75f_q3 = ms_75r_75f.quantile(q=0.75, axis=1)
# high
hs_75r_75f = pd.read_csv('high_sed_75r_75f.csv', index_col=0)
hs_75r_75f_q1 = hs_75r_75f.quantile(q=0.25, axis=1)
hs_75r_75f_q3 = hs_75r_75f.quantile(q=0.75, axis=1)

### 75 rms 1.0 fdim ###
# low
ls_75r_10f = pd.read_csv('low_sed_75r_10f.csv', index_col=0)
ls_75r_10f_q1 = ls_75r_10f.quantile(q=0.25, axis=1)
ls_75r_10f_q3 = ls_75r_10f.quantile(q=0.75, axis=1)
# med
ms_75r_10f = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0)
# ms_75r_10f = ms_75r_10f.iloc[:,:10]
ms_75r_10f_q1 = ms_75r_10f.quantile(q=0.25, axis=1)
ms_75r_10f_q3 = ms_75r_10f.quantile(q=0.75, axis=1)
# high
hs_75r_10f = pd.read_csv('high_sed_75r_10f.csv', index_col=0)
hs_75r_10f_q1 = hs_75r_10f.quantile(q=0.25, axis=1)
hs_75r_10f_q3 = hs_75r_10f.quantile(q=0.75, axis=1)



######## 100 rms ########

### 100 rms 0.25 fdim ###
# low
ls_100r_25f = pd.read_csv('low_sed_100r_25f.csv', index_col=0)
ls_100r_25f_q1 = ls_100r_25f.quantile(q=0.25, axis=1)
ls_100r_25f_q3 = ls_100r_25f.quantile(q=0.75, axis=1)
# med
ms_100r_25f = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0)
# ms_100r_25f = ms_100r_25f.iloc[:,:10]
ms_100r_25f_q1 = ms_100r_25f.quantile(q=0.25, axis=1)
ms_100r_25f_q3 = ms_100r_25f.quantile(q=0.75, axis=1)
# high
hs_100r_25f = pd.read_csv('high_sed_100r_25f.csv', index_col=0)
hs_100r_25f_q1 = hs_100r_25f.quantile(q=0.25, axis=1)
hs_100r_25f_q3 = hs_100r_25f.quantile(q=0.75, axis=1)

### 100 rms 0.50 fdim ###
# low
ls_100r_50f = pd.read_csv('low_sed_100r_50f.csv', index_col=0)
ls_100r_50f_q1 = ls_100r_50f.quantile(q=0.25, axis=1)
ls_100r_50f_q3 = ls_100r_50f.quantile(q=0.75, axis=1)
# med
ms_100r_50f = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0)
# ms_100r_50f = ms_100r_50f.iloc[:,:10]
ms_100r_50f_q1 = ms_100r_50f.quantile(q=0.25, axis=1)
ms_100r_50f_q3 = ms_100r_50f.quantile(q=0.75, axis=1)
# high
hs_100r_50f = pd.read_csv('high_sed_100r_50f.csv', index_col=0)
hs_100r_50f_q1 = hs_100r_50f.quantile(q=0.25, axis=1)
hs_100r_50f_q3 = hs_100r_50f.quantile(q=0.75, axis=1)

### 100 rms 0.75 fdim ###
# low
ls_100r_75f = pd.read_csv('low_sed_100r_75f.csv', index_col=0)
ls_100r_75f_q1 = ls_100r_75f.quantile(q=0.25, axis=1)
ls_100r_75f_q3 = ls_100r_75f.quantile(q=0.75, axis=1)
# med
ms_100r_75f = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0)
# ms_100r_75f = ms_100r_75f.iloc[:,:10]
ms_100r_75f_q1 = ms_100r_75f.quantile(q=0.25, axis=1)
ms_100r_75f_q3 = ms_100r_75f.quantile(q=0.75, axis=1)
# high
hs_100r_75f = pd.read_csv('high_sed_100r_75f.csv', index_col=0)
hs_100r_75f_q1 = hs_100r_75f.quantile(q=0.25, axis=1)
hs_100r_75f_q3 = hs_100r_75f.quantile(q=0.75, axis=1)

### 100 rms 1.0 fdim ###
# low
ls_100r_10f = pd.read_csv('low_sed_100r_10f.csv', index_col=0)
ls_100r_10f_q1 = ls_100r_10f.quantile(q=0.25, axis=1)
ls_100r_10f_q3 = ls_100r_10f.quantile(q=0.75, axis=1)
# med
ms_100r_10f = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0)
# ms_100r_10f = ms_100r_10f.iloc[:,:10]
ms_100r_10f_q1 = ms_100r_10f.quantile(q=0.25, axis=1)
ms_100r_10f_q3 = ms_100r_10f.quantile(q=0.75, axis=1)
# high
hs_100r_10f = pd.read_csv('high_sed_100r_10f.csv', index_col=0)
hs_100r_10f_q1 = hs_100r_10f.quantile(q=0.25, axis=1)
hs_100r_10f_q3 = hs_100r_10f.quantile(q=0.75, axis=1)


###################################
####### plot across rms ###########
###################################

### 25 rms plot ###

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - 25 rms, all fdim')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# 0.25 fdim
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ls_25r_25f.mean(axis=1), ls = '-', label='low sed')
ax1.plot(ls_25r_25f_q1,c='b',ls = '-')
ax1.plot(ls_25r_25f_q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(ls_25r_25f_q1)),ls_25r_25f_q1,ls_25r_25f_q3, alpha=0.2)
ax1.plot(ms_25r_25f.mean(axis=1), ls = '-', label='med sed')
ax1.plot(ms_25r_25f_q1,c='orange',ls = '--')
ax1.plot(ms_25r_25f_q3,c='orange',ls = '--')
ax1.fill_between(np.arange(len(ms_25r_25f_q1)),ms_25r_25f_q1,ms_25r_25f_q3, alpha=0.2)
ax1.plot(hs_25r_25f.mean(axis=1), ls = '-.', label='high sed')
ax1.plot(hs_25r_25f_q1,c='g', ls = '-.')
ax1.plot(hs_25r_25f_q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(hs_25r_25f_q1)),hs_25r_25f_q1,hs_25r_25f_q3, alpha=0.2)
# 0.50 fdim
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ls_25r_50f.mean(axis=1), ls = '-', label='low sed')
ax2.plot(ls_25r_50f_q1,c='b',ls = '-')
ax2.plot(ls_25r_50f_q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(ls_25r_50f_q1)),ls_25r_50f_q1,ls_25r_50f_q3, alpha=0.2)
ax2.plot(ms_25r_50f.mean(axis=1), ls = '-', label='med sed')
ax2.plot(ms_25r_50f_q1,c='orange',ls = '--')
ax2.plot(ms_25r_50f_q3,c='orange',ls = '--')
ax2.fill_between(np.arange(len(ms_25r_50f_q1)),ms_25r_50f_q1,ms_25r_50f_q3, alpha=0.2)
ax2.plot(hs_25r_50f.mean(axis=1), ls = '-.', label='high sed')
ax2.plot(hs_25r_50f_q1,c='g', ls = '-.')
ax2.plot(hs_25r_50f_q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(hs_25r_50f_q1)),hs_25r_50f_q1,hs_25r_50f_q3, alpha=0.2)
# 0.75 fdim
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ls_25r_75f.mean(axis=1), ls = '-', label='low sed')
ax3.plot(ls_25r_75f_q1,c='b',ls = '-')
ax3.plot(ls_25r_75f_q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(ls_25r_75f_q1)),ls_25r_75f_q1,ls_25r_75f_q3, alpha=0.2)
ax3.plot(ms_25r_75f.mean(axis=1), ls = '-', label='med sed')
ax3.plot(ms_25r_75f_q1,c='orange',ls = '--')
ax3.plot(ms_25r_75f_q3,c='orange',ls = '--')
ax3.fill_between(np.arange(len(ms_25r_75f_q1)),ms_25r_75f_q1,ms_25r_75f_q3, alpha=0.2)
ax3.plot(hs_25r_75f.mean(axis=1), ls = '-.', label='high sed')
ax3.plot(hs_25r_75f_q1,c='g', ls = '-.')
ax3.plot(hs_25r_75f_q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(hs_25r_75f_q1)),hs_25r_75f_q1,hs_25r_75f_q3, alpha=0.2)
# 1.0 fdim
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ls_25r_10f.mean(axis=1), ls = '-', label='low sed')
ax4.plot(ls_25r_10f_q1,c='b',ls = '-')
ax4.plot(ls_25r_10f_q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(ls_25r_10f_q1)),ls_25r_10f_q1,ls_25r_10f_q3, alpha=0.2)
ax4.plot(ms_25r_10f.mean(axis=1), ls = '-', label='med sed')
ax4.plot(ms_25r_10f_q1,c='orange',ls = '--')
ax4.plot(ms_25r_10f_q3,c='orange',ls = '--')
ax4.fill_between(np.arange(len(ms_25r_10f_q1)),ms_25r_10f_q1,ms_25r_10f_q3, alpha=0.2)
ax4.plot(hs_25r_10f.mean(axis=1), ls = '-.', label='high sed')
ax4.plot(hs_25r_10f_q1,c='g', ls = '-.')
ax4.plot(hs_25r_10f_q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(hs_25r_10f_q1)),hs_25r_10f_q1,hs_25r_10f_q3, alpha=0.2)
plt.savefig("25rms_all_sed_quantile_ice_vol_no_equal_mem.png", dpi=800)



### 50 rms plot ###

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - 50 rms, all fdim')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# 0.25 fdim
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ls_50r_25f.mean(axis=1), ls = '-', label='low sed')
ax1.plot(ls_50r_25f_q1,c='b',ls = '-')
ax1.plot(ls_50r_25f_q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(ls_50r_25f_q1)),ls_50r_25f_q1,ls_50r_25f_q3, alpha=0.2)
ax1.plot(ms_50r_25f.mean(axis=1), ls = '-', label='med sed')
ax1.plot(ms_50r_25f_q1,c='orange',ls = '--')
ax1.plot(ms_50r_25f_q3,c='orange',ls = '--')
ax1.fill_between(np.arange(len(ms_50r_25f_q1)),ms_50r_25f_q1,ms_50r_25f_q3, alpha=0.2)
ax1.plot(hs_50r_25f.mean(axis=1), ls = '-.', label='high sed')
ax1.plot(hs_50r_25f_q1,c='g', ls = '-.')
ax1.plot(hs_50r_25f_q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(hs_50r_25f_q1)),hs_50r_25f_q1,hs_50r_25f_q3, alpha=0.2)
# 0.50 fdim
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ls_50r_50f.mean(axis=1), ls = '-', label='low sed')
ax2.plot(ls_50r_50f_q1,c='b',ls = '-')
ax2.plot(ls_50r_50f_q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(ls_50r_50f_q1)),ls_50r_50f_q1,ls_50r_50f_q3, alpha=0.2)
ax2.plot(ms_50r_50f.mean(axis=1), ls = '-', label='med sed')
ax2.plot(ms_50r_50f_q1,c='orange',ls = '--')
ax2.plot(ms_50r_50f_q3,c='orange',ls = '--')
ax2.fill_between(np.arange(len(ms_50r_50f_q1)),ms_50r_50f_q1,ms_50r_50f_q3, alpha=0.2)
ax2.plot(hs_50r_50f.mean(axis=1), ls = '-.', label='high sed')
ax2.plot(hs_50r_50f_q1,c='g', ls = '-.')
ax2.plot(hs_50r_50f_q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(hs_50r_50f_q1)),hs_50r_50f_q1,hs_50r_50f_q3, alpha=0.2)
# 0.75 fdim
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ls_50r_75f.mean(axis=1), ls = '-', label='low sed')
ax3.plot(ls_50r_75f_q1,c='b',ls = '-')
ax3.plot(ls_50r_75f_q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(ls_50r_75f_q1)),ls_50r_75f_q1,ls_50r_75f_q3, alpha=0.2)
ax3.plot(ms_50r_75f.mean(axis=1), ls = '-', label='med sed')
ax3.plot(ms_50r_75f_q1,c='orange',ls = '--')
ax3.plot(ms_50r_75f_q3,c='orange',ls = '--')
ax3.fill_between(np.arange(len(ms_50r_75f_q1)),ms_50r_75f_q1,ms_50r_75f_q3, alpha=0.2)
ax3.plot(hs_50r_75f.mean(axis=1), ls = '-.', label='high sed')
ax3.plot(hs_50r_75f_q1,c='g', ls = '-.')
ax3.plot(hs_50r_75f_q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(hs_50r_75f_q1)),hs_50r_75f_q1,hs_50r_75f_q3, alpha=0.2)
# 1.0 fdim
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ls_50r_10f.mean(axis=1), ls = '-', label='low sed')
ax4.plot(ls_50r_10f_q1,c='b',ls = '-')
ax4.plot(ls_50r_10f_q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(ls_50r_10f_q1)),ls_50r_10f_q1,ls_50r_10f_q3, alpha=0.2)
ax4.plot(ms_50r_10f.mean(axis=1), ls = '-', label='med sed')
ax4.plot(ms_50r_10f_q1,c='orange',ls = '--')
ax4.plot(ms_50r_10f_q3,c='orange',ls = '--')
ax4.fill_between(np.arange(len(ms_50r_10f_q1)),ms_50r_10f_q1,ms_50r_10f_q3, alpha=0.2)
ax4.plot(hs_50r_10f.mean(axis=1), ls = '-.', label='high sed')
ax4.plot(hs_50r_10f_q1,c='g', ls = '-.')
ax4.plot(hs_50r_10f_q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(hs_50r_10f_q1)),hs_50r_10f_q1,hs_50r_10f_q3, alpha=0.2)
plt.savefig("50rms_all_sed_quantile_ice_vol_no_equal_mem.png", dpi=800)



### 75 rms plot ###

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - 75 rms, all fdim')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# 0.25 fdim
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ls_75r_25f.mean(axis=1), ls = '-', label='low sed')
ax1.plot(ls_75r_25f_q1,c='b',ls = '-')
ax1.plot(ls_75r_25f_q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(ls_75r_25f_q1)),ls_75r_25f_q1,ls_75r_25f_q3, alpha=0.2)
ax1.plot(ms_75r_25f.mean(axis=1), ls = '-', label='med sed')
ax1.plot(ms_75r_25f_q1,c='orange',ls = '--')
ax1.plot(ms_75r_25f_q3,c='orange',ls = '--')
ax1.fill_between(np.arange(len(ms_75r_25f_q1)),ms_75r_25f_q1,ms_75r_25f_q3, alpha=0.2)
ax1.plot(hs_75r_25f.mean(axis=1), ls = '-.', label='high sed')
ax1.plot(hs_75r_25f_q1,c='g', ls = '-.')
ax1.plot(hs_75r_25f_q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(hs_75r_25f_q1)),hs_75r_25f_q1,hs_75r_25f_q3, alpha=0.2)
# 0.50 fdim
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ls_75r_50f.mean(axis=1), ls = '-', label='low sed')
ax2.plot(ls_75r_50f_q1,c='b',ls = '-')
ax2.plot(ls_75r_50f_q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(ls_75r_50f_q1)),ls_75r_50f_q1,ls_75r_50f_q3, alpha=0.2)
ax2.plot(ms_75r_50f.mean(axis=1), ls = '-', label='med sed')
ax2.plot(ms_75r_50f_q1,c='orange',ls = '--')
ax2.plot(ms_75r_50f_q3,c='orange',ls = '--')
ax2.fill_between(np.arange(len(ms_75r_50f_q1)),ms_75r_50f_q1,ms_75r_50f_q3, alpha=0.2)
ax2.plot(hs_75r_50f.mean(axis=1), ls = '-.', label='high sed')
ax2.plot(hs_75r_50f_q1,c='g', ls = '-.')
ax2.plot(hs_75r_50f_q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(hs_75r_50f_q1)),hs_75r_50f_q1,hs_75r_50f_q3, alpha=0.2)
# 0.75 fdim
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ls_75r_75f.mean(axis=1), ls = '-', label='low sed')
ax3.plot(ls_75r_75f_q1,c='b',ls = '-')
ax3.plot(ls_75r_75f_q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(ls_75r_75f_q1)),ls_75r_75f_q1,ls_75r_75f_q3, alpha=0.2)
ax3.plot(ms_75r_75f.mean(axis=1), ls = '-', label='med sed')
ax3.plot(ms_75r_75f_q1,c='orange',ls = '--')
ax3.plot(ms_75r_75f_q3,c='orange',ls = '--')
ax3.fill_between(np.arange(len(ms_75r_75f_q1)),ms_75r_75f_q1,ms_75r_75f_q3, alpha=0.2)
ax3.plot(hs_75r_75f.mean(axis=1), ls = '-.', label='high sed')
ax3.plot(hs_75r_75f_q1,c='g', ls = '-.')
ax3.plot(hs_75r_75f_q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(hs_75r_75f_q1)),hs_75r_75f_q1,hs_75r_75f_q3, alpha=0.2)
# 1.0 fdim
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ls_75r_10f.mean(axis=1), ls = '-', label='low sed')
ax4.plot(ls_75r_10f_q1,c='b',ls = '-')
ax4.plot(ls_75r_10f_q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(ls_75r_10f_q1)),ls_75r_10f_q1,ls_75r_10f_q3, alpha=0.2)
ax4.plot(ms_75r_10f.mean(axis=1), ls = '-', label='med sed')
ax4.plot(ms_75r_10f_q1,c='orange',ls = '--')
ax4.plot(ms_75r_10f_q3,c='orange',ls = '--')
ax4.fill_between(np.arange(len(ms_75r_10f_q1)),ms_75r_10f_q1,ms_75r_10f_q3, alpha=0.2)
ax4.plot(hs_75r_10f.mean(axis=1), ls = '-.', label='high sed')
ax4.plot(hs_75r_10f_q1,c='g', ls = '-.')
ax4.plot(hs_75r_10f_q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(hs_75r_10f_q1)),hs_75r_10f_q1,hs_75r_10f_q3, alpha=0.2)
plt.savefig("75rms_all_sed_quantile_ice_vol_no_equal_mem.png", dpi=800)



### 100 rms plot ###

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - 100 rms, all fdim')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# 0.25 fdim
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ls_100r_25f.mean(axis=1), ls = '-', label='low sed')
ax1.plot(ls_100r_25f_q1,c='b',ls = '-')
ax1.plot(ls_100r_25f_q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(ls_100r_25f_q1)),ls_100r_25f_q1,ls_100r_25f_q3, alpha=0.2)
ax1.plot(ms_100r_25f.mean(axis=1), ls = '-', label='med sed')
ax1.plot(ms_100r_25f_q1,c='orange',ls = '--')
ax1.plot(ms_100r_25f_q3,c='orange',ls = '--')
ax1.fill_between(np.arange(len(ms_100r_25f_q1)),ms_100r_25f_q1,ms_100r_25f_q3, alpha=0.2)
ax1.plot(hs_100r_25f.mean(axis=1), ls = '-.', label='high sed')
ax1.plot(hs_100r_25f_q1,c='g', ls = '-.')
ax1.plot(hs_100r_25f_q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(hs_100r_25f_q1)),hs_100r_25f_q1,hs_100r_25f_q3, alpha=0.2)
# 0.50 fdim
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ls_100r_50f.mean(axis=1), ls = '-', label='low sed')
ax2.plot(ls_100r_50f_q1,c='b',ls = '-')
ax2.plot(ls_100r_50f_q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(ls_100r_50f_q1)),ls_100r_50f_q1,ls_100r_50f_q3, alpha=0.2)
ax2.plot(ms_100r_50f.mean(axis=1), ls = '-', label='med sed')
ax2.plot(ms_100r_50f_q1,c='orange',ls = '--')
ax2.plot(ms_100r_50f_q3,c='orange',ls = '--')
ax2.fill_between(np.arange(len(ms_100r_50f_q1)),ms_100r_50f_q1,ms_100r_50f_q3, alpha=0.2)
ax2.plot(hs_100r_50f.mean(axis=1), ls = '-.', label='high sed')
ax2.plot(hs_100r_50f_q1,c='g', ls = '-.')
ax2.plot(hs_100r_50f_q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(hs_100r_50f_q1)),hs_100r_50f_q1,hs_100r_50f_q3, alpha=0.2)
# 0.75 fdim
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ls_100r_75f.mean(axis=1), ls = '-', label='low sed')
ax3.plot(ls_100r_75f_q1,c='b',ls = '-')
ax3.plot(ls_100r_75f_q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(ls_100r_75f_q1)),ls_100r_75f_q1,ls_100r_75f_q3, alpha=0.2)
ax3.plot(ms_100r_75f.mean(axis=1), ls = '-', label='med sed')
ax3.plot(ms_100r_75f_q1,c='orange',ls = '--')
ax3.plot(ms_100r_75f_q3,c='orange',ls = '--')
ax3.fill_between(np.arange(len(ms_100r_75f_q1)),ms_100r_75f_q1,ms_100r_75f_q3, alpha=0.2)
ax3.plot(hs_100r_75f.mean(axis=1), ls = '-.', label='high sed')
ax3.plot(hs_100r_75f_q1,c='g', ls = '-.')
ax3.plot(hs_100r_75f_q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(hs_100r_75f_q1)),hs_100r_75f_q1,hs_100r_75f_q3, alpha=0.2)
# 1.0 fdim
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ls_100r_10f.mean(axis=1), ls = '-', label='low sed')
ax4.plot(ls_100r_10f_q1,c='b',ls = '-')
ax4.plot(ls_100r_10f_q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(ls_100r_10f_q1)),ls_100r_10f_q1,ls_100r_10f_q3, alpha=0.2)
ax4.plot(ms_100r_10f.mean(axis=1), ls = '-', label='med sed')
ax4.plot(ms_100r_10f_q1,c='orange',ls = '--')
ax4.plot(ms_100r_10f_q3,c='orange',ls = '--')
ax4.fill_between(np.arange(len(ms_100r_10f_q1)),ms_100r_10f_q1,ms_100r_10f_q3, alpha=0.2)
ax4.plot(hs_100r_10f.mean(axis=1), ls = '-.', label='high sed')
ax4.plot(hs_100r_10f_q1,c='g', ls = '-.')
ax4.plot(hs_100r_10f_q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(hs_100r_10f_q1)),hs_100r_10f_q1,hs_100r_10f_q3, alpha=0.2)
plt.savefig("100rms_all_sed_quantile_ice_vol_no_equal_mem.png", dpi=800)





