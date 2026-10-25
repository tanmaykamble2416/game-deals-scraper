from database import get_game_deals

deals = get_game_deals()

print(f"Total records found: {len(deals)}")
print()

for deal in deals:
    print("ID:", deal[0])
    print("Game:", deal[1])
    print("Original price: $", deal[2])
    print("Sale price: $", deal[3])
    print("Discount:", round(deal[4]), "%")
    print("-" * 30)