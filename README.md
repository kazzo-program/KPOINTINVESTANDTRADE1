# KPoint Equities Alpha // Institutional Macro Stock Terminal

> **100% Equities Focus // Macro Hedge Fund News Strategy // Powered by Yahoo Finance API**  
> Complete coverage of **Top 20 US Stocks**, **Top 20 UK Stocks**, and **High Risers** (rapid value acceleration & hyper-growth).  
> Incorporates real-time price quotes, daily changes, and breaking equities news syndicated directly from **Yahoo Finance API (v8)**.

---

## ⚡ Key Highlights & Architecture

### 1. 100% Focused on Stocks & Equities
- **Zero non-stock instruments**: Completely free of XAUUSD, BTCUSD, CFDs, futures, crypto, or commodities. 100% dedicated to equities investing and trading.
- **Industry & Sector for Every Stock**: Every equity displays a color-coded industry badge (*Semiconductors & AI*, *Enterprise Software*, *Cloud Infrastructure*, *Aerospace & Defense*, *Nuclear & Clean Baseload*, *Biopharma*, *Financials*, *Critical Mining*).
- **Interactive Industry Filter**: Dedicated dropdown on every stock tab to isolate specific industries.

### 2. Live Yahoo Finance API (v8) Integration
- **Real-Time Quotes**: Ingests `regularMarketPrice`, `chartPreviousClose`, `regularMarketVolume`, and daily percentage changes from Yahoo Finance v8 chart API.
- **Live Equities News Wire**: Syndicates real-time breaking stock headlines, analyst ratings revisions, and SEC regulatory filings from Yahoo Finance RSS feeds.
- **Continuous Streaming Ticker**: Micro-tick engine runs sub-second bid/ask price simulations with green (`price-flash-green`) and red (`price-flash-red`) flash animations.
- **One-Click Refresh**: Prominent `[⚡ REFRESH YAHOO FINANCE]` button in the top navigation.

### 3. Dedicated Stock Coverage
- 🇺🇸 **Top 20 US Stocks**: `NVDA`, `MSFT`, `PLTR`, `AMZN`, `AAPL`, `META`, `AVGO`, `TSLA`, `LLY`, `VRT`, `CEG`, `JPM`, `BRK.B`, `TSM`, `GE`, `LMT`, `AMD`, `NOW`, `XOM`, `GOOGL`.
- 🇬🇧 **Top 20 UK Stocks**: `RR.L`, `AZN.L`, `BA.L`, `SHEL.L`, `ARM`, `BARC.L`, `HSBA.L`, `REL.L`, `RIO.L`, `III.L`, `LSEG.L`, `ULVR.L`, `GSK.L`, `FLTR.L`, `NXT.L`, `GLEN.L`, `BP.L`, `CPG.L`, `AHT.L`, `IHG.L`.
- 🚀 **High Risers (High Growth & Rising Value)**: `PLTR`, `APP`, `MSTR`, `ALAB`, `IONQ`, `RKLB`, `VRT`, `NVDA`, `CEG`, `HOOD`, `VKTX`, `CLS`, `AXON`, `NET`, `SMCI`, `ANET`.

### 4. Multi-Timeframe Sections (Week, Month, Year)
- Every stock tab features a side-by-side **Multi-Timeframe Showcase Leaderboard**:
  - ⚡ **Top of the Week**: 5-day breakout velocity (+12% to +48%) and breaking news momentum.
  - 🚀 **Top of the Month**: 30-day post-earnings acceleration and institutional accumulation (+25% to +88%).
  - 👑 **Top of the Year**: Secular multi-quarter compounders (+90% to +420% YTD).
- Interactive toolbar filter chips (`All Top 20`, `Top of Week`, `Top of Month`, `Top of Year`) to dynamically sort and re-rank the main table and cards view.

### 5. Pitch Black Institutional Terminal Interface
- Deep obsidian black theme (`#010204`, `#060910`), high-contrast cyan and emerald glows, monospace data grids, and one-click Theme Switcher (`⬛ BLACK INTERFACE` / `🔷 DEEP BLUE`).

---

## 🚀 How to Run

### Option 1: Double-Click Launcher (Standalone)
Simply double-click [`index.html`](file:///c:/Users/kb90G/OneDrive/quanto2/index.html) in your browser (Chrome, Edge, Brave). All stock rankings, live micro-ticks, timeframe showcases, and filters work client-side out-of-the-box.

### Option 2: Run Local Python Server (Recommended for Live Yahoo Sync)
Open PowerShell or Command Prompt in this folder and execute:

```powershell
python server.py
```

Then visit:
```
http://localhost:8080
```

---

## 📁 File Structure

```
quanto2/
├── index.html        # Pitch black stock terminal interface with 5 core tabs
├── styles.css        # Institutional pitch-black styling, data grids, and tick animations
├── app.js            # Stock datasets, Yahoo Finance API engine, and live tick simulator
├── server.py         # Python REST server with Yahoo Finance quote & news proxy
├── push_to_github.bat# One-click GitHub synchronization script
└── README.md         # Operational documentation
```
