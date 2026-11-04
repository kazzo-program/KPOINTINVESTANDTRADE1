# -*- coding: utf-8 -*-
"""
Football - Premier League Polymarket Top 10 Markets (Day, Week, Month)
Covering top UK football fixtures, team props, player markets, and league standings.
With full Macro Hedge Fund Strategy, News Catalysts, and Social Media Radar.
"""

PREMIER_LEAGUE_DATA = {
    "day": [
        {
            "id": "epl-d-01", "rank": 1,
            "title": "Will Manchester City defeat Arsenal at the Etihad Stadium today?",
            "slug": "manchester-city-defeat-arsenal-etihad-today",
            "volume": "$32,800,000", "volumeRaw": 32800000, "volumeLabel": "24H Volume",
            "liquidity": "$7,100,000", "endDate": "Today 6:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.54, "pct": 54}, {"name": "NO", "price": 0.46, "pct": 46}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.5% EV+", "impliedProb": 54, "fairValueProb": 64.5,
                "targetExit": "$0.71 (+31.5% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Pep Guardiola's tactical restructuring with Rodri / Kovačić double pivot generates 64% field tilt at home. Arsenal's defensive deep block without Martin Ødegaard at 100% loses 32% of its central counter-pressing turnover rate.",
                "newsCatalyst": {
                    "headline": "Sky Sports: Kevin De Bruyne and Erling Haaland declared 100% fit after final tactical walkthrough",
                    "source": "Sky Sports Premier League", "time": "1h 15m ago", "impact": "SQUAD ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "X / Football Twitter & Statman Dave",
                    "sentimentScore": 79, "sentimentTrend": "+18% City Etihad aura",
                    "whaleFlows": "Polymarket UK football whales entered $340,000 in YES contracts at 0.52-0.54.",
                    "retailPositioning": "Retail split down the middle due to Arsenal hype, underpricing City's home dominance."
                },
                "riskMitigation": "Lock 50% profits if City score first; hedge with draw if 1-0 past 80 mins."
            }
        },
        {
            "id": "epl-d-02", "rank": 2,
            "title": "Will Liverpool vs Chelsea produce Over 2.5 Total Goals today?",
            "slug": "liverpool-chelsea-over-25-goals-today",
            "volume": "$24,100,000", "volumeRaw": 24100000, "volumeLabel": "24H Volume",
            "liquidity": "$5,200,000", "endDate": "Today 4:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.2% EV+", "impliedProb": 68, "fairValueProb": 78.5,
                "targetExit": "$0.83 (+22.0% gain)", "stopLoss": "$0.54",
                "macroStrategy": "Enzo Maresca's inverted fullback system leaves enormous wide transition channels that Salah and Luis Díaz exploit ruthlessly. Combined xG in both teams' last 5 matches averages 3.42 goals per 90.",
                "newsCatalyst": {
                    "headline": "The Athletic: Arne Slot deploys hyper-direct wing transition targeting Chelsea's high defensive line",
                    "source": "The Athletic Tactical Analysis", "time": "2h ago", "impact": "TACTICAL OPENNESS"
                },
                "socialMediaRadar": {
                    "platform": "r/LiverpoolFC & Chelsea X Community",
                    "sentimentScore": 84, "sentimentTrend": "+21% High-scoring expectation",
                    "whaleFlows": "Vegas & Asian handicap syndicates pounded Over 2.75 Asian Goal line.",
                    "retailPositioning": "Heavy retail backing on goals; supported by underlying xG metrics."
                },
                "riskMitigation": "Execute on Over 2.5 Goals YES; exit once 3rd goal hits the net."
            }
        },
        {
            "id": "epl-d-03", "rank": 3,
            "title": "Will Erling Haaland score an anytime goal in today's fixture?",
            "slug": "erling-haaland-score-anytime-goal-today",
            "volume": "$21,500,000", "volumeRaw": 21500000, "volumeLabel": "24H Volume",
            "liquidity": "$4,650,000", "endDate": "Today 6:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+13.1% EV+", "impliedProb": 63, "fairValueProb": 73.5,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Haaland averages 1.18 goals per 90 at the Etihad with an individual xG of 0.94. Manchester City's box entries from cutbacks (Doku/Grealish) specifically isolate Haaland against the weakside center-back.",
                "newsCatalyst": {
                    "headline": "Opta Analyst: Haaland has converted 34% of big chances in home fixtures this campaign",
                    "source": "Opta Premier League Feed", "time": "1h 45m ago", "impact": "GOAL CONVERSION"
                },
                "socialMediaRadar": {
                    "platform": "FPL Twitter / Fantasy Premier League Watch",
                    "sentimentScore": 86, "sentimentTrend": "+20% Captaincy favorite",
                    "whaleFlows": "High-volume football prop traders accumulating Haaland anytime goal YES.",
                    "retailPositioning": "Massive FPL community consensus backing the Norwegian goal machine."
                },
                "riskMitigation": "Cash out immediately upon Haaland goal (first half or second half)."
            }
        },
        {
            "id": "epl-d-04", "rank": 4,
            "title": "Will Tottenham vs Newcastle see Both Teams To Score (BTTS) today?",
            "slug": "tottenham-newcastle-both-teams-to-score-today",
            "volume": "$16,900,000", "volumeRaw": 16900000, "volumeLabel": "24H Volume",
            "liquidity": "$3,700,000", "endDate": "Today 2:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.4% EV+", "impliedProb": 76, "fairValueProb": 86.5,
                "targetExit": "$0.91 (+19.7% gain)", "stopLoss": "$0.62",
                "macroStrategy": "Ange Postecoglou's high defensive line and relentless pressing yield an average of 1.74 goals against per game, while creating 2.18 xG. Newcastle with Isak and Gordon on transition have scored in 9 of their last 10 away matches.",
                "newsCatalyst": {
                    "headline": "BBC Sport: Both Spurs and Newcastle deploy ultra-attacking front threes with zero central holding re-enforcements",
                    "source": "BBC Sport Matchday Live", "time": "2h 15m ago", "impact": "END-TO-END TEMPO"
                },
                "socialMediaRadar": {
                    "platform": "Spurs Official / Newcastle Toon Army X",
                    "sentimentScore": 88, "sentimentTrend": "+23% BTTS lock consensus",
                    "whaleFlows": "Betting syndicates parlaying BTTS across major European exchanges.",
                    "retailPositioning": "Complete alignment between public and sharp money."
                },
                "riskMitigation": "Redeem early profit as soon as both teams score (often by 60th minute)."
            }
        },
        {
            "id": "epl-d-05", "rank": 5,
            "title": "Will Mohamed Salah register 1 or more assists for Liverpool today?",
            "slug": "mohamed-salah-register-assist-today",
            "volume": "$12,400,000", "volumeRaw": 12400000, "volumeLabel": "24H Volume",
            "liquidity": "$2,600,000", "endDate": "Today 4:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.42, "pct": 42}, {"name": "NO", "price": 0.58, "pct": 58}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 79, "evEdge": "+13.2% EV+", "impliedProb": 42, "fairValueProb": 51.5,
                "targetExit": "$0.60 (+42.8% gain)", "stopLoss": "$0.30",
                "macroStrategy": "Salah has transitioned into Liverpool's primary playmaker under Arne Slot, leading the Premier League in big chances created (14) and expected assists (xA 0.48/90). Market pricing at 0.42 offers tremendous EV value.",
                "newsCatalyst": {
                    "headline": "Anfield Watch: Salah creating 3.2 open-play shooting opportunities per game for Darwin Núñez and Díaz",
                    "source": "Anfield Watch Intelligence", "time": "3h ago", "impact": "PLAYMAKING HUB"
                },
                "socialMediaRadar": {
                    "platform": "FPL Community / Liverpool Echo",
                    "sentimentScore": 76, "sentimentTrend": "+16% Salah creative surge",
                    "whaleFlows": "Sharp prop bettors taking the mispriced 0.42 line on Salah assist.",
                    "retailPositioning": "Public focuses only on goals, underappreciating assist volume."
                },
                "riskMitigation": "High-reward asymmetric value trade; size at 3.5% allocation."
            }
        },
        {
            "id": "epl-d-06", "rank": 6,
            "title": "Will Aston Villa keep a clean sheet against Fulham today?",
            "slug": "aston-villa-keep-clean-sheet-today",
            "volume": "$11,200,000", "volumeRaw": 11200000, "volumeLabel": "24H Volume",
            "liquidity": "$2,400,000", "endDate": "Today 3:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.47, "pct": 47}, {"name": "NO", "price": 0.53, "pct": 53}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+14.0% EV+", "impliedProb": 53, "fairValueProb": 64.5,
                "targetExit": "$0.70 (+32.0% gain on NO)", "stopLoss": "$0.40",
                "macroStrategy": "Emiliano Martínez and Villa's offside trap have been breached in 7 of their last 8 home fixtures due to European fixture congestion. Fulham's Raúl Jiménez and Alex Iwobi generate 1.35 xG per away game.",
                "newsCatalyst": {
                    "headline": "Birmingham Mail: Unai Emery rotates central defensive partnership following Champions League midweek trip",
                    "source": "Birmingham Mail Sports", "time": "3h 30m ago", "impact": "DEFENSIVE FATIGUE"
                },
                "socialMediaRadar": {
                    "platform": "Villa Talk / Fulhamish Podcast",
                    "sentimentScore": 73, "sentimentTrend": "+18% Fulham goal threat",
                    "whaleFlows": "Sharp European punters backing Fulham team goal over 0.5.",
                    "retailPositioning": "Casual fans backing Villa clean sheet based on top-4 league position."
                },
                "riskMitigation": "Bet NO on Villa clean sheet (cash out when Fulham scores a single goal)."
            }
        },
        {
            "id": "epl-d-07", "rank": 7,
            "title": "Will Manchester United win away against Everton at Goodison Park today?",
            "slug": "manchester-united-win-everton-goodison-today",
            "volume": "$15,700,000", "volumeRaw": 15700000, "volumeLabel": "24H Volume",
            "liquidity": "$3,300,000", "endDate": "Today 1:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.49, "pct": 49}, {"name": "NO", "price": 0.51, "pct": 51}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+13.4% EV+", "impliedProb": 51, "fairValueProb": 62.0,
                "targetExit": "$0.68 (+33.3% gain on NO)", "stopLoss": "$0.40",
                "macroStrategy": "Goodison Park atmosphere under Sean Dyche produces maximum physical direct-aerial pressure (Everton ranks #1 in aerial duel win rate at 58.2%). United's transitional midfield defense concedes 15.4 shots per away game.",
                "newsCatalyst": {
                    "headline": "Manchester Evening News: United midfield depleted with key defensive pivots out with muscular strains",
                    "source": "MEN Sport Desk", "time": "4h ago", "impact": "MIDFIELD HOLE"
                },
                "socialMediaRadar": {
                    "platform": "The United Stand / Everton Aren't We",
                    "sentimentScore": 45, "sentimentTrend": "-16% United away fragility",
                    "whaleFlows": "Professional UK bookmakers laying United straight win, favoring Everton +0.5 handicap.",
                    "retailPositioning": "Global United fanbase over-betting brand reputation."
                },
                "riskMitigation": "Bet NO on United win (collect on Everton win or draw)."
            }
        },
        {
            "id": "epl-d-08", "rank": 8,
            "title": "Will Bukayo Saka have Over 1.5 Shots on Target today?",
            "slug": "bukayo-saka-over-15-shots-on-target-today",
            "volume": "$9,300,000", "volumeRaw": 9300000, "volumeLabel": "24H Volume",
            "liquidity": "$2,000,000", "endDate": "Today 6:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.1% EV+", "impliedProb": 58, "fairValueProb": 67.5,
                "targetExit": "$0.72 (+24.1% gain)", "stopLoss": "$0.45",
                "macroStrategy": "Saka is Arsenal's designated penalty taker and primary inside-cut shooter, averaging 2.6 shots per 90 with 1.6 on target in big away games. City's left-back area offers space for cutting onto his left foot.",
                "newsCatalyst": {
                    "headline": "Arsenal Matchday Preview: Saka cleared of minor knock, starts on right wing with full tactical freedom",
                    "source": "Arsenal Media Hub", "time": "2h 45m ago", "impact": "STARTER CONFIRMED"
                },
                "socialMediaRadar": {
                    "platform": "Gunners Reddit / Prop Bet Hub",
                    "sentimentScore": 81, "sentimentTrend": "+17% Saka talisman reliance",
                    "whaleFlows": "Player prop specialists taking the Over on Saka shots on target.",
                    "retailPositioning": "Solid backing from Arsenal fans and prop bettors."
                },
                "riskMitigation": "Lock profit once 2nd shot on target registers on Opta official feed."
            }
        },
        {
            "id": "epl-d-09", "rank": 9,
            "title": "Will Cole Palmer record an anytime Goal or Assist (G/A) today?",
            "slug": "cole-palmer-anytime-goal-or-assist-today",
            "volume": "$13,800,000", "volumeRaw": 13800000, "volumeLabel": "24H Volume",
            "liquidity": "$2,950,000", "endDate": "Today 4:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.9% EV+", "impliedProb": 61, "fairValueProb": 71.5,
                "targetExit": "$0.76 (+24.5% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Palmer possesses a monstrous 62% direct involvement rate in all Chelsea goals scored this calendar year. He takes direct free kicks, penalties, and corners, maximizing set-piece and open-play EV.",
                "newsCatalyst": {
                    "headline": "Telegraph Football: Cole Palmer leads Premier League in goal involvements per 90 (1.24) since start of 2024",
                    "source": "Telegraph Sports Desk", "time": "3h ago", "impact": "CHELSEA TALISMAN"
                },
                "socialMediaRadar": {
                    "platform": "Chelsea X / FPL Focal",
                    "sentimentScore": 87, "sentimentTrend": "+22% Cold Palmer momentum",
                    "whaleFlows": "Smart money taking Palmer G/A prop as primary Chelsea angle.",
                    "retailPositioning": "Universal fan admiration; cold-blooded finishing profile."
                },
                "riskMitigation": "Cash out immediately upon Chelsea goal scored or assisted by Palmer."
            }
        },
        {
            "id": "epl-d-10", "rank": 10,
            "title": "Will today's Premier League fixtures average Over 3.2 Goals per match?",
            "slug": "today-premier-league-average-over-32-goals",
            "volume": "$10,600,000", "volumeRaw": 10600000, "volumeLabel": "24H Volume",
            "liquidity": "$2,200,000", "endDate": "Today 8:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 78, "evEdge": "+11.5% EV+", "impliedProb": 52, "fairValueProb": 60.5,
                "targetExit": "$0.67 (+28.8% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Longer stoppage times under PGMOL guidance (averaging +9.8 minutes per game) alongside inverted wing tactics have elevated 2024 Premier League goals per game to 3.28 across all fixtures.",
                "newsCatalyst": {
                    "headline": "Opta Analyst Season Review: Premier League tracking at highest goals-per-game average since 1964/65",
                    "source": "Opta Football Records", "time": "5h ago", "impact": "HISTORIC GOAL RATE"
                },
                "socialMediaRadar": {
                    "platform": "Match of the Day Twitter / Football Daily",
                    "sentimentScore": 79, "sentimentTrend": "+16% Goals galore trend",
                    "whaleFlows": "Multi-match goal accumulator syndicates driving Polymarket liquidity.",
                    "retailPositioning": "Recreational viewers always prefer backing goals."
                },
                "riskMitigation": "Track aggregate goals across early kickoffs; hedge in afternoon matches."
            }
        }
    ],
    "week": [
        {
            "id": "epl-w-01", "rank": 1,
            "title": "Will Liverpool remain top of the Premier League table after this weekend's matchweek?",
            "slug": "liverpool-remain-top-table-this-weekend",
            "volume": "$48,200,000", "volumeRaw": 48200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$10,400,000", "endDate": "Sunday 7:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.8% EV+", "impliedProb": 72, "fairValueProb": 83.5,
                "targetExit": "$0.87 (+20.8% gain)", "stopLoss": "$0.60",
                "macroStrategy": "Arne Slot's Liverpool holds a 2-point cushion with a superior goal difference (+15). With title rival Man City facing Arsenal, at least one direct challenger is guaranteed to drop points this matchweek.",
                "newsCatalyst": {
                    "headline": "Liverpool Echo: Reds enter weekend with zero fresh injury concerns; Virgil van Dijk marshals league's best defense",
                    "source": "Liverpool Echo Sports", "time": "6h ago", "impact": "POINTS CUSHION"
                },
                "socialMediaRadar": {
                    "platform": "Sky Sports Debate / The Redmen TV",
                    "sentimentScore": 86, "sentimentTrend": "+20% Top of table momentum",
                    "whaleFlows": "Institutional sports funds backing Liverpool matchweek table retention.",
                    "retailPositioning": "High confidence across the footballing public."
                },
                "riskMitigation": "Lock 60% profit once Liverpool secures victory in their own tie."
            }
        },
        {
            "id": "epl-w-02", "rank": 2,
            "title": "Will Arsenal take maximum 6/6 points from their two Premier League matches this week?",
            "slug": "arsenal-take-6-points-two-matches-this-week",
            "volume": "$34,500,000", "volumeRaw": 34500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$7,300,000", "endDate": "Sunday 8:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.39, "pct": 39}, {"name": "NO", "price": 0.61, "pct": 61}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.2% EV+", "impliedProb": 61, "fairValueProb": 73.0,
                "targetExit": "$0.76 (+24.6% gain on NO)", "stopLoss": "$0.48",
                "macroStrategy": "Arsenal's schedule includes an away fixture at the Etihad followed by a midweek derby. Winning back-to-back matches against top-half opposition in a 4-day span holds an empirical probability under 30%.",
                "newsCatalyst": {
                    "headline": "Guardian Sport: Mikel Arteta warns squad rotation will be vital to navigate grueling 7-day schedule",
                    "source": "Guardian Football Desk", "time": "8h ago", "impact": "SCHEDULE ATTRITION"
                },
                "socialMediaRadar": {
                    "platform": "AFTV / Gooner Twitter",
                    "sentimentScore": 44, "sentimentTrend": "-15% Tough fixture realism",
                    "whaleFlows": "Quant trading desks taking NO on Arsenal 6-point sweep.",
                    "retailPositioning": "Optimistic Arsenal retail fans taking YES; smart money takes NO."
                },
                "riskMitigation": "Bet NO on 6/6 points; cash out immediately if Arsenal draws or loses either game."
            }
        },
        {
            "id": "epl-w-03", "rank": 3,
            "title": "Will Chelsea climb into the Premier League Top 4 by Sunday evening?",
            "slug": "chelsea-climb-top-4-sunday-evening",
            "volume": "$27,300,000", "volumeRaw": 27300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$5,800,000", "endDate": "Sunday 9:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+12.5% EV+", "impliedProb": 58, "fairValueProb": 68.0,
                "targetExit": "$0.73 (+25.8% gain)", "stopLoss": "$0.44",
                "macroStrategy": "Chelsea currently sits in 5th place, trailing 4th by only 1 point with superior goal difference. Villa and Newcastle face daunting fixtures, giving Maresca's squad the statistical edge to leapfrog into 4th.",
                "newsCatalyst": {
                    "headline": "Telegraph Sport: Chelsea's depth paying dividends as second-unit players impress in cup rotations",
                    "source": "Telegraph Chelsea Beat", "time": "10h ago", "impact": "DEPTH EDGE"
                },
                "socialMediaRadar": {
                    "platform": "London Is Blue Podcast / Chelsea X",
                    "sentimentScore": 81, "sentimentTrend": "+18% Top 4 push",
                    "whaleFlows": "London betting syndicates buying Chelsea top-4 matchweek props.",
                    "retailPositioning": "Growing public belief in Maresca's project."
                },
                "riskMitigation": "Lock partial profits when Chelsea wins their fixture."
            }
        },
        {
            "id": "epl-w-04", "rank": 4,
            "title": "Will Alexander Isak score 2 or more goals across this matchweek?",
            "slug": "alexander-isak-score-2-plus-goals-this-week",
            "volume": "$18,900,000", "volumeRaw": 18900000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,100,000", "endDate": "Monday 10:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.46, "pct": 46}, {"name": "NO", "price": 0.54, "pct": 54}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.8% EV+", "impliedProb": 46, "fairValueProb": 55.0,
                "targetExit": "$0.65 (+41.3% gain)", "stopLoss": "$0.32",
                "macroStrategy": "Newcastle plays twice this week against bottom-half defensive units. Isak's non-penalty xG/90 is 0.72, and he assumes primary spot-kick duties for Eddie Howe's high-tempo side.",
                "newsCatalyst": {
                    "headline": "Chronicle Live: Eddie Howe confirms Isak will start both matches as Newcastle pushes for European spots",
                    "source": "Newcastle Chronicle", "time": "12h ago", "impact": "HIGH USAGE"
                },
                "socialMediaRadar": {
                    "platform": "Toon Army Twitter / FPL Scouts",
                    "sentimentScore": 77, "sentimentTrend": "+17% Isak brace anticipation",
                    "whaleFlows": "Sharp FPL / football prop syndicates taking 0.46 underdog pricing.",
                    "retailPositioning": "Retail hesitant on multiple-goal props, creating an attractive price buffer."
                },
                "riskMitigation": "Cash out if Isak nets in Game 1 and enters Game 2 on 1 goal."
            }
        },
        {
            "id": "epl-w-05", "rank": 5,
            "title": "Will Nottingham Forest remain in European qualification spots (top 7) after this matchweek?",
            "slug": "nottingham-forest-remain-top-7-this-matchweek",
            "volume": "$15,200,000", "volumeRaw": 15200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,300,000", "endDate": "Sunday 8:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.4% EV+", "impliedProb": 67, "fairValueProb": 77.5,
                "targetExit": "$0.82 (+22.4% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Nuno Espírito Santo's compact 4-2-3-1 has conceded only 10 goals all season (second fewest behind Liverpool). A 3-point buffer over 8th place guarantees safety with a single point this weekend.",
                "newsCatalyst": {
                    "headline": "Opta Analyst: Forest's defensive block registers the lowest expected goals conceded from open play in Europe",
                    "source": "Opta Matchweek Preview", "time": "14h ago", "impact": "DEFENSIVE ANCHOR"
                },
                "socialMediaRadar": {
                    "platform": "Nottingham Post / r/nffc",
                    "sentimentScore": 84, "sentimentTrend": "+19% European dream momentum",
                    "whaleFlows": "European football syndicates backing Forest matchweek position.",
                    "retailPositioning": "Public recognizing Nuno's tactical masterclass."
                },
                "riskMitigation": "Steady statistical bet; hold through the weekend."
            }
        },
        {
            "id": "epl-w-06", "rank": 6,
            "title": "Will any Premier League manager be sacked before next Monday morning?",
            "slug": "premier-league-manager-sacked-before-monday",
            "volume": "$21,100,000", "volumeRaw": 21100000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,500,000", "endDate": "Monday 8:00 AM GMT",
            "outcomes": [{"name": "YES", "price": 0.31, "pct": 31}, {"name": "NO", "price": 0.69, "pct": 69}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+14.6% EV+", "impliedProb": 69, "fairValueProb": 82.5,
                "targetExit": "$0.84 (+21.7% gain on NO)", "stopLoss": "$0.55",
                "macroStrategy": "Boardroom sources across bottom-six clubs (Wolves, Southampton, Palace) indicate boards have confirmed backing for managers through the upcoming international break rather than hasty mid-week dismissals.",
                "newsCatalyst": {
                    "headline": "Fabrizio Romano: Southampton and Wolves boards currently not negotiating with any replacement managerial candidates",
                    "source": "Fabrizio Romano Transfer & Manager Feed", "time": "16h ago", "impact": "BOARD STABILITY"
                },
                "socialMediaRadar": {
                    "platform": "Sack Race Odds / TalkSPORT Live",
                    "sentimentScore": 77, "sentimentTrend": "+20% No sack certainty",
                    "whaleFlows": "Smart money accumulating NO contracts on sensationalist sack rumors.",
                    "retailPositioning": "Retail chasing 31% underdog payoff on tabloid rumors."
                },
                "riskMitigation": "Bet NO on sack; capture high probability premium."
            }
        },
        {
            "id": "epl-w-07", "rank": 7,
            "title": "Will VAR overturn 4 or more on-field referee decisions across all 10 weekend fixtures?",
            "slug": "var-overturn-4-plus-decisions-this-weekend",
            "volume": "$11,800,000", "volumeRaw": 11800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,500,000", "endDate": "Sunday 9:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.64, "pct": 64}, {"name": "NO", "price": 0.36, "pct": 36}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.7% EV+", "impliedProb": 64, "fairValueProb": 75.0,
                "targetExit": "$0.79 (+23.4% gain)", "stopLoss": "$0.50",
                "macroStrategy": "PGMOL's independent key match incident panel recorded 0.44 overturns per match in 2024, mathematically projecting 4.4 overturns across a 10-match gameweek.",
                "newsCatalyst": {
                    "headline": "PGMOL Review: Semi-automated offside review and pitchside monitor protocols tracking at 98% factual compliance",
                    "source": "Premier League Official Officials Desk", "time": "1d ago", "impact": "INTERVENTION FREQUENCY"
                },
                "socialMediaRadar": {
                    "platform": "Dale Johnson / ESPN VAR Review",
                    "sentimentScore": 82, "sentimentTrend": "+17% VAR controversy consensus",
                    "whaleFlows": "Statistical prop funds taking Over on VAR intervention counts.",
                    "retailPositioning": "Widespread fan expectation of VAR drama."
                },
                "riskMitigation": "Cash out once the 4th decision is overturned."
            }
        },
        {
            "id": "epl-w-08", "rank": 8,
            "title": "Will Brighton win by 2 or more goals against bottom-six opposition this week?",
            "slug": "brighton-win-by-2-plus-goals-this-week",
            "volume": "$13,400,000", "volumeRaw": 13400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,900,000", "endDate": "Saturday 5:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.53, "pct": 53}, {"name": "NO", "price": 0.47, "pct": 47}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.6% EV+", "impliedProb": 53, "fairValueProb": 62.5,
                "targetExit": "$0.69 (+30.1% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Fabian Hürzeler's Brighton side generates the 4th highest expected goal difference (+0.61/90) in the league. Mitoma, Welbeck, and Rutter create constant overload mismatches against low-block defenses.",
                "newsCatalyst": {
                    "headline": "The Argus: Brighton welcoming back Joao Pedro to starting lineup after full training week",
                    "source": "Brighton Argus Sports", "time": "1d ago", "impact": "ATTACKING BOOST"
                },
                "socialMediaRadar": {
                    "platform": "Seagulls Central / FPL Twitter",
                    "sentimentScore": 78, "sentimentTrend": "+16% Brighton attacking swagger",
                    "whaleFlows": "Asian handicap syndicates backing Brighton -1.5 goal spread.",
                    "retailPositioning": "Retail warming to Brighton's attractive style."
                },
                "riskMitigation": "Lock profit if Brighton leads 2-0 before 70th minute."
            }
        },
        {
            "id": "epl-w-09", "rank": 9,
            "title": "Will Tottenham Hotspur record the highest possession percentage (>65%) in this gameweek?",
            "slug": "tottenham-highest-possession-gameweek",
            "volume": "$10,200,000", "volumeRaw": 10200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,200,000", "endDate": "Sunday 8:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.1% EV+", "impliedProb": 61, "fairValueProb": 71.0,
                "targetExit": "$0.76 (+24.5% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Spurs lead the Premier League in average possession (67.4%) and field tilt. Their weekend opponent ranks bottom-3 in passing sequence duration, ensuring Tottenham controls 68-72% of match ball possession.",
                "newsCatalyst": {
                    "headline": "Opta Stats: Ange Postecoglou's Tottenham have recorded under 60% possession in only 1 of 18 matches",
                    "source": "Opta Premier League Intelligence", "time": "1d ago", "impact": "TACTICAL IDENTITY"
                },
                "socialMediaRadar": {
                    "platform": "The Extra Inch / Spurs Analytics",
                    "sentimentScore": 82, "sentimentTrend": "+18% Ball dominance",
                    "whaleFlows": "Football analytics quants loading Tottenham possession props.",
                    "retailPositioning": "Recognized identity across betting communities."
                },
                "riskMitigation": "Redeem upon completion of Sunday fixtures."
            }
        },
        {
            "id": "epl-w-10", "rank": 10,
            "title": "Will over 28 total goals be scored across all 10 Premier League matches this weekend?",
            "slug": "over-28-total-goals-premier-league-weekend",
            "volume": "$14,700,000", "volumeRaw": 14700000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,150,000", "endDate": "Sunday 9:00 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.4% EV+", "impliedProb": 68, "fairValueProb": 78.5,
                "targetExit": "$0.83 (+22.0% gain)", "stopLoss": "$0.54",
                "macroStrategy": "The current Premier League season averages 3.14 goals per match, projecting an expected total of 31.4 goals for 10 matches. A 28-goal hurdle requires only 2.9 goals per match, well below seasonal baseline.",
                "newsCatalyst": {
                    "headline": "Premier League Matchday Data: Five of this weekend's ten fixtures feature top-6 attacking teams vs porous defenses",
                    "source": "Premier League Stats Lab", "time": "1d ago", "impact": "GOAL EXPECTANCY"
                },
                "socialMediaRadar": {
                    "platform": "Match of the Day / Football Accumulators",
                    "sentimentScore": 85, "sentimentTrend": "+20% High-scoring weekend",
                    "whaleFlows": "Syndicate bettors backing weekend goal aggregate Overs.",
                    "retailPositioning": "Widespread entertainment backing."
                },
                "riskMitigation": "Cash out once 29th goal is scored across Saturday and Sunday games."
            }
        }
    ],
    "month": [
        {
            "id": "epl-m-01", "rank": 1,
            "title": "Will Manchester City win the Premier League Title 2024/25?",
            "slug": "manchester-city-win-premier-league-title-2025",
            "volume": "$76,400,000", "volumeRaw": 76400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$16,500,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.48, "pct": 48}, {"name": "NO", "price": 0.52, "pct": 52}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.8% EV+", "impliedProb": 48, "fairValueProb": 58.0,
                "targetExit": "$0.66 (+37.5% gain)", "stopLoss": "$0.36",
                "macroStrategy": "Historical spring sprint modeling shows Manchester City averages 2.45 points per game from February to May over the past 5 title-winning campaigns. With 4 consecutive crowns in the bag, 0.48 pricing severely discounts Pep Guardiola's squad depth.",
                "newsCatalyst": {
                    "headline": "Opta Supercomputer Title Simulation: Manchester City simulated to win title in 56.4% of 10,000 full-season runs",
                    "source": "Opta Football Simulations", "time": "2d ago", "impact": "SIMULATION FAVORITE"
                },
                "socialMediaRadar": {
                    "platform": "Sky Sports / Gary Neville & Jamie Carragher Debate",
                    "sentimentScore": 79, "sentimentTrend": "+17% Inevitability thesis",
                    "whaleFlows": "Institutional sports hedge funds accumulating Man City title shares under 0.50.",
                    "retailPositioning": "Retail seduced by Liverpool's hot start, leaving City at attractive discount."
                },
                "riskMitigation": "Core portfolio holding; rebalance after the head-to-head title showdown."
            }
        },
        {
            "id": "epl-m-02", "rank": 2,
            "title": "Will Chelsea qualify for the UEFA Champions League (Top 4 Finish)?",
            "slug": "chelsea-qualify-champions-league-top-4",
            "volume": "$54,200,000", "volumeRaw": 54200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$11,800,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.9% EV+", "impliedProb": 62, "fairValueProb": 73.0,
                "targetExit": "$0.78 (+25.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Chelsea ranks #2 in Premier League expected goal difference (+0.78/90) behind only Man City. With Manchester United and Tottenham struggling for defensive consistency, Chelsea has solidified its place as the 3rd or 4th strongest outfit.",
                "newsCatalyst": {
                    "headline": "The Athletic: Enzo Maresca establishes clear tactical hierarchy as squad depth powers through fatigue",
                    "source": "The Athletic Tactical Hub", "time": "3d ago", "impact": "TACTICAL CONSOLIDATION"
                },
                "socialMediaRadar": {
                    "platform": "Chelsea News / Football Daily",
                    "sentimentScore": 84, "sentimentTrend": "+21% Top-4 certainty",
                    "whaleFlows": "High-net-worth football syndicates taking large positions on Chelsea top 4.",
                    "retailPositioning": "Public consensus aligning with statistical reality."
                },
                "riskMitigation": "Lock 50% profits once Chelsea builds a 6-point cushion over 5th place."
            }
        },
        {
            "id": "epl-m-03", "rank": 3,
            "title": "Will Erling Haaland win the Premier League Golden Boot?",
            "slug": "erling-haaland-win-premier-league-golden-boot",
            "volume": "$61,800,000", "volumeRaw": 61800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$13,400,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.79, "pct": 79}, {"name": "NO", "price": 0.21, "pct": 21}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 92, "evEdge": "+10.6% EV+", "impliedProb": 79, "fairValueProb": 89.5,
                "targetExit": "$0.94 (+19.0% gain)", "stopLoss": "$0.68",
                "macroStrategy": "Haaland holds a 4-goal lead over the chasing pack with an underlying xG of 1.02 per 90. Barring a multi-month injury catastrophe, no other Premier League striker generates comparable volume in a dominant attacking system.",
                "newsCatalyst": {
                    "headline": "BBC Sport: Haaland on course for third consecutive Golden Boot as City supply line expands",
                    "source": "BBC Sport Football Records", "time": "2d ago", "impact": "GOAL CORONATION"
                },
                "socialMediaRadar": {
                    "platform": "FPL Twitter / Premier League Central",
                    "sentimentScore": 93, "sentimentTrend": "+24% Inevitable winner",
                    "whaleFlows": "Arbitrage syndicates treating Haaland Golden Boot as a high-yield institutional cash substitute.",
                    "retailPositioning": "Complete alignment across world football."
                },
                "riskMitigation": "Safe, institutional-grade wager; hold into final weeks of the season."
            }
        },
        {
            "id": "epl-m-04", "rank": 4,
            "title": "Will Southampton finish 20th (Bottom of the Table) in the Premier League?",
            "slug": "southampton-finish-20th-premier-league",
            "volume": "$29,500,000", "volumeRaw": 29500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$6,400,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.7% EV+", "impliedProb": 65, "fairValueProb": 76.5,
                "targetExit": "$0.82 (+26.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Southampton possesses the lowest expected goals scored (0.74/90) and highest defensive errors leading to goals (9). Their commitment to low-tempo possession play without elite ball progressors is fatal at Premier League tempo.",
                "newsCatalyst": {
                    "headline": "Daily Echo: Saints goal conversion rate drops to league-worst 6.2% across opening months",
                    "source": "Southern Daily Echo", "time": "3d ago", "impact": "RELEGATION METRICS"
                },
                "socialMediaRadar": {
                    "platform": "Saints Web / Championship Bound X",
                    "sentimentScore": 86, "sentimentTrend": "+20% Bottom finish consensus",
                    "whaleFlows": "Relegation quants loading Southampton dead-last contracts.",
                    "retailPositioning": "Widespread acknowledgement of insurmountable talent deficit."
                },
                "riskMitigation": "Redeem when Southampton's points deficit exceeds 9 points."
            }
        },
        {
            "id": "epl-m-05", "rank": 5,
            "title": "Will Liverpool score 12 or more goals in all competitions this calendar month?",
            "slug": "liverpool-score-12-plus-goals-this-month",
            "volume": "$23,700,000", "volumeRaw": 23700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,100,000", "endDate": "End of Month 11:59 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.2% EV+", "impliedProb": 71, "fairValueProb": 82.0,
                "targetExit": "$0.86 (+21.1% gain)", "stopLoss": "$0.58",
                "macroStrategy": "Liverpool has 6 scheduled fixtures across Premier League, Champions League, and Carabao Cup. Scoring 12 goals requires an average of just 2.0 goals per game, lower than Slot's seasonal average of 2.38.",
                "newsCatalyst": {
                    "headline": "This Is Anfield: Slot's attack averaging 2.45 goals per game across Anfield fixtures",
                    "source": "This Is Anfield Media", "time": "4d ago", "impact": "ATTACKING EFFICIENCY"
                },
                "socialMediaRadar": {
                    "platform": "The Anfield Wrap / Redmen TV",
                    "sentimentScore": 87, "sentimentTrend": "+22% High goal scoring output",
                    "whaleFlows": "Sports syndicates backing monthly team goal over totals.",
                    "retailPositioning": "Liverpool fans highly confident in attacking firepower."
                },
                "riskMitigation": "Cash out immediately upon the 12th goal scored."
            }
        },
        {
            "id": "epl-m-06", "rank": 6,
            "title": "Will Mikel Arteta win Premier League Manager of the Month?",
            "slug": "mikel-arteta-win-manager-of-the-month",
            "volume": "$19,400,000", "volumeRaw": 19400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,200,000", "endDate": "End of Month Award Announcement",
            "outcomes": [{"name": "YES", "price": 0.36, "pct": 36}, {"name": "NO", "price": 0.64, "pct": 64}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.6% EV+", "impliedProb": 64, "fairValueProb": 76.5,
                "targetExit": "$0.80 (+25.0% gain on NO)", "stopLoss": "$0.50",
                "macroStrategy": "Arne Slot (Liverpool) and Fabian Hürzeler (Brighton) have easier monthly fixture schedules and higher point expectations. Arteta's tough calendar virtually guarantees at least one drawn match.",
                "newsCatalyst": {
                    "headline": "Premier League Monthly Preview: Slot frontrunner for MOTM award on undefeated record",
                    "source": "Premier League Broadcast", "time": "3d ago", "impact": "AWARD FAVORITE"
                },
                "socialMediaRadar": {
                    "platform": "Premier League Awards Twitter / TalkSPORT",
                    "sentimentScore": 76, "sentimentTrend": "+19% Arne Slot favorite consensus",
                    "whaleFlows": "Prop betting syndicates laying Arteta to back Slot.",
                    "retailPositioning": "Arsenal fans over-betting Arteta on name recognition."
                },
                "riskMitigation": "Bet NO on Arteta winning MOTM; take attractive 64% baseline edge."
            }
        },
        {
            "id": "epl-m-07", "rank": 7,
            "title": "Will Arsenal concede the fewest goals in the Premier League during this calendar month?",
            "slug": "arsenal-concede-fewest-goals-this-month",
            "volume": "$25,800,000", "volumeRaw": 25800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,600,000", "endDate": "End of Month 11:59 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.7% EV+", "impliedProb": 61, "fairValueProb": 71.5,
                "targetExit": "$0.76 (+24.6% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Saliba and Gabriel represent Europe's most stifling center-back duo, allowing an absurdly low 0.68 xGA per 90. Arsenal conceded only 29 goals all last season and lead the league in clean sheet percentage (52%).",
                "newsCatalyst": {
                    "headline": "Telegraph Sport: Saliba and Gabriel defensive partnership sets 5-year low in big chances conceded",
                    "source": "Telegraph Football Analysis", "time": "4d ago", "impact": "DEFENSIVE FORTRESS"
                },
                "socialMediaRadar": {
                    "platform": "Gunners Reddit / Squawka Football",
                    "sentimentScore": 85, "sentimentTrend": "+20% Defensive supremacy",
                    "whaleFlows": "Defensive prop specialists accumulating Arsenal defensive supremacy props.",
                    "retailPositioning": "Broad consensus on Arsenal's backline reliability."
                },
                "riskMitigation": "Ride into final gameweek; hedge if Saliba incurs a suspension."
            }
        },
        {
            "id": "epl-m-08", "rank": 8,
            "title": "Will Aston Villa surpass 52 points in the league table before the end of this month?",
            "slug": "aston-villa-surpass-52-points-this-month",
            "volume": "$17,600,000", "volumeRaw": 17600000, "volumeLabel": "30-Day Volume",
            "liquidity": "$3,800,000", "endDate": "End of Month 11:59 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+12.2% EV+", "impliedProb": 58, "fairValueProb": 67.5,
                "targetExit": "$0.73 (+25.8% gain)", "stopLoss": "$0.45",
                "macroStrategy": "Unai Emery's Villa currently sits at 44 points and has four winnable matches against lower-table opposition. Taking 8 points from 12 available comfortably pushes them beyond the 52-point benchmark.",
                "newsCatalyst": {
                    "headline": "Express & Star: Ollie Watkins and Morgan Rogers find lethal tandem rhythm in training",
                    "source": "Express & Star Villa Beat", "time": "4d ago", "impact": "POINTS TRAJECTORY"
                },
                "socialMediaRadar": {
                    "platform": "Villa Talk / Under A Gaslit Lamp",
                    "sentimentScore": 80, "sentimentTrend": "+17% Points target optimism",
                    "whaleFlows": "Midlands betting syndicates taking YES on Villa points milestones.",
                    "retailPositioning": "Solid backing from Villa supporters and neutrals."
                },
                "riskMitigation": "Lock winnings once 53rd point is secured."
            }
        },
        {
            "id": "epl-m-09", "rank": 9,
            "title": "Will Cole Palmer win Premier League Player of the Month award?",
            "slug": "cole-palmer-win-player-of-the-month",
            "volume": "$22,100,000", "volumeRaw": 22100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,800,000", "endDate": "End of Month Award Announcement",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+13.4% EV+", "impliedProb": 52, "fairValueProb": 62.0,
                "targetExit": "$0.69 (+32.7% gain)", "stopLoss": "$0.40",
                "macroStrategy": "Palmer has 4 goals and 3 assists in 3 appearances this calendar month, with one match remaining. No other Premier League player matches his 7 direct goal involvements over the qualification window.",
                "newsCatalyst": {
                    "headline": "EA Sports / Premier League: Cole Palmer leads public fan voting and expert captain's ballot by wide margin",
                    "source": "Premier League Awards Committee", "time": "5d ago", "impact": "VOTE LEAD"
                },
                "socialMediaRadar": {
                    "platform": "Chelsea X / Premier League Official",
                    "sentimentScore": 88, "sentimentTrend": "+24% POTM landslide",
                    "whaleFlows": "Award prop bettors accumulating Palmer YES.",
                    "retailPositioning": "Viral popularity guarantees strong public vote weighting."
                },
                "riskMitigation": "Hold into official award announcement on second Friday of next month."
            }
        },
        {
            "id": "epl-m-10", "rank": 10,
            "title": "Will Manchester United sack their manager before the end of this calendar month?",
            "slug": "manchester-united-sack-manager-this-month",
            "volume": "$38,400,000", "volumeRaw": 38400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$8,200,000", "endDate": "End of Month 11:59 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.28, "pct": 28}, {"name": "NO", "price": 0.72, "pct": 72}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+13.8% EV+", "impliedProb": 72, "fairValueProb": 84.0,
                "targetExit": "$0.86 (+19.4% gain on NO)", "stopLoss": "$0.58",
                "macroStrategy": "INEOS leadership (Sir Jim Ratcliffe and Dan Ashworth) have repeatedly stressed a multi-year project horizon with new coaching architecture. A sacking before the summer window would incur hefty contractual severance and disrupt squad stabilization.",
                "newsCatalyst": {
                    "headline": "David Ornstein / The Athletic: INEOS executive committee committed to current tactical setup through the winter campaign",
                    "source": "The Athletic INEOS Special", "time": "5d ago", "impact": "EXECUTIVE BACKING"
                },
                "socialMediaRadar": {
                    "platform": "The United Stand / r/reddevils",
                    "sentimentScore": 81, "sentimentTrend": "+22% Managerial patience",
                    "whaleFlows": "Sharp sports traders laying the sensationalist sacking narrative.",
                    "retailPositioning": "Tabloids whip up daily panic, giving smart money 72% safe yield."
                },
                "riskMitigation": "Bet NO on United manager sacking this month; high conviction win."
            }
        }
    ]
}
