import tomllib
import json
from googleapiclient.discovery import build


def get_keys(filename: str) -> dict:
    with open(filename, "rb") as f:
        data = tomllib.load(f)
    return data["access"]


def search(term: str, **kwargs) -> None:
    keys = get_keys("key.toml")
    api_key, cx_id = keys["api_key"], keys["cx"]
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=term, cx=cx_id, **kwargs).execute()

    out = [
        {"title": item["title"], "snippet": item["snippet"], "link": item["link"]}
        for item in res["items"]
    ]

    with open(f"results.json", "w") as f:
        json.dump(out, f)

    print(f"saved results to {f.name}")


keys = get_keys("key.toml")
search("dog")
