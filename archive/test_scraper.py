from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

"""
    To Avoid getting blocked from IMDB Server, headers are needed.
    Failing to provide a header results to 403 error
"""
  
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    
    print("Successfully fetched the IMDb Top 250 page.")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open('imdb_top250_pretty2.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    movies = soup.find_all("div", class_="sc-5179a348-0 kfocva cli-children")
        
    for movie in movies:
        title_tag = movie.find("h3")
        title = title_tag.text.strip() if title_tag else "N/A"
        
        meta_data = movie.find_all("span", class_="sc-5179a348-7 idrYgr cli-title-metadata-item")
        year = meta_data[0].text if len(meta_data) > 0 else "N/A"
        length = meta_data[1].text if len(meta_data) > 1 else "N/A"
        rated = meta_data[2].text if len(meta_data) > 2 else "N/A"
        
        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"Length: {length}")
        print(f"Rated: {rated}")
        
        
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the page. Error: {e}")
    
