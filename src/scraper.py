from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

"""
    To Avoid getting blocked from IMDB Server, headers are needed.
    Failing to provide a header results to 403 error
"""
headers = {
    'User-Agent': 'Chrome/91.0.4472.124',
    'Accept-Language': 'en-US,en;q=0.9',
}

#check if successfully requested in IMDB
try: 
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    
    print("Successfully fetched the IMDb Top 250 page.")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Looks for script tag with JSON-LD that contains the movie data
    scripts = soup.find("script", id="__NEXT_DATA__", type="application/json")
    
    #parse it as JSON
    if scripts:
        try:
            data = json.loads(scripts.string)
            edges = data["props"]["pageProps"]["pageData"]["chartTitles"]["edges"]
            
            movies_data = [
                {
                    "rank":movie["currentRank"],
                    "title":movie["node"]["titleText"]["text"],
                    "release_date": f'{movie["node"].get("releaseDate").get("day","??")}-{movie["node"].get("releaseDate").get("month","N/A")}-{movie["node"].get("releaseDate").get("year","N/A")}',
                    "genre":[g["genre"]["text"] for g in movie["node"].get("titleGenres", {}).get("genres", [])],
                    "movie_rating": (movie["node"].get("certificate") or {}).get("rating", "N/A"),
                    "rating_summary":movie["node"].get("ratingsSummary", {}).get("aggregateRating", "N/A"),
                    "vote_count":movie["node"].get("ratingsSummary", {}).get("voteCount", "N/A"),
                    "run_time_seconds":movie["node"].get("runtime",{}).get("seconds","N/A")
                }
                    
                for movie in edges
            ]
            
            scraped_data = {
                "scraped_at": datetime.now().isoformat(), #local time
                "movies": movies_data
            }

            with open("../data/raw/data.json","w") as file:
                json.dump(scraped_data, file, indent=4,ensure_ascii=False)  
                
            print("Saved movies to raw folder ✅")
              
        except KeyError as e:
            print(f"Key error in JSON structure: {e}")

    
# return if error  
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the page. Error: {e}")
    