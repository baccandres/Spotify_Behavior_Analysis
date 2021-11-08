Spotify Pipeline 

The Spotify Pipeline project is about complementing a database with data sourced from the internet via an API and afterward tell a story about it.

The second part of the project consists of building a data pipeline so the analysis can be automated for future updates.

For this project I chose to download a set of files from Spotify that show my streaming history during the past year. Then I enhanced it with specific information about the artists and tracks I listened to by downloading additional features through the their API.

The exploratory analysis shows a glimpse of the variables and statistics that Spotify might use for their segmentation and recommendations to regular users.

The analysis is conducted in Python using the following libraries: pandas, numpy, requests, json, os, seaborn and matplotlib.

The repository contains the following jupyter notebooks:

    1-enriching-and-cleaning: a step by step explanation of it.

    2-visualizations_notebook: the conclusions of the analysis with charts and figures.

Python files:

    1-downloading_and_cleaning: includes the functions used to clean the databases and visuals.
    
    2-main: the functions called to automate the analysis.

Data files have been hidden for privacy.














References:

https://support.spotify.com/us/article/understanding-my-data/
https://developer.spotify.com/dashboard/applications/07e518e5e13b469d81f8d41e7227fbc7
https://stmorse.github.io/journal/spotify-api.html
https://towardsdatascience.com/visualizing-spotify-data-with-python-tableau-687f2f528cdd
Ironhack notes
https://developer.spotify.com/documentation/web-api/reference/#/
https://developer.spotify.com/documentation/web-api/guides/rate-limits/
https://towardsdatascience.com/visualizing-spotify-songs-with-python-an-exploratory-data-analysis-fc3fae3c2c09
