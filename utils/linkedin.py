import config

import requests


def scrape_linkedin_profile(linkedin_profile_url: str) -> dict:
    """
    Scrape information from Linkedin profiles
    """
    headers = {"Authorization": f"Bearer {config.PROXY_CURL_API_KEY}"}
    params = {"url": "linkedin_profile_url"}

    # response = requests.get(config.PROXY_CURL_LINKEDIN_API_URL, params=params, headers=headers)
    response = requests.get(
        "https://gist.githubusercontent.com/m-c-hill/343778bb7d08fcf88e764f40fd432e56/raw/6dda401be49e3194806503aec9cb47b1d93dc5ec/gistfile1.txt"
    )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
