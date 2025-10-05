import requests
import json

def get_recent_photos():
    api_url = "https://photos.injoon5.com/feed.json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Ensure we only have 6 photos
        data["photos"] = data["photos"][:8]
        
        with open("photos.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print("Saved recent photos to photos.json")
    else:
        print(f"Failed to fetch photos: {response.status_code}")

if __name__ == "__main__":
    get_recent_photos()
