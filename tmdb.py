import requests
import time
from datetime import datetime, timedelta

api_key = "b1c6b1d4eee69018389a08305b8e88cd"

base_url = "https://api.themoviedb.org/3/discover/movie?language=en-US&region=IN&with_original_language=hi"

end_date = datetime.now().date()

start_date = end_date - timedelta(days=1)

page = 1
max_pages = 10
data = []

while page <= max_pages:
    params = {
        "api_key": api_key,

        "page": page,
        # "primary_release_date.gte": start_date,
        # "primary_release_date.lte": end_date,
    
    }

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
