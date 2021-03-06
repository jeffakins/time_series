# Acquire Scripts

# Imports:
import requests
import pandas as pd
import os

# Acquire Function:
def acquire_store_data():
    '''Function to read store data from a csv or from the API'''
    if os.path.isfile('store_sales_items.csv') == False:
        df = get_store_data()
    else:
        df = pd.read_csv('store_sales_items.csv')
    return df

# Get the store data:
def get_store_data():
    '''Function to acquire store data from api'''

    base_url = 'https://python.zgulde.net'


    # Items ----------
    response = requests.get(base_url + '/api/v1/items')
    data = response.json()
    num_pages = data['payload']['max_page']                 # Max page number for the 'for' loop
    pages = []                                              # Initializing a list to hold the sales information
    
    for i in range(1, num_pages+1):                         # for loop to put all of the sales pages in a list
        response = requests.get(base_url + '/api/v1/items?page=' + str(i))
        items = response.json()['payload']['items']
        pages += items
        
    item_list = pd.DataFrame(pages)                        # Converting the list to a dataframe


    # Stores -----------
    response = requests.get(base_url + '/api/v1/stores')
    data = response.json()
    num_pages = data['payload']['max_page']                 # Max page number for the 'for' loop
    pages = []                                              # Initializing a list to hold the sales information
    
    for i in range(1, num_pages+1):                         # for loop to put all of the sales pages in a list
        response = requests.get(base_url + '/api/v1/stores?page=' + str(i))
        stores = response.json()['payload']['stores']
        pages += stores
        
    store_list = pd.DataFrame(pages)                        # Converting the list to a dataframe


    # Sales --------------
    response = requests.get(base_url + '/api/v1/sales')
    data = response.json()
    num_pages = data['payload']['max_page']                 # Max page number for the 'for' loop
    pages = []                                              # Initializing a list to hold the sales information
    
    for i in range(1, num_pages+1):                         # for loop to put all of the sales pages in a list
        response = requests.get(base_url + '/api/v1/sales?page=' + str(i))
        sales = response.json()['payload']['sales']
        pages += sales
        
    sales_list = pd.DataFrame(pages)                        # Converting the list to a dataframe

    # Combining sales, stores, and items ------
    sales_plus_stores = pd.merge(
        sales_list, 
        store_list,
        how='left',
        left_on='store',
        right_on='store_id')

    sales_stores_items = pd.merge(
        sales_plus_stores,
        item_list,
        how='left',
        left_on='item',
        right_on='item_id')

    sales_stores_items.to_csv('store_sales_items.csv')        # create csv file

    return sales_stores_items


# Open Power Systems Data for Germany
def get_opsd_data():
    '''Function to get the Open Power Systems Data for Germany'''

    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    
    if os.path.isfile('opsd_germany_daily.csv') == False:
        df = pd.read_csv(url)
        df.to_csv('opsd_germany_daily.csv')
    else:
        df = pd.read_csv('opsd_germany_daily.csv')
    return df