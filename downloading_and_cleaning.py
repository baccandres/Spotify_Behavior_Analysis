import pandas as pd
import numpy as np
import requests
import json
import os
from dotenv import load_dotenv
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression


load_dotenv()

client_ID = os.getenv("client_ID")
client_secret = os.getenv("client_secret")

def connect_api (client_ID, client_secret):
    """
    Run this function every now and then to
    reconnect to Spotify API.    
    """
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_ID,
        'client_secret': client_secret
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    return access_token, headers


def song_attributes (endPoint, uri, headers):
    """
    This function helps iterate by track id 
    over the different endpoints Spotify 
    offers.

    endPoint = self explanatory
    uri = Spotify track_id (list)

    """
    dummyList = []
    for i in uri:
        base_url = 'https://api.spotify.com/v1/'
        r = requests.get(base_url + endPoint + i, headers=headers).json()
        dummyList.append(r)
    return pd.DataFrame(dummyList)


def part_of_day (x):
    """
    Returns the part of the day 
    based on the hour.
    """
    if (x > 4) and (x <= 8):
        return 'Early Morning'
    elif (x > 8) and (x <= 12 ):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return'Noon'
    elif (x > 16) and (x <= 20) :
        return 'Eve'
    elif (x > 20) and (x <= 24):
        return'Night'
    elif (x <= 4):
        return'Late Night'


def year_quarter (y):
    """
    Returns year quarter based
    on month.
    """
    if y >= 1 and y <= 3:
        return 'Q1'
    elif y >= 4 and y <= 6:
        return 'Q2'
    elif y >= 7 and y <= 9:
        return 'Q3'
    elif y >= 10 and y <= 12:
        return 'Q4'

def scatters (q,w,t):
    """
    q = a list of x's
    w = a fixed 'y'
    t = the database for y
    Returns the scatterplots of a list of 'Xs'
    while the 'y' remains the same through iterations.
    """
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20,5))
    for i in range(len(q)):
        r = sns.scatterplot(y=w, x=q[i], data=t, ax=axs[i])
    return r


