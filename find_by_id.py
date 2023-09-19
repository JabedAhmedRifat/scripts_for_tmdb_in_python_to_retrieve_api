import requests
import time
from datetime import datetime, timedelta

api_key = "b1c6b1d4eee69018389a08305b8e88cd"

# Construct the URL using the TMDb ID
base_url = "https://api.themoviedb.org/3/trending/movie/week"


end_date = datetime.now().date()

start_date = end_date - timedelta(days=7) 

# Define your API parameters, if needed
params = {
    "api_key": api_key,
    "primary_release_date.gte": None,  
    "primary_release_date.lte": start_date,
    
    }
    # Add any other parameters you need here

response = requests.get(base_url, params=params)

if response.status_code == 200:
    movie_data = response.json()
    # print("Movie Details:")
    # print("Title:", movie_data.get("title"))
    # print("Release Date:", movie_data.get("release_date"))
    print(movie_data)
    
else:
    print(f"Failed to retrieve movie details. Status code:", response.status_code)
