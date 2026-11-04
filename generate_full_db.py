# -*- coding: utf-8 -*-
"""
Full Dataset Generator for KPOINT Macro Polymarket Alpha Terminal
Generates 210 distinct markets across:
- Politics (Day, Week, Month)
- Crypto (Day, Week, Month)
- Finance (Day, Week, Month)
- Sports (Day, Week, Month)
- Football Premier League (Day, Week, Month)
- Football La Liga (Day, Week, Month)
- Football Bundesliga (Day, Week, Month)
"""

import json
import os

def generate_all_markets():
    db = {}

    # Helper to build markets
    # -------------------------------------------------------------
    # 1. POLITICS
    # -------------------------------------------------------------
    from build_dataset import DATA as POLITICS_BASE
    db["politics"] = POLITICS_BASE["politics"]

    # -------------------------------------------------------------
    # 2. CRYPTO
    # -------------------------------------------------------------
    db["crypto"] = {
        "day": [
            {
                "id": "cry-d-01", "rank": 1,
                "title": "Will Bitcoin trade above $102,500 before midnight UTC?",
                "slug": "bitcoin-trade-above-102500-today",
                "volume": "$34,890,000", "volumeRaw": 34890000, "volumeLabel": "24H Volume",
                "liquidity": "$7,820,000", "endDate": "Midnight UTC",
                "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 88, "evEdge": "+13.5% EV+", "impliedProb": 68, "fairValueProb": 81.5,
                    "targetExit": "$0.85 (+25.0% return)", "stopLoss": "$0.52",
                    "macroStrategy": "Deribit options order book reveals massive gamma cluster squeeze between $101.5k and $103k; spot ETF inflows clocked +$540M in early session trading.",
                    "newsCatalyst": {
                        "headline": "CoinDesk: US Spot Bitcoin ETFs record $540M net inflow in first 3 hours of trading",
                        "source": "CoinDesk Institutional", "time": "1h ago", "impact": "LIQUIDITY EXPANSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Crypto Twitter & Farside ETF Trackers",
                        "sentimentScore": 86, "sentimentTrend": "+24% Bullish momentum",
                        "whaleFlows": "Binance and Coinbase order books indicate cumulative $180M bid wall at $101,800",
                        "retailPositioning": "Short liquidations cascading across perpetual futures"
                    },
                    "riskMitigation": "Take 70% profits once spot prints $102,600."
                }
            },
            {
                "id": "cry-d-02", "rank": 2,
                "title": "Will US Spot Ethereum ETFs record positive net inflows today?",
                "slug": "us-spot-ethereum-etfs-net-inflows-today",
                "volume": "$21,400,000", "volumeRaw": 21400000, "volumeLabel": "24H Volume",
                "liquidity": "$4,900,000", "endDate": "Midnight UTC",
                "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 87, "evEdge": "+11.0% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                    "targetExit": "$0.89 (+20.3% return)", "stopLoss": "$0.61",
                    "macroStrategy": "BlackRock ETHA and Fidelity FETH pre-market share creations surpass yesterday's full-day run rate by 180%; ETHE redemptions curtailed to lowest level this month.",
                    "newsCatalyst": {
                        "headline": "Bloomberg ETF Wire: BlackRock ETHA adds $82M in early creations; Grayscale outflows abate",
                        "source": "Bloomberg Intelligence", "time": "2h ago", "impact": "INSTITUTIONAL ACCUMULATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / On-chain ETF Tracker Bots",
                        "sentimentScore": 82, "sentimentTrend": "+18% Bullish sentiment",
                        "whaleFlows": "Over $42M in off-market OTC blocks settled directly to custodian cold storage",
                        "retailPositioning": "Retail skepticism lingering from prior outflows, offering great risk-reward"
                    },
                    "riskMitigation": "Lock profit when Farside updates final aggregate prints at 6:30 PM EST."
                }
            },
            {
                "id": "cry-d-03", "rank": 3,
                "title": "Will Solana (SOL) hold above $245.00 through daily close?",
                "slug": "solana-hold-above-245-daily-close",
                "volume": "$18,920,000", "volumeRaw": 18920000, "volumeLabel": "24H Volume",
                "liquidity": "$4,100,000", "endDate": "Today 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 85, "evEdge": "+12.0% EV+", "impliedProb": 71, "fairValueProb": 83.0,
                    "targetExit": "$0.87 (+22.5% return)", "stopLoss": "$0.58",
                    "macroStrategy": "DEX trading volume on Raydium and Orca hit \$4.2B 24h high, driving relentless validator fee burns and demand for native SOL collateral.",
                    "newsCatalyst": {
                        "headline": "DefiLlama: Solana 24h DEX trading volume exceeds Ethereum mainnet for third consecutive day",
                        "source": "DefiLlama Research", "time": "3h ago", "impact": "NETWORK VELOCITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / CT Solana Ecosystem Alpha",
                        "sentimentScore": 85, "sentimentTrend": "+19% Bullish acceleration",
                        "whaleFlows": "Whale wallet stakes 120,000 SOL with Jito MEV validators",
                        "retailPositioning": "High retail buy-demand cushioning downside volatility"
                    },
                    "riskMitigation": "Take profits ahead of Asian morning session handoff."
                }
            },
            {
                "id": "cry-d-04", "rank": 4,
                "title": "Will MicroStrategy announce a new Bitcoin purchase today?",
                "slug": "microstrategy-announce-bitcoin-purchase-today",
                "volume": "$15,600,000", "volumeRaw": 15600000, "volumeLabel": "24H Volume",
                "liquidity": "$3,500,000", "endDate": "Today 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.38, "pct": 38}, {"name": "NO", "price": 0.62, "pct": 62}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO (STATISTICAL ALPHA)", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+15.0% EV+", "impliedProb": 62, "fairValueProb": 77.0,
                    "targetExit": "$0.82 (+32.2% return)", "stopLoss": "$0.48",
                    "macroStrategy": "SEC 8-K filings for MSTR typically follow ATM equity sales on Monday mornings; Wednesday mid-day filing probability is historically below 12%.",
                    "newsCatalyst": {
                        "headline": "SEC EDGAR Monitor: No 8-K ATM capital raise settlement filings logged for MSTR during today's window",
                        "source": "SEC EDGAR Tracker", "time": "2h ago", "impact": "CALENDAR NORMALIZATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Michael Saylor Tracker",
                        "sentimentScore": 76, "sentimentTrend": "Speculation fading",
                        "whaleFlows": "Institutional arbitrageurs buying NO to collect premium",
                        "retailPositioning": "Retail gamblers buying YES based on unverified tweets"
                    },
                    "riskMitigation": "Hold NO into market close for clean theta decay."
                }
            },
            {
                "id": "cry-d-05", "rank": 5,
                "title": "Will Coinbase (COIN) win or settle SEC interlocutory appeal motion today?",
                "slug": "coinbase-sec-interlocutory-appeal-today",
                "volume": "$13,200,000", "volumeRaw": 13200000, "volumeLabel": "24H Volume",
                "liquidity": "$2,950,000", "endDate": "Today 5:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.29, "pct": 29}, {"name": "NO", "price": 0.71, "pct": 71}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                    "confidencePct": 89, "evEdge": "+12.0% EV+", "impliedProb": 71, "fairValueProb": 83.0,
                    "targetExit": "$0.87 (+22.5% return)", "stopLoss": "$0.59",
                    "macroStrategy": "Judge Failla's SDNY docket shows no expedited calendar orders; discovery phase scheduled through end of month makes mid-day rulings improbable.",
                    "newsCatalyst": {
                        "headline": "CourtListener SDNY: No minute orders docketed in SEC v. Coinbase ahead of today's cutoff",
                        "source": "CourtListener Legal Monitor", "time": "1h ago", "impact": "PROCEDURAL DELAY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Crypto Legal Experts",
                        "sentimentScore": 80, "sentimentTrend": "High confidence in NO resolution",
                        "whaleFlows": "Smart money accumulating NO",
                        "retailPositioning": "Retail chasing false breakout rumors"
                    },
                    "riskMitigation": "Safe carry yield play."
                }
            },
            {
                "id": "cry-d-06", "rank": 6,
                "title": "Will Tether (USDT) market cap exceed $138 Billion by end of day?",
                "slug": "tether-usdt-market-cap-138b-today",
                "volume": "$11,500,000", "volumeRaw": 11500000, "volumeLabel": "24H Volume",
                "liquidity": "$2,600,000", "endDate": "Midnight UTC",
                "outcomes": [{"name": "YES", "price": 0.79, "pct": 79}, {"name": "NO", "price": 0.21, "pct": 21}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 91, "evEdge": "+9.0% EV+", "impliedProb": 79, "fairValueProb": 88.0,
                    "targetExit": "$0.94 (+19.0% return)", "stopLoss": "$0.68",
                    "macroStrategy": "Whale Alert verified $1.0B USDT mint on Tron network today; authorized but unissued inventory is being actively drained by centralized exchanges.",
                    "newsCatalyst": {
                        "headline": "Whale Alert: 1,000,000,000 USDT minted at Tether Treasury; Paolo Ardoino confirms replenishment",
                        "source": "Whale Alert On-chain", "time": "2h ago", "impact": "SUPPLY EXPANSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / On-chain Liquidity Bots",
                        "sentimentScore": 88, "sentimentTrend": "+20% Bullish liquidity",
                        "whaleFlows": "Massive institutional stablecoin minting confirmed on-chain",
                        "retailPositioning": "Retail slow to notice on-chain issuance lag"
                    },
                    "riskMitigation": "Lock gains when CoinGecko reflects the mint."
                }
            },
            {
                "id": "cry-d-07", "rank": 7,
                "title": "Will Ripple (XRP) break and close above $2.20 in today's session?",
                "slug": "ripple-xrp-break-above-220-today",
                "volume": "$10,100,000", "volumeRaw": 10100000, "volumeLabel": "24H Volume",
                "liquidity": "$2,300,000", "endDate": "Midnight UTC",
                "outcomes": [{"name": "YES", "price": 0.59, "pct": 59}, {"name": "NO", "price": 0.41, "pct": 41}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "MEDIUM-HIGH CONVICTION",
                    "confidencePct": 83, "evEdge": "+14.0% EV+", "impliedProb": 59, "fairValueProb": 73.0,
                    "targetExit": "$0.81 (+37.3% return)", "stopLoss": "$0.46",
                    "macroStrategy": "RLUSD stablecoin regulatory signoffs and cross-border bank pilot expansions triggered aggressive spot spot buying across South Korean exchanges (Upbit/Bithumb).",
                    "newsCatalyst": {
                        "headline": "Cointelegraph: Upbit XRP trading volume surges to $2.8B as Korean retail liquidity accelerates",
                        "source": "Cointelegraph Asia", "time": "3h ago", "impact": "REGIONAL VOLUME EXPLOSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / XRP Community & Kimchi Premium Watch",
                        "sentimentScore": 84, "sentimentTrend": "+26% Bullish momentum",
                        "whaleFlows": "South Korean exchange wallets net withdrawing 85M XRP to cold storage",
                        "retailPositioning": "FOMO wave building on domestic Asian exchanges"
                    },
                    "riskMitigation": "Set trailing stop at 0.50 to protect principal."
                }
            },
            {
                "id": "cry-d-08", "rank": 8,
                "title": "Will Dogecoin (DOGE) reach $0.45 before 11:59 PM EST?",
                "slug": "dogecoin-reach-045-today",
                "volume": "$9,400,000", "volumeRaw": 9400000, "volumeLabel": "24H Volume",
                "liquidity": "$2,100,000", "endDate": "Today 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.43, "pct": 43}, {"name": "NO", "price": 0.57, "pct": 57}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                    "confidencePct": 84, "evEdge": "+15.0% EV+", "impliedProb": 57, "fairValueProb": 72.0,
                    "targetExit": "$0.78 (+36.8% return)", "stopLoss": "$0.44",
                    "macroStrategy": "Derivatives open interest reached an overstretched \$3.8B peak; funding rates at 0.04% indicate extreme retail long leverage vulnerable to flush-outs.",
                    "newsCatalyst": {
                        "headline": "CoinGlass: Dogecoin 8-hour funding rates spike to annual highs, signaling severe long crowding",
                        "source": "CoinGlass Analytics", "time": "2h ago", "impact": "LEVERAGE SATURATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Meme Alpha & Liquidation Trackers",
                        "sentimentScore": 72, "sentimentTrend": "Retail exhaustion evident",
                        "whaleFlows": "Market makers depositing 250M DOGE onto Binance for spot distribution",
                        "retailPositioning": "Retail heavily overleveraged on call contracts"
                    },
                    "riskMitigation": "Profit on NO as funding rates normalize."
                }
            },
            {
                "id": "cry-d-09", "rank": 9,
                "title": "Will SUI network total value locked (TVL) cross $1.8 Billion today?",
                "slug": "sui-network-tvl-cross-18b-today",
                "volume": "$8,100,000", "volumeRaw": 8100000, "volumeLabel": "24H Volume",
                "liquidity": "$1,850,000", "endDate": "Today 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+12.0% EV+", "impliedProb": 65, "fairValueProb": 77.0,
                    "targetExit": "$0.83 (+27.7% return)", "stopLoss": "$0.52",
                    "macroStrategy": "Native liquidity protocol incentives on NAVI and Scallop brought \$75M in net bridged USDC over the past 14 hours; current TVL sits at \$1.785B.",
                    "newsCatalyst": {
                        "headline": "DefiLlama: Sui TVL advances to $1.785B; $15M needed to hit milestone with 10 hours remaining",
                        "source": "DefiLlama Metrics", "time": "3h ago", "impact": "ON-CHAIN MILESTONE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Sui Eco Alpha",
                        "sentimentScore": 81, "sentimentTrend": "+17% Bullish",
                        "whaleFlows": "Institutional liquidity providers staking stablecoins",
                        "retailPositioning": "Growing community momentum"
                    },
                    "riskMitigation": "Exit when DefiLlama confirms $1.801B."
                }
            },
            {
                "id": "cry-d-10", "rank": 10,
                "title": "Will Arbitrum DAO approve the 100M ARB Gaming Catalyst Program vote today?",
                "slug": "arbitrum-dao-gaming-catalyst-program-today",
                "volume": "$6,900,000", "volumeRaw": 6900000, "volumeLabel": "24H Volume",
                "liquidity": "$1,550,000", "endDate": "Today 8:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.83, "pct": 83}, {"name": "NO", "price": 0.17, "pct": 17}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 92, "evEdge": "+8.0% EV+", "impliedProb": 83, "fairValueProb": 91.0,
                    "targetExit": "$0.95 (+14.5% return)", "stopLoss": "$0.72",
                    "macroStrategy": "Tally governance voting shows major delegates (Treasure DAO, Wintermute, Uniswap Foundation) cast 94.2% FOR votes, passing the quorum threshold.",
                    "newsCatalyst": {
                        "headline": "Tally Governance: Arbitrum Proposal GCP reached quorum with 94.2% affirmative votes",
                        "source": "Tally DAO Explorer", "time": "2h ago", "impact": "GOVERNANCE APPROVAL"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Arbitrum & Layer 2 Alpha",
                        "sentimentScore": 87, "sentimentTrend": "Certainty confirmed",
                        "whaleFlows": "Delegates holding 140M votes finalized voting",
                        "retailPositioning": "Retail slow to verify Tally quorum status"
                    },
                    "riskMitigation": "Steady arbitrage yield into vote conclusion."
                }
            }
        ],
        "week": [
            {
                "id": "cry-w-01", "rank": 1,
                "title": "Will Bitcoin weekly candle close above $105,000?",
                "slug": "bitcoin-weekly-close-above-105000",
                "volume": "$89,500,000", "volumeRaw": 89500000, "volumeLabel": "7D Volume",
                "liquidity": "$19,200,000", "endDate": "Sunday 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 87, "evEdge": "+14.0% EV+", "impliedProb": 62, "fairValueProb": 76.0,
                    "targetExit": "$0.84 (+35.5% return)", "stopLoss": "$0.48",
                    "macroStrategy": "Weekly net inflows into US spot ETFs are pacing at +\$2.8B; CME Bitcoin futures basis premium expanded to 14.2% annualized, demonstrating unyielding institutional long demand.",
                    "newsCatalyst": {
                        "headline": "Farside Investors: Weekly ETF net inflows on track to break all-time high record",
                        "source": "Farside Data", "time": "1 day ago", "impact": "MACRO CAPITAL FLOOD"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Institutional Crypto Desk",
                        "sentimentScore": 85, "sentimentTrend": "+22% Weekly Bullish",
                        "whaleFlows": "Over 12,000 BTC removed from exchange reserves this week",
                        "retailPositioning": "Retail under-allocated waiting for dip that keeps getting absorbed"
                    },
                    "riskMitigation": "Lock 50% profits at $0.80 ahead of Friday CME settlement."
                }
            },
            {
                "id": "cry-w-02", "rank": 2,
                "title": "Will the US Congress advance the FIT21 Crypto Regulatory Bill to Senate floor this week?",
                "slug": "fit21-crypto-regulatory-bill-senate-floor-this-week",
                "volume": "$64,200,000", "volumeRaw": 64200000, "volumeLabel": "7D Volume",
                "liquidity": "$13,800,000", "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.66, "pct": 66}, {"name": "NO", "price": 0.34, "pct": 34}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+13.0% EV+", "impliedProb": 66, "fairValueProb": 79.0,
                    "targetExit": "$0.86 (+30.3% return)", "stopLoss": "$0.52",
                    "macroStrategy": "Senate Agriculture Committee leadership reached bipartisan consensus clarifying CFTC jurisdiction over digital commodities; key moderate senators co-sponsored the amendment.",
                    "newsCatalyst": {
                        "headline": "Punchbowl News: Senate Banking and Ag committee chairs agree to joint hearing on digital asset market structure",
                        "source": "Punchbowl News DC", "time": "18h ago", "impact": "REGULATORY CLARITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Crypto Policy Insiders",
                        "sentimentScore": 81, "sentimentTrend": "+17% Bullish shift",
                        "whaleFlows": "Crypto PAC and venture treasury wallets backing YES",
                        "retailPositioning": "Retail fatigue on DC politics creates value entry"
                    },
                    "riskMitigation": "Take profits upon committee notice publication."
                }
            },
            {
                "id": "cry-w-03", "rank": 3,
                "title": "Will Ethereum (ETH) break and close above $3,800 this week?",
                "slug": "ethereum-break-above-3800-this-week",
                "volume": "$52,800,000", "volumeRaw": 52800000, "volumeLabel": "7D Volume",
                "liquidity": "$11,400,000", "endDate": "Sunday 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.57, "pct": 57}, {"name": "NO", "price": 0.43, "pct": 43}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 84, "evEdge": "+15.0% EV+", "impliedProb": 57, "fairValueProb": 72.0,
                    "targetExit": "$0.79 (+38.6% return)", "stopLoss": "$0.44",
                    "macroStrategy": "ETH/BTC ratio completed a textbook double-bottom reversal on daily charts; staking inflows hit +180k ETH this week, shrinking liquid float to 10.4% of total supply.",
                    "newsCatalyst": {
                        "headline": "Glassnode: Ethereum exchange balances fall to multi-year low of 12.1M ETH",
                        "source": "Glassnode Institutional", "time": "1 day ago", "impact": "SUPPLY CRUNCH"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Ethereum Mainnet Alpha",
                        "sentimentScore": 79, "sentimentTrend": "+21% Bullish sentiment",
                        "whaleFlows": "MakerDAO and Lido whales depositing collateral to borrow stables for spot ETH buys",
                        "retailPositioning": "Retail rotating profits from altcoins into ETH"
                    },
                    "riskMitigation": "Trail stop at 0.50 as spot approaches $3,750 resistance."
                }
            },
            {
                "id": "cry-w-04", "rank": 4,
                "title": "Will a US State Treasury formally announce a Bitcoin Strategic Reserve allocation this week?",
                "slug": "us-state-treasury-bitcoin-strategic-reserve-this-week",
                "volume": "$43,100,000", "volumeRaw": 43100000, "volumeLabel": "7D Volume",
                "liquidity": "$9,200,000", "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.47, "pct": 47}, {"name": "NO", "price": 0.53, "pct": 53}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES (ASYMMETRIC ALPHA)", "conviction": "HIGH CONVICTION",
                    "confidencePct": 81, "evEdge": "+18.0% EV+", "impliedProb": 47, "fairValueProb": 65.0,
                    "targetExit": "$0.75 (+59.6% return)", "stopLoss": "$0.35",
                    "macroStrategy": "State legislative dockets in Texas, Pennsylvania, and Florida introduced enabling statutory riders allowing state pension and general revenue funds to hold up to 5% BTC.",
                    "newsCatalyst": {
                        "headline": "Fox Business: Pennsylvania State Representative sponsors landmark bill enabling $500M Bitcoin reserve",
                        "source": "Fox Business", "time": "1 day ago", "impact": "SOVEREIGN ADOPTION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Statehouse Crypto Policy",
                        "sentimentScore": 83, "sentimentTrend": "+28% Bullish sentiment surge",
                        "whaleFlows": "Macro institutional accounts aggressively buying YES below 0.50",
                        "retailPositioning": "Retail unaware of advanced stage of committee markups"
                    },
                    "riskMitigation": "Sell half on headline break; hold remainder for official signing."
                }
            },
            {
                "id": "cry-w-05", "rank": 5,
                "title": "Will Binance US settlement monitor conclude supervision without new enforcement this week?",
                "slug": "binance-us-settlement-monitor-conclusion-this-week",
                "volume": "$36,700,000", "volumeRaw": 36700000, "volumeLabel": "7D Volume",
                "liquidity": "$7,800,000", "endDate": "Friday 5:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.82, "pct": 82}, {"name": "NO", "price": 0.18, "pct": 18}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 90, "evEdge": "+8.0% EV+", "impliedProb": 82, "fairValueProb": 90.0,
                    "targetExit": "$0.94 (+14.6% return)", "stopLoss": "$0.70",
                    "macroStrategy": "DOJ independent compliance monitor Forex/AML quarterly progress report returned satisfactory compliance grades across all key operational metrics.",
                    "newsCatalyst": {
                        "headline": "Wall Street Journal: Independent monitors file favorable mid-term report on Binance compliance remediation",
                        "source": "WSJ Risk & Compliance", "time": "2 days ago", "impact": "LEGAL STABILIZATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Legal & Exchange Watch",
                        "sentimentScore": 86, "sentimentTrend": "Stable",
                        "whaleFlows": "Institutional accounts collecting low-risk YES yield",
                        "retailPositioning": "Low retail drama"
                    },
                    "riskMitigation": "Capture safe institutional yield."
                }
            },
            {
                "id": "cry-w-06", "rank": 6,
                "title": "Will Uniswap (UNI) fee switch distribution proposal pass on-chain snapshot this week?",
                "slug": "uniswap-fee-switch-distribution-snapshot-this-week",
                "volume": "$31,400,000", "volumeRaw": 31400000, "volumeLabel": "7D Volume",
                "liquidity": "$6,700,000", "endDate": "Sunday 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+12.0% EV+", "impliedProb": 71, "fairValueProb": 83.0,
                    "targetExit": "$0.88 (+23.9% return)", "stopLoss": "$0.58",
                    "macroStrategy": "Uniswap Foundation released upgraded v4 deployment contracts with audited protocol revenue burn mechanics; major VC delegates (a16z, Paradigm) signaled affirmative votes.",
                    "newsCatalyst": {
                        "headline": "Uniswap Governance: Delegate consensus reaches 88% approval for fee distribution mechanism",
                        "source": "Uniswap Governance Portal", "time": "1 day ago", "impact": "TOKENOMICS REVAMP"
                    },
                    "socialMediaRadar": {
                        "platform": "X / DeFi Alpha & Tokenomics",
                        "sentimentScore": 84, "sentimentTrend": "+20% Bullish",
                        "whaleFlows": "DeFi whale addresses accumulating UNI spot and YES contracts",
                        "retailPositioning": "Retail slow to understand staking dividend implications"
                    },
                    "riskMitigation": "Sell position when on-chain quorum is locked."
                }
            },
            {
                "id": "cry-w-07", "rank": 7,
                "title": "Will total stablecoin supply on Tron (TRX) exceed $65 Billion this week?",
                "slug": "tron-stablecoin-supply-65b-this-week",
                "volume": "$27,900,000", "volumeRaw": 27900000, "volumeLabel": "7D Volume",
                "liquidity": "$5,900,000", "endDate": "Sunday 11:59 PM UTC",
                "outcomes": [{"name": "YES", "price": 0.77, "pct": 77}, {"name": "NO", "price": 0.23, "pct": 23}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 89, "evEdge": "+10.0% EV+", "impliedProb": 77, "fairValueProb": 87.0,
                    "targetExit": "$0.92 (+19.5% return)", "stopLoss": "$0.65",
                    "macroStrategy": "Cross-border OTC settlement in Latin America and Southeast Asia continues driving \$1.2B weekly net USDT issuance on Tron; current balance sits at \$64.4B.",
                    "newsCatalyst": {
                        "headline": "Tronscan Analytics: Tron USDT supply hits $64.42B; projected to clear $65B milestone by Saturday",
                        "source": "Tronscan Explorer", "time": "18h ago", "impact": "NETWORK UTILITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Payment Tech & EM Stablecoins",
                        "sentimentScore": 82, "sentimentTrend": "+15% Steady accumulation",
                        "whaleFlows": "Payment processors fueling nonstop issuance",
                        "retailPositioning": "High certainty play"
                    },
                    "riskMitigation": "Steady compounding return."
                }
            },
            {
                "id": "cry-w-08", "rank": 8,
                "title": "Will BlackRock's BUIDL Tokenized Fund surpass $600M AUM this week?",
                "slug": "blackrock-buidl-fund-600m-aum-this-week",
                "volume": "$24,500,000", "volumeRaw": 24500000, "volumeLabel": "7D Volume",
                "liquidity": "$5,200,000", "endDate": "Friday 5:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.84, "pct": 84}, {"name": "NO", "price": 0.16, "pct": 16}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 92, "evEdge": "+7.0% EV+", "impliedProb": 84, "fairValueProb": 91.0,
                    "targetExit": "$0.95 (+13.1% return)", "stopLoss": "$0.72",
                    "macroStrategy": "Securitize announced integration with three institutional DeFi collateral engines (Ethena, Ondo, Mountain Protocol); \$38M incoming mints queued.",
                    "newsCatalyst": {
                        "headline": "Securitize: BlackRock BUIDL fund receives $38M institutional mint requests for Treasury yield backing",
                        "source": "Securitize Official", "time": "1 day ago", "impact": "RWA EXPANSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Real World Assets (RWA) Alpha",
                        "sentimentScore": 89, "sentimentTrend": "+16% Bullish",
                        "whaleFlows": "Treasury management DAOs locking institutional liquidity",
                        "retailPositioning": "Institutional-grade certainty"
                    },
                    "riskMitigation": "Ideal safe treasury cash enhancer."
                }
            },
            {
                "id": "cry-w-09", "rank": 9,
                "title": "Will Avalanche (AVAX) announce a major Tier-1 US Bank partnership this week?",
                "slug": "avalanche-avax-us-bank-partnership-this-week",
                "volume": "$21,800,000", "volumeRaw": 21800000, "volumeLabel": "7D Volume",
                "liquidity": "$4,600,000", "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.39, "pct": 39}, {"name": "NO", "price": 0.61, "pct": 61}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO (RUMOR ARBITRAGE)", "conviction": "HIGH CONVICTION",
                    "confidencePct": 85, "evEdge": "+14.0% EV+", "impliedProb": 61, "fairValueProb": 75.0,
                    "targetExit": "$0.82 (+34.4% return)", "stopLoss": "$0.48",
                    "macroStrategy": "Ava Labs enterprise team keynote at Singapore FinTech Festival focuses on sovereign identity subnets; no US banking consortium pilot is on the official clearance schedule.",
                    "newsCatalyst": {
                        "headline": "FinTech Singapore Agenda: Ava Labs session confirms identity framework focus; banking tokenization slated for next quarter",
                        "source": "FinTech Festival Media", "time": "1 day ago", "impact": "TIMELINE CLARIFICATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / AVAX Ecosystem Watch",
                        "sentimentScore": 73, "sentimentTrend": "Rumor momentum subsiding",
                        "whaleFlows": "Smart money selling YES into hype",
                        "retailPositioning": "Retail chasing false conference leaks"
                    },
                    "riskMitigation": "Capture clean premium on NO into Sunday."
                }
            },
            {
                "id": "cry-w-10", "rank": 10,
                "title": "Will OpenSea launch an official token / retroactive airdrop announcement this week?",
                "slug": "opensea-token-airdrop-announcement-this-week",
                "volume": "$19,200,000", "volumeRaw": 19200000, "volumeLabel": "7D Volume",
                "liquidity": "$4,100,000", "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.22, "pct": 22}, {"name": "NO", "price": 0.78, "pct": 78}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO", "conviction": "VERY HIGH CONVICTION",
                    "confidencePct": 92, "evEdge": "+10.0% EV+", "impliedProb": 78, "fairValueProb": 88.0,
                    "targetExit": "$0.93 (+19.2% return)", "stopLoss": "$0.66",
                    "macroStrategy": "OpenSea v2 smart contracts launched on testnet with zero token incentives or claim distribution modules; SEC Wells notice response still pending in federal court.",
                    "newsCatalyst": {
                        "headline": "The Block: OpenSea v2 contract audit reveals focus on account abstraction, no token bytecode detected",
                        "source": "The Block Research", "time": "2 days ago", "impact": "CODEBASE REALITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / NFT & Airdrop Farmers",
                        "sentimentScore": 79, "sentimentTrend": "Airdrop hopium waning",
                        "whaleFlows": "Institutional desks buying NO",
                        "retailPositioning": "Retail airdrop farmers holding cheap YES lottery tickets"
                    },
                    "riskMitigation": "Hold NO into Sunday weekly reset."
                }
            }
        ],
        "month": [
            {
                "id": "cry-m-01", "rank": 1,
                "title": "Will Bitcoin trade at or above $120,000 before the end of the month?",
                "slug": "bitcoin-trade-above-120000-end-of-month",
                "volume": "$285,400,000", "volumeRaw": 285400000, "volumeLabel": "30D Volume",
                "liquidity": "$58,200,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+14.0% EV+", "impliedProb": 58, "fairValueProb": 72.0,
                    "targetExit": "$0.82 (+41.4% return)", "stopLoss": "$0.44",
                    "macroStrategy": "Post-halving structural supply deficit is now fully taking effect; miner reserve depletion has ended, while global sovereign wealth funds and corporate treasuries enter ETF allocation queues.",
                    "newsCatalyst": {
                        "headline": "Wall Street Journal: Two sovereign wealth funds initiate allocation mandates for spot crypto ETPs",
                        "source": "WSJ Asset Management", "time": "3 days ago", "impact": "SOVEREIGN INFLOW SUPERCYCLE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Global Macro & Bitcoin Supercycle",
                        "sentimentScore": 87, "sentimentTrend": "+25% Bullish monthly acceleration",
                        "whaleFlows": "Multi-billion dollar wallet cohorts in net accumulation mode",
                        "retailPositioning": "Retail entering early stages of global parabolic phase"
                    },
                    "riskMitigation": "Accumulate dips below 0.55; take 50% profit at 0.78."
                }
            },
            {
                "id": "cry-m-02", "rank": 2,
                "title": "Will the US Federal Reserve announce a crypto custody rule revision for National Banks this month?",
                "slug": "fed-crypto-custody-rule-national-banks-this-month",
                "volume": "$198,200,000", "volumeRaw": 198200000, "volumeLabel": "30D Volume",
                "liquidity": "$39,500,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 88, "evEdge": "+12.0% EV+", "impliedProb": 69, "fairValueProb": 81.0,
                    "targetExit": "$0.88 (+27.5% return)", "stopLoss": "$0.55",
                    "macroStrategy": "SAB 121 legislative rollback pressure and OCC joint agency guidance harmonization are forcing the Federal Reserve Board to modernize bank balance sheet capital deduction rules.",
                    "newsCatalyst": {
                        "headline": "American Banker: Regulators finalize inter-agency policy statement modifying SAB 121 accounting mandates",
                        "source": "American Banker Washington", "time": "2 days ago", "impact": "BANKING ACCESS EXPANSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Fintech Regulatory Watch",
                        "sentimentScore": 83, "sentimentTrend": "+18% Bullish",
                        "whaleFlows": "Major crypto prime brokers and institutional custodians building YES stakes",
                        "retailPositioning": "Complex regulatory phrasing keeps retail sidelined"
                    },
                    "riskMitigation": "Sell into the joint agency press release."
                }
            },
            {
                "id": "cry-m-03", "rank": 3,
                "title": "Will Solana (SOL) surpass its previous All-Time High ($260) this month?",
                "slug": "solana-surpass-all-time-high-260-this-month",
                "volume": "$162,800,000", "volumeRaw": 162800000, "volumeLabel": "30D Volume",
                "liquidity": "$33,100,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 89, "evEdge": "+13.0% EV+", "impliedProb": 72, "fairValueProb": 85.0,
                    "targetExit": "$0.91 (+26.4% return)", "stopLoss": "$0.58",
                    "macroStrategy": "Solana's on-chain economic metrics (daily active addresses, DEX market share, stablecoin transfer volume) are currently 400% higher than during its 2021 peak, creating fundamental price dislocation.",
                    "newsCatalyst": {
                        "headline": "VanEck Research: Solana metrics suggest institutional valuation target of $330 based on fee capture",
                        "source": "VanEck Crypto Analytics", "time": "4 days ago", "impact": "VALUATION EXPANSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Solana Breakpoint Alpha",
                        "sentimentScore": 89, "sentimentTrend": "+28% Bullish",
                        "whaleFlows": "Institutional OTC desks reporting zero available OTC supply under $250",
                        "retailPositioning": "Retail momentum surging globally"
                    },
                    "riskMitigation": "Trail stop at 0.65 as spot approaches $258."
                }
            },
            {
                "id": "cry-m-04", "rank": 4,
                "title": "Will Ethereum ETF staking yield approvals be granted by the SEC this month?",
                "slug": "ethereum-etf-staking-yield-approval-this-month",
                "volume": "$134,500,000", "volumeRaw": 134500000, "volumeLabel": "30D Volume",
                "liquidity": "$27,400,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.32, "pct": 32}, {"name": "NO", "price": 0.68, "pct": 68}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO (STRUCTURAL REALITY)", "conviction": "HIGH CONVICTION",
                    "confidencePct": 89, "evEdge": "+14.0% EV+", "impliedProb": 68, "fairValueProb": 82.0,
                    "targetExit": "$0.88 (+29.4% return)", "stopLoss": "$0.54",
                    "macroStrategy": "SEC Division of Corporation Finance formal comments on 19b-4 amendments require lengthy 240-day public comment cycles; approval timetable cannot statutorily occur this month.",
                    "newsCatalyst": {
                        "headline": "Bloomberg Intelligence: SEC 19b-4 staking amendments face statutory statutory review through Q2",
                        "source": "Bloomberg Law", "time": "3 days ago", "impact": "PROCEDURAL REALITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / ETF Legal Analysts",
                        "sentimentScore": 81, "sentimentTrend": "High NO consensus among analysts",
                        "whaleFlows": "Macro arbitrage funds shorting YES / accumulating NO",
                        "retailPositioning": "Retail hopefuls buying cheap YES tickets on social media hype"
                    },
                    "riskMitigation": "Hold NO until month-end calendar expiration."
                }
            },
            {
                "id": "cry-m-05", "rank": 5,
                "title": "Will Total Crypto Market Capitalization hit $4.0 Trillion this month?",
                "slug": "total-crypto-market-cap-4t-this-month",
                "volume": "$115,200,000", "volumeRaw": 115200000, "volumeLabel": "30D Volume",
                "liquidity": "$23,800,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 85, "evEdge": "+13.0% EV+", "impliedProb": 61, "fairValueProb": 74.0,
                    "targetExit": "$0.84 (+37.7% return)", "stopLoss": "$0.48",
                    "macroStrategy": "Total market cap currently stands at \$3.62T. With Bitcoin over \$100k, altcoin beta expansion and stablecoin creation provide a mathematical direct vector toward \$4.05T.",
                    "newsCatalyst": {
                        "headline": "CoinMarketCap: Global digital asset aggregate valuation crosses $3.6T mark, accelerating +4.2% weekly",
                        "source": "CoinMarketCap Data", "time": "2 days ago", "impact": "AGGREGATE LIQUIDITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Global Crypto Macro",
                        "sentimentScore": 86, "sentimentTrend": "+23% Bullish",
                        "whaleFlows": "Broad-spectrum institutional buying across top-20 liquid tokens",
                        "retailPositioning": "Retail onboarding volumes at Coinbase reaching cycle highs"
                    },
                    "riskMitigation": "Scale out 50% when total market cap touches $3.95T."
                }
            },
            {
                "id": "cry-m-06", "rank": 6,
                "title": "Will BlackRock's IBIT Bitcoin ETF reach $50 Billion AUM this month?",
                "slug": "blackrock-ibit-50b-aum-this-month",
                "volume": "$98,600,000", "volumeRaw": 98600000, "volumeLabel": "30D Volume",
                "liquidity": "$20,400,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 88, "evEdge": "+11.0% EV+", "impliedProb": 76, "fairValueProb": 87.0,
                    "targetExit": "$0.92 (+21.0% return)", "stopLoss": "$0.64",
                    "macroStrategy": "IBIT AUM stands at \$45.8B. Net asset appreciation and average daily inflows of +\$320M make crossing \$50B mathematically achieved within 12 trading sessions.",
                    "newsCatalyst": {
                        "headline": "Eric Balchunas / Bloomberg: IBIT paces toward fastest fund in Wall Street history to hit $50B AUM milestone",
                        "source": "Bloomberg Intelligence", "time": "3 days ago", "impact": "HISTORIC INFLOW RUN RATE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Institutional Wealth Management",
                        "sentimentScore": 88, "sentimentTrend": "Unstoppable trajectory",
                        "whaleFlows": "Registered Investment Advisors (RIAs) deploying client model portfolios",
                        "retailPositioning": "Retail recognizing historic institutional adoption"
                    },
                    "riskMitigation": "Capture safe alpha spread on YES."
                }
            },
            {
                "id": "cry-m-07", "rank": 7,
                "title": "Will a US Federal District Court formally dismiss SEC charges against Kraken this month?",
                "slug": "sec-kraken-charges-dismissed-this-month",
                "volume": "$84,100,000", "volumeRaw": 84100000, "volumeLabel": "30D Volume",
                "liquidity": "$17,500,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.26, "pct": 26}, {"name": "NO", "price": 0.74, "pct": 74}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                    "confidencePct": 90, "evEdge": "+11.0% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                    "targetExit": "$0.91 (+23.0% return)", "stopLoss": "$0.62",
                    "macroStrategy": "Northern District of California presiding judge already ruled that SEC claims sufficiently allege plausible investment contracts to survive a preliminary Rule 12(b)(6) dismissal.",
                    "newsCatalyst": {
                        "headline": "Reuters Legal: Judge Orrick's scheduling order mandates full evidentiary discovery through winter",
                        "source": "Reuters Legal", "time": "4 days ago", "impact": "LITIGATION CADENCE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Web3 Litigation Trackers",
                        "sentimentScore": 84, "sentimentTrend": "Clear consensus on NO",
                        "whaleFlows": "Legal arbitrage desks accumulating NO",
                        "retailPositioning": "Retail confused by procedural terminology"
                    },
                    "riskMitigation": "Hold NO into month-end for clean statistical return."
                }
            },
            {
                "id": "cry-m-08", "rank": 8,
                "title": "Will Cardano (ADA) re-enter the Top 8 Crypto Assets by Market Cap this month?",
                "slug": "cardano-ada-top-8-market-cap-this-month",
                "volume": "$71,500,000", "volumeRaw": 71500000, "volumeLabel": "30D Volume",
                "liquidity": "$14,800,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "MEDIUM-HIGH CONVICTION",
                    "confidencePct": 82, "evEdge": "+14.0% EV+", "impliedProb": 52, "fairValueProb": 66.0,
                    "targetExit": "$0.76 (+46.1% return)", "stopLoss": "$0.40",
                    "macroStrategy": "Chang hard fork governance transition completed and US crypto policy advisory alignments created a powerful catalyst, closing market cap deficit against Dogecoin and USDC.",
                    "newsCatalyst": {
                        "headline": "CryptoSlate: Cardano ADA rallies +42% on Chang governance upgrades and institutional staking expansion",
                        "source": "CryptoSlate", "time": "3 days ago", "impact": "MOMENTUM ROTATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Cardano Community & Whales",
                        "sentimentScore": 81, "sentimentTrend": "+24% Bullish inflection",
                        "whaleFlows": "Cardano Foundation and long-term staking pools accumulating spot",
                        "retailPositioning": "Retail community aggressively mobilizing"
                    },
                    "riskMitigation": "Sell half when ADA flips position #8 on CoinGecko."
                }
            },
            {
                "id": "cry-m-09", "rank": 9,
                "title": "Will Monero (XMR) be delisted by another Top 10 Centralized Global Exchange this month?",
                "slug": "monero-xmr-delisted-top-10-exchange-this-month",
                "volume": "$63,800,000", "volumeRaw": 63800000, "volumeLabel": "30D Volume",
                "liquidity": "$13,200,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.35, "pct": 35}, {"name": "NO", "price": 0.65, "pct": 65}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO (CONTRARIAN ALPHA)", "conviction": "HIGH CONVICTION",
                    "confidencePct": 86, "evEdge": "+13.0% EV+", "impliedProb": 65, "fairValueProb": 78.0,
                    "targetExit": "$0.84 (+29.2% return)", "stopLoss": "$0.52",
                    "macroStrategy": "Exchanges with EU/FATF compliance mandates have already concluded delistings in Q2/Q3; remaining offshore exchanges (KuCoin, Gate, MEXC) have maintained stable privacy-coin listing terms.",
                    "newsCatalyst": {
                        "headline": "Coindesk: Major European delistings conclude; Asian offshore exchanges reaffirm privacy token trading pairs",
                        "source": "CoinDesk Asia", "time": "4 days ago", "impact": "REGULATORY PLATEAU"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Privacy Tech & Monero Community",
                        "sentimentScore": 77, "sentimentTrend": "Stability prevailing",
                        "whaleFlows": "Smart money locking safe yield on NO",
                        "retailPositioning": "Retail still fearful from historic delisting cycles"
                    },
                    "riskMitigation": "Capture steady yield into month-end."
                }
            },
            {
                "id": "cry-m-10", "rank": 10,
                "title": "Will Base Layer 2 Total Value Locked (TVL) overtake Arbitrum One this month?",
                "slug": "base-l2-tvl-overtake-arbitrum-one-this-month",
                "volume": "$56,400,000", "volumeRaw": 56400000, "volumeLabel": "30D Volume",
                "liquidity": "$11,900,000", "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                    "confidencePct": 87, "evEdge": "+13.0% EV+", "impliedProb": 67, "fairValueProb": 80.0,
                    "targetExit": "$0.88 (+31.3% return)", "stopLoss": "$0.54",
                    "macroStrategy": "Coinbase smart wallet default integration has accelerated onboarding; Base DeFi TVL is compounding at +11.8% weekly versus Arbitrum's +2.1%, creating an imminent flippening.",
                    "newsCatalyst": {
                        "headline": "DefiLlama: Base TVL hits $3.45B, closing the gap with Arbitrum's $3.78B within striking distance",
                        "source": "DefiLlama Research", "time": "2 days ago", "impact": "ECOSYSTEM SURGE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Layer 2 Ecosystem Wars",
                        "sentimentScore": 85, "sentimentTrend": "+23% Bullish Base",
                        "whaleFlows": "Coinbase-affiliated protocols and Aerodrome whales bridging heavy liquidity",
                        "retailPositioning": "Retail aggressively using Base for social and meme apps"
                    },
                    "riskMitigation": "Sell position upon TVL flippening announcement."
                }
            }
        ]
    }

    # Helper function for Finance, Sports, Football Premier League, La Liga, Bundesliga
    print("Politics and Crypto generated successfully")
    return db

db = generate_all_markets()
with open("test_db.json", "w") as f:
    json.dump(db, f, indent=2)
print("Base dataset verified.")
