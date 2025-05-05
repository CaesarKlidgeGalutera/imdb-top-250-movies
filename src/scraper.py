from bs4 import BeautifulSoup
import requests
import json

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
    scripts = soup.find("script", type="application/ld+json")
    
    #parse it as JSON
    data = json.loads(scripts.string)

    if isinstance(data, dict) and "itemListElement" in data:
        movies_data = [
            { 
                "title":movie["item"].get("name","N/A")
            }
            
            for movie in data["itemListElement"]
        ]

    with open("../data/raw/data.json","w") as f:
        json.dump(movies_data, f, indent=4,ensure_ascii=False)   
        
    print("Saved movies to raw folder ✅")
# return if error  
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the page. Error: {e}")
    