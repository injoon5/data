import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url: str = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=injoon5&api_key={os.environ["LAST_FM_PUBLIC_API_KEY"]}&format=json'

headers: dict = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_now_playing():
    import requests
    result = requests.get(url, headers=headers)
    print(result.status_code)
    print(result.headers)
    print(result.content)
    return result


if __name__ == '__main__':
    response = get_now_playing().json()
    
    # Ensure we only have 4 tracks
    response['recenttracks']['track'] = response['recenttracks']['track'][:4]
    
    with open('now-playing.json', 'w') as f:
        json.dump(response, f, indent=2)
