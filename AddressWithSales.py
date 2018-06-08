#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:53:56 2018

@author: michaelpalmer
"""

import pandas as pd
data=pd.read_csv('EXTR_ResBldg.csv')
sales_data=pd.read_csv('EXTR_RPSale.csv')
data['PIN'] = data['Major'].map(str)  +'-' + data["Minor"].map(str)
sales_data['PIN'] = sales_data['Major'].map(str)  +'-' + sales_data["Minor"].map(str)
filtered_data = data[data['YrBuilt'] > 2011]
AddressWithSales=pd.merge(filtered_data, sales_data, on='PIN')
