from bs4 import BeautifulSoup

def get_game_deals(html):
    """Extract game titles and prices from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    
    games = soup.find_all("div", class_="game")
    if not games:
      print("No games found in the HTML.")
      return []
 
    deals = []

    for game in games:
        title_element=game.find("h2")
        price_element=game.find("p")

        if title_element is None or price_element is None:
           continue
        deal={
            "title":title_element.get_text(strip=True),
             "price":price_element.get_text(strip=True)

        }
        
    

        deals.append(deal)
        return deals

if __name__ == "__main__":
 sample_html = """ <html> <body> 
       
    </body>
</html>
"""

game_deals = get_game_deals(sample_html)

for deal in game_deals:
    print(deal)

