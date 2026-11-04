# KPOINT // Polymarket Macro Alpha Terminal

An institutional-grade prediction market intelligence terminal built with a crisp **Blue and White** interface. The terminal analyzes the top 10 largest markets on Polymarket across **Politics**, **Finance**, **Crypto**, **Sport**, and **Major UK & European Football Tournaments** (**Premier League**, **La Liga**, and **Bundesliga**) across **Day (24H)**, **Week (7D)**, and **Month (30D)** timeframes.

> *"KPOINT made this one. Not financial advice the risk is yours and yours only."*

---

## ⚡ Core Features

1. **Executive Blue & White Fintech UI**:
   - High-contrast, clean royal navy and pure white aesthetic designed for professional hedge fund desks and retail prediction market participants.
   - Interactive live odds tickers, probability fills, and responsive layouts across desktop, tablet, and mobile.

2. **210 Comprehensive Polymarket Markets**:
   - **🏛️ Politics** (Day 10, Week 10, Month 10 = 30 markets)
   - **💰 Finance** (Day 10, Week 10, Month 10 = 30 markets)
   - **🪙 Crypto** (Day 10, Week 10, Month 10 = 30 markets)
   - **🏆 Sport** (Day 10, Week 10, Month 10 = 30 markets)
   - **⚽ Football Major Tournaments**:
     - 🏴󠁧󠁢󠁥󠁮󠁧󠁿 **Premier League (UK)** (Day 10, Week 10, Month 10 = 30 markets)
     - 🇪🇸 **La Liga (Spain)** (Day 10, Week 10, Month 10 = 30 markets)
     - 🇩🇪 **Bundesliga (Germany)** (Day 10, Week 10, Month 10 = 30 markets)

3. **Macro Hedge Fund Advisory Engine**:
   - **Explicit Recommendation**: Direct `BET YES` or `BET NO` advice based on expected value (EV+) calculations.
   - **Conviction & Confidence**: Scoring from 75% to 96% with quantified EV edge (e.g. `+14.6% EV+`).
   - **Macro Strategy Thesis**: Institutional breakdowns detailing order book flow, structural supply/demand dynamics, interest rate transmission, and regulatory realities.
   - **Verified News Catalysts**: Breaking news headlines with source attribution (Bloomberg, Reuters, Financial Times, CoinDesk, Fabrizio Romano, Sky Sports, Kicker, Opta) and catalyst impact tags.
   - **Social Media Radar**: Quantified sentiment percentage, platform velocity tracking (X / Twitter, Reddit, Telegram), whale orderbook accumulation alerts, and smart money vs. retail positioning.
   - **Execution & Risk Mitigation**: Precise profit exit targets (e.g. `Target: $0.88 (+23.9%)`), stop-losses, and trailing risk limits.

4. **Advanced Analytical Tools**:
   - **🧮 Kelly Criterion Position Sizer**: Computes mathematically optimal stake allocations to maximize compound growth while protecting against drawdown.
   - **📡 Macro Alpha Radar**: Cross-sector sentiment heatmap and whale volume tracking.
   - **⭐ Interactive Watchlist**: Track high-conviction opportunities with local persistence.
   - **📊 One-Click CSV Alpha Export**: Download market datasets and hedge fund memos for offline quantitative analysis.

---

## 🚀 How to Run

### Option 1: Double-Click Launcher
Double-click `start_terminal.bat` to launch the Python server on port 8080 and open the terminal in your browser automatically.

### Option 2: Command Line
```powershell
python server.py
```
Then navigate in your browser to:
[http://localhost:8080](http://localhost:8080)

### Option 3: Standalone Offline Mode
Open `index.html` directly in any web browser. The app includes client-side fallback parsing that runs seamlessly without server dependencies.

---

## 🏛️ Project Structure

- `index.html` — Blue and white structural frontend with all navigation tabs, timeframe toggles, and modals.
- `styles.css` — Modern institutional blue and white styling, glass cards, and animations.
- `app.js` — Client-side state machine, Kelly calculator, watchlist manager, and dynamic card renderer.
- `server.py` — Python backend server with REST endpoints (`/api/markets`, `/api/status`, `/api/scan`).
- `polymarket_data.json` — 210-market structured alpha database.
- `start_terminal.bat` — Single-click launcher for Windows.

---

*Attribution:*
**KPOINT made this one. Not financial advice the risk is yours and yours only.**
