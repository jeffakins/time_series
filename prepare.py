# Time series prepare file:

# Imports:
import pandas as pd
import numpy as np
from datetime import timedelta, datetime

import acquire as ac

# Prepare Function:
def prepare_store_data():
    '''Function to prepare store data'''

    store_df = ac.acquire_store_data()                          # Acquire the data
    store_df.sale_date = pd.to_datetime(store_df.sale_date)     # Convert sales date to datetime format
    store_df['month'] = store_df.sale_date.dt.month             # Create a month column
    store_df['day'] = store_df.sale_date.dt.day                 # Create a day column

    return store_df