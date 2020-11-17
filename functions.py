import pandas as pd
import numpy as np

import collections

import matplotlib.pyplot as plt

def missing_data(df):
    """ This function takes in a dataframe, calculates
    the total missing values and the percentage of missing
    values per column and returns a new dataframe.
    """
    new = pd.DataFrame()
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
    new = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return new.loc[new['Percent']>0]

def melt_data(df): # from flatiron starter notebook - I made slight changes 
    """ Takes in a dataframe in wide format, keeps
    all columns listed the same and melts any columns not
    listed.  Returns dataframe with melted columns as 
    datetime.
    """
    melted = pd.melt(df, id_vars=['RegionID','ZipCode', 'City', 'State', 'Metro', 'CountyName',                             'SizeRank'], var_name='time', value_name='MeanValue')
    melted['time'] = pd.to_datetime(melted['time'], format='%Y-%m')
    melted = melted.dropna(subset=['MeanValue'])
    return melted

def plot(df):
    """ Takes in: dataframe
    
        Returns: plot
    """
    df.plot(figsize=(13, 8))
    plt.show()
    
def subplots(df):
    """ Takes in: dataframe
    
        Returns: subplots
    """
    df.plot( figsize=(13, 8), subplots=True)
    plt.show()
    
def get_plotting(df, col_1, col_2):
    """ Takes in: dataframe and two columns
        
        Groups time columns by col_2 and sets time
        column as index and to datetime object.
    
    
        Returns: plot
    """
    df = df.groupby("time")[col_2].sum().reset_index()
    df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
    df.set_index('time', inplace=True)
    df.plot( figsize=(13, 8))
    plt.show()
    return df

def change_time(df):
    """ Takes in: dataframe
        
        Sets time column to index and changes to datetime object.
    
        Returns: dataframe
    """
    df['Time'] = pd.to_datetime(df['Time'], infer_datetime_format=True)
    df.set_index('Time', inplace=True)
    return df

def get_return_rate(col_1, col_2, df):
    """ Takes in: dataframe and two columns
        
        Calculates the return on investment rate percentage
    
        Returns: return rate 
    """
    cost_year = df[col_1]
    gain_year = df[col_2]
    return_rate = ((gain_year-cost_year) / cost_year)*100
    return return_rate


def get_index_ready(df):  
    """ Takes in: dataframe
        
        Resets the index and renames column as 'time'
        (used for saving to csv)
    
        Returns: df
    """
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'time'}, inplace=True)
    
def get_mean_year(df, year): 
    """ Takes in: dataframe and a year
    
        Makes a temp dataframe copy of dataframe, 
        iterates through and drops all columns besides year
        and adds the mean of year column and drops all the 
        individual month columns
      
        Returns: dataframe with updated year mean column 
    """
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
   