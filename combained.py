import requests
import time
from datetime import datetime, timedelta

api_key = "b1c6b1d4eee69018389a08305b8e88cd"



base_url = "https://api.themoviedb.org/3/movie/popular"



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
    
    total_pages = movie_data.get("total_pages", 1)
    
    if total_pages == 1:
        
        print(movie_data)
    else:
        page = 1
        max_pages = 10
        data = []

        while page <= max_pages:
            params["page"] = page
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                results = response.json().get("results", [])

                if not results:
                    break

                data.extend(results)
                page += 1

                time.sleep(1)
            else:
                print(f"Failed to retrieve changes. Status code:", response.status_code)
                break

        print("Media objects:", data)
else:
    print(f"Failed to retrieve movie details. Status code:", response.status_code)
