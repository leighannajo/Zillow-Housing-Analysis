import pandas as pd
import numpy as np

import collections

import matplotlib.pyplot as plt

def missing_data(df):
    new = pd.DataFrame()
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
    new = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return new.loc[new['Percent']>0]

def melt_data(df): # from flatiron starter notebook
    melted = pd.melt(df, id_vars=['RegionID','RegionName', 'City', 'State', 'Metro', 'CountyName',                             'SizeRank'], var_name='time', value_name='MeanValue')
    melted['time'] = pd.to_datetime(melted['time'], format='%Y-%m')
    melted = melted.dropna(subset=['MeanValue'])
    return melted

def plot(df):
    df.plot( figsize=(13, 8))
    plt.show()
    
def subplots(df):
    df.plot( figsize=(13, 8), subplots=True)
    plt.show()
    
def get_plotting(df):
    df = df.groupby("time")['roi'].sum().reset_index()
    df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
    df = df.set_index('time')
    df.plot( figsize=(13, 8))
    plt.show()
    return df

def change_time(df):
    df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
    return df

def get_return_rate(col_1, col_2, df):
    cost_year = df[col_1]
    gain_year = df[col_2]
    return_rate = ((gain_year-cost_year) / cost_year)*100
    return return_rate


def get_index_ready(df):    
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'time'}, inplace=True)
    
def get_mean_year(df, year='1996'):   
    temp_df = df.copy()
    for col in temp_df:
        if year not in col:
            temp_df.drop([col], inplace=True, axis=1)
        temp_df[year] = temp_df.mean(axis=1).astype('int')
    for col in temp_df.columns:
        if '-' in col:
            temp_df.drop([col], inplace=True, axis=1)
        df[year] = temp_df[year]
    return df
   