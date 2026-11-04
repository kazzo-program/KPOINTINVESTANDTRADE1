# -*- coding: utf-8 -*-
"""
Football - Bundesliga Polymarket Top 10 Markets (Day, Week, Month)
Covering top German football fixtures (Der Klassiker, Bayern, Leverkusen, Dortmund, Leipzig), team props, player markets, and league standings.
With full Macro Hedge Fund Strategy, News Catalysts, and Social Media Radar.
"""

BUNDESLIGA_DATA = {
    "day": [
        {
            "id": "bun-d-01", "rank": 1,
            "title": "Will Bayern Munich defeat Borussia Dortmund in today's Der Klassiker?",
            "slug": "bayern-munich-defeat-borussia-dortmund-der-klassiker",
            "volume": "$38,400,000", "volumeRaw": 38400000, "volumeLabel": "24H Volume",
            "liquidity": "$8,200,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.64, "pct": 64}, {"name": "NO", "price": 0.36, "pct": 36}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.9% EV+", "impliedProb": 64, "fairValueProb": 75.0,
                "targetExit": "$0.79 (+23.4% gain)", "stopLoss": "$0.50",
                "macroStrategy": "Vincent Kompany's aggressive high-press forces 14.8 turnovers per 90 in the opposition half. Nuri Şahin's Dortmund has displayed severe defensive vulnerability away from home, conceding 2.2 goals per away fixture.",
                "newsCatalyst": {
                    "headline": "Kicker: Harry Kane, Musiala, and Olise fully fit; Dortmund missing two key defensive anchors through injury",
                    "source": "Kicker Sportmagazin", "time": "1h 30m ago", "impact": "SQUAD ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "Sky Sport DE / r/fcbayern & BVB Reddit",
                    "sentimentScore": 84, "sentimentTrend": "+20% Allianz Arena fortress",
                    "whaleFlows": "German and international betting syndicates entered $420,000 in YES contracts at 0.62-0.64.",
                    "retailPositioning": "Casual fans tempted by Dortmund upset; smart money takes Bayern home dominance."
                },
                "riskMitigation": "Lock 50% profits once Bayern opens a 2-goal lead; hedge if 1-0 past 80 mins."
            }
        },
        {
            "id": "bun-d-02", "rank": 2,
            "title": "Will Harry Kane score an anytime goal in today's Bundesliga fixture?",
            "slug": "harry-kane-score-anytime-goal-today",
            "volume": "$25,800,000", "volumeRaw": 25800000, "volumeLabel": "24H Volume",
            "liquidity": "$5,600,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 90, "evEdge": "+11.8% EV+", "impliedProb": 71, "fairValueProb": 82.0,
                "targetExit": "$0.86 (+21.1% gain)", "stopLoss": "$0.58",
                "macroStrategy": "Kane has scored in 8 of his last 9 Allianz Arena matches, averaging 1.34 goals per 90. He takes penalties and direct free kicks, with Michael Olise and Musiala providing 4.2 shot assists per game directly to him.",
                "newsCatalyst": {
                    "headline": "Opta Franz: Kane conversion rate in Der Klassiker fixtures stands at an extraordinary 38.5%",
                    "source": "Opta Bundesliga Feed", "time": "2h ago", "impact": "LETHAL FINISHING"
                },
                "socialMediaRadar": {
                    "platform": "Kane Tracker / Bundesliga English",
                    "sentimentScore": 91, "sentimentTrend": "+22% Inevitable Kane goal",
                    "whaleFlows": "High-volume football prop syndicates accumulating Kane anytime goal YES.",
                    "retailPositioning": "Complete alignment across world football handicappers."
                },
                "riskMitigation": "Cash out immediately upon Kane's goal."
            }
        },
        {
            "id": "bun-d-03", "rank": 3,
            "title": "Will Bayer Leverkusen score 2 or more goals against RB Leipzig today?",
            "slug": "bayer-leverkusen-score-2-plus-goals-today",
            "volume": "$19,600,000", "volumeRaw": 19600000, "volumeLabel": "24H Volume",
            "liquidity": "$4,200,000", "endDate": "Today 3:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.2% EV+", "impliedProb": 67, "fairValueProb": 77.0,
                "targetExit": "$0.82 (+22.4% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Xabi Alonso's champions average 2.65 goals per game at the BayArena. Florian Wirtz and Victor Boniface create relentless half-space overloads, generating an average xG of 2.44 against high-pressing opponents.",
                "newsCatalyst": {
                    "headline": "BILD Sport: Xabi Alonso deploys full-strength gala attacking lineup with Wirtz, Boniface, and Frimpong starting",
                    "source": "BILD Leverkusen Desk", "time": "2h 30m ago", "impact": "FIREPOWER CONFIRMED"
                },
                "socialMediaRadar": {
                    "platform": "Werkself Live / Bundesliga Twitter",
                    "sentimentScore": 84, "sentimentTrend": "+19% Leverkusen goals momentum",
                    "whaleFlows": "Goal prop specialists pounding Leverkusen Team Total Over 1.5.",
                    "retailPositioning": "High confidence in Alonso's exciting attacking philosophy."
                },
                "riskMitigation": "Execute on Team Over 1.5 Goals YES; exit once second goal is scored."
            }
        },
        {
            "id": "bun-d-04", "rank": 4,
            "title": "Will Jamal Musiala register 1 or more assists today?",
            "slug": "jamal-musiala-register-assist-today",
            "volume": "$14,500,000", "volumeRaw": 14500000, "volumeLabel": "24H Volume",
            "liquidity": "$3,100,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.46, "pct": 46}, {"name": "NO", "price": 0.54, "pct": 54}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+13.4% EV+", "impliedProb": 46, "fairValueProb": 55.5,
                "targetExit": "$0.65 (+41.3% gain)", "stopLoss": "$0.34",
                "macroStrategy": "Musiala's expected assists (xA) in home games is 0.52 per 90. His ability to glide through central mid-blocks creates unmatched tap-in opportunities for Harry Kane and Serge Gnabry.",
                "newsCatalyst": {
                    "headline": "Kicker: Musiala in dazzling form during final training session, slicing through starting center-backs",
                    "source": "Kicker Bayern Beat", "time": "3h ago", "impact": "CREATIVE HUB"
                },
                "socialMediaRadar": {
                    "platform": "Musiala Magic / FCB Inside",
                    "sentimentScore": 79, "sentimentTrend": "+18% Musiala playmaking buzz",
                    "whaleFlows": "Sharp prop syndicates taking the mispriced 0.46 line on Musiala assist.",
                    "retailPositioning": "Public focuses primarily on goalscorers, underpricing assist EV."
                },
                "riskMitigation": "Asymmetric value trade; size at 3.5% allocation."
            }
        },
        {
            "id": "bun-d-05", "rank": 5,
            "title": "Will Eintracht Frankfurt defeat VfB Stuttgart at Deutsche Bank Park today?",
            "slug": "eintracht-frankfurt-defeat-vfb-stuttgart-today",
            "volume": "$16,200,000", "volumeRaw": 16200000, "volumeLabel": "24H Volume",
            "liquidity": "$3,500,000", "endDate": "Today 5:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.55, "pct": 55}, {"name": "NO", "price": 0.45, "pct": 45}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+12.7% EV+", "impliedProb": 55, "fairValueProb": 65.0,
                "targetExit": "$0.71 (+29.1% gain)", "stopLoss": "$0.41",
                "macroStrategy": "Frankfurt's dynamic strike duo (Omar Marmoush and Hugo Ekitike) represents the most explosive counter-attacking unit in Germany, averaging 2.5 goals per match at home. Stuttgart's defense has conceded in 8 consecutive road games.",
                "newsCatalyst": {
                    "headline": "Hessenschau: Marmoush and Ekitike combination deemed unstoppable by opposition scouting reports",
                    "source": "Hessenschau Sport", "time": "3h 30m ago", "impact": "STRIKE FORCE"
                },
                "socialMediaRadar": {
                    "platform": "SGE4EVER / Frankfurt Fans X",
                    "sentimentScore": 81, "sentimentTrend": "+17% Waldstadion fervor",
                    "whaleFlows": "German domestic syndicates backing Frankfurt straight win.",
                    "retailPositioning": "Solid backing for Dino Toppmöller's entertaining side."
                },
                "riskMitigation": "Lock 50% profits once Frankfurt leads by a goal."
            }
        },
        {
            "id": "bun-d-06", "rank": 6,
            "title": "Will Florian Wirtz record Over 2.5 Total Shots on Goal today?",
            "slug": "florian-wirtz-over-25-shots-today",
            "volume": "$12,800,000", "volumeRaw": 12800000, "volumeLabel": "24H Volume",
            "liquidity": "$2,750,000", "endDate": "Today 3:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.4% EV+", "impliedProb": 62, "fairValueProb": 72.0,
                "targetExit": "$0.77 (+24.2% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Wirtz averages 3.4 shots per 90 in Bundesliga fixtures, with Alonso encouraging him to test goalkeepers from distance against compact low blocks. He also takes direct free kicks on the edge of the box.",
                "newsCatalyst": {
                    "headline": "Opta Franz: Florian Wirtz leads all European central attacking midfielders in shots attempted from outside box",
                    "source": "Opta Bundesliga Lab", "time": "4h ago", "impact": "SHOOTING VOLUME"
                },
                "socialMediaRadar": {
                    "platform": "Wirtz Fans / Bundesliga Hub",
                    "sentimentScore": 83, "sentimentTrend": "+18% Shooting confidence",
                    "whaleFlows": "Player prop specialists taking the Over on Wirtz total shots.",
                    "retailPositioning": "Public recognizing Wirtz as Germany's premier generational talent."
                },
                "riskMitigation": "Cash out once 3rd shot is logged on official match stat sheet."
            }
        },
        {
            "id": "bun-d-07", "rank": 7,
            "title": "Will Borussia Dortmund score in the first 30 minutes today?",
            "slug": "borussia-dortmund-score-first-30-minutes-today",
            "volume": "$11,400,000", "volumeRaw": 11400000, "volumeLabel": "24H Volume",
            "liquidity": "$2,450,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.37, "pct": 37}, {"name": "NO", "price": 0.63, "pct": 63}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.1% EV+", "impliedProb": 63, "fairValueProb": 75.0,
                "targetExit": "$0.79 (+25.4% gain on NO)", "stopLoss": "$0.50",
                "macroStrategy": "Bayern Munich's early-match defensive press under Kompany has conceded zero first-half goals at home this season. Dortmund plays cautiously in early Der Klassiker away minutes to survive the initial onslaught.",
                "newsCatalyst": {
                    "headline": "Ruhr Nachrichten: Şahin adopts cautious 5-4-1 low-block strategy for opening 30 minutes in Munich",
                    "source": "Ruhr Nachrichten BVB", "time": "4h 30m ago", "impact": "DEFENSIVE CAUTION"
                },
                "socialMediaRadar": {
                    "platform": "Schwatzgelb / BVB Twitter",
                    "sentimentScore": 76, "sentimentTrend": "+20% Early survival focus",
                    "whaleFlows": "Quant trading desks taking NO on early Dortmund goal.",
                    "retailPositioning": "Recreational punters betting early excitement; data supports clean early sheet."
                },
                "riskMitigation": "Bet NO on early Dortmund goal; redeem automatically at 30:00 mark."
            }
        },
        {
            "id": "bun-d-08", "rank": 8,
            "title": "Will RB Leipzig keep a clean sheet against Wolfsburg today?",
            "slug": "rb-leipzig-keep-clean-sheet-wolfsburg-today",
            "volume": "$13,100,000", "volumeRaw": 13100000, "volumeLabel": "24H Volume",
            "liquidity": "$2,800,000", "endDate": "Today 3:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.5% EV+", "impliedProb": 61, "fairValueProb": 71.5,
                "targetExit": "$0.76 (+24.6% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Marco Rose's Leipzig has the best defensive record in the Bundesliga, conceding only 5 goals in 10 matches (0.50 per game). Péter Gulácsi leads the league in clean sheets (6) and save percentage (84.6%).",
                "newsCatalyst": {
                    "headline": "Leipziger Volkszeitung: Willi Orbán and Castello Lukeba form unbreachable defensive wall",
                    "source": "Leipziger Volkszeitung", "time": "5h ago", "impact": "DEFENSIVE PEAK"
                },
                "socialMediaRadar": {
                    "platform": "RBL Live / German Football Pod",
                    "sentimentScore": 82, "sentimentTrend": "+17% Clean sheet reliability",
                    "whaleFlows": "Defensive prop specialists backing Leipzig clean sheet YES.",
                    "retailPositioning": "Solid institutional backing for Germany's tightest backline."
                },
                "riskMitigation": "Redeem early if Leipzig secures a 2-0 lead."
            }
        },
        {
            "id": "bun-d-09", "rank": 9,
            "title": "Will Michael Olise record an anytime Goal or Assist (G/A) today?",
            "slug": "michael-olise-anytime-goal-or-assist-today",
            "volume": "$15,300,000", "volumeRaw": 15300000, "volumeLabel": "24H Volume",
            "liquidity": "$3,300,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.9% EV+", "impliedProb": 58, "fairValueProb": 68.5,
                "targetExit": "$0.74 (+27.5% gain)", "stopLoss": "$0.45",
                "macroStrategy": "Olise has registered 7 goals and 6 assists in 13 Bayern appearances, averaging a goal contribution every 68 minutes. His left-foot inswinging deliveries and cutbacks are Bayern's primary weapon against Dortmund's left flank.",
                "newsCatalyst": {
                    "headline": "BILD: Kompany identifies Dortmund left-back as prime tactical target for Olise's 1v1 isolation",
                    "source": "BILD Bayern Exclusives", "time": "5h 30m ago", "impact": "TACTICAL TARGET"
                },
                "socialMediaRadar": {
                    "platform": "FCB Inside / French Football Talents",
                    "sentimentScore": 85, "sentimentTrend": "+20% Olise breakout star",
                    "whaleFlows": "Smart money taking Olise G/A prop as top Bayern value angle.",
                    "retailPositioning": "Rapidly growing international fan appreciation."
                },
                "riskMitigation": "Cash out immediately upon Olise goal or assist."
            }
        },
        {
            "id": "bun-d-10", "rank": 10,
            "title": "Will today's Bayern Munich vs Dortmund clash feature Over 3.5 Total Goals?",
            "slug": "bayern-dortmund-over-35-goals-today",
            "volume": "$22,400,000", "volumeRaw": 22400000, "volumeLabel": "24H Volume",
            "liquidity": "$4,800,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.6% EV+", "impliedProb": 65, "fairValueProb": 75.5,
                "targetExit": "$0.80 (+23.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Der Klassiker fixtures have averaged 4.4 goals per match over the last 10 meetings, clearing Over 3.5 in 8 of the last 10 (80% empirical hit rate). Neither team is built to absorb pressure without trading chances.",
                "newsCatalyst": {
                    "headline": "Opta Franz: Der Klassiker is Europe's highest-scoring marquee rivalry of the past decade",
                    "source": "Opta Football Records", "time": "6h ago", "impact": "GOAL SPECTACLE"
                },
                "socialMediaRadar": {
                    "platform": "Bundesliga International / Football Daily",
                    "sentimentScore": 88, "sentimentTrend": "+23% Goal fest expectation",
                    "whaleFlows": "Goal accumulator funds heavily backing Over 3.5 goals.",
                    "retailPositioning": "Complete alignment across world football enthusiasts."
                },
                "riskMitigation": "Redeem once the 4th goal is scored."
            }
        }
    ],
    "week": [
        {
            "id": "bun-w-01", "rank": 1,
            "title": "Will Bayern Munich maintain a 5+ point lead at the top of the Bundesliga this week?",
            "slug": "bayern-munich-maintain-5-point-lead-this-week",
            "volume": "$41,500,000", "volumeRaw": 41500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$8,900,000", "endDate": "Sunday 8:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.73, "pct": 73}, {"name": "NO", "price": 0.27, "pct": 27}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.2% EV+", "impliedProb": 73, "fairValueProb": 83.5,
                "targetExit": "$0.87 (+19.1% gain)", "stopLoss": "$0.60",
                "macroStrategy": "Bayern holds a 5-point lead with a monstrous +26 goal difference. Direct pursuers Leipzig and Frankfurt play each other this week, ensuring dropped points among the chasing pack.",
                "newsCatalyst": {
                    "headline": "Kicker: Vincent Kompany's squad firing on all cylinders with highest xG differential in Europe (+1.82/90)",
                    "source": "Kicker Analysis", "time": "8h ago", "impact": "TITLE SPRINT"
                },
                "socialMediaRadar": {
                    "platform": "FCB Inside / Sky Sport DE",
                    "sentimentScore": 87, "sentimentTrend": "+21% Dominant lead certainty",
                    "whaleFlows": "Institutional sports funds backing Bayern table margin retention.",
                    "retailPositioning": "Strong retail backing supported by mathematical safety cushion."
                },
                "riskMitigation": "Lock 60% profit after Bayern's own victory is secured."
            }
        },
        {
            "id": "bun-w-02", "rank": 2,
            "title": "Will Bayer Leverkusen stay unbeaten across both fixtures this week?",
            "slug": "bayer-leverkusen-stay-unbeaten-both-fixtures-week",
            "volume": "$28,900,000", "volumeRaw": 28900000, "volumeLabel": "7-Day Volume",
            "liquidity": "$6,300,000", "endDate": "Sunday 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.77, "pct": 77}, {"name": "NO", "price": 0.23, "pct": 23}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 90, "evEdge": "+11.4% EV+", "impliedProb": 77, "fairValueProb": 87.5,
                "targetExit": "$0.92 (+19.5% gain)", "stopLoss": "$0.66",
                "macroStrategy": "Xabi Alonso's Leverkusen has lost only 1 domestic league match in their last 46 Bundesliga games. Their late-game stamina (scoring 28 goals after the 80th minute) virtually eliminates defeat.",
                "newsCatalyst": {
                    "headline": "Rheinische Post: Werkself mental resilience intact as Alonso rotates fresh legs for midweek tie",
                    "source": "Rheinische Post Sport", "time": "10h ago", "impact": "UNBEATEN DNA"
                },
                "socialMediaRadar": {
                    "platform": "Leverkusen UK / Bundesliga Buzz",
                    "sentimentScore": 90, "sentimentTrend": "+22% Unbeaten aura",
                    "whaleFlows": "Sports betting syndicates treating Leverkusen double-chance props as cash substitutes.",
                    "retailPositioning": "Universal fan awe at Leverkusen's late-game miracles."
                },
                "riskMitigation": "Hold into the final whistle of Sunday's match; redeem at $1.00."
            }
        },
        {
            "id": "bun-w-03", "rank": 3,
            "title": "Will Harry Kane score a Hat-Trick across this matchweek?",
            "slug": "harry-kane-score-hat-trick-this-matchweek",
            "volume": "$17,400,000", "volumeRaw": 17400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,800,000", "endDate": "Sunday 8:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.34, "pct": 34}, {"name": "NO", "price": 0.66, "pct": 66}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+14.6% EV+", "impliedProb": 66, "fairValueProb": 78.5,
                "targetExit": "$0.81 (+22.7% gain on NO)", "stopLoss": "$0.52",
                "macroStrategy": "While Kane is prolific, scoring 3+ goals across a single matchweek against top-half opposition occurs in fewer than 18% of historical samples. Pricing at 0.34 for YES is overly optimistic retail speculation.",
                "newsCatalyst": {
                    "headline": "Kicker Stats: Hat-tricks in Der Klassiker and top-six German clashes occur only once every 24 meetings",
                    "source": "Kicker Historical Records", "time": "12h ago", "impact": "HISTORICAL RARITY"
                },
                "socialMediaRadar": {
                    "platform": "Kane Fans / FPL Reddit",
                    "sentimentScore": 73, "sentimentTrend": "+18% Kane realism",
                    "whaleFlows": "Sharp sports traders laying the Hat-Trick prop, taking the NO side.",
                    "retailPositioning": "Recreational punters chasing viral hat-trick payout."
                },
                "riskMitigation": "Bet NO on Kane Hat-Trick; capture substantial 66% baseline edge."
            }
        },
        {
            "id": "bun-w-04", "rank": 4,
            "title": "Will Borussia Dortmund take all 6 points from their two matchweek games?",
            "slug": "borussia-dortmund-take-all-6-points-this-week",
            "volume": "$21,600,000", "volumeRaw": 21600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,700,000", "endDate": "Sunday 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.32, "pct": 32}, {"name": "NO", "price": 0.68, "pct": 68}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+13.9% EV+", "impliedProb": 68, "fairValueProb": 80.0,
                "targetExit": "$0.84 (+23.5% gain on NO)", "stopLoss": "$0.55",
                "macroStrategy": "Dortmund's first game of the week is an away clash at the Allianz Arena where they are heavy underdogs (+450 / 0.18 probability). Capturing 6 points requires winning in Munich, making NO the statistically superior position.",
                "newsCatalyst": {
                    "headline": "Ruhr Nachrichten: Dortmund have won in Munich only once in their last 10 Bundesliga visits",
                    "source": "Ruhr Nachrichten Der Klassiker Special", "time": "14h ago", "impact": "ALLIANZ CURSE"
                },
                "socialMediaRadar": {
                    "platform": "Yellow Wall / BVB Twitter",
                    "sentimentScore": 78, "sentimentTrend": "+20% NO certainty",
                    "whaleFlows": "Quant trading desks taking NO on Dortmund 6-point sweep.",
                    "retailPositioning": "Emotional Dortmund fans taking YES; smart money takes NO."
                },
                "riskMitigation": "Bet NO on 6/6 points; cash out immediately if Dortmund drops points in Match 1."
            }
        },
        {
            "id": "bun-w-05", "rank": 5,
            "title": "Will Omar Marmoush or Hugo Ekitike lead Frankfurt to 2 wins this week?",
            "slug": "marmoush-ekitike-frankfurt-2-wins-this-week",
            "volume": "$18,300,000", "volumeRaw": 18300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,000,000", "endDate": "Sunday 7:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.6% EV+", "impliedProb": 58, "fairValueProb": 68.0,
                "targetExit": "$0.73 (+25.8% gain)", "stopLoss": "$0.45",
                "macroStrategy": "Marmoush leads the Bundesliga in combined goals and assists (10G, 6A). Frankfurt's home dominance and favorable midweek opponent provide a 68% statistical probability of sweeping both fixtures.",
                "newsCatalyst": {
                    "headline": "Sky Sport DE: Marmoush receiving Premier League interest but committed to Frankfurt's top-4 charge",
                    "source": "Sky Sport Germany", "time": "16h ago", "impact": "SUPERSTAR FORM"
                },
                "socialMediaRadar": {
                    "platform": "SGE Twitter / Egyptian Football Desk",
                    "sentimentScore": 84, "sentimentTrend": "+19% Marmoush magic",
                    "whaleFlows": "European betting syndicates backing Frankfurt matchweek progression.",
                    "retailPositioning": "Growing appreciation for Frankfurt's scintillating duo."
                },
                "riskMitigation": "Lock 50% profits once Game 1 victory is secured."
            }
        },
        {
            "id": "bun-w-06", "rank": 6,
            "title": "Will RB Leipzig concede 1 or fewer goals throughout the matchweek?",
            "slug": "rb-leipzig-concede-1-or-fewer-goals-week",
            "volume": "$14,900,000", "volumeRaw": 14900000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,250,000", "endDate": "Sunday 8:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.64, "pct": 64}, {"name": "NO", "price": 0.36, "pct": 36}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.4% EV+", "impliedProb": 64, "fairValueProb": 74.5,
                "targetExit": "$0.79 (+23.4% gain)", "stopLoss": "$0.50",
                "macroStrategy": "Leipzig's defensive structure allows only 0.74 xGA per 90. In their last 7 matches, they have conceded 1 or fewer goals in 6 of them (85.7% empirical rate).",
                "newsCatalyst": {
                    "headline": "Mitteldeutsche Zeitung: Marco Rose's defensive pairing Lukeba and Orbán boast league's highest tackle success (76%)",
                    "source": "Mitteldeutsche Zeitung", "time": "18h ago", "impact": "DEFENSIVE ANCHOR"
                },
                "socialMediaRadar": {
                    "platform": "RBL Fans / Bundesliga Stat Leaders",
                    "sentimentScore": 82, "sentimentTrend": "+17% Tight defense consensus",
                    "whaleFlows": "Defensive prop specialists accumulating Leipzig low-goals conceded props.",
                    "retailPositioning": "Solid backing for Leipzig's defensive discipline."
                },
                "riskMitigation": "Redeem upon completion of Leipzig's weekend fixture."
            }
        },
        {
            "id": "bun-w-07", "rank": 7,
            "title": "Will VfB Stuttgart climb back into the Bundesliga Top 4 by Sunday evening?",
            "slug": "vfb-stuttgart-climb-top-4-this-week",
            "volume": "$12,400,000", "volumeRaw": 12400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,700,000", "endDate": "Sunday 9:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.44, "pct": 44}, {"name": "NO", "price": 0.56, "pct": 56}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+13.1% EV+", "impliedProb": 56, "fairValueProb": 66.0,
                "targetExit": "$0.71 (+26.8% gain on NO)", "stopLoss": "$0.44",
                "macroStrategy": "Stuttgart faces a grueling away trip to Frankfurt and has struggled with Champions League fatigue, dropping points in 4 of their last 6 league outings. Teams currently in 3rd and 4th have easier fixtures.",
                "newsCatalyst": {
                    "headline": "Stuttgarter Nachrichten: Sebastian Hoeneß manages heavy squad rotation amidst packed European schedule",
                    "source": "Stuttgarter Nachrichten", "time": "1d ago", "impact": "FATIGUE ATTRITION"
                },
                "socialMediaRadar": {
                    "platform": "VfB1893 Twitter / Brustring Talk",
                    "sentimentScore": 47, "sentimentTrend": "-13% Top 4 struggle realism",
                    "whaleFlows": "Sports quant syndicates taking NO on Stuttgart top-4 ascent this week.",
                    "retailPositioning": "Casual fans overestimating Stuttgart's ability to leapfrog multiple teams."
                },
                "riskMitigation": "Bet NO on Stuttgart reaching top 4; cash out if they fail to win in Frankfurt."
            }
        },
        {
            "id": "bun-w-08", "rank": 8,
            "title": "Will over 30 total goals be scored across all 9 Bundesliga matches this weekend?",
            "slug": "over-30-total-goals-bundesliga-weekend",
            "volume": "$16,500,000", "volumeRaw": 16500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,600,000", "endDate": "Sunday 9:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.4% EV+", "impliedProb": 69, "fairValueProb": 79.5,
                "targetExit": "$0.85 (+23.2% gain)", "stopLoss": "$0.55",
                "macroStrategy": "The Bundesliga is the highest-scoring league in world football, averaging 3.48 goals per match. Across 9 fixtures, the mathematical expectation is 31.32 goals, easily clearing the 30-goal hurdle.",
                "newsCatalyst": {
                    "headline": "Opta Franz: Bundesliga 2024/25 leads all European top-flight leagues in open-play goals per 90 minutes",
                    "source": "Opta European Records", "time": "1d ago", "impact": "GOAL DOMINANCE"
                },
                "socialMediaRadar": {
                    "platform": "Sportschau / Bundesliga Official",
                    "sentimentScore": 86, "sentimentTrend": "+20% High-scoring weekend",
                    "whaleFlows": "Multi-match goal accumulator funds taking Over 30 aggregate goals.",
                    "retailPositioning": "Broad retail enthusiasm for Bundesliga goal-fests."
                },
                "riskMitigation": "Cash out once the 31st goal is scored across the weekend."
            }
        },
        {
            "id": "bun-w-09", "rank": 9,
            "title": "Will Xabi Alonso announce contract commitment amidst European managerial interest this week?",
            "slug": "xabi-alonso-contract-commitment-announcement-week",
            "volume": "$13,800,000", "volumeRaw": 13800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,000,000", "endDate": "Friday 6:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.1% EV+", "impliedProb": 72, "fairValueProb": 82.5,
                "targetExit": "$0.87 (+20.8% gain)", "stopLoss": "$0.58",
                "macroStrategy": "Bayer Leverkusen CEO Fernando Carro confirmed that Alonso has reiterating complete focus on the current season with zero intention of discussing summer departures until May 2025.",
                "newsCatalyst": {
                    "headline": "Fabrizio Romano: Xabi Alonso confirms 100% focus on Leverkusen project; contract runs until 2026",
                    "source": "Fabrizio Romano European Football", "time": "1d ago", "impact": "PROJECT COMMITMENT"
                },
                "socialMediaRadar": {
                    "platform": "Werkself News / German Football Twitter",
                    "sentimentScore": 88, "sentimentTrend": "+22% Commitment confirmation",
                    "whaleFlows": "Managerial prop specialists accumulating Alonso commitment YES.",
                    "retailPositioning": "Widespread relief among Leverkusen supporters."
                },
                "riskMitigation": "Hold into the pre-match press conference."
            }
        },
        {
            "id": "bun-w-10", "rank": 10,
            "title": "Will Bundesliga average match attendance exceed 42,500 across this gameweek?",
            "slug": "bundesliga-average-attendance-exceed-42500-week",
            "volume": "$9,500,000", "volumeRaw": 9500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,100,000", "endDate": "Sunday 10:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.78, "pct": 78}, {"name": "NO", "price": 0.22, "pct": 22}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 91, "evEdge": "+11.4% EV+", "impliedProb": 78, "fairValueProb": 88.5,
                "targetExit": "$0.93 (+19.2% gain)", "stopLoss": "$0.68",
                "macroStrategy": "With Der Klassiker at the 75,000-seat Allianz Arena and home matches for Frankfurt (58,000) and Gladbach (54,000), total capacity utilization mathematically guarantees an average above 44,000.",
                "newsCatalyst": {
                    "headline": "DFL Official: 8 of 9 Bundesliga weekend fixtures declared complete sellouts",
                    "source": "DFL Deutsche Fußball Liga", "time": "1d ago", "impact": "SELLOUT CARD"
                },
                "socialMediaRadar": {
                    "platform": "FanKultur / Bundesliga Official",
                    "sentimentScore": 92, "sentimentTrend": "+24% Packed stadiums",
                    "whaleFlows": "Prop specialists locking mathematical stadium capacity models.",
                    "retailPositioning": "German football fan culture celebrated worldwide."
                },
                "riskMitigation": "Redeem upon completion of final Sunday fixture."
            }
        }
    ],
    "month": [
        {
            "id": "bun-m-01", "rank": 1,
            "title": "Will Bayern Munich win the Bundesliga Title 2024/25?",
            "slug": "bayern-munich-win-bundesliga-title-2025",
            "volume": "$78,900,000", "volumeRaw": 78900000, "volumeLabel": "30-Day Volume",
            "liquidity": "$17,200,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+12.2% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                "targetExit": "$0.89 (+20.2% gain)", "stopLoss": "$0.62",
                "macroStrategy": "Vincent Kompany has revitalized Bayern's dominance, posting a +26 goal difference in 10 matches. Leverkusen has already dropped points in 4 draws, giving Bayern a commanding mathematical and financial superiority.",
                "newsCatalyst": {
                    "headline": "Opta Supercomputer Projections: Bayern Munich title win probability jumps to 84.6% following undefeated start",
                    "source": "Opta Football Simulations", "time": "2d ago", "impact": "TITLE CORONATION"
                },
                "socialMediaRadar": {
                    "platform": "BILD Sport / Sky Sport DE",
                    "sentimentScore": 89, "sentimentTrend": "+22% Rekordmeister rebound",
                    "whaleFlows": "European sports hedge funds accumulating Bayern title contracts.",
                    "retailPositioning": "Consensus agreement across European football fraternity."
                },
                "riskMitigation": "Core portfolio anchor holding; hold into title clinch in April/May."
            }
        },
        {
            "id": "bun-m-02", "rank": 2,
            "title": "Will Harry Kane win the Torjägerkanone (Bundesliga Top Goalscorer)?",
            "slug": "harry-kane-win-torjagerkanone-top-scorer",
            "volume": "$63,500,000", "volumeRaw": 63500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$13,800,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.86, "pct": 86}, {"name": "NO", "price": 0.14, "pct": 14}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 94, "evEdge": "+8.4% EV+", "impliedProb": 86, "fairValueProb": 94.5,
                "targetExit": "$0.97 (+12.8% gain)", "stopLoss": "$0.76",
                "macroStrategy": "Kane currently leads the scoring charts with 11 goals in 10 appearances, backed by Europe's highest team xG. No other striker in Germany approaches his combination of penalty duties and 4.2 shots per game.",
                "newsCatalyst": {
                    "headline": "Kicker: Kane tracking for back-to-back 35+ goal campaigns as Kompany's tactical supply maximizes his touches",
                    "source": "Kicker Torjägerkanone Desk", "time": "3d ago", "impact": "SCORING REIGN"
                },
                "socialMediaRadar": {
                    "platform": "Kane Tracker / Bundesliga International",
                    "sentimentScore": 95, "sentimentTrend": "+25% Torjägerkanone lock",
                    "whaleFlows": "Arbitrage syndicates treating Kane Top Scorer as institutional yield instrument.",
                    "retailPositioning": "Complete alignment across world football."
                },
                "riskMitigation": "Ultra-low-risk capital preservation bet; redeem upon season conclusion."
            }
        },
        {
            "id": "bun-m-03", "rank": 3,
            "title": "Will Bayer Leverkusen successfully defend their Bundesliga Title?",
            "slug": "bayer-leverkusen-defend-bundesliga-title",
            "volume": "$48,700,000", "volumeRaw": 48700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$10,500,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.22, "pct": 22}, {"name": "NO", "price": 0.78, "pct": 78}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+12.1% EV+", "impliedProb": 78, "fairValueProb": 88.5,
                "targetExit": "$0.92 (+17.9% gain on NO)", "stopLoss": "$0.68",
                "macroStrategy": "Leverkusen already trails Bayern by 7 points and has conceded 15 goals in 10 matches (compared to only 24 all last season). Regressing defensive metrics mean defending the title requires Bayern to implode, which is statistically improbable.",
                "newsCatalyst": {
                    "headline": "Kicker Analysis: Leverkusen's defensive regression from open play prevents realistic title defense",
                    "source": "Kicker Tactical Review", "time": "3d ago", "impact": "TITLE FADE"
                },
                "socialMediaRadar": {
                    "platform": "Bundesliga Pod / Sky Sport DE",
                    "sentimentScore": 81, "sentimentTrend": "+22% Title handover consensus",
                    "whaleFlows": "Smart money taking NO on Leverkusen repeat at 0.78.",
                    "retailPositioning": "Nostalgic fans holding Leverkusen; smart money takes the math."
                },
                "riskMitigation": "Bet NO on Leverkusen defending title; high conviction statistical lock."
            }
        },
        {
            "id": "bun-m-04", "rank": 4,
            "title": "Will Eintracht Frankfurt finish in the Bundesliga Top 4 (Champions League)?",
            "slug": "eintracht-frankfurt-finish-top-4-champions-league",
            "volume": "$34,200,000", "volumeRaw": 34200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$7,400,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.54, "pct": 54}, {"name": "NO", "price": 0.46, "pct": 46}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+13.5% EV+", "impliedProb": 54, "fairValueProb": 64.5,
                "targetExit": "$0.71 (+31.5% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Frankfurt currently sits in 3rd place, possessing the 2nd highest goal tally in Germany (26). With Dortmund struggling on the road and Stuttgart fatigued by European games, Frankfurt is the strongest contender for the 3rd or 4th spot.",
                "newsCatalyst": {
                    "headline": "Hessenschau: Dino Toppmöller's squad tactical maturity and depth provide sustained top-4 cushion",
                    "source": "Hessenschau Sports", "time": "4d ago", "impact": "TOP 4 BUFFER"
                },
                "socialMediaRadar": {
                    "platform": "SGE4EVER / German Football Pod",
                    "sentimentScore": 81, "sentimentTrend": "+19% Champions League dream",
                    "whaleFlows": "German betting syndicates backing Frankfurt top-4 qualification.",
                    "retailPositioning": "Public slow to price Frankfurt's sustainable attacking dominance."
                },
                "riskMitigation": "Lock 50% profits once Frankfurt builds an 8-point gap over 5th place."
            }
        },
        {
            "id": "bun-m-05", "rank": 5,
            "title": "Will Borussia Dortmund finish in the Top 4 of the Bundesliga table?",
            "slug": "borussia-dortmund-finish-top-4-table",
            "volume": "$42,800,000", "volumeRaw": 42800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$9,200,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+11.9% EV+", "impliedProb": 63, "fairValueProb": 72.0,
                "targetExit": "$0.77 (+22.2% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Dortmund has qualified for the Champions League in 9 of the last 10 seasons. The Yellow Wall at Signal Iduna Park delivers an unmatched home win rate (83%), which alone provides enough points to edge out Stuttgart and Freiburg.",
                "newsCatalyst": {
                    "headline": "Ruhr Nachrichten: Serhou Guirassy and Julian Brandt step up leadership as BVB resets away tactical balance",
                    "source": "Ruhr Nachrichten", "time": "4d ago", "impact": "HOME ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "BVB Buzz / r/borussiadortmund",
                    "sentimentScore": 79, "sentimentTrend": "+17% Top 4 qualification faith",
                    "whaleFlows": "Institutional syndicates taking Dortmund top 4 on recent price dip.",
                    "retailPositioning": "Historic qualification reliability backs the position."
                },
                "riskMitigation": "Trim position if Dortmund drops points in two consecutive home games."
            }
        },
        {
            "id": "bun-m-06", "rank": 6,
            "title": "Will Vincent Kompany win Bundesliga Coach of the Month?",
            "slug": "vincent-kompany-win-coach-of-the-month",
            "volume": "$21,400,000", "volumeRaw": 21400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,600,000", "endDate": "End of Month Award Announcement",
            "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.2% EV+", "impliedProb": 68, "fairValueProb": 78.5,
                "targetExit": "$0.83 (+22.0% gain)", "stopLoss": "$0.54",
                "macroStrategy": "Bayern's dominant monthly record (4 wins from 4 matches with +15 goal difference) puts Kompany well ahead of competitors. German media praise for his tactical revolution cements the award.",
                "newsCatalyst": {
                    "headline": "DFL Awards Committee: Kompany leads all statistical coach indices for the current voting window",
                    "source": "DFL Official Media", "time": "5d ago", "impact": "AWARD FAVORITE"
                },
                "socialMediaRadar": {
                    "platform": "BILD / Sky Sport DE Awards",
                    "sentimentScore": 88, "sentimentTrend": "+23% Kompany coronation",
                    "whaleFlows": "Prop specialists accumulating Kompany award YES.",
                    "retailPositioning": "Widespread recognition of Bayern's aesthetic turnaround."
                },
                "riskMitigation": "Hold into the official award ceremony announcement."
            }
        },
        {
            "id": "bun-m-07", "rank": 7,
            "title": "Will Florian Wirtz record 5 or more goal involvements (G/A) in this calendar month?",
            "slug": "florian-wirtz-record-5-plus-goal-involvements-month",
            "volume": "$25,100,000", "volumeRaw": 25100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,400,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.7% EV+", "impliedProb": 61, "fairValueProb": 71.5,
                "targetExit": "$0.76 (+24.6% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Wirtz averages 1.15 direct goal involvements per 90 across all competitions. With 5 fixtures scheduled this month against open, high-pressing opponents, achieving 5 involvements holds a 72% simulation hit rate.",
                "newsCatalyst": {
                    "headline": "Kicker: Wirtz registered 18 shot-creating actions in his last two competitive appearances",
                    "source": "Kicker Performance Index", "time": "5d ago", "impact": "ELITE PLAYMAKING"
                },
                "socialMediaRadar": {
                    "platform": "Werkself Fans / German Football X",
                    "sentimentScore": 86, "sentimentTrend": "+20% Wirtz masterclass",
                    "whaleFlows": "Player prop specialists taking the Over on Wirtz monthly total.",
                    "retailPositioning": "Widespread admiration for Wirtz's creative output."
                },
                "riskMitigation": "Cash out immediately once the 5th involvement is registered."
            }
        },
        {
            "id": "bun-m-08", "rank": 8,
            "title": "Will Bayer Leverkusen extend their domestic unbeaten streak to 8 or more matches this month?",
            "slug": "leverkusen-extend-unbeaten-streak-8-matches-month",
            "volume": "$29,400,000", "volumeRaw": 29400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$6,400,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.2% EV+", "impliedProb": 69, "fairValueProb": 79.5,
                "targetExit": "$0.84 (+21.7% gain)", "stopLoss": "$0.55",
                "macroStrategy": "Leverkusen has only 3 remaining domestic fixtures this month, all against lower-half opposition (Heidenheim, Union Berlin, St. Pauli). Their streak currently sits at 6 games.",
                "newsCatalyst": {
                    "headline": "Rheinische Post: Alonso's tactical adaptability prevents domestic defeats as defense stabilizes",
                    "source": "Rheinische Post", "time": "6d ago", "impact": "STREAK PRESERVATION"
                },
                "socialMediaRadar": {
                    "platform": "Leverkusen International / Sky Sport DE",
                    "sentimentScore": 87, "sentimentTrend": "+21% Unbeaten streak faith",
                    "whaleFlows": "Sports funds backing Leverkusen streak retention.",
                    "retailPositioning": "Solid backing for the reigning champions."
                },
                "riskMitigation": "Hold into the final whistle of the month; redeem at $1.00."
            }
        },
        {
            "id": "bun-m-09", "rank": 9,
            "title": "Will FC St. Pauli remain out of the automatic relegation positions this month?",
            "slug": "st-pauli-remain-out-relegation-spots-month",
            "volume": "$15,600,000", "volumeRaw": 15600000, "volumeLabel": "30-Day Volume",
            "liquidity": "$3,400,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+12.6% EV+", "impliedProb": 58, "fairValueProb": 67.5,
                "targetExit": "$0.73 (+25.8% gain)", "stopLoss": "$0.45",
                "macroStrategy": "St. Pauli's compact defensive structure has conceded only 11 goals, ranking 4th best in the entire Bundesliga. A 4-point buffer over VfL Bochum and Holstein Kiel ensures survival outside the bottom 2.",
                "newsCatalyst": {
                    "headline": "Hamburger Morgenpost: Alexander Blessin's defensive organization earns rave reviews across Germany",
                    "source": "Hamburger Morgenpost", "time": "6d ago", "impact": "DEFENSIVE RESILIENCE"
                },
                "socialMediaRadar": {
                    "platform": "Millernton / St Pauli Fans X",
                    "sentimentScore": 80, "sentimentTrend": "+17% Safety margin confidence",
                    "whaleFlows": "Relegation quants backing St. Pauli defensive metrics.",
                    "retailPositioning": "Cult fan favorite backed by robust defensive numbers."
                },
                "riskMitigation": "Cash out once St. Pauli wins their home relegation six-pointer."
            }
        },
        {
            "id": "bun-m-10", "rank": 10,
            "title": "Will Bayern Munich goal difference surpass +45 before the end of this calendar month?",
            "slug": "bayern-munich-goal-difference-surpass-45-month",
            "volume": "$21,800,000", "volumeRaw": 21800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,750,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+13.1% EV+", "impliedProb": 52, "fairValueProb": 62.0,
                "targetExit": "$0.69 (+32.7% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Bayern's goal difference currently stands at +33 with 4 matches remaining against weak defensive outfits. Kompany's relentless attacking tempo rarely eases up even with big leads.",
                "newsCatalyst": {
                    "headline": "BILD: Bayern averaging +3.2 goal differential per 90 in domestic matches this season",
                    "source": "BILD Bayern Analytics", "time": "7d ago", "impact": "GOAL DIFFERENCE SURGE"
                },
                "socialMediaRadar": {
                    "platform": "FCB Inside / Bundesliga Stat Lab",
                    "sentimentScore": 83, "sentimentTrend": "+18% Relentless goal machine",
                    "whaleFlows": "Statistical prop syndicates taking YES on Bayern milestone.",
                    "retailPositioning": "Recognized goalscoring power across the continent."
                },
                "riskMitigation": "Redeem once the +46th goal differential threshold is reached."
            }
        }
    ]
}
