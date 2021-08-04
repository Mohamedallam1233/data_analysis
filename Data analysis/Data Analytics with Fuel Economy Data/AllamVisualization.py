import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def show_heatmap(dff):
    sns.heatmap(dff.corr(), cmap='coolwarm', annot=True)
    plt.suptitle("heatmap of the data")
def show_clustermap(dff):
    sns.clustermap(dff.corr(), annot=True)
    plt.suptitle("cluster map of the data")
def ckeck_for_null(dff):
    print(dff.isna().sum())
    plt.figure(figsize=(12,12))
    sns.heatmap(dff.isnull(), cbar=False)
    plt.suptitle("check missing values")
    #plt.show()
