from flask import Flask, render_template, jsonify
from database import get_game_deals, create_database, save_game_deals
from scraper import fetch_game_deals

app = Flask(__name__)

@app.route("/")
def home():
    deals = get_game_deals()
    return render_template("index.html", deals=deals)


@app.route("/api/refresh", methods=["POST"])
def refresh_deals():
    # Fetch fresh deals from the CheapShark API.
    fresh_deals = fetch_game_deals(10)

    # Some APIs return a dict with a "deals" key, while others return a list.
    if isinstance(fresh_deals, dict):
        fresh_deals = fresh_deals.get("deals", [])

    if not fresh_deals or not isinstance(fresh_deals, list):
        return jsonify({
            "success": False,
            "message": "Could not fetch deals. Please try again."
        }), 502

    try:
        # Save the fetched deals to SQLite.
        save_game_deals(fresh_deals)

        # Retrieve the updated database records.
        deals = get_game_deals()
    except Exception as exc:
        return jsonify({
            "success": False,
            "message": f"Could not save deals: {exc}"
        }), 500

    # Convert database tuples into JSON-friendly dictionaries.
    deals_data = []
    for deal in deals:
        if isinstance(deal, dict):
            deals_data.append({
                "id": deal.get("id"),
                "title": deal.get("title"),
                "normal_price": deal.get("normal_price"),
                "sale_price": deal.get("sale_price"),
                "savings": deal.get("savings")
            })
        elif isinstance(deal, (tuple, list)) and len(deal) >= 5:
            deals_data.append({
                "id": deal[0],
                "title": deal[1],
                "normal_price": deal[2],
                "sale_price": deal[3],
                "savings": deal[4]
            })

    return jsonify({
        "success": True,
        "message": f"Successfully refreshed {len(fresh_deals)} deals!",
        "deals": deals_data
    })


if __name__ == "__main__":
    create_database()
    app.run(debug=True)