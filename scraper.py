import requests


def fetch_game_deals(limit=5):
    """Fetch game deals from the CheapShark API."""

    url = "https://www.cheapshark.com/api/1.0/deals"

    params = {
        "pageSize": limit
    }

    headers = {
        "User-Agent": "GameDealsScraper/1.0"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=(5, 30)
        )

        response.raise_for_status()

        deals = response.json()

        return deals

    except requests.exceptions.RequestException as error:
        print("Failed to fetch game deals:", error)
        return []


if __name__ == "__main__":
    from database import create_database, save_game_deals

    create_database()

    deals = fetch_game_deals(10)

    if deals:
        save_game_deals(deals)
    else:
        print("No game deals were fetched.")