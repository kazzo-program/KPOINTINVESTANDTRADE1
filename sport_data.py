# -*- coding: utf-8 -*-
"""
Sport Polymarket Top 10 Markets (Day, Week, Month)
Covering Major Global Sports: Champions League, NBA, NFL, Formula 1, Tennis, UFC, MLB, Boxing.
With full Macro Hedge Fund Strategy, News Catalysts, and Social Media Radar.
"""

SPORT_DATA = {
    "day": [
        {
            "id": "spt-d-01", "rank": 1,
            "title": "Will Boston Celtics defeat Denver Nuggets by >4.5 points tonight?",
            "slug": "celtics-defeat-nuggets-by-over-45-tonight",
            "volume": "$18,400,000", "volumeRaw": 18400000, "volumeLabel": "24H Volume",
            "liquidity": "$3,950,000", "endDate": "Tonight 10:30 PM EST",
            "outcomes": [{"name": "YES", "price": 0.64, "pct": 64}, {"name": "NO", "price": 0.36, "pct": 36}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+13.4% EV+", "impliedProb": 64, "fairValueProb": 75.0,
                "targetExit": "$0.79 (+23.4% gain)", "stopLoss": "$0.50",
                "macroStrategy": "Quantitative net rating models show Boston +11.4 differential at TD Garden. Denver's perimeter defensive rotation allows 38.6% from 3PT on road back-to-backs, directly playing into Boston's high-volume three-point shooting scheme.",
                "newsCatalyst": {
                    "headline": "ESPN NBA Shootaround: Denver starting point guard listed questionable with calf tightness; Boston at full health",
                    "source": "ESPN NBA Insiders", "time": "1h ago", "impact": "ROSTER ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "Action Network / NBA Betting Reddit",
                    "sentimentScore": 82, "sentimentTrend": "+21% Boston sharp money",
                    "whaleFlows": "Vegas sportsbook line moved from -3.5 to -5.0 as syndicate syndicates pounded Boston.",
                    "retailPositioning": "Public backing Jokic triple-double narrative, ignoring matchup fatigue metrics."
                },
                "riskMitigation": "Lock partial profit if Boston opens a 12+ point lead in the 2nd quarter."
            }
        },
        {
            "id": "spt-d-02", "rank": 2,
            "title": "Will Real Madrid defeat Bayern Munich in tonight's Champions League clash?",
            "slug": "real-madrid-defeat-bayern-munich-cl-tonight",
            "volume": "$29,700,000", "volumeRaw": 29700000, "volumeLabel": "24H Volume",
            "liquidity": "$6,400,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.8% EV+", "impliedProb": 58, "fairValueProb": 68.0,
                "targetExit": "$0.74 (+27.5% gain)", "stopLoss": "$0.44",
                "macroStrategy": "Santiago Bernabéu knockout stage expected goals (xG) overperformance historically runs at +0.72 goals for Madrid. Bayern's high defensive line is uniquely susceptible to Vinícius Jr and Mbappé counter-transition pace.",
                "newsCatalyst": {
                    "headline": "Marca: Ancelotti prepares twin-spear counter setup with Camavinga anchoring midfield transition",
                    "source": "Marca Madrid Desk", "time": "2h ago", "impact": "TACTICAL MISMATCH"
                },
                "socialMediaRadar": {
                    "platform": "X / Football Twitter & Champions League Live",
                    "sentimentScore": 79, "sentimentTrend": "+18% Madrid Bernabéu aura",
                    "whaleFlows": "Polymarket European football whales entered $410k in YES contracts between 0.55-0.58.",
                    "retailPositioning": "Retail split evenly, creating a favorable pricing inefficiency."
                },
                "riskMitigation": "Bet YES; hedge with draw insurance if game remains scoreless past 70 minutes."
            }
        },
        {
            "id": "spt-d-03", "rank": 3,
            "title": "Will Max Verstappen secure Pole Position in today's F1 Qualifying?",
            "slug": "max-verstappen-pole-position-qualifying-today",
            "volume": "$14,800,000", "volumeRaw": 14800000, "volumeLabel": "24H Volume",
            "liquidity": "$3,200,000", "endDate": "Today 4:00 PM Local Track Time",
            "outcomes": [{"name": "YES", "price": 0.46, "pct": 46}, {"name": "NO", "price": 0.54, "pct": 54}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+14.2% EV+", "impliedProb": 54, "fairValueProb": 66.5,
                "targetExit": "$0.72 (+33.3% gain on NO)", "stopLoss": "$0.42",
                "macroStrategy": "McLaren's MCL38 telemetry data from Free Practice 3 reveals a 0.18s sector-2 aerodynamic advantage over Red Bull's RB20. Norris and Piastri tire warm-up curves in Q3 conditions are statistically superior.",
                "newsCatalyst": {
                    "headline": "Sky Sports F1: McLaren engineers dial in aggressive low-drag rear wing; Norris fastest across high-speed apexes",
                    "source": "Sky Sports F1 Pit Lane", "time": "1h 30m ago", "impact": "TELEMETRY ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "F1 Technical Reddit / Paddock Twitter",
                    "sentimentScore": 76, "sentimentTrend": "+23% McLaren pole momentum",
                    "whaleFlows": "Sharp racing syndicates taking NO on Verstappen pole to back McLaren front row lockout.",
                    "retailPositioning": "Casual fans over-betting Verstappen based on historical reputation."
                },
                "riskMitigation": "Bet NO on Verstappen pole; take profits immediately after Q3 chequered flag."
            }
        },
        {
            "id": "spt-d-04", "rank": 4,
            "title": "Will Jannik Sinner win his ATP Masters 1000 match in straight sets today?",
            "slug": "jannik-sinner-win-straight-sets-today",
            "volume": "$12,300,000", "volumeRaw": 12300000, "volumeLabel": "24H Volume",
            "liquidity": "$2,650,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.73, "pct": 73}, {"name": "NO", "price": 0.27, "pct": 27}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.8% EV+", "impliedProb": 73, "fairValueProb": 84.0,
                "targetExit": "$0.87 (+19.1% gain)", "stopLoss": "$0.60",
                "macroStrategy": "Sinner has won 88% of hard-court sets over the past 6 months. Opponent's first-serve return win rate is merely 26%, unable to break Sinner's 130mph pinpoint delivery on fast indoor courts.",
                "newsCatalyst": {
                    "headline": "Tennis Channel Court Report: Sinner flawless in warmups, holding 94% service games this tournament",
                    "source": "Tennis Channel Analytics", "time": "2h ago", "impact": "DOMINANT FORM"
                },
                "socialMediaRadar": {
                    "platform": "Tennis Abstract / Tennis Twitter",
                    "sentimentScore": 89, "sentimentTrend": "+19% Straight-set consensus",
                    "whaleFlows": "Tennis quantitative trading models backing Sinner 2-0 set score.",
                    "retailPositioning": "Strong smart money backing; high-probability win vector."
                },
                "riskMitigation": "Lock profits after 1st set win (e.g. at 6-2 / 6-3)."
            }
        },
        {
            "id": "spt-d-05", "rank": 5,
            "title": "Will the UFC Main Event finish by KO/TKO or Submission inside 3 rounds tonight?",
            "slug": "ufc-main-event-finish-inside-3-rounds-tonight",
            "volume": "$16,500,000", "volumeRaw": 16500000, "volumeLabel": "24H Volume",
            "liquidity": "$3,500,000", "endDate": "Tonight 11:45 PM EST",
            "outcomes": [{"name": "YES", "price": 0.67, "pct": 67}, {"name": "NO", "price": 0.33, "pct": 33}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.9% EV+", "impliedProb": 67, "fairValueProb": 78.0,
                "targetExit": "$0.83 (+23.8% gain)", "stopLoss": "$0.54",
                "macroStrategy": "Both heavyweights hold career stoppage rates over 85% within rounds 1-2. Strike defense metrics under 52% combined with 4-ounce gloves create statistical inevitability of an early finish.",
                "newsCatalyst": {
                    "headline": "MMA Fighting Weigh-in Report: Both fighters make championship weight looking aggressive and rehydrated",
                    "source": "MMA Fighting Official", "time": "3h ago", "impact": "STOPPAGE TRAJECTORY"
                },
                "socialMediaRadar": {
                    "platform": "r/MMA / Combat Sports X",
                    "sentimentScore": 84, "sentimentTrend": "+22% Early violence expectation",
                    "whaleFlows": "Combat sports syndicates pounding 'Does Not Go The Distance' prop contracts.",
                    "retailPositioning": "Retail unanimous on explosive stoppage."
                },
                "riskMitigation": "Execution strictly on under 3.5 rounds / stoppage YES contract."
            }
        },
        {
            "id": "spt-d-06", "rank": 6,
            "title": "Will LeBron James record 25+ Points tonight vs Phoenix Suns?",
            "slug": "lebron-james-score-over-25-points-tonight",
            "volume": "$11,700,000", "volumeRaw": 11700000, "volumeLabel": "24H Volume",
            "liquidity": "$2,400,000", "endDate": "Tonight 10:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.57, "pct": 57}, {"name": "NO", "price": 0.43, "pct": 43}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.0% EV+", "impliedProb": 57, "fairValueProb": 66.0,
                "targetExit": "$0.72 (+26.3% gain)", "stopLoss": "$0.44",
                "macroStrategy": "Matchup modeling against Phoenix shows Kevin Durant switched to defense will limit Anthony Davis post entries, forcing LeBron into 18+ field goal attempts and primary paint drives.",
                "newsCatalyst": {
                    "headline": "Lakers Nation Beat: LeBron averaged 28.4 PPG in last 5 meetings against Phoenix small-ball lineups",
                    "source": "Lakers Beat Report", "time": "2h 30m ago", "impact": "SCORING USAGE"
                },
                "socialMediaRadar": {
                    "platform": "Underdog Fantasy / NBA Prop Twitter",
                    "sentimentScore": 77, "sentimentTrend": "+16% Over 25.5 points trend",
                    "whaleFlows": "High-volume prop trading accounts taking the Over on LeBron scoring.",
                    "retailPositioning": "Retail heavily backing the King in primetime TV matchup."
                },
                "riskMitigation": "Take profits early if LeBron reaches 16 points by halftime."
            }
        },
        {
            "id": "spt-d-07", "rank": 7,
            "title": "Will New York Yankees hit Over 1.5 Home Runs in tonight's game?",
            "slug": "ny-yankees-hit-over-15-home-runs-tonight",
            "volume": "$9,800,000", "volumeRaw": 9800000, "volumeLabel": "24H Volume",
            "liquidity": "$2,100,000", "endDate": "Tonight 7:05 PM EST",
            "outcomes": [{"name": "YES", "price": 0.54, "pct": 54}, {"name": "NO", "price": 0.46, "pct": 46}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 79, "evEdge": "+11.8% EV+", "impliedProb": 54, "fairValueProb": 63.5,
                "targetExit": "$0.69 (+27.7% gain)", "stopLoss": "$0.41",
                "macroStrategy": "Weather forecasts at Yankee Stadium show 14 mph winds blowing out to short right porch. Opposing starting pitcher yields 1.62 HR/9 against right-handed power hitters like Judge and Stanton.",
                "newsCatalyst": {
                    "headline": "MLB Statcast Weather: Temperature 74°F with air density index favoring deep fly-ball carry",
                    "source": "Statcast Weather Lab", "time": "3h ago", "impact": "HOME RUN CONDITIONS"
                },
                "socialMediaRadar": {
                    "platform": "Baseball Savant / MLB Prop Discord",
                    "sentimentScore": 75, "sentimentTrend": "+15% Dinger Tuesday momentum",
                    "whaleFlows": "Sharp MLB syndicates backing Yankee Stadium Over totals.",
                    "retailPositioning": "Aaron Judge anytime home run favorite among recreational bettors."
                },
                "riskMitigation": "Manage risk; exit if opposing pitcher completes 4 scoreless innings."
            }
        },
        {
            "id": "spt-d-08", "rank": 8,
            "title": "Will Edmonton Oilers defeat Dallas Stars in regulation time tonight?",
            "slug": "edmonton-oilers-defeat-dallas-stars-regulation",
            "volume": "$10,400,000", "volumeRaw": 10400000, "volumeLabel": "24H Volume",
            "liquidity": "$2,250,000", "endDate": "Tonight 8:30 PM CST",
            "outcomes": [{"name": "YES", "price": 0.48, "pct": 48}, {"name": "NO", "price": 0.52, "pct": 52}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "MODERATE CONVICTION",
                "confidencePct": 78, "evEdge": "+11.2% EV+", "impliedProb": 52, "fairValueProb": 60.5,
                "targetExit": "$0.67 (+28.8% gain on NO)", "stopLoss": "$0.40",
                "macroStrategy": "Dallas Stars rank #2 in NHL 5-on-5 expected goals against (xGA). Their ability to roll four balanced checking lines neutralizes McDavid and Draisaitl transition rushes, pushing games toward overtime.",
                "newsCatalyst": {
                    "headline": "Daily Faceoff: Stars starting goaltender Jake Oettinger posts .934 save percentage past two weeks",
                    "source": "Daily Faceoff NHL", "time": "4h ago", "impact": "GOALIE WALL"
                },
                "socialMediaRadar": {
                    "platform": "NHL Betting Subreddit / PuckPicks",
                    "sentimentScore": 71, "sentimentTrend": "+17% Low-scoring / tight game bias",
                    "whaleFlows": "Pro hockey bettors taking NO on regulation Oilers win, anticipating overtime dogfight.",
                    "retailPositioning": "Casual fans over-betting Oilers star power."
                },
                "riskMitigation": "Bet NO on regulation win (cash if game ties in regulation or Dallas wins)."
            }
        },
        {
            "id": "spt-d-09", "rank": 9,
            "title": "Will India chase down target in tonight's T20 International?",
            "slug": "india-chase-down-target-t20-tonight",
            "volume": "$15,100,000", "volumeRaw": 15100000, "volumeLabel": "24H Volume",
            "liquidity": "$3,100,000", "endDate": "Tonight 10:00 PM IST",
            "outcomes": [{"name": "YES", "price": 0.71, "pct": 71}, {"name": "NO", "price": 0.29, "pct": 29}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.4% EV+", "impliedProb": 71, "fairValueProb": 82.0,
                "targetExit": "$0.86 (+21.1% gain)", "stopLoss": "$0.58",
                "macroStrategy": "Dew factor at Wankhede Stadium significantly reduces second-innings spin grip, resulting in a 74% historic win rate for the team batting second under lights.",
                "newsCatalyst": {
                    "headline": "ESPNCricinfo Pitch Report: Heavy evening dew expected; surface offers true bounce and fast outfield",
                    "source": "ESPNCricinfo Live", "time": "2h ago", "impact": "DEW ADVANTAGE"
                },
                "socialMediaRadar": {
                    "platform": "Cricket Twitter / Cricbuzz Community",
                    "sentimentScore": 88, "sentimentTrend": "+24% Chasing bias",
                    "whaleFlows": "Asian cricket liquidity pools pricing Indian chase depth favorably.",
                    "retailPositioning": "Massive retail volume backing India; structural pitch conditions support bet."
                },
                "riskMitigation": "Secure profits when required run rate stays under 8.5 with 7+ wickets in hand."
            }
        },
        {
            "id": "spt-d-10", "rank": 10,
            "title": "Will World Title Boxing Match go the full 12 rounds tonight?",
            "slug": "world-title-boxing-match-full-12-rounds",
            "volume": "$8,900,000", "volumeRaw": 8900000, "volumeLabel": "24H Volume",
            "liquidity": "$1,900,000", "endDate": "Tonight 11:30 PM GMT",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.1% EV+", "impliedProb": 62, "fairValueProb": 72.0,
                "targetExit": "$0.77 (+24.2% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Both orthodox defensive fighters possess iron chins and zero career stoppage losses. Punch output is predominantly jab-heavy with low inside risk, making a judges' decision the mathematically dominant outcome.",
                "newsCatalyst": {
                    "headline": "The Ring Magazine: Both fighters emphasize tactical discipline and punch-output pacing in pre-fight interviews",
                    "source": "The Ring Boxing Desk", "time": "5h ago", "impact": "DECISION PROFILE"
                },
                "socialMediaRadar": {
                    "platform": "Boxing Scene / r/Boxing",
                    "sentimentScore": 81, "sentimentTrend": "+18% Distance consensus",
                    "whaleFlows": "Sharp boxing syndicates buying 'Goes 12 Rounds' prop contracts.",
                    "retailPositioning": "Recreational punters hunting knockout highlight reels; sharp money takes distance."
                },
                "riskMitigation": "Execute on Polymarket 'Goes the Distance YES' outcome."
            }
        }
    ],
    "week": [
        {
            "id": "spt-w-01", "rank": 1,
            "title": "Will Kansas City Chiefs clinch the AFC #1 playoff seed this game week?",
            "slug": "chiefs-clinch-afc-1-seed-this-gameweek",
            "volume": "$38,600,000", "volumeRaw": 38600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$8,200,000", "endDate": "Monday Night Football Final",
            "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.6% EV+", "impliedProb": 76, "fairValueProb": 87.0,
                "targetExit": "$0.91 (+19.7% gain)", "stopLoss": "$0.64",
                "macroStrategy": "Chiefs defense EPA/play ranks top-3 in NFL, while AFC rival Buffalo Bills face an arduous road matchup. Kansas City needs just one win or Buffalo loss to lock home-field advantage through Arrowhead.",
                "newsCatalyst": {
                    "headline": "NFL Network: Andy Reid confirms starters fully healthy; Patrick Mahomes 16-1 straight up in December games",
                    "source": "NFL Network Insider", "time": "6h ago", "impact": "CLINCH SCENARIO"
                },
                "socialMediaRadar": {
                    "platform": "NFL Reddit / Fantasy Life & X Sports",
                    "sentimentScore": 87, "sentimentTrend": "+22% Arrowhead inevitability",
                    "whaleFlows": "Vegas sharp books taking massive Kansas City moneyline parlays.",
                    "retailPositioning": "Public backing Chiefs dynasty relentlessly."
                },
                "riskMitigation": "Lock winnings once 4th quarter lead is secured."
            }
        },
        {
            "id": "spt-w-02", "rank": 2,
            "title": "Will McLaren score a double podium finish at this weekend's Grand Prix?",
            "slug": "mclaren-score-double-podium-this-weekend",
            "volume": "$24,500,000", "volumeRaw": 24500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$5,100,000", "endDate": "Sunday Race Finish",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+13.2% EV+", "impliedProb": 65, "fairValueProb": 76.5,
                "targetExit": "$0.80 (+23.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "McLaren MCL38 tire degradation coefficient is 0.04s per lap lower than Ferrari and 0.09s lower than Red Bull on high-downforce medium tires. Lando Norris and Oscar Piastri form the most consistent dual-podium pairing on the grid.",
                "newsCatalyst": {
                    "headline": "Autosport: Andrea Stella confirms floor upgrade delivering anticipated 0.22s simulation gains",
                    "source": "Autosport F1 Intelligence", "time": "8h ago", "impact": "AERO DOMINANCE"
                },
                "socialMediaRadar": {
                    "platform": "F1 Technical / Papaya Army Twitter",
                    "sentimentScore": 84, "sentimentTrend": "+19% Double podium momentum",
                    "whaleFlows": "High-net-worth motorsport syndicates buying McLaren team props.",
                    "retailPositioning": "Retail fans confident in Papaya pace."
                },
                "riskMitigation": "Exit if first-lap collision damage compromises either car."
            }
        },
        {
            "id": "spt-w-03", "rank": 3,
            "title": "Will Carlos Alcaraz win the ATP Masters 1000 tournament this Sunday?",
            "slug": "carlos-alcaraz-win-atp-masters-this-sunday",
            "volume": "$19,200,000", "volumeRaw": 19200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,200,000", "endDate": "Sunday 6:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.54, "pct": 54}, {"name": "NO", "price": 0.46, "pct": 46}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+12.4% EV+", "impliedProb": 54, "fairValueProb": 63.5,
                "targetExit": "$0.70 (+29.6% gain)", "stopLoss": "$0.42",
                "macroStrategy": "Alcaraz's draw path opened up following the early exit of seed #4. His baseline forehand heavy topspin speed (81 mph avg) creates unplayable angles on this specific court surface.",
                "newsCatalyst": {
                    "headline": "L'Équipe: Alcaraz moves freely in practice; physical conditioning coach confirms peak fitness indices",
                    "source": "L'Équipe Tennis Desk", "time": "10h ago", "impact": "CLEAN PATH"
                },
                "socialMediaRadar": {
                    "platform": "Tennis Abstract / Tennis Channel Community",
                    "sentimentScore": 79, "sentimentTrend": "+17% Title favorite surge",
                    "whaleFlows": "Futures arbitrage traders hedging Sinner vs Alcaraz tournament winner.",
                    "retailPositioning": "Retail enthusiasm high; market price offers 12% EV margin."
                },
                "riskMitigation": "Lock 50% profits once Carlos qualifies for Sunday's final."
            }
        },
        {
            "id": "spt-w-04", "rank": 4,
            "title": "Will Golden State Warriors go 3-0 on their current 3-game road trip?",
            "slug": "warriors-go-3-0-road-trip-this-week",
            "volume": "$13,700,000", "volumeRaw": 13700000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,900,000", "endDate": "Sunday 11:30 PM EST",
            "outcomes": [{"name": "YES", "price": 0.41, "pct": 41}, {"name": "NO", "price": 0.59, "pct": 59}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+13.9% EV+", "impliedProb": 59, "fairValueProb": 70.0,
                "targetExit": "$0.74 (+25.4% gain on NO)", "stopLoss": "$0.46",
                "macroStrategy": "Winning all three games of an NBA road swing has a historical league baseline probability of only 29%. Game 3 is a back-to-back at high altitude in Salt Lake City, where Curry's minutes will be capped.",
                "newsCatalyst": {
                    "headline": "The Athletic NBA: Steve Kerr hints at rotational minutes management for veteran core on back-to-back legs",
                    "source": "The Athletic Warriors Beat", "time": "12h ago", "impact": "LOAD MANAGEMENT"
                },
                "socialMediaRadar": {
                    "platform": "Warriors Reddit / Hoops Analysis",
                    "sentimentScore": 42, "sentimentTrend": "-15% Road fatigue realism",
                    "whaleFlows": "Quant sports models shorting road-trip sweep props.",
                    "retailPositioning": "Casual fans backing Steph Curry stardom, ignoring back-to-back attrition."
                },
                "riskMitigation": "Bet NO on 3-0 sweep; capture high-probability statistical fade."
            }
        },
        {
            "id": "spt-w-05", "rank": 5,
            "title": "Will Scottie Scheffler finish in the Top 5 at this week's PGA Tour event?",
            "slug": "scottie-scheffler-finish-top-5-this-weekend",
            "volume": "$17,600,000", "volumeRaw": 17600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,800,000", "endDate": "Sunday 6:30 PM EST",
            "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.2% EV+", "impliedProb": 68, "fairValueProb": 79.0,
                "targetExit": "$0.83 (+22.0% gain)", "stopLoss": "$0.55",
                "macroStrategy": "Scheffler's Strokes Gained: Tee-to-Green (+2.84) leads the PGA Tour by a historic margin. In his last 18 starts, Scheffler has finished inside the top 5 in 14 of them (77.8% empirical hit rate).",
                "newsCatalyst": {
                    "headline": "Golf Digest: Scheffler switches to optimized mallet putter setup, gaining +1.2 strokes putting in early practice rounds",
                    "source": "Golf Digest Pro Tour", "time": "14h ago", "impact": "PUTTING RECOVERY"
                },
                "socialMediaRadar": {
                    "platform": "PGA Tour Twitter / No Laying Up Community",
                    "sentimentScore": 88, "sentimentTrend": "+21% Scheffler reliability",
                    "whaleFlows": "Golf statistical quants loading Scheffler Top-5 props.",
                    "retailPositioning": "Unanimous consensus among professional golf handicappers."
                },
                "riskMitigation": "Hold into Sunday round; hedge if wind conditions exceed 30 knots."
            }
        },
        {
            "id": "spt-w-06", "rank": 6,
            "title": "Will English clubs win 3 or more matches in this week's Champions League fixtures?",
            "slug": "english-clubs-win-3-plus-cl-matches-this-week",
            "volume": "$21,400,000", "volumeRaw": 21400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,600,000", "endDate": "Wednesday 11:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.66, "pct": 66}, {"name": "NO", "price": 0.34, "pct": 34}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.7% EV+", "impliedProb": 66, "fairValueProb": 76.5,
                "targetExit": "$0.80 (+21.2% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Manchester City, Arsenal, Liverpool, and Aston Villa all face favorable European group-stage ties. Combined financial wage bills and squad depths provide overwhelming statistical superiority.",
                "newsCatalyst": {
                    "headline": "Opta Analyst: Premier League teams projected to win 3.4 out of 4 European fixtures this matchweek",
                    "source": "Opta European Football", "time": "16h ago", "impact": "STATISTICAL EDGE"
                },
                "socialMediaRadar": {
                    "platform": "Football Daily / r/soccer",
                    "sentimentScore": 83, "sentimentTrend": "+19% Premier League dominance",
                    "whaleFlows": "European syndicates backing multi-team English accumulators.",
                    "retailPositioning": "Widespread retail backing; underpinned by massive squad value disparity."
                },
                "riskMitigation": "Cash out once 3 victories are secured across Tuesday and Wednesday fixtures."
            }
        },
        {
            "id": "spt-w-07", "rank": 7,
            "title": "Will Los Angeles Dodgers sweep their 3-game weekend baseball series?",
            "slug": "la-dodgers-sweep-3-game-series-this-weekend",
            "volume": "$15,800,000", "volumeRaw": 15800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,300,000", "endDate": "Sunday 8:00 PM PST",
            "outcomes": [{"name": "YES", "price": 0.43, "pct": 43}, {"name": "NO", "price": 0.57, "pct": 57}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+14.1% EV+", "impliedProb": 57, "fairValueProb": 68.0,
                "targetExit": "$0.72 (+26.3% gain on NO)", "stopLoss": "$0.44",
                "macroStrategy": "Sweeping any 3-game MLB series carries high inherent variance. In Game 2, the Dodgers bullpen game faces an opponent with a rested ace starter, capping sweep probability at roughly 33%.",
                "newsCatalyst": {
                    "headline": "Dodgers Beat: Dave Roberts confirms starting rotation reshuffle to preserve arms for postseason",
                    "source": "LA Times Sports Desk", "time": "18h ago", "impact": "ROTATION VARIANCE"
                },
                "socialMediaRadar": {
                    "platform": "Dodger Blue / MLB Trade Rumors",
                    "sentimentScore": 46, "sentimentTrend": "-14% Fade sweep bias",
                    "whaleFlows": "Sharp baseball handicappers buying NO on sweep props across the board.",
                    "retailPositioning": "Recreational public betting Dodgers sweep due to Ohtani star power."
                },
                "riskMitigation": "Bet NO on Dodgers 3-game sweep; win if Dodgers drop any single match."
            }
        },
        {
            "id": "spt-w-08", "rank": 8,
            "title": "Will New York Rangers maintain the NHL's lowest goals-against average this week?",
            "slug": "ny-rangers-lowest-nhl-gaa-this-week",
            "volume": "$11,200,000", "volumeRaw": 11200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,400,000", "endDate": "Sunday 11:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.0% EV+", "impliedProb": 62, "fairValueProb": 71.5,
                "targetExit": "$0.76 (+22.5% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Igor Shesterkin leads the NHL in Goals Saved Above Expected (GSAx) at +14.2. With penalty kill operating at 89.2% efficiency, Rangers allow under 2.1 goals per 60 minutes.",
                "newsCatalyst": {
                    "headline": "NHL.com: Rangers defensive core clears slot shots at league-best 78% rebound suppression rate",
                    "source": "NHL Analytics Bureau", "time": "1d ago", "impact": "DEFENSIVE FORTRESS"
                },
                "socialMediaRadar": {
                    "platform": "Blueshirts Brotherhood / Puck Guru",
                    "sentimentScore": 82, "sentimentTrend": "+17% Shesterkin dominance",
                    "whaleFlows": "Hockey analytics funds betting defensive props on Madison Square Garden games.",
                    "retailPositioning": "Retail recognizing historic goalie performance."
                },
                "riskMitigation": "Ride trend; hedge if backup netminder gets surprise start."
            }
        },
        {
            "id": "spt-w-09", "rank": 9,
            "title": "Will UFC Main Event favorite betting odds shorten further before fight night?",
            "slug": "ufc-main-event-favorite-odds-shorten-fight-night",
            "volume": "$14,300,000", "volumeRaw": 14300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,050,000", "endDate": "Saturday 10:00 PM EST",
            "outcomes": [{"name": "YES", "price": 0.59, "pct": 59}, {"name": "NO", "price": 0.41, "pct": 41}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+12.5% EV+", "impliedProb": 59, "fairValueProb": 68.5,
                "targetExit": "$0.74 (+25.4% gain)", "stopLoss": "$0.46",
                "macroStrategy": "Fight week open workouts and press conference media buzz consistently trigger a late recreational avalanche on the reigning champion, driving odds from -180 to -240.",
                "newsCatalyst": {
                    "headline": "MMA Junkie: Champion arrives looking shredded with entire Dagestani training camp in attendance",
                    "source": "MMA Junkie Fight Week", "time": "1d ago", "impact": "MEDIA MOMENTUM"
                },
                "socialMediaRadar": {
                    "platform": "X / Combat Twitter & UFC Embedded",
                    "sentimentScore": 81, "sentimentTrend": "+18% Heavy favorite steam",
                    "whaleFlows": "Market makers widening lines to balance retail parlay exposure.",
                    "retailPositioning": "Public overwhelmingly adds champion to all weekend parlays."
                },
                "riskMitigation": "Lock profit on Friday evening after official weigh-ins."
            }
        },
        {
            "id": "spt-w-10", "rank": 10,
            "title": "Will South Africa defeat New Zealand in this weekend's Rugby clash?",
            "slug": "south-africa-defeat-new-zealand-rugby-this-weekend",
            "volume": "$12,900,000", "volumeRaw": 12900000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,700,000", "endDate": "Saturday 5:00 PM SAST",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.9% EV+", "impliedProb": 63, "fairValueProb": 73.5,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.50",
                "macroStrategy": "Springboks 'Bomb Squad' 7-1 bench split produces overwhelming second-half scrum dominance at altitude in Johannesburg. All Blacks ruck retention drops 14% under sustained physical collisions.",
                "newsCatalyst": {
                    "headline": "SuperSport Rugby: Rassie Erasmus names full-strength forward pack with Eben Etzebeth starting",
                    "source": "SuperSport Rugby Central", "time": "1d ago", "impact": "SCRUM DOMINANCE"
                },
                "socialMediaRadar": {
                    "platform": "r/rugbyunion / Rugby Pass",
                    "sentimentScore": 80, "sentimentTrend": "+16% Springbok physical supremacy",
                    "whaleFlows": "Southern Hemisphere bookmakers moving handicap spread from -3.5 to -5.5.",
                    "retailPositioning": "Global rugby fraternity split; highveld conditions favor Springboks."
                },
                "riskMitigation": "Take profits when Springboks lead by 8+ points past 60th minute mark."
            }
        }
    ],
    "month": [
        {
            "id": "spt-m-01", "rank": 1,
            "title": "Will Kansas City Chiefs or Detroit Lions win Super Bowl LIX?",
            "slug": "chiefs-or-lions-win-super-bowl-lix",
            "volume": "$88,400,000", "volumeRaw": 88400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$19,200,000", "endDate": "Super Bowl Sunday",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+13.8% EV+", "impliedProb": 58, "fairValueProb": 69.5,
                "targetExit": "$0.76 (+31.0% gain)", "stopLoss": "$0.45",
                "macroStrategy": "DVOA analytics rank Detroit #1 in offensive efficiency and Kansas City #2 in defensive late-down stops. Combining both conference frontrunners captures over 68% true simulation equity.",
                "newsCatalyst": {
                    "headline": "Football Outsiders / FTN Data: Lions and Chiefs combine for highest Super Bowl matchup probability in 15 years",
                    "source": "FTN Football Analytics", "time": "2d ago", "impact": "SIMULATION DOMINANCE"
                },
                "socialMediaRadar": {
                    "platform": "NFL FinTwit / The Ringer NFL Show",
                    "sentimentScore": 86, "sentimentTrend": "+23% Powerhouse consensus",
                    "whaleFlows": "Institutional sports hedge funds accumulating yes contracts on the two dominant favorites.",
                    "retailPositioning": "Retail loves both teams; hedge fund statistical portfolio construction confirms edge."
                },
                "riskMitigation": "Hold into playoff conference championship weekend; cash out high returns."
            }
        },
        {
            "id": "spt-m-02", "rank": 2,
            "title": "Will Real Madrid reach the UEFA Champions League Final?",
            "slug": "real-madrid-reach-champions-league-final",
            "volume": "$64,200,000", "volumeRaw": 64200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$14,100,000", "endDate": "Champions League Semi-Finals Conclusion",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.9% EV+", "impliedProb": 52, "fairValueProb": 62.5,
                "targetExit": "$0.70 (+34.6% gain)", "stopLoss": "$0.38",
                "macroStrategy": "Carlo Ancelotti's knockout tournament conversion rate (6 European finals reached) is unmatched in modern football history. With Mbappé, Vinícius, and Bellingham peaking in spring, market severely underprices Madrid's pedigree.",
                "newsCatalyst": {
                    "headline": "UEFA Technical Study Group: Real Madrid maintain highest xG efficiency in knockout transition football",
                    "source": "UEFA Technical Reports", "time": "3d ago", "impact": "KNOCKOUT MASTERY"
                },
                "socialMediaRadar": {
                    "platform": "Football Twitter / Real Madrid Zone",
                    "sentimentScore": 82, "sentimentTrend": "+19% Bernabéu mystique",
                    "whaleFlows": "Polymarket football syndicates building sizable positions on Madrid reaching Wembley / Munich.",
                    "retailPositioning": "Retail tempted by Manchester City or Barcelona, leaving Madrid at attractive value."
                },
                "riskMitigation": "Lock 60% position once Madrid advances through the quarter-finals."
            }
        },
        {
            "id": "spt-m-03", "rank": 3,
            "title": "Will Boston Celtics reach the NBA Finals again this season?",
            "slug": "boston-celtics-reach-nba-finals-this-season",
            "volume": "$52,800,000", "volumeRaw": 52800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$11,500,000", "endDate": "Eastern Conference Finals Conclusion",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.7% EV+", "impliedProb": 65, "fairValueProb": 76.5,
                "targetExit": "$0.82 (+26.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "The Eastern Conference presents historically weak competition with Philadelphia and Milwaukee plagued by health and depth deficiencies. Boston's net rating (+10.8) makes an Eastern Finals exit statistically improbable.",
                "newsCatalyst": {
                    "headline": "Zach Lowe / ESPN: Celtics have virtually no structural flaw in a 7-game playoff series in the East",
                    "source": "ESPN Lowe Post", "time": "2d ago", "impact": "CONFERENCE DOMINANCE"
                },
                "socialMediaRadar": {
                    "platform": "NBA Twitter / Bill Simmons Podcast Feeds",
                    "sentimentScore": 89, "sentimentTrend": "+22% Repeat finalist consensus",
                    "whaleFlows": "Vegas sportsbooks have Boston priced at -175 to win East; Polymarket at 0.65 is deeply discounted.",
                    "retailPositioning": "Heavy smart money accumulation on Celtics Eastern Conference crown."
                },
                "riskMitigation": "Core high-probability tournament holding; cash out prior to NBA Finals Game 1."
            }
        },
        {
            "id": "spt-m-04", "rank": 4,
            "title": "Will Jannik Sinner remain ATP World No. 1 at the end of this calendar month?",
            "slug": "jannik-sinner-remain-world-no-1-month-end",
            "volume": "$39,700,000", "volumeRaw": 39700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$8,600,000", "endDate": "End of Month ATP Ranking Update",
            "outcomes": [{"name": "YES", "price": 0.91, "pct": 91}, {"name": "NO", "price": 0.09, "pct": 9}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 96, "evEdge": "+6.8% EV+", "impliedProb": 91, "fairValueProb": 98.2,
                "targetExit": "$0.99 (+8.8% gain)", "stopLoss": "$0.84",
                "macroStrategy": "Sinner holds an unassailable mathematical ranking points lead of over 3,800 points above Carlos Alcaraz and Alexander Zverev. Even a withdrawal from upcoming tournaments leaves Sinner as mathematical #1.",
                "newsCatalyst": {
                    "headline": "ATP Tour Rankings Analysis: Sinner mathematically locks year-end / monthly No. 1 position",
                    "source": "ATP Official Rankings Desk", "time": "3d ago", "impact": "MATHEMATICAL LOCK"
                },
                "socialMediaRadar": {
                    "platform": "Tennis Abstract / Tennis Twitter",
                    "sentimentScore": 97, "sentimentTrend": "+25% Mathematical certainty",
                    "whaleFlows": "Whales using this contract for institutional cash-yielding yield farm arbitrage.",
                    "retailPositioning": "Complete institutional alignment."
                },
                "riskMitigation": "Ultra-low-risk capital preservation bet with guaranteed high-yield redemption."
            }
        },
        {
            "id": "spt-m-05", "rank": 5,
            "title": "Will McLaren secure the Formula 1 World Constructors Championship before the final race?",
            "slug": "mclaren-secure-f1-constructors-championship-early",
            "volume": "$44,100,000", "volumeRaw": 44100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$9,700,000", "endDate": "Penultimate GP Finish",
            "outcomes": [{"name": "YES", "price": 0.78, "pct": 78}, {"name": "NO", "price": 0.22, "pct": 22}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 90, "evEdge": "+11.8% EV+", "impliedProb": 78, "fairValueProb": 88.5,
                "targetExit": "$0.93 (+19.2% gain)", "stopLoss": "$0.68",
                "macroStrategy": "McLaren averages 36.4 points per race weekend versus Ferrari's 29.1 and Red Bull's 21.8 (hampered by Sergio Pérez underperformance). The mathematical gap widens at approx +8.5 points per weekend.",
                "newsCatalyst": {
                    "headline": "BBC Sport F1: McLaren points trajectory guarantees constructors title clinch with one round to spare",
                    "source": "BBC Sport Paddock", "time": "4d ago", "impact": "TITLE CLINCH"
                },
                "socialMediaRadar": {
                    "platform": "F1 Technical / Motorsport Network",
                    "sentimentScore": 92, "sentimentTrend": "+22% Papaya coronation",
                    "whaleFlows": "Motorsport prop funds locking long McLaren championship contracts.",
                    "retailPositioning": "Consensus agreement; Perez struggles seal Red Bull defeat."
                },
                "riskMitigation": "Hold into the clinching race; redeem at $1.00."
            }
        },
        {
            "id": "spt-m-06", "rank": 6,
            "title": "Will Los Angeles Dodgers repeat as World Series favorites with implied odds >25% at month end?",
            "slug": "la-dodgers-world-series-favorites-implied-over-25",
            "volume": "$35,900,000", "volumeRaw": 35900000, "volumeLabel": "30-Day Volume",
            "liquidity": "$7,800,000", "endDate": "End of Month 11:59 PM EST",
            "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.2% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                "targetExit": "$0.88 (+18.9% gain)", "stopLoss": "$0.62",
                "macroStrategy": "Shohei Ohtani returning to dual-way pitching alongside Yoshinobu Yamamoto and Tyler Glasnow, paired with the league's top-3 batting wRC+, keeps the Dodgers perpetually priced at the top of Vegas boards.",
                "newsCatalyst": {
                    "headline": "Vegas Consensus Odds: Dodgers open at +350 (22.2% implied), steaming rapidly towards +280 on free agent additions",
                    "source": "Covers Sports Betting", "time": "3d ago", "impact": "VEGAS STEAM"
                },
                "socialMediaRadar": {
                    "platform": "MLB Twitter / Dodger Blue",
                    "sentimentScore": 88, "sentimentTrend": "+20% Dynasty status",
                    "whaleFlows": "Vegas sportsbook consensus consolidating around Dodgers dominance.",
                    "retailPositioning": "Global baseball public overwhelmingly backs LA."
                },
                "riskMitigation": "Steady institutional winner; exit upon $0.88 milestone."
            }
        },
        {
            "id": "spt-m-07", "rank": 7,
            "title": "Will Shai Gilgeous-Alexander surpass Nikola Jokic in NBA MVP odds ranking this month?",
            "slug": "shai-gilgeous-alexander-surpass-jokic-mvp-odds",
            "volume": "$31,400,000", "volumeRaw": 31400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$6,900,000", "endDate": "End of Month 11:59 PM EST",
            "outcomes": [{"name": "YES", "price": 0.44, "pct": 44}, {"name": "NO", "price": 0.56, "pct": 56}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+14.6% EV+", "impliedProb": 56, "fairValueProb": 68.5,
                "targetExit": "$0.72 (+28.5% gain on NO)", "stopLoss": "$0.44",
                "macroStrategy": "Jokic's historic triple-double pace (averaging 30-14-11) and #1 rank in PER, BPM, and VORP command an immovable voter preference. OKC's balanced team construct dilutes SGA's raw statistical dominance.",
                "newsCatalyst": {
                    "headline": "The Ringer NBA MVP Straw Poll: Jokic captures 76 out of 100 first-place voter ballots in mid-season snapshot",
                    "source": "The Ringer NBA Analytics", "time": "2d ago", "impact": "VOTER MONOPOLY"
                },
                "socialMediaRadar": {
                    "platform": "Hoops Twitter / Thinking Basketball",
                    "sentimentScore": 77, "sentimentTrend": "+19% Jokic statistical aura",
                    "whaleFlows": "Sports analytics funds taking NO on SGA flip, confirming Jokic voter lock.",
                    "retailPositioning": "Retail chasing OKC team record hype; individual metrics favor Jokic."
                },
                "riskMitigation": "Bet NO on SGA surpassing Jokic; capture significant 44% mispricing."
            }
        },
        {
            "id": "spt-m-08", "rank": 8,
            "title": "Will Alexander Volkanovski or Ilia Topuria headline the next major UFC stadium event?",
            "slug": "volkanovski-or-topuria-headline-ufc-spain",
            "volume": "$26,300,000", "volumeRaw": 26300000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,700,000", "endDate": "End of Month UFC Announcement",
            "outcomes": [{"name": "YES", "price": 0.81, "pct": 81}, {"name": "NO", "price": 0.19, "pct": 19}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 91, "evEdge": "+11.2% EV+", "impliedProb": 81, "fairValueProb": 91.5,
                "targetExit": "$0.94 (+16.0% gain)", "stopLoss": "$0.70",
                "macroStrategy": "Dana White and Hunter Campbell confirmed that negotiations for a 2025 Madrid / Sydney stadium showcase are in the final stages. Both fighters are medically cleared with zero contract disputes.",
                "newsCatalyst": {
                    "headline": "Ariel Helwani / The MMA Hour: UFC finalized preliminary agreement for Topuria vs Volkanovski 2 rematch",
                    "source": "The MMA Hour Exclusive", "time": "3d ago", "impact": "BOUT AGREEMENT"
                },
                "socialMediaRadar": {
                    "platform": "MMA Junkie / r/MMA & Dana White Feeds",
                    "sentimentScore": 92, "sentimentTrend": "+24% Bout certainty",
                    "whaleFlows": "Polymarket UFC market makers accumulating YES shares.",
                    "retailPositioning": "Universal excitement across the combat community."
                },
                "riskMitigation": "Hold into the official press conference announcement."
            }
        },
        {
            "id": "spt-m-09", "rank": 9,
            "title": "Will Luke Littler win the upcoming World Darts Championship?",
            "slug": "luke-littler-win-world-darts-championship",
            "volume": "$22,500,000", "volumeRaw": 22500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,900,000", "endDate": "Alexandra Palace Final",
            "outcomes": [{"name": "YES", "price": 0.42, "pct": 42}, {"name": "NO", "price": 0.58, "pct": 58}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.8% EV+", "impliedProb": 58, "fairValueProb": 67.5,
                "targetExit": "$0.73 (+25.8% gain on NO)", "stopLoss": "$0.46",
                "macroStrategy": "PDC Darts knockout format features extreme volatility with Humphries, van Gerwen, and Cross averaging 102+ three-dart averages. Individual title probability for any single player rarely exceeds 28% in field models.",
                "newsCatalyst": {
                    "headline": "PDC Darts Analytics: Luke Humphries posts tournament-leading 44.8% double checkout conversion rate",
                    "source": "PDC Darts Intelligence", "time": "4d ago", "impact": "FIELD DEPTH"
                },
                "socialMediaRadar": {
                    "platform": "Sky Sports Darts / UK Sports Twitter",
                    "sentimentScore": 48, "sentimentTrend": "-14% The field vs Littler",
                    "whaleFlows": "Professional UK betting syndicates laying Littler to back 'The Field'.",
                    "retailPositioning": "UK mainstream public obsessively backing teen sensation Littler."
                },
                "riskMitigation": "Bet NO on Littler winning outright; back the world-class field."
            }
        },
        {
            "id": "spt-m-10", "rank": 10,
            "title": "Will India reach the ICC Champions Trophy Final?",
            "slug": "india-reach-icc-champions-trophy-final",
            "volume": "$28,700,000", "volumeRaw": 28700000, "volumeLabel": "30-Day Volume",
            "liquidity": "$6,100,000", "endDate": "Tournament Semi-Finals",
            "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+13.1% EV+", "impliedProb": 69, "fairValueProb": 80.0,
                "targetExit": "$0.85 (+23.2% gain)", "stopLoss": "$0.56",
                "macroStrategy": "India's ODI top-order batting depth (Rohit Sharma, Shubman Gill, Virat Kohli) paired with Jasprit Bumrah's unmatched death bowling economy (3.84) guarantees deep knockout progression across subcontinental pitches.",
                "newsCatalyst": {
                    "headline": "ICC Match Preview: India enters tournament as #1 ranked ODI squad with 14 wins in last 16 fixtures",
                    "source": "ICC Media Release", "time": "5d ago", "impact": "ODI HEGEMONY"
                },
                "socialMediaRadar": {
                    "platform": "ESPNCricinfo / Cricket Twitter",
                    "sentimentScore": 89, "sentimentTrend": "+21% Dominant favorite status",
                    "whaleFlows": "Global cricket liquidity providers taking heavy yes exposure on Indian qualification.",
                    "retailPositioning": "Billion-strong supporter base backed by pure statistical dominance."
                },
                "riskMitigation": "Lock 60% position once India books their semi-final spot."
            }
        }
    ]
}
