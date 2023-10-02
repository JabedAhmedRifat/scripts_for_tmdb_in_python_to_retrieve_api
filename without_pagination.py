import requests
import time
from datetime import datetime, timedelta

api_key = "b1c6b1d4eee69018389a08305b8e88cd"


base_url = "https://api.themoviedb.org/3/find/tt15354916?external_source=imdb_id"



end_date = datetime.now().date()

start_date = end_date - timedelta(days=7) 


params = {
    "api_key": api_key,
    "primary_release_date.gte": None,  
    "primary_release_date.lte": start_date,
    
    }
response = requests.get(base_url, params=params)

if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
    
else:
    print(f"Failed to retrieve movie details. Status code:", response.status_code)
