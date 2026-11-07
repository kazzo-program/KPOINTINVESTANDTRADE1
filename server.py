#!/usr/bin/env python3
"""
KPOINT EQUITIES ALPHA // INSTITUTIONAL HEDGE FUND STOCK TERMINAL
100% Stock-Focused Backend Server with Real-Time Yahoo Finance API Integration

Features:
- Live Yahoo Finance Quote Ingestion (/api/yahoo/quotes)
- Live Yahoo Finance Equities News Ingestion (/api/yahoo/news)
- Complete coverage of Top 20 US Stocks, Top 20 UK Stocks, and High Risers
- In-memory intelligent caching with TTL to prevent rate limiting
- Zero external dependencies (uses standard library http.server, urllib, json, xml)
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from http.server import HTTPServer, SimpleHTTPRequestHandler
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

PORT = 8080
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caching storage
QUOTES_CACHE = {}
QUOTES_CACHE_TIMESTAMP = 0
NEWS_CACHE = []
NEWS_CACHE_TIMESTAMP = 0
CACHE_TTL_SECONDS = 15

# Symbols coverage
US_SYMBOLS = [
    "NVDA", "MSFT", "PLTR", "AMZN", "AAPL", "META", "AVGO", "TSLA",
    "LLY", "VRT", "CEG", "JPM", "BRK-B", "TSM", "GE", "LMT", "AMD",
    "NOW", "XOM", "GOOGL"
]

UK_SYMBOLS = [
    "RR.L", "AZN.L", "BA.L", "SHEL.L", "ARM", "BARC.L", "HSBA.L", "REL.L",
    "RIO.L", "III.L", "LSEG.L", "ULVR.L", "GSK.L", "FLTR.L", "NXT.L",
    "GLEN.L", "BP.L", "CPG.L", "AHT.L", "IHG.L"
]

RISER_SYMBOLS = [
    "PLTR", "APP", "MSTR", "ALAB", "IONQ", "RKLB", "VRT", "NVDA",
    "CEG", "HOOD", "VKTX", "CLS", "AXON", "NET", "SMCI", "ANET"
]

ALL_TRACKED_SYMBOLS = list(dict.fromkeys(US_SYMBOLS + UK_SYMBOLS + RISER_SYMBOLS))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch_single_quote(symbol):
    """Fetch live quote from Yahoo Finance v8 chart API."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?interval=1d&range=5d"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode("utf-8"))
            result = data.get("chart", {}).get("result", [])
            if not result:
                return None
            meta = result[0].get("meta", {})
            current_price = meta.get("regularMarketPrice")
            prev_close = meta.get("chartPreviousClose") or meta.get("previousClose") or current_price
            
            if current_price is None:
                return None
                
            change = current_price - prev_close if prev_close else 0.0
            change_percent = (change / prev_close * 100.0) if prev_close else 0.0
            
            return {
                "symbol": symbol,
                "price": round(current_price, 2),
                "previousClose": round(prev_close, 2) if prev_close else round(current_price, 2),
                "change": round(change, 2),
                "changePercent": round(change_percent, 2),
                "dayHigh": round(meta.get("regularMarketDayHigh", current_price), 2),
                "dayLow": round(meta.get("regularMarketDayLow", current_price), 2),
                "volume": meta.get("regularMarketVolume", 0),
                "currency": meta.get("currency", "USD"),
                "exchange": meta.get("exchangeName", "US"),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
    except Exception as e:
        return None

def fetch_all_quotes(symbols=None):
    """Fetch quotes for symbols in parallel with intelligent caching."""
    global QUOTES_CACHE, QUOTES_CACHE_TIMESTAMP
    now = time.time()
    
    target_symbols = symbols or ALL_TRACKED_SYMBOLS
    
    # Return cache if still fresh and covers target symbols
    if (now - QUOTES_CACHE_TIMESTAMP < CACHE_TTL_SECONDS) and all(s in QUOTES_CACHE for s in target_symbols):
        return {s: QUOTES_CACHE[s] for s in target_symbols if s in QUOTES_CACHE}
        
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(fetch_single_quote, target_symbols))
        
    for res in results:
        if res:
            QUOTES_CACHE[res["symbol"]] = res
            
    QUOTES_CACHE_TIMESTAMP = now
    return {s: QUOTES_CACHE[s] for s in target_symbols if s in QUOTES_CACHE}

def fetch_yahoo_stock_news(symbols=None):
    """Fetch real-time stock news from Yahoo Finance RSS feeds."""
    global NEWS_CACHE, NEWS_CACHE_TIMESTAMP
    now = time.time()
    
    if (now - NEWS_CACHE_TIMESTAMP < CACHE_TTL_SECONDS * 2) and NEWS_CACHE:
        return NEWS_CACHE
        
    sample_symbols = "NVDA,MSFT,AAPL,PLTR,TSLA,AMZN,META,GOOGL,RR.L,AZN.L"
    urls = [
        f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={sample_symbols}&region=US&lang=en-US",
        "https://finance.yahoo.com/news/rssindex"
    ]
    
    all_news = []
    seen_titles = set()
    
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=4) as response:
                xml_data = response.read()
                root = ET.fromstring(xml_data)
                for item in root.findall(".//item")[:15]:
                    title = item.findtext("title", "").strip()
                    link = item.findtext("link", "").strip()
                    pub_date = item.findtext("pubDate", "").strip()
                    desc = item.findtext("description", "").strip()
                    
                    if title and title not in seen_titles:
                        seen_titles.add(title)
                        
                        # Tag relevant stock symbol
                        matched_symbol = "GENERAL"
                        for sym in ALL_TRACKED_SYMBOLS:
                            if sym.replace(".L", "").lower() in title.lower() or sym.replace(".L", "").lower() in desc.lower():
                                matched_symbol = sym
                                break
                                
                        all_news.append({
                            "source": "Yahoo Finance",
                            "symbol": matched_symbol,
                            "title": title,
                            "url": link,
                            "published": pub_date,
                            "snippet": desc[:160] + "..." if len(desc) > 160 else desc,
                            "sentiment": "BULLISH" if any(w in title.lower() for w in ["soars", "jumps", "rally", "high", "buy", "gain", "surges", "upgrade"]) else ("BEARISH" if any(w in title.lower() for w in ["falls", "drops", "slumps", "sell", "cuts", "crash"]) else "CATALYST")
                        })
        except Exception:
            pass
            
    if all_news:
        NEWS_CACHE = all_news
        NEWS_CACHE_TIMESTAMP = now
        
    return NEWS_CACHE

class StockTerminalHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/api/status":
            self.send_json_response({
                "status": "ONLINE",
                "engine": "KPOINT EQUITIES ALPHA // YAHOO FINANCE LIVE FEED",
                "coverage": {
                    "total_stocks": len(ALL_TRACKED_SYMBOLS),
                    "us_stocks": len(US_SYMBOLS),
                    "uk_stocks": len(UK_SYMBOLS),
                    "high_risers": len(RISER_SYMBOLS)
                },
                "yahoo_api_sync": "CONNECTED",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "port": PORT
            })
            return

        if parsed.path == "/api/yahoo/quotes":
            sym_param = params.get("symbols", [None])[0]
            symbols_to_fetch = [s.strip().upper() for s in sym_param.split(",")] if sym_param else ALL_TRACKED_SYMBOLS
            quotes = fetch_all_quotes(symbols_to_fetch)
            self.send_json_response({
                "status": "success",
                "source": "Yahoo Finance API (v8)",
                "count": len(quotes),
                "quotes": quotes,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        if parsed.path == "/api/yahoo/news":
            news = fetch_yahoo_stock_news()
            self.send_json_response({
                "status": "success",
                "source": "Yahoo Finance RSS Equities Wire",
                "count": len(news),
                "items": news,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        if parsed.path == "/api/stocks/us":
            quotes = fetch_all_quotes(US_SYMBOLS)
            self.send_json_response({
                "status": "success",
                "market": "US_TOP_20",
                "symbols": US_SYMBOLS,
                "quotes": quotes,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        if parsed.path == "/api/stocks/uk":
            quotes = fetch_all_quotes(UK_SYMBOLS)
            self.send_json_response({
                "status": "success",
                "market": "UK_TOP_20",
                "symbols": UK_SYMBOLS,
                "quotes": quotes,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        if parsed.path == "/api/stocks/high-risers":
            quotes = fetch_all_quotes(RISER_SYMBOLS)
            self.send_json_response({
                "status": "success",
                "category": "HIGH_GROWTH_RISERS",
                "symbols": RISER_SYMBOLS,
                "quotes": quotes,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path in ["/api/yahoo/sync", "/api/scan"]:
            quotes = fetch_all_quotes(ALL_TRACKED_SYMBOLS)
            news = fetch_yahoo_stock_news()
            self.send_json_response({
                "status": "success",
                "message": "Real-time Yahoo Finance stock quotes and equities news synchronized.",
                "synced_quotes_count": len(quotes),
                "synced_news_count": len(news),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            return

        self.send_error(404, "Endpoint Not Found")

    def send_json_response(self, data, status_code=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, StockTerminalHandler)
    print("=" * 72)
    print("  KPOINT EQUITIES ALPHA // INSTITUTIONAL HEDGE FUND STOCK TERMINAL")
    print(f"  URL: http://localhost:{PORT}")
    print("  Live Data Provider: Yahoo Finance API (v8)")
    print("  Stock Coverage: Top 20 US Stocks, Top 20 UK Stocks, High Risers")
    print("  API Endpoints:")
    print(f"    - GET  http://localhost:{PORT}/api/status")
    print(f"    - GET  http://localhost:{PORT}/api/yahoo/quotes")
    print(f"    - GET  http://localhost:{PORT}/api/yahoo/news")
    print(f"    - POST http://localhost:{PORT}/api/yahoo/sync")
    print("=" * 72)
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
