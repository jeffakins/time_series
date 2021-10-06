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