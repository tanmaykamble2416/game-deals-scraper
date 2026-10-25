import requests

url = "https://www.cheapshark.com/api/1.0/deals?pageSize=5"

headers = {
    "User-Agent": "GameDealsScraper/1.0"
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=(5, 30)
    )

    print("Status code:", response.status_code)

    response.raise_for_status()

    deals = response.json()

    for deal in deals:
        print("Game:", deal["title"])
        print("Original price: $", deal["normalPrice"])
        print("Sale price: $", deal["salePrice"])
        print("Discount:", round(float(deal["savings"])), "%")
        print("-" * 30)

except requests.exceptions.Timeout:
    print("The server took too long to respond. Please try again.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the server. Check your internet connection.")

except requests.exceptions.HTTPError as error:
    print("The server returned an HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)