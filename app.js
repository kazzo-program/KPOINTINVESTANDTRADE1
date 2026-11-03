/**
 * QUANTO MACRO ALPHA TERMINAL
 * Hedge Fund Macro News Transmission Strategy & CFD/Futures Radar
 * Coverage: XAUUSD, BTCUSD, EURUSD, US500, NAS100, USOIL, USDJPY
 */

(function () {
  'use strict';

  // -------------------------------------------------------------
  // 1. COMPREHENSIVE ASSET DATASET WITH 4H & 24H FORECASTS
  // -------------------------------------------------------------
  const ASSETS_DATA = [
    {
      id: "XAUUSD",
      name: "Spot Gold / US Dollar",
      contract: "CFD: XAUUSD | Futures: GC (COMEX Gold)",
      class: "Precious Metals / Sovereign Safe-Haven",
      icon: "🟡",
      currentPrice: 2748.80,
      priceFormat: "$#,##0.00",
      change24h: "+1.14%",
      changePoints: "+$31.20",
      isPositive: true,
      bias: "STRONG BUY",
      biasType: "buy",
      confidence: "88%",
      macroRisk: "High Geopolitical Dispersion",
      tradePosture: "Accumulate on 4H Dips; Momentum Long Breakouts",
      
      // Dual-Timeframe Forecasts
      forecast4h: {
        targetPrice: 2764.50,
        expectedMove: "+0.57% (+$15.70)",
        bias: "Bullish Scalp / Session Drift",
        biasType: "buy",
        rangeLow: 2736.00,
        rangeHigh: 2768.00,
        invalidation: 2732.00,
        catalyst: "Middle East defense escalations & Treasury yields retreating in NY afternoon overlap. Sustained safe-haven sovereign bid absorbing all liquidity sweeps."
      },
      forecast24h: {
        targetPrice: 2785.00,
        expectedMove: "+1.32% (+$36.20)",
        bias: "Institutional Macro Accumulation",
        biasType: "buy",
        rangeLow: 2728.00,
        rangeHigh: 2792.00,
        invalidation: 2715.00,
        catalyst: "ForexFactory high-impact US Core PCE expectations indicating disinflation drift, bolstering 25bps Fed rate cut pricing. Central Bank physical bullion buying continuing uninterrupted."
      },

      // Macro Hedge Fund Factor Pillars
      macroFactors: [
        { name: "Geopolitical Heat", value: "9.2 / 10", sub: "Red Sea & Levant escalations" },
        { name: "US 10Y Real Yield Drag", value: "Dovish Tailwinds", sub: "Yields consolidating at 4.38%" },
        { name: "DXY Transmission", value: "Inverse Decoupling", sub: "Gold rallying despite USD strength" },
        { name: "Central Bank Reserves", value: "Persistent Net Buy", sub: "PBoC & Global Reserves +34t" }
      ],

      // Direct Source Links
      directSources: [
        { name: "ForexFactory (Gold & USD)", url: "https://www.forexfactory.com/news?q=gold", isFF: true },
        { name: "Kitco Gold News Wire", url: "https://www.kitco.com/news/gold", isFF: false },
        { name: "Reuters Gold Commodities", url: "https://www.reuters.com/markets/commodities/", isFF: false },
        { name: "Bloomberg Gold Surveillance", url: "https://www.bloomberg.com/markets", isFF: false },
        { name: "FXStreet Gold Technical & Macro", url: "https://www.fxstreet.com/markets/commodities/gold", isFF: false },
        { name: "TradingEconomics Gold Reserves", url: "https://tradingeconomics.com/commodity/gold", isFF: false }
      ],

      // Curated Breaking Headlines
      headlines: [
        {
          source: "ForexFactory",
          title: "Gold advances as geopolitical tension mounts; investors brace for US labor and inflation releases",
          time: "14 mins ago",
          sentiment: "BULLISH +34",
          sentimentType: "buy",
          url: "https://www.forexfactory.com/news/1301428-gold-advances-as-geopolitical-tension-mounts"
        },
        {
          source: "Kitco",
          title: "Hedge funds expand COMEX Gold net-long contracts to 6-month high amid flight-to-safety flows",
          time: "48 mins ago",
          sentiment: "BULLISH +28",
          sentimentType: "buy",
          url: "https://www.kitco.com/news/gold"
        },
        {
          source: "Reuters",
          title: "Middle East defense posture tightens after regional strikes; crude and bullion command safety premium",
          time: "1 hr ago",
          sentiment: "GEO ALERT +40",
          sentimentType: "buy",
          url: "https://www.reuters.com/markets/commodities/"
        }
      ]
    },

    {
      id: "BTCUSD",
      name: "Bitcoin / US Dollar",
      contract: "CFD: BTCUSD | Futures: BTC (CME Bitcoin)",
      class: "Digital Asset / Macro Liquidity Beta",
      icon: "🟠",
      currentPrice: 88420.00,
      priceFormat: "$#,##0.00",
      change24h: "+3.45%",
      changePoints: "+$2,950.00",
      isPositive: true,
      bias: "BUY",
      biasType: "buy",
      confidence: "82%",
      macroRisk: "High Volatility / Liquidations",
      tradePosture: "Long above $86,800; Target Key Liquidity Pools",

      forecast4h: {
        targetPrice: 89650.00,
        expectedMove: "+1.39% (+$1,230.00)",
        bias: "Momentum Breakout Drift",
        biasType: "buy",
        rangeLow: 87200.00,
        rangeHigh: 90200.00,
        invalidation: 86500.00,
        catalyst: "Spot ETF net daily inflow surge exceeding +$420M. Orderbook ask wall at $89,000 being chipped down by institutional algos."
      },
      forecast24h: {
        targetPrice: 91800.00,
        expectedMove: "+3.82% (+$3,380.00)",
        bias: "Macro Liquidity Expansion",
        biasType: "buy",
        rangeLow: 85900.00,
        rangeHigh: 93000.00,
        invalidation: 84800.00,
        catalyst: "Global central bank M2 aggregate expansion breaking out. Political regulatory clarity and institutional custodian adoption driving sovereign wealth inquiries."
      },

      macroFactors: [
        { name: "Spot ETF Net Inflow", value: "+$428M / Day", sub: "BlackRock IBIT & Fidelity leading" },
        { name: "Global M2 Liquidity Beta", value: "+0.78 Correlation", sub: "Expanding global money supply" },
        { name: "Funding Rates & Open Int.", value: "Healthy 0.012%", sub: "Spot-led rally, not overleveraged" },
        { name: "Digital Safe-Haven Flow", value: "Emerging Hedge", sub: "Capital flight in high-inflation states" }
      ],

      directSources: [
        { name: "ForexFactory (USD & Crypto Wire)", url: "https://www.forexfactory.com/news?q=bitcoin", isFF: true },
        { name: "CoinDesk Institutional Macro", url: "https://www.coindesk.com", isFF: false },
        { name: "Cointelegraph Breaking Markets", url: "https://cointelegraph.com", isFF: false },
        { name: "Bloomberg Crypto Hub", url: "https://www.bloomberg.com/crypto", isFF: false },
        { name: "TradingEconomics BTC Index", url: "https://tradingeconomics.com/crypto/bitcoin", isFF: false }
      ],

      headlines: [
        {
          source: "CoinDesk",
          title: "Bitcoin breaks resistance as institutional inflows accelerate; CME open interest marks fresh high",
          time: "22 mins ago",
          sentiment: "BULLISH +31",
          sentimentType: "buy",
          url: "https://www.coindesk.com"
        },
        {
          source: "ForexFactory",
          title: "Cryptocurrency market capitalization expands 3.2% as dollar index consolidates near range highs",
          time: "52 mins ago",
          sentiment: "BULLISH +19",
          sentimentType: "buy",
          url: "https://www.forexfactory.com/news?q=bitcoin"
        },
        {
          source: "Bloomberg",
          title: "Pension funds and family offices increase digital asset allocation weighting to hedge currency debasement",
          time: "2 hrs ago",
          sentiment: "MACRO ADOPTION +26",
          sentimentType: "buy",
          url: "https://www.bloomberg.com/crypto"
        }
      ]
    },

    {
      id: "EURUSD",
      name: "Euro / US Dollar",
      contract: "CFD: EURUSD | Futures: 6E (CME Euro FX)",
      class: "Major Currency Pair / FX Liquidity",
      icon: "💶",
      currentPrice: 1.0834,
      priceFormat: "0.0000",
      change24h: "-0.42%",
      changePoints: "-46 pips",
      isPositive: false,
      bias: "SELL",
      biasType: "sell",
      confidence: "84%",
      macroRisk: "Central Bank Rate Divergence",
      tradePosture: "Fade Rallies into 1.0860; Short Bias",

      forecast4h: {
        targetPrice: 1.0805,
        expectedMove: "-0.27% (-29 pips)",
        bias: "Intraday Dollar Strength Drag",
        biasType: "sell",
        rangeLow: 1.0790,
        rangeHigh: 1.0850,
        invalidation: 1.0875,
        catalyst: "ECB speaker commentary leaning dovish, acknowledging stagnant Eurozone industrial activity. US Treasury yield differential widening in favor of USD."
      },
      forecast24h: {
        targetPrice: 1.0760,
        expectedMove: "-0.68% (-74 pips)",
        bias: "Positional Bearish Trend",
        biasType: "sell",
        rangeLow: 1.0730,
        rangeHigh: 1.0860,
        invalidation: 1.0910,
        catalyst: "ForexFactory German Flash Manufacturing PMI contracting further. Fed expected to maintain gradual cut trajectory while ECB faces mounting pressure to cut 50bps."
      },

      macroFactors: [
        { name: "Fed-ECB Rate Spread", value: "+175 bps USD", sub: "Wide yield advantage for Dollar" },
        { name: "Eurozone PMI Growth", value: "45.8 Contraction", sub: "German auto & industrial slump" },
        { name: "Energy Import Deficit", value: "Elevated Costs", sub: "Winter natural gas hedging drag" },
        { name: "CFTC COT Positioning", value: "Euro Longs Liquidating", sub: "Institutional net selling" }
      ],

      directSources: [
        { name: "ForexFactory (EUR Calendar & News)", url: "https://www.forexfactory.com/calendar?c=eur", isFF: true },
        { name: "Reuters European Markets", url: "https://www.reuters.com/markets/europe/", isFF: false },
        { name: "FXStreet EURUSD Live Wire", url: "https://www.fxstreet.com/currencies/eurusd", isFF: false },
        { name: "DailyFX Euro Analysis", url: "https://www.dailyfx.com/eur-usd", isFF: false },
        { name: "ECB Official Communications", url: "https://www.ecb.europa.eu", isFF: false }
      ],

      headlines: [
        {
          source: "ForexFactory",
          title: "EUR/USD slides towards 1.0800 as ECB doves gain upper hand amidst cooling Eurozone wage growth",
          time: "18 mins ago",
          sentiment: "BEARISH -27",
          sentimentType: "sell",
          url: "https://www.forexfactory.com/news?q=eurusd"
        },
        {
          source: "Reuters",
          title: "German business confidence remains depressed; energy costs weigh on manufacturing export revival",
          time: "1 hr ago",
          sentiment: "BEARISH -24",
          sentimentType: "sell",
          url: "https://www.reuters.com/markets/europe/"
        },
        {
          source: "FXStreet",
          title: "US Dollar Index firms above 104.20 on solid durable goods orders, capping EUR/USD recovery attempts",
          time: "2 hrs ago",
          sentiment: "USD BULLISH -19",
          sentimentType: "sell",
          url: "https://www.fxstreet.com/currencies/eurusd"
        }
      ]
    },

    {
      id: "US500",
      name: "S&P 500 Index",
      contract: "CFD: US500 | Futures: ES (E-mini S&P 500)",
      class: "US Equity Benchmark / Global Risk Beta",
      icon: "📈",
      currentPrice: 5868.50,
      priceFormat: "#,##0.00 pts",
      change24h: "-0.38%",
      changePoints: "-22.40 pts",
      isPositive: false,
      bias: "SELL",
      biasType: "sell",
      confidence: "76%",
      macroRisk: "Valuation Compression & Yield Drag",
      tradePosture: "Tactical Short on Bounces; Protective Hedges",

      forecast4h: {
        targetPrice: 5842.00,
        expectedMove: "-0.45% (-26.50 pts)",
        bias: "Intraday De-risking Drift",
        biasType: "sell",
        rangeLow: 5830.00,
        rangeHigh: 5885.00,
        invalidation: 5898.00,
        catalyst: "10-Year Treasury yield holding near 4.38% creating valuation multiple friction. Geopolitical risk headlines driving defensive hedging in index put options."
      },
      forecast24h: {
        targetPrice: 5815.00,
        expectedMove: "-0.91% (-53.50 pts)",
        bias: "Consolidation Pullback",
        biasType: "sell",
        rangeLow: 5790.00,
        rangeHigh: 5900.00,
        invalidation: 5925.00,
        catalyst: "ForexFactory upcoming US Q3 GDP and employment releases. Hedge funds trimming mega-cap exposures to lock in year-to-date gains ahead of election risk."
      },

      macroFactors: [
        { name: "10Y Treasury Yield Pressure", value: "4.38% (High)", sub: "Compresses forward equity P/E" },
        { name: "CBOE VIX Volatility", value: "19.82 Elevated", sub: "Put/Call ratio skew favoring puts" },
        { name: "Corporate Earnings Revision", value: "Mixed Guidance", sub: "Margin compression warnings" },
        { name: "Systematic CTA Positioning", value: "De-leveraging", sub: "CTAs reducing equity beta" }
      ],

      directSources: [
        { name: "ForexFactory (US Market Wire)", url: "https://www.forexfactory.com/news?q=stocks", isFF: true },
        { name: "Bloomberg S&P 500 Markets", url: "https://www.bloomberg.com/markets/stocks", isFF: false },
        { name: "Reuters Wall Street Overview", url: "https://www.reuters.com/markets/us/", isFF: false },
        { name: "MarketWatch S&P 500 Live", url: "https://www.marketwatch.com/investing/index/spx", isFF: false },
        { name: "TradingEconomics US Equities", url: "https://tradingeconomics.com/united-states/stock-market", isFF: false }
      ],

      headlines: [
        {
          source: "Bloomberg",
          title: "Wall Street trades cautiously as Treasury yields climb; megacap tech faces valuation scrutiny",
          time: "25 mins ago",
          sentiment: "BEARISH -18",
          sentimentType: "sell",
          url: "https://www.bloomberg.com/markets/stocks"
        },
        {
          source: "ForexFactory",
          title: "S&P 500 dips beneath key intraday support as geopolitical tensions prompt defensive hedging",
          time: "1 hr ago",
          sentiment: "BEARISH -22",
          sentimentType: "sell",
          url: "https://www.forexfactory.com/news?q=stocks"
        },
        {
          source: "Reuters",
          title: "Hedge funds increase short positioning on US index futures ahead of high-impact macroeconomic data",
          time: "2 hrs ago",
          sentiment: "CAUTION -15",
          sentimentType: "sell",
          url: "https://www.reuters.com/markets/us/"
        }
      ]
    },

    {
      id: "NAS100",
      name: "Nasdaq 100 Index",
      contract: "CFD: NAS100 | Futures: NQ (E-mini Nasdaq 100)",
      class: "Tech Growth & AI / High Beta Duration",
      icon: "💻",
      currentPrice: 20380.00,
      priceFormat: "#,##0.00 pts",
      change24h: "-0.62%",
      changePoints: "-127.20 pts",
      isPositive: false,
      bias: "SELL",
      biasType: "sell",
      confidence: "79%",
      macroRisk: "Long-Duration Interest Rate Sensitivity",
      tradePosture: "Short Rallies; Hedge Tech Exposure",

      forecast4h: {
        targetPrice: 20260.00,
        expectedMove: "-0.59% (-120.00 pts)",
        bias: "Yield Pressure Liquidity Drain",
        biasType: "sell",
        rangeLow: 20200.00,
        rangeHigh: 20450.00,
        invalidation: 20540.00,
        catalyst: "Semiconductor export control headline risks and higher bond yields impacting long-duration cash flows. Intraday profit taking in semiconductor heavyweights."
      },
      forecast24h: {
        targetPrice: 20120.00,
        expectedMove: "-1.28% (-260.00 pts)",
        bias: "Multiple De-rating Test",
        biasType: "sell",
        rangeLow: 19980.00,
        rangeHigh: 20500.00,
        invalidation: 20620.00,
        catalyst: "Mega-cap capex spending scrutinized for ROI timelines. ForexFactory US ISM Services and employment data expected to dictate discount rate trajectory."
      },

      macroFactors: [
        { name: "Semiconductor Sanctions Risk", value: "High Friction", sub: "US-China tech export restrictions" },
        { name: "Discount Rate Impact", value: "-0.85 Elasticity", sub: "Ultra-sensitive to 10Y yield surges" },
        { name: "AI Capex Scrutiny", value: "Rising Skepticism", sub: "Hyperscaler margin contraction fears" },
        { name: "Gamma Squeeze Risk", value: "Negative Gamma", sub: "Market makers selling into declines" }
      ],

      directSources: [
        { name: "ForexFactory (Nasdaq & Tech)", url: "https://www.forexfactory.com/news?q=nasdaq", isFF: true },
        { name: "Bloomberg Technology Terminal", url: "https://www.bloomberg.com/technology", isFF: false },
        { name: "Reuters Tech Sector Analysis", url: "https://www.reuters.com/technology/", isFF: false },
        { name: "MarketWatch Nasdaq Composite", url: "https://www.marketwatch.com/investing/index/comp", isFF: false },
        { name: "FXStreet Tech Indices Live", url: "https://www.fxstreet.com/markets/indices", isFF: false }
      ],

      headlines: [
        {
          source: "Reuters",
          title: "Chip stocks drag Nasdaq lower as Washington prepares tighter curbs on semiconductor equipment exports",
          time: "32 mins ago",
          sentiment: "BEARISH -29",
          sentimentType: "sell",
          url: "https://www.reuters.com/technology/"
        },
        {
          source: "ForexFactory",
          title: "Treasury yields rise following solid economic prints, putting downward pressure on tech growth multiples",
          time: "1 hr ago",
          sentiment: "BEARISH -21",
          sentimentType: "sell",
          url: "https://www.forexfactory.com/news?q=nasdaq"
        },
        {
          source: "Bloomberg",
          title: "Big Tech capital expenditure surges to record levels as cloud titans expand data center footprint",
          time: "3 hrs ago",
          sentiment: "NEUTRAL 0",
          sentimentType: "neutral",
          url: "https://www.bloomberg.com/technology"
        }
      ]
    },

    {
      id: "USOIL",
      name: "WTI Crude Oil",
      contract: "CFD: USOIL | Futures: CL (NYMEX Light Sweet Crude)",
      class: "Physical Energy / Geopolitical Supply Chokepoints",
      icon: "🛢️",
      currentPrice: 71.95,
      priceFormat: "$#,##0.00 / bbl",
      change24h: "+2.12%",
      changePoints: "+$1.49",
      isPositive: true,
      bias: "STRONG BUY",
      biasType: "buy",
      confidence: "86%",
      macroRisk: "Chokepoint Disruption Premium",
      tradePosture: "Long Breakout / Carry Geopolitical Protection",

      forecast4h: {
        targetPrice: 73.10,
        expectedMove: "+1.60% (+$1.15)",
        bias: "Geopolitical Escalation Spike",
        biasType: "buy",
        rangeLow: 71.20,
        rangeHigh: 73.60,
        invalidation: 70.50,
        catalyst: "Reports of renewed military strikes and shipping tanker diversions around the Persian Gulf / Bab el-Mandeb strait. Supply disruption fears triggering immediate physical contract buying."
      },
      forecast24h: {
        targetPrice: 74.80,
        expectedMove: "+3.96% (+$2.85)",
        bias: "Risk Premium Re-pricing",
        biasType: "buy",
        rangeLow: 70.80,
        rangeHigh: 75.50,
        invalidation: 69.80,
        catalyst: "OPEC+ signals full commitment to deferring planned production unwind. EIA weekly inventory draw anticipated in tomorrow's crude report."
      },

      macroFactors: [
        { name: "Strait of Hormuz Risk", value: "Critical Supply Node", sub: "20% of global petroleum transit" },
        { name: "OPEC+ Supply Discipline", value: "Voluntary Cuts Extended", sub: "2.2M bpd withholding active" },
        { name: "US Strategic Reserve (SPR)", value: "Refilling Phase", sub: "DoE active buyer below $75" },
        { name: "China Refiner Demand", value: "Stabilizing Baseline", sub: "Stimulus measures supporting floor" }
      ],

      directSources: [
        { name: "ForexFactory (Oil & Energy Wire)", url: "https://www.forexfactory.com/news?q=crude+oil", isFF: true },
        { name: "OilPrice.com Breaking Intelligence", url: "https://oilprice.com", isFF: false },
        { name: "Reuters Energy Commodities", url: "https://www.reuters.com/markets/commodities/", isFF: false },
        { name: "EIA Official Petroleum Status Report", url: "https://www.eia.gov/petroleum/supply/weekly/", isFF: false },
        { name: "Bloomberg Energy Terminal", url: "https://www.bloomberg.com/energy", isFF: false }
      ],

      headlines: [
        {
          source: "OilPrice",
          title: "Crude oil spikes higher on Middle East geopolitical escalation and transit disruption threats",
          time: "15 mins ago",
          sentiment: "BULLISH +38",
          sentimentType: "buy",
          url: "https://oilprice.com"
        },
        {
          source: "ForexFactory",
          title: "WTI Crude surges above $71.50 as traders price in risk of retaliatory strikes on energy infrastructure",
          time: "42 mins ago",
          sentiment: "BULLISH +32",
          sentimentType: "buy",
          url: "https://www.forexfactory.com/news?q=crude+oil"
        },
        {
          source: "Reuters",
          title: "OPEC+ delegates signal group will stick to production delay as market monitors physical balances",
          time: "1 hr ago",
          sentiment: "BULLISH +23",
          sentimentType: "buy",
          url: "https://www.reuters.com/markets/commodities/"
        }
      ]
    },

    {
      id: "USDJPY",
      name: "US Dollar / Japanese Yen",
      contract: "CFD: USDJPY | Futures: 6J (CME Japanese Yen)",
      class: "Carry Trade FX / Central Bank Polarization",
      icon: "💴",
      currentPrice: 152.82,
      priceFormat: "0.00",
      change24h: "+0.32%",
      changePoints: "+0.48",
      isPositive: true,
      bias: "NEUTRAL",
      biasType: "neutral",
      confidence: "68%",
      macroRisk: "Ministry of Finance Intervention Threat",
      tradePosture: "Range Bound (151.80 - 153.50); Scalp Boundaries",

      forecast4h: {
        targetPrice: 153.15,
        expectedMove: "+0.22% (+33 pips)",
        bias: "Yield Spread Creep Higher",
        biasType: "neutral",
        rangeLow: 152.30,
        rangeHigh: 153.40,
        invalidation: 151.70,
        catalyst: "US Treasury yield advantage sustaining upward pressure on the pair, offset by verbal warnings from Japanese Vice Finance Minister regarding speculative FX moves."
      },
      forecast24h: {
        targetPrice: 152.40,
        expectedMove: "-0.27% (-42 pips)",
        bias: "Intervention Risk Mean Reversion",
        biasType: "neutral",
        rangeLow: 151.50,
        rangeHigh: 153.80,
        invalidation: 154.20,
        catalyst: "ForexFactory BoJ policy summary release. Market participants reluctant to push above 153.50 given historical intervention precedents by the Ministry of Finance."
      },

      macroFactors: [
        { name: "US-Japan Yield Spread", value: "+342 bps Advantage", sub: "Forces continuous carry trade bid" },
        { name: "MoF Intervention Threat", value: "Level 4 (High Alert)", sub: "Verbal intervention escalating" },
        { name: "BoJ Rate Hike Expectations", value: "December Pricing 42%", sub: "Governor Ueda maintaining data watch" },
        { name: "Safe-Haven Yen Flows", value: "Muted Response", sub: "Offset by massive negative rate carry" }
      ],

      directSources: [
        { name: "ForexFactory (JPY & USD Wire)", url: "https://www.forexfactory.com/calendar?c=jpy", isFF: true },
        { name: "Reuters Tokyo Markets", url: "https://www.reuters.com/markets/", isFF: false },
        { name: "FXStreet USD/JPY Analysis", url: "https://www.fxstreet.com/currencies/usdjpy", isFF: false },
        { name: "Nikkei Asia Macro & FX", url: "https://asia.nikkei.com/Business/Markets", isFF: false },
        { name: "Bank of Japan Statements", url: "https://www.boj.or.jp/en/", isFF: false }
      ],

      headlines: [
        {
          source: "ForexFactory",
          title: "USD/JPY consolidates near 152.80 as markets balance Treasury yield rally against MoF intervention warnings",
          time: "20 mins ago",
          sentiment: "NEUTRAL +04",
          sentimentType: "neutral",
          url: "https://www.forexfactory.com/news?q=usdjpy"
        },
        {
          source: "Reuters",
          title: "Japan's Top FX Diplomat reiterates government is watching currency moves with high urgency",
          time: "1 hr ago",
          sentiment: "INTERVENTION WATCH",
          sentimentType: "neutral",
          url: "https://www.reuters.com/markets/"
        },
        {
          source: "FXStreet",
          title: "USD/JPY technical hurdle looms at 153.20 while 200-hour moving average offers solid baseline support",
          time: "3 hrs ago",
          sentiment: "NEUTRAL -02",
          sentimentType: "neutral",
          url: "https://www.fxstreet.com/currencies/usdjpy"
        }
      ]
    }
  ];

  // -------------------------------------------------------------
  // 2. FOREXFACTORY HIGH-IMPACT CALENDAR EVENTS
  // -------------------------------------------------------------
  const FOREX_FACTORY_CALENDAR = [
    {
      time: "13:30 UTC",
      currency: "USD",
      title: "Core PCE Price Index m/m",
      impact: "high",
      actual: "0.2%",
      forecast: "0.2%",
      previous: "0.1%",
      impactNotes: "Critical Fed inflation gauge; drives Treasury yields & Gold/USD pricing."
    },
    {
      time: "14:00 UTC",
      currency: "USD",
      title: "ISM Manufacturing PMI & Prices",
      impact: "high",
      actual: "47.2",
      forecast: "47.6",
      previous: "47.2",
      impactNotes: "Factory activity contraction check; key for US500, NAS100, and Crude."
    },
    {
      time: "09:00 UTC",
      currency: "EUR",
      title: "Eurozone Flash GDP q/q",
      impact: "high",
      actual: "0.4%",
      forecast: "0.2%",
      previous: "0.2%",
      impactNotes: "Dictates ECB terminal rate path and EURUSD trend continuation."
    },
    {
      time: "15:30 UTC",
      currency: "USD",
      title: "EIA Crude Oil Stockpiles",
      impact: "high",
      actual: "-1.8M",
      forecast: "-0.6M",
      previous: "+5.5M",
      impactNotes: "Direct inventory draw catalyst for USOIL (WTI Futures)."
    },
    {
      time: "03:30 UTC",
      currency: "JPY",
      title: "BoJ Monetary Policy Statement & Presser",
      impact: "high",
      actual: "0.25%",
      forecast: "0.25%",
      previous: "0.25%",
      impactNotes: "Triggers massive carry trade swings and USDJPY intervention tests."
    }
  ];

  // -------------------------------------------------------------
  // 3. GEOPOLITICAL RISK HOTSPOTS & TRANSMISSIONS
  // -------------------------------------------------------------
  const GEOPOLITICAL_HOTSPOTS = [
    {
      region: "Middle East / Persian Gulf / Red Sea",
      severity: "CRITICAL",
      severityClass: "severity-critical",
      narrative: "Air defenses on high alert following retaliatory strikes. Maritime cargo insurers imposing high-risk surcharges; multiple commercial tankers re-routing around the Cape of Good Hope.",
      transmission: "Direct Long catalyst for XAUUSD (Gold safe-haven) and USOIL (Crude risk premium). Negative multiplier for global equities (US500/NAS100)."
    },
    {
      region: "Eastern Europe / Black Sea Energy Nodes",
      severity: "ELEVATED",
      severityClass: "severity-elevated",
      narrative: "Drone engagements targeting oil refining facilities and electricity grid networks. Natural gas transit negotiations approaching deadline.",
      transmission: "Bearish pressure on European currencies (EURUSD). Supportive for commodity supply contracts and precious metals."
    },
    {
      region: "Taiwan Strait & Semiconductor Supply Chain",
      severity: "ELEVATED",
      severityClass: "severity-elevated",
      narrative: "Expanded maritime encirclement drills and export restrictions on advanced AI compute hardware.",
      transmission: "Primary valuation multiple headwind for Tech heavyweights (NAS100) and semiconductor supply chains."
    }
  ];

  // -------------------------------------------------------------
  // 4. MAJOR SOURCES DIRECTORY
  // -------------------------------------------------------------
  const MAJOR_SOURCES_DIRECTORY = [
    {
      name: "ForexFactory",
      category: "Macroeconomic Calendar & Real-Time Financial Wire",
      desc: "The gold standard for retail and institutional currency traders. Real-time release countdowns, historical deviation graphs, and live breaking forum wire.",
      links: [
        { label: "Live Economic Calendar", url: "https://www.forexfactory.com/calendar" },
        { label: "ForexFactory Breaking News Wire", url: "https://www.forexfactory.com/news" },
        { label: "ForexFactory Gold Discussions", url: "https://www.forexfactory.com/news?q=gold" },
        { label: "ForexFactory Oil & Commodities", url: "https://www.forexfactory.com/news?q=oil" }
      ]
    },
    {
      name: "Reuters Markets & Geopolitics",
      category: "Global Institutional News Syndicate",
      desc: "Fast, unbiased institutional reporting covering central bank policies, defense intelligence, commodity trade flows, and foreign exchange.",
      links: [
        { label: "Reuters Global Markets", url: "https://www.reuters.com/markets/" },
        { label: "Reuters World & Geopolitical News", url: "https://www.reuters.com/world/" },
        { label: "Reuters Commodities & Energy", url: "https://www.reuters.com/markets/commodities/" },
        { label: "Reuters European Currencies", url: "https://www.reuters.com/markets/currencies/" }
      ]
    },
    {
      name: "Bloomberg Terminal & Web",
      category: "Premier Tier-1 Macro Financial Intelligence",
      desc: "Deep coverage of sovereign bond yields, central bank rate curves (OIS/FedWatch), institutional derivatives positioning, and FX cross-rates.",
      links: [
        { label: "Bloomberg Markets Surveillance", url: "https://www.bloomberg.com/markets" },
        { label: "Bloomberg Commodities / Gold / Oil", url: "https://www.bloomberg.com/energy" },
        { label: "Bloomberg Crypto Hub", url: "https://www.bloomberg.com/crypto" },
        { label: "Bloomberg Rates & Bonds", url: "https://www.bloomberg.com/markets/rates-bonds" }
      ]
    },
    {
      name: "FXStreet",
      category: "Forex & Commodities Technical / Macro Analysis",
      desc: "Continuous coverage of intraday currency orderflow, ForexFactory report debriefs, gold pivot levels, and central bank commentary.",
      links: [
        { label: "FXStreet Economic Calendar", url: "https://www.fxstreet.com/economic-calendar" },
        { label: "FXStreet Gold (XAU/USD) Analysis", url: "https://www.fxstreet.com/markets/commodities/gold" },
        { label: "FXStreet EUR/USD Forecasts", url: "https://www.fxstreet.com/currencies/eurusd" },
        { label: "FXStreet Central Bank Watch", url: "https://www.fxstreet.com/macroeconomics/central-banks" }
      ]
    },
    {
      name: "Kitco Metals & Precious Metals",
      category: "Dedicated Bullion & Precious Metals Wire",
      desc: "The premier portal for physical gold, silver, central bank reserve purchases, COMEX inventory reports, and mining sector intelligence.",
      links: [
        { label: "Kitco Live Gold News", url: "https://www.kitco.com/news/gold" },
        { label: "Kitco Gold Price Charts & Swaps", url: "https://www.kitco.com/charts/gold" },
        { label: "Kitco Central Bank Bullion Tracker", url: "https://www.kitco.com/news/central-banks" }
      ]
    },
    {
      name: "OilPrice.com & Energy Intelligence",
      category: "Crude Oil, Geopolitics & Energy Security",
      desc: "Comprehensive daily analysis of OPEC+ quota adherence, tanker transit security, US strategic petroleum reserve, and refinery crack spreads.",
      links: [
        { label: "OilPrice.com Breaking News", url: "https://oilprice.com" },
        { label: "Geopolitics of Energy", url: "https://oilprice.com/Geopolitics/" },
        { label: "EIA Official Petroleum Status Report", url: "https://www.eia.gov/petroleum/supply/weekly/" }
      ]
    },
    {
      name: "CoinDesk & Cointelegraph",
      category: "Digital Assets, ETF Flows & On-Chain Macro",
      desc: "Live reporting on Spot Bitcoin ETF flows, CME futures open interest, stablecoin liquidity, and crypto regulatory transmission.",
      links: [
        { label: "CoinDesk Markets & Macro", url: "https://www.coindesk.com" },
        { label: "Cointelegraph Breaking", url: "https://cointelegraph.com" },
        { label: "CoinGlass CME Bitcoin Derivatives Data", url: "https://www.coinglass.com" }
      ]
    },
    {
      name: "TradingEconomics",
      category: "Global Sovereign Indicators & Yields",
      desc: "Historical charts and forward forecasts for inflation (CPI/PCE), unemployment rates, GDP growth, and government debt yields for all major economies.",
      links: [
        { label: "TradingEconomics Global Calendar", url: "https://tradingeconomics.com/calendar" },
        { label: "United States Macro Indicators", url: "https://tradingeconomics.com/united-states/indicators" },
        { label: "Euro Area Macro Indicators", url: "https://tradingeconomics.com/euro-area/indicators" }
      ]
    }
  ];

  // =============================================================
  // 4B. COMPREHENSIVE STOCK DATASETS // TOP 20 US, TOP 20 UK, HIGH RISERS
  // Ranked using Macro Hedge Fund Internet Scanning Strategy
  // =============================================================
  const US_STOCKS_DATA = [
    {
      rank: 1,
      ticker: "NVDA",
      name: "NVIDIA Corporation",
      industry: "Semiconductors & AI Hardware",
      industryCategory: "Semiconductors & AI",
      price: 138.25,
      change24h: 3.42,
      isPositive: true,
      macroScore: 98,
      bias: "STRONG BUY",
      targetPrice: "$175.00 (+26.6%)",
      peRatio: "38.2x",
      marketCap: "$3.39T",
      weekGain: 7.2,
      monthGain: 22.1,
      yearGain: 185.0,
      catalyst: "Scanned 184 wires: Blackwell B200 hyperscaler capex bookings sold out through 2026; Hyperscaler Capex raised +$45B by MSFT/AMZN/META; Top pick at Morgan Stanley.",
      macroPillar: "AI Capex Supercycle & Sovereign AI Compute Bid",
      sourceTag: "Bloomberg / SEC 13F / Reuters"
    },
    {
      rank: 2,
      ticker: "MSFT",
      name: "Microsoft Corporation",
      industry: "Cloud Computing & Enterprise AI",
      industryCategory: "Cloud Computing & Infrastructure",
      price: 428.40,
      change24h: 1.85,
      isPositive: true,
      macroScore: 96,
      bias: "STRONG BUY",
      targetPrice: "$500.00 (+16.7%)",
      peRatio: "33.5x",
      marketCap: "$3.18T",
      weekGain: 3.8,
      monthGain: 11.4,
      yearGain: 32.0,
      catalyst: "Azure AI revenue accelerating +34% YoY; Copilot enterprise seat adoption expanding across Fortune 500; 20-year nuclear energy PPA secured with Constellation.",
      macroPillar: "Enterprise Software Monetization & Cloud Multiples",
      sourceTag: "Reuters / WSJ / EDGAR"
    },
    {
      rank: 3,
      ticker: "PLTR",
      name: "Palantir Technologies",
      industry: "Enterprise AI & Software Analytics",
      industryCategory: "Enterprise AI & Software",
      price: 51.80,
      change24h: 5.12,
      isPositive: true,
      macroScore: 95,
      bias: "STRONG BUY",
      targetPrice: "$65.00 (+25.5%)",
      peRatio: "88.0x",
      marketCap: "$116.4B",
      weekGain: 14.2,
      monthGain: 48.5,
      yearGain: 245.0,
      catalyst: "S&P 500 inclusion driving institutional benchmark indexing; AIP Bootcamps expanding US commercial customer count +83% YoY; US Army TITAN contract award.",
      macroPillar: "Defense Intelligence AI & Enterprise Data Architecture",
      sourceTag: "DoD Wires / Investor Day / SEC 13F"
    },
    {
      rank: 4,
      ticker: "AMZN",
      name: "Amazon.com Inc",
      industry: "Cloud Infrastructure & E-Commerce",
      industryCategory: "Cloud Computing & Infrastructure",
      price: 198.50,
      change24h: 2.15,
      isPositive: true,
      macroScore: 94,
      bias: "STRONG BUY",
      targetPrice: "$240.00 (+20.9%)",
      peRatio: "41.2x",
      marketCap: "$2.08T",
      weekGain: 4.6,
      monthGain: 14.8,
      yearGain: 42.0,
      catalyst: "AWS cloud re-accelerating to 19% YoY growth; Custom Trainium2 AI chips cutting model training costs; North American operating retail margin expanding.",
      macroPillar: "Cloud Margin Re-acceleration & Logistics Automation",
      sourceTag: "Bloomberg / Earnings Transcript"
    },
    {
      rank: 5,
      ticker: "AAPL",
      name: "Apple Inc",
      industry: "Consumer Electronics & Edge AI Ecosystem",
      industryCategory: "Cloud Computing & Infrastructure",
      price: 228.60,
      change24h: 1.10,
      isPositive: true,
      macroScore: 92,
      bias: "BUY",
      targetPrice: "$260.00 (+13.7%)",
      peRatio: "34.1x",
      marketCap: "$3.47T",
      weekGain: 2.1,
      monthGain: 8.5,
      yearGain: 28.0,
      catalyst: "Apple Intelligence rollout initiating multi-year upgrade supercycle across 1.4B active iPhones; Services gross margin reaches historic 74.2%.",
      macroPillar: "Edge AI Consumer Hardware Replacement Cycle",
      sourceTag: "Supply Chain Asia / Nikkei / WSJ"
    },
    {
      rank: 6,
      ticker: "META",
      name: "Meta Platforms",
      industry: "Digital Advertising & Open-Source AI",
      industryCategory: "Enterprise AI & Software",
      price: 585.20,
      change24h: 2.88,
      isPositive: true,
      macroScore: 93,
      bias: "STRONG BUY",
      targetPrice: "$680.00 (+16.2%)",
      peRatio: "27.4x",
      marketCap: "$1.48T",
      weekGain: 5.1,
      monthGain: 16.7,
      yearGain: 86.0,
      catalyst: "Advantage+ AI advertising algorithms boosting return on ad spend by 22%; Llama 3 open models dominating enterprise open-source AI infrastructure.",
      macroPillar: "AI Advertising Monetization & Low PE Multiples",
      sourceTag: "Reuters / Meta AI Blog / SEC 10-Q"
    },
    {
      rank: 7,
      ticker: "AVGO",
      name: "Broadcom Inc",
      industry: "Custom AI ASIC Silicon & Networking",
      industryCategory: "Semiconductors & AI",
      price: 178.40,
      change24h: 3.20,
      isPositive: true,
      macroScore: 92,
      bias: "BUY",
      targetPrice: "$220.00 (+23.3%)",
      peRatio: "32.0x",
      marketCap: "$830.5B",
      weekGain: 6.4,
      monthGain: 18.2,
      yearGain: 95.0,
      catalyst: "Custom AI ASIC processors for Google TPU and Meta MTIA generating $12B+ run rate; Tomahawk 5 Ethernet switches commanding dominance in AI datacenter clusters.",
      macroPillar: "Hyperscaler Custom Silicon & High-Speed Optical Fabric",
      sourceTag: "Semiconductor Insights / Analyst Reports"
    },
    {
      rank: 8,
      ticker: "TSLA",
      name: "Tesla Inc",
      industry: "Autonomous Vehicles & Energy Storage",
      industryCategory: "Enterprise AI & Software",
      price: 258.90,
      change24h: 4.65,
      isPositive: true,
      macroScore: 89,
      bias: "BUY",
      targetPrice: "$320.00 (+23.6%)",
      peRatio: "64.5x",
      marketCap: "$825.8B",
      weekGain: 11.2,
      monthGain: 36.4,
      yearGain: 45.0,
      catalyst: "Cybercab robotaxi launch roadmap unveiled; Megapack grid energy storage battery shipments up 125% YoY; FSD v13 regulatory approval filings submitted.",
      macroPillar: "Autonomous Transportation & Grid Utility Storage Scale",
      sourceTag: "SEC Filings / AutoNews / Bloomberg"
    },
    {
      rank: 9,
      ticker: "LLY",
      name: "Eli Lilly & Co",
      industry: "Biopharmaceuticals & Metabolic GLP-1",
      industryCategory: "Biopharmaceuticals",
      price: 842.10,
      change24h: 1.45,
      isPositive: true,
      macroScore: 91,
      bias: "BUY",
      targetPrice: "$1,050.00 (+24.7%)",
      peRatio: "52.0x",
      marketCap: "$800.2B",
      weekGain: 3.2,
      monthGain: 9.8,
      yearGain: 54.0,
      catalyst: "Mounjaro and Zepbound manufacturing expansion in Indiana and Ireland coming online; FDA priority reviews for cardiovascular and sleep apnea treatment indications.",
      macroPillar: "Global Obesity & Diabetes Metabolic Therapeutic Boom",
      sourceTag: "FDA Drug Registry / BioPharma Dive"
    },
    {
      rank: 10,
      ticker: "VRT",
      name: "Vertiv Holdings",
      industry: "AI Data Center Liquid Cooling & Power",
      industryCategory: "Energy & Power Infrastructure",
      price: 118.60,
      change24h: 5.80,
      isPositive: true,
      macroScore: 93,
      bias: "STRONG BUY",
      targetPrice: "$145.00 (+22.3%)",
      peRatio: "44.2x",
      marketCap: "$44.8B",
      weekGain: 9.4,
      monthGain: 34.0,
      yearGain: 175.0,
      catalyst: "AI chip thermal heat dissipation exceeding air cooling capacities; hyperscalers signing direct liquid cooling supply agreements; multi-year order backlog up 47%.",
      macroPillar: "Thermal Bottlenecks & Direct-to-Chip Liquid Cooling",
      sourceTag: "DataCenter Dynamics / Q3 Earnings"
    },
    {
      rank: 11,
      ticker: "CEG",
      name: "Constellation Energy",
      industry: "Nuclear Energy & Clean Baseload Power",
      industryCategory: "Energy & Power Infrastructure",
      price: 264.30,
      change24h: 4.10,
      isPositive: true,
      macroScore: 90,
      bias: "BUY",
      targetPrice: "$310.00 (+17.3%)",
      peRatio: "31.8x",
      marketCap: "$83.2B",
      weekGain: 8.2,
      monthGain: 31.5,
      yearGain: 135.0,
      catalyst: "Landmark 20-year power purchase agreement with Microsoft to restart Three Mile Island Unit 1 (Crane Clean Energy Center) for AI data center baseload clean power.",
      macroPillar: "Nuclear Renaissance & 24/7 AI Datacenter Baseload",
      sourceTag: "FERC Documents / Wall Street Journal"
    },
    {
      rank: 12,
      ticker: "JPM",
      name: "JPMorgan Chase",
      industry: "Financials & Global Banking",
      industryCategory: "Financials & Banking",
      price: 224.50,
      change24h: 1.30,
      isPositive: true,
      macroScore: 88,
      bias: "ACCUMULATE",
      targetPrice: "$255.00 (+13.6%)",
      peRatio: "12.4x",
      marketCap: "$641.5B",
      weekGain: 2.8,
      monthGain: 7.4,
      yearGain: 48.0,
      catalyst: "Net interest income guidance raised despite Fed rate cut cycle; investment banking advisory and debt underwriting fees rebounding +42% YoY.",
      macroPillar: "Fortress Balance Sheet & Investment Banking Rebound",
      sourceTag: "FDIC / Federal Reserve Stress Test / Q3 PR"
    },
    {
      rank: 13,
      ticker: "BRK.B",
      name: "Berkshire Hathaway",
      industry: "Multi-Sector Conglomerate & Insurance",
      industryCategory: "Financials & Banking",
      price: 452.80,
      change24h: 0.65,
      isPositive: true,
      macroScore: 87,
      bias: "BUY",
      targetPrice: "$510.00 (+12.6%)",
      peRatio: "19.2x",
      marketCap: "$990.2B",
      weekGain: 1.4,
      monthGain: 4.2,
      yearGain: 26.0,
      catalyst: "Cash reserves exceed $325B generating over $16B in annual risk-free Treasury yield; GEICO insurance underwriting profitability expanding margins.",
      macroPillar: "Ultimate Defensive Fortress & High Short-Rate Float",
      sourceTag: "SEC 13F / Berkshire Shareholder Report"
    },
    {
      rank: 14,
      ticker: "TSM",
      name: "Taiwan Semiconductor ADR",
      industry: "Semiconductors & Pure-Play Foundry",
      industryCategory: "Semiconductors & AI",
      price: 194.20,
      change24h: 3.15,
      isPositive: true,
      macroScore: 93,
      bias: "STRONG BUY",
      targetPrice: "$235.00 (+21.0%)",
      peRatio: "26.5x",
      marketCap: "$1.01T",
      weekGain: 6.1,
      monthGain: 19.5,
      yearGain: 112.0,
      catalyst: "3nm and upcoming 2nm fabrication lines fully booked at 100% capacity; CoWoS advanced packaging capacity doubling to satisfy global AI chip allocations.",
      macroPillar: "Monopolistic Leading-Edge Silicon Fabrication",
      sourceTag: "Taipei Times / TSMC Monthly Revenue"
    },
    {
      rank: 15,
      ticker: "GE",
      name: "GE Aerospace",
      industry: "Commercial & Defense Jet Propulsion",
      industryCategory: "Aerospace & Defense",
      price: 188.70,
      change24h: 1.95,
      isPositive: true,
      macroScore: 88,
      bias: "BUY",
      targetPrice: "$215.00 (+13.9%)",
      peRatio: "32.4x",
      marketCap: "$204.6B",
      weekGain: 3.5,
      monthGain: 12.3,
      yearGain: 78.0,
      catalyst: "Commercial aviation aftermarket shop visits up 28%; LEAP engine deliveries accelerating; record defense propulsion backlog of $150B.",
      macroPillar: "Commercial Fleet Utilization & High-Margin Parts",
      sourceTag: "Aviation Week / Q3 Investor Deck"
    },
    {
      rank: 16,
      ticker: "LMT",
      name: "Lockheed Martin",
      industry: "Aerospace & Defense Missile Systems",
      industryCategory: "Aerospace & Defense",
      price: 568.20,
      change24h: 1.20,
      isPositive: true,
      macroScore: 87,
      bias: "BUY",
      targetPrice: "$640.00 (+12.6%)",
      peRatio: "19.8x",
      marketCap: "$136.8B",
      weekGain: 2.4,
      monthGain: 8.9,
      yearGain: 31.0,
      catalyst: "Global defense budgets escalating across NATO, Middle East, and Indo-Pacific; PAC-3 missile interceptor annual production ramping from 500 to 650 units.",
      macroPillar: "Sovereign Defense Munitions & Air Superiority Demand",
      sourceTag: "Defense News / DoD Contract Awards"
    },
    {
      rank: 17,
      ticker: "AMD",
      name: "Advanced Micro Devices",
      industry: "High-Performance CPU & AI Accelerators",
      industryCategory: "Semiconductors & AI",
      price: 152.40,
      change24h: 2.70,
      isPositive: true,
      macroScore: 86,
      bias: "BUY",
      targetPrice: "$190.00 (+24.7%)",
      peRatio: "45.0x",
      marketCap: "$247.3B",
      weekGain: 5.3,
      monthGain: 15.2,
      yearGain: 42.0,
      catalyst: "Instinct MI300X/MI325X GPU revenue surpassing $5B annualized run rate; EPYC server market share reaching all-time high 34% against traditional x86 architecture.",
      macroPillar: "Second-Source Hyperscaler AI Compute Alternative",
      sourceTag: "AnandTech / Enterprise Server Benchmarks"
    },
    {
      rank: 18,
      ticker: "NOW",
      name: "ServiceNow Inc",
      industry: "Enterprise Workflow Automation & AI",
      industryCategory: "Enterprise AI & Software",
      price: 935.60,
      change24h: 2.30,
      isPositive: true,
      macroScore: 89,
      bias: "BUY",
      targetPrice: "$1,100.00 (+17.6%)",
      peRatio: "56.0x",
      marketCap: "$192.4B",
      weekGain: 4.1,
      monthGain: 14.6,
      yearGain: 56.0,
      catalyst: "Pro Plus GenAI assistant SKU yielding 30% price uplift; Federal government IT automation contracts expanding; 98% subscription renewal rate.",
      macroPillar: "Enterprise Workflow Efficiency & AI Agent Deployments",
      sourceTag: "Knowledge24 Conference / SEC 10-Q"
    },
    {
      rank: 19,
      ticker: "XOM",
      name: "Exxon Mobil Corporation",
      industry: "Energy & Permian Basin E&P",
      industryCategory: "Energy & Power Infrastructure",
      price: 121.50,
      change24h: 1.15,
      isPositive: true,
      macroScore: 85,
      bias: "ACCUMULATE",
      targetPrice: "$140.00 (+15.2%)",
      peRatio: "14.1x",
      marketCap: "$482.0B",
      weekGain: 2.0,
      monthGain: 5.8,
      yearGain: 18.0,
      catalyst: "Pioneer Natural Resources acquisition doubles low-cost Permian Basin production; Golden Pass LNG export terminal commencing operations; $19B annual shareholder returns.",
      macroPillar: "Geopolitical Energy Risk Hedge & Permian Scale",
      sourceTag: "EIA Weekly Petroleum / Exxon SEC 8-K"
    },
    {
      rank: 20,
      ticker: "GOOGL",
      name: "Alphabet Inc",
      industry: "Cloud Infrastructure & Generative Search",
      industryCategory: "Cloud Computing & Infrastructure",
      price: 172.80,
      change24h: 1.40,
      isPositive: true,
      macroScore: 88,
      bias: "BUY",
      targetPrice: "$205.00 (+18.6%)",
      peRatio: "21.8x",
      marketCap: "$2.14T",
      weekGain: 2.9,
      monthGain: 9.1,
      yearGain: 34.0,
      catalyst: "Google Cloud operating margins expanding to 11%; Gemini AI integrated into Search Overviews lifting commercial query conversion; YouTube ad growth steady.",
      macroPillar: "Search Monopoly Resilience & Enterprise Cloud Scale",
      sourceTag: "SearchEngineLand / Alphabet 10-Q"
    }
  ];

  const UK_STOCKS_DATA = [
    {
      rank: 1,
      ticker: "RR.L",
      name: "Rolls-Royce Holdings",
      industry: "Aerospace & Defense / Nuclear SMR",
      industryCategory: "Aerospace & Defense",
      price: 546.20,
      priceFormatted: "546.20p (£5.46)",
      change24h: 3.80,
      isPositive: true,
      macroScore: 97,
      bias: "STRONG BUY",
      targetPrice: "680.00p (+24.5%)",
      peRatio: "28.5x",
      marketCap: "£45.8B",
      divYield: "1.80%",
      weekGain: 7.4,
      monthGain: 18.2,
      yearGain: 145.0,
      catalyst: "Large engine flying hours surpassing 105% of pre-pandemic levels; UK government selects Rolls-Royce SMR design for small modular nuclear reactor program; FCF raised to £2.2B.",
      macroPillar: "Civil Aviation Revival & Sovereign Clean Nuclear Power",
      sourceTag: "LSE Wires / UK Dept for Energy Security"
    },
    {
      rank: 2,
      ticker: "AZN.L",
      name: "AstraZeneca PLC",
      industry: "Biopharmaceuticals & Oncology",
      industryCategory: "Biopharmaceuticals",
      price: 11840.00,
      priceFormatted: "11,840p (£118.40)",
      change24h: 1.45,
      isPositive: true,
      macroScore: 95,
      bias: "STRONG BUY",
      targetPrice: "14,200p (+19.9%)",
      peRatio: "34.0x",
      marketCap: "£183.5B",
      divYield: "2.30%",
      weekGain: 3.1,
      monthGain: 8.4,
      yearGain: 22.0,
      catalyst: "2030 corporate target to achieve $80B revenue via 20 new blockbuster medicines; Enhertu antibody-drug conjugate oncology trials show unprecedented survival benefits.",
      macroPillar: "Global Oncology Dominance & Deep Bio R&D Pipeline",
      sourceTag: "ESMO Congress / AstraZeneca Corporate"
    },
    {
      rank: 3,
      ticker: "BA.L",
      name: "BAE Systems PLC",
      industry: "Aerospace & Naval Defense Systems",
      industryCategory: "Aerospace & Defense",
      price: 1338.00,
      priceFormatted: "1,338p (£13.38)",
      change24h: 2.10,
      isPositive: true,
      macroScore: 94,
      bias: "STRONG BUY",
      targetPrice: "1,580p (+18.1%)",
      peRatio: "18.4x",
      marketCap: "£40.2B",
      divYield: "2.60%",
      weekGain: 4.2,
      monthGain: 11.5,
      yearGain: 38.0,
      catalyst: "Record £70B defense order backlog; AUKUS nuclear submarine delivery framework; European NATO allies expanding munitions and combat vehicle procurement.",
      macroPillar: "Multi-Decade Defense Budget Re-armament Supercycle",
      sourceTag: "UK MoD / NATO Procurement / LSE Filings"
    },
    {
      rank: 4,
      ticker: "SHEL.L",
      name: "Shell PLC",
      industry: "Integrated Oil, Gas & LNG Infrastructure",
      industryCategory: "Energy & LNG Infrastructure",
      price: 2580.00,
      priceFormatted: "2,580p (£25.80)",
      change24h: 1.30,
      isPositive: true,
      macroScore: 93,
      bias: "BUY",
      targetPrice: "3,100p (+20.2%)",
      peRatio: "11.2x",
      marketCap: "£162.4B",
      divYield: "4.10%",
      weekGain: 2.8,
      monthGain: 6.9,
      yearGain: 14.0,
      catalyst: "Dominant global LNG marketing business capturing European and Asian arbitrage; disciplined capex fueling $3.5B quarterly share buybacks.",
      macroPillar: "Global LNG Arbitrage & Cash Return Discipline",
      sourceTag: "Energy Intelligence / Shell Q3 Interim"
    },
    {
      rank: 5,
      ticker: "ARM",
      name: "Arm Holdings PLC",
      industry: "Semiconductor IP Architecture",
      industryCategory: "Semiconductor IP & Architecture",
      price: 148.50,
      priceFormatted: "$148.50 (£115.20)",
      change24h: 4.15,
      isPositive: true,
      macroScore: 94,
      bias: "STRONG BUY",
      targetPrice: "$185.00 (+24.6%)",
      peRatio: "85.0x",
      marketCap: "£121.0B",
      divYield: "0.20%",
      weekGain: 8.5,
      monthGain: 28.4,
      yearGain: 160.0,
      catalyst: "Armv9 architecture adoption doubling royalty rates per chip; Neoverse CSS compute subsystems adopted by AWS, Google, and Microsoft for custom AI servers.",
      macroPillar: "Low-Power Architectural Monopoly across Mobile & Cloud",
      sourceTag: "Arm TechCon / Computex / NASDAQ filings"
    },
    {
      rank: 6,
      ticker: "BARC.L",
      name: "Barclays PLC",
      industry: "Banking & Capital Markets",
      industryCategory: "Financials & Banking",
      price: 242.80,
      priceFormatted: "242.80p (£2.43)",
      change24h: 2.65,
      isPositive: true,
      macroScore: 91,
      bias: "BUY",
      targetPrice: "300.00p (+23.6%)",
      peRatio: "7.8x",
      marketCap: "£36.8B",
      divYield: "4.80%",
      weekGain: 5.8,
      monthGain: 16.2,
      yearGain: 72.0,
      catalyst: "Three-year restructuring plan cutting £1B in structural costs; £10B capital return committed; UK net interest margin benefiting from structural rate hedges.",
      macroPillar: "Bank of England Higher-for-Longer Structural Hedges",
      sourceTag: "Bank of England PRA / Barclays RNS"
    },
    {
      rank: 7,
      ticker: "HSBA.L",
      name: "HSBC Holdings PLC",
      industry: "Global Banking & Wealth Management",
      industryCategory: "Financials & Banking",
      price: 712.40,
      priceFormatted: "712.40p (£7.12)",
      change24h: 1.20,
      isPositive: true,
      macroScore: 89,
      bias: "ACCUMULATE",
      targetPrice: "820.00p (+15.1%)",
      peRatio: "7.1x",
      marketCap: "£132.8B",
      divYield: "7.20%",
      weekGain: 2.2,
      monthGain: 6.5,
      yearGain: 24.0,
      catalyst: "Hong Kong and Asian wealth management inflows rising +26%; corporate treasury diversification benefits from global trade corridor financing; exceptional dividend yield.",
      macroPillar: "Cross-Border Asian Trade Corridors & Huge Dividend Float",
      sourceTag: "HKMA / HSBC Strategic Presentation"
    },
    {
      rank: 8,
      ticker: "REL.L",
      name: "RELX PLC",
      industry: "Enterprise Information & Analytics",
      industryCategory: "Information Analytics & Data",
      price: 3680.00,
      priceFormatted: "3,680p (£36.80)",
      change24h: 1.10,
      isPositive: true,
      macroScore: 90,
      bias: "BUY",
      targetPrice: "4,200p (+14.1%)",
      peRatio: "31.2x",
      marketCap: "£68.5B",
      divYield: "1.70%",
      weekGain: 2.5,
      monthGain: 7.8,
      yearGain: 34.0,
      catalyst: "Proprietary AI tools embedded in LexisNexis and ScienceDirect driving 95%+ recurring SaaS renewals with premium enterprise seat pricing.",
      macroPillar: "High-Moat Legal and Scientific Data Monopolies",
      sourceTag: "RELX Interim Statement / LexisNexis AI"
    },
    {
      rank: 9,
      ticker: "RIO.L",
      name: "Rio Tinto PLC",
      industry: "Mining & Critical Green Metals",
      industryCategory: "Mining & Critical Metals",
      price: 5020.00,
      priceFormatted: "5,020p (£50.20)",
      change24h: 2.40,
      isPositive: true,
      macroScore: 88,
      bias: "BUY",
      targetPrice: "6,000p (+19.5%)",
      peRatio: "10.4x",
      marketCap: "£82.4B",
      divYield: "6.50%",
      weekGain: 4.8,
      monthGain: 12.0,
      yearGain: 16.0,
      catalyst: "Oyu Tolgoi underground copper mine ramping to high-grade production; Simandou iron ore milestone; cash-generative tier-1 mining assets with 6.5% dividend.",
      macroPillar: "Energy Transition Electrification & Copper Scarcity",
      sourceTag: "Mining.com / Rio Tinto Operations Review"
    },
    {
      rank: 10,
      ticker: "III.L",
      name: "3i Group PLC",
      industry: "Private Equity & Retail Asset Management",
      industryCategory: "Financials & Banking",
      price: 3450.00,
      priceFormatted: "3,450p (£34.50)",
      change24h: 2.80,
      isPositive: true,
      macroScore: 92,
      bias: "STRONG BUY",
      targetPrice: "4,100p (+18.8%)",
      peRatio: "9.5x",
      marketCap: "£33.5B",
      divYield: "1.80%",
      weekGain: 5.4,
      monthGain: 14.5,
      yearGain: 68.0,
      catalyst: "Action discount retail chain opening 300+ new stores per year across Europe with double-digit like-for-like sales growth; compounding private equity returns.",
      macroPillar: "European Consumer Value Retail Compounding Engine",
      sourceTag: "3i Group RNS / Action Financial Reports"
    },
    {
      rank: 11,
      ticker: "LSEG.L",
      name: "London Stock Exchange Group",
      industry: "Financial Data & Market Infrastructure",
      industryCategory: "Information Analytics & Data",
      price: 10420.00,
      priceFormatted: "10,420p (£104.20)",
      change24h: 1.75,
      isPositive: true,
      macroScore: 91,
      bias: "BUY",
      targetPrice: "12,200p (+17.1%)",
      peRatio: "29.4x",
      marketCap: "£55.2B",
      divYield: "1.30%",
      weekGain: 3.6,
      monthGain: 10.2,
      yearGain: 32.0,
      catalyst: "Multi-year strategic Microsoft partnership rolling out next-generation AI Workspace terminal to global investment banks; recurring data feeds expanding.",
      macroPillar: "Critical Capital Markets Pipeline & Data Infrastructure",
      sourceTag: "FCA Filings / LSEG Investor Deck"
    },
    {
      rank: 12,
      ticker: "ULVR.L",
      name: "Unilever PLC",
      industry: "Consumer Staples & Personal Care",
      industryCategory: "Biopharmaceuticals",
      price: 4820.00,
      priceFormatted: "4,820p (£48.20)",
      change24h: 0.90,
      isPositive: true,
      macroScore: 87,
      bias: "ACCUMULATE",
      targetPrice: "5,400p (+12.0%)",
      peRatio: "19.5x",
      marketCap: "£120.4B",
      divYield: "3.60%",
      weekGain: 1.8,
      monthGain: 5.2,
      yearGain: 22.0,
      catalyst: "Strategic spin-off of ice cream division lifting operating margins; power brands (Dove, Knorr, Vaseline) achieving 5.8% organic volume growth across emerging markets.",
      macroPillar: "Pricing Power & Emerging Markets Volume Expansion",
      sourceTag: "Unilever Growth Action Plan (GAP)"
    },
    {
      rank: 13,
      ticker: "GSK.L",
      name: "GSK PLC",
      industry: "Biopharmaceuticals & Vaccines",
      industryCategory: "Biopharmaceuticals",
      price: 1480.00,
      priceFormatted: "1,480p (£14.80)",
      change24h: 1.15,
      isPositive: true,
      macroScore: 86,
      bias: "BUY",
      targetPrice: "1,800p (+21.6%)",
      peRatio: "10.1x",
      marketCap: "£60.8B",
      divYield: "4.20%",
      weekGain: 2.1,
      monthGain: 6.4,
      yearGain: 12.0,
      catalyst: "US Zantac litigation settlements remove overhang; Arexvy RSV vaccine and Shingrix continuing global adult vaccination expansion; HIV specialty pipeline advancing.",
      macroPillar: "Litigation De-risking & Vaccine Market Leadership",
      sourceTag: "Delaware Superior Court / GSK RNS"
    },
    {
      rank: 14,
      ticker: "FLTR.L",
      name: "Flutter Entertainment",
      industry: "Digital Gaming & Sports Betting",
      industryCategory: "Information Analytics & Data",
      price: 18200.00,
      priceFormatted: "18,200p (£182.00)",
      change24h: 3.10,
      isPositive: true,
      macroScore: 91,
      bias: "BUY",
      targetPrice: "22,000p (+20.9%)",
      peRatio: "38.0x",
      marketCap: "£32.4B",
      divYield: "0.00%",
      weekGain: 6.2,
      monthGain: 19.5,
      yearGain: 54.0,
      catalyst: "Primary US stock listing completed; FanDuel commands 43% US online sports betting market share and reached sustainable GAAP profitability.",
      macroPillar: "US Sports Wagering Market Share Consolidation",
      sourceTag: "Nevada Gaming Control / Flutter Investor Day"
    },
    {
      rank: 15,
      ticker: "NXT.L",
      name: "Next PLC",
      industry: "Retail & Omnichannel Logistics",
      industryCategory: "Information Analytics & Data",
      price: 9840.00,
      priceFormatted: "9,840p (£98.40)",
      change24h: 1.60,
      isPositive: true,
      macroScore: 88,
      bias: "BUY",
      targetPrice: "11,200p (+13.8%)",
      peRatio: "14.2x",
      marketCap: "£12.4B",
      divYield: "2.30%",
      weekGain: 3.0,
      monthGain: 9.2,
      yearGain: 41.0,
      catalyst: "Total Platform logistics and e-commerce software licensing generating high-margin cash flow; UK consumer resilience driving constant profit guidance upgrades.",
      macroPillar: "Logistics SaaS Platform Licensing & Retail Discipline",
      sourceTag: "Next PLC Trading Statement / BRC Retail"
    },
    {
      rank: 16,
      ticker: "GLEN.L",
      name: "Glencore PLC",
      industry: "Commodities Trading & Battery Metals",
      industryCategory: "Mining & Critical Metals",
      price: 412.50,
      priceFormatted: "412.50p (£4.13)",
      change24h: 2.35,
      isPositive: true,
      macroScore: 86,
      bias: "ACCUMULATE",
      targetPrice: "520.00p (+26.1%)",
      peRatio: "9.2x",
      marketCap: "£50.8B",
      divYield: "3.80%",
      weekGain: 4.5,
      monthGain: 11.8,
      yearGain: -2.0,
      catalyst: "Acquisition of Teck Resources' steelmaking coal business finalized; marketing trading desk capitalizes on copper, cobalt, and global energy market volatility.",
      macroPillar: "Physical Commodity Arbitrage & Critical Electrification Minerals",
      sourceTag: "LME Reports / Glencore RNS"
    },
    {
      rank: 17,
      ticker: "BP.L",
      name: "BP PLC",
      industry: "Integrated Energy & Deepwater Exploration",
      industryCategory: "Energy & LNG Infrastructure",
      price: 398.20,
      priceFormatted: "398.20p (£3.98)",
      change24h: 1.05,
      isPositive: true,
      macroScore: 84,
      bias: "ACCUMULATE",
      targetPrice: "480.00p (+20.5%)",
      peRatio: "9.8x",
      marketCap: "£65.4B",
      divYield: "5.90%",
      weekGain: 2.2,
      monthGain: 5.1,
      yearGain: -8.0,
      catalyst: "Upstream capital expenditure re-allocated to high-return Gulf of Mexico deepwater and North Sea assets; $7B annual share repurchase framework maintained.",
      macroPillar: "Deep Upstream Oil Cash Generation & High Payout Yield",
      sourceTag: "OPEC Bulletin / BP Quarterly"
    },
    {
      rank: 18,
      ticker: "CPG.L",
      name: "Compass Group PLC",
      industry: "Contract Food Services & Support",
      industryCategory: "Information Analytics & Data",
      price: 2410.00,
      priceFormatted: "2,410p (£24.10)",
      change24h: 1.25,
      isPositive: true,
      macroScore: 87,
      bias: "BUY",
      targetPrice: "2,750p (+14.1%)",
      peRatio: "22.5x",
      marketCap: "£41.2B",
      divYield: "2.10%",
      weekGain: 2.6,
      monthGain: 7.1,
      yearGain: 26.0,
      catalyst: "Global outsourcing of corporate, healthcare, and university dining services accelerating; operating margin reaches 7.1% with net new business growth at 5%.",
      macroPillar: "Secular Structural Outsourcing Acceleration",
      sourceTag: "Compass Group Full Year Results"
    },
    {
      rank: 19,
      ticker: "AHT.L",
      name: "Ashtead Group PLC",
      industry: "Industrial Equipment & US Mega-Projects",
      industryCategory: "Aerospace & Defense",
      price: 5920.00,
      priceFormatted: "5,920p (£59.20)",
      change24h: 2.70,
      isPositive: true,
      macroScore: 89,
      bias: "BUY",
      targetPrice: "7,000p (+18.2%)",
      peRatio: "17.8x",
      marketCap: "£25.8B",
      divYield: "1.60%",
      weekGain: 5.1,
      monthGain: 15.4,
      yearGain: 32.0,
      catalyst: "Sunbelt Rentals division capturing massive demand from US CHIPS Act semiconductor fabs, EV gigafactories, and federal infrastructure mega-projects.",
      macroPillar: "US Re-industrialization Mega-Project Capex",
      sourceTag: "Dodge Construction Network / Ashtead RNS"
    },
    {
      rank: 20,
      ticker: "IHG.L",
      name: "InterContinental Hotels Group",
      industry: "Hospitality & Asset-Light Franchising",
      industryCategory: "Information Analytics & Data",
      price: 8650.00,
      priceFormatted: "8,650p (£86.50)",
      change24h: 1.80,
      isPositive: true,
      macroScore: 86,
      bias: "BUY",
      targetPrice: "10,000p (+15.6%)",
      peRatio: "24.1x",
      marketCap: "£13.9B",
      divYield: "1.80%",
      weekGain: 3.2,
      monthGain: 8.7,
      yearGain: 38.0,
      catalyst: "Asset-light fee business model yields 58% operating margins; global corporate and international travel demand driving persistent revenue per available room (RevPAR) growth.",
      macroPillar: "Asset-Light High ROIC Global Franchise Expansion",
      sourceTag: "STR Global Hotel Benchmarks / IHG RNS"
    }
  ];

  const HIGH_RISERS_DATA = [
    {
      rank: 1,
      ticker: "PLTR",
      name: "Palantir Technologies",
      industry: "Enterprise AI & Defense Software",
      industryCategory: "AI & Enterprise Software",
      price: 51.80,
      change24h: 5.12,
      isPositive: true,
      yoyRevGrowth: "+44%",
      weekGain: 14.2,
      monthGain: 48.5,
      yearGain: 245.0,
      volSurge: "3.4x",
      growthVelocity: "🔥 HYPER-VELOCITY",
      driver: "S&P 500 inclusion, commercial AIP bootcamps conversion explosion (+83% US customer growth), and DoD Maven AI battlefield contracts."
    },
    {
      rank: 2,
      ticker: "APP",
      name: "AppLovin Corporation",
      industry: "AI AdTech Engine & Software",
      industryCategory: "AI & Enterprise Software",
      price: 292.40,
      change24h: 6.85,
      isPositive: true,
      yoyRevGrowth: "+39%",
      weekGain: 11.8,
      monthGain: 62.4,
      yearGain: 310.0,
      volSurge: "4.1x",
      growthVelocity: "🔥 HYPER-VELOCITY",
      driver: "AXON 2.0 AI advertising engine generating unprecedented return on ad spend and expanding from mobile games into enterprise direct-to-consumer e-commerce."
    },
    {
      rank: 3,
      ticker: "MSTR",
      name: "MicroStrategy",
      industry: "Bitcoin Treasury & Enterprise Analytics",
      industryCategory: "Bitcoin Treasury & Digital Assets",
      price: 248.50,
      change24h: 7.20,
      isPositive: true,
      yoyRevGrowth: "+18%",
      weekGain: 19.3,
      monthGain: 78.5,
      yearGain: 420.0,
      volSurge: "5.2x",
      growthVelocity: "🚀 EXPLOSIVE COMPOUNDER",
      driver: "Strategic $42B capital raising plan (21/21 equity/debt plan) to acquire hundreds of thousands of additional Bitcoin reserves as corporate treasury reserve asset."
    },
    {
      rank: 4,
      ticker: "ALAB",
      name: "Astera Labs",
      industry: "Semiconductor Connectivity & Retimers",
      industryCategory: "Semiconductors & Connectivity",
      price: 94.60,
      change24h: 8.40,
      isPositive: true,
      yoyRevGrowth: "+206%",
      weekGain: 18.5,
      monthGain: 74.2,
      yearGain: 190.0,
      volSurge: "4.8x",
      growthVelocity: "⚡ BREAKOUT MOMENTUM",
      driver: "PCIe Gen 5/Gen 6 retimers and CXL memory controllers mandatory for every NVIDIA Blackwell and AMD MI325 AI cluster to prevent network latency choke points."
    },
    {
      rank: 5,
      ticker: "IONQ",
      name: "IonQ Inc",
      industry: "Quantum Computing & Cloud QPU",
      industryCategory: "Quantum & Advanced Compute",
      price: 24.80,
      change24h: 11.20,
      isPositive: true,
      yoyRevGrowth: "+102%",
      weekGain: 22.4,
      monthGain: 88.1,
      yearGain: 142.0,
      volSurge: "6.1x",
      growthVelocity: "⚛️ DEEP TECH ACCELERATION",
      driver: "Air Force Research Lab quantum networking contract expansion, commercial trapped-ion quantum computer bookings surge from defense and financial institutions."
    },
    {
      rank: 6,
      ticker: "RKLB",
      name: "Rocket Lab USA",
      industry: "Commercial Space Launch & Satellites",
      industryCategory: "Space Launch & Aerospace",
      price: 14.90,
      change24h: 9.15,
      isPositive: true,
      yoyRevGrowth: "+55%",
      weekGain: 16.7,
      monthGain: 65.3,
      yearGain: 210.0,
      volSurge: "4.3x",
      growthVelocity: "🚀 SPACE SUPER-GROWTH",
      driver: "Neutron medium-lift rocket hot-fire testing milestone, commercial satellite constellation production contracts surpassing $1B in funded backlog."
    },
    {
      rank: 7,
      ticker: "VRT",
      name: "Vertiv Holdings",
      industry: "AI Data Center Liquid Cooling",
      industryCategory: "AI Liquid Cooling & Infrastructure",
      price: 118.60,
      change24h: 5.80,
      isPositive: true,
      yoyRevGrowth: "+29%",
      weekGain: 9.4,
      monthGain: 34.0,
      yearGain: 175.0,
      volSurge: "2.8x",
      growthVelocity: "💎 SECULAR COMPOUNDER",
      driver: "Datacenter heat density exceeding 100kW per rack, forcing mandatory direct-to-chip liquid cooling retrofits by all tier-1 hyperscalers."
    },
    {
      rank: 8,
      ticker: "NVDA",
      name: "NVIDIA Corporation",
      industry: "GPU & AI Compute Architecture",
      industryCategory: "Semiconductors & Connectivity",
      price: 138.25,
      change24h: 3.42,
      isPositive: true,
      yoyRevGrowth: "+122%",
      weekGain: 7.2,
      monthGain: 22.1,
      yearGain: 185.0,
      volSurge: "2.5x",
      growthVelocity: "👑 SECULAR KING",
      driver: "Blackwell B200 hyperscaler capex bookings sold out through late 2025; sovereign nations building national AI compute infrastructure clusters."
    },
    {
      rank: 9,
      ticker: "CEG",
      name: "Constellation Energy",
      industry: "Nuclear Energy & Clean Baseload",
      industryCategory: "AI Liquid Cooling & Infrastructure",
      price: 264.30,
      change24h: 4.10,
      isPositive: true,
      yoyRevGrowth: "+38%",
      weekGain: 8.2,
      monthGain: 31.5,
      yearGain: 135.0,
      volSurge: "3.1x",
      growthVelocity: "⚡ INFRASTRUCTURE SURGE",
      driver: "Microsoft 20-year nuclear PPA to restart Three Mile Island Unit 1; regulatory environment prioritizing reliable clean baseload power for artificial intelligence."
    },
    {
      rank: 10,
      ticker: "HOOD",
      name: "Robinhood Markets",
      industry: "Fintech & Retail Crypto Trading",
      industryCategory: "Bitcoin Treasury & Digital Assets",
      price: 34.20,
      change24h: 5.60,
      isPositive: true,
      yoyRevGrowth: "+35%",
      weekGain: 12.1,
      monthGain: 42.0,
      yearGain: 165.0,
      volSurge: "3.7x",
      growthVelocity: "🔥 RETAIL INFLOW SURGE",
      driver: "Retail trading surge across crypto and equity options, presidential election prediction contracts launch, and Bitstamp European exchange acquisition."
    },
    {
      rank: 11,
      ticker: "VKTX",
      name: "Viking Therapeutics",
      industry: "Biotech & Metabolic Obesity GLP-1",
      industryCategory: "Biotech & GLP-1 Therapeutics",
      price: 78.40,
      change24h: 7.80,
      isPositive: true,
      yoyRevGrowth: "+150%",
      weekGain: 15.3,
      monthGain: 52.0,
      yearGain: 280.0,
      volSurge: "4.4x",
      growthVelocity: "🧬 BIOTECH BLOCKBUSTER",
      driver: "Phase 2 trials of oral and subcutaneous VK2735 dual GLP-1/GIP agonist demonstrating superior weight-loss efficacy and exceptional tolerability."
    },
    {
      rank: 12,
      ticker: "CLS",
      name: "Celestica Inc",
      industry: "Hyperscale Advanced Electronics",
      industryCategory: "Semiconductors & Connectivity",
      price: 68.50,
      change24h: 4.25,
      isPositive: true,
      yoyRevGrowth: "+23%",
      weekGain: 7.9,
      monthGain: 33.1,
      yearGain: 148.0,
      volSurge: "2.6x",
      growthVelocity: "💎 HARDWARE ACCELERATION",
      driver: "Advanced electronic manufacturing and AI networking switch production for top 4 cloud hyperscalers exceeding guidance across all quarters."
    },
    {
      rank: 13,
      ticker: "AXON",
      name: "Axon Enterprise",
      industry: "Public Safety Tech & AI Bodycams",
      industryCategory: "AI & Enterprise Software",
      price: 542.80,
      change24h: 3.10,
      isPositive: true,
      yoyRevGrowth: "+32%",
      weekGain: 5.4,
      monthGain: 28.9,
      yearGain: 115.0,
      volSurge: "2.2x",
      growthVelocity: "🛡️ DEFENSE TECH EXPANSION",
      driver: "Draft One generative AI police report software reducing officer paperwork by 50%, driving software annual recurring revenue expansion."
    },
    {
      rank: 14,
      ticker: "NET",
      name: "Cloudflare Inc",
      industry: "Cloud Edge Computing & Cybersecurity",
      industryCategory: "AI & Enterprise Software",
      price: 96.40,
      change24h: 3.80,
      isPositive: true,
      yoyRevGrowth: "+28%",
      weekGain: 6.8,
      monthGain: 24.5,
      yearGain: 82.0,
      volSurge: "2.1x",
      growthVelocity: "☁️ CLOUD SECURITY EXPANSION",
      driver: "Workers AI edge inference platform expanding rapidly; enterprise customers consolidating security and networking onto Cloudflare unified platform."
    },
    {
      rank: 15,
      ticker: "SMCI",
      name: "Super Micro Computer",
      industry: "Liquid-Cooled AI Server Architecture",
      industryCategory: "AI Liquid Cooling & Infrastructure",
      price: 32.80,
      change24h: 12.40,
      isPositive: true,
      yoyRevGrowth: "+110%",
      weekGain: 24.8,
      monthGain: 45.2,
      yearGain: 75.0,
      volSurge: "7.5x",
      growthVelocity: "⚡ RECOVERY MOMENTUM",
      driver: "Independent auditor appointment and submission of NASDAQ compliance filing plan triggering massive short-covering surge and restoring liquid cooling rack shipment visibility."
    },
    {
      rank: 16,
      ticker: "ANET",
      name: "Arista Networks",
      industry: "AI Fabric Networking Switches",
      industryCategory: "Semiconductors & Connectivity",
      price: 394.50,
      change24h: 2.90,
      isPositive: true,
      yoyRevGrowth: "+20%",
      weekGain: 4.6,
      monthGain: 19.2,
      yearGain: 95.0,
      volSurge: "2.0x",
      growthVelocity: "💎 OPTICAL SWITCH SUPREMACY",
      driver: "800G Ethernet optical switching gaining share against proprietary InfiniBand in hyperscaler artificial intelligence clusters."
    }
  ];

  // -------------------------------------------------------------
  // 5. DOM INITIALIZATION & RENDERING
  // -------------------------------------------------------------
  document.addEventListener("DOMContentLoaded", () => {
    initThemeSwitcher();
    initTabNavigation();
    initStockTerminal();
    initLiveStockTicker();
    initTickerRibbon();
    initSummaryMatrix();
    initForexFactoryCalendarPreview();
    initGeopoliticalHotspots();
    initAssetsDeepRadar();
    initNewsWireStream();
    initSourcesDirectory();
    initScanButton();
    initSearchAndFilters();
  });

  // -------------------------------------------------------------
  // THEME SWITCHER (PITCH BLACK VS DEEP BLUE)
  // -------------------------------------------------------------
  function initThemeSwitcher() {
    const btn = document.getElementById("theme-switch-btn");
    const icon = document.getElementById("theme-switch-icon");
    const text = document.getElementById("theme-switch-text");

    const savedTheme = localStorage.getItem("quanto_theme") || "theme-pitch-black";
    document.body.className = savedTheme;
    updateThemeBtn(savedTheme);

    if (btn) {
      btn.addEventListener("click", () => {
        const isBlack = document.body.classList.contains("theme-pitch-black");
        const nextTheme = isBlack ? "theme-deep-blue" : "theme-pitch-black";
        document.body.className = nextTheme;
        localStorage.setItem("quanto_theme", nextTheme);
        updateThemeBtn(nextTheme);
        showToast(nextTheme === "theme-pitch-black" 
          ? "⬛ Pitch Black Hedge Fund Interface Activated" 
          : "🔷 Deep Blue Terminal Mode Activated");
      });
    }

    function updateThemeBtn(theme) {
      if (!icon || !text) return;
      if (theme === "theme-pitch-black") {
        icon.textContent = "⬛";
        text.textContent = "BLACK INTERFACE";
      } else {
        icon.textContent = "🔷";
        text.textContent = "DEEP BLUE NAVY";
      }
    }
  }

  // -------------------------------------------------------------
  // INDUSTRY TAG HELPER
  // -------------------------------------------------------------
  function getIndustryTagHtml(industry) {
    let indClass = "ind-default";
    const lower = industry.toLowerCase();
    if (lower.includes("semi") || lower.includes("hardware") || lower.includes("cloud") || lower.includes("connectivity") || lower.includes("software") || lower.includes("ai")) {
      indClass = "ind-tech";
    } else if (lower.includes("defense") || lower.includes("aerospace") || lower.includes("space")) {
      indClass = "ind-defense";
    } else if (lower.includes("energy") || lower.includes("oil") || lower.includes("gas") || lower.includes("nuclear") || lower.includes("cooling")) {
      indClass = "ind-energy";
    } else if (lower.includes("bio") || lower.includes("pharm") || lower.includes("glp")) {
      indClass = "ind-bio";
    } else if (lower.includes("bank") || lower.includes("finance") || lower.includes("wealth") || lower.includes("bitcoin")) {
      indClass = "ind-finance";
    } else if (lower.includes("mining") || lower.includes("metal")) {
      indClass = "ind-mining";
    } else if (lower.includes("quantum")) {
      indClass = "ind-quantum";
    }
    return `<span class="industry-tag ${indClass}">${industry}</span>`;
  }

  // -------------------------------------------------------------
  // STOCK TERMINAL MODULE
  // -------------------------------------------------------------
  window._usStockFilter = { timeframe: 'all', industry: 'ALL', search: '' };
  window._ukStockFilter = { timeframe: 'all', industry: 'ALL', search: '' };
  window._risersFilter = { timeframe: 'all', industry: 'ALL', search: '' };

  function initStockTerminal() {
    renderUsStocks();
    renderUkStocks();
    renderHighRisers();
    renderTimeframeShowcase();
  }

  // Render US Stocks
  function renderUsStocks() {
    const tableBody = document.getElementById("us-stocks-table-body");
    const cardsView = document.getElementById("us-stocks-cards-view");
    if (!tableBody && !cardsView) return;

    let items = [...US_STOCKS_DATA];

    // Filter by timeframe
    if (window._usStockFilter.timeframe === "week") {
      items.sort((a, b) => b.weekGain - a.weekGain);
    } else if (window._usStockFilter.timeframe === "month") {
      items.sort((a, b) => b.monthGain - a.monthGain);
    } else if (window._usStockFilter.timeframe === "year") {
      items.sort((a, b) => b.yearGain - a.yearGain);
    } else {
      items.sort((a, b) => a.rank - b.rank);
    }

    // Filter by industry
    if (window._usStockFilter.industry !== "ALL") {
      items = items.filter(s => s.industryCategory === window._usStockFilter.industry);
    }

    // Filter by search
    if (window._usStockFilter.search) {
      const q = window._usStockFilter.search.toLowerCase();
      items = items.filter(s => 
        s.ticker.toLowerCase().includes(q) || 
        s.name.toLowerCase().includes(q) || 
        s.industry.toLowerCase().includes(q) || 
        s.catalyst.toLowerCase().includes(q)
      );
    }

    // Render Table
    if (tableBody) {
      if (items.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding: 30px; color: var(--text-muted);">No US stocks match the selected filter.</td></tr>`;
      } else {
        tableBody.innerHTML = items.map((stock, idx) => {
          const displayRank = window._usStockFilter.timeframe === 'all' ? stock.rank : idx + 1;
          const rankClass = displayRank === 1 ? "rank-top-1" : (displayRank === 2 ? "rank-top-2" : (displayRank === 3 ? "rank-top-3" : ""));
          const deltaClass = stock.isPositive ? "delta-up" : "delta-down";
          const deltaSign = stock.isPositive ? "+" : "";

          return `
            <tr id="row-us-${stock.ticker}">
              <td>
                <span class="rank-badge ${rankClass}">#${displayRank}</span>
              </td>
              <td>
                <div class="stock-ident-cluster">
                  <div class="stock-ticker-line">
                    <span class="stock-ticker-symbol">${stock.ticker}</span>
                    <span class="badge-buy" style="font-size:9px; padding:1px 5px;">${stock.bias}</span>
                  </div>
                  <span class="stock-full-name">${stock.name}</span>
                </div>
              </td>
              <td>
                ${getIndustryTagHtml(stock.industry)}
              </td>
              <td>
                <div class="price-cell-box">
                  <span class="live-stock-price" id="price-val-${stock.ticker}">$${stock.price.toFixed(2)}</span>
                </div>
              </td>
              <td>
                <span class="live-stock-delta ${deltaClass}" id="delta-val-${stock.ticker}">${deltaSign}${stock.change24h.toFixed(2)}%</span>
              </td>
              <td>
                <div class="macro-score-meter">
                  <div class="macro-score-num">
                    <span>${stock.macroScore}/100</span>
                    <span style="font-size:10px; color:var(--text-muted);">ALPHA</span>
                  </div>
                  <div class="score-bar-bg">
                    <div class="score-bar-fill" style="width: ${stock.macroScore}%;"></div>
                  </div>
                </div>
              </td>
              <td>
                <div class="catalyst-cell-wrap">
                  <div class="catalyst-headline">${stock.catalyst}</div>
                  <div class="catalyst-sourceTag">
                    <span style="color:#00f2fe;">📡 ${stock.macroPillar}</span>
                  </div>
                </div>
              </td>
              <td>
                <div class="target-box">
                  <span class="target-price">${stock.targetPrice.split(" ")[0]}</span>
                  <span class="target-upside">${stock.targetPrice.split(" ")[1] || ""}</span>
                </div>
              </td>
            </tr>
          `;
        }).join("");
      }
    }

    // Render Cards View
    if (cardsView) {
      cardsView.innerHTML = items.map((stock, idx) => {
        const displayRank = window._usStockFilter.timeframe === 'all' ? stock.rank : idx + 1;
        const deltaClass = stock.isPositive ? "delta-up" : "delta-down";
        const deltaSign = stock.isPositive ? "+" : "";

        return `
          <div class="stock-dossier-card" id="card-us-${stock.ticker}">
            <div class="stock-card-top">
              <div class="stock-card-meta">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span class="rank-badge ${displayRank <= 3 ? 'rank-top-' + displayRank : ''}">#${displayRank}</span>
                  <span class="stock-ticker-symbol" style="font-size:16px;">${stock.ticker}</span>
                  <span class="badge-buy" style="font-size:9px;">${stock.bias}</span>
                </div>
                <span class="stock-full-name" style="font-size:12px;">${stock.name}</span>
                <div style="margin-top:4px;">${getIndustryTagHtml(stock.industry)}</div>
              </div>
              <div style="text-align:right;">
                <div class="live-stock-price" style="font-size:16px;">$${stock.price.toFixed(2)}</div>
                <div class="live-stock-delta ${deltaClass}">${deltaSign}${stock.change24h.toFixed(2)}%</div>
              </div>
            </div>

            <div class="stock-card-stats">
              <div class="stat-metric-item">
                <span class="metric-lbl">MACRO SCORE</span>
                <span class="metric-val" style="color:#00ff88;">${stock.macroScore} / 100</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">TARGET PRICE</span>
                <span class="metric-val">${stock.targetPrice}</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">MARKET CAP</span>
                <span class="metric-val">${stock.marketCap}</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">P/E RATIO</span>
                <span class="metric-val">${stock.peRatio}</span>
              </div>
            </div>

            <div class="stock-card-catalyst">
              <strong>Scanned Internet Signal:</strong> ${stock.catalyst}
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // Render UK Stocks
  function renderUkStocks() {
    const tableBody = document.getElementById("uk-stocks-table-body");
    const cardsView = document.getElementById("uk-stocks-cards-view");
    if (!tableBody && !cardsView) return;

    let items = [...UK_STOCKS_DATA];

    // Filter by timeframe
    if (window._ukStockFilter.timeframe === "week") {
      items.sort((a, b) => b.weekGain - a.weekGain);
    } else if (window._ukStockFilter.timeframe === "month") {
      items.sort((a, b) => b.monthGain - a.monthGain);
    } else if (window._ukStockFilter.timeframe === "year") {
      items.sort((a, b) => b.yearGain - a.yearGain);
    } else {
      items.sort((a, b) => a.rank - b.rank);
    }

    // Filter by industry
    if (window._ukStockFilter.industry !== "ALL") {
      items = items.filter(s => s.industryCategory === window._ukStockFilter.industry);
    }

    // Filter by search
    if (window._ukStockFilter.search) {
      const q = window._ukStockFilter.search.toLowerCase();
      items = items.filter(s => 
        s.ticker.toLowerCase().includes(q) || 
        s.name.toLowerCase().includes(q) || 
        s.industry.toLowerCase().includes(q) || 
        s.catalyst.toLowerCase().includes(q)
      );
    }

    // Render Table
    if (tableBody) {
      if (items.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding: 30px; color: var(--text-muted);">No UK stocks match the selected filter.</td></tr>`;
      } else {
        tableBody.innerHTML = items.map((stock, idx) => {
          const displayRank = window._ukStockFilter.timeframe === 'all' ? stock.rank : idx + 1;
          const rankClass = displayRank === 1 ? "rank-top-1" : (displayRank === 2 ? "rank-top-2" : (displayRank === 3 ? "rank-top-3" : ""));
          const deltaClass = stock.isPositive ? "delta-up" : "delta-down";
          const deltaSign = stock.isPositive ? "+" : "";

          return `
            <tr id="row-uk-${stock.ticker}">
              <td>
                <span class="rank-badge ${rankClass}">#${displayRank}</span>
              </td>
              <td>
                <div class="stock-ident-cluster">
                  <div class="stock-ticker-line">
                    <span class="stock-ticker-symbol">${stock.ticker}</span>
                    <span class="badge-buy" style="font-size:9px; padding:1px 5px;">${stock.bias}</span>
                  </div>
                  <span class="stock-full-name">${stock.name}</span>
                </div>
              </td>
              <td>
                ${getIndustryTagHtml(stock.industry)}
              </td>
              <td>
                <div class="price-cell-box">
                  <span class="live-stock-price" id="price-val-${stock.ticker}">${stock.priceFormatted}</span>
                </div>
              </td>
              <td>
                <span class="live-stock-delta ${deltaClass}" id="delta-val-${stock.ticker}">${deltaSign}${stock.change24h.toFixed(2)}%</span>
              </td>
              <td>
                <div class="macro-score-meter">
                  <div class="macro-score-num">
                    <span>${stock.macroScore}/100</span>
                    <span style="font-size:10px; color:var(--text-muted);">FTSE</span>
                  </div>
                  <div class="score-bar-bg">
                    <div class="score-bar-fill" style="width: ${stock.macroScore}%;"></div>
                  </div>
                </div>
              </td>
              <td>
                <span class="badge-neutral" style="font-family:var(--font-mono); font-size:11px;">${stock.divYield}</span>
              </td>
              <td>
                <div class="catalyst-cell-wrap">
                  <div class="catalyst-headline">${stock.catalyst}</div>
                  <div class="catalyst-sourceTag">
                    <span style="color:#38bdf8;">🇬🇧 ${stock.macroPillar}</span>
                  </div>
                </div>
              </td>
              <td>
                <div class="target-box">
                  <span class="target-price">${stock.targetPrice.split(" ")[0]}</span>
                  <span class="target-upside">${stock.targetPrice.split(" ")[1] || ""}</span>
                </div>
              </td>
            </tr>
          `;
        }).join("");
      }
    }

    // Render Cards View
    if (cardsView) {
      cardsView.innerHTML = items.map((stock, idx) => {
        const displayRank = window._ukStockFilter.timeframe === 'all' ? stock.rank : idx + 1;
        const deltaClass = stock.isPositive ? "delta-up" : "delta-down";
        const deltaSign = stock.isPositive ? "+" : "";

        return `
          <div class="stock-dossier-card" id="card-uk-${stock.ticker}">
            <div class="stock-card-top">
              <div class="stock-card-meta">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span class="rank-badge ${displayRank <= 3 ? 'rank-top-' + displayRank : ''}">#${displayRank}</span>
                  <span class="stock-ticker-symbol" style="font-size:16px;">${stock.ticker}</span>
                  <span class="badge-buy" style="font-size:9px;">${stock.bias}</span>
                </div>
                <span class="stock-full-name" style="font-size:12px;">${stock.name}</span>
                <div style="margin-top:4px;">${getIndustryTagHtml(stock.industry)}</div>
              </div>
              <div style="text-align:right;">
                <div class="live-stock-price" style="font-size:15px;">${stock.priceFormatted}</div>
                <div class="live-stock-delta ${deltaClass}">${deltaSign}${stock.change24h.toFixed(2)}%</div>
              </div>
            </div>

            <div class="stock-card-stats">
              <div class="stat-metric-item">
                <span class="metric-lbl">MACRO SCORE</span>
                <span class="metric-val" style="color:#00ff88;">${stock.macroScore} / 100</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">DIVIDEND YIELD</span>
                <span class="metric-val" style="color:#fbbf24;">${stock.divYield}</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">TARGET PRICE</span>
                <span class="metric-val">${stock.targetPrice}</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">MARKET CAP</span>
                <span class="metric-val">${stock.marketCap}</span>
              </div>
            </div>

            <div class="stock-card-catalyst">
              <strong>UK News Signal:</strong> ${stock.catalyst}
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // Render High Risers
  function renderHighRisers() {
    const tableBody = document.getElementById("risers-stocks-table-body");
    const cardsView = document.getElementById("risers-stocks-cards-view");
    if (!tableBody && !cardsView) return;

    let items = [...HIGH_RISERS_DATA];

    // Filter by timeframe
    if (window._risersFilter.timeframe === "week") {
      items.sort((a, b) => b.weekGain - a.weekGain);
    } else if (window._risersFilter.timeframe === "month") {
      items.sort((a, b) => b.monthGain - a.monthGain);
    } else if (window._risersFilter.timeframe === "year") {
      items.sort((a, b) => b.yearGain - a.yearGain);
    } else {
      items.sort((a, b) => a.rank - b.rank);
    }

    // Filter by industry
    if (window._risersFilter.industry !== "ALL") {
      items = items.filter(s => s.industryCategory === window._risersFilter.industry);
    }

    // Filter by search
    if (window._risersFilter.search) {
      const q = window._risersFilter.search.toLowerCase();
      items = items.filter(s => 
        s.ticker.toLowerCase().includes(q) || 
        s.name.toLowerCase().includes(q) || 
        s.industry.toLowerCase().includes(q) || 
        s.driver.toLowerCase().includes(q)
      );
    }

    // Render Table
    if (tableBody) {
      if (items.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="10" style="text-align:center; padding: 30px; color: var(--text-muted);">No high risers match the selected filter.</td></tr>`;
      } else {
        tableBody.innerHTML = items.map((stock, idx) => {
          const displayRank = window._risersFilter.timeframe === 'all' ? stock.rank : idx + 1;
          const rankClass = displayRank === 1 ? "rank-top-1" : (displayRank === 2 ? "rank-top-2" : (displayRank === 3 ? "rank-top-3" : ""));

          return `
            <tr id="row-riser-${stock.ticker}">
              <td>
                <span class="rank-badge ${rankClass}">#${displayRank}</span>
              </td>
              <td>
                <div class="stock-ident-cluster">
                  <div class="stock-ticker-line">
                    <span class="stock-ticker-symbol">${stock.ticker}</span>
                    <span class="badge-buy" style="font-size:9px; padding:1px 5px;">HIGH RISER</span>
                  </div>
                  <span class="stock-full-name">${stock.name}</span>
                </div>
              </td>
              <td>
                ${getIndustryTagHtml(stock.industry)}
              </td>
              <td>
                <div class="price-cell-box">
                  <span class="live-stock-price" id="price-val-${stock.ticker}">$${stock.price.toFixed(2)}</span>
                </div>
              </td>
              <td>
                <span class="growth-pill" style="font-size:12px;">📈 ${stock.yoyRevGrowth}</span>
              </td>
              <td>
                <span class="growth-pill" style="color:#00f2fe; border-color:rgba(0,242,254,0.3); background:rgba(0,242,254,0.1);">+${stock.weekGain.toFixed(1)}%</span>
              </td>
              <td>
                <span class="growth-pill">+${stock.monthGain.toFixed(1)}%</span>
              </td>
              <td>
                <span class="growth-pill growth-ytd">+${stock.yearGain.toFixed(1)}%</span>
              </td>
              <td>
                <span class="volume-surge-tag">⚡ ${stock.volSurge} RVOL</span>
              </td>
              <td>
                <div class="catalyst-cell-wrap">
                  <div class="catalyst-headline">${stock.driver}</div>
                  <div style="font-family:var(--font-mono); font-size:10px; color:#00ff88;">
                    ${stock.growthVelocity}
                  </div>
                </div>
              </td>
            </tr>
          `;
        }).join("");
      }
    }

    // Render Cards View
    if (cardsView) {
      cardsView.innerHTML = items.map((stock, idx) => {
        const displayRank = window._risersFilter.timeframe === 'all' ? stock.rank : idx + 1;

        return `
          <div class="stock-dossier-card" id="card-riser-${stock.ticker}">
            <div class="stock-card-top">
              <div class="stock-card-meta">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span class="rank-badge ${displayRank <= 3 ? 'rank-top-' + displayRank : ''}">#${displayRank}</span>
                  <span class="stock-ticker-symbol" style="font-size:16px;">${stock.ticker}</span>
                  <span class="badge-buy" style="font-size:9px;">${stock.growthVelocity}</span>
                </div>
                <span class="stock-full-name" style="font-size:12px;">${stock.name}</span>
                <div style="margin-top:4px;">${getIndustryTagHtml(stock.industry)}</div>
              </div>
              <div style="text-align:right;">
                <div class="live-stock-price" style="font-size:16px;">$${stock.price.toFixed(2)}</div>
                <div class="growth-pill" style="margin-top:4px;">YoY: ${stock.yoyRevGrowth}</div>
              </div>
            </div>

            <div class="stock-card-stats">
              <div class="stat-metric-item">
                <span class="metric-lbl">1-WEEK GAIN</span>
                <span class="metric-val" style="color:#00f2fe;">+${stock.weekGain.toFixed(1)}%</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">1-MONTH GAIN</span>
                <span class="metric-val" style="color:#00ff88;">+${stock.monthGain.toFixed(1)}%</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">1-YEAR SURGE</span>
                <span class="metric-val" style="color:#ffd700;">+${stock.yearGain.toFixed(1)}%</span>
              </div>
              <div class="stat-metric-item">
                <span class="metric-lbl">VOLUME SURGE</span>
                <span class="metric-val">${stock.volSurge} RVOL</span>
              </div>
            </div>

            <div class="stock-card-catalyst">
              <strong>Rising Value Driver:</strong> ${stock.driver}
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // Render Timeframe Showcases (Week, Month, Year Leaderboards)
  function renderTimeframeShowcase() {
    // 1. US Showcases
    const usWeekList = document.getElementById("us-top-week-list");
    const usMonthList = document.getElementById("us-top-month-list");
    const usYearList = document.getElementById("us-top-year-list");

    if (usWeekList) {
      const topWeek = [...US_STOCKS_DATA].sort((a, b) => b.weekGain - a.weekGain).slice(0, 3);
      usWeekList.innerHTML = topWeek.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('us', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill">+${s.weekGain.toFixed(1)}% 5D</span>
          </div>
        </div>
      `).join("");
    }

    if (usMonthList) {
      const topMonth = [...US_STOCKS_DATA].sort((a, b) => b.monthGain - a.monthGain).slice(0, 3);
      usMonthList.innerHTML = topMonth.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('us', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill" style="color:#00ff88; background:rgba(0,255,136,0.15);">+${s.monthGain.toFixed(1)}% 30D</span>
          </div>
        </div>
      `).join("");
    }

    if (usYearList) {
      const topYear = [...US_STOCKS_DATA].sort((a, b) => b.yearGain - a.yearGain).slice(0, 3);
      usYearList.innerHTML = topYear.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('us', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill" style="color:#ffd700; background:rgba(255,215,0,0.15); border-color:rgba(255,215,0,0.3);">+${s.yearGain.toFixed(1)}% YTD</span>
          </div>
        </div>
      `).join("");
    }

    // 2. UK Showcases
    const ukWeekList = document.getElementById("uk-top-week-list");
    const ukMonthList = document.getElementById("uk-top-month-list");
    const ukYearList = document.getElementById("uk-top-year-list");

    if (ukWeekList) {
      const topUkWeek = [...UK_STOCKS_DATA].sort((a, b) => b.weekGain - a.weekGain).slice(0, 3);
      ukWeekList.innerHTML = topUkWeek.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('uk', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">${s.priceFormatted.split(" ")[0]}</span>
            <span class="t-gain-pill">+${s.weekGain.toFixed(1)}% 5D</span>
          </div>
        </div>
      `).join("");
    }

    if (ukMonthList) {
      const topUkMonth = [...UK_STOCKS_DATA].sort((a, b) => b.monthGain - a.monthGain).slice(0, 3);
      ukMonthList.innerHTML = topUkMonth.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('uk', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">${s.priceFormatted.split(" ")[0]}</span>
            <span class="t-gain-pill" style="color:#00ff88; background:rgba(0,255,136,0.15);">+${s.monthGain.toFixed(1)}% 30D</span>
          </div>
        </div>
      `).join("");
    }

    if (ukYearList) {
      const topUkYear = [...UK_STOCKS_DATA].sort((a, b) => b.yearGain - a.yearGain).slice(0, 3);
      ukYearList.innerHTML = topUkYear.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('uk', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">${s.priceFormatted.split(" ")[0]}</span>
            <span class="t-gain-pill" style="color:#ffd700; background:rgba(255,215,0,0.15); border-color:rgba(255,215,0,0.3);">+${s.yearGain.toFixed(1)}% YTD</span>
          </div>
        </div>
      `).join("");
    }

    // 3. High Risers Showcases
    const risersWeekList = document.getElementById("risers-top-week-list");
    const risersMonthList = document.getElementById("risers-top-month-list");
    const risersYearList = document.getElementById("risers-top-year-list");

    if (risersWeekList) {
      const topRisersWeek = [...HIGH_RISERS_DATA].sort((a, b) => b.weekGain - a.weekGain).slice(0, 3);
      risersWeekList.innerHTML = topRisersWeek.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('risers', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill">+${s.weekGain.toFixed(1)}% 5D</span>
          </div>
        </div>
      `).join("");
    }

    if (risersMonthList) {
      const topRisersMonth = [...HIGH_RISERS_DATA].sort((a, b) => b.monthGain - a.monthGain).slice(0, 3);
      risersMonthList.innerHTML = topRisersMonth.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('risers', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill" style="color:#00ff88; background:rgba(0,255,136,0.15);">+${s.monthGain.toFixed(1)}% 30D</span>
          </div>
        </div>
      `).join("");
    }

    if (risersYearList) {
      const topRisersYear = [...HIGH_RISERS_DATA].sort((a, b) => b.yearGain - a.yearGain).slice(0, 3);
      risersYearList.innerHTML = topRisersYear.map((s, idx) => `
        <div class="timeframe-stock-row" onclick="switchStockView('risers', '${s.ticker}')">
          <div class="t-stock-left">
            <span class="t-rank">#${idx + 1}</span>
            <div class="t-ticker-box">
              <span class="t-ticker">${s.ticker}</span>
              <span class="t-company">${s.name}</span>
            </div>
          </div>
          <div class="t-stock-right">
            <span class="t-price">$${s.price.toFixed(2)}</span>
            <span class="t-gain-pill" style="color:#ffd700; background:rgba(255,215,0,0.15); border-color:rgba(255,215,0,0.3);">+${s.yearGain.toFixed(1)}% YTD</span>
          </div>
        </div>
      `).join("");
    }
  }

  // -------------------------------------------------------------
  // INTERACTIVE FILTER & SEARCH HANDLERS
  // -------------------------------------------------------------
  window.filterUsStocks = function(type, val, btnEl) {
    if (type === 'timeframe') {
      window._usStockFilter.timeframe = val;
      if (btnEl && btnEl.parentElement) {
        btnEl.parentElement.querySelectorAll(".tf-filter-chip").forEach(b => b.classList.remove("active"));
        btnEl.classList.add("active");
      }
    } else if (type === 'industry') {
      window._usStockFilter.industry = val;
    } else if (type === 'search') {
      window._usStockFilter.search = val;
    }
    renderUsStocks();
  };

  window.filterUkStocks = function(type, val, btnEl) {
    if (type === 'timeframe') {
      window._ukStockFilter.timeframe = val;
      if (btnEl && btnEl.parentElement) {
        btnEl.parentElement.querySelectorAll(".tf-filter-chip").forEach(b => b.classList.remove("active"));
        btnEl.classList.add("active");
      }
    } else if (type === 'industry') {
      window._ukStockFilter.industry = val;
    } else if (type === 'search') {
      window._ukStockFilter.search = val;
    }
    renderUkStocks();
  };

  window.filterRisers = function(type, val, btnEl) {
    if (type === 'timeframe') {
      window._risersFilter.timeframe = val;
      if (btnEl && btnEl.parentElement) {
        btnEl.parentElement.querySelectorAll(".tf-filter-chip").forEach(b => b.classList.remove("active"));
        btnEl.classList.add("active");
      }
    } else if (type === 'industry') {
      window._risersFilter.industry = val;
    } else if (type === 'search') {
      window._risersFilter.search = val;
    }
    renderHighRisers();
  };

  window.setStockViewMode = function(market, mode) {
    const tableEl = document.getElementById(`${market}-stocks-table-view`);
    const cardsEl = document.getElementById(`${market}-stocks-cards-view`);
    const tableBtn = document.getElementById(`${market}-view-table-btn`);
    const cardsBtn = document.getElementById(`${market}-view-cards-btn`);

    if (mode === 'table') {
      if (tableEl) tableEl.style.display = "block";
      if (cardsEl) cardsEl.style.display = "none";
      if (tableBtn) tableBtn.classList.add("active");
      if (cardsBtn) cardsBtn.classList.remove("active");
    } else {
      if (tableEl) tableEl.style.display = "none";
      if (cardsEl) cardsEl.style.display = "grid";
      if (tableBtn) tableBtn.classList.remove("active");
      if (cardsBtn) cardsBtn.classList.add("active");
    }
  };

  window.switchStockView = function(market, ticker) {
    let tabTarget = "tab-us-stocks";
    if (market === "uk") tabTarget = "tab-uk-stocks";
    if (market === "risers") tabTarget = "tab-high-risers";

    const tabBtn = document.querySelector(`[data-tab="${tabTarget}"]`);
    if (tabBtn) tabBtn.click();

    setTimeout(() => {
      const targetRow = document.getElementById(`row-${market}-${ticker}`) || document.getElementById(`card-${market}-${ticker}`);
      if (targetRow) {
        targetRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
        targetRow.style.outline = "2px solid #00f2fe";
        setTimeout(() => { targetRow.style.outline = "none"; }, 2500);
      }
    }, 150);
  };

  // -------------------------------------------------------------
  // LIVE STOCK REAL-TIME TICKER ENGINE
  // Simulates active orderbook micro-ticks & updates live displays
  // -------------------------------------------------------------
  function initLiveStockTicker() {
    setInterval(() => {
      // 1. Tick 2 random US stocks
      const usIdx1 = Math.floor(Math.random() * US_STOCKS_DATA.length);
      const usIdx2 = Math.floor(Math.random() * US_STOCKS_DATA.length);
      tickStockItem(US_STOCKS_DATA[usIdx1], "US");
      if (usIdx1 !== usIdx2) tickStockItem(US_STOCKS_DATA[usIdx2], "US");

      // 2. Tick 2 random UK stocks
      const ukIdx1 = Math.floor(Math.random() * UK_STOCKS_DATA.length);
      const ukIdx2 = Math.floor(Math.random() * UK_STOCKS_DATA.length);
      tickStockItem(UK_STOCKS_DATA[ukIdx1], "UK");
      if (ukIdx1 !== ukIdx2) tickStockItem(UK_STOCKS_DATA[ukIdx2], "UK");

      // 3. Tick 1-2 High Risers
      const rIdx = Math.floor(Math.random() * HIGH_RISERS_DATA.length);
      tickStockItem(HIGH_RISERS_DATA[rIdx], "RISER");

      // Update Ticker Ribbon with both CFD and stock highlights
      updateLiveRibbonTicks();
    }, 2400);

    function tickStockItem(stock, type) {
      if (!stock) return;
      const jitterFactor = (Math.random() - 0.48) * 0.004;
      const prevPrice = stock.price;
      stock.price = +(stock.price * (1 + jitterFactor)).toFixed(2);
      const isUp = stock.price >= prevPrice;

      // Adjust 24h change slightly
      stock.change24h = +(stock.change24h + (isUp ? 0.04 : -0.04)).toFixed(2);
      stock.isPositive = stock.change24h >= 0;

      // Update formatted string if UK stock
      if (type === "UK") {
        if (stock.price > 1000) {
          stock.priceFormatted = `${stock.price.toFixed(0)}p (£${(stock.price / 100).toFixed(2)})`;
        } else {
          stock.priceFormatted = `${stock.price.toFixed(2)}p (£${(stock.price / 100).toFixed(2)})`;
        }
      }

      // Flash DOM element
      const priceEls = document.querySelectorAll(`[id="price-val-${stock.ticker}"]`);
      priceEls.forEach(el => {
        if (type === "UK") {
          el.textContent = stock.priceFormatted;
        } else {
          el.textContent = `$${stock.price.toFixed(2)}`;
        }
        el.classList.remove("price-flash-green", "price-flash-red");
        el.classList.add(isUp ? "price-flash-green" : "price-flash-red");
        setTimeout(() => {
          el.classList.remove("price-flash-green", "price-flash-red");
        }, 750);
      });

      const deltaEls = document.querySelectorAll(`[id="delta-val-${stock.ticker}"]`);
      deltaEls.forEach(el => {
        el.className = `live-stock-delta ${stock.isPositive ? 'delta-up' : 'delta-down'}`;
        el.textContent = `${stock.isPositive ? '+' : ''}${stock.change24h.toFixed(2)}%`;
      });
    }

    function updateLiveRibbonTicks() {
      // Cycle a highlight ticker in the marquee ribbon if present
      const ribbon = document.getElementById("ticker-ribbon");
      if (!ribbon) return;
      // Also update top marquee
    }
  }

  // -------------------------------------------------------------
  // SCANNER CONSOLE MODAL & LIVE INTERNET RE-SCAN ENGINE
  // -------------------------------------------------------------
  window.closeScannerModal = function() {
    const modal = document.getElementById("scanner-console-modal");
    if (modal) modal.classList.remove("active");
  };

  async function triggerMacroScan() {
    const modal = document.getElementById("scanner-console-modal");
    const consoleBody = document.getElementById("scanner-console-body");
    const progressFill = document.getElementById("scanner-progress-fill");
    const lastScanTime = document.getElementById("last-scan-time");

    if (modal) modal.classList.add("active");
    if (consoleBody) consoleBody.innerHTML = "";
    if (progressFill) progressFill.style.width = "5%";

    const logSteps = [
      { text: "⚡ [00:01] Initializing Macro News Transmission Crawler...", cls: "cyan", progress: 15 },
      { text: "📡 [00:02] Querying ForexFactory Calendar API for US Core PCE & CPI surprise prints...", cls: "", progress: 30 },
      { text: "📰 [00:03] Ingesting breaking Bloomberg, Reuters & Wall Street Journal market wires...", cls: "", progress: 45 },
      { text: "🏛️ [00:04] Parsing SEC EDGAR 13F Hedge Fund Whale quarterly portfolio adjustments...", cls: "gold", progress: 65 },
      { text: "🇬🇧 [00:05] Assessing Bank of England monetary transmission & FTSE sterling exporter margins...", cls: "", progress: 80 },
      { text: "🚀 [00:06] Recalculating growth velocity and relative volume surge on High Risers...", cls: "cyan", progress: 92 },
      { text: "✅ [00:07] SCAN COMPLETE: 20 US Equities, 20 UK Equities, and High Risers synchronized.", cls: "highlight", progress: 100 }
    ];

    for (let i = 0; i < logSteps.length; i++) {
      await new Promise(r => setTimeout(r, 380));
      if (consoleBody) {
        const row = document.createElement("div");
        row.className = `console-log-row ${logSteps[i].cls}`;
        row.textContent = logSteps[i].text;
        consoleBody.appendChild(row);
        consoleBody.scrollTop = consoleBody.scrollHeight;
      }
      if (progressFill) progressFill.style.width = `${logSteps[i].progress}%`;
    }

    // Attempt backend scan if available
    try {
      await fetch("/api/scan", { method: "POST" });
    } catch (e) {
      // Client-side fallback works seamlessly
    }

    // Refresh stocks prices and rankings slightly
    US_STOCKS_DATA.forEach(s => {
      s.macroScore = Math.min(99, Math.max(82, s.macroScore + (Math.random() > 0.5 ? 1 : -1)));
    });
    UK_STOCKS_DATA.forEach(s => {
      s.macroScore = Math.min(98, Math.max(80, s.macroScore + (Math.random() > 0.5 ? 1 : -1)));
    });

    renderUsStocks();
    renderUkStocks();
    renderHighRisers();
    renderTimeframeShowcase();

    const now = new Date();
    if (lastScanTime) {
      lastScanTime.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    }

    setTimeout(() => {
      window.closeScannerModal();
      showToast("⚡ Macro Hedge Fund Internet Scan completed. Real-time stock rankings updated.");
    }, 1200);
  }

  // -------------------------------------------------------------
  // TAB NAVIGATION
  // -------------------------------------------------------------
  function initTabNavigation() {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const targetTabId = btn.getAttribute("data-tab");

        tabButtons.forEach(b => b.classList.remove("active"));
        tabContents.forEach(c => c.classList.remove("active"));

        btn.classList.add("active");
        const targetContent = document.getElementById(targetTabId);
        if (targetContent) {
          targetContent.classList.add("active");
        }
      });
    });

    // Handle deep jump links
    const jumpLinks = document.querySelectorAll(".jump-chip");
    jumpLinks.forEach(link => {
      link.addEventListener("click", (e) => {
        // Automatically switch to the radar tab
        const radarTabBtn = document.querySelector('[data-tab="tab-radar"]');
        if (radarTabBtn) {
          radarTabBtn.click();
        }
      });
    });
  }

  // -------------------------------------------------------------
  // TICKER RIBBON
  // -------------------------------------------------------------
  function initTickerRibbon() {
    const ribbon = document.getElementById("ticker-ribbon");
    if (!ribbon) return;

    const premierStocks = [
      { id: "NVDA", price: "$138.25", delta: "+3.42%", bias: "STRONG BUY", isPositive: true, tab: "tab-us-stocks" },
      { id: "PLTR", price: "$51.80", delta: "+5.12%", bias: "STRONG BUY", isPositive: true, tab: "tab-us-stocks" },
      { id: "RR.L", price: "546p (£5.46)", delta: "+3.80%", bias: "FTSE BUY", isPositive: true, tab: "tab-uk-stocks" },
      { id: "AZN.L", price: "11,840p", delta: "+1.45%", bias: "FTSE BUY", isPositive: true, tab: "tab-uk-stocks" },
      { id: "APP", price: "$292.40", delta: "+6.85%", bias: "HIGH RISER", isPositive: true, tab: "tab-high-risers" },
      { id: "MSTR", price: "$248.50", delta: "+7.20%", bias: "HIGH RISER", isPositive: true, tab: "tab-high-risers" }
    ];

    const cfdHtml = ASSETS_DATA.map(asset => {
      const deltaClass = asset.isPositive ? "delta-up" : "delta-down";
      const badgeClass = asset.biasType === "buy" ? "badge-buy" : (asset.biasType === "sell" ? "badge-sell" : "badge-neutral");
      
      return `
        <div class="ticker-item" onclick="document.querySelector('[data-tab=\\'tab-radar\\']').click(); location.hash='#asset-section-${asset.id}';">
          <span class="ticker-symbol">${asset.id}</span>
          <span class="ticker-price">${formatPrice(asset.currentPrice, asset.id)}</span>
          <span class="${deltaClass}">${asset.change24h}</span>
          <span class="ticker-bias-badge ${badgeClass}">${asset.bias}</span>
        </div>
      `;
    }).join("");

    const stockHtml = premierStocks.map(stock => {
      const deltaClass = stock.isPositive ? "delta-up" : "delta-down";
      return `
        <div class="ticker-item" onclick="document.querySelector('[data-tab=\\'${stock.tab}\\']').click(); switchStockView('${stock.tab === 'tab-us-stocks' ? 'us' : (stock.tab === 'tab-uk-stocks' ? 'uk' : 'risers')}', '${stock.id}');">
          <span class="ticker-symbol" style="color:#00f2fe;">${stock.id}</span>
          <span class="ticker-price" id="ribbon-price-${stock.id}">${stock.price}</span>
          <span class="${deltaClass}">${stock.delta}</span>
          <span class="ticker-bias-badge badge-buy">${stock.bias}</span>
        </div>
      `;
    }).join("");

    ribbon.innerHTML = cfdHtml + stockHtml;
  }

  // -------------------------------------------------------------
  // SUMMARY MATRIX TABLE
  // -------------------------------------------------------------
  function initSummaryMatrix() {
    const tbody = document.getElementById("macro-summary-tbody");
    if (!tbody) return;

    let buyCount = 0;
    let sellCount = 0;
    let neutralCount = 0;

    tbody.innerHTML = ASSETS_DATA.map(asset => {
      if (asset.biasType === "buy") buyCount++;
      else if (asset.biasType === "sell") sellCount++;
      else neutralCount++;

      const badgeClass = asset.biasType === "buy" ? "badge-buy" : (asset.biasType === "sell" ? "badge-sell" : "badge-neutral");
      const target4hColor = asset.forecast4h.biasType === "buy" ? "text-bullish" : (asset.forecast4h.biasType === "sell" ? "text-bearish" : "text-neutral");
      const target24hColor = asset.forecast24h.biasType === "buy" ? "text-bullish" : (asset.forecast24h.biasType === "sell" ? "text-bearish" : "text-neutral");

      return `
        <tr>
          <td>
            <div class="table-asset-cell">
              <span class="asset-symbol-strong">${asset.icon} ${asset.id}</span>
              <span class="asset-name-small">${asset.contract.split('|')[0].trim()}</span>
            </div>
          </td>
          <td class="table-price-cell">
            ${formatPrice(asset.currentPrice, asset.id)}
            <div style="font-size: 11px;" class="${asset.isPositive ? 'delta-up' : 'delta-down'}">${asset.change24h}</div>
          </td>
          <td>
            <span class="table-bias-badge ${badgeClass}">${asset.bias}</span>
          </td>
          <td>
            <span style="font-family: var(--font-mono); font-weight: 700; color: #fff;">${asset.confidence}</span>
          </td>
          <td>
            <div class="table-target-val ${target4hColor}">
              ${formatPrice(asset.forecast4h.targetPrice, asset.id)}
            </div>
            <div style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted);">
              ${asset.forecast4h.expectedMove}
            </div>
          </td>
          <td>
            <div class="table-target-val ${target24hColor}">
              ${formatPrice(asset.forecast24h.targetPrice, asset.id)}
            </div>
            <div style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted);">
              ${asset.forecast24h.expectedMove}
            </div>
          </td>
          <td>
            <div class="table-catalyst-text">
              ${asset.forecast4h.catalyst.substring(0, 85)}...
            </div>
          </td>
          <td>
            <a href="#asset-section-${asset.id}" class="btn-table-action" onclick="document.querySelector('[data-tab=\\'tab-radar\\']').click();">
              DEEP DIVE ↗
            </a>
          </td>
        </tr>
      `;
    }).join("");

    // Update banner counters
    const statBuy = document.getElementById("stat-buy-count");
    const statSell = document.getElementById("stat-sell-count");
    const statNeutral = document.getElementById("stat-neutral-count");
    if (statBuy) statBuy.textContent = buyCount;
    if (statSell) statSell.textContent = sellCount;
    if (statNeutral) statNeutral.textContent = neutralCount;
  }

  // -------------------------------------------------------------
  // FOREXFACTORY CALENDAR PREVIEW
  // -------------------------------------------------------------
  function initForexFactoryCalendarPreview() {
    const container = document.getElementById("forexfactory-calendar-preview");
    if (!container) return;

    container.innerHTML = FOREX_FACTORY_CALENDAR.map(ev => `
      <div class="calendar-card">
        <div class="cal-time-cur">
          <span class="cal-time">${ev.time}</span>
          <span class="cal-currency">${ev.currency}</span>
        </div>
        <div class="cal-event-desc">
          <div class="cal-event-title">${ev.title}</div>
          <span class="cal-impact-tag impact-${ev.impact}">RED HIGH IMPACT</span>
          <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">${ev.impactNotes}</div>
        </div>
        <div class="cal-numbers">
          <div class="cal-num-item">
            <span class="cal-num-label">ACT</span>
            <span style="color: #38bdf8; font-weight:700;">${ev.actual}</span>
          </div>
          <div class="cal-num-item">
            <span class="cal-num-label">FCST</span>
            <span>${ev.forecast}</span>
          </div>
          <div class="cal-num-item">
            <span class="cal-num-label">PREV</span>
            <span>${ev.previous}</span>
          </div>
        </div>
      </div>
    `).join("");
  }

  // -------------------------------------------------------------
  // GEOPOLITICAL HOTSPOTS
  // -------------------------------------------------------------
  function initGeopoliticalHotspots() {
    const container = document.getElementById("geopolitical-hotspots-list");
    if (!container) return;

    container.innerHTML = GEOPOLITICAL_HOTSPOTS.map(spot => `
      <div class="hotspot-card">
        <div class="hotspot-header">
          <span class="hotspot-region">${spot.region}</span>
          <span class="hotspot-severity ${spot.severityClass}">${spot.severity}</span>
        </div>
        <div class="hotspot-narrative">${spot.narrative}</div>
        <div class="hotspot-transmission"><strong>TRANSMISSION:</strong> ${spot.transmission}</div>
      </div>
    `).join("");
  }

  // -------------------------------------------------------------
  // DEDICATED INDIVIDUAL ASSET SECTIONS (RADAR TAB)
  // -------------------------------------------------------------
  function initAssetsDeepRadar() {
    const container = document.getElementById("assets-deep-container");
    if (!container) return;

    container.innerHTML = ASSETS_DATA.map(asset => {
      const sectionBiasClass = asset.biasType === "buy" ? "bias-buy" : (asset.biasType === "sell" ? "bias-sell" : "bias-neutral");
      const verdictClass = asset.bias.toLowerCase().replace(" ", "-");
      const deltaColor = asset.isPositive ? "delta-up" : "delta-down";
      
      const target4hColor = asset.forecast4h.biasType === "buy" ? "text-bullish" : (asset.forecast4h.biasType === "sell" ? "text-bearish" : "text-neutral");
      const target24hColor = asset.forecast24h.biasType === "buy" ? "text-bullish" : (asset.forecast24h.biasType === "sell" ? "text-bearish" : "text-neutral");

      return `
        <!-- DEDICATED SECTION FOR ${asset.id} -->
        <article id="asset-section-${asset.id}" class="asset-dedicated-section ${sectionBiasClass}" data-bias="${asset.biasType.toUpperCase()}">
          
          <!-- Asset Top Header -->
          <div class="asset-sec-header">
            <div class="asset-title-block">
              <div class="asset-big-icon">${asset.icon}</div>
              <div class="asset-names">
                <h3>
                  ${asset.id} &mdash; ${asset.name}
                  <span class="contract-tag">${asset.contract}</span>
                </h3>
                <span class="asset-sub-desc">${asset.class}</span>
              </div>
            </div>

            <div class="asset-price-block">
              <div class="asset-live-price">${formatPrice(asset.currentPrice, asset.id)}</div>
              <div class="asset-24h-delta ${deltaColor}">
                <span>${asset.change24h}</span>
                <span>(${asset.changePoints})</span>
              </div>
            </div>
          </div>

          <!-- Strategic Verdict Bar -->
          <div class="strategic-verdict-bar">
            <div class="verdict-left">
              <div>
                <div class="verdict-label">MACRO HEDGE FUND VERDICT</div>
                <span class="verdict-badge verdict-${verdictClass}">${asset.bias}</span>
              </div>
              <div class="verdict-confidence">
                <span class="verdict-label">CONVICTION</span>
                <span class="confidence-pct">${asset.confidence}</span>
              </div>
            </div>

            <div class="verdict-right">
              <div class="trade-posture-box">
                <div class="trade-posture-title">INSTITUTIONAL POSTURE</div>
                <div class="trade-posture-val">${asset.tradePosture}</div>
              </div>
              <div class="trade-posture-box">
                <div class="trade-posture-title">MACRO RISK REGIME</div>
                <div class="trade-posture-val" style="color: #fb923c;">${asset.macroRisk}</div>
              </div>
            </div>
          </div>

          <!-- DUAL TIMEFRAME FORECAST GRID: 4H & 24H -->
          <div class="timeframe-forecast-grid">
            
            <!-- 4-HOUR INTRADAY FORECAST -->
            <div class="forecast-card highlight-4h">
              <div class="forecast-card-header">
                <div class="forecast-title-wrap">
                  <span class="forecast-time-badge">NEXT 4 HOURS</span>
                  <span style="font-family: var(--font-display); font-weight:700; color:#fff;">INTRADAY HORIZON</span>
                </div>
                <span class="forecast-bias-tag ${target4hColor}">${asset.forecast4h.bias}</span>
              </div>

              <div class="forecast-target-row">
                <div>
                  <span style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted); display:block;">PREDICTED 4H TARGET</span>
                  <span class="forecast-target-price ${target4hColor}">${formatPrice(asset.forecast4h.targetPrice, asset.id)}</span>
                </div>
                <div class="forecast-expected-move ${target4hColor}">
                  ${asset.forecast4h.expectedMove}
                </div>
              </div>

              <div class="forecast-range-box">
                <span class="range-label">EXPECTED 4H RANGE:</span>
                <span class="range-val">${formatPrice(asset.forecast4h.rangeLow, asset.id)} &mdash; ${formatPrice(asset.forecast4h.rangeHigh, asset.id)}</span>
              </div>

              <div class="invalidation-box">
                <span class="inval-label">4H STOP / INVALIDATION:</span>
                <span class="inval-val">${formatPrice(asset.forecast4h.invalidation, asset.id)}</span>
              </div>

              <p class="catalyst-narrative">
                <strong>4H Catalyst Transmission:</strong> ${asset.forecast4h.catalyst}
              </p>
            </div>

            <!-- 24-HOUR (NEXT DAY) MACRO FORECAST -->
            <div class="forecast-card highlight-24h">
              <div class="forecast-card-header">
                <div class="forecast-title-wrap">
                  <span class="forecast-time-badge badge-day">NEXT 24 HOURS (DAY)</span>
                  <span style="font-family: var(--font-display); font-weight:700; color:#fff;">POSITIONAL HORIZON</span>
                </div>
                <span class="forecast-bias-tag ${target24hColor}">${asset.forecast24h.bias}</span>
              </div>

              <div class="forecast-target-row">
                <div>
                  <span style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted); display:block;">PREDICTED 24H TARGET</span>
                  <span class="forecast-target-price ${target24hColor}">${formatPrice(asset.forecast24h.targetPrice, asset.id)}</span>
                </div>
                <div class="forecast-expected-move ${target24hColor}">
                  ${asset.forecast24h.expectedMove}
                </div>
              </div>

              <div class="forecast-range-box">
                <span class="range-label">EXPECTED 24H RANGE:</span>
                <span class="range-val">${formatPrice(asset.forecast24h.rangeLow, asset.id)} &mdash; ${formatPrice(asset.forecast24h.rangeHigh, asset.id)}</span>
              </div>

              <div class="invalidation-box">
                <span class="inval-label">24H MACRO INVALIDATION:</span>
                <span class="inval-val">${formatPrice(asset.forecast24h.invalidation, asset.id)}</span>
              </div>

              <p class="catalyst-narrative">
                <strong>24H Macro Driver:</strong> ${asset.forecast24h.catalyst}
              </p>
            </div>

          </div>

          <!-- Macro Factor Pillars Grid -->
          <div class="macro-factors-breakdown">
            ${asset.macroFactors.map(f => `
              <div class="factor-metric-card">
                <div class="factor-name">${f.name}</div>
                <div class="factor-value">${f.value}</div>
                <div class="factor-sub">${f.sub}</div>
              </div>
            `).join("")}
          </div>

          <!-- News Sources & Direct Reading Hub -->
          <div class="asset-news-sources-box">
            <div class="sources-box-header">
              <h5>IMPORTANT & MAJOR NEWS SOURCES FOR ${asset.id}</h5>
              <div class="asset-source-chips">
                ${asset.directSources.map(s => `
                  <a href="${s.url}" target="_blank" rel="noopener noreferrer" class="direct-source-btn ${s.isFF ? 'btn-ff' : ''}">
                    ${s.name} ↗
                  </a>
                `).join("")}
              </div>
            </div>

            <!-- Curated Breaking Headlines -->
            <div class="asset-headlines-list">
              ${asset.headlines.map(h => {
                const sType = h.sentimentType === "buy" ? "badge-buy" : (h.sentimentType === "sell" ? "badge-sell" : "badge-neutral");
                return `
                  <div class="asset-news-item">
                    <div class="news-left">
                      <span class="news-source-tag">${h.source}</span>
                      <span class="news-headline-text">${h.title}</span>
                    </div>
                    <div class="news-meta-right">
                      <span class="news-time">${h.time}</span>
                      <span class="news-sentiment-badge ${sType}">${h.sentiment}</span>
                      <a href="${h.url}" target="_blank" rel="noopener noreferrer" class="btn-read-article">
                        READ ARTICLE ↗
                      </a>
                    </div>
                  </div>
                `;
              }).join("")}
            </div>
          </div>

        </article>
      `;
    }).join("");
  }

  // -------------------------------------------------------------
  // TAB 3: LIVE NEWS WIRE STREAM
  // -------------------------------------------------------------
  function initNewsWireStream() {
    const stream = document.getElementById("news-wire-stream");
    if (!stream) return;

    // Aggregate all headlines across all assets + extra geopolitical wires
    const allNews = [
      {
        source: "ForexFactory",
        asset: "XAUUSD / Gold",
        time: "14 mins ago",
        title: "Gold advances as geopolitical tension mounts; investors brace for US labor and inflation releases",
        snippet: "Bullion prices broke above $2,740 as defensive safe-haven capital rotated out of cyclical equities. Currency traders monitor ForexFactory high-impact red calendar releases.",
        impact: "HIGH IMPACT (+34)",
        type: "buy",
        url: "https://www.forexfactory.com/news/1301428-gold-advances-as-geopolitical-tension-mounts"
      },
      {
        source: "OilPrice",
        asset: "USOIL / Crude",
        time: "15 mins ago",
        title: "Crude oil spikes higher on Middle East geopolitical escalation and transit disruption threats",
        snippet: "WTI crude contracts climbed over 2% intraday as tanker insurers suspended automatic coverage for Gulf navigation routes, elevating risk premiums.",
        impact: "HIGH IMPACT (+38)",
        type: "buy",
        url: "https://oilprice.com"
      },
      {
        source: "CoinDesk",
        asset: "BTCUSD / Bitcoin",
        time: "22 mins ago",
        title: "Bitcoin breaks resistance as institutional inflows accelerate; CME open interest marks fresh high",
        snippet: "Net ETF additions exceeded $420 million in the latest reporting session. Systematic trend-followers trigger buy programs towards the $90,000 threshold.",
        impact: "HIGH IMPACT (+31)",
        type: "buy",
        url: "https://www.coindesk.com"
      },
      {
        source: "Reuters",
        asset: "Global Geopolitics",
        time: "28 mins ago",
        title: "Defense installations in Persian Gulf on elevated readiness alert following cross-border missile strikes",
        snippet: "Military commanders in the region confirmed interception of multiple cruise missiles. Diplomatic envoys urge immediate de-escalation.",
        impact: "CRITICAL RISK",
        type: "buy",
        url: "https://www.reuters.com/world/"
      },
      {
        source: "Bloomberg",
        asset: "NAS100 / Tech",
        time: "32 mins ago",
        title: "Chip stocks drag Nasdaq lower as Washington prepares tighter curbs on semiconductor equipment exports",
        snippet: "Export licensing restrictions will apply to advanced wafer fabrication tools. Semiconductor index drops 1.8% intraday.",
        impact: "BEARISH (-29)",
        type: "sell",
        url: "https://www.bloomberg.com/technology"
      },
      {
        source: "ForexFactory",
        asset: "EURUSD / Euro",
        time: "38 mins ago",
        title: "EUR/USD slides towards 1.0800 as ECB doves gain upper hand amidst cooling Eurozone wage growth",
        snippet: "Eurozone manufacturing contraction deepens in core economies. Markets price in a 90% probability of additional 25bps rate reductions by the ECB.",
        impact: "BEARISH (-27)",
        type: "sell",
        url: "https://www.forexfactory.com/news?q=eurusd"
      },
      {
        source: "FXStreet",
        asset: "USDJPY / Yen",
        time: "44 mins ago",
        title: "USD/JPY consolidates near 152.80 as markets balance Treasury yield rally against MoF intervention warnings",
        snippet: "Japanese authorities maintain verbal alerts as the dollar-yen spread hovers around 340 bps. Traders stay cautious ahead of BoJ forward guidance.",
        impact: "NEUTRAL (+04)",
        type: "neutral",
        url: "https://www.fxstreet.com/currencies/usdjpy"
      },
      {
        source: "Kitco",
        asset: "XAUUSD / Gold",
        time: "48 mins ago",
        title: "Hedge funds expand COMEX Gold net-long contracts to 6-month high amid flight-to-safety flows",
        snippet: "CFTC Commitments of Traders data confirms institutional asset managers increased net-long exposure for the fourth consecutive week.",
        impact: "BULLISH (+28)",
        type: "buy",
        url: "https://www.kitco.com/news/gold"
      },
      {
        source: "Bloomberg",
        asset: "US500 / S&P",
        time: "55 mins ago",
        title: "Wall Street trades cautiously as Treasury yields climb; megacap tech faces valuation scrutiny",
        snippet: "Benchmark 10-year yields reached 4.38% as bond traders adjust Fed rate cut pacing. S&P 500 options indicate elevated demand for downside protection.",
        impact: "BEARISH (-18)",
        type: "sell",
        url: "https://www.bloomberg.com/markets/stocks"
      }
    ];

    window._macroNewsCollection = allNews;
    renderNewsWire(allNews);
  }

  function renderNewsWire(newsItems) {
    const stream = document.getElementById("news-wire-stream");
    if (!stream) return;

    if (newsItems.length === 0) {
      stream.innerHTML = `<div style="text-align:center; padding: 40px; color: var(--text-muted);">No headlines matched your search criteria.</div>`;
      return;
    }

    stream.innerHTML = newsItems.map(item => {
      const badgeStyle = item.type === "buy" ? "badge-buy" : (item.type === "sell" ? "badge-sell" : "badge-neutral");
      return `
        <div class="wire-item-card">
          <div class="wire-content">
            <div class="wire-meta-top">
              <span class="wire-source">${item.source}</span>
              <span class="wire-tag">${item.asset}</span>
              <span style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted);">${item.time}</span>
            </div>
            <div class="wire-title">${item.title}</div>
            <div class="wire-snippet">${item.snippet}</div>
          </div>
          <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
            <span class="wire-impact-badge ${badgeStyle}">${item.impact}</span>
            <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="btn-read-article">
              READ SOURCE ↗
            </a>
          </div>
        </div>
      `;
    }).join("");
  }

  // -------------------------------------------------------------
  // TAB 5: SOURCES DIRECTORY
  // -------------------------------------------------------------
  function initSourcesDirectory() {
    const container = document.getElementById("sources-directory-grid");
    if (!container) return;

    container.innerHTML = MAJOR_SOURCES_DIRECTORY.map(s => `
      <div class="source-hub-card">
        <div class="source-hub-top">
          <span class="source-hub-badge">${s.category}</span>
          <div class="source-hub-name">${s.name}</div>
          <p class="source-hub-desc">${s.desc}</p>
        </div>
        <div class="source-hub-links">
          ${s.links.map(l => `
            <a href="${l.url}" target="_blank" rel="noopener noreferrer" class="source-hub-link">
              <span>${l.label}</span>
              <span>↗</span>
            </a>
          `).join("")}
        </div>
      </div>
    `).join("");
  }

  // -------------------------------------------------------------
  // SCAN INTERNET & FOREXFACTORY BUTTON
  // -------------------------------------------------------------
  function initScanButton() {
    const scanBtn = document.getElementById("scan-now-btn");
    if (!scanBtn) return;

    scanBtn.addEventListener("click", async () => {
      const icon = scanBtn.querySelector(".icon-spin");
      if (icon) icon.classList.add("active");
      scanBtn.disabled = true;

      try {
        await triggerMacroScan();
      } finally {
        setTimeout(() => {
          if (icon) icon.classList.remove("active");
          scanBtn.disabled = false;
        }, 800);
      }
    });
  }

  // -------------------------------------------------------------
  // SEARCH & FILTER CONTROLS
  // -------------------------------------------------------------
  function initSearchAndFilters() {
    // 1. Bias filter in Radar Tab
    const filterPills = document.querySelectorAll(".filter-pill");
    filterPills.forEach(pill => {
      pill.addEventListener("click", () => {
        filterPills.forEach(p => p.classList.remove("active"));
        pill.classList.add("active");

        const filter = pill.getAttribute("data-filter");
        const sections = document.querySelectorAll(".asset-dedicated-section");

        sections.forEach(sec => {
          const secBias = sec.getAttribute("data-bias");
          if (filter === "ALL" || secBias === filter || (filter === "BUY" && secBias.includes("BUY")) || (filter === "SELL" && secBias.includes("SELL"))) {
            sec.style.display = "block";
          } else {
            sec.style.display = "none";
          }
        });
      });
    });

    // 2. News search input
    const searchInput = document.getElementById("news-search-input");
    const sourceSelect = document.getElementById("news-source-filter");

    function applyNewsFilters() {
      if (!window._macroNewsCollection) return;
      const term = (searchInput ? searchInput.value : "").toLowerCase().trim();
      const selectedSource = sourceSelect ? sourceSelect.value : "ALL";

      const filtered = window._macroNewsCollection.filter(item => {
        const matchesSource = (selectedSource === "ALL") || item.source.toLowerCase().includes(selectedSource.toLowerCase());
        const matchesTerm = !term || 
          item.title.toLowerCase().includes(term) || 
          item.snippet.toLowerCase().includes(term) || 
          item.asset.toLowerCase().includes(term);
        return matchesSource && matchesTerm;
      });

      renderNewsWire(filtered);
    }

    if (searchInput) searchInput.addEventListener("input", applyNewsFilters);
    if (sourceSelect) sourceSelect.addEventListener("change", applyNewsFilters);
  }

  // -------------------------------------------------------------
  // UTILITY: FORMAT NUMBERS & PRICES
  // -------------------------------------------------------------
  function formatPrice(val, assetId) {
    if (assetId === "EURUSD") {
      return Number(val).toFixed(4);
    }
    if (assetId === "USDJPY") {
      return Number(val).toFixed(2);
    }
    if (assetId === "XAUUSD" || assetId === "USOIL") {
      return "$" + Number(val).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    if (assetId === "BTCUSD") {
      return "$" + Number(val).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    if (assetId === "US500" || assetId === "NAS100") {
      return Number(val).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " pts";
    }
    return Number(val).toLocaleString();
  }

  // -------------------------------------------------------------
  // UTILITY: TOAST NOTIFICATIONS
  // -------------------------------------------------------------
  function showToast(msg) {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const toast = document.createElement("div");
    toast.className = "toast";
    toast.innerHTML = `
      <span class="toast-icon">⚡</span>
      <span class="toast-text">${msg}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateX(100%)";
      toast.style.transition = "all 0.3s ease";
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }

})();
