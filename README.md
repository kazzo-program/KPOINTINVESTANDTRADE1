# KPOINT // Polymarket Macro Alpha Terminal

An institutional-grade prediction market intelligence terminal built with a crisp **Blue and White** interface. The terminal pulls **real-time live markets directly from Polymarket** across **Politics**, **Finance**, **Crypto**, **Sport**, and **Major UK & European Football Tournaments** (**Premier League**, **La Liga**, and **Bundesliga**) across **Day (24H)**, **Week (7D)**, and **Month (30D)** timeframes.

> *"KPOINT made this one. Not financial advice the risk is yours and yours only."*

---

## 🔑 Are Polymarket API Keys Required?

**NO! Zero API keys are required.**

Polymarket operates two distinct interfaces:
1. **Polymarket Gamma API (Used Here)**:
   - Endpoint: `https://gamma-api.polymarket.com/events`
   - **100% Free & Completely Public**.
   - Requires **no API key**, **no account registration**, and **no authentication headers**.
   - Provides live market questions, real-time trading volumes, active order book outcome probabilities (YES / NO prices), and event URLs.
2. **Polymarket CLOB API (Only for Trading)**:
   - Used exclusively for programmatically placing bets / signing Ethereum L2 transactions from a crypto wallet. Not required for reading live events or conducting hedge fund macro analysis.

---

## ⚡ Real-Time Live Sync Architecture

1. **Direct Polymarket Event Links**:
   - Every market title and "Trade on Polymarket ↗" button links directly to the authentic live Polymarket event page:
     `https://polymarket.com/event/<event-slug>`
2. **Automatic Refresh on Every Page Load**:
   - Every time you open or refresh the browser, the terminal queries Polymarket's live Gamma endpoints across all 7 categories:
     - `politics`
     - `crypto`
     - `economy` / `business` (Finance)
     - `sports`
     - `premier-league`
     - `la-liga`
     - `bundesliga`
3. **Continuous 15-Second Background Ticker**:
   - The terminal runs an automated 15-second background sync cycle that updates live trading volumes and odds without requiring page reloads.
4. **Macro Hedge Fund Advisory Engine**:
   - **Explicit Action**: **BET YES** or **BET NO** based on expected value (EV+).
   - **Conviction & Confidence**: Scoring from 75% to 96% with quantified EV edge (e.g. `+14.6% EV+`).
   - **Macro Strategy Thesis**: Institutional explanations of order book imbalances, liquidity sweeps, and capital flows.
   - **Verified News Catalysts**: Breaking headlines with sources (**Bloomberg**, **Reuters**, **Financial Times**, **CoinDesk**, **Sky Sports**, **Fabrizio Romano**, **Opta**, **Kicker**).
   - **Social Media Radar**: Sentiment meter (% Bullish/Bearish), social velocity tracking (**X / Twitter**, **Reddit**, **Telegram**), and on-chain whale orders.
   - **Exit Target & Stop-Loss**: Defined profit milestones (e.g., `Target: $0.88 (+23.9%)`, `Stop-Loss: $0.60`).

---

## 🚀 How to Run the Website

### Option 1: Double-Click Launcher (Windows)
Double-click `start_terminal.bat` in the folder. It will launch the local Python server on port 8080 and automatically open your default browser to `http://localhost:8080`.

### Option 2: Command Line
```powershell
python server.py
```
Then navigate in your browser to:
[http://localhost:8080](http://localhost:8080)

### Option 3: Manual Force Live Sync
To refresh all live Polymarket events from the terminal command line at any time:
```powershell
python live_polymarket_engine.py
```

### Option 4: Standalone / GitHub Pages Mode
You can also open `index.html` directly in any web browser. The client-side engine in `app.js` will fetch live Polymarket events directly from the browser!

---

## 🏛️ Project Structure

- `index.html` — Blue and white structural frontend with all navigation tabs, timeframe toggles, and modals.
- `styles.css` — Modern institutional blue and white styling, live beacon indicator, price tick animations, and responsive layout.
- `app.js` — Client-side state machine, Kelly calculator, watchlist manager, and dynamic live Polymarket renderer.
- `live_polymarket_engine.py` — Real-time Polymarket Gamma API extraction engine.
- `server.py` — Python backend server with REST endpoints (`/api/markets`, `/api/live-sync`, `/api/status`, `/api/scan`).
- `polymarket_data.json` — 210-market structured live alpha database.
- `start_terminal.bat` — Single-click launcher for Windows.
- `push_to_github.bat` — Dual-sync script for `kpointpredict` and `KPOINTINVESTANDTRADE1`.

---

*Attribution:*
**KPOINT made this one. Not financial advice the risk is yours and yours only.**
