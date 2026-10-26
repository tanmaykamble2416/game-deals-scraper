import requests


def fetch_game_deals(limit=10, page_number=0, sort_by="Deal Rating"):
    """Fetch game deals from the CheapShark API."""
    url = "https://www.cheapshark.com/api/1.0/deals"

    params = {
        "pageSize": limit,
        "pageNumber": page_number,
        "sortBy": sort_by,
    }

    headers = {
        "User-Agent": "GameDealsScraper/1.0",
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=(5, 30),
        )

        response.raise_for_status()
        deals = response.json()

        print(f"API returned {len(deals)} deals.")

        for deal in deals:
            print("Fetched:", deal.get("title", "Unknown game"))

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




