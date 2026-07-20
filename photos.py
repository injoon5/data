import json
import requests


def get_recent_photos() -> dict:
    api_url = "https://photos.injoon5.com/feed.json"
    response = requests.get(api_url, timeout=30)
    response.raise_for_status()
    data = response.json()

    photos = data.get("photos")
    if photos is None:
        raise RuntimeError("Photos feed missing photos array")

    # Keep the 8 most recent photos
    data["photos"] = photos[:8]
    return data


if __name__ == "__main__":
    payload = get_recent_photos()
    with open("photos.json", "w") as f:
        json.dump(payload, f, indent=2)
    print("Saved recent photos to photos.json")
