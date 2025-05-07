import json

file_path = '../data/raw/data.json'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    """
        Transforming seconds into Hours and Minutes format e.g. 2h 50m
    """
    
    for movie in data["movies"]:
        hours = movie["run_time_seconds"] / 3600
        remaining = movie['run_time_seconds'] % 3600
        minutes = remaining / 60
        movie['run_time_seconds'] = f"{int(hours)}h {int(minutes)}m"


    with open("../data/cleaned/cleaned.json", 'w') as file:
        json.dump(data, file, indent=4)
        

except KeyError as e: #raises an error if keys value pairs are wrong
    print(f"Key error in JSON structure: {e}")
