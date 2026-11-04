# -*- coding: utf-8 -*-
"""
Builder for the Complete KPOINT Macro Polymarket Alpha Database.
Combines all 7 categories:
1. Politics (Day 10, Week 10, Month 10) = 30
2. Crypto (Day 10, Week 10, Month 10) = 30
3. Finance (Day 10, Week 10, Month 10) = 30
4. Sport (Day 10, Week 10, Month 10) = 30
5. Football - Premier League (Day 10, Week 10, Month 10) = 30
6. Football - La Liga (Day 10, Week 10, Month 10) = 30
7. Football - Bundesliga (Day 10, Week 10, Month 10) = 30
Total = 210 fully analyzed institutional markets.
"""

import json
import os

from build_dataset import DATA as POLITICS_BASE
import generate_full_db
from finance_data import FINANCE_DATA
from sport_data import SPORT_DATA
from football_premier_league_data import PREMIER_LEAGUE_DATA
from football_la_liga_data import LA_LIGA_DATA
from football_bundesliga_data import BUNDESLIGA_DATA

def build_database():
    crypto_data = generate_full_db.generate_all_markets()["crypto"]

    db = {
        "metadata": {
            "platform": "Polymarket Alpha Terminal // KPOINT Hedge Fund Strategy",
            "tagline": "Macro Institutional Polymarket Intelligence & Alpha Signals",
            "generatedAt": "2026-11-04T02:15:00Z",
            "totalCategories": 7,
            "totalMarkets": 210,
            "signature": "KPOINT made this one. Not financial advice the risk is yours and yours only."
        },
        "politics": POLITICS_BASE["politics"],
        "crypto": crypto_data,
        "finance": FINANCE_DATA,
        "sport": SPORT_DATA,
        "premier_league": PREMIER_LEAGUE_DATA,
        "la_liga": LA_LIGA_DATA,
        "bundesliga": BUNDESLIGA_DATA
    }

    # Verify counts
    total = 0
    categories = ["politics", "crypto", "finance", "sport", "premier_league", "la_liga", "bundesliga"]
    for cat in categories:
        for tf in ["day", "week", "month"]:
            count = len(db[cat][tf])
            total += count
            assert count == 10, f"Error: {cat} {tf} has {count} items, expected 10"

    print(f"Verification successful: {len(categories)} categories x 3 timeframes x 10 markets = {total} markets.")

    out_path = os.path.join(os.path.dirname(__file__), "polymarket_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    build_database()
