#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:58:07 2022

@author: mikaylapascual
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import rcParams
import numpy as np
import pandas as pd
import seaborn as sns

###################################
########### load data #############
###################################

### control ###
# SED
ctrl_SED = pd.read_csv('ice_vol_1000yr_control_case.csv', index_col=0)
# REU
ctrl_REU = pd.read_csv('control_case_total_vs.csv', header=None)
ctrl_REU = ctrl_REU.transpose()
ctrl_REU = ctrl_REU.multiply(1.0E-9)

########### FROM SED #############

### 25 rms ###
ice_vol_25rms_25fdim = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0)
ice_vol_25rms_50fdim = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0)
ice_vol_25rms_75fdim = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0)
ice_vol_25rms_10fdim = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0)


### 50 rms ###
ice_vol_50rms_25fdim = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0)
ice_vol_50rms_50fdim = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0)
ice_vol_50rms_75fdim = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0)
ice_vol_50rms_10fdim = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0)

### 75 rms ###
ice_vol_75rms_25fdim = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0)
ice_vol_75rms_50fdim = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0)
ice_vol_75rms_75fdim = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0)
ice_vol_75rms_10fdim = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0)

### 100 rms ###
ice_vol_100rms_25fdim = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0)
ice_vol_100rms_50fdim = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0)
ice_vol_100rms_75fdim = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0)
ice_vol_100rms_10fdim = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0)


############ FROM REU #############

# structure:
# 1. load data
# 2. transpose 
# 3. convert km3 to m3

REU_vol_25rms_25fdim = pd.read_csv('25rms_25fdim_total_vs.csv', header=None)
REU_vol_25rms_25fdim = REU_vol_25rms_25fdim.transpose()
REU_vol_25rms_25fdim = REU_vol_25rms_25fdim.multiply(1.0E-9, axis=1)
REU_vol_25rms_50fdim = pd.read_csv('25rms_50fdim_total_vs.csv', header=None)
REU_vol_25rms_50fdim = REU_vol_25rms_50fdim.transpose()
REU_vol_25rms_50fdim = REU_vol_25rms_50fdim.multiply(1.0E-9, axis=1)
REU_vol_25rms_75fdim = pd.read_csv('25rms_75fdim_total_vs.csv', header=None)
REU_vol_25rms_75fdim = REU_vol_25rms_75fdim.transpose()
REU_vol_25rms_75fdim = REU_vol_25rms_75fdim.multiply(1.0E-9, axis=1)
REU_vol_25rms_10fdim = pd.read_csv('25rms_10fdim_total_vs.csv', header=None)
REU_vol_25rms_10fdim = REU_vol_25rms_10fdim.transpose()
REU_vol_25rms_10fdim = REU_vol_25rms_10fdim.multiply(1.0E-9, axis=1)


### 50 rms ###
REU_vol_50rms_25fdim = pd.read_csv('50rms_25fdim_total_vs.csv', header=None)
REU_vol_50rms_25fdim = REU_vol_50rms_25fdim.transpose()
REU_vol_50rms_25fdim = REU_vol_50rms_25fdim.multiply(1.0E-9, axis=1)
REU_vol_50rms_50fdim = pd.read_csv('50rms_50fdim_total_vs.csv', header=None)
REU_vol_50rms_50fdim = REU_vol_50rms_50fdim.transpose()
REU_vol_50rms_50fdim = REU_vol_50rms_50fdim.multiply(1.0E-9, axis=1)
REU_vol_50rms_75fdim = pd.read_csv('50rms_75fdim_total_vs.csv', header=None)
REU_vol_50rms_75fdim = REU_vol_50rms_75fdim.transpose()
REU_vol_50rms_75fdim = REU_vol_50rms_75fdim.multiply(1.0E-9, axis=1)
REU_vol_50rms_10fdim = pd.read_csv('50rms_10fdim_total_vs.csv', header=None)
REU_vol_50rms_10fdim = REU_vol_50rms_10fdim.transpose()
REU_vol_50rms_10fdim = REU_vol_50rms_10fdim.multiply(1.0E-9, axis=1)

### 75 rms ###
REU_vol_75rms_25fdim = pd.read_csv('75rms_25fdim_total_vs.csv', header=None)
REU_vol_75rms_25fdim = REU_vol_75rms_25fdim.transpose()
REU_vol_75rms_25fdim = REU_vol_75rms_25fdim.multiply(1.0E-9, axis=1)
REU_vol_75rms_50fdim = pd.read_csv('75rms_50fdim_total_vs.csv', header=None)
REU_vol_75rms_50fdim = REU_vol_75rms_50fdim.transpose()
REU_vol_75rms_50fdim = REU_vol_75rms_50fdim.multiply(1.0E-9, axis=1)
REU_vol_75rms_75fdim = pd.read_csv('75rms_75fdim_total_vs.csv', header=None)
REU_vol_75rms_75fdim = REU_vol_75rms_75fdim.transpose()
REU_vol_75rms_75fdim = REU_vol_75rms_75fdim.multiply(1.0E-9, axis=1)
REU_vol_75rms_10fdim = pd.read_csv('75rms_10fdim_total_vs.csv', header=None)
REU_vol_75rms_10fdim = REU_vol_75rms_10fdim.transpose()
REU_vol_75rms_10fdim = REU_vol_75rms_10fdim.multiply(1.0E-9, axis=1)

### 100 rms ###
REU_vol_100rms_25fdim = pd.read_csv('100rms_25fdim_total_vs.csv', header=None)
REU_vol_100rms_25fdim = REU_vol_100rms_25fdim.transpose()
REU_vol_100rms_25fdim = REU_vol_100rms_25fdim.multiply(1.0E-9, axis=1)
REU_vol_100rms_50fdim = pd.read_csv('100rms_50fdim_total_vs.csv', header=None)
REU_vol_100rms_50fdim = REU_vol_100rms_50fdim.transpose()
REU_vol_100rms_50fdim = REU_vol_100rms_50fdim.multiply(1.0E-9, axis=1)
REU_vol_100rms_75fdim = pd.read_csv('100rms_75fdim_total_vs.csv', header=None)
REU_vol_100rms_75fdim = REU_vol_100rms_75fdim.transpose()
REU_vol_100rms_75fdim = REU_vol_100rms_75fdim.multiply(1.0E-9, axis=1)
REU_vol_100rms_10fdim = pd.read_csv('100rms_10fdim_total_vs.csv', header=None)
REU_vol_100rms_10fdim = REU_vol_100rms_10fdim.transpose()
REU_vol_100rms_10fdim = REU_vol_100rms_10fdim.multiply(1.0E-9, axis=1)


###################################
###### ice volume over time #######
###################################

# ### 25 rms SED ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time - 25 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(ice_vol_25rms_25fdim, c = 'lightskyblue')
# ax1.plot(ctrl_SED,c='k')
# ax2.plot(ice_vol_25rms_50fdim, c = 'lightskyblue')
# ax2.plot(ctrl_SED,c='k')
# ax3.plot(ice_vol_25rms_75fdim, c = 'lightskyblue')
# ax3.plot(ctrl_SED,c='k')
# ax4.plot(ice_vol_25rms_10fdim, c = 'lightskyblue')
# ax4.plot(ctrl_SED,c='k')
# plt.savefig("25rms_ens_ice_vol.png", dpi=800)

# ### 25 rms REU ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time (no sed.) - 25 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.10,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(REU_vol_25rms_25fdim, c = 'slategrey')
# ax1.plot(ctrl_REU,c='k')
# ax2.plot(REU_vol_25rms_50fdim, c = 'slategrey')
# ax2.plot(ctrl_REU,c='k')
# ax3.plot(REU_vol_25rms_75fdim, c = 'slategrey')
# ax3.plot(ctrl_REU,c='k')
# ax4.plot(REU_vol_25rms_10fdim, c = 'slategrey')
# ax4.plot(ctrl_REU,c='k')
# plt.savefig("25rms_ens_ice_vol_REU.png", dpi=800)



# ### 50 rms ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time - 50 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(ice_vol_50rms_25fdim, c = 'lightskyblue')
# ax1.plot(ctrl_SED,c='k')
# ax2.plot(ice_vol_50rms_50fdim, c = 'lightskyblue')
# ax2.plot(ctrl_SED,c='k')
# ax3.plot(ice_vol_50rms_75fdim, c = 'lightskyblue')
# ax3.plot(ctrl_SED,c='k')
# ax4.plot(ice_vol_50rms_10fdim, c = 'lightskyblue')
# ax4.plot(ctrl_SED,c='k')
# plt.savefig("50rms_ens_ice_vol.png", dpi=800)

# ### 50 rms REU ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time (no sed.) - 50 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.10,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(REU_vol_50rms_25fdim, c = 'slategrey')
# ax1.plot(ctrl_REU,c='k')
# ax2.plot(REU_vol_50rms_50fdim, c = 'slategrey')
# ax2.plot(ctrl_REU,c='k')
# ax3.plot(REU_vol_50rms_75fdim, c = 'slategrey')
# ax3.plot(ctrl_REU,c='k')
# ax4.plot(REU_vol_50rms_10fdim, c = 'slategrey')
# ax4.plot(ctrl_REU,c='k')
# plt.savefig("50rms_ens_ice_vol_REU.png", dpi=800)


# ### 75 rms ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time - 75 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(ice_vol_75rms_25fdim, c = 'lightskyblue')
# ax1.plot(ctrl_SED,c='k')
# ax2.plot(ice_vol_75rms_50fdim, c = 'lightskyblue')
# ax2.plot(ctrl_SED,c='k')
# ax3.plot(ice_vol_75rms_75fdim, c = 'lightskyblue')
# ax3.plot(ctrl_SED,c='k')
# ax4.plot(ice_vol_75rms_10fdim, c = 'lightskyblue')
# ax4.plot(ctrl_SED,c='k')
# plt.savefig("75rms_ens_ice_vol.png", dpi=800)

# ### 75 rms REU ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time (no sed.) - 75 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.10,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(REU_vol_75rms_25fdim, c = 'slategrey')
# ax1.plot(ctrl_REU,c='k')
# ax2.plot(REU_vol_75rms_50fdim, c = 'slategrey')
# ax2.plot(ctrl_REU,c='k')
# ax3.plot(REU_vol_75rms_75fdim, c = 'slategrey')
# ax3.plot(ctrl_REU,c='k')
# ax4.plot(REU_vol_75rms_10fdim, c = 'slategrey')
# ax4.plot(ctrl_REU,c='k')
# plt.savefig("75rms_ens_ice_vol_REU.png", dpi=800)


# ### 100 rms ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time - 100 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(ice_vol_100rms_25fdim, c = 'lightskyblue')
# ax1.plot(ctrl_SED,c='k')
# ax2.plot(ice_vol_100rms_50fdim, c = 'lightskyblue')
# ax2.plot(ctrl_SED,c='k')
# ax3.plot(ice_vol_100rms_75fdim, c = 'lightskyblue')
# ax3.plot(ctrl_SED,c='k')
# ax4.plot(ice_vol_100rms_10fdim, c = 'lightskyblue')
# ax4.plot(ctrl_SED,c='k')
# plt.savefig("100rms_ens_ice_vol.png", dpi=800)

# ### 100 rms REU ###
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
# fig.suptitle('Ice Volume over Time (no sed.) - 100 rms, all fdim')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
# fdims = (0.25,0.50,0.75,1.0)
# axs = (ax1,ax2,ax3,ax4)
# for (ax,f) in zip (axs,fdims):
#     ax.text(0.1,0.10,'fractal dimension {}'.format(f),transform=ax.transAxes)
# ax1.plot(REU_vol_100rms_25fdim, c = 'slategrey')
# ax1.plot(ctrl_REU,c='k')
# ax2.plot(REU_vol_100rms_50fdim, c = 'slategrey')
# ax2.plot(ctrl_REU,c='k')
# ax3.plot(REU_vol_100rms_75fdim, c = 'slategrey')
# ax3.plot(ctrl_REU,c='k')
# ax4.plot(REU_vol_100rms_10fdim, c = 'slategrey')
# ax4.plot(ctrl_REU,c='k')
# plt.savefig("100rms_ens_ice_vol_REU.png", dpi=800)


###################################
### kde plots at diff time steps ##
###################################

### 25 rms ###

### 25 rms, 0.25 fdim ###
# load data
ice_vol_25rms_25fdim_100 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, nrows=100)
ice_vol_25rms_25fdim_200 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_25rms_25fdim_300 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_25rms_25fdim_400 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_25rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_25rms_25fdim_600 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_25rms_25fdim_700 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_25rms_25fdim_800 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_25rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_25rms_25fdim_1000 = pd.read_csv('ice_vol_1000yr_25rms_25fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_25r_25f_100y = np.mean(ice_vol_25rms_25fdim_100)
tivm_25r_25f_200y = np.mean(ice_vol_25rms_25fdim_200)
tivm_25r_25f_300y = np.mean(ice_vol_25rms_25fdim_300)
tivm_25r_25f_400y = np.mean(ice_vol_25rms_25fdim_400)
tivm_25r_25f_500y = np.mean(ice_vol_25rms_25fdim_500)
tivm_25r_25f_600y = np.mean(ice_vol_25rms_25fdim_600)
tivm_25r_25f_700y = np.mean(ice_vol_25rms_25fdim_700)
tivm_25r_25f_800y = np.mean(ice_vol_25rms_25fdim_800)
tivm_25r_25f_900y = np.mean(ice_vol_25rms_25fdim_900)
tivm_25r_25f_1000y = np.mean(ice_vol_25rms_25fdim_1000)
# build df 
tivm_tot_time_steps_25r_25f = np.array([tivm_25r_25f_100y, tivm_25r_25f_200y, tivm_25r_25f_300y, tivm_25r_25f_400y, 
                                        tivm_25r_25f_500y,tivm_25r_25f_600y, tivm_25r_25f_700y, tivm_25r_25f_800y,
                                        tivm_25r_25f_900y, tivm_25r_25f_1000y])
tivm_tot_time_steps_25r_25f = tivm_tot_time_steps_25r_25f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_25r_25f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0, 2.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("25rms_25fdim_kde_all_time_steps.png", dpi=800)



### 25 rms, 0.50 fdim ###
# load data
ice_vol_25rms_50fdim_100 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, nrows=100)
ice_vol_25rms_50fdim_200 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_25rms_50fdim_300 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_25rms_50fdim_400 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_25rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_25rms_50fdim_600 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_25rms_50fdim_700 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_25rms_50fdim_800 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_25rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_25rms_50fdim_1000 = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_25r_50f_100y = np.mean(ice_vol_25rms_50fdim_100)
tivm_25r_50f_200y = np.mean(ice_vol_25rms_50fdim_200)
tivm_25r_50f_300y = np.mean(ice_vol_25rms_50fdim_300)
tivm_25r_50f_400y = np.mean(ice_vol_25rms_50fdim_400)
tivm_25r_50f_500y = np.mean(ice_vol_25rms_50fdim_500)
tivm_25r_50f_600y = np.mean(ice_vol_25rms_50fdim_600)
tivm_25r_50f_700y = np.mean(ice_vol_25rms_50fdim_700)
tivm_25r_50f_800y = np.mean(ice_vol_25rms_50fdim_800)
tivm_25r_50f_900y = np.mean(ice_vol_25rms_50fdim_900)
tivm_25r_50f_1000y = np.mean(ice_vol_25rms_50fdim_1000)
# build df 
tivm_tot_time_steps_25r_50f = np.array([tivm_25r_50f_100y, tivm_25r_50f_200y, tivm_25r_50f_300y, tivm_25r_50f_400y, 
                                        tivm_25r_50f_500y,tivm_25r_50f_600y, tivm_25r_50f_700y, tivm_25r_50f_800y,
                                        tivm_25r_50f_900y, tivm_25r_50f_1000y])
tivm_tot_time_steps_25r_50f = tivm_tot_time_steps_25r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_25r_50f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 25 rms, 0.50 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("25rms_50fdim_kde_all_time_steps.png", dpi=800)



### 25 rms, 0.75 fdim ###
# load data
ice_vol_25rms_75fdim_100 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, nrows=100)
ice_vol_25rms_75fdim_200 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_25rms_75fdim_300 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_25rms_75fdim_400 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_25rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_25rms_75fdim_600 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_25rms_75fdim_700 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_25rms_75fdim_800 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_25rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_25rms_75fdim_1000 = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_25r_75f_100y = np.mean(ice_vol_25rms_75fdim_100)
tivm_25r_75f_200y = np.mean(ice_vol_25rms_75fdim_200)
tivm_25r_75f_300y = np.mean(ice_vol_25rms_75fdim_300)
tivm_25r_75f_400y = np.mean(ice_vol_25rms_75fdim_400)
tivm_25r_75f_500y = np.mean(ice_vol_25rms_75fdim_500)
tivm_25r_75f_600y = np.mean(ice_vol_25rms_75fdim_600)
tivm_25r_75f_700y = np.mean(ice_vol_25rms_75fdim_700)
tivm_25r_75f_800y = np.mean(ice_vol_25rms_75fdim_800)
tivm_25r_75f_900y = np.mean(ice_vol_25rms_75fdim_900)
tivm_25r_75f_1000y = np.mean(ice_vol_25rms_75fdim_1000)
# build df 
tivm_tot_time_steps_25r_75f = np.array([tivm_25r_75f_100y, tivm_25r_75f_200y, tivm_25r_75f_300y, tivm_25r_75f_400y, 
                                        tivm_25r_75f_500y,tivm_25r_75f_600y, tivm_25r_75f_700y, tivm_25r_75f_800y,
                                        tivm_25r_75f_900y, tivm_25r_75f_1000y])
tivm_tot_time_steps_25r_75f = tivm_tot_time_steps_25r_75f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_25r_75f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 25 rms, 0.75 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("25rms_75fdim_kde_all_time_steps.png", dpi=800)



### 25 rms, 1.0 fdim ###
# load data
ice_vol_25rms_10fdim_100 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, nrows=100)
ice_vol_25rms_10fdim_200 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_25rms_10fdim_300 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_25rms_10fdim_400 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_25rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_25rms_10fdim_600 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_25rms_10fdim_700 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_25rms_10fdim_800 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_25rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_25rms_10fdim_1000 = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_25r_10f_100y = np.mean(ice_vol_25rms_10fdim_100)
tivm_25r_10f_200y = np.mean(ice_vol_25rms_10fdim_200)
tivm_25r_10f_300y = np.mean(ice_vol_25rms_10fdim_300)
tivm_25r_10f_400y = np.mean(ice_vol_25rms_10fdim_400)
tivm_25r_10f_500y = np.mean(ice_vol_25rms_10fdim_500)
tivm_25r_10f_600y = np.mean(ice_vol_25rms_10fdim_600)
tivm_25r_10f_700y = np.mean(ice_vol_25rms_10fdim_700)
tivm_25r_10f_800y = np.mean(ice_vol_25rms_10fdim_800)
tivm_25r_10f_900y = np.mean(ice_vol_25rms_10fdim_900)
tivm_25r_10f_1000y = np.mean(ice_vol_25rms_10fdim_1000)
# build df 
tivm_tot_time_steps_25r_10f = np.array([tivm_25r_10f_100y, tivm_25r_10f_200y, tivm_25r_10f_300y, tivm_25r_10f_400y, 
                                        tivm_25r_10f_500y,tivm_25r_10f_600y, tivm_25r_10f_700y, tivm_25r_10f_800y,
                                        tivm_25r_10f_900y, tivm_25r_10f_1000y])
tivm_tot_time_steps_25r_10f = tivm_tot_time_steps_25r_10f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_25r_10f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 25 rms, 1.0 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("25rms_10fdim_kde_all_time_steps.png", dpi=800)




### 50 rms ###

### 50 rms, 0.25 fdim ###
# load data
ice_vol_50rms_25fdim_100 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, nrows=100)
ice_vol_50rms_25fdim_200 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_50rms_25fdim_300 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_50rms_25fdim_400 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_50rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_50rms_25fdim_600 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_50rms_25fdim_700 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_50rms_25fdim_800 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_50rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_50rms_25fdim_1000 = pd.read_csv('ice_vol_1000yr_50rms_25fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_50r_25f_100y = np.mean(ice_vol_50rms_25fdim_100)
tivm_50r_25f_200y = np.mean(ice_vol_50rms_25fdim_200)
tivm_50r_25f_300y = np.mean(ice_vol_50rms_25fdim_300)
tivm_50r_25f_400y = np.mean(ice_vol_50rms_25fdim_400)
tivm_50r_25f_500y = np.mean(ice_vol_50rms_25fdim_500)
tivm_50r_25f_600y = np.mean(ice_vol_50rms_25fdim_600)
tivm_50r_25f_700y = np.mean(ice_vol_50rms_25fdim_700)
tivm_50r_25f_800y = np.mean(ice_vol_50rms_25fdim_800)
tivm_50r_25f_900y = np.mean(ice_vol_50rms_25fdim_900)
tivm_50r_25f_1000y = np.mean(ice_vol_50rms_25fdim_1000)
# build df 
tivm_tot_time_steps_50r_25f = np.array([tivm_50r_25f_100y, tivm_50r_25f_200y, tivm_50r_25f_300y, tivm_50r_25f_400y, 
                                        tivm_50r_25f_500y,tivm_50r_25f_600y, tivm_50r_25f_700y, tivm_50r_25f_800y,
                                        tivm_50r_25f_900y, tivm_50r_25f_1000y])
tivm_tot_time_steps_50r_25f = tivm_tot_time_steps_50r_25f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_25f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 50 rms, 0.25 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("50rms_25fdim_kde_all_time_steps.png", dpi=800)



### 50 rms, 0.50 fdim ###
# load data
ice_vol_50rms_50fdim_100 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, nrows=100)
ice_vol_50rms_50fdim_200 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_50rms_50fdim_300 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_50rms_50fdim_400 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_50rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_50rms_50fdim_600 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_50rms_50fdim_700 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_50rms_50fdim_800 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_50rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_50rms_50fdim_1000 = pd.read_csv('ice_vol_1000yr_50rms_50fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_50r_50f_100y = np.mean(ice_vol_50rms_50fdim_100)
tivm_50r_50f_200y = np.mean(ice_vol_50rms_50fdim_200)
tivm_50r_50f_300y = np.mean(ice_vol_50rms_50fdim_300)
tivm_50r_50f_400y = np.mean(ice_vol_50rms_50fdim_400)
tivm_50r_50f_500y = np.mean(ice_vol_50rms_50fdim_500)
tivm_50r_50f_600y = np.mean(ice_vol_50rms_50fdim_600)
tivm_50r_50f_700y = np.mean(ice_vol_50rms_50fdim_700)
tivm_50r_50f_800y = np.mean(ice_vol_50rms_50fdim_800)
tivm_50r_50f_900y = np.mean(ice_vol_50rms_50fdim_900)
tivm_50r_50f_1000y = np.mean(ice_vol_50rms_50fdim_1000)
# build df 
tivm_tot_time_steps_50r_50f = np.array([tivm_50r_50f_100y, tivm_50r_50f_200y, tivm_50r_50f_300y, tivm_50r_50f_400y, 
                                        tivm_50r_50f_500y,tivm_50r_50f_600y, tivm_50r_50f_700y, tivm_50r_50f_800y,
                                        tivm_50r_50f_900y, tivm_50r_50f_1000y])
tivm_tot_time_steps_50r_50f = tivm_tot_time_steps_50r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_50f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 50 rms, 0.50 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("50rms_50fdim_kde_all_time_steps.png", dpi=800)



### 50 rms, 0.75 fdim ###
# load data
ice_vol_50rms_75fdim_100 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, nrows=100)
ice_vol_50rms_75fdim_200 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_50rms_75fdim_300 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_50rms_75fdim_400 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_50rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_50rms_75fdim_600 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_50rms_75fdim_700 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_50rms_75fdim_800 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_50rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_50rms_75fdim_1000 = pd.read_csv('ice_vol_1000yr_50rms_75fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_50r_75f_100y = np.mean(ice_vol_50rms_75fdim_100)
tivm_50r_75f_200y = np.mean(ice_vol_50rms_75fdim_200)
tivm_50r_75f_300y = np.mean(ice_vol_50rms_75fdim_300)
tivm_50r_75f_400y = np.mean(ice_vol_50rms_75fdim_400)
tivm_50r_75f_500y = np.mean(ice_vol_50rms_75fdim_500)
tivm_50r_75f_600y = np.mean(ice_vol_50rms_75fdim_600)
tivm_50r_75f_700y = np.mean(ice_vol_50rms_75fdim_700)
tivm_50r_75f_800y = np.mean(ice_vol_50rms_75fdim_800)
tivm_50r_75f_900y = np.mean(ice_vol_50rms_75fdim_900)
tivm_50r_75f_1000y = np.mean(ice_vol_50rms_75fdim_1000)
# build df 
tivm_tot_time_steps_50r_75f = np.array([tivm_50r_75f_100y, tivm_50r_75f_200y, tivm_50r_75f_300y, tivm_50r_75f_400y, 
                                        tivm_50r_75f_500y,tivm_50r_75f_600y, tivm_50r_75f_700y, tivm_50r_75f_800y,
                                        tivm_50r_75f_900y, tivm_50r_75f_1000y])
tivm_tot_time_steps_50r_75f = tivm_tot_time_steps_50r_75f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_75f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 50 rms, 0.75 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("50rms_75fdim_kde_all_time_steps.png", dpi=800)



### 50 rms, 1.0 fdim ###
# load data
ice_vol_50rms_10fdim_100 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, nrows=100)
ice_vol_50rms_10fdim_200 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_50rms_10fdim_300 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_50rms_10fdim_400 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_50rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_50rms_10fdim_600 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_50rms_10fdim_700 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_50rms_10fdim_800 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_50rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_50rms_10fdim_1000 = pd.read_csv('ice_vol_1000yr_50rms_10fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_50r_10f_100y = np.mean(ice_vol_50rms_10fdim_100)
tivm_50r_10f_200y = np.mean(ice_vol_50rms_10fdim_200)
tivm_50r_10f_300y = np.mean(ice_vol_50rms_10fdim_300)
tivm_50r_10f_400y = np.mean(ice_vol_50rms_10fdim_400)
tivm_50r_10f_500y = np.mean(ice_vol_50rms_10fdim_500)
tivm_50r_10f_600y = np.mean(ice_vol_50rms_10fdim_600)
tivm_50r_10f_700y = np.mean(ice_vol_50rms_10fdim_700)
tivm_50r_10f_800y = np.mean(ice_vol_50rms_10fdim_800)
tivm_50r_10f_900y = np.mean(ice_vol_50rms_10fdim_900)
tivm_50r_10f_1000y = np.mean(ice_vol_50rms_10fdim_1000)
# build df 
tivm_tot_time_steps_50r_10f = np.array([tivm_50r_10f_100y, tivm_50r_10f_200y, tivm_50r_10f_300y, tivm_50r_10f_400y, 
                                        tivm_50r_10f_500y,tivm_50r_10f_600y, tivm_50r_10f_700y, tivm_50r_10f_800y,
                                        tivm_50r_10f_900y, tivm_50r_10f_1000y])
tivm_tot_time_steps_50r_10f = tivm_tot_time_steps_50r_10f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_10f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 50 rms, 1.0 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("50rms_10fdim_kde_all_time_steps.png", dpi=800)




### 75 rms ###

### 75 rms, 0.25 fdim ###
# load data
ice_vol_75rms_25fdim_100 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, nrows=100)
ice_vol_75rms_25fdim_200 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_75rms_25fdim_300 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_75rms_25fdim_400 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_75rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_75rms_25fdim_600 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_75rms_25fdim_700 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_75rms_25fdim_800 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_75rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_75rms_25fdim_1000 = pd.read_csv('ice_vol_1000yr_75rms_25fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_75r_25f_100y = np.mean(ice_vol_75rms_25fdim_100)
tivm_75r_25f_200y = np.mean(ice_vol_75rms_25fdim_200)
tivm_75r_25f_300y = np.mean(ice_vol_75rms_25fdim_300)
tivm_75r_25f_400y = np.mean(ice_vol_75rms_25fdim_400)
tivm_75r_25f_500y = np.mean(ice_vol_75rms_25fdim_500)
tivm_75r_25f_600y = np.mean(ice_vol_75rms_25fdim_600)
tivm_75r_25f_700y = np.mean(ice_vol_75rms_25fdim_700)
tivm_75r_25f_800y = np.mean(ice_vol_75rms_25fdim_800)
tivm_75r_25f_900y = np.mean(ice_vol_75rms_25fdim_900)
tivm_75r_25f_1000y = np.mean(ice_vol_75rms_25fdim_1000)
# build df 
tivm_tot_time_steps_75r_25f = np.array([tivm_75r_25f_100y, tivm_75r_25f_200y, tivm_75r_25f_300y, tivm_75r_25f_400y, 
                                        tivm_75r_25f_500y,tivm_75r_25f_600y, tivm_75r_25f_700y, tivm_75r_25f_800y,
                                        tivm_75r_25f_900y, tivm_75r_25f_1000y])
tivm_tot_time_steps_75r_25f = tivm_tot_time_steps_75r_25f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_75r_25f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 75 rms, 0.25 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("75rms_25fdim_kde_all_time_steps.png", dpi=800)



### 75 rms, 0.50 fdim ###
# load data
ice_vol_75rms_50fdim_100 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, nrows=100)
ice_vol_75rms_50fdim_200 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_75rms_50fdim_300 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_75rms_50fdim_400 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_75rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_75rms_50fdim_600 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_75rms_50fdim_700 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_75rms_50fdim_800 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_75rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_75rms_50fdim_1000 = pd.read_csv('ice_vol_1000yr_75rms_50fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_75r_50f_100y = np.mean(ice_vol_75rms_50fdim_100)
tivm_75r_50f_200y = np.mean(ice_vol_75rms_50fdim_200)
tivm_75r_50f_300y = np.mean(ice_vol_75rms_50fdim_300)
tivm_75r_50f_400y = np.mean(ice_vol_75rms_50fdim_400)
tivm_75r_50f_500y = np.mean(ice_vol_75rms_50fdim_500)
tivm_75r_50f_600y = np.mean(ice_vol_75rms_50fdim_600)
tivm_75r_50f_700y = np.mean(ice_vol_75rms_50fdim_700)
tivm_75r_50f_800y = np.mean(ice_vol_75rms_50fdim_800)
tivm_75r_50f_900y = np.mean(ice_vol_75rms_50fdim_900)
tivm_75r_50f_1000y = np.mean(ice_vol_75rms_50fdim_1000)
# build df 
tivm_tot_time_steps_75r_50f = np.array([tivm_75r_50f_100y, tivm_75r_50f_200y, tivm_75r_50f_300y, tivm_75r_50f_400y, 
                                        tivm_75r_50f_500y,tivm_75r_50f_600y, tivm_75r_50f_700y, tivm_75r_50f_800y,
                                        tivm_75r_50f_900y, tivm_75r_50f_1000y])
tivm_tot_time_steps_75r_50f = tivm_tot_time_steps_75r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_75r_50f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 75 rms, 0.50 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("75rms_50fdim_kde_all_time_steps.png", dpi=800)



### 75 rms, 0.75 fdim ###
# load data
ice_vol_75rms_75fdim_100 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, nrows=100)
ice_vol_75rms_75fdim_200 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_75rms_75fdim_300 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_75rms_75fdim_400 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_75rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_75rms_75fdim_600 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_75rms_75fdim_700 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_75rms_75fdim_800 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_75rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_75rms_75fdim_1000 = pd.read_csv('ice_vol_1000yr_75rms_75fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_75r_75f_100y = np.mean(ice_vol_75rms_75fdim_100)
tivm_75r_75f_200y = np.mean(ice_vol_75rms_75fdim_200)
tivm_75r_75f_300y = np.mean(ice_vol_75rms_75fdim_300)
tivm_75r_75f_400y = np.mean(ice_vol_75rms_75fdim_400)
tivm_75r_75f_500y = np.mean(ice_vol_75rms_75fdim_500)
tivm_75r_75f_600y = np.mean(ice_vol_75rms_75fdim_600)
tivm_75r_75f_700y = np.mean(ice_vol_75rms_75fdim_700)
tivm_75r_75f_800y = np.mean(ice_vol_75rms_75fdim_800)
tivm_75r_75f_900y = np.mean(ice_vol_75rms_75fdim_900)
tivm_75r_75f_1000y = np.mean(ice_vol_75rms_75fdim_1000)
# build df 
tivm_tot_time_steps_75r_75f = np.array([tivm_75r_75f_100y, tivm_75r_75f_200y, tivm_75r_75f_300y, tivm_75r_75f_400y, 
                                        tivm_75r_75f_500y,tivm_75r_75f_600y, tivm_75r_75f_700y, tivm_75r_75f_800y,
                                        tivm_75r_75f_900y, tivm_75r_75f_1000y])
tivm_tot_time_steps_75r_75f = tivm_tot_time_steps_75r_75f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_75r_75f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 75 rms, 0.75 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("75rms_75fdim_kde_all_time_steps.png", dpi=800)



### 75 rms, 1.0 fdim ###
# load data
ice_vol_75rms_10fdim_100 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, nrows=100)
ice_vol_75rms_10fdim_200 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_75rms_10fdim_300 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_75rms_10fdim_400 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_75rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_75rms_10fdim_600 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_75rms_10fdim_700 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_75rms_10fdim_800 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_75rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_75rms_10fdim_1000 = pd.read_csv('ice_vol_1000yr_75rms_10fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_75r_10f_100y = np.mean(ice_vol_75rms_10fdim_100)
tivm_75r_10f_200y = np.mean(ice_vol_75rms_10fdim_200)
tivm_75r_10f_300y = np.mean(ice_vol_75rms_10fdim_300)
tivm_75r_10f_400y = np.mean(ice_vol_75rms_10fdim_400)
tivm_75r_10f_500y = np.mean(ice_vol_75rms_10fdim_500)
tivm_75r_10f_600y = np.mean(ice_vol_75rms_10fdim_600)
tivm_75r_10f_700y = np.mean(ice_vol_75rms_10fdim_700)
tivm_75r_10f_800y = np.mean(ice_vol_75rms_10fdim_800)
tivm_75r_10f_900y = np.mean(ice_vol_75rms_10fdim_900)
tivm_75r_10f_1000y = np.mean(ice_vol_75rms_10fdim_1000)
# build df 
tivm_tot_time_steps_75r_10f = np.array([tivm_75r_10f_100y, tivm_75r_10f_200y, tivm_75r_10f_300y, tivm_75r_10f_400y, 
                                        tivm_75r_10f_500y,tivm_75r_10f_600y, tivm_75r_10f_700y, tivm_75r_10f_800y,
                                        tivm_75r_10f_900y, tivm_75r_10f_1000y])
tivm_tot_time_steps_75r_10f = tivm_tot_time_steps_75r_10f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_10f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 75 rms, 1.0 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("75rms_10fdim_kde_all_time_steps.png", dpi=800)




### 100 rms ###

### 100 rms, 0.25 fdim ###
# load data
ice_vol_100rms_25fdim_100 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, nrows=100)
ice_vol_100rms_25fdim_200 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_100rms_25fdim_300 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_100rms_25fdim_400 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_100rms_25fdim_500 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_100rms_25fdim_600 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_100rms_25fdim_700 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_100rms_25fdim_800 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_100rms_25fdim_900 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_100rms_25fdim_1000 = pd.read_csv('ice_vol_1000yr_100rms_25fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_100r_25f_100y = np.mean(ice_vol_100rms_25fdim_100)
tivm_100r_25f_200y = np.mean(ice_vol_100rms_25fdim_200)
tivm_100r_25f_300y = np.mean(ice_vol_100rms_25fdim_300)
tivm_100r_25f_400y = np.mean(ice_vol_100rms_25fdim_400)
tivm_100r_25f_500y = np.mean(ice_vol_100rms_25fdim_500)
tivm_100r_25f_600y = np.mean(ice_vol_100rms_25fdim_600)
tivm_100r_25f_700y = np.mean(ice_vol_100rms_25fdim_700)
tivm_100r_25f_800y = np.mean(ice_vol_100rms_25fdim_800)
tivm_100r_25f_900y = np.mean(ice_vol_100rms_25fdim_900)
tivm_100r_25f_1000y = np.mean(ice_vol_100rms_25fdim_1000)
# build df 
tivm_tot_time_steps_100r_25f = np.array([tivm_100r_25f_100y, tivm_100r_25f_200y, tivm_100r_25f_300y, tivm_100r_25f_400y, 
                                        tivm_100r_25f_500y,tivm_100r_25f_600y, tivm_100r_25f_700y, tivm_100r_25f_800y,
                                        tivm_100r_25f_900y, tivm_100r_25f_1000y])
tivm_tot_time_steps_100r_25f = tivm_tot_time_steps_100r_25f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_100r_25f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 100 rms, 0.25 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("100rms_25fdim_kde_all_time_steps.png", dpi=800)



### 100 rms, 0.50 fdim ###
# load data
ice_vol_100rms_50fdim_100 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, nrows=100)
ice_vol_100rms_50fdim_200 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_100rms_50fdim_300 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_100rms_50fdim_400 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_100rms_50fdim_500 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_100rms_50fdim_600 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_100rms_50fdim_700 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_100rms_50fdim_800 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_100rms_50fdim_900 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_100rms_50fdim_1000 = pd.read_csv('ice_vol_1000yr_100rms_50fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_100r_50f_100y = np.mean(ice_vol_100rms_50fdim_100)
tivm_100r_50f_200y = np.mean(ice_vol_100rms_50fdim_200)
tivm_100r_50f_300y = np.mean(ice_vol_100rms_50fdim_300)
tivm_100r_50f_400y = np.mean(ice_vol_100rms_50fdim_400)
tivm_100r_50f_500y = np.mean(ice_vol_100rms_50fdim_500)
tivm_100r_50f_600y = np.mean(ice_vol_100rms_50fdim_600)
tivm_100r_50f_700y = np.mean(ice_vol_100rms_50fdim_700)
tivm_100r_50f_800y = np.mean(ice_vol_100rms_50fdim_800)
tivm_100r_50f_900y = np.mean(ice_vol_100rms_50fdim_900)
tivm_100r_50f_1000y = np.mean(ice_vol_100rms_50fdim_1000)
# build df 
tivm_tot_time_steps_100r_50f = np.array([tivm_100r_50f_100y, tivm_100r_50f_200y, tivm_100r_50f_300y, tivm_100r_50f_400y, 
                                        tivm_100r_50f_500y,tivm_100r_50f_600y, tivm_100r_50f_700y, tivm_100r_50f_800y,
                                        tivm_100r_50f_900y, tivm_100r_50f_1000y])
tivm_tot_time_steps_100r_50f = tivm_tot_time_steps_100r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_100r_50f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 100 rms, 0.50 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("100rms_50fdim_kde_all_time_steps.png", dpi=800)



### 100 rms, 0.75 fdim ###
# load data
ice_vol_100rms_75fdim_100 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, nrows=100)
ice_vol_100rms_75fdim_200 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_100rms_75fdim_300 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_100rms_75fdim_400 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_100rms_75fdim_500 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_100rms_75fdim_600 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_100rms_75fdim_700 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_100rms_75fdim_800 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_100rms_75fdim_900 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_100rms_75fdim_1000 = pd.read_csv('ice_vol_1000yr_100rms_75fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_100r_75f_100y = np.mean(ice_vol_100rms_75fdim_100)
tivm_100r_75f_200y = np.mean(ice_vol_100rms_75fdim_200)
tivm_100r_75f_300y = np.mean(ice_vol_100rms_75fdim_300)
tivm_100r_75f_400y = np.mean(ice_vol_100rms_75fdim_400)
tivm_100r_75f_500y = np.mean(ice_vol_100rms_75fdim_500)
tivm_100r_75f_600y = np.mean(ice_vol_100rms_75fdim_600)
tivm_100r_75f_700y = np.mean(ice_vol_100rms_75fdim_700)
tivm_100r_75f_800y = np.mean(ice_vol_100rms_75fdim_800)
tivm_100r_75f_900y = np.mean(ice_vol_100rms_75fdim_900)
tivm_100r_75f_1000y = np.mean(ice_vol_100rms_75fdim_1000)
# build df 
tivm_tot_time_steps_100r_75f = np.array([tivm_100r_75f_100y, tivm_100r_75f_200y, tivm_100r_75f_300y, tivm_100r_75f_400y, 
                                        tivm_100r_75f_500y,tivm_100r_75f_600y, tivm_100r_75f_700y, tivm_100r_75f_800y,
                                        tivm_100r_75f_900y, tivm_100r_75f_1000y])
tivm_tot_time_steps_100r_75f = tivm_tot_time_steps_100r_75f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_100r_75f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,3.0e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 100 rms, 0.75 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("100rms_75fdim_kde_all_time_steps.png", dpi=800)



### 100 rms, 1.0 fdim ###
# load data
ice_vol_100rms_10fdim_100 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, nrows=100)
ice_vol_100rms_10fdim_200 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_100rms_10fdim_300 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_100rms_10fdim_400 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_100rms_10fdim_500 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_100rms_10fdim_600 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_100rms_10fdim_700 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_100rms_10fdim_800 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_100rms_10fdim_900 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_100rms_10fdim_1000 = pd.read_csv('ice_vol_1000yr_100rms_10fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_100r_10f_100y = np.mean(ice_vol_100rms_10fdim_100)
tivm_100r_10f_200y = np.mean(ice_vol_100rms_10fdim_200)
tivm_100r_10f_300y = np.mean(ice_vol_100rms_10fdim_300)
tivm_100r_10f_400y = np.mean(ice_vol_100rms_10fdim_400)
tivm_100r_10f_500y = np.mean(ice_vol_100rms_10fdim_500)
tivm_100r_10f_600y = np.mean(ice_vol_100rms_10fdim_600)
tivm_100r_10f_700y = np.mean(ice_vol_100rms_10fdim_700)
tivm_100r_10f_800y = np.mean(ice_vol_100rms_10fdim_800)
tivm_100r_10f_900y = np.mean(ice_vol_100rms_10fdim_900)
tivm_100r_10f_1000y = np.mean(ice_vol_100rms_10fdim_1000)
# build df 
tivm_tot_time_steps_100r_10f = np.array([tivm_100r_10f_100y, tivm_100r_10f_200y, tivm_100r_10f_300y, tivm_100r_10f_400y, 
                                        tivm_100r_10f_500y,tivm_100r_10f_600y, tivm_100r_10f_700y, tivm_100r_10f_800y,
                                        tivm_100r_10f_900y, tivm_100r_10f_1000y])
tivm_tot_time_steps_100r_10f = tivm_tot_time_steps_100r_10f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=tivm_tot_time_steps_50r_10f, fill=True, palette = "crest")
plt.tight_layout(pad=0.5, w_pad=0.3, h_pad=1.0)
ax = plt.gca()
ax.set_xlim([0,2.5e8])
plt.xlabel(r'ice volume (m$^3$)')
plt.title('gaussian KDE for 100 rms, 1.0 fdim every 100 years')
plt.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("100rms_10fdim_kde_all_time_steps.png", dpi=800)





#############################
### SNS plot for bookends ###
#############################

### 25 rms, 0.50 fdim ###
# load data
# REU_V_25rms_50fdim_100 = REU_vol_25rms_50fdim.columns
ice_vol_25rms_50fdim_200 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,100), nrows=100)
ice_vol_25rms_50fdim_300 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,200), nrows=100)
ice_vol_25rms_50fdim_400 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,300), nrows=100)
ice_vol_25rms_50fdim_500 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,400), nrows=100)
ice_vol_25rms_50fdim_600 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,500), nrows=100)
ice_vol_25rms_50fdim_700 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,600), nrows=100)
ice_vol_25rms_50fdim_800 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,700), nrows=100)
ice_vol_25rms_50fdim_900 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,800), nrows=100)
ice_vol_25rms_50fdim_1000 = pd.read_csv('REU_vol_25rms_50fdim.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
tivm_25r_50f_100y = np.mean(ice_vol_25rms_50fdim_100)
tivm_25r_50f_200y = np.mean(ice_vol_25rms_50fdim_200)
tivm_25r_50f_300y = np.mean(ice_vol_25rms_50fdim_300)
tivm_25r_50f_400y = np.mean(ice_vol_25rms_50fdim_400)
tivm_25r_50f_500y = np.mean(ice_vol_25rms_50fdim_500)
tivm_25r_50f_600y = np.mean(ice_vol_25rms_50fdim_600)
tivm_25r_50f_700y = np.mean(ice_vol_25rms_50fdim_700)
tivm_25r_50f_800y = np.mean(ice_vol_25rms_50fdim_800)
tivm_25r_50f_900y = np.mean(ice_vol_25rms_50fdim_900)
tivm_25r_50f_1000y = np.mean(ice_vol_25rms_50fdim_1000)
# build df 
tivm_tot_time_steps_25r_50f = np.array([tivm_25r_50f_100y, tivm_25r_50f_200y, tivm_25r_50f_300y, tivm_25r_50f_400y, 
                                        tivm_25r_50f_500y,tivm_25r_50f_600y, tivm_25r_50f_700y, tivm_25r_50f_800y,
                                        tivm_25r_50f_900y, tivm_25r_50f_1000y])
tivm_tot_time_steps_25r_50f = tivm_tot_time_steps_25r_50f.transpose() # switch rows and columns 


sns_years_lbl = ['0-100 years','100-200','200-300','300-400','400-500','500-600','600-700','700-800','800-900','900-1000']


fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)
rcParams['figure.figsize'] = 8, 4
fig.subplots_adjust(top=0.8)
fig.suptitle('Bookend Gaussian KDE of Ice Volume every 100 years', y = 0.98)
fig.supxlabel(r'Ice Volume (m$^3$)')
sns.kdeplot(data=tivm_tot_time_steps_100r_50f, fill=True, ls='-', lw=2, palette = "crest", label='100 rms, 0.50 fdim', ax = ax1)
handles1 = ax1.legend_.legendHandles
for h, t in zip(handles1, sns_years_lbl):
    h.set_label(t)
# ax1.legend(loc='best')
sns.kdeplot(data=tivm_tot_time_steps_25r_50f, fill=None, ls= '--',lw=2, palette = "crest", label='25 rms, 0.50 fdim', ax = ax2)
for ax in (ax1,ax2):
    ax.set(ylim=[0,1.2e-7])
# plt.xlabel('ice volume (m^3)')
# fig.subplots_adjust(top=0.1)
# rcParams['axes.titlepad'] = 20
fig.subplots_adjust(bottom=0.2)
# plt.title('bookend gaussian KDE of ice volume every 100 years')
# extra1 = Rectangle((0,0), 0.1, 0.1, fc='w', fill=False, 
#                           edgecolor='none', linewidth=0)
# extra2 = Rectangle((0,0), 0.1, 0.1, fc='w', fill=False, 
#                   edgecolor='none', linewidth=0)
# leg = ax.legend([extra1,extra2], 
#                         [('- 100 rms, 0.50 fdim'), ('-- 25 rms, 0.50 fdim')],
#                         loc='best', handlelength=0, handletextpad=0, fancybox=True)
ax1.set_title('100 rms, 0.50 fdim', pad=20)
ax2.set_title('25 rms, 0.50 fdim',pad=20)
ax1.get_legend().remove()
ax2.get_legend().remove()
# # make empty rectangles and assign; supplement_multiplot-ens_mean.py on lizz github
# plt.legend(bbox_to_anchor=(1,1), loc="upper left")
fig.tight_layout(pad=0.4, w_pad=0.3, h_pad=1.0)
fig.legend(['900-1000 years','800-900','700-800','600-700','500-600','400-500',
            '300-400','200-300','100-200','0-100'],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("bookend_kde_all_time_steps.png", dpi=800)  






#####################
### ensmeble mean ###
#####################

### SED ###
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - all rms, all fdim')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
rms = (25,50,75,100)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,rms):
    ax.text(0.1,0.80,'rms {}'.format(f),transform=ax.transAxes)
    
### 25 rms SED ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 25 rms, all fdim (SED)')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ice_vol_25rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = ice_vol_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_25fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='b',ls = '-')
ax1.plot(q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_25rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='orange', ls = '--')
ax1.plot(q3,c='orange', ls = '--')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_25rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = ice_vol_25rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_75fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='g', ls = '-.')
ax1.plot(q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_25rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = ice_vol_25rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_10fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='r', ls = ':')
ax1.plot(q3,c='r', ls = ':')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax1.legend(loc='best')
# plt.savefig("25rms_SED_ens_quantile_ice_vol.png", dpi=800)


### 50 rms SED ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 50 rms, all fdim (SED)')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ice_vol_50rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = ice_vol_50rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_25fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='b',ls = '-')
ax2.plot(q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_50rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = ice_vol_50rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_50fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='orange', ls = '--')
ax2.plot(q3,c='orange', ls = '--')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_50rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = ice_vol_50rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_75fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='g', ls = '-.')
ax2.plot(q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_50rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = ice_vol_50rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_10fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='r', ls = ':')
ax2.plot(q3,c='r', ls = ':')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("50rms_SED_ens_quantile_ice_vol.png", dpi=800)


### 75 rms SED ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 75 rms, all fdim (SED)')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ice_vol_75rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = ice_vol_75rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_25fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='b',ls = '-')
ax3.plot(q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_75rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = ice_vol_75rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_50fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='orange', ls = '--')
ax3.plot(q3,c='orange', ls = '--')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_75rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = ice_vol_75rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_75fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='g', ls = '-.')
ax3.plot(q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_75rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = ice_vol_75rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_10fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='r', ls = ':')
ax3.plot(q3,c='r', ls = ':')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("75rms_SED_ens_quantile_ice_vol.png", dpi=800)


### 100 rms SED ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 100 rms, all fdim (SED)')
# fig.supxlabel('Time (years)')
# fig.supylabel('Volume (m^3)')
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ice_vol_100rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = ice_vol_100rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_25fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='b',ls = '-')
ax4.plot(q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_100rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = ice_vol_100rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_50fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='orange', ls = '--')
ax4.plot(q3,c='orange', ls = '--')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_100rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = ice_vol_100rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_75fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='g', ls = '-.')
ax4.plot(q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_100rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = ice_vol_100rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_10fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='r', ls = ':')
ax4.plot(q3,c='r', ls = ':')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("100rms_SED_ens_quantile_ice_vol.png", dpi=800)
plt.savefig("tot_rms_fdim_med_sed_ens_quantile_ice_vol.png", dpi=800)


### REU ###

### 25 rms REU ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 25 rms, all fdim (REU)')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(REU_vol_25rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = REU_vol_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_25rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = REU_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_25rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = REU_vol_25rms_75fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_25rms_75fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_25rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = REU_vol_25rms_10fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_25rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("25rms_REU_ens_quantile_ice_vol.png", dpi=800)


### 50 rms REU ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 50 rms, all fdim (REU)')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(REU_vol_50rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = REU_vol_50rms_25fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_50rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_50rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = REU_vol_50rms_50fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_50rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_50rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = REU_vol_50rms_75fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_50rms_75fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_50rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = REU_vol_50rms_10fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_50rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("50rms_REU_ens_quantile_ice_vol.png", dpi=800)


### 75 rms REU ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 75 rms, all fdim (REU)')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(REU_vol_75rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = REU_vol_75rms_25fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_75rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_75rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = REU_vol_75rms_50fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_75rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_75rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = REU_vol_75rms_75fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_75rms_75fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_75rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = REU_vol_75rms_10fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_75rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("75rms_REU_ens_quantile_ice_vol.png", dpi=800)


### 100 rms REU ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 100 rms, all fdim (REU)')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(REU_vol_100rms_25fdim.mean(axis=1), ls = '-', label='0.25 fdim')
q1 = REU_vol_100rms_25fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_100rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_100rms_50fdim.mean(axis=1), ls = '--', label='0.50 fdim')
q1 = REU_vol_100rms_50fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_100rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_100rms_75fdim.mean(axis=1), ls = '-.', label='0.75 fdim')
q1 = REU_vol_100rms_75fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_100rms_75fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(REU_vol_100rms_10fdim.mean(axis=1), ls = ':', label='1.0 fdim')
q1 = REU_vol_100rms_10fdim.quantile(q=0.25, axis=1)
q3 = REU_vol_100rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("100rms_REU_ens_quantile_ice_vol.png", dpi=800)



### 0.25 fdim  ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 0.25 fdim, all rms')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax.plot(ice_vol_25rms_25fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_50rms_25fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_75rms_25fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_100rms_25fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("25fdim_ens_quantile_ice_vol.png", dpi=800)

### 0.50 fdim ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 0.50 fdim, all rms')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(ice_vol_25rms_50fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_50rms_50fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_75rms_50fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_100rms_50fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("50fdim_ens_quantile_ice_vol.png", dpi=800)


### 0.75 fdim ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 0.75 fdim, all rms')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(ice_vol_25rms_50fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_50rms_50fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_75rms_50fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_100rms_50fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_50fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("75fdim_ens_quantile_ice_vol.png", dpi=800)

### 1.0 fdim  ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 1.0 fdim, all rms')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_REU,c='k',linewidth=2,label='control')
ax.plot(ice_vol_25rms_10fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_50rms_10fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_25rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_75rms_10fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(ice_vol_100rms_10fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_10fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='r', ls = ':')
ax.plot(q3,c='r', ls = ':')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
plt.savefig("10fdim_ens_quantile_ice_vol.png", dpi=800)


# return em # pandas Series object 
# df.rolling.mean()
# df.quantile(q=0.25 or 0.75 (1st or 3rd quantile), axis = (row or column), interpolation = 'lower' (for 1st quar.) 'higher' (for 3rd quar))



###################################
### ensemble mean - across fdim ###
###################################

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
fig.suptitle('Ice Volume over Time - all fdim, all rms')
fig.supxlabel('Time (years)')
fig.supylabel(r'Volume (m$^3$)')
fdims = (0.25,0.50,0.75,1.0)
axs = (ax1,ax2,ax3,ax4)
for (ax,f) in zip (axs,fdims):
    ax.text(0.1,0.80,'fractal dimension {}'.format(f),transform=ax.transAxes)
   
ax1.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax1.plot(ice_vol_25rms_25fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_25fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='b',ls = '-')
ax1.plot(q3,c='b',ls = '-')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_50rms_25fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_50rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_25fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='orange', ls = '--')
ax1.plot(q3,c='orange', ls = '--')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_75rms_25fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_25fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='g', ls = '-.')
ax1.plot(q3,c='g', ls = '-.')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax1.plot(ice_vol_100rms_25fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_25fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_25fdim.quantile(q=0.75, axis=1)
ax1.plot(q1,c='r', ls = ':')
ax1.plot(q3,c='r', ls = ':')
ax1.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("25fdim_SED_ens_quantile_ice_vol.png", dpi=800)


### 0.50 fdim ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 0.50 fdim, all rms')
# fig.supxlabel('Time (years)')
# fig.supylabel(r'Volume (m$^3$)')
ax2.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax2.plot(ice_vol_25rms_50fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_50fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='b',ls = '-')
ax2.plot(q3,c='b',ls = '-')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_50rms_50fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_50rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_50fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='orange', ls = '--')
ax2.plot(q3,c='orange', ls = '--')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_75rms_50fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_50fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='g', ls = '-.')
ax2.plot(q3,c='g', ls = '-.')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax2.plot(ice_vol_100rms_50fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_50fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_50fdim.quantile(q=0.75, axis=1)
ax2.plot(q1,c='r', ls = ':')
ax2.plot(q3,c='r', ls = ':')
ax2.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("50fdim_SED_ens_quantile_ice_vol.png", dpi=800)


### 0.75 fdim ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 0.75 fdim, all rms')
# fig.supxlabel('Time (years)')
# fig.supylabel(r'Volume (m$^3$)')
ax3.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax3.plot(ice_vol_25rms_75fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_75fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='b',ls = '-')
ax3.plot(q3,c='b',ls = '-')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_50rms_75fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_50rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_75fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='orange', ls = '--')
ax3.plot(q3,c='orange', ls = '--')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_75rms_75fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_75fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='g', ls = '-.')
ax3.plot(q3,c='g', ls = '-.')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax3.plot(ice_vol_100rms_75fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_75fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_75fdim.quantile(q=0.75, axis=1)
ax3.plot(q1,c='r', ls = ':')
ax3.plot(q3,c='r', ls = ':')
ax3.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax.legend(loc='best')
# plt.savefig("75fdim_SED_ens_quantile_ice_vol.png", dpi=800)


### 1.0 fdim ###
# fig, ax = plt.subplots(sharey=True)
# fig.suptitle('Mean Ice Volume over Time - 1.0 fdim, all rms')
# fig.supxlabel('Time (years)')
# fig.supylabel(r'Volume (m$^3$)')
ax4.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax4.plot(ice_vol_25rms_10fdim.mean(axis=1), ls = '-', label='25 rms')
q1 = ice_vol_25rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_25rms_10fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='b',ls = '-')
ax4.plot(q3,c='b',ls = '-')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_50rms_10fdim.mean(axis=1), ls = '--', label='50 rms')
q1 = ice_vol_50rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_50rms_10fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='orange', ls = '--')
ax4.plot(q3,c='orange', ls = '--')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_75rms_10fdim.mean(axis=1), ls = '-.', label='75 rms')
q1 = ice_vol_75rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_75rms_10fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='g', ls = '-.')
ax4.plot(q3,c='g', ls = '-.')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax4.plot(ice_vol_100rms_10fdim.mean(axis=1), ls = ':', label='100 rms')
q1 = ice_vol_100rms_10fdim.quantile(q=0.25, axis=1)
q3 = ice_vol_100rms_10fdim.quantile(q=0.75, axis=1)
ax4.plot(q1,c='r', ls = ':')
ax4.plot(q3,c='r', ls = ':')
ax4.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
# ax4.legend(loc='best')
# plt.savefig("10fdim_SED_ens_quantile_ice_vol.png", dpi=800)

plt.savefig("tot_fdim_rms_ice_vol_quantile.png", dpi=800)


###################################
##### compare rates of change #####
###################################

# calculate time different 
# calculate difference between two data points 
# remember to take absolute value for REU bc its a negative number for mass loss
# could use pandas:
    # df_series = pd.Series(df)
    # df_series.pct_change()
# could use numpy:
    # Compute an array of velocities as the slope between each point
        # diff_distances = np.diff(____)
        # diff_times = np.diff(____)
        # velocities = ____ / diff_times

    # Chracterize the center and spread of the velocities
        # v_avg = np.____(velocities)
        # v_max = np.____(velocities)
        # v_min = np.____(velocities)
        # v_range = ____ - ____

    # Plot the distribution of velocities
        # fig = plot_velocity_timeseries(times[1:], velocities)

### 25 rms ###

### 25 rms REU ###

# set new timestamp index for REU data to match SED
REU_time_inc = np.array([50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 
                          600.0, 650.0, 700.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0])

ROC_REU_25r_25f = REU_vol_25rms_25fdim.pct_change()
ROC_REU_25r_25f = np.abs(ROC_REU_25r_25f)
ROC_REU_25r_25f["Timestamp"] = REU_time_inc
ROC_REU_25r_25f = ROC_REU_25r_25f.set_index("Timestamp")

ROC_REU_25r_50f = REU_vol_25rms_50fdim.pct_change()
ROC_REU_25r_50f = np.abs(ROC_REU_25r_50f)
ROC_REU_25r_50f["Timestamp"] = REU_time_inc
ROC_REU_25r_50f = ROC_REU_25r_50f.set_index("Timestamp")

ROC_REU_25r_75f = REU_vol_25rms_75fdim.pct_change()
ROC_REU_25r_75f = np.abs(ROC_REU_25r_75f)
ROC_REU_25r_75f["Timestamp"] = REU_time_inc
ROC_REU_25r_75f = ROC_REU_25r_75f.set_index("Timestamp")

ROC_REU_25r_10f = REU_vol_25rms_10fdim.pct_change()
ROC_REU_25r_10f = np.abs(ROC_REU_25r_10f)
ROC_REU_25r_10f["Timestamp"] = REU_time_inc
ROC_REU_25r_10f = ROC_REU_25r_10f.set_index("Timestamp")

### 25 rms SED ###
ROC_SED_25r_25f = ice_vol_25rms_25fdim.pct_change()
ROC_SED_25r_25f = np.abs(ROC_SED_25r_25f)

ROC_SED_25r_50f = ice_vol_25rms_50fdim.pct_change()
ROC_SED_25r_50f = np.abs(ROC_SED_25r_50f)

ROC_SED_25r_75f = ice_vol_25rms_75fdim.pct_change()
ROC_SED_25r_75f = np.abs(ROC_SED_25r_75f)

ROC_SED_25r_10f = ice_vol_25rms_10fdim.pct_change()
ROC_SED_25r_10f = np.abs(ROC_SED_25r_10f)

### 25 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 25 rms, all fdim (REU vs. SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.plot(ROC_REU_25r_25f.mean(axis=1), c = 'b', ls='-', label = 'REU')
ax.plot(ROC_REU_25r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_REU_25r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_REU_25r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_SED_25r_25f.mean(axis=1), c = 'k', ls=':', label = 'SED')
ax.plot(ROC_SED_25r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_25r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_25r_10f.mean(axis=1), c = 'k', ls=':')
ax.legend()
plt.savefig("pct_chg_REUvSED_25rms.png", dpi=800)



### 50 rms ###

### 50 rms REU ###
ROC_REU_50r_25f = REU_vol_50rms_25fdim.pct_change()
ROC_REU_50r_25f = np.abs(ROC_REU_50r_25f)
ROC_REU_50r_25f["Timestamp"] = REU_time_inc
ROC_REU_50r_25f = ROC_REU_50r_25f.set_index("Timestamp")

ROC_REU_50r_50f = REU_vol_50rms_50fdim.pct_change()
ROC_REU_50r_50f = np.abs(ROC_REU_50r_50f)
ROC_REU_50r_50f["Timestamp"] = REU_time_inc
ROC_REU_50r_50f = ROC_REU_50r_50f.set_index("Timestamp")

ROC_REU_50r_75f = REU_vol_50rms_75fdim.pct_change()
ROC_REU_50r_75f = np.abs(ROC_REU_50r_75f)
ROC_REU_50r_75f["Timestamp"] = REU_time_inc
ROC_REU_50r_75f = ROC_REU_50r_75f.set_index("Timestamp")

ROC_REU_50r_10f = REU_vol_50rms_10fdim.pct_change()
ROC_REU_50r_10f = np.abs(ROC_REU_50r_10f)
ROC_REU_50r_10f["Timestamp"] = REU_time_inc
ROC_REU_50r_10f = ROC_REU_50r_10f.set_index("Timestamp")

### 50 rms SED ###
ROC_SED_50r_25f = ice_vol_50rms_25fdim.pct_change()
ROC_SED_50r_25f = np.abs(ROC_SED_50r_25f)

ROC_SED_50r_50f = ice_vol_50rms_50fdim.pct_change()
ROC_SED_50r_50f = np.abs(ROC_SED_50r_50f)

ROC_SED_50r_75f = ice_vol_50rms_75fdim.pct_change()
ROC_SED_50r_75f = np.abs(ROC_SED_50r_75f)

ROC_SED_50r_10f = ice_vol_50rms_10fdim.pct_change()
ROC_SED_50r_10f = np.abs(ROC_SED_50r_10f)

### 50 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 50 rms, all fdim (REU vs. SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.plot(ROC_REU_50r_25f.mean(axis=1), c = 'b', ls='-', label='REU')
ax.plot(ROC_REU_50r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_REU_50r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_REU_50r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_SED_50r_25f.mean(axis=1), c = 'k', ls=':', label='SED')
ax.plot(ROC_SED_50r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_50r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_50r_10f.mean(axis=1), c = 'k', ls=':')
ax.legend()
plt.savefig("pct_chg_REUvSED_50rms.png", dpi=800)


### 75 rms ###

### LOW ###
# ROC_REU_100r_25f = REU_vol_100rms_25fdim.pct_change()
# ROC_REU_100r_25f = np.abs(ROC_REU_100r_25f)
# ROC_REU_100r_25f["Timestamp"] = REU_time_inc
# ROC_REU_100r_25f = ROC_REU_100r_25f.set_index("Timestamp")

low_sed_75r_25f = pd.read_csv('low_sed_75r_25f.csv', index_col=0)
low_sed_75r_25f = low_sed_75r_25f.pct_change()
low_sed_75r_25f = np.abs(low_sed_75r_25f)

low_sed_75r_50f = pd.read_csv('low_sed_75r_50f.csv', index_col=0)
low_sed_75r_50f = low_sed_75r_50f.pct_change()
low_sed_75r_50f = np.abs(low_sed_75r_50f)

low_sed_75r_75f = pd.read_csv('low_sed_75r_75f.csv', index_col=0)
low_sed_75r_75f = low_sed_75r_75f.pct_change()
low_sed_75r_75f = np.abs(low_sed_75r_75f)

low_sed_75r_10f = pd.read_csv('low_sed_75r_10f.csv', index_col=0)
low_sed_75r_10f = low_sed_75r_10f.pct_change()
low_sed_75r_10f = np.abs(low_sed_75r_10f)

### MED ###
ROC_SED_75r_25f = ice_vol_75rms_25fdim.pct_change()
ROC_SED_75r_25f = np.abs(ROC_SED_75r_25f)

ROC_SED_75r_50f = ice_vol_75rms_50fdim.pct_change()
ROC_SED_75r_50f = np.abs(ROC_SED_75r_50f)

ROC_SED_75r_75f = ice_vol_75rms_75fdim.pct_change()
ROC_SED_75r_75f = np.abs(ROC_SED_75r_75f)

ROC_SED_75r_10f = ice_vol_75rms_10fdim.pct_change()
ROC_SED_75r_10f = np.abs(ROC_SED_75r_10f)

### HIGH ###
high_sed_75r_25f = pd.read_csv('high_sed_75r_25f.csv', index_col=0)
high_sed_75r_25f = high_sed_75r_25f.pct_change()
high_sed_75r_25f = np.abs(high_sed_75r_25f)

high_sed_75r_50f = pd.read_csv('high_sed_75r_50f.csv', index_col=0)
high_sed_75r_50f = high_sed_75r_50f.pct_change()
high_sed_75r_50f = np.abs(high_sed_75r_50f)

high_sed_75r_75f = pd.read_csv('high_sed_75r_75f.csv', index_col=0)
high_sed_75r_75f = high_sed_75r_75f.pct_change()
high_sed_75r_75f = np.abs(high_sed_75r_75f)

high_sed_75r_10f = pd.read_csv('high_sed_75r_10f.csv', index_col=0)
high_sed_75r_10f = high_sed_75r_10f.pct_change()
high_sed_75r_10f = np.abs(high_sed_75r_10f)

### 100 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 100 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.plot(low_sed_75r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(low_sed_75r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(low_sed_75r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(low_sed_75r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_SED_75r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ROC_SED_75r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_75r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_75r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(high_sed_75r_25f.mean(axis=1), c = 'k', ls='--', label = "high sed")
ax.plot(high_sed_75r_50f.mean(axis=1), c = 'k', ls='--')
ax.plot(high_sed_75r_75f.mean(axis=1), c = 'k', ls='--')
ax.plot(high_sed_75r_10f.mean(axis=1), c = 'k', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_rms75.png", dpi=800)


### 100 rms ###

### LOW ###
# ROC_REU_100r_25f = REU_vol_100rms_25fdim.pct_change()
# ROC_REU_100r_25f = np.abs(ROC_REU_100r_25f)
# ROC_REU_100r_25f["Timestamp"] = REU_time_inc
# ROC_REU_100r_25f = ROC_REU_100r_25f.set_index("Timestamp")

low_sed_100r_25f = pd.read_csv('low_sed_100r_25f.csv', index_col=0)
low_sed_100r_25f = low_sed_100r_25f.pct_change()
low_sed_100r_25f = np.abs(low_sed_100r_25f)

low_sed_100r_50f = pd.read_csv('low_sed_100r_50f.csv', index_col=0)
low_sed_100r_50f = low_sed_100r_50f.pct_change()
low_sed_100r_50f = np.abs(low_sed_100r_50f)

low_sed_100r_75f = pd.read_csv('low_sed_100r_75f.csv', index_col=0)
low_sed_100r_75f = low_sed_100r_75f.pct_change()
low_sed_100r_75f = np.abs(low_sed_100r_75f)

low_sed_100r_10f = pd.read_csv('low_sed_100r_10f.csv', index_col=0)
low_sed_100r_10f = low_sed_100r_10f.pct_change()
low_sed_100r_10f = np.abs(low_sed_100r_10f)

### MED ###
ROC_SED_100r_25f = ice_vol_100rms_25fdim.pct_change()
ROC_SED_100r_25f = np.abs(ROC_SED_100r_25f)

ROC_SED_100r_50f = ice_vol_100rms_50fdim.pct_change()
ROC_SED_100r_50f = np.abs(ROC_SED_100r_50f)

ROC_SED_100r_75f = ice_vol_100rms_75fdim.pct_change()
ROC_SED_100r_75f = np.abs(ROC_SED_100r_75f)

ROC_SED_100r_10f = ice_vol_100rms_10fdim.pct_change()
ROC_SED_100r_10f = np.abs(ROC_SED_100r_10f)

### HIGH ###
high_sed_100r_25f = pd.read_csv('high_sed_100r_25f.csv', index_col=0)
high_sed_100r_25f = high_sed_100r_25f.pct_change()
high_sed_100r_25f = np.abs(high_sed_100r_25f)

high_sed_100r_50f = pd.read_csv('high_sed_100r_50f.csv', index_col=0)
high_sed_100r_50f = high_sed_100r_50f.pct_change()
high_sed_100r_50f = np.abs(high_sed_100r_50f)

high_sed_100r_75f = pd.read_csv('high_sed_100r_75f.csv', index_col=0)
high_sed_100r_75f = high_sed_100r_75f.pct_change()
high_sed_100r_75f = np.abs(high_sed_100r_75f)

high_sed_100r_10f = pd.read_csv('high_sed_100r_10f.csv', index_col=0)
high_sed_100r_10f = high_sed_100r_10f.pct_change()
high_sed_100r_10f = np.abs(high_sed_100r_10f)

### 100 rms plot ###
fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean % Ice Volume Change over Time - 100 rms, all fdim (all SED)')
fig.supxlabel('Time (years)')
fig.supylabel('percent change')
ax.plot(low_sed_100r_25f.mean(axis=1), c = 'b', ls='-', label = 'low sed')
ax.plot(low_sed_100r_50f.mean(axis=1), c = 'b', ls='-')
ax.plot(low_sed_100r_75f.mean(axis=1), c = 'b', ls='-')
ax.plot(low_sed_100r_10f.mean(axis=1), c = 'b', ls='-')
ax.plot(ROC_SED_100r_25f.mean(axis=1), c = 'k', ls=':', label = "med. sed")
ax.plot(ROC_SED_100r_50f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_100r_75f.mean(axis=1), c = 'k', ls=':')
ax.plot(ROC_SED_100r_10f.mean(axis=1), c = 'k', ls=':')
ax.plot(high_sed_100r_25f.mean(axis=1), c = 'k', ls='--', label = "high sed")
ax.plot(high_sed_100r_50f.mean(axis=1), c = 'k', ls='--')
ax.plot(high_sed_100r_75f.mean(axis=1), c = 'k', ls='--')
ax.plot(high_sed_100r_10f.mean(axis=1), c = 'k', ls='--')
ax.legend()
plt.savefig("pct_chg_all_SED_100rms.png", dpi=800)




###################################
####### compare SED values ########
###################################

### 25 rms ###
LSIV_25rms_25fdim = pd.read_csv('low_sed_25r_25f.csv', index_col=0)
MSIV_25rms_25fdim = ice_vol_25rms_25fdim.iloc[:,:10]
HSIV_25rms_25fdim = pd.read_csv('high_sed_25r_25f.csv', index_col=0)

# MIV_25rms_50fdim = pd.read_csv('ice_vol_1000yr_25rms_50fdim.csv', index_col=0, nrows=10)

# MIV_25rms_75fdim = pd.read_csv('ice_vol_1000yr_25rms_75fdim.csv', index_col=0, nrows=10)

# MIV_25rms_10fdim = pd.read_csv('ice_vol_1000yr_25rms_10fdim.csv', index_col=0, nrows=10)

fig, ax = plt.subplots(sharey=True)
fig.suptitle('Mean Ice Volume over Time - 25 rms, 0.25 fdim')
fig.supxlabel('Time (years)')
fig.supylabel('Volume (m^3)')
ax.plot(ctrl_SED,c='k',linewidth=2,label='control')
ax.plot(LSIV_25rms_25fdim.mean(axis=1), ls = '-', label='low sed')
q1 = LSIV_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = LSIV_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='b',ls = '-')
ax.plot(q3,c='b',ls = '-')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(MSIV_25rms_25fdim.mean(axis=1), ls = '--', label='med sed')
q1 = MSIV_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = MSIV_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='orange', ls = '--')
ax.plot(q3,c='orange', ls = '--')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.plot(HSIV_25rms_25fdim.mean(axis=1), ls = '-.', label='high sed')
q1 = HSIV_25rms_25fdim.quantile(q=0.25, axis=1)
q3 = HSIV_25rms_25fdim.quantile(q=0.75, axis=1)
ax.plot(q1,c='g', ls = '-.')
ax.plot(q3,c='g', ls = '-.')
ax.fill_between(np.arange(len(q1)),q1,q3, alpha=0.2)
ax.legend(loc='best')
# plt.savefig("100rms_REU_ens_quantile_ice_vol.png", dpi=800)

### low sed 25 rms, 0.25 fdim ###
# load data
LSIV_25rms_25fdim_100 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, nrows=100)
LSIV_25rms_25fdim_200 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,100), nrows=100)
LSIV_25rms_25fdim_300 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,200), nrows=100)
LSIV_25rms_25fdim_400 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,300), nrows=100)
LSIV_25rms_25fdim_500 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,400), nrows=100)
LSIV_25rms_25fdim_600 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,500), nrows=100)
LSIV_25rms_25fdim_700 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,600), nrows=100)
LSIV_25rms_25fdim_800 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,700), nrows=100)
LSIV_25rms_25fdim_900 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,800), nrows=100)
LSIV_25rms_25fdim_1000 = pd.read_csv('low_sed_25r_25f.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
LSIV_25r_25f_100y = np.mean(LSIV_25rms_25fdim_100)
LSIV_25r_25f_200y = np.mean(LSIV_25rms_25fdim_200)
LSIV_25r_25f_300y = np.mean(LSIV_25rms_25fdim_300)
LSIV_25r_25f_400y = np.mean(LSIV_25rms_25fdim_400)
LSIV_25r_25f_500y = np.mean(LSIV_25rms_25fdim_500)
LSIV_25r_25f_600y = np.mean(LSIV_25rms_25fdim_600)
LSIV_25r_25f_700y = np.mean(LSIV_25rms_25fdim_700)
LSIV_25r_25f_800y = np.mean(LSIV_25rms_25fdim_800)
LSIV_25r_25f_900y = np.mean(LSIV_25rms_25fdim_900)
LSIV_25r_25f_1000y = np.mean(LSIV_25rms_25fdim_1000)
# build df 
LSIV_tot_time_steps_50r_25f = np.array([LSIV_25r_25f_100y, LSIV_25r_25f_200y, LSIV_25r_25f_300y, LSIV_25r_25f_400y, 
                                        LSIV_25r_25f_500y,LSIV_25r_25f_600y, LSIV_25r_25f_700y, LSIV_25r_25f_800y,
                                        LSIV_25r_25f_900y, LSIV_25r_25f_1000y])
LSIV_tot_time_steps_50r_25f = LSIV_tot_time_steps_50r_25f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=LSIV_tot_time_steps_50r_25f, fill=True, palette = "crest")
plt.xlabel('ice volume (m^3)')
plt.title('gaussian KDE for 25 rms, 0.25 fdim every 100 years')
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("low_sed_25rms_25fdim_kde_all_time_steps.png", dpi=800)


### low sed 25 rms, 0.50 fdim ###
# load data
LSIV_25rms_50fdim_100 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, nrows=100)
LSIV_25rms_50fdim_200 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,100), nrows=100)
LSIV_25rms_50fdim_300 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,200), nrows=100)
LSIV_25rms_50fdim_400 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,300), nrows=100)
LSIV_25rms_50fdim_500 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,400), nrows=100)
LSIV_25rms_50fdim_600 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,500), nrows=100)
LSIV_25rms_50fdim_700 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,600), nrows=100)
LSIV_25rms_50fdim_800 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,700), nrows=100)
LSIV_25rms_50fdim_900 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,800), nrows=100)
LSIV_25rms_50fdim_1000 = pd.read_csv('low_sed_25r_50f.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
LSIV_25r_50f_100y = np.mean(LSIV_25rms_50fdim_100)
LSIV_25r_50f_200y = np.mean(LSIV_25rms_50fdim_200)
LSIV_25r_50f_300y = np.mean(LSIV_25rms_50fdim_300)
LSIV_25r_50f_400y = np.mean(LSIV_25rms_50fdim_400)
LSIV_25r_50f_500y = np.mean(LSIV_25rms_50fdim_500)
LSIV_25r_50f_600y = np.mean(LSIV_25rms_50fdim_600)
LSIV_25r_50f_700y = np.mean(LSIV_25rms_50fdim_700)
LSIV_25r_50f_800y = np.mean(LSIV_25rms_50fdim_800)
LSIV_25r_50f_900y = np.mean(LSIV_25rms_50fdim_900)
LSIV_25r_50f_1000y = np.mean(LSIV_25rms_50fdim_1000)
# build df 
LSIV_tot_time_steps_50r_50f = np.array([LSIV_25r_50f_100y, LSIV_25r_50f_200y, LSIV_25r_50f_300y, LSIV_25r_50f_400y, 
                                        LSIV_25r_50f_500y,LSIV_25r_50f_600y, LSIV_25r_50f_700y, LSIV_25r_50f_800y,
                                        LSIV_25r_50f_900y, LSIV_25r_50f_1000y])
LSIV_tot_time_steps_50r_50f = LSIV_tot_time_steps_50r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=LSIV_tot_time_steps_50r_50f, fill=True, palette = "crest")
plt.xlabel('ice volume (m^3)')
plt.title('gaussian KDE for low sed 25 rms, 0.50 fdim every 100 years')
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("low_sed_25rms_50fdim_kde_all_time_steps.png", dpi=800)


### high sed 25 rms, 0.50 fdim ###
# load data
LSIV_25rms_50fdim_100 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, nrows=100)
LSIV_25rms_50fdim_200 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,100), nrows=100)
LSIV_25rms_50fdim_300 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,200), nrows=100)
LSIV_25rms_50fdim_400 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,300), nrows=100)
LSIV_25rms_50fdim_500 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,400), nrows=100)
LSIV_25rms_50fdim_600 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,500), nrows=100)
LSIV_25rms_50fdim_700 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,600), nrows=100)
LSIV_25rms_50fdim_800 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,700), nrows=100)
LSIV_25rms_50fdim_900 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,800), nrows=100)
LSIV_25rms_50fdim_1000 = pd.read_csv('high_sed_25r_50f.csv', index_col=0, skiprows=range(1,900), nrows=100)
# get mean, tiv = total ice vol mean
LSIV_25r_50f_100y = np.mean(LSIV_25rms_50fdim_100)
LSIV_25r_50f_200y = np.mean(LSIV_25rms_50fdim_200)
LSIV_25r_50f_300y = np.mean(LSIV_25rms_50fdim_300)
LSIV_25r_50f_400y = np.mean(LSIV_25rms_50fdim_400)
LSIV_25r_50f_500y = np.mean(LSIV_25rms_50fdim_500)
LSIV_25r_50f_600y = np.mean(LSIV_25rms_50fdim_600)
LSIV_25r_50f_700y = np.mean(LSIV_25rms_50fdim_700)
LSIV_25r_50f_800y = np.mean(LSIV_25rms_50fdim_800)
LSIV_25r_50f_900y = np.mean(LSIV_25rms_50fdim_900)
LSIV_25r_50f_1000y = np.mean(LSIV_25rms_50fdim_1000)
# build df 
LSIV_tot_time_steps_50r_50f = np.array([LSIV_25r_50f_100y, LSIV_25r_50f_200y, LSIV_25r_50f_300y, LSIV_25r_50f_400y, 
                                        LSIV_25r_50f_500y,LSIV_25r_50f_600y, LSIV_25r_50f_700y, LSIV_25r_50f_800y,
                                        LSIV_25r_50f_900y, LSIV_25r_50f_1000y])
LSIV_tot_time_steps_50r_50f = LSIV_tot_time_steps_50r_50f.transpose() # switch rows and columns 

# SNS plot
plt.figure()
sns.kdeplot(data=LSIV_tot_time_steps_50r_50f, fill=True, palette = "crest")
plt.xlabel('ice volume (m^3)')
plt.title('gaussian KDE for high sed 25 rms, 0.50 fdim every 100 years')
# plt.legend(["0-100", "100-200","200-300","300-400","400-500","500-600",
#             "600-700","700-800","800-900","900-1000"], loc ="upper right")
plt.savefig("high_sed_25rms_50fdim_kde_all_time_steps.png", dpi=800)



