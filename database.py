import sqlite3


def create_database():
    """Create the database and game deals table."""

    connection = sqlite3.connect("game_deals.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_deals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            deal_id TEXT UNIQUE,
            title TEXT NOT NULL,
            normal_price REAL,
            sale_price REAL,
            savings REAL
        )
    """)

    cursor.execute("PRAGMA table_info(game_deals)")
    columns = [column[1] for column in cursor.fetchall()]

    if "deal_id" not in columns:
        cursor.execute(
            "ALTER TABLE game_deals ADD COLUMN deal_id TEXT"
        )

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_game_deals_deal_id
        ON game_deals(deal_id)
    """)

    connection.commit()
    connection.close()

def save_game_deals(deals):
    """Insert new deals or update existing deals."""

    connection = sqlite3.connect("game_deals.db")
    cursor = connection.cursor()

    for deal in deals:
        deal_id = deal["dealID"]
        title = deal["title"]
        normal_price = float(deal["normalPrice"])
        sale_price = float(deal["salePrice"])
        savings = float(deal["savings"])

        # Check whether this deal already exists by its deal ID.
        cursor.execute(
            "SELECT id FROM game_deals WHERE deal_id = ?",
            (deal_id,)
        )

        existing_deal = cursor.fetchone()

        if existing_deal:
            cursor.execute("""
                UPDATE game_deals
                SET title = ?,
                    normal_price = ?,
                    sale_price = ?,
                    savings = ?
                WHERE deal_id = ?
            """, (
                title,
                normal_price,
                sale_price,
                savings,
                deal_id
            ))

        else:
            # Check whether an old record matches this deal.
            cursor.execute("""
                SELECT id FROM game_deals
                WHERE deal_id IS NULL
                  AND title = ?
                  AND normal_price = ?
                  AND sale_price = ?
                LIMIT 1
            """, (title, normal_price, sale_price))

            old_deal = cursor.fetchone()

            if old_deal:
                cursor.execute("""
                    UPDATE game_deals
                    SET deal_id = ?,
                        savings = ?
                    WHERE id = ?
                """, (deal_id, savings, old_deal[0]))

            else:
                cursor.execute("""
                    INSERT INTO game_deals (
                        deal_id,
                        title,
                        normal_price,
                        sale_price,
                        savings
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    deal_id,
                    title,
                    normal_price,
                    sale_price,
                    savings
                ))

    connection.commit()
    connection.close()

    print(f"Processed {len(deals)} game deals successfully!")

def get_game_deals():
    """Retrieve all saved game deals from the database."""

    connection = sqlite3.connect("game_deals.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, normal_price, sale_price, savings
        FROM game_deals
    """)

    deals = cursor.fetchall()

    connection.close()

    return deals
def migrate_old_deals():
    """Remove old records that duplicate deals with existing deal IDs."""

    connection = sqlite3.connect("game_deals.db")
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM game_deals
        WHERE deal_id IS NULL
          AND EXISTS (
              SELECT 1
              FROM game_deals AS newer
              WHERE newer.deal_id IS NOT NULL
                AND newer.title = game_deals.title
                AND newer.normal_price = game_deals.normal_price
                AND newer.sale_price = game_deals.sale_price
          )
    """)

    removed = cursor.rowcount

    connection.commit()
    connection.close()

    print(f"Removed {removed} old duplicate records.")

if __name__ == "__main__":
    create_database()
    print("Database and table created successfully!")