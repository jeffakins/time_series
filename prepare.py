# Time series prepare file:

# Imports:
import pandas as pd
import numpy as np
from datetime import timedelta, datetime

import acquire as ac

# Prepare Function for Store Data:
def prepare_store_data():
    '''Function to prepare store data'''

    store_df = ac.acquire_store_data()                                      # Acquire the data
    store_df.sale_date = pd.to_datetime(store_df.sale_date)                 # Convert sales date to datetime format
    store_df = store_df.set_index('sale_date').sort_index()                 # Set date as index
    store_df['month'] = store_df.index.month_name()                         # Create a month column
    store_df['day'] = store_df.index.day_name()                             # Create a day column
    store_df['sales_total'] = store_df.sale_amount * store_df.item_price    # Creation of a sales total column

    return store_df



# Prepare function for the opsd_germany_daily.csv data
def prepare_opsd():
    '''Function to prepare the ops data'''
    opsd = ac.get_opsd_data()                                   # Acquire the data
    opsd.Date = pd.to_datetime(opsd.Date)                       # Convert date column to pd datetime
    opsd = opsd.set_index('Date').sort_index()                  # Sort by date
    opsd = opsd.drop(columns='Unnamed: 0')                      # Drop random column
    opsd['month'] = opsd.index.month_name()                     # Create month column
    opsd['year'] = opsd.index.year                              # Create date column
    opsd = opsd.fillna(0)                                       # Fill NaN with zero
    opsd['wind_plus_solar'] = opsd['Wind'] + opsd['Solar']      # Calculate wind+solar
    opsd = opsd.drop(columns='Wind+Solar')                      # Drop the Wind+Solar column due to missing calculations

    return opsd