# -*- coding: utf-8 -*-
"""
Finance Polymarket Top 10 Markets (Day, Week, Month)
With full Macro Hedge Fund Strategy, News Catalysts, and Social Media Radar.
"""

FINANCE_DATA = {
    "day": [
        {
            "id": "fin-d-01", "rank": 1,
            "title": "Will the S&P 500 close at a fresh all-time high today?",
            "slug": "sp500-close-fresh-ath-today",
            "volume": "$41,250,000", "volumeRaw": 41250000, "volumeLabel": "24H Volume",
            "liquidity": "$8,950,000", "endDate": "Today 4:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+14.6% EV+", "impliedProb": 72, "fairValueProb": 84.5,
                "targetExit": "$0.88 (+22.2% gain)", "stopLoss": "$0.60",
                "macroStrategy": "S&P 500 0DTE options gamma tilt sits overwhelmingly positive above 5,980. CTAs and systematic trend followers have triggered mechanical $6.8B net equity buys into the NY open.",
                "newsCatalyst": {
                    "headline": "Goldman Sachs Prime Brokerage: Systematic fund equity allocations hit multi-month rebalancing highs",
                    "source": "Goldman Sachs FICC & Equities", "time": "35m ago", "impact": "SYSTEMATIC INFLOW"
                },
                "socialMediaRadar": {
                    "platform": "FinTwit / Bloomberg Terminal IB Chat",
                    "sentimentScore": 87, "sentimentTrend": "+19% Bullish surge",
                    "whaleFlows": "Dark pool print at SPY $598.40 exceeded $420M blocks; institutional call skew dominating puts 2.4:1.",
                    "retailPositioning": "Retail put-call ratio declining rapidly, signaling late FOMO chase."
                },
                "riskMitigation": "Lock 40% position profits at $0.82; place trailing protective stop at $0.66."
            }
        },
        {
            "id": "fin-d-02", "rank": 2,
            "title": "Will US 10-Year Treasury Yield close above 4.45% today?",
            "slug": "us-10y-yield-close-above-445-today",
            "volume": "$28,400,000", "volumeRaw": 28400000, "volumeLabel": "24H Volume",
            "liquidity": "$6,120,000", "endDate": "Today 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.38, "pct": 38}, {"name": "NO", "price": 0.62, "pct": 62}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+15.2% EV+", "impliedProb": 62, "fairValueProb": 76.0,
                "targetExit": "$0.78 (+25.8% gain on NO)", "stopLoss": "$0.48",
                "macroStrategy": "Primary dealer auction bid-to-cover metrics indicate resilient overseas duration demand from Japanese lifers. 10Y yield resistance at 4.445% is reinforced by substantial convex swap hedging.",
                "newsCatalyst": {
                    "headline": "Reuters: Foreign central banks and institutional asset managers step up long-duration Treasury purchases",
                    "source": "Reuters Global Fixed Income", "time": "1h ago", "impact": "YIELD COMPRESSION"
                },
                "socialMediaRadar": {
                    "platform": "Macro Hive / Bond Twitter",
                    "sentimentScore": 79, "sentimentTrend": "+28% Yield-peak consensus",
                    "whaleFlows": "Direct SOFR futures block buy of 14,000 contracts betting on rate stability.",
                    "retailPositioning": "Retail bears shorting bond ETFs into institutional support wall."
                },
                "riskMitigation": "Bet NO (against yield staying >4.45%). Cut if 10Y breaks 4.462% on high volume."
            }
        },
        {
            "id": "fin-d-03", "rank": 3,
            "title": "Will Spot Gold trade above $2,820/oz before the London fix?",
            "slug": "gold-spot-trade-above-2820-london-fix",
            "volume": "$22,600,000", "volumeRaw": 22600000, "volumeLabel": "24H Volume",
            "liquidity": "$4,850,000", "endDate": "Today 3:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.66, "pct": 66}, {"name": "NO", "price": 0.34, "pct": 34}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+11.4% EV+", "impliedProb": 66, "fairValueProb": 75.5,
                "targetExit": "$0.80 (+21.2% gain)", "stopLoss": "$0.54",
                "macroStrategy": "Eastern European and Asian central bank monthly gold accumulation accelerated +18%. Geopolitical friction in the Levant is prompting sovereign asset managers to diversify away from paper reserves.",
                "newsCatalyst": {
                    "headline": "Financial Times: Sovereign wealth funds increase physical gold allocation to hedge debt sustainability risks",
                    "source": "Financial Times Commodities", "time": "2h ago", "impact": "PHYSICAL BID"
                },
                "socialMediaRadar": {
                    "platform": "Kitco / Metals Subreddit & X Macro",
                    "sentimentScore": 82, "sentimentTrend": "+16% Bullish momentum",
                    "whaleFlows": "COMEX December contract open interest expanded by 11,200 contracts.",
                    "retailPositioning": "Retail jewelry demand soft, but institutional macro bullion desks driving order books."
                },
                "riskMitigation": "Position size at 4% of bankroll. Rebalance on DXY dollar bounce."
            }
        },
        {
            "id": "fin-d-04", "rank": 4,
            "title": "Will WTI Crude Oil settle above $76.50/bbl on energy inventory data?",
            "slug": "wti-crude-oil-settle-above-7650-today",
            "volume": "$18,900,000", "volumeRaw": 18900000, "volumeLabel": "24H Volume",
            "liquidity": "$4,100,000", "endDate": "Today 2:30 PM EST",
            "outcomes": [{"name": "YES", "price": 0.44, "pct": 44}, {"name": "NO", "price": 0.56, "pct": 56}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+13.8% EV+", "impliedProb": 56, "fairValueProb": 68.2,
                "targetExit": "$0.72 (+28.5% gain on NO)", "stopLoss": "$0.44",
                "macroStrategy": "EIA preview reports point to a surprise +2.8M barrel inventory build at Cushing, Oklahoma. Refinery run rates slipped 1.4% amid seasonal maintenance turnarounds.",
                "newsCatalyst": {
                    "headline": "Energy Intelligence: US Gulf Coast export bottlenecks create short-term domestic crude surplus",
                    "source": "Energy Intelligence Desk", "time": "1h ago", "impact": "SUPPLY SURPLUS"
                },
                "socialMediaRadar": {
                    "platform": "OilPrice / Commodities Discord",
                    "sentimentScore": 38, "sentimentTrend": "-14% Bearish drift",
                    "whaleFlows": "Glencore and Vitol hedging desks active with prompt-month short collar spreads.",
                    "retailPositioning": "Retail traders aggressively bottom-fishing crude calls."
                },
                "riskMitigation": "Execute on Polymarket NO outcome; exit immediately if Middle East shipping transit halted."
            }
        },
        {
            "id": "fin-d-05", "rank": 5,
            "title": "Will Nvidia (NVDA) market cap remain above $3.5 Trillion at daily close?",
            "slug": "nvidia-nvda-market-cap-above-35t-close",
            "volume": "$32,100,000", "volumeRaw": 32100000, "volumeLabel": "24H Volume",
            "liquidity": "$7,400,000", "endDate": "Today 4:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.79, "pct": 79}, {"name": "NO", "price": 0.21, "pct": 21}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 91, "evEdge": "+12.1% EV+", "impliedProb": 79, "fairValueProb": 90.0,
                "targetExit": "$0.94 (+19.0% gain)", "stopLoss": "$0.68",
                "macroStrategy": "Blackwell enterprise rack shipments confirmed accelerating at hyperscaler client centers. Major tech enterprise capex guidance revisions provide structural valuation floor at $140/share.",
                "newsCatalyst": {
                    "headline": "Morgan Stanley Equity Research: Reaffirms NVDA as Top Pick with cloud capex runway expanding into 2026",
                    "source": "Morgan Stanley Tech Pulse", "time": "50m ago", "impact": "ANALYST RE-RATING"
                },
                "socialMediaRadar": {
                    "platform": "Tech Twitter / r/wallstreetbets & Finviz",
                    "sentimentScore": 91, "sentimentTrend": "+22% Dominant bullish dominance",
                    "whaleFlows": "Citadel and Jane Street options desks writing deep OTM puts, pinning stock above support.",
                    "retailPositioning": "Unanimous retail call buying, supported by deep institutional floor."
                },
                "riskMitigation": "Hold through close. High win rate profile with small tail exposure."
            }
        },
        {
            "id": "fin-d-06", "rank": 6,
            "title": "Will US Initial Jobless Claims come in below 215,000?",
            "slug": "us-initial-jobless-claims-below-215k",
            "volume": "$14,500,000", "volumeRaw": 14500000, "volumeLabel": "24H Volume",
            "liquidity": "$3,200,000", "endDate": "Today 8:30 AM EST",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 78, "evEdge": "+10.8% EV+", "impliedProb": 58, "fairValueProb": 66.5,
                "targetExit": "$0.72 (+24.1% gain)", "stopLoss": "$0.46",
                "macroStrategy": "State-level WARN notices and continuing claims rollover figures indicate labor hoarding remains predominant among mid-sized manufacturing and healthcare firms.",
                "newsCatalyst": {
                    "headline": "Department of Labor Advance Data: State unemployment insurance filings drop across Southeast corridors",
                    "source": "Bureau of Labor Statistics Feed", "time": "2h ago", "impact": "TIGHT LABOR MARKET"
                },
                "socialMediaRadar": {
                    "platform": "Macro Twitter & Economic Cal Trackers",
                    "sentimentScore": 65, "sentimentTrend": "+11% Soft-landing bias",
                    "whaleFlows": "Macro multi-strat fund placed $180,000 in YES contracts.",
                    "retailPositioning": "Retail divided on recession risks versus resilience."
                },
                "riskMitigation": "Take quick profit right after official 8:30 AM release prints."
            }
        },
        {
            "id": "fin-d-07", "rank": 7,
            "title": "Will the US Dollar Index (DXY) stay above 104.50 at European close?",
            "slug": "us-dollar-index-dxy-stay-above-10450",
            "volume": "$16,200,000", "volumeRaw": 16200000, "volumeLabel": "24H Volume",
            "liquidity": "$3,650,000", "endDate": "Today 11:30 AM EST",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.7% EV+", "impliedProb": 65, "fairValueProb": 75.8,
                "targetExit": "$0.80 (+23.0% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Eurozone PMI divergence and dovish ECB speaker remarks are weighing heavily on EUR/USD, which constitutes 57.6% of the DXY basket. Rate spread differential favors US dollar carry.",
                "newsCatalyst": {
                    "headline": "Bloomberg FX: European industrial output slows, widening US-EU policy rate divergence expectation",
                    "source": "Bloomberg FX Markets", "time": "1h 15m ago", "impact": "DOLLAR STRENGTH"
                },
                "socialMediaRadar": {
                    "platform": "ForexFactory / FX Street Live",
                    "sentimentScore": 76, "sentimentTrend": "+18% Greenback strength",
                    "whaleFlows": "Corporate treasuries locking forward FX hedges against weaker EUR and GBP.",
                    "retailPositioning": "Retail attempting to short dollar top too early."
                },
                "riskMitigation": "Set stop-loss if EUR/USD violently breaks above 1.0820 resistance."
            }
        },
        {
            "id": "fin-d-08", "rank": 8,
            "title": "Will the Cboe VIX Index spike above 18.00 before equity close?",
            "slug": "vix-index-spike-above-18-today",
            "volume": "$12,800,000", "volumeRaw": 12800000, "volumeLabel": "24H Volume",
            "liquidity": "$2,900,000", "endDate": "Today 4:15 PM EST",
            "outcomes": [{"name": "YES", "price": 0.28, "pct": 28}, {"name": "NO", "price": 0.72, "pct": 72}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+14.0% EV+", "impliedProb": 72, "fairValueProb": 84.0,
                "targetExit": "$0.86 (+19.4% gain on NO)", "stopLoss": "$0.58",
                "macroStrategy": "Systematic volatility-selling funds (dispersion traders, covered-call ETFs) are dumping vega into the market, exerting relentless suppression on the implied volatility surface.",
                "newsCatalyst": {
                    "headline": "Cboe Derivatives Intelligence: Implied volatility risk premium remains deeply negative across index options",
                    "source": "Cboe Institutional Insights", "time": "1h 40m ago", "impact": "VOLATILITY CRUSH"
                },
                "socialMediaRadar": {
                    "platform": "Reddit r/options / Volatility Desk",
                    "sentimentScore": 81, "sentimentTrend": "+24% Vol crush consensus",
                    "whaleFlows": "Large institutional sales of VIX 20 strike call spreads.",
                    "retailPositioning": "Retail hedging catastrophe puts, getting steadily bled by theta decay."
                },
                "riskMitigation": "Bet NO on VIX spike; hedge if geopolitical breaking headline triggers market gap."
            }
        },
        {
            "id": "fin-d-09", "rank": 9,
            "title": "Will Apple (AAPL) announce an expanded OpenAI or Gemini partnership feature today?",
            "slug": "apple-aapl-announce-ai-partnership-today",
            "volume": "$15,400,000", "volumeRaw": 15400000, "volumeLabel": "24H Volume",
            "liquidity": "$3,400,000", "endDate": "Today 6:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.31, "pct": 31}, {"name": "NO", "price": 0.69, "pct": 69}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+16.5% EV+", "impliedProb": 69, "fairValueProb": 82.5,
                "targetExit": "$0.84 (+21.7% gain on NO)", "stopLoss": "$0.55",
                "macroStrategy": "Apple developer beta release cycles show iOS point releases scheduled for mid-month, not today. PR calendar contains no scheduled keynote or Cupertino press briefings.",
                "newsCatalyst": {
                    "headline": "Mark Gurman / Bloomberg Power On: Apple Intelligence feature rollouts slated for staggered multi-week release",
                    "source": "Bloomberg Tech Insider", "time": "3h ago", "impact": "CALENDAR DELAY"
                },
                "socialMediaRadar": {
                    "platform": "MacRumors / Tech X Feeds",
                    "sentimentScore": 72, "sentimentTrend": "+15% NO certainty",
                    "whaleFlows": "Smart money accumulating NO contracts on false rumor pump.",
                    "retailPositioning": "Retail speculation on unverified blog rumors."
                },
                "riskMitigation": "Capture attractive 31% mispricing by taking NO side."
            }
        },
        {
            "id": "fin-d-10", "rank": 10,
            "title": "Will 2-Year US Treasury Yield drop below 4.15% after Fed speech?",
            "slug": "2y-treasury-yield-drop-below-415-today",
            "volume": "$11,900,000", "volumeRaw": 11900000, "volumeLabel": "24H Volume",
            "liquidity": "$2,700,000", "endDate": "Today 4:30 PM EST",
            "outcomes": [{"name": "YES", "price": 0.46, "pct": 46}, {"name": "NO", "price": 0.54, "pct": 54}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "MODERATE CONVICTION",
                "confidencePct": 77, "evEdge": "+11.5% EV+", "impliedProb": 54, "fairValueProb": 62.0,
                "targetExit": "$0.67 (+24.0% gain on NO)", "stopLoss": "$0.42",
                "macroStrategy": "Fed Governor speech preview notes indicate persistent emphasis on data dependency and warning against cutting too fast. Front-end curves will likely reprice towards hawkish stability.",
                "newsCatalyst": {
                    "headline": "Federal Reserve Communications: Fed speakers emphasize patience on inflation return to 2.0% objective",
                    "source": "Dow Jones Newswires", "time": "45m ago", "impact": "HAWKISH RESTRAINT"
                },
                "socialMediaRadar": {
                    "platform": "FedWatch / Rate Cut Monitor",
                    "sentimentScore": 68, "sentimentTrend": "+14% Rate resilience",
                    "whaleFlows": "Commercial banks increasing repo operations at prevailing policy rates.",
                    "retailPositioning": "Retail betting on aggressive rate cut rhetoric."
                },
                "riskMitigation": "Bet NO on yield drop; size position conservatively."
            }
        }
    ],
    "week": [
        {
            "id": "fin-w-01", "rank": 1,
            "title": "Will US Headline CPI for the month print at or below 2.5% YoY?",
            "slug": "us-headline-cpi-print-below-25-yoy",
            "volume": "$78,500,000", "volumeRaw": 78500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$14,200,000", "endDate": "Thursday 8:30 AM EST",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+13.7% EV+", "impliedProb": 63, "fairValueProb": 74.0,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Truflation real-time index reads 2.38%. Used vehicle wholesale prices (Manheim) plunged -2.1% month-on-month, and shelter cooling lags are finally flowing into BLS official metrics.",
                "newsCatalyst": {
                    "headline": "Cleveland Fed Inflation Nowcast: CPI forecast revised down 0.12 percentage points on fuel and shelter cooling",
                    "source": "Federal Reserve Bank of Cleveland", "time": "4h ago", "impact": "DISINFLATION CONFIRMATION"
                },
                "socialMediaRadar": {
                    "platform": "FinTwit / Macro Alf & Michael Kao Feeds",
                    "sentimentScore": 84, "sentimentTrend": "+21% Disinflation consensus",
                    "whaleFlows": "TIPS breakeven rates collapsing, reflecting massive institutional deflationary positioning.",
                    "retailPositioning": "Retail still fearful of sticky inflation headlines, underestimating goods deflation."
                },
                "riskMitigation": "Lock 50% profits immediately on release if print lands <= 2.5%."
            }
        },
        {
            "id": "fin-w-02", "rank": 2,
            "title": "Will the Federal Reserve cut interest rates at the upcoming FOMC meeting?",
            "slug": "federal-reserve-cut-rates-next-fomc",
            "volume": "$94,300,000", "volumeRaw": 94300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$18,500,000", "endDate": "Next Wednesday 2:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.84, "pct": 84}, {"name": "NO", "price": 0.16, "pct": 16}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 92, "evEdge": "+9.8% EV+", "impliedProb": 84, "fairValueProb": 93.5,
                "targetExit": "$0.96 (+14.3% gain)", "stopLoss": "$0.75",
                "macroStrategy": "CME FedWatch displays 91.2% priced-in probability for 25 bps reduction. Labor market rebalancing combined with benign Beige Book economic surveys cements Powell's recalibration mandate.",
                "newsCatalyst": {
                    "headline": "Wall Street Journal (Nick Timiraos): Fed on track for measured 25 basis point rate cut as labor market softens",
                    "source": "WSJ Macro Desk", "time": "6h ago", "impact": "POLICY SIGNAL"
                },
                "socialMediaRadar": {
                    "platform": "Bloomberg Surveillance / X Macro Terminal",
                    "sentimentScore": 92, "sentimentTrend": "+25% Dovish certainty",
                    "whaleFlows": "SOFR options call condor structures loaded by Citadel, Millennium, and Point72.",
                    "retailPositioning": "Overwhelming consensus, but asymmetrical risk still favors staying long YES."
                },
                "riskMitigation": "High probability anchor bet. Size moderately; hold into the rate announcement."
            }
        },
        {
            "id": "fin-w-03", "rank": 3,
            "title": "Will Tesla (TSLA) weekly deliveries exceed Wall Street consensus forecast?",
            "slug": "tesla-tsla-weekly-deliveries-exceed-consensus",
            "volume": "$46,700,000", "volumeRaw": 46700000, "volumeLabel": "7-Day Volume",
            "liquidity": "$9,800,000", "endDate": "Friday 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.5% EV+", "impliedProb": 52, "fairValueProb": 61.0,
                "targetExit": "$0.68 (+30.7% gain)", "stopLoss": "$0.40",
                "macroStrategy": "China CPCA weekly auto registration insurance data logged a stellar 18,200 units for Tesla, tracking 14% higher than institutional models. Giga Shanghai export volumes surged to European hubs.",
                "newsCatalyst": {
                    "headline": "China Passenger Car Association (CPCA): Tesla China weekly insured registrations jump to second-highest weekly record",
                    "source": "CPCA Official Automotive Feed", "time": "7h ago", "impact": "DELIVERY BEAT"
                },
                "socialMediaRadar": {
                    "platform": "Tesla Investor Twitter / Troy Teslike Tracker",
                    "sentimentScore": 78, "sentimentTrend": "+20% Bullish inflection",
                    "whaleFlows": "Substantial call sweep in TSLA $260 weekly options.",
                    "retailPositioning": "Retail sentiment historically polarized; smart money following real-time registration data."
                },
                "riskMitigation": "Trim 50% position if price surges past $0.65 prior to official press release."
            }
        },
        {
            "id": "fin-w-04", "rank": 4,
            "title": "Will Brent Crude Oil close the week above $82.00/bbl?",
            "slug": "brent-crude-oil-weekly-close-above-82",
            "volume": "$39,400,000", "volumeRaw": 39400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$8,100,000", "endDate": "Friday 5:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.36, "pct": 36}, {"name": "NO", "price": 0.64, "pct": 64}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+14.8% EV+", "impliedProb": 64, "fairValueProb": 76.5,
                "targetExit": "$0.79 (+23.4% gain on NO)", "stopLoss": "$0.52",
                "macroStrategy": "OPEC+ surplus capacity overhang (approx. 5.8 mbpd) alongside non-OPEC Americas production growth (US, Guyana, Brazil) will cap prompt Brent rallies below psychological $82 threshold.",
                "newsCatalyst": {
                    "headline": "International Energy Agency (IEA): Global oil demand growth forecast clipped as renewables and EV share expand",
                    "source": "IEA Monthly Oil Report", "time": "8h ago", "impact": "STRUCTURAL CAP"
                },
                "socialMediaRadar": {
                    "platform": "Hedge Fund Energy Alpha Chat",
                    "sentimentScore": 77, "sentimentTrend": "+17% Bearish oil tilt",
                    "whaleFlows": "Commodity trading houses selling call spreads to hedge offshore production.",
                    "retailPositioning": "Retail chasing geopolitical war-premium spikes and getting trapped."
                },
                "riskMitigation": "Hold NO contracts into weekend close; exit only if Hormuz strait incident escalates."
            }
        },
        {
            "id": "fin-w-05", "rank": 5,
            "title": "Will High Yield US Corporate Credit Spreads stay compressed below 320 bps this week?",
            "slug": "us-high-yield-credit-spreads-below-320bps",
            "volume": "$27,800,000", "volumeRaw": 27800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$5,900,000", "endDate": "Friday 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+12.4% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                "targetExit": "$0.88 (+18.9% gain)", "stopLoss": "$0.62",
                "macroStrategy": "Massive institutional liquidity overhang and private credit refinancing facilities have eliminated near-term default walls. Inflows into HYG and JNK funds hit $1.4B net past 5 days.",
                "newsCatalyst": {
                    "headline": "Barclays Credit Research: High-yield issuance absorbed with 4.2x oversubscription books",
                    "source": "Barclays Global Credit", "time": "12h ago", "impact": "CREDIT EUPHORIA"
                },
                "socialMediaRadar": {
                    "platform": "Credit Suisse Alum Desk / LevFin Twitter",
                    "sentimentScore": 88, "sentimentTrend": "+21% Tight spreads consensus",
                    "whaleFlows": "PIMCO, BlackRock, and Oaktree participating in senior secured secondary tranches.",
                    "retailPositioning": "Retail under-allocated to credit; institutional demand dominates."
                },
                "riskMitigation": "Low volatility high probability income trade on Polymarket YES outcome."
            }
        },
        {
            "id": "fin-w-06", "rank": 6,
            "title": "Will Japanese Yen (USD/JPY) strengthen below 149.50 by Friday close?",
            "slug": "usdjpy-strengthen-below-14950-friday",
            "volume": "$33,200,000", "volumeRaw": 33200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$7,100,000", "endDate": "Friday 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.42, "pct": 42}, {"name": "NO", "price": 0.58, "pct": 58}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "MODERATE CONVICTION",
                "confidencePct": 79, "evEdge": "+11.9% EV+", "impliedProb": 58, "fairValueProb": 67.5,
                "targetExit": "$0.73 (+25.8% gain on NO)", "stopLoss": "$0.45",
                "macroStrategy": "Bank of Japan Governor Ueda's dovish tone regarding wage growth pace dampens odds of an imminent rate hike. Carry trade unwind pressure has normalized with US yield differentials intact.",
                "newsCatalyst": {
                    "headline": "Nikkei Asia: Bank of Japan officials signal patience on normalization until spring wage negotiations conclude",
                    "source": "Nikkei Economic Service", "time": "10h ago", "impact": "YEN WEAKNESS"
                },
                "socialMediaRadar": {
                    "platform": "Tokyo FX Desk / Macro Hedge Twitter",
                    "sentimentScore": 73, "sentimentTrend": "+16% Carry stability",
                    "whaleFlows": "Japanese retail margin accounts rebuilding long USD/JPY carry trades.",
                    "retailPositioning": "Retail attempting to time BOJ intervention spikes."
                },
                "riskMitigation": "Bet NO on Yen breaking under 149.50. Close position if Ministry of Finance announces verbal intervention."
            }
        },
        {
            "id": "fin-w-07", "rank": 7,
            "title": "Will Bank of England hold Bank Rate at 4.75% at this week's MPC meeting?",
            "slug": "bank-of-england-hold-rate-475-this-week",
            "volume": "$25,600,000", "volumeRaw": 25600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$5,400,000", "endDate": "Thursday 12:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.81, "pct": 81}, {"name": "NO", "price": 0.19, "pct": 19}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 90, "evEdge": "+10.2% EV+", "impliedProb": 81, "fairValueProb": 91.0,
                "targetExit": "$0.94 (+16.0% gain)", "stopLoss": "$0.70",
                "macroStrategy": "UK Autumn Budget fiscal expansion and sticky UK services inflation (4.9%) eliminate room for a rapid rate-cutting cycle. MPC vote split expected at 7-2 or 8-1 in favor of holding steady.",
                "newsCatalyst": {
                    "headline": "Reuters UK: Financial markets price only 12% probability of November rate cut following Chancellor's budget stimulus",
                    "source": "Reuters UK Economics", "time": "9h ago", "impact": "HOLD CONSENSUS"
                },
                "socialMediaRadar": {
                    "platform": "UK Gilts Desk / City of London Feeds",
                    "sentimentScore": 89, "sentimentTrend": "+23% Rate hold consensus",
                    "whaleFlows": "Sterling interest rate swap curves flatlining around 4.75% benchmark.",
                    "retailPositioning": "Broad consensus; safe alpha extraction."
                },
                "riskMitigation": "High conviction lock; redeem winnings immediately following 12:00 GMT announcement."
            }
        },
        {
            "id": "fin-w-08", "rank": 8,
            "title": "Will Copper Futures rally above $4.50/lb on China stimulus announcement?",
            "slug": "copper-futures-rally-above-450-this-week",
            "volume": "$21,300,000", "volumeRaw": 21300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,600,000", "endDate": "Friday 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.55, "pct": 55}, {"name": "NO", "price": 0.45, "pct": 45}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+12.6% EV+", "impliedProb": 55, "fairValueProb": 64.5,
                "targetExit": "$0.70 (+27.2% gain)", "stopLoss": "$0.43",
                "macroStrategy": "China National People's Congress Standing Committee approved local government debt refinancing quota of 10 Trillion Yuan. Grid investment by State Grid of China up 13% YoY, driving physical copper cathode tightness.",
                "newsCatalyst": {
                    "headline": "Shanghai Metals Market: LME and SHFE copper warehouse inventories draw down for fourth consecutive week",
                    "source": "SMM Metals Intelligence", "time": "11h ago", "impact": "INVENTORY DRAWDOWN"
                },
                "socialMediaRadar": {
                    "platform": "Mining Twitter / Commodities Edge",
                    "sentimentScore": 80, "sentimentTrend": "+19% Bullish metals momentum",
                    "whaleFlows": "Macro commodity funds accumulating copper call options across LME and COMEX.",
                    "retailPositioning": "Retail hesitant due to mixed Chinese consumer data."
                },
                "riskMitigation": "Set stop-loss if US Dollar Index breaks above 105.20."
            }
        },
        {
            "id": "fin-w-09", "rank": 9,
            "title": "Will Microsoft (MSFT) cloud revenue growth exceed 29% YoY this quarter?",
            "slug": "microsoft-msft-azure-cloud-growth-above-29",
            "volume": "$36,900,000", "volumeRaw": 36900000, "volumeLabel": "7-Day Volume",
            "liquidity": "$7,800,000", "endDate": "Thursday 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+13.1% EV+", "impliedProb": 67, "fairValueProb": 78.0,
                "targetExit": "$0.83 (+23.8% gain)", "stopLoss": "$0.55",
                "macroStrategy": "Azure AI enterprise workload migration surveys indicate that Copilot seat expansions and OpenAI API consumption accounted for 8.5 percentage points of incremental growth alone.",
                "newsCatalyst": {
                    "headline": "Jefferies Tech Equity Report: Channel checks reveal Azure AI capacity backlog remains fully booked through Q2",
                    "source": "Jefferies Technology Equity Desk", "time": "14h ago", "impact": "EARNINGS ACCELERATION"
                },
                "socialMediaRadar": {
                    "platform": "Silicon Valley Cloud Watch / Hacker News",
                    "sentimentScore": 86, "sentimentTrend": "+20% Azure outperformance",
                    "whaleFlows": "Tiger Global, Coatue, and institutional tech funds accumulating long exposure.",
                    "retailPositioning": "Retail bullish on AI hype; data fundamentally validates thesis."
                },
                "riskMitigation": "Lock partial profits ahead of earnings conference call."
            }
        },
        {
            "id": "fin-w-10", "rank": 10,
            "title": "Will the German DAX index hit a new historical peak this week?",
            "slug": "german-dax-index-new-ath-this-week",
            "volume": "$19,800,000", "volumeRaw": 19800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,200,000", "endDate": "Friday 5:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.48, "pct": 48}, {"name": "NO", "price": 0.52, "pct": 52}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "MODERATE CONVICTION",
                "confidencePct": 78, "evEdge": "+12.0% EV+", "impliedProb": 52, "fairValueProb": 61.5,
                "targetExit": "$0.68 (+30.7% gain on NO)", "stopLoss": "$0.40",
                "macroStrategy": "German factory orders and industrial output contractions continue to drag on SAP and Siemens heavy index weighting. Political uncertainty following Bundestag coalition friction limits multiple expansion.",
                "newsCatalyst": {
                    "headline": "Handelsblatt: German industrial chambers report subdued capital expenditure plans heading into winter",
                    "source": "Handelsblatt Finance", "time": "13h ago", "impact": "MACRO HEADWIND"
                },
                "socialMediaRadar": {
                    "platform": "Frankfurt Börse Desk / Eurostoxx Chat",
                    "sentimentScore": 41, "sentimentTrend": "-13% Cautious European stance",
                    "whaleFlows": "European pension funds rotating capital out of DAX into US mega-caps.",
                    "retailPositioning": "Retail chasing DAX resistance levels blindly."
                },
                "riskMitigation": "Bet NO on DAX new peak; stop out if ECB signals aggressive 50 bps December rate cut."
            }
        }
    ],
    "month": [
        {
            "id": "fin-m-01", "rank": 1,
            "title": "Will the S&P 500 cross 6,100 before the end of the month?",
            "slug": "sp500-cross-6100-before-month-end",
            "volume": "$142,500,000", "volumeRaw": 142500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$28,400,000", "endDate": "End of Month 4:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+14.3% EV+", "impliedProb": 71, "fairValueProb": 83.5,
                "targetExit": "$0.88 (+23.9% gain)", "stopLoss": "$0.58",
                "macroStrategy": "Seasonal year-end corporate share buyback windows ($5.5B daily execution) combined with post-election policy certainty and corporate earnings growth of +11.8% YoY mathematically propel S&P 500 above 6,100.",
                "newsCatalyst": {
                    "headline": "UBS Global Wealth Management: Raises year-end S&P 500 price target to 6,200 citing robust profit margins",
                    "source": "UBS Equity Strategy", "time": "1d ago", "impact": "TARGET UPGRADE"
                },
                "socialMediaRadar": {
                    "platform": "Institutional Prime Brokerage Roundtables / FinTwit",
                    "sentimentScore": 88, "sentimentTrend": "+24% Bull market confirmation",
                    "whaleFlows": "Systematic volatility control funds levering up equity exposure from 45th to 82nd percentile.",
                    "retailPositioning": "Retail cash sitting in money market funds ($6.4T) beginning to rotate into index funds."
                },
                "riskMitigation": "Core alpha bet. Rebalance if 10Y Treasury yield breaks above 4.60% sustainably."
            }
        },
        {
            "id": "fin-m-02", "rank": 2,
            "title": "Will Gold (XAU/USD) reach $2,900/oz before the end of this month?",
            "slug": "gold-xauusd-reach-2900-month-end",
            "volume": "$118,200,000", "volumeRaw": 118200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$22,600,000", "endDate": "End of Month 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.9% EV+", "impliedProb": 58, "fairValueProb": 69.5,
                "targetExit": "$0.76 (+31.0% gain)", "stopLoss": "$0.46",
                "macroStrategy": "Structural de-dollarization by Global South central banks, combined with expanding US sovereign debt interest costs ($1.1T annualized), ensures relentless monthly structural bid for non-sovereign reserve bullion.",
                "newsCatalyst": {
                    "headline": "World Gold Council: Central bank net bullion purchases set all-time record pace for third quarter running",
                    "source": "World Gold Council Quarterly", "time": "2d ago", "impact": "STRUCTURAL BID"
                },
                "socialMediaRadar": {
                    "platform": "GoldBug Twitter / Macro Bullion Watch",
                    "sentimentScore": 85, "sentimentTrend": "+22% Secular bull sentiment",
                    "whaleFlows": "Physical bullion bars departing London LBMA vaults to Swiss refineries and Asian buyers.",
                    "retailPositioning": "Retail ETF allocations still under-indexed relative to past bull cycles, leaving room to run."
                },
                "riskMitigation": "Ride trend; set trailing profit lock once gold touches $2,875."
            }
        },
        {
            "id": "fin-m-03", "rank": 3,
            "title": "Will the Federal Reserve announce a formal slowdown in Balance Sheet QT this month?",
            "slug": "federal-reserve-slowdown-qt-balance-sheet-month",
            "volume": "$86,400,000", "volumeRaw": 86400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$16,900,000", "endDate": "End of Month 2:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.64, "pct": 64}, {"name": "NO", "price": 0.36, "pct": 36}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.8% EV+", "impliedProb": 64, "fairValueProb": 75.0,
                "targetExit": "$0.80 (+25.0% gain)", "stopLoss": "$0.51",
                "macroStrategy": "Fed Overnight Reverse Repo (ON RRP) facility has dwindled down toward $150B, approaching the 'ample reserves' threshold where quantitative tightening threatens interbank repo plumbing stability.",
                "newsCatalyst": {
                    "headline": "Federal Reserve Bank of Dallas Staff Paper: Ample reserve framework necessitates cautious taper of Treasury roll-offs",
                    "source": "Dallas Fed Economic Research", "time": "1d ago", "impact": "LIQUIDITY SUPPORT"
                },
                "socialMediaRadar": {
                    "platform": "Zoltan Pozsar Plumbing Trackers / Fed Watchers",
                    "sentimentScore": 84, "sentimentTrend": "+19% Taper expectation",
                    "whaleFlows": "Fixed income primary dealers lobbying Fed to avoid September 2019 repo spike recurrence.",
                    "retailPositioning": "Retail unaware of balance sheet plumbing, presenting huge asymmetric edge."
                },
                "riskMitigation": "Hold through FOMC minutes release; take profits upon official taper announcement."
            }
        },
        {
            "id": "fin-m-04", "rank": 4,
            "title": "Will US Core PCE Inflation drop below 2.6% YoY on the upcoming monthly release?",
            "slug": "us-core-pce-drop-below-26-yoy",
            "volume": "$72,100,000", "volumeRaw": 72100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$14,300,000", "endDate": "End of Month 8:30 AM EST",
            "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+13.3% EV+", "impliedProb": 69, "fairValueProb": 80.5,
                "targetExit": "$0.85 (+23.2% gain)", "stopLoss": "$0.56",
                "macroStrategy": "PCE healthcare and airfare inputs (derived from PPI and CPI subcomponents) show consistent deceleration. Core PCE 3-month annualized rate already tracks at 2.2%, pulling 12-month figure down below 2.6%.",
                "newsCatalyst": {
                    "headline": "Morgan Stanley Economics: Core PCE track revised downward to 2.54% YoY as medical services normalize",
                    "source": "Morgan Stanley US Economics", "time": "2d ago", "impact": "DISINFLATION DRIFT"
                },
                "socialMediaRadar": {
                    "platform": "FinTwit / Macro Compass",
                    "sentimentScore": 83, "sentimentTrend": "+20% PCE cooling consensus",
                    "whaleFlows": "Treasury 2-year and 5-year swap spreads reflecting confident disinflation roadmap.",
                    "retailPositioning": "Retail still fixated on supermarket prices rather than official PCE basket methodology."
                },
                "riskMitigation": "Lock 60% position profit upon data print."
            }
        },
        {
            "id": "fin-m-05", "rank": 5,
            "title": "Will Berkshire Hathaway cash pile surpass $335 Billion in quarterly regulatory filings?",
            "slug": "berkshire-hathaway-cash-pile-surpass-335b",
            "volume": "$54,600,000", "volumeRaw": 54600000, "volumeLabel": "30-Day Volume",
            "liquidity": "$11,200,000", "endDate": "End of Month 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.77, "pct": 77}, {"name": "NO", "price": 0.23, "pct": 23}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 90, "evEdge": "+11.4% EV+", "impliedProb": 77, "fairValueProb": 88.0,
                "targetExit": "$0.92 (+19.5% gain)", "stopLoss": "$0.65",
                "macroStrategy": "Buffett sold an estimated additional 100M Apple shares and continued trimming Bank of America, while Berkshire operating businesses generate $10B+ quarterly free cash flow invested in 5% T-bills.",
                "newsCatalyst": {
                    "headline": "Wall Street Journal: Warren Buffett continues strategic capital preservation with T-bill holdings topping US Fed",
                    "source": "WSJ Corporate Finance", "time": "3d ago", "impact": "CAPITAL ACCUMULATION"
                },
                "socialMediaRadar": {
                    "platform": "Value Investing Subreddit / Omaha Watch",
                    "sentimentScore": 91, "sentimentTrend": "+23% Cash hoarding certainty",
                    "whaleFlows": "Value hedge funds mirroring Berkshire conservative stance into elevated multiples.",
                    "retailPositioning": "Unanimous agreement among institutional analysts."
                },
                "riskMitigation": "Safe, institutional-grade probability arbitrage on Polymarket."
            }
        },
        {
            "id": "fin-m-06", "rank": 6,
            "title": "Will European Central Bank cut interest rates by 50 bps at next governing council meeting?",
            "slug": "ecb-cut-rates-50bps-next-governing-council",
            "volume": "$48,900,000", "volumeRaw": 48900000, "volumeLabel": "30-Day Volume",
            "liquidity": "$10,100,000", "endDate": "End of Month 2:15 PM CET",
            "outcomes": [{"name": "YES", "price": 0.34, "pct": 34}, {"name": "NO", "price": 0.66, "pct": 66}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.6% EV+", "impliedProb": 66, "fairValueProb": 78.5,
                "targetExit": "$0.82 (+24.2% gain on NO)", "stopLoss": "$0.52",
                "macroStrategy": "Despite German stagnation, ECB hawks (Schnabel, Nagel, Holzmann) command a disciplined majority favoring predictable 25 bps decrements over jumbo cuts to prevent premature euro depreciation.",
                "newsCatalyst": {
                    "headline": "Financial Times: ECB Governing Council members push back against jumbo 50 bps rate cut calls",
                    "source": "FT Frankfurt Central Banking", "time": "2d ago", "impact": "MEASURED EASING"
                },
                "socialMediaRadar": {
                    "platform": "Eurozone Macro Chat / FX Wire Pro",
                    "sentimentScore": 79, "sentimentTrend": "+21% 25 bps consensus",
                    "whaleFlows": "Euribor futures curve fully pricing 25 bps with zero expectation of 50 bps.",
                    "retailPositioning": "Retail conflating German recession with ECB panic rate cuts."
                },
                "riskMitigation": "Bet NO on 50 bps cut; highly mispriced retail fear premium."
            }
        },
        {
            "id": "fin-m-07", "rank": 7,
            "title": "Will US Q3/Q4 Real GDP Growth be finalized above 2.8% annualized?",
            "slug": "us-real-gdp-finalized-above-28-annualized",
            "volume": "$63,700,000", "volumeRaw": 63700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$13,500,000", "endDate": "End of Month 8:30 AM EST",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.1% EV+", "impliedProb": 62, "fairValueProb": 73.0,
                "targetExit": "$0.78 (+25.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Atlanta Fed GDPNow forecast tracks at 2.9% to 3.1%. Consumer expenditure resilience and AI corporate infrastructure outlays continue delivering robust US exceptionalism growth.",
                "newsCatalyst": {
                    "headline": "Federal Reserve Bank of Atlanta: GDPNow model projects real GDP growth at 2.9% for latest benchmark",
                    "source": "Atlanta Fed GDPNow Service", "time": "3d ago", "impact": "GROWTH RESILIENCE"
                },
                "socialMediaRadar": {
                    "platform": "Macro Alf / Hedge Fund Research Briefs",
                    "sentimentScore": 81, "sentimentTrend": "+17% US exceptionalism",
                    "whaleFlows": "Long US equities vs short Europe/EM equity pairs.",
                    "retailPositioning": "Persistent retail recession expectations proven consistently wrong."
                },
                "riskMitigation": "Hold YES into official Bureau of Economic Analysis revision."
            }
        },
        {
            "id": "fin-m-08", "rank": 8,
            "title": "Will China's CSI 300 Index record a monthly gain exceeding +8.0%?",
            "slug": "china-csi300-index-monthly-gain-exceed-8pct",
            "volume": "$59,400,000", "volumeRaw": 59400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$12,400,000", "endDate": "End of Month 3:00 PM CST",
            "outcomes": [{"name": "YES", "price": 0.53, "pct": 53}, {"name": "NO", "price": 0.47, "pct": 47}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.8% EV+", "impliedProb": 53, "fairValueProb": 62.5,
                "targetExit": "$0.70 (+32.0% gain)", "stopLoss": "$0.40",
                "macroStrategy": "People's Bank of China monetary injection facilities and Central Huijin sovereign buying backstop domestic equities. Margin debt expansion in Shenzhen indicates domestic retail re-engagement.",
                "newsCatalyst": {
                    "headline": "Caixin Global: State-backed funds expand ETF allocations across onshore A-share equities",
                    "source": "Caixin Macro & Markets", "time": "2d ago", "impact": "STATE LIQUIDITY BID"
                },
                "socialMediaRadar": {
                    "platform": "WeChat Finance Channels / Asian Macro Desk",
                    "sentimentScore": 76, "sentimentTrend": "+18% Stimulus optimism",
                    "whaleFlows": "Global hedge funds covering Chinese equity short positions and buying offshore call options.",
                    "retailPositioning": "Retail participation returning with daily turnover crossing 2 Trillion Yuan."
                },
                "riskMitigation": "Size moderately; protect profits if US announces escalated export controls."
            }
        },
        {
            "id": "fin-m-09", "rank": 9,
            "title": "Will the UK FTSE 100 hit an all-time record closing high this month?",
            "slug": "uk-ftse-100-all-time-record-close-month",
            "volume": "$42,700,000", "volumeRaw": 42700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$8,900,000", "endDate": "End of Month 4:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.2% EV+", "impliedProb": 61, "fairValueProb": 71.0,
                "targetExit": "$0.76 (+24.5% gain)", "stopLoss": "$0.48",
                "macroStrategy": "FTSE 100 index composition (78% overseas revenue exposure in commodities, aerospace, and pharmaceuticals) benefits tremendously from stable sterling and global resource dividend yields.",
                "newsCatalyst": {
                    "headline": "London Stock Exchange: Energy and mining blue-chips drive FTSE 100 dividend yields above 3.8%",
                    "source": "LSE Market Analytics", "time": "3d ago", "impact": "VALUE INFLOWS"
                },
                "socialMediaRadar": {
                    "platform": "City of London Brokers / Telegraph Business",
                    "sentimentScore": 81, "sentimentTrend": "+16% Value rotation",
                    "whaleFlows": "Income funds reallocating out of high-valuation growth into cash-generative UK multinationals.",
                    "retailPositioning": "UK retail sentiment depressed, providing an underappreciated valuation discount."
                },
                "riskMitigation": "Favorable risk-reward; trail stop-loss upward as FTSE nears record highs."
            }
        },
        {
            "id": "fin-m-10", "rank": 10,
            "title": "Will Global Corporate Default Rate remain below 4.0% through the end of the year?",
            "slug": "global-corporate-default-rate-below-4pct",
            "volume": "$38,100,000", "volumeRaw": 38100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$7,600,000", "endDate": "End of Month 5:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.6% EV+", "impliedProb": 76, "fairValueProb": 87.0,
                "targetExit": "$0.90 (+18.4% gain)", "stopLoss": "$0.64",
                "macroStrategy": "S&P and Moody's trailing 12-month speculative-grade default rate peaked at 4.1% and has now cooled to 3.6%. Proactive maturity wall extensions in 2024 ensure benign credit distress into 2026.",
                "newsCatalyst": {
                    "headline": "Moody's Ratings: Speculative-grade corporate default trajectory downgraded on successful loan refinancings",
                    "source": "Moody's Credit Research", "time": "4d ago", "impact": "CREDIT HEALTH"
                },
                "socialMediaRadar": {
                    "platform": "Distressed Debt Network / Leveraged Commentary",
                    "sentimentScore": 87, "sentimentTrend": "+20% Credit safety",
                    "whaleFlows": "Private credit direct lenders absorbing distressed tranches before public default trigger.",
                    "retailPositioning": "Retail credit fears unsubstantiated by underlying corporate balance sheet data."
                },
                "riskMitigation": "High probability statistical arbitrage on Polymarket YES outcome."
            }
        }
    ]
}
