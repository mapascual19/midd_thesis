#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:12:21 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


###################################
### load data and collect stats ###
###################################

######## 25 rms ########

### 25 rms 0.25 fdim ###
# low
ls_25r_25f = pd.read_csv('low_sed_25r_25f.csv', index_col=0)
ls_25r_25f = ls_25r_25f.pct_change()
ls_25r_25f = np.abs(ls_25r_25f)
# med
ms_25r_25f = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)
ms_25r_25f = ms_25r_25f.pct_change()
ms_25r_25f = np.abs(ms_25r_25f)
# high
hs_25r_25f = pd.read_csv('high_sed_25r_25f.csv', index_col=0)
hs_25r_25f = hs_25r_25f.pct_change()
hs_25r_25f = np.abs(hs_25r_25f)

### 25 rms 0.50 fdim ###
# low
ls_25r_50f = pd.read_csv('low_sed_25r_50f.csv', index_col=0)
ls_25r_50f = ls_25r_50f.pct_change()
ls_25r_50f = np.abs(ls_25r_50f)
# med
ms_25r_50f = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0)
ms_25r_50f = ms_25r_50f.pct_change()
ms_25r_50f = np.abs(ms_25r_50f)
# high
hs_25r_50f = pd.read_csv('high_sed_25r_50f.csv', index_col=0)
hs_25r_50f = hs_25r_50f.pct_change()
hs_25r_50f = np.abs(hs_25r_50f)

### 25 rms 0.75 fdim ###
# low
ls_25r_75f = pd.read_csv('low_sed_25r_75f.csv', index_col=0)
ls_25r_75f = ls_25r_50f.pct_change()
ls_25r_75f = np.abs(ls_25r_75f)
# med
ms_25r_75f = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0)
ms_25r_75f = ms_25r_75f.pct_change()
ms_25r_75f = np.abs(ms_25r_75f)
# high
hs_25r_75f = pd.read_csv('high_sed_25r_75f.csv', index_col=0)
hs_25r_75f = hs_25r_75f.pct_change()
hs_25r_75f = np.abs(hs_25r_75f)

### 25 rms 1.0 fdim ###
# low
ls_25r_10f = pd.read_csv('low_sed_25r_10f.csv', index_col=0)
ls_25r_10f = ls_25r_10f.pct_change()
ls_25r_10f = np.abs(ls_25r_10f)
# med
ms_25r_10f = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)
ms_25r_10f = ms_25r_10f.pct_change()
ms_25r_10f = np.abs(ms_25r_10f)
# high
hs_25r_10f = pd.read_csv('high_sed_25r_10f.csv', index_col=0)
hs_25r_10f = hs_25r_10f.pct_change()
hs_25r_10f = np.abs(hs_25r_10f)



######## 50 rms ########

### 50 rms 0.25 fdim ###
# low
ls_50r_25f = pd.read_csv('low_sed_50r_25f.csv', index_col=0)
ls_50r_25f = ls_50r_25f.pct_change()
ls_50r_25f = np.abs(ls_50r_25f)
# med
ms_50r_25f = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0)
ms_50r_25f = ms_50r_25f.pct_change()
ms_50r_25f = np.abs(ms_50r_25f)
# high
hs_50r_25f = pd.read_csv('high_sed_50r_25f.csv', index_col=0)
hs_50r_25f = hs_50r_25f.pct_change()
hs_50r_25f = np.abs(hs_50r_25f)

### 50 rms 0.50 fdim ###
# low
ls_50r_50f = pd.read_csv('low_sed_50r_50f.csv', index_col=0)
ls_50r_50f = ls_50r_50f.pct_change()
ls_50r_50f = np.abs(ls_50r_50f)
# med
ms_50r_50f = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0)
ms_50r_50f = ms_50r_50f.pct_change()
ms_50r_50f = np.abs(ms_50r_50f)
# high
hs_50r_50f = pd.read_csv('high_sed_50r_50f.csv', index_col=0)
hs_50r_50f = hs_50r_50f.pct_change()
hs_50r_50f = np.abs(hs_50r_50f)

### 50 rms 0.75 fdim ###
# low
ls_50r_75f = pd.read_csv('low_sed_50r_75f.csv', index_col=0)
ls_50r_75f = ls_50r_50f.pct_change()
ls_50r_75f = np.abs(ls_50r_75f)
# med
ms_50r_75f = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0)
ms_50r_75f = ms_50r_75f.pct_change()
ms_50r_75f = np.abs(ms_50r_75f)
# high
hs_50r_75f = pd.read_csv('high_sed_50r_75f.csv', index_col=0)
hs_50r_75f = hs_50r_75f.pct_change()
hs_50r_75f = np.abs(hs_50r_75f)

### 50 rms 1.0 fdim ###
# low
ls_50r_10f = pd.read_csv('low_sed_50r_10f.csv', index_col=0)
ls_50r_10f = ls_50r_10f.pct_change()
ls_50r_10f = np.abs(ls_50r_10f)
# med
ms_50r_10f = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0)
ms_50r_10f = ms_50r_10f.pct_change()
ms_50r_10f = np.abs(ms_50r_10f)
# high
hs_50r_10f = pd.read_csv('high_sed_50r_10f.csv', index_col=0)
hs_50r_10f = hs_50r_10f.pct_change()
hs_50r_10f = np.abs(hs_50r_10f)



######## 75 rms ########

### 75 rms 0.25 fdim ###
# low
ls_75r_25f = pd.read_csv('low_sed_75r_25f.csv', index_col=0)
ls_75r_25f = ls_75r_25f.pct_change()
ls_75r_25f = np.abs(ls_75r_25f)
# med
ms_75r_25f = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0)
ms_75r_25f = ms_75r_25f.pct_change()
ms_75r_25f = np.abs(ms_75r_25f)
# high
hs_75r_25f = pd.read_csv('high_sed_75r_25f.csv', index_col=0)
hs_75r_25f = hs_75r_25f.pct_change()
hs_75r_25f = np.abs(hs_75r_25f)

### 75 rms 0.50 fdim ###
# low
ls_75r_50f = pd.read_csv('low_sed_75r_50f.csv', index_col=0)
ls_75r_50f = ls_75r_50f.pct_change()
ls_75r_50f = np.abs(ls_75r_50f)
# med
ms_75r_50f = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0)
ms_75r_50f = ms_75r_50f.pct_change()
ms_75r_50f = np.abs(ms_75r_50f)
# high
hs_75r_50f = pd.read_csv('high_sed_75r_50f.csv', index_col=0)
hs_75r_50f = hs_75r_50f.pct_change()
hs_75r_50f = np.abs(hs_75r_50f)

### 75 rms 0.75 fdim ###
# low
ls_75r_75f = pd.read_csv('low_sed_75r_75f.csv', index_col=0)
ls_75r_75f = ls_75r_50f.pct_change()
ls_75r_75f = np.abs(ls_75r_75f)
# med
ms_75r_75f = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0)
ms_75r_75f = ms_75r_75f.pct_change()
ms_75r_75f = np.abs(ms_75r_75f)
# high
hs_75r_75f = pd.read_csv('high_sed_75r_75f.csv', index_col=0)
hs_75r_75f = hs_75r_75f.pct_change()
hs_75r_75f = np.abs(hs_75r_75f)

### 75 rms 1.0 fdim ###
# low
ls_75r_10f = pd.read_csv('low_sed_75r_10f.csv', index_col=0)
ls_75r_10f = ls_75r_10f.pct_change()
ls_75r_10f = np.abs(ls_75r_10f)
# med
ms_75r_10f = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0)
ms_75r_10f = ms_75r_10f.pct_change()
ms_75r_10f = np.abs(ms_75r_10f)
# high
hs_75r_10f = pd.read_csv('high_sed_75r_10f.csv', index_col=0)
hs_75r_10f = hs_75r_10f.pct_change()
hs_75r_10f = np.abs(hs_75r_10f)



######## 100 rms ########

### 100 rms 0.25 fdim ###
# low
ls_100r_25f = pd.read_csv('low_sed_100r_25f.csv', index_col=0)
ls_100r_25f = ls_100r_25f.pct_change()
ls_100r_25f = np.abs(ls_100r_25f)
# med
ms_100r_25f = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0)
ms_100r_25f = ms_100r_25f.pct_change()
ms_100r_25f = np.abs(ms_100r_25f)
# high
hs_100r_25f = pd.read_csv('high_sed_100r_25f.csv', index_col=0)
hs_100r_25f = hs_100r_25f.pct_change()
hs_100r_25f = np.abs(hs_100r_25f)

### 100 rms 0.50 fdim ###
# low
ls_100r_50f = pd.read_csv('low_sed_100r_50f.csv', index_col=0)
ls_100r_50f = ls_100r_50f.pct_change()
ls_100r_50f = np.abs(ls_100r_50f)
# med
ms_100r_50f = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0)
ms_100r_50f = ms_100r_50f.pct_change()
ms_100r_50f = np.abs(ms_100r_50f)
# high
hs_100r_50f = pd.read_csv('high_sed_100r_50f.csv', index_col=0)
hs_100r_50f = hs_100r_50f.pct_change()
hs_100r_50f = np.abs(hs_100r_50f)

### 100 rms 0.75 fdim ###
# low
ls_100r_75f = pd.read_csv('low_sed_100r_75f.csv', index_col=0)
ls_100r_75f = ls_100r_50f.pct_change()
ls_100r_75f = np.abs(ls_100r_75f)
# med
ms_100r_75f = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0)
ms_100r_75f = ms_100r_75f.pct_change()
ms_100r_75f = np.abs(ms_100r_75f)
# high
hs_100r_75f = pd.read_csv('high_sed_100r_75f.csv', index_col=0)
hs_100r_75f = hs_100r_75f.pct_change()
hs_100r_75f = np.abs(hs_100r_75f)

### 100 rms 1.0 fdim ###
# low
ls_100r_10f = pd.read_csv('low_sed_100r_10f.csv', index_col=0)
ls_100r_10f = ls_100r_10f.pct_change()
ls_100r_10f = np.abs(ls_100r_10f)
# med
ms_100r_10f = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0)
ms_100r_10f = ms_100r_10f.pct_change()
ms_100r_10f = np.abs(ms_100r_10f)
# high
hs_100r_10f = pd.read_csv('high_sed_100r_10f.csv', index_col=0)
hs_100r_10f = hs_100r_10f.pct_change()
hs_100r_10f = np.abs(hs_100r_10f)

###################################
####### plot across rms ###########
###################################

### 25 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 25 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_25r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_25r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_25r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_25r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_25r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_25r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_25r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_25r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_25r_25f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_25r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_25r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_25r_10f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_25rms.png", dpi=800)


### 50 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 50 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_50r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_50r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_50r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_50r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_50r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_50r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_50r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_50r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_50r_25f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_50r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_50r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_50r_10f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_50rms.png", dpi=800)


### 75 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 75 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_75r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_75r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_75r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_75r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_75r_25f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_75r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_10f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_75rms.png", dpi=800)


### 100 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 100 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_100r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_100r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_100r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_100r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_100r_25f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_100r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_10f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_100rms.png", dpi=800)


###################################
####### plot across fdim ##########
###################################

### 0.25 fdim plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 0.25 fdim, all rms (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_25r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_50r_25f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_25f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_25f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_25r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_50r_25f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_25f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_25f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_25r_25f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_50r_25f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_25f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_25f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_25fdim.png", dpi=800)


### 0.50 fdim plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 0.50 fdim, all rms (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_25r_50f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_50r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_25r_50f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_50r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_25r_50f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_50r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_50f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_50f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_50fdim.png", dpi=800)


### 0.75 fdim plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 0.75 fdim, all rms (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.25])
ax.plot(ls_25r_75f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_50r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_25r_75f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_50r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_25r_75f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_50r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_75f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_75f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_75fdim.png", dpi=800)


### 1.0 fdim plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 1.0 fdim, all rms (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.set(ylim=[0,0.05])
ax.plot(ls_25r_10f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(ls_50r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_75r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ls_100r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ms_25r_10f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ms_50r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_75r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(ms_100r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(hs_25r_10f.mean(axis=1), c = 'g', ls='--', label = "high sed")
ax.plot(hs_50r_10f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_75r_10f.mean(axis=1), c = 'g', ls='--')
ax.plot(hs_100r_10f.mean(axis=1), c = 'g', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_10fdim.png", dpi=800)
