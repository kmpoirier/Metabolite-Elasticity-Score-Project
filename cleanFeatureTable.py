#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:58:55 2025

@author: kaylapoirier
"""

import pandas as pd #version 2.2.2
import numpy as np #version 1.26.4
from scipy.stats import mannwhitneyu #version 1.15.2


df = pd.read_csv('feature_table_ex_meta.csv') #load data

positions = df['DigitizedPosition'].unique() #make an array of all organ positions
infection_time = df['days.post.infection'].unique() #make an array of 12 and 89 days


for pos in positions:
    for t in infection_time:
        filtered_df = df[(df['DigitizedPosition'] == pos) & (df['days.post.infection']==t)] 
        filtered_df=filtered_df.drop(['ID', 'sample_type', 'DigitizedPosition', 'days.post.infection'], axis=1) #remove ID, sample type, digitized postions and days post infection
        
        infected_df=filtered_df[filtered_df["condition"]=='infected'] #makes dataframe of just infected with specific organ and post day infection
        uninfected_df=filtered_df[filtered_df["condition"]=='uninfected'] #makes dataframe of just uninfected with specific organ and post day infection
        
        p_values={}
        for column in filtered_df.select_dtypes(include=[np.number]).columns:
            infected_vals=infected_df[column].dropna() #remove NAs for infected
            uninfected_vals=uninfected_df[column].dropna() #remove NAs for uninfected
            stats, p_val=mannwhitneyu(infected_vals, uninfected_vals) #p-values comparing infected with uninfected of each metabolite in each time and organ
            p_values[column]=p_val
            
            
        pval_df = pd.DataFrame.from_dict(p_values, orient='index', columns=['adj.P.Val'])
        
        
        median_df=filtered_df.groupby("condition").median(numeric_only=True)
        ratio_df=(median_df.loc["infected"]+0.5)/(median_df.loc["uninfected"]+0.5) #log(median infected+0.5/median uninfected+0.5)
        ratio_df=np.log(ratio_df)
        ratio_df=pd.DataFrame(ratio_df, columns=['log2FC'])
        
        result_df = ratio_df.join(pval_df) #join p-value dataframe and logFC dataframe together
        result_df.index.name = 'ID'
        filename = f'{pos}/newratio_{t}.txt' #make a new file called newratio_12.txt and newratio_89.txt for each organ and save it to individual folders by organ
        with open(filename, "w") as file: 
            file.write(str(result_df))

        print(f'df_{pos}_{t}.csv')
        
        
        
        