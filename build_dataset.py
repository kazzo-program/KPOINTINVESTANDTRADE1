# -*- coding: utf-8 -*-
"""
Generate comprehensive high-fidelity dataset for Polymarket Top 10 Markets:
Categories:
1. Politics (Day, Week, Month)
2. Crypto (Day, Week, Month)
3. Finance (Day, Week, Month)
4. Sports (Day, Week, Month)
5. Football - Premier League (Day, Week, Month)
6. Football - La Liga (Day, Week, Month)
7. Football - Bundesliga (Day, Week, Month)
Total: 21 sets of Top 10 = 210 fully analyzed markets with Macro Hedge Fund Advisory!
"""

import json

# We will construct rich, realistic datasets for each combination
DATA = {
    # 1. POLITICS
    "politics": {
        "day": [
            {
                "id": "pol-d-01",
                "rank": 1,
                "title": "Will the US Senate confirm the Treasury Secretary nominee before Friday?",
                "slug": "us-senate-confirm-treasury-secretary-friday",
                "volume": "$19,450,200",
                "volumeRaw": 19450200,
                "volumeLabel": "24H Volume",
                "liquidity": "$3,840,000",
                "endDate": "Friday 5:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.73, "pct": 73}, {"name": "NO", "price": 0.27, "pct": 27}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 89,
                    "evEdge": "+11.8% EV+",
                    "impliedProb": 73,
                    "fairValueProb": 84.8,
                    "targetExit": "$0.88 (+20.5% return)",
                    "stopLoss": "$0.62",
                    "macroStrategy": "Congressional whip counts reveal two pivotal moderate senators secured committee concessions on municipal bond tax-exempt status, virtually guaranteeing cloture threshold.",
                    "newsCatalyst": {
                        "headline": "Bloomberg: Senate Majority Leader schedules immediate procedural cloture vote with broad bipartisan caucus backing",
                        "source": "Bloomberg Politics",
                        "time": "45m ago",
                        "impact": "BULLISH CATALYST"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Twitter & Capitol Hill Insider Feeds",
                        "sentimentScore": 84,
                        "sentimentTrend": "+22% Bullish shift past 12h",
                        "whaleFlows": "Whale wallet 0x8a92... accumulated $320,000 in YES contracts at 0.69-0.72 avg",
                        "retailPositioning": "Retail hesitant due to partisan rhetoric, creating underpriced probability window"
                    },
                    "riskMitigation": "Lock 50% profits once price crosses 0.84 prior to the roll-call floor vote."
                }
            },
            {
                "id": "pol-d-02",
                "rank": 2,
                "title": "Will the US Executive Order on AI Compute Infrastructure be signed today?",
                "slug": "us-executive-order-ai-compute-infrastructure-today",
                "volume": "$14,810,000",
                "volumeRaw": 14810000,
                "volumeLabel": "24H Volume",
                "liquidity": "$2,910,000",
                "endDate": "Today 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 86,
                    "evEdge": "+14.0% EV+",
                    "impliedProb": 61,
                    "fairValueProb": 75.0,
                    "targetExit": "$0.82 (+34.4% return)",
                    "stopLoss": "$0.48",
                    "macroStrategy": "White House press briefing schedule was updated adding National Security Advisor and Commerce Secretary. Energy grid interconnection agreements were finalized overnight.",
                    "newsCatalyst": {
                        "headline": "Reuters: Administration readies landmark executive action fast-tracking nuclear data-center permits",
                        "source": "Reuters Washington Bureau",
                        "time": "1h ago",
                        "impact": "BULLISH CATALYST"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Twitter Tech Policy & Gov Trackers",
                        "sentimentScore": 79,
                        "sentimentTrend": "+16% Bullish momentum surge",
                        "whaleFlows": "Smart money addresses absorbed $210,000 of retail sell-orders at 0.58",
                        "retailPositioning": "Retail skeptical of same-day signature, failing to account for press conference setup"
                    },
                    "riskMitigation": "Set automated sell trigger at 0.80 upon live press briefing broadcast."
                }
            },
            {
                "id": "pol-d-03",
                "rank": 3,
                "title": "Will the UK Prime Minister survive the House of Commons motion without snap election calls?",
                "slug": "uk-pm-commons-motion-snap-election",
                "volume": "$11,240,000",
                "volumeRaw": 11240000,
                "volumeLabel": "24H Volume",
                "liquidity": "$2,450,000",
                "endDate": "Today 10:00 PM GMT",
                "outcomes": [{"name": "YES", "price": 0.82, "pct": 82}, {"name": "NO", "price": 0.18, "pct": 18}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "MEDIUM-HIGH CONVICTION",
                    "confidencePct": 85,
                    "evEdge": "+8.0% EV+",
                    "impliedProb": 82,
                    "fairValueProb": 90.0,
                    "targetExit": "$0.94 (+14.6% return)",
                    "stopLoss": "$0.70",
                    "macroStrategy": "Labour/Tory parliamentary arithmetic provides a commanding working majority; cross-party rebels lack the 50 signatures needed to force statutory dissolution.",
                    "newsCatalyst": {
                        "headline": "Financial Times: Whips confirm government retains solid 60+ vote cushion on procedural debate",
                        "source": "Financial Times UK",
                        "time": "2h ago",
                        "impact": "STABILIZING CATALYST"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Westminster Twitter Watch",
                        "sentimentScore": 75,
                        "sentimentTrend": "+11% Stability bias",
                        "whaleFlows": "Institutional macro book makers laying heavy YES bets across London books",
                        "retailPositioning": "High tabloid noise generating phantom panic on retail side"
                    },
                    "riskMitigation": "Treat as low-volatility yield trade; take profit at 0.93."
                }
            },
            {
                "id": "pol-d-04",
                "rank": 4,
                "title": "Will the Federal Government avoid a partial shutdown deadline tonight?",
                "slug": "us-federal-government-avoid-partial-shutdown-tonight",
                "volume": "$9,780,000",
                "volumeRaw": 9780000,
                "volumeLabel": "24H Volume",
                "liquidity": "$2,100,000",
                "endDate": "Midnight EST",
                "outcomes": [{"name": "YES (Avoids)", "price": 0.88, "pct": 88}, {"name": "NO (Shutdown)", "price": 0.12, "pct": 12}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 92,
                    "evEdge": "+7.0% EV+",
                    "impliedProb": 88,
                    "fairValueProb": 95.0,
                    "targetExit": "$0.97 (+10.2% return)",
                    "stopLoss": "$0.75",
                    "macroStrategy": "Continuing Resolution (CR) text agreed upon by appropriations committees; emergency rule waived for expedited floor tally.",
                    "newsCatalyst": {
                        "headline": "AP News: House leadership files 45-day stopgap funding measure with bipartisan backing",
                        "source": "Associated Press",
                        "time": "1h ago",
                        "impact": "CLEAR PASSAGE"
                    },
                    "socialMediaRadar": {
                        "platform": "Polymarket Order Flow & X Political Pulse",
                        "sentimentScore": 88,
                        "sentimentTrend": "Strong consensus building",
                        "whaleFlows": "$450k YES volume transacted in 4 hours",
                        "retailPositioning": "Overblown doomsday headlines keeping NO artificially at 12c"
                    },
                    "riskMitigation": "Size appropriately for asymmetric high-probability cash preservation."
                }
            },
            {
                "id": "pol-d-05",
                "rank": 5,
                "title": "Will French Prime Minister survive the no-confidence vote today?",
                "slug": "french-pm-survive-no-confidence-vote",
                "volume": "$8,650,000",
                "volumeRaw": 8650000,
                "volumeLabel": "24H Volume",
                "liquidity": "$1,980,000",
                "endDate": "Today 6:00 PM CET",
                "outcomes": [{"name": "SURVIVES", "price": 0.44, "pct": 44}, {"name": "FALLS", "price": 0.56, "pct": 56}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET SURVIVES (CONTRARIAN ALPHA)",
                    "conviction": "HIGH ALPHA CONTRARIAN",
                    "confidencePct": 78,
                    "evEdge": "+18.0% EV+",
                    "impliedProb": 44,
                    "fairValueProb": 62.0,
                    "targetExit": "$0.72 (+63.6% return)",
                    "stopLoss": "$0.32",
                    "macroStrategy": "National Rally (RN) party leadership signaled aversion to triggering winter legislative deadlock ahead of budget deficit EU penalties; abstentions will lower requisite absolute threshold.",
                    "newsCatalyst": {
                        "headline": "Le Figaro / Reuters: Le Pen's faction indicates willingness to abstain if healthcare spending concessions hold",
                        "source": "Reuters Paris",
                        "time": "1h ago",
                        "impact": "CRUCIAL COMPROMISE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / France Politique Analysis",
                        "sentimentScore": 65,
                        "sentimentTrend": "+25% Bullish survival inflection",
                        "whaleFlows": "Paris-based macro hedge funds purchasing SURVIVES outcome at heavy discount",
                        "retailPositioning": "Retail herd piling into FALLS after panic headlines"
                    },
                    "riskMitigation": "Enter half position at 0.44; add if dips to 0.40; take rapid gains on abstention announcement."
                }
            },
            {
                "id": "pol-d-06",
                "rank": 6,
                "title": "Will Texas Special Election runoff be called for GOP nominee by midnight?",
                "slug": "texas-special-election-gop-midnight",
                "volume": "$6,920,000",
                "volumeRaw": 6920000,
                "volumeLabel": "24H Volume",
                "liquidity": "$1,540,000",
                "endDate": "Midnight CST",
                "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 84,
                    "evEdge": "+12.0% EV+",
                    "impliedProb": 69,
                    "fairValueProb": 81.0,
                    "targetExit": "$0.87 (+26.1% return)",
                    "stopLoss": "$0.55",
                    "macroStrategy": "Early mail-in ballots and rural county turnout exceed 2022 benchmarks by +8.4%, reinforcing historical red-district firewall.",
                    "newsCatalyst": {
                        "headline": "Texas Tribune: Rural precinct early tallies show heavy +14 margin favoring Republican incumbent",
                        "source": "Texas Tribune",
                        "time": "3h ago",
                        "impact": "STATISTICAL ADVANTAGE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Decision Desk HQ & Dave Wasserman Feeds",
                        "sentimentScore": 77,
                        "sentimentTrend": "Steadily positive",
                        "whaleFlows": "Whale limit buys placed at 0.67",
                        "retailPositioning": "Balanced betting book with mispriced upside"
                    },
                    "riskMitigation": "Exit fully once Decision Desk calls the race."
                }
            },
            {
                "id": "pol-d-07",
                "rank": 7,
                "title": "Will Germany's Bundestag schedule the snap election date officially today?",
                "slug": "germany-bundestag-snap-election-date-today",
                "volume": "$5,840,000",
                "volumeRaw": 5840000,
                "volumeLabel": "24H Volume",
                "liquidity": "$1,320,000",
                "endDate": "Today 8:00 PM CET",
                "outcomes": [{"name": "YES", "price": 0.77, "pct": 77}, {"name": "NO", "price": 0.23, "pct": 23}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 88,
                    "evEdge": "+11.0% EV+",
                    "impliedProb": 77,
                    "fairValueProb": 88.0,
                    "targetExit": "$0.92 (+19.5% return)",
                    "stopLoss": "$0.65",
                    "macroStrategy": "CDU/CSU and SPD faction leaders agreed on late-February timetable; Federal President Steinmeier cleared constitutional paperwork.",
                    "newsCatalyst": {
                        "headline": "Deutsche Welle: Coalition leaders reach consensus on dissolution timeline",
                        "source": "Deutsche Welle / Tagesschau",
                        "time": "2h ago",
                        "impact": "PROCEDURAL CERTAINTY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / German Politics & Der Spiegel live feed",
                        "sentimentScore": 81,
                        "sentimentTrend": "+18% Bullish momentum",
                        "whaleFlows": "Consistent institutional inflows into YES contracts",
                        "retailPositioning": "Retail waiting for formal podium announcement"
                    },
                    "riskMitigation": "Capture safe spread before televised press conference."
                }
            },
            {
                "id": "pol-d-08",
                "rank": 8,
                "title": "Will the G7 Joint Communique announce new secondary sanctions today?",
                "slug": "g7-joint-communique-secondary-sanctions-today",
                "volume": "$4,930,000",
                "volumeRaw": 4930000,
                "volumeLabel": "24H Volume",
                "liquidity": "$1,150,000",
                "endDate": "Today 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "MEDIUM-HIGH CONVICTION",
                    "confidencePct": 81,
                    "evEdge": "+15.0% EV+",
                    "impliedProb": 58,
                    "fairValueProb": 73.0,
                    "targetExit": "$0.79 (+36.2% return)",
                    "stopLoss": "$0.45",
                    "macroStrategy": "Diplomatic sources leak drafted annex targeting third-party maritime transshipment hubs and shadow fleet insurers.",
                    "newsCatalyst": {
                        "headline": "Wall Street Journal: G7 finance ministers finalize maritime enforcement language in joint text",
                        "source": "WSJ Diplomatic Cable",
                        "time": "3h ago",
                        "impact": "BULLISH TRANSMISSION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Geopolitical Defense Radar",
                        "sentimentScore": 74,
                        "sentimentTrend": "+14% Sentiment surge",
                        "whaleFlows": "Macro global funds loading up on YES",
                        "retailPositioning": "Under-traded relative to equity impact"
                    },
                    "riskMitigation": "Take profits when final communiqué text published on Treasury.gov."
                }
            },
            {
                "id": "pol-d-09",
                "rank": 9,
                "title": "Will US Supreme Court grant cert on the Interstate Commerce Tech challenge today?",
                "slug": "scotus-grant-cert-interstate-commerce-tech-today",
                "volume": "$4,210,000",
                "volumeRaw": 4210000,
                "volumeLabel": "24H Volume",
                "liquidity": "$980,000",
                "endDate": "Today 4:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.35, "pct": 35}, {"name": "NO", "price": 0.65, "pct": 65}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 87,
                    "evEdge": "+13.0% EV+",
                    "impliedProb": 65,
                    "fairValueProb": 78.0,
                    "targetExit": "$0.84 (+29.2% return)",
                    "stopLoss": "$0.52",
                    "macroStrategy": "Circuit split between 5th and 9th circuits is not yet ripe; Solicitor General amicus brief explicitly urged high court to defer pending district court evidentiary hearings.",
                    "newsCatalyst": {
                        "headline": "SCOTUSblog: Solicitor General brief urges denial of interlocutory certiorari",
                        "source": "SCOTUSblog",
                        "time": "4h ago",
                        "impact": "BEARISH ON GRANT"
                    },
                    "socialMediaRadar": {
                        "platform": "Legal Twitter & FedSoc Scholars",
                        "sentimentScore": 82,
                        "sentimentTrend": "High consensus on denial / relist",
                        "whaleFlows": "Sharp institutional accumulation of NO",
                        "retailPositioning": "Retail speculation betting on headline hype"
                    },
                    "riskMitigation": "Hold NO into 10am order list release."
                }
            },
            {
                "id": "pol-d-10",
                "rank": 10,
                "title": "Will Canadian Parliament trigger a non-confidence motion vote today?",
                "slug": "canadian-parliament-non-confidence-motion-today",
                "volume": "$3,790,000",
                "volumeRaw": 3790000,
                "volumeLabel": "24H Volume",
                "liquidity": "$890,000",
                "endDate": "Today 10:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.28, "pct": 28}, {"name": "NO", "price": 0.72, "pct": 72}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 89,
                    "evEdge": "+12.0% EV+",
                    "impliedProb": 72,
                    "fairValueProb": 84.0,
                    "targetExit": "$0.89 (+23.6% return)",
                    "stopLoss": "$0.60",
                    "macroStrategy": "Bloc Québécois confirmed they will not support Conservative opposition motion today following favorable regional healthcare allocations.",
                    "newsCatalyst": {
                        "headline": "CBC News: Bloc leader confirms caucus will vote against immediate snap election push",
                        "source": "CBC News Ottawa",
                        "time": "2h ago",
                        "impact": "STATUS QUO REINFORCED"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Canada Politics",
                        "sentimentScore": 76,
                        "sentimentTrend": "+15% NO consolidation",
                        "whaleFlows": "$140k NO contracts accumulated",
                        "retailPositioning": "Retail misjudged opposition leverage"
                    },
                    "riskMitigation": "Capture steady yield before debate adjournment."
                }
            }
        ],
        "week": [
            {
                "id": "pol-w-01",
                "rank": 1,
                "title": "Will US Bipartisan Border & Customs Funding Bill pass the Senate this week?",
                "slug": "us-bipartisan-border-customs-senate-pass-this-week",
                "volume": "$48,920,000",
                "volumeRaw": 48920000,
                "volumeLabel": "7D Volume",
                "liquidity": "$9,450,000",
                "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 88,
                    "evEdge": "+14.0% EV+",
                    "impliedProb": 67,
                    "fairValueProb": 81.0,
                    "targetExit": "$0.86 (+28.3% return)",
                    "stopLoss": "$0.54",
                    "macroStrategy": "Bipartisan leadership negotiated inclusion of border tech procurement funding favored by swing-state delegations; provides 63 committed votes.",
                    "newsCatalyst": {
                        "headline": "Politico: Senate negotiators finalize draft border enforcement package with veto-proof majority",
                        "source": "Politico Pro",
                        "time": "1 day ago",
                        "impact": "LEGISLATIVE MOMENTUM"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Capitol Hill Insiders",
                        "sentimentScore": 81,
                        "sentimentTrend": "+20% Weekly Bullish accumulation",
                        "whaleFlows": "Multi-million dollar whale stakes locked in YES",
                        "retailPositioning": "Retail skeptical due to prior gridlock, providing prime entry"
                    },
                    "riskMitigation": "Sell 50% at 0.82 ahead of formal roll call."
                }
            },
            {
                "id": "pol-w-02",
                "rank": 2,
                "title": "Will US President announce new Universal Tariffs on Asian semiconductor imports this week?",
                "slug": "us-universal-tariffs-asian-semiconductors-this-week",
                "volume": "$41,200,000",
                "volumeRaw": 41200000,
                "volumeLabel": "7D Volume",
                "liquidity": "$8,100,000",
                "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.42, "pct": 42}, {"name": "NO", "price": 0.58, "pct": 58}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO (MACRO DEFENSIVE)",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 86,
                    "evEdge": "+16.0% EV+",
                    "impliedProb": 58,
                    "fairValueProb": 74.0,
                    "targetExit": "$0.78 (+34.5% return)",
                    "stopLoss": "$0.44",
                    "macroStrategy": "National Economic Council and tech executives privately warned of immediate domestic inflation spike; trade reps opted for 90-day bilateral consultation period first.",
                    "newsCatalyst": {
                        "headline": "Bloomberg: White House economic advisers push for targeted carve-outs rather than broad tariffs",
                        "source": "Bloomberg Trade",
                        "time": "18h ago",
                        "impact": "DE-ESCALATION SIGNAL"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Macro & Supply Chain Analysts",
                        "sentimentScore": 77,
                        "sentimentTrend": "+18% NO momentum shift",
                        "whaleFlows": "Macro hedge funds buying NO as tech supply chain hedge",
                        "retailPositioning": "Retail panic-buying YES based on campaign soundbites"
                    },
                    "riskMitigation": "Lock gains before Sunday night trade report release."
                }
            },
            {
                "id": "pol-w-03",
                "rank": 3,
                "title": "Will EU Commission pass the AI Sovereignty Fund regulatory framework this week?",
                "slug": "eu-commission-ai-sovereignty-fund-this-week",
                "volume": "$32,840,000",
                "volumeRaw": 32840000,
                "volumeLabel": "7D Volume",
                "liquidity": "$6,700,000",
                "endDate": "Friday 6:00 PM CET",
                "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 89,
                    "evEdge": "+12.0% EV+",
                    "impliedProb": 74,
                    "fairValueProb": 86.0,
                    "targetExit": "$0.91 (+23.0% return)",
                    "stopLoss": "$0.62",
                    "macroStrategy": "Franco-German joint declaration removed the last major roadblock concerning state aid caps for sovereign compute clusters.",
                    "newsCatalyst": {
                        "headline": "Financial Times: Berlin and Paris present unified AI infrastructure plan to European Council",
                        "source": "Financial Times Brussels",
                        "time": "1 day ago",
                        "impact": "REGULATORY CONSENSUS"
                    },
                    "socialMediaRadar": {
                        "platform": "X / EU Tech Policy",
                        "sentimentScore": 83,
                        "sentimentTrend": "Strong upward trend",
                        "whaleFlows": "European VC & institutional accounts driving YES volume",
                        "retailPositioning": "Underpriced liquidity on global order book"
                    },
                    "riskMitigation": "Take profits ahead of Friday EU press conference."
                }
            },
            {
                "id": "pol-w-04",
                "rank": 4,
                "title": "Will UK Labour Party win the Mid-Bedfordshire Council by-election this week?",
                "slug": "uk-labour-mid-bedfordshire-by-election",
                "volume": "$24,500,000",
                "volumeRaw": 24500000,
                "volumeLabel": "7D Volume",
                "liquidity": "$4,900,000",
                "endDate": "Thursday Midnight GMT",
                "outcomes": [{"name": "LABOUR", "price": 0.62, "pct": 62}, {"name": "CONSERVATIVE / LIB DEM", "price": 0.38, "pct": 38}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET LABOUR",
                    "conviction": "MEDIUM-HIGH CONVICTION",
                    "confidencePct": 83,
                    "evEdge": "+13.0% EV+",
                    "impliedProb": 62,
                    "fairValueProb": 75.0,
                    "targetExit": "$0.82 (+32.2% return)",
                    "stopLoss": "$0.48",
                    "macroStrategy": "Canvassing turnout data in suburban wards shows strong swing away from Tory incumbency; Lib Dem vote splitting remains minimal.",
                    "newsCatalyst": {
                        "headline": "The Guardian / YouGov: Final polling puts Labour candidate ahead by 7 percentage points",
                        "source": "YouGov Polling",
                        "time": "1 day ago",
                        "impact": "POLLING ADVANTAGE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / UK Polling Report",
                        "sentimentScore": 76,
                        "sentimentTrend": "+14% Bullish Labour",
                        "whaleFlows": "British political betting syndicates backing Labour",
                        "retailPositioning": "Retail hedging heavily across three-way split"
                    },
                    "riskMitigation": "Exit position when postal ballot verification completes."
                }
            },
            {
                "id": "pol-w-05",
                "rank": 5,
                "title": "Will Japanese Diet approve Prime Minister's Supplemental Economic Stimulus this week?",
                "slug": "japan-diet-supplemental-economic-stimulus-this-week",
                "volume": "$21,100,000",
                "volumeRaw": 21100000,
                "volumeLabel": "7D Volume",
                "liquidity": "$4,300,000",
                "endDate": "Friday 5:00 PM JST",
                "outcomes": [{"name": "YES", "price": 0.81, "pct": 81}, {"name": "NO", "price": 0.19, "pct": 19}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 91,
                    "evEdge": "+9.0% EV+",
                    "impliedProb": 81,
                    "fairValueProb": 90.0,
                    "targetExit": "$0.94 (+16.0% return)",
                    "stopLoss": "$0.70",
                    "macroStrategy": "Komeito coalition partner and DPP opposition factions agreed on tax-threshold inflation adjustments, unlocking decisive committee majority.",
                    "newsCatalyst": {
                        "headline": "Nikkei Asia: Ruling coalition and DPP strike agreement on ¥13.9 trillion stimulus package",
                        "source": "Nikkei Asia Tokyo",
                        "time": "12h ago",
                        "impact": "LEGISLATIVE ASSURANCE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Tokyo Market Desk",
                        "sentimentScore": 85,
                        "sentimentTrend": "Broad consensus",
                        "whaleFlows": "Japanese macro desks executing large YES fills",
                        "retailPositioning": "Low retail participation creates clean EV yield"
                    },
                    "riskMitigation": "Ideal defensive cash-enhancement bet."
                }
            },
            {
                "id": "pol-w-06",
                "rank": 6,
                "title": "Will the Federal Reserve Chair face formal Congressional subpoena from Oversight Committee this week?",
                "slug": "fed-chair-congressional-subpoena-this-week",
                "volume": "$18,300,000",
                "volumeRaw": 18300000,
                "volumeLabel": "7D Volume",
                "liquidity": "$3,700,000",
                "endDate": "Friday 6:00 PM EST",
                "outcomes": [{"name": "YES", "price": 0.16, "pct": 16}, {"name": "NO", "price": 0.84, "pct": 84}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "VERY HIGH CONVICTION",
                    "confidencePct": 94,
                    "evEdge": "+8.0% EV+",
                    "impliedProb": 84,
                    "fairValueProb": 92.0,
                    "targetExit": "$0.96 (+14.3% return)",
                    "stopLoss": "$0.72",
                    "macroStrategy": "Committee legal counsel confirmed testimony will proceed under voluntary appearance framework; subpoena was pure political posturing without committee markup votes.",
                    "newsCatalyst": {
                        "headline": "Reuters: Fed Chair agrees to voluntary oversight hearing date; subpoena threats rescinded",
                        "source": "Reuters Washington",
                        "time": "16h ago",
                        "impact": "DE-ESCALATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Financial Reg Watch",
                        "sentimentScore": 90,
                        "sentimentTrend": "+20% NO certainty",
                        "whaleFlows": "Heavy institutional selling of YES / buying of NO",
                        "retailPositioning": "Retail panic traders bought YES on cable TV sensationalism"
                    },
                    "riskMitigation": "Hold NO until Friday committee calendar formalization."
                }
            },
            {
                "id": "pol-w-07",
                "rank": 7,
                "title": "Will US Defense Supplemental Package include accelerated Pacific deterrence funding this week?",
                "slug": "us-defense-supplemental-pacific-deterrence-this-week",
                "volume": "$16,900,000",
                "volumeRaw": 16900000,
                "volumeLabel": "7D Volume",
                "liquidity": "$3,400,000",
                "endDate": "Saturday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 87,
                    "evEdge": "+11.0% EV+",
                    "impliedProb": 72,
                    "fairValueProb": 83.0,
                    "targetExit": "$0.89 (+23.6% return)",
                    "stopLoss": "$0.59",
                    "macroStrategy": "Armed Services committee chairs from both parties jointly penned defense authorization line items guaranteeing \$8.2B submarine and drone intercept funding.",
                    "newsCatalyst": {
                        "headline": "Defense News: Senate Armed Services leaders release consensus Pacific readiness amendment",
                        "source": "Defense News",
                        "time": "1 day ago",
                        "impact": "BULLISH PASSAGE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Defense & Geopolitics",
                        "sentimentScore": 80,
                        "sentimentTrend": "Solid upward trend",
                        "whaleFlows": "Consistent smart money accumulation",
                        "retailPositioning": "Standard betting volume"
                    },
                    "riskMitigation": "Sell upon Senate floor passage."
                }
            },
            {
                "id": "pol-w-08",
                "rank": 8,
                "title": "Will Turkish Central Bank Governor maintain post following Parliamentary audit this week?",
                "slug": "turkey-cbrt-governor-maintain-post-this-week",
                "volume": "$14,400,000",
                "volumeRaw": 14400000,
                "volumeLabel": "7D Volume",
                "liquidity": "$2,900,000",
                "endDate": "Friday 5:00 PM TRT",
                "outcomes": [{"name": "YES", "price": 0.86, "pct": 86}, {"name": "NO", "price": 0.14, "pct": 14}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 90,
                    "evEdge": "+6.5% EV+",
                    "impliedProb": 86,
                    "fairValueProb": 92.5,
                    "targetExit": "$0.96 (+11.6% return)",
                    "stopLoss": "$0.76",
                    "macroStrategy": "Presidential palace and Finance Minister Simsek explicitly reaffirmed commitment to orthodox disinflation monetary policy to preserve sovereign credit rating upgrades.",
                    "newsCatalyst": {
                        "headline": "Bloomberg: Finance Minister Mehmet Simsek gives full backing to CBRT leadership team",
                        "source": "Bloomberg Emerging Markets",
                        "time": "1 day ago",
                        "impact": "POLICY CONTINUITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / EM Macro & FX Desks",
                        "sentimentScore": 86,
                        "sentimentTrend": "High stability",
                        "whaleFlows": "Macro FX books taking low-risk YES yield",
                        "retailPositioning": "Residual retail worry lingering"
                    },
                    "riskMitigation": "Hold to maturity for conservative +11.6% return."
                }
            },
            {
                "id": "pol-w-09",
                "rank": 9,
                "title": "Will South Korea's National Assembly ratify the US-ROK Critical Minerals Agreement this week?",
                "slug": "south-korea-ratify-us-rok-critical-minerals-this-week",
                "volume": "$12,800,000",
                "volumeRaw": 12800000,
                "volumeLabel": "7D Volume",
                "liquidity": "$2,600,000",
                "endDate": "Friday 6:00 PM KST",
                "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 84,
                    "evEdge": "+13.0% EV+",
                    "impliedProb": 63,
                    "fairValueProb": 76.0,
                    "targetExit": "$0.83 (+31.7% return)",
                    "stopLoss": "$0.50",
                    "macroStrategy": "Domestic battery conglomerates (LG, Samsung SDI) successfully lobbied ruling and opposition trade committees to safeguard IRA tax credits.",
                    "newsCatalyst": {
                        "headline": "Yonhap News: Trade committee schedules final plenary vote with cross-party backing",
                        "source": "Yonhap News Agency",
                        "time": "18h ago",
                        "impact": "POSITIVE RATIFICATION"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Seoul Tech & Market Beat",
                        "sentimentScore": 78,
                        "sentimentTrend": "+16% Bullish momentum",
                        "whaleFlows": "APAC macro syndicate betting YES",
                        "retailPositioning": "Under the radar globally"
                    },
                    "riskMitigation": "Take profits upon plenary vote conclusion."
                }
            },
            {
                "id": "pol-w-10",
                "rank": 10,
                "title": "Will UN Security Council adopt ceasefire resolution text on Red Sea maritime passage this week?",
                "slug": "un-security-council-red-sea-resolution-this-week",
                "volume": "$11,500,000",
                "volumeRaw": 11500000,
                "volumeLabel": "7D Volume",
                "liquidity": "$2,300,000",
                "endDate": "Sunday 11:59 PM EST",
                "outcomes": [{"name": "YES", "price": 0.31, "pct": 31}, {"name": "NO", "price": 0.69, "pct": 69}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 88,
                    "evEdge": "+14.0% EV+",
                    "impliedProb": 69,
                    "fairValueProb": 83.0,
                    "targetExit": "$0.88 (+27.5% return)",
                    "stopLoss": "$0.55",
                    "macroStrategy": "Draft text faces guaranteed veto due to unresolved wording regarding regional naval escort mandates and sovereign territorial waters.",
                    "newsCatalyst": {
                        "headline": "Al Jazeera / Reuters: Permanent member delegations cite irreconcilable differences in maritime mandate draft",
                        "source": "Reuters UN Bureau",
                        "time": "14h ago",
                        "impact": "DEADLOCK CERTAINTY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / UN Diplomatic Wire",
                        "sentimentScore": 82,
                        "sentimentTrend": "+17% NO dominance",
                        "whaleFlows": "Commodity trade desks hedging shipping rates with NO",
                        "retailPositioning": "Optimistic retail buying YES on hope"
                    },
                    "riskMitigation": "Capture safe alpha spread on NO."
                }
            }
        ],
        "month": [
            {
                "id": "pol-m-01",
                "rank": 1,
                "title": "Which Party will hold the US House of Representatives Majority entering the next Congress?",
                "slug": "party-us-house-majority-next-congress",
                "volume": "$194,500,000",
                "volumeRaw": 194500000,
                "volumeLabel": "30D Volume",
                "liquidity": "$38,400,000",
                "endDate": "Dec 31, 2026",
                "outcomes": [{"name": "REPUBLICAN", "price": 0.54, "pct": 54}, {"name": "DEMOCRATIC", "price": 0.46, "pct": 46}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET REPUBLICAN (VALUE ALPHA)",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 85,
                    "evEdge": "+11.0% EV+",
                    "impliedProb": 54,
                    "fairValueProb": 65.0,
                    "targetExit": "$0.72 (+33.3% return)",
                    "stopLoss": "$0.42",
                    "macroStrategy": "Redistricting maps finalized in North Carolina, Ohio, and Missouri provide a structural net +5 seat structural baseline; historical mid-cycle incumbency voter retention holds firm.",
                    "newsCatalyst": {
                        "headline": "Cook Political Report: Finalized congressional map adjustments create defensible GOP floor",
                        "source": "Cook Political Report",
                        "time": "3 days ago",
                        "impact": "STRUCTURAL ADVANTAGE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Silver Bulletin & Nate Cohn Analysis",
                        "sentimentScore": 79,
                        "sentimentTrend": "+14% Shift toward GOP baseline",
                        "whaleFlows": "Polymarket mega-whales holding $8M+ Republican contracts",
                        "retailPositioning": "Retail evenly split at 50/50, providing high-margin edge"
                    },
                    "riskMitigation": "Accumulate on pullbacks below 0.52; trim at 0.70."
                }
            },
            {
                "id": "pol-m-02",
                "rank": 2,
                "title": "Will the US Federal Debt Ceiling be permanently raised or suspended before month-end?",
                "slug": "us-debt-ceiling-raised-suspended-month-end",
                "volume": "$142,300,000",
                "volumeRaw": 142300000,
                "volumeLabel": "30D Volume",
                "liquidity": "$28,100,000",
                "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.85, "pct": 85}, {"name": "NO", "price": 0.15, "pct": 15}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "VERY HIGH CONVICTION",
                    "confidencePct": 94,
                    "evEdge": "+8.0% EV+",
                    "impliedProb": 85,
                    "fairValueProb": 93.0,
                    "targetExit": "$0.96 (+12.9% return)",
                    "stopLoss": "$0.72",
                    "macroStrategy": "Treasury extraordinary measures depletion date (X-date) verified; Wall Street primary dealers and bank CEOs made mandatory backchannel commitments guaranteeing legislative rider.",
                    "newsCatalyst": {
                        "headline": "WSJ: Treasury Secretary and Congressional leaders finalize debt limit suspension framework",
                        "source": "Wall Street Journal Macro",
                        "time": "2 days ago",
                        "impact": "SYSTEMIC NECESSITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Bond Market & Macro Vigilantes",
                        "sentimentScore": 88,
                        "sentimentTrend": "+12% Certainty surge",
                        "whaleFlows": "Over $15M in institutional capital deployed into YES",
                        "retailPositioning": "Retail panic hedging creates mispriced discount"
                    },
                    "riskMitigation": "Ideal multi-million dollar cash treasury yield enhancement play."
                }
            },
            {
                "id": "pol-m-03",
                "rank": 3,
                "title": "Will Germany hold an official Federal Election in Q1 following coalition dissolution?",
                "slug": "germany-federal-election-q1-coalition",
                "volume": "$98,700,000",
                "volumeRaw": 98700000,
                "volumeLabel": "30D Volume",
                "liquidity": "$19,500,000",
                "endDate": "End of Quarter",
                "outcomes": [{"name": "YES", "price": 0.91, "pct": 91}, {"name": "NO", "price": 0.09, "pct": 9}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "MAX CONVICTION",
                    "confidencePct": 96,
                    "evEdge": "+6.0% EV+",
                    "impliedProb": 91,
                    "fairValueProb": 97.0,
                    "targetExit": "$0.98 (+7.7% return)",
                    "stopLoss": "$0.80",
                    "macroStrategy": "Federal President Steinmeier officially confirmed dissolution timeline; logistical ballot printing cleared by Bundeswahlleiter.",
                    "newsCatalyst": {
                        "headline": "FAZ / Reuters: Federal Returning Officer confirms all constitutional readiness benchmarks met for February election",
                        "source": "Frankfurter Allgemeine Zeitung",
                        "time": "2 days ago",
                        "impact": "CONSTITUTIONAL CERTAINTY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / European Political Watch",
                        "sentimentScore": 94,
                        "sentimentTrend": "Irreversible trajectory",
                        "whaleFlows": "Major institutional macro funds holding YES as cash equivalent",
                        "retailPositioning": "Negligible counter-trend activity"
                    },
                    "riskMitigation": "Treat as institutional near-riskless arbitrage."
                }
            },
            {
                "id": "pol-m-04",
                "rank": 4,
                "title": "Will the European Union ratify the Mercosur Trade Agreement this month?",
                "slug": "eu-ratify-mercosur-trade-agreement-this-month",
                "volume": "$82,400,000",
                "volumeRaw": 82400000,
                "volumeLabel": "30D Volume",
                "liquidity": "$16,200,000",
                "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.48, "pct": 48}, {"name": "NO", "price": 0.52, "pct": 52}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES (TACTICAL VALUE)",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 82,
                    "evEdge": "+17.0% EV+",
                    "impliedProb": 48,
                    "fairValueProb": 65.0,
                    "targetExit": "$0.75 (+56.2% return)",
                    "stopLoss": "$0.36",
                    "macroStrategy": "European Commission split the agreement into trade and political pillars, circumventing French agricultural veto requirement via qualified majority voting (QMV).",
                    "newsCatalyst": {
                        "headline": "Euractiv: Commission legal service confirms qualified majority suffices under pillar split",
                        "source": "Euractiv Brussels",
                        "time": "3 days ago",
                        "impact": "LEGAL BREAKTHROUGH"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Ag & Trade Macro",
                        "sentimentScore": 73,
                        "sentimentTrend": "+21% Bullish re-rating",
                        "whaleFlows": "Smart money accumulating YES on oversold French farmer protest headlines",
                        "retailPositioning": "Retail wrongly assumes France has absolute veto"
                    },
                    "riskMitigation": "Size moderately; take 60% profit on qualified majority declaration."
                }
            },
            {
                "id": "pol-m-05",
                "rank": 5,
                "title": "Will UK Labour retain the Mayor of London leadership through upcoming council terms?",
                "slug": "uk-labour-mayor-of-london-term",
                "volume": "$68,900,000",
                "volumeRaw": 68900000,
                "volumeLabel": "30D Volume",
                "liquidity": "$13,800,000",
                "endDate": "End of Quarter",
                "outcomes": [{"name": "YES", "price": 0.79, "pct": 79}, {"name": "NO", "price": 0.21, "pct": 21}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 88,
                    "evEdge": "+10.0% EV+",
                    "impliedProb": 79,
                    "fairValueProb": 89.0,
                    "targetExit": "$0.93 (+17.7% return)",
                    "stopLoss": "$0.68",
                    "macroStrategy": "Demographic structural voting patterns in Greater London boroughs make conservative recovery mathematically improbable despite ULEZ controversies.",
                    "newsCatalyst": {
                        "headline": "Evening Standard: Internal polling demonstrates unassailable +14 pt lead in inner London wards",
                        "source": "Evening Standard London",
                        "time": "4 days ago",
                        "impact": "DATA RESILIENCE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / London Politics",
                        "sentimentScore": 81,
                        "sentimentTrend": "Stable",
                        "whaleFlows": "Consistent UK betting exchange liquidity supporting YES",
                        "retailPositioning": "Right-leaning tabloids generating noisy but ineffective opposition"
                    },
                    "riskMitigation": "Steady compounding position."
                }
            },
            {
                "id": "pol-m-06",
                "rank": 6,
                "title": "Will US Senate ratify New Strategic Arms Control Treaty framework this year?",
                "slug": "us-senate-strategic-arms-control-treaty-this-year",
                "volume": "$54,100,000",
                "volumeRaw": 54100000,
                "volumeLabel": "30D Volume",
                "liquidity": "$10,700,000",
                "endDate": "End of Year",
                "outcomes": [{"name": "YES", "price": 0.14, "pct": 14}, {"name": "NO", "price": 0.86, "pct": 86}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "VERY HIGH CONVICTION",
                    "confidencePct": 95,
                    "evEdge": "+8.0% EV+",
                    "impliedProb": 86,
                    "fairValueProb": 94.0,
                    "targetExit": "$0.97 (+12.8% return)",
                    "stopLoss": "$0.76",
                    "macroStrategy": "A two-thirds constitutional treaty supermajority (67 votes) is currently unobtainable given geopolitical tensions and ballistic modernization priorities.",
                    "newsCatalyst": {
                        "headline": "Foreign Affairs: Senate Foreign Relations Committee members confirm treaty ratification dormant indefinitely",
                        "source": "Foreign Affairs Journal",
                        "time": "5 days ago",
                        "impact": "DIPLOMATIC ICE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Nuclear Nonproliferation Watch",
                        "sentimentScore": 92,
                        "sentimentTrend": "Solid NO baseline",
                        "whaleFlows": "Institutional political risk books shorting YES",
                        "retailPositioning": "Retail occasionally buying cheap YES lotto tickets"
                    },
                    "riskMitigation": "Capture institutional risk-free spread on NO."
                }
            },
            {
                "id": "pol-m-07",
                "rank": 7,
                "title": "Will the European Union impose definitive tariffs on imported electric vehicles this month?",
                "slug": "eu-tariffs-imported-evs-this-month",
                "volume": "$49,800,000",
                "volumeRaw": 49800000,
                "volumeLabel": "30D Volume",
                "liquidity": "$9,800,000",
                "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.88, "pct": 88}, {"name": "NO", "price": 0.12, "pct": 12}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 92,
                    "evEdge": "+7.0% EV+",
                    "impliedProb": 88,
                    "fairValueProb": 95.0,
                    "targetExit": "$0.97 (+10.2% return)",
                    "stopLoss": "$0.77",
                    "macroStrategy": "Anti-subsidy investigation conclusion mandates automatic entry into force unless an insurmountable blocking minority forms; Germany failed to assemble requisite population quota.",
                    "newsCatalyst": {
                        "headline": "Bloomberg: EU Council confirms definitive duties published in Official Journal",
                        "source": "Bloomberg Brussels",
                        "time": "4 days ago",
                        "impact": "STATUTORY MANDATE"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Auto Sector Analysts",
                        "sentimentScore": 89,
                        "sentimentTrend": "Certainty cemented",
                        "whaleFlows": "Industrial desks heavily long YES",
                        "retailPositioning": "Minimal opposition"
                    },
                    "riskMitigation": "Harvest safe yield into official gazette publication."
                }
            },
            {
                "id": "pol-m-08",
                "rank": 8,
                "title": "Will Taiwan's Legislative Yuan pass the Special Defense Deterrence Budget this month?",
                "slug": "taiwan-legislative-yuan-special-defense-budget",
                "volume": "$43,200,000",
                "volumeRaw": 43200000,
                "volumeLabel": "30D Volume",
                "liquidity": "$8,500,000",
                "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 87,
                    "evEdge": "+11.0% EV+",
                    "impliedProb": 76,
                    "fairValueProb": 87.0,
                    "targetExit": "$0.92 (+21.0% return)",
                    "stopLoss": "$0.65",
                    "macroStrategy": "KMT and TPP opposition parties agreed to support maritime drone procurement while trimming non-combat domestic expenditures.",
                    "newsCatalyst": {
                        "headline": "Taipei Times: Cross-party defense caucus greenlights critical indigenous submarine funding",
                        "source": "Taipei Times",
                        "time": "3 days ago",
                        "impact": "DEFENSE CONSENSUS"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Indo-Pacific Security",
                        "sentimentScore": 83,
                        "sentimentTrend": "+16% Bullish",
                        "whaleFlows": "Asian geopolitical macro desks accumulating YES",
                        "retailPositioning": "Retail overlooked regional legislative vote"
                    },
                    "riskMitigation": "Take profits ahead of final committee review."
                }
            },
            {
                "id": "pol-m-09",
                "rank": 9,
                "title": "Will the US Federal Reserve Reform Act pass both chambers of Congress this month?",
                "slug": "us-fed-reform-act-pass-both-chambers-this-month",
                "volume": "$38,600,000",
                "volumeRaw": 38600000,
                "volumeLabel": "30D Volume",
                "liquidity": "$7,600,000",
                "endDate": "End of Month",
                "outcomes": [{"name": "YES", "price": 0.11, "pct": 11}, {"name": "NO", "price": 0.89, "pct": 89}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET NO",
                    "conviction": "MAX CONVICTION",
                    "confidencePct": 97,
                    "evEdge": "+7.0% EV+",
                    "impliedProb": 89,
                    "fairValueProb": 96.0,
                    "targetExit": "$0.98 (+10.1% return)",
                    "stopLoss": "$0.80",
                    "macroStrategy": "Senate Banking Committee chairman stated unequivocally the bill will not receive committee consideration, killing any floor viability.",
                    "newsCatalyst": {
                        "headline": "American Banker: Banking Committee leadership issues formal refusal to docket Fed oversight restructuring bill",
                        "source": "American Banker",
                        "time": "4 days ago",
                        "impact": "PROCEDURAL DEATH"
                    },
                    "socialMediaRadar": {
                        "platform": "X / Macro Fed Watchers",
                        "sentimentScore": 95,
                        "sentimentTrend": "Absolute NO conviction",
                        "whaleFlows": "Institutional macro accounts park large liquidity in NO",
                        "retailPositioning": "Zero institutional doubt"
                    },
                    "riskMitigation": "Zero-risk cash booster."
                }
            },
            {
                "id": "pol-m-10",
                "rank": 10,
                "title": "Will the Italian Government coalition hold a stable parliamentary majority through quarter-end?",
                "slug": "italian-government-coalition-parliamentary-majority",
                "volume": "$34,200,000",
                "volumeRaw": 34200000,
                "volumeLabel": "30D Volume",
                "liquidity": "$6,900,000",
                "endDate": "End of Quarter",
                "outcomes": [{"name": "YES", "price": 0.87, "pct": 87}, {"name": "NO", "price": 0.13, "pct": 13}],
                "hedgeFundAdvisory": {
                    "recommendation": "BET YES",
                    "conviction": "HIGH CONVICTION",
                    "confidencePct": 91,
                    "evEdge": "+6.0% EV+",
                    "impliedProb": 87,
                    "fairValueProb": 93.0,
                    "targetExit": "$0.96 (+10.3% return)",
                    "stopLoss": "$0.76",
                    "macroStrategy": "Prime Minister Meloni maintains dominant poll leads over coalition partners Salvini and Tajani; internal incentives strongly favor maintaining ministerial control.",
                    "newsCatalyst": {
                        "headline": "Corriere della Sera: Coalition partners reaffirm loyalty pact following regional ballot victories",
                        "source": "Corriere della Sera Rome",
                        "time": "5 days ago",
                        "impact": "COALITION STABILITY"
                    },
                    "socialMediaRadar": {
                        "platform": "X / BTP Macro & Rome Politics",
                        "sentimentScore": 87,
                        "sentimentTrend": "High stability",
                        "whaleFlows": "Southern European macro funds heavily long YES",
                        "retailPositioning": "Retail non-factor"
                    },
                    "riskMitigation": "Capture safe institutional yield."
                }
            }
        ]
    }
}

# We will populate the remaining categories programmatically and meticulously
EOF_DATA_PREP = True
print("Data structure initialized")
