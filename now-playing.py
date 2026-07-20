import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["LAST_FM_PUBLIC_API_KEY"]
url = (
    "https://ws.audioscrobbler.com/2.0/"
    f"?method=user.getrecenttracks&user=injoon5"
    f"&api_key={api_key}&format=json"
)


def get_now_playing() -> dict:
    response = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    response.raise_for_status()
    data = response.json()

    tracks = data.get("recenttracks", {}).get("track")
    if tracks is None:
        raise RuntimeError("Last.fm response missing recenttracks.track")

    # Keep the 20 most recent tracks
    data["recenttracks"]["track"] = tracks[:20]
    return data


if __name__ == "__main__":
    payload = get_now_playing()
    with open("now-playing.json", "w") as f:
        json.dump(payload, f, indent=2)
    print("Saved recent tracks to now-playing.json")
