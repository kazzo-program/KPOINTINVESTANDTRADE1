# -*- coding: utf-8 -*-
"""
Football - La Liga Polymarket Top 10 Markets (Day, Week, Month)
Covering top Spanish football fixtures (El Clásico, Madrid, Barcelona, Atleti), team props, player markets, and league standings.
With full Macro Hedge Fund Strategy, News Catalysts, and Social Media Radar.
"""

LA_LIGA_DATA = {
    "day": [
        {
            "id": "lal-d-01", "rank": 1,
            "title": "Will Real Madrid defeat Barcelona in tonight's El Clásico?",
            "slug": "real-madrid-defeat-barcelona-el-clasico-tonight",
            "volume": "$46,500,000", "volumeRaw": 46500000, "volumeLabel": "24H Volume",
            "liquidity": "$9,800,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.53, "pct": 53}, {"name": "NO", "price": 0.47, "pct": 47}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+13.7% EV+", "impliedProb": 53, "fairValueProb": 63.5,
                "targetExit": "$0.70 (+32.0% gain)", "stopLoss": "$0.39",
                "macroStrategy": "Hansi Flick's aggressive high-offside defensive trap (catching opponents offside 6.8 times per game) is extremely high-risk against the explosive recovery pace of Vinícius Júnior and Kylian Mbappé at the Santiago Bernabéu.",
                "newsCatalyst": {
                    "headline": "Marca: Ancelotti designs rapid vertical long-ball scheme to exploit Barcelona's halfway line defensive posture",
                    "source": "Marca Madrid Beat", "time": "1h 30m ago", "impact": "TACTICAL EXPLOITATION"
                },
                "socialMediaRadar": {
                    "platform": "El Chiringuito TV / X La Liga",
                    "sentimentScore": 81, "sentimentTrend": "+19% Bernabéu Clásico aura",
                    "whaleFlows": "Madrid and international whales accumulating YES contracts at 0.50-0.53.",
                    "retailPositioning": "Global public divided; high liquidity provides pristine execution."
                },
                "riskMitigation": "Lock 50% profit if Real Madrid takes the lead; hedge if Barcelona leads at half."
            }
        },
        {
            "id": "lal-d-02", "rank": 2,
            "title": "Will Kylian Mbappé score 2 or more goals in tonight's La Liga fixture?",
            "slug": "kylian-mbappe-score-2-plus-goals-tonight",
            "volume": "$28,400,000", "volumeRaw": 28400000, "volumeLabel": "24H Volume",
            "liquidity": "$6,100,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.41, "pct": 41}, {"name": "NO", "price": 0.59, "pct": 59}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 78, "evEdge": "+12.9% EV+", "impliedProb": 41, "fairValueProb": 49.5,
                "targetExit": "$0.60 (+46.3% gain)", "stopLoss": "$0.28",
                "macroStrategy": "Mbappé generates 4.6 shots per 90 and takes penalties for Real Madrid. In marquee prime-time fixtures against teams leaving space behind, Mbappé's multi-goal conversion probability exceeds 48%.",
                "newsCatalyst": {
                    "headline": "Diario AS: Mbappé clocked at 35.8 km/h in training sprints; fully motivated for signature Spanish display",
                    "source": "Diario AS Madrid", "time": "2h ago", "impact": "PEAK FORM"
                },
                "socialMediaRadar": {
                    "platform": "Mbappé Fan Hub / r/realmadrid",
                    "sentimentScore": 76, "sentimentTrend": "+17% Brace expectation",
                    "whaleFlows": "Sharp football prop syndicates taking 0.41 mispriced line on Mbappé 2+ goals.",
                    "retailPositioning": "Casual fans backing anytime goal; brace offers superior EV+ multiplier."
                },
                "riskMitigation": "Cash out if Mbappé scores in the first half (contract will surge to ~0.70)."
            }
        },
        {
            "id": "lal-d-03", "rank": 3,
            "title": "Will Lamine Yamal complete 4 or more successful dribbles tonight?",
            "slug": "lamine-yamal-complete-4-plus-dribbles-tonight",
            "volume": "$19,700,000", "volumeRaw": 19700000, "volumeLabel": "24H Volume",
            "liquidity": "$4,300,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.66, "pct": 66}, {"name": "NO", "price": 0.34, "pct": 34}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.4% EV+", "impliedProb": 66, "fairValueProb": 76.5,
                "targetExit": "$0.81 (+22.7% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Yamal leads all European top 5 leagues in successful 1v1 take-ons per 90 (4.82) with a 67% success rate. Opposing left-back Ferland Mendy concedes 3.1 take-on attempts per 90.",
                "newsCatalyst": {
                    "headline": "Mundo Deportivo: Hansi Flick gives Yamal green light for unrestricted right-wing 1v1 isolation play",
                    "source": "Mundo Deportivo Barcelona", "time": "2h 30m ago", "impact": "ISOLATION TACTIC"
                },
                "socialMediaRadar": {
                    "platform": "Barca Universal / La Liga Stat Leaders",
                    "sentimentScore": 86, "sentimentTrend": "+21% Yamal wizardry",
                    "whaleFlows": "Skill prop traders loading the Over on Yamal dribble volume.",
                    "retailPositioning": "Public captivated by teen prodigy's electric wing play."
                },
                "riskMitigation": "Track live Opta stats; cash out as soon as 4th dribble is recorded."
            }
        },
        {
            "id": "lal-d-04", "rank": 4,
            "title": "Will Atlético Madrid win with a clean sheet against Valencia tonight?",
            "slug": "atletico-madrid-win-clean-sheet-tonight",
            "volume": "$17,300,000", "volumeRaw": 17300000, "volumeLabel": "24H Volume",
            "liquidity": "$3,800,000", "endDate": "Tonight 8:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.59, "pct": 59}, {"name": "NO", "price": 0.41, "pct": 41}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.8% EV+", "impliedProb": 59, "fairValueProb": 69.5,
                "targetExit": "$0.75 (+27.1% gain)", "stopLoss": "$0.46",
                "macroStrategy": "Diego Simeone's Metropolitano fortress boasts the lowest xGA in Spain (0.58 per 90). Valencia ranks 19th in away goals scored (just 4 all season) and lacks central penetration to test Jan Oblak.",
                "newsCatalyst": {
                    "headline": "Superdeporte Valencia: Valencia traveling to Madrid missing starting striker and primary set-piece taker",
                    "source": "Superdeporte Valencian", "time": "3h ago", "impact": "VALENCIA ATTACK CRISIS"
                },
                "socialMediaRadar": {
                    "platform": "Atleti Francia / Colchonero Twitter",
                    "sentimentScore": 83, "sentimentTrend": "+19% Classic Cholo 1-0 or 2-0 lock",
                    "whaleFlows": "Spanish syndicates taking Atleti Win to Nil combo bets.",
                    "retailPositioning": "Strong backing for Simeone's defensive masterclass."
                },
                "riskMitigation": "Redeem early if Atleti leads 2-0 into the 75th minute."
            }
        },
        {
            "id": "lal-d-05", "rank": 5,
            "title": "Will Vinícius Júnior win the Official Man of the Match award tonight?",
            "slug": "vinicius-junior-man-of-the-match-tonight",
            "volume": "$14,600,000", "volumeRaw": 14600000, "volumeLabel": "24H Volume",
            "liquidity": "$3,200,000", "endDate": "Tonight 11:15 PM CET",
            "outcomes": [{"name": "YES", "price": 0.44, "pct": 44}, {"name": "NO", "price": 0.56, "pct": 56}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 79, "evEdge": "+12.7% EV+", "impliedProb": 44, "fairValueProb": 53.0,
                "targetExit": "$0.62 (+40.9% gain)", "stopLoss": "$0.32",
                "macroStrategy": "Vinícius averages 1.4 goal contributions against Barcelona across his career, notably netting a Clásico hat-trick in last season's Supercopa. Fan and expert MOTM voting overwhelmingly favors Brazilian star flair.",
                "newsCatalyst": {
                    "headline": "La Liga TV Preview: Vini Jr has won MOTM in 4 of his last 6 appearances at the Bernabéu",
                    "source": "La Liga Official Broadcast", "time": "3h 30m ago", "impact": "MOTM TRACK RECORD"
                },
                "socialMediaRadar": {
                    "platform": "Bailando Vini / Madrid X Hub",
                    "sentimentScore": 78, "sentimentTrend": "+18% Vini showcase hype",
                    "whaleFlows": "High-payout prop specialists backing Vinícius MOTM.",
                    "retailPositioning": "Retail split between Mbappé and Vini, creating EV discount on Vini."
                },
                "riskMitigation": "Exit if Vini is substituted before 75 minutes."
            }
        },
        {
            "id": "lal-d-06", "rank": 6,
            "title": "Will Barcelona score in both halves against Sevilla tonight?",
            "slug": "barcelona-score-both-halves-tonight",
            "volume": "$13,200,000", "volumeRaw": 13200000, "volumeLabel": "24H Volume",
            "liquidity": "$2,850,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.2% EV+", "impliedProb": 63, "fairValueProb": 73.0,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Hansi Flick's Barcelona is the most prolific scoring team in Europe, averaging 3.25 goals per game. They have scored in both halves in 10 out of their 13 competitive matches this season.",
                "newsCatalyst": {
                    "headline": "Sport.es: Lewandowski, Raphinha, and Yamal all start; Barcelona's first-half goal conversion reaches 68%",
                    "source": "Diario Sport Catalunya", "time": "4h ago", "impact": "ATTACKING JUGGERNAUT"
                },
                "socialMediaRadar": {
                    "platform": "Barca Blaugranes / Catalan Radio",
                    "sentimentScore": 85, "sentimentTrend": "+20% Ruthless attack consensus",
                    "whaleFlows": "Goal timing specialists backing Barcelona both halves.",
                    "retailPositioning": "Broad retail agreement with Flick's high-octane setup."
                },
                "riskMitigation": "Lock 50% profits once first-half goal is scored."
            }
        },
        {
            "id": "lal-d-07", "rank": 7,
            "title": "Will Athletic Bilbao defeat Real Sociedad in today's Basque Derby?",
            "slug": "athletic-bilbao-defeat-real-sociedad-basque-derby",
            "volume": "$15,400,000", "volumeRaw": 15400000, "volumeLabel": "24H Volume",
            "liquidity": "$3,300,000", "endDate": "Today 6:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.56, "pct": 56}, {"name": "NO", "price": 0.44, "pct": 44}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.9% EV+", "impliedProb": 56, "fairValueProb": 66.0,
                "targetExit": "$0.72 (+28.5% gain)", "stopLoss": "$0.42",
                "macroStrategy": "San Mamés atmosphere creates massive local intensity (+0.84 home goal differential). Nico and Iñaki Williams' double-flank transition breaks Real Sociedad's possession-based mid-block.",
                "newsCatalyst": {
                    "headline": "El Correo: Ernesto Valverde names full Basque gala XI with Nico Williams declared 100% fit",
                    "source": "El Correo Bilbao", "time": "4h 15m ago", "impact": "SAN MAMÉS STRENGTH"
                },
                "socialMediaRadar": {
                    "platform": "Athletic Club X / Basque Football Talk",
                    "sentimentScore": 81, "sentimentTrend": "+17% San Mamés roar",
                    "whaleFlows": "Regional Basque betting syndicates heavily backing Athletic Club.",
                    "retailPositioning": "Derby rivalry creates close odds, giving home side substantial EV."
                },
                "riskMitigation": "Hedge with draw if match is level at 75 minutes."
            }
        },
        {
            "id": "lal-d-08", "rank": 8,
            "title": "Will Robert Lewandowski score the opening goal of the match tonight?",
            "slug": "robert-lewandowski-score-opening-goal-tonight",
            "volume": "$11,900,000", "volumeRaw": 11900000, "volumeLabel": "24H Volume",
            "liquidity": "$2,550,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.38, "pct": 38}, {"name": "NO", "price": 0.62, "pct": 62}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 77, "evEdge": "+13.1% EV+", "impliedProb": 38, "fairValueProb": 46.5,
                "targetExit": "$0.55 (+44.7% gain)", "stopLoss": "$0.26",
                "macroStrategy": "Lewandowski has scored first in 6 of Barcelona's 11 league matches this campaign. His box movement on early low crosses (Raphinha/Balde) provides lethal conversion within the first 25 minutes.",
                "newsCatalyst": {
                    "headline": "Opta Jose: Lewandowski leads La Liga in first-goal match openers (6) and conversion inside six-yard box",
                    "source": "Opta Spanish Football", "time": "5h ago", "impact": "OPENER SPECIALIST"
                },
                "socialMediaRadar": {
                    "platform": "Lewy Goals / Barca Live",
                    "sentimentScore": 75, "sentimentTrend": "+16% First goalscorer pick",
                    "whaleFlows": "Sharp goalscorer syndicates buying Lewandowski first goal YES at 0.38.",
                    "retailPositioning": "Attractive odds profile with huge upside."
                },
                "riskMitigation": "Size moderately at 3% bankroll; binary outcome."
            }
        },
        {
            "id": "lal-d-09", "rank": 9,
            "title": "Will Girona take all 3 points at the Montilivi stadium today?",
            "slug": "girona-take-3-points-montilivi-today",
            "volume": "$10,500,000", "volumeRaw": 10500000, "volumeLabel": "24H Volume",
            "liquidity": "$2,300,000", "endDate": "Today 4:15 PM CET",
            "outcomes": [{"name": "YES", "price": 0.61, "pct": 61}, {"name": "NO", "price": 0.39, "pct": 39}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+12.1% EV+", "impliedProb": 61, "fairValueProb": 71.0,
                "targetExit": "$0.76 (+24.5% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Míchel's Girona side has rebounded with improved pressing rhythm and vertical line-breaking passes. Opponent Getafe has scored the fewest away goals in the division and concedes heavy territorial control.",
                "newsCatalyst": {
                    "headline": "L'Esportiu: Girona recovers key midfield pivots from injury; Montilivi sellout crowd announced",
                    "source": "L'Esportiu de Catalunya", "time": "5h 30m ago", "impact": "SQUAD RECOVERY"
                },
                "socialMediaRadar": {
                    "platform": "Girona FC English / Catalan Sports",
                    "sentimentScore": 80, "sentimentTrend": "+16% Montilivi home win",
                    "whaleFlows": "European syndicates backing Girona straight moneyline.",
                    "retailPositioning": "Public sentiment recovering on Girona form."
                },
                "riskMitigation": "Lock profit once Girona scores the opening goal."
            }
        },
        {
            "id": "lal-d-10", "rank": 10,
            "title": "Will over 5.5 Yellow Cards be shown in tonight's Seville Derby?",
            "slug": "over-55-yellow-cards-seville-derby-tonight",
            "volume": "$12,100,000", "volumeRaw": 12100000, "volumeLabel": "24H Volume",
            "liquidity": "$2,600,000", "endDate": "Tonight 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.72, "pct": 72}, {"name": "NO", "price": 0.28, "pct": 28}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.5% EV+", "impliedProb": 72, "fairValueProb": 83.0,
                "targetExit": "$0.88 (+22.2% gain)", "stopLoss": "$0.58",
                "macroStrategy": "The Gran Derbi (Sevilla vs Real Betis) is historically the most disciplinary-heavy fixture in European football, averaging 7.4 cards per match over the last 10 meetings. Appointed referee Mateu Lahoz disciple averages 5.8 cards per game.",
                "newsCatalyst": {
                    "headline": "Diario de Sevilla: Intense hostility surrounds derby buildup; both managers demand full physical commitment",
                    "source": "Diario de Sevilla Deportes", "time": "6h ago", "impact": "CARD FESTIVAL"
                },
                "socialMediaRadar": {
                    "platform": "Sevillismo / Beticos Twitter",
                    "sentimentScore": 88, "sentimentTrend": "+24% Yellow cards certainty",
                    "whaleFlows": "Card prop specialists pounding Over 5.5 booking points.",
                    "retailPositioning": "Complete consensus across Spanish football analysts."
                },
                "riskMitigation": "Cash out once 6th card is brandished (typically by 75th minute)."
            }
        }
    ],
    "week": [
        {
            "id": "lal-w-01", "rank": 1,
            "title": "Will Barcelona remain #1 in the La Liga table at the end of this matchweek?",
            "slug": "barcelona-remain-number-1-table-this-week",
            "volume": "$42,600,000", "volumeRaw": 42600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$9,200,000", "endDate": "Sunday 11:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.69, "pct": 69}, {"name": "NO", "price": 0.31, "pct": 31}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.6% EV+", "impliedProb": 69, "fairValueProb": 80.0,
                "targetExit": "$0.85 (+23.2% gain)", "stopLoss": "$0.56",
                "macroStrategy": "Barcelona holds a 3-point advantage and a staggering +21 goal difference cushion over Real Madrid. Even a draw in their fixture keeps them mathematically ahead of all contenders.",
                "newsCatalyst": {
                    "headline": "Mundo Deportivo: Hansi Flick has engineered the best 10-game league start in Barcelona modern history",
                    "source": "Mundo Deportivo Analysis", "time": "8h ago", "impact": "TABLE CUSHION"
                },
                "socialMediaRadar": {
                    "platform": "Barca Times / Spanish Football Pod",
                    "sentimentScore": 86, "sentimentTrend": "+21% Table leadership certainty",
                    "whaleFlows": "Institutional sports funds backing Barcelona table retention.",
                    "retailPositioning": "Strong retail backing backed by mathematical safety cushion."
                },
                "riskMitigation": "Hold into the weekend close; redeem at $1.00."
            }
        },
        {
            "id": "lal-w-02", "rank": 2,
            "title": "Will Real Madrid score 5 or more combined goals across their two league matches this week?",
            "slug": "real-madrid-score-5-plus-goals-this-week",
            "volume": "$29,300,000", "volumeRaw": 29300000, "volumeLabel": "7-Day Volume",
            "liquidity": "$6,400,000", "endDate": "Sunday 11:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.8% EV+", "impliedProb": 62, "fairValueProb": 72.5,
                "targetExit": "$0.78 (+25.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Real Madrid averages 2.7 goals per home match and faces high-line Barcelona followed by bottom-ranked Espanyol at the Bernabéu. Expected total goals across the two matches is 5.4.",
                "newsCatalyst": {
                    "headline": "Marca: Bellingham, Vinícius, Mbappé, and Rodrygo starting together in full attacking trident setup",
                    "source": "Marca Madrid Live", "time": "10h ago", "impact": "ATTACKING FORCE"
                },
                "socialMediaRadar": {
                    "platform": "Managing Madrid / Real Madrid TV",
                    "sentimentScore": 84, "sentimentTrend": "+19% Goal rush expectation",
                    "whaleFlows": "Syndicate bettors taking the Over on Madrid weekly team goals.",
                    "retailPositioning": "Widespread fan confidence in Galáctico frontline firepower."
                },
                "riskMitigation": "Cash out once 5th goal is scored across the two games."
            }
        },
        {
            "id": "lal-w-03", "rank": 3,
            "title": "Will Atlético Madrid concede 0 goals across this matchweek?",
            "slug": "atletico-madrid-concede-zero-goals-this-week",
            "volume": "$21,400,000", "volumeRaw": 21400000, "volumeLabel": "7-Day Volume",
            "liquidity": "$4,600,000", "endDate": "Sunday 10:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.54, "pct": 54}, {"name": "NO", "price": 0.46, "pct": 46}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 81, "evEdge": "+13.0% EV+", "impliedProb": 54, "fairValueProb": 63.5,
                "targetExit": "$0.70 (+29.6% gain)", "stopLoss": "$0.42",
                "macroStrategy": "Simeone's backline featuring Robin Le Normand and José María Giménez has kept clean sheets in 65% of domestic matches. Their weekend opponent ranks lowest in shots created from inside the penalty box.",
                "newsCatalyst": {
                    "headline": "Diario AS: Atleti's defensive structure registers fewest shots on target conceded (2.1/90) in all of Europe",
                    "source": "Diario AS Deportes", "time": "12h ago", "impact": "CLEAN SHEET MACHINE"
                },
                "socialMediaRadar": {
                    "platform": "Colchonero Talk / La Liga Stat Zone",
                    "sentimentScore": 80, "sentimentTrend": "+17% Simeone defensive masterclass",
                    "whaleFlows": "Clean sheet specialists accumulating Atleti zero-goals conceded prop.",
                    "retailPositioning": "Recognized defensive reputation across betting markets."
                },
                "riskMitigation": "Take profits when 1-0 or 2-0 victory is wrapped up."
            }
        },
        {
            "id": "lal-w-04", "rank": 4,
            "title": "Will Raphinha record 3 or more direct goal involvements (G/A) this week?",
            "slug": "raphinha-record-3-plus-goal-involvements-this-week",
            "volume": "$16,800,000", "volumeRaw": 16800000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,700,000", "endDate": "Sunday 11:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.48, "pct": 48}, {"name": "NO", "price": 0.52, "pct": 52}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "MODERATE CONVICTION",
                "confidencePct": 80, "evEdge": "+12.7% EV+", "impliedProb": 48, "fairValueProb": 57.0,
                "targetExit": "$0.67 (+39.5% gain)", "stopLoss": "$0.36",
                "macroStrategy": "Raphinha has been Europe's most in-form playmaker in Flick's system, tallying 12 goals and 9 assists in 15 appearances. Playing as a free central #10/left-winger, he generates 1.45 xGI per 90.",
                "newsCatalyst": {
                    "headline": "Cadena SER: Raphinha awarded captain's armband, leading team in high sprints and key passes",
                    "source": "Cadena SER Catalunya", "time": "14h ago", "impact": "CENTRAL HUB"
                },
                "socialMediaRadar": {
                    "platform": "Barca X / Fantasy La Liga",
                    "sentimentScore": 82, "sentimentTrend": "+18% Raphinha Ballon d'Or form",
                    "whaleFlows": "Player prop specialists taking the 0.48 underpriced line on Raphinha multi-involvement.",
                    "retailPositioning": "Public slow to adjust to Raphinha's monstrous statistical output under Flick."
                },
                "riskMitigation": "Lock profit if Raphinha registers 2 involvements in Match 1."
            }
        },
        {
            "id": "lal-w-05", "rank": 5,
            "title": "Will Real Betis climb into the European qualification positions (top 6) this week?",
            "slug": "real-betis-climb-top-6-this-week",
            "volume": "$14,100,000", "volumeRaw": 14100000, "volumeLabel": "7-Day Volume",
            "liquidity": "$3,100,000", "endDate": "Sunday 11:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.5% EV+", "impliedProb": 63, "fairValueProb": 73.0,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Manuel Pellegrini's Betis side has won 3 consecutive league matches and sits only 1 point behind 6th place. Opponents above them face tough away tests against Madrid and Bilbao.",
                "newsCatalyst": {
                    "headline": "ABC de Sevilla: Giovani Lo Celso in scintillating scoring form; Betis midfield dominating transition control",
                    "source": "ABC Sevilla Deportes", "time": "16h ago", "impact": "FORM RESURGENCE"
                },
                "socialMediaRadar": {
                    "platform": "Real Betis Official / Betisweb",
                    "sentimentScore": 81, "sentimentTrend": "+19% European charge",
                    "whaleFlows": "Spanish betting syndicates taking Betis matchweek progression.",
                    "retailPositioning": "Andalusian fans backing Pellegrini's consistency."
                },
                "riskMitigation": "Lock partial profits when Betis wins their weekend fixture."
            }
        },
        {
            "id": "lal-w-06", "rank": 6,
            "title": "Will Kylian Mbappé take sole lead in the Pichichi (La Liga Top Scorer) race this week?",
            "slug": "mbappe-take-sole-lead-pichichi-this-week",
            "volume": "$25,700,000", "volumeRaw": 25700000, "volumeLabel": "7-Day Volume",
            "liquidity": "$5,600,000", "endDate": "Sunday 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.38, "pct": 38}, {"name": "NO", "price": 0.62, "pct": 62}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.3% EV+", "impliedProb": 62, "fairValueProb": 74.5,
                "targetExit": "$0.78 (+25.8% gain on NO)", "stopLoss": "$0.48",
                "macroStrategy": "Robert Lewandowski currently holds a commanding 4-goal lead in the Pichichi standings (14 goals to Mbappé's 8). Even a multi-goal performance by Mbappé is unlikely to surpass Lewandowski within a single matchweek.",
                "newsCatalyst": {
                    "headline": "Opta Analyst: Lewandowski's 4-goal Pichichi buffer requires a historic 5-goal swing to flip in one week",
                    "source": "Opta La Liga Stat Bureau", "time": "18h ago", "impact": "LEADER CUSHION"
                },
                "socialMediaRadar": {
                    "platform": "La Liga TV / r/soccer",
                    "sentimentScore": 77, "sentimentTrend": "+20% Lewandowski safety margin",
                    "whaleFlows": "Sharp sports traders laying Mbappé Pichichi lead for the week.",
                    "retailPositioning": "Recreational public over-estimating single-week goal swing capability."
                },
                "riskMitigation": "Bet NO on Mbappé taking sole lead this week; capture 62% baseline edge."
            }
        },
        {
            "id": "lal-w-07", "rank": 7,
            "title": "Will Villarreal remain unbeaten at home (Estadio de la Cerámica) this matchweek?",
            "slug": "villarreal-remain-unbeaten-at-home-this-week",
            "volume": "$11,500,000", "volumeRaw": 11500000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,500,000", "endDate": "Saturday 8:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.74, "pct": 74}, {"name": "NO", "price": 0.26, "pct": 26}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.8% EV+", "impliedProb": 74, "fairValueProb": 85.0,
                "targetExit": "$0.88 (+18.9% gain)", "stopLoss": "$0.62",
                "macroStrategy": "Marcelino's Yellow Submarine has won 5 and drawn 2 of their home games this season. Ayoze Pérez and Álex Baena produce rapid counter-attacking combinations that overwhelm visiting mid-table teams.",
                "newsCatalyst": {
                    "headline": "Castellón Plaza: Marcelino has full squad available; Villarreal's home xG ranks #3 in La Liga",
                    "source": "Castellón Plaza Deportes", "time": "1d ago", "impact": "HOME FORTRESS"
                },
                "socialMediaRadar": {
                    "platform": "Submarino Amarillo X / Valencian Football",
                    "sentimentScore": 85, "sentimentTrend": "+18% Cerámica fortress",
                    "whaleFlows": "Handicap syndicates taking Villarreal 1X (win or draw) props.",
                    "retailPositioning": "Solid backing for Marcelino's organized unit."
                },
                "riskMitigation": "Low-risk capital preserver; cash out after home victory or draw."
            }
        },
        {
            "id": "lal-w-08", "rank": 8,
            "title": "Will La Liga Refereeing Committee issue a public VAR clarification statement this week?",
            "slug": "la-liga-refereeing-committee-var-clarification-week",
            "volume": "$9,700,000", "volumeRaw": 9700000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,100,000", "endDate": "Tuesday 2:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.9% EV+", "impliedProb": 65, "fairValueProb": 76.0,
                "targetExit": "$0.80 (+23.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Following contentious semi-automated offside calls and hand-ball interpretation disputes, the CTA (Comité Técnico de Árbitros) has scheduled a mandatory weekly media debrief releasing audio recordings.",
                "newsCatalyst": {
                    "headline": "RFEF Communications: CTA confirms weekly audio release protocol for controversial penalty and red card reviews",
                    "source": "RFEF Official Desk", "time": "1d ago", "impact": "SCHEDULED PROTOCOL"
                },
                "socialMediaRadar": {
                    "platform": "Archivo VAR / Carrusel Deportivo",
                    "sentimentScore": 84, "sentimentTrend": "+20% Audio release certainty",
                    "whaleFlows": "Institutional prop traders locking the scheduled RFEF protocol.",
                    "retailPositioning": "Widespread media focus on referee accountability."
                },
                "riskMitigation": "Hold into scheduled Tuesday RFEF press release."
            }
        },
        {
            "id": "lal-w-09", "rank": 9,
            "title": "Will Real Sociedad win back-to-back league matches this week?",
            "slug": "real-sociedad-win-back-to-back-matches-week",
            "volume": "$11,200,000", "volumeRaw": 11200000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,400,000", "endDate": "Sunday 9:00 PM CET",
            "outcomes": [{"name": "YES", "price": 0.42, "pct": 42}, {"name": "NO", "price": 0.58, "pct": 58}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+13.1% EV+", "impliedProb": 58, "fairValueProb": 68.0,
                "targetExit": "$0.72 (+24.1% gain on NO)", "stopLoss": "$0.45",
                "macroStrategy": "Imanol Alguacil's squad is battling Europa League fatigue and has only scored 11 goals in 12 league matches this season. Winning two games in 5 days with an xG of 0.92 per game is statistically improbable.",
                "newsCatalyst": {
                    "headline": "Noticias de Gipuzkoa: Real Sociedad struggling for cutting edge as striker rotation fails to ignite",
                    "source": "Noticias de Gipuzkoa", "time": "1d ago", "impact": "ATTACKING DROUGHT"
                },
                "socialMediaRadar": {
                    "platform": "Erreala X / Basque Football",
                    "sentimentScore": 46, "sentimentTrend": "-14% Fatigue realism",
                    "whaleFlows": "Quant syndicates taking NO on Sociedad winning both matches.",
                    "retailPositioning": "Casual fans overestimating Sociedad's recent form."
                },
                "riskMitigation": "Bet NO on back-to-back wins; cash out if Sociedad draws or loses either fixture."
            }
        },
        {
            "id": "lal-w-10", "rank": 10,
            "title": "Will over 26 total goals be scored across all 10 La Liga matches this weekend?",
            "slug": "over-26-total-goals-la-liga-weekend",
            "volume": "$13,600,000", "volumeRaw": 13600000, "volumeLabel": "7-Day Volume",
            "liquidity": "$2,950,000", "endDate": "Sunday 11:30 PM CET",
            "outcomes": [{"name": "YES", "price": 0.63, "pct": 63}, {"name": "NO", "price": 0.37, "pct": 37}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 85, "evEdge": "+12.4% EV+", "impliedProb": 63, "fairValueProb": 73.0,
                "targetExit": "$0.78 (+23.8% gain)", "stopLoss": "$0.50",
                "macroStrategy": "Barcelona (3.25 gpg) and Real Madrid (2.4 gpg) fixtures alone project over 7 combined goals. The current weekend card features 5 bottom-half defensive units facing top-heavy offenses, easily clearing 2.6 goals per game.",
                "newsCatalyst": {
                    "headline": "Opta Jose: La Liga 2024/25 goals per game tracking 12% higher than previous 3-year historical average",
                    "source": "Opta Spain Analytics", "time": "1d ago", "impact": "GOAL INFLATION"
                },
                "socialMediaRadar": {
                    "platform": "La Liga Gol / El Chiringuito",
                    "sentimentScore": 82, "sentimentTrend": "+17% Goals galore weekend",
                    "whaleFlows": "Multi-match goal accumulator funds taking Over 26.5 aggregate goals.",
                    "retailPositioning": "General public preference for entertainment and goals."
                },
                "riskMitigation": "Cash out once 27th goal is scored across the weekend slate."
            }
        }
    ],
    "month": [
        {
            "id": "lal-m-01", "rank": 1,
            "title": "Will Real Madrid win the La Liga Title 2024/25?",
            "slug": "real-madrid-win-la-liga-title-2025",
            "volume": "$72,100,000", "volumeRaw": 72100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$15,400,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.52, "pct": 52}, {"name": "NO", "price": 0.48, "pct": 48}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+13.9% EV+", "impliedProb": 52, "fairValueProb": 62.5,
                "targetExit": "$0.70 (+34.6% gain)", "stopLoss": "$0.38",
                "macroStrategy": "Real Madrid's unmatched squad depth across midfield (Camavinga, Valverde, Bellingham, Tchouaméni) and frontline provides immense second-half marathon endurance. Barcelona's thin squad depth and financial constraints will show fatigue during spring fixture congestion.",
                "newsCatalyst": {
                    "headline": "Opta Supercomputer La Liga Projections: Real Madrid projected champion in 58.2% of full-season simulations",
                    "source": "Opta Football Simulations", "time": "2d ago", "impact": "SIMULATION FAVORITE"
                },
                "socialMediaRadar": {
                    "platform": "El Chiringuito / Marca & AS Live",
                    "sentimentScore": 80, "sentimentTrend": "+17% Madrid marathon pedigree",
                    "whaleFlows": "European hedge funds accumulating Real Madrid title shares under 0.55.",
                    "retailPositioning": "Barcelona's early season hype created an attractive entry point for Madrid."
                },
                "riskMitigation": "Core position; rebalance after the second El Clásico at Montjuïc."
            }
        },
        {
            "id": "lal-m-02", "rank": 2,
            "title": "Will Robert Lewandowski win the Pichichi Trophy (Top Scorer)?",
            "slug": "robert-lewandowski-win-pichichi-trophy",
            "volume": "$58,400,000", "volumeRaw": 58400000, "volumeLabel": "30-Day Volume",
            "liquidity": "$12,600,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.76, "pct": 76}, {"name": "NO", "price": 0.24, "pct": 24}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 89, "evEdge": "+11.8% EV+", "impliedProb": 76, "fairValueProb": 87.0,
                "targetExit": "$0.91 (+19.7% gain)", "stopLoss": "$0.64",
                "macroStrategy": "Lewandowski has 14 league goals in 11 appearances with an unmatched individual xG of 1.14/90 in Flick's high-pressing vertical system. A 6-goal cushion over Mbappé provides immense statistical buffer.",
                "newsCatalyst": {
                    "headline": "Mundo Deportivo: Lewandowski on pace for 38-goal league campaign, shattering previous post-Messi scoring marks",
                    "source": "Mundo Deportivo Pichichi Track", "time": "3d ago", "impact": "SCORING BLITZ"
                },
                "socialMediaRadar": {
                    "platform": "Barca Blaugranes / La Liga Stat Leaders",
                    "sentimentScore": 91, "sentimentTrend": "+23% Pichichi lock",
                    "whaleFlows": "Institutional sports betting desks locking long Lewandowski Pichichi contracts.",
                    "retailPositioning": "Consensus agreement across European sports analysts."
                },
                "riskMitigation": "Safe, institutional-grade wager; hold into final weeks of the season."
            }
        },
        {
            "id": "lal-m-03", "rank": 3,
            "title": "Will Atlético Madrid secure a UEFA Champions League Berth (Top 4 Finish)?",
            "slug": "atletico-madrid-secure-top-4-champions-league",
            "volume": "$47,300,000", "volumeRaw": 47300000, "volumeLabel": "30-Day Volume",
            "liquidity": "$10,200,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.88, "pct": 88}, {"name": "NO", "price": 0.12, "pct": 12}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 94, "evEdge": "+7.5% EV+", "impliedProb": 88, "fairValueProb": 95.5,
                "targetExit": "$0.97 (+10.2% gain)", "stopLoss": "$0.80",
                "macroStrategy": "Diego Simeone has guided Atlético Madrid into the top 4 in all 12 of his full seasons as manager. With Julián Álvarez, Griezmann, and Le Normand, their wage bill and squad quality vastly dwarf 5th-placed Athletic Bilbao.",
                "newsCatalyst": {
                    "headline": "Diario AS: Atlético Madrid top-4 probability exceeds 96% in proprietary predictive club models",
                    "source": "Diario AS Analytics", "time": "3d ago", "impact": "HISTORIC CERTAINTY"
                },
                "socialMediaRadar": {
                    "platform": "Colchonero Live / Spanish Football Pod",
                    "sentimentScore": 95, "sentimentTrend": "+25% 12-year streak consensus",
                    "whaleFlows": "Arbitrage syndicates treating Atleti Top-4 as fixed-income yield instrument.",
                    "retailPositioning": "Complete alignment across world football."
                },
                "riskMitigation": "Ultra-low-risk capital preservation bet; redeem upon formal mathematical clinch."
            }
        },
        {
            "id": "lal-m-04", "rank": 4,
            "title": "Will Athletic Bilbao qualify for the UEFA Champions League spot (Top 4)?",
            "slug": "athletic-bilbao-qualify-champions-league-top-4",
            "volume": "$32,800,000", "volumeRaw": 32800000, "volumeLabel": "30-Day Volume",
            "liquidity": "$7,100,000", "endDate": "May 2025 Season Finale",
            "outcomes": [{"name": "YES", "price": 0.44, "pct": 44}, {"name": "NO", "price": 0.56, "pct": 56}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 83, "evEdge": "+13.8% EV+", "impliedProb": 44, "fairValueProb": 54.0,
                "targetExit": "$0.65 (+47.7% gain)", "stopLoss": "$0.32",
                "macroStrategy": "Spain is favored to receive a 5th Champions League spot via UEFA coefficient points. Ernesto Valverde's Bilbao side has the 3rd highest xG difference in Spain and San Mamés home form is imperious.",
                "newsCatalyst": {
                    "headline": "UEFA Coefficient Update: La Liga on track to secure bonus 5th Champions League qualification spot",
                    "source": "UEFA Club Competitions", "time": "4d ago", "impact": "EXTRA SPOT EXPANSION"
                },
                "socialMediaRadar": {
                    "platform": "San Mames Vibe / Basque Football",
                    "sentimentScore": 79, "sentimentTrend": "+19% Champions League dream",
                    "whaleFlows": "Sharp European sports syndicates taking Bilbao European qualification YES.",
                    "retailPositioning": "Public focuses only on top 3, underappreciating Bilbao's structural consistency."
                },
                "riskMitigation": "Lock 50% profits if Bilbao establishes a 5-point cushion over 6th place."
            }
        },
        {
            "id": "lal-m-05", "rank": 5,
            "title": "Will Hansi Flick win La Liga Manager of the Month award?",
            "slug": "hansi-flick-win-manager-of-the-month",
            "volume": "$23,500,000", "volumeRaw": 23500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,100,000", "endDate": "End of Month Award Announcement",
            "outcomes": [{"name": "YES", "price": 0.65, "pct": 65}, {"name": "NO", "price": 0.35, "pct": 35}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+12.4% EV+", "impliedProb": 65, "fairValueProb": 75.5,
                "targetExit": "$0.80 (+23.1% gain)", "stopLoss": "$0.52",
                "macroStrategy": "Barcelona's flawless 4-match winning streak, scoring 16 goals while conceding only 2 this month, makes Flick the overwhelming statistical frontrunner over Simeone and Ancelotti.",
                "newsCatalyst": {
                    "headline": "La Liga Official Awards Panel: Flick's goal differential record (+14) tops all monthly candidates",
                    "source": "La Liga Awards Bureau", "time": "4d ago", "impact": "AWARD FAVORITE"
                },
                "socialMediaRadar": {
                    "platform": "Barca Times / Spanish Football X",
                    "sentimentScore": 87, "sentimentTrend": "+22% Flick coronation",
                    "whaleFlows": "Award prop bettors accumulating Flick YES contracts.",
                    "retailPositioning": "Widespread fan excitement around Flick's transformation of Barcelona."
                },
                "riskMitigation": "Hold into scheduled award reveal on the first Friday of next month."
            }
        },
        {
            "id": "lal-m-06", "rank": 6,
            "title": "Will Lamine Yamal reach 15 or more total assists across all competitions this month?",
            "slug": "lamine-yamal-reach-15-plus-assists-this-month",
            "volume": "$20,100,000", "volumeRaw": 20100000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,400,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.58, "pct": 58}, {"name": "NO", "price": 0.42, "pct": 42}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.7% EV+", "impliedProb": 58, "fairValueProb": 68.0,
                "targetExit": "$0.73 (+25.8% gain)", "stopLoss": "$0.45",
                "macroStrategy": "Yamal currently sits at 12 assists and has 4 matches scheduled this month. In Flick's attack, Yamal averages 0.68 expected assists (xA) per 90, creating 3.8 big chances per fixture.",
                "newsCatalyst": {
                    "headline": "Mundo Deportivo: Yamal's trivela and inswinging cross conversion with Lewandowski at all-time high",
                    "source": "Mundo Deportivo Analytics", "time": "5d ago", "impact": "ASSIST PRODUCTION"
                },
                "socialMediaRadar": {
                    "platform": "Yamal Magic / r/Barca",
                    "sentimentScore": 85, "sentimentTrend": "+20% Assist milestone momentum",
                    "whaleFlows": "Player prop specialists taking YES on Yamal assist milestone.",
                    "retailPositioning": "Retail fascinated by the young star's world-class output."
                },
                "riskMitigation": "Cash out immediately upon the 15th assist."
            }
        },
        {
            "id": "lal-m-07", "rank": 7,
            "title": "Will Espanyol avoid the relegation zone throughout this calendar month?",
            "slug": "espanyol-avoid-relegation-zone-this-month",
            "volume": "$16,200,000", "volumeRaw": 16200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$3,500,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.37, "pct": 37}, {"name": "NO", "price": 0.63, "pct": 63}],
            "hedgeFundAdvisory": {
                "recommendation": "BET NO", "conviction": "HIGH CONVICTION",
                "confidencePct": 86, "evEdge": "+14.0% EV+", "impliedProb": 63, "fairValueProb": 75.0,
                "targetExit": "$0.79 (+25.4% gain on NO)", "stopLoss": "$0.50",
                "macroStrategy": "Espanyol has a brutal monthly schedule facing Barcelona, Atlético Madrid, and Girona. They currently sit just 1 point above the drop zone, with underlying xG metrics (-0.84 diff) ranking 19th in the division.",
                "newsCatalyst": {
                    "headline": "La Grada: Espanyol defensive injuries mount ahead of daunting derby and top-four fixtures",
                    "source": "La Grada Espanyol Beat", "time": "5d ago", "impact": "RELEGATION DANGER"
                },
                "socialMediaRadar": {
                    "platform": "Pericos Online / La Liga Relegation Watch",
                    "sentimentScore": 76, "sentimentTrend": "+21% Drop zone drop consensus",
                    "whaleFlows": "Relegation quants buying NO on Espanyol staying clear.",
                    "retailPositioning": "Retail underestimating the mathematical difficulty of Espanyol's schedule."
                },
                "riskMitigation": "Bet NO on Espanyol avoiding drop zone; cash out once they slip into bottom 3."
            }
        },
        {
            "id": "lal-m-08", "rank": 8,
            "title": "Will Real Madrid remain unbeaten in all home matches this month?",
            "slug": "real-madrid-remain-unbeaten-at-home-this-month",
            "volume": "$27,900,000", "volumeRaw": 27900000, "volumeLabel": "30-Day Volume",
            "liquidity": "$6,100,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.73, "pct": 73}, {"name": "NO", "price": 0.27, "pct": 27}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 88, "evEdge": "+12.1% EV+", "impliedProb": 73, "fairValueProb": 83.5,
                "targetExit": "$0.87 (+19.1% gain)", "stopLoss": "$0.60",
                "macroStrategy": "Real Madrid hasn't lost a domestic league fixture at the Santiago Bernabéu in over 18 months. Ancelotti's record of 24 wins and 4 draws over the last 28 home ties represents an 85.7% home win rate and 100% unbeaten rate.",
                "newsCatalyst": {
                    "headline": "Marca: Santiago Bernabéu home unbeaten streak hits 520 days across all domestic competitions",
                    "source": "Marca Madrid Records", "time": "6d ago", "impact": "BERNABÉU FORTRESS"
                },
                "socialMediaRadar": {
                    "platform": "Madridistas Global / Real Madrid TV",
                    "sentimentScore": 89, "sentimentTrend": "+21% Home fortress certainty",
                    "whaleFlows": "Sports funds backing Real Madrid home match retention.",
                    "retailPositioning": "Universal belief in Bernabéu invincibility."
                },
                "riskMitigation": "Lock winnings once the final home whistle blows."
            }
        },
        {
            "id": "lal-m-09", "rank": 9,
            "title": "Will Girona finish the month inside the Top 8 of the La Liga table?",
            "slug": "girona-finish-month-top-8",
            "volume": "$18,500,000", "volumeRaw": 18500000, "volumeLabel": "30-Day Volume",
            "liquidity": "$4,000,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.62, "pct": 62}, {"name": "NO", "price": 0.38, "pct": 38}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 84, "evEdge": "+12.5% EV+", "impliedProb": 62, "fairValueProb": 72.0,
                "targetExit": "$0.77 (+24.2% gain)", "stopLoss": "$0.48",
                "macroStrategy": "Girona is navigating the post-Champions League adaptation phase and their remaining monthly games are against 14th, 16th, and 18th placed opponents. Taking 7 points from 9 will cement their top-8 standing.",
                "newsCatalyst": {
                    "headline": "L'Esportiu: Míchel successfully rotates European and domestic squads with positive physical recovery data",
                    "source": "L'Esportiu Catalunya", "time": "6d ago", "impact": "SCHEDULE RELIEF"
                },
                "socialMediaRadar": {
                    "platform": "Girona FC Community / Catalan Sport",
                    "sentimentScore": 81, "sentimentTrend": "+17% Top 8 consolidation",
                    "whaleFlows": "Regional Catalan syndicates backing Girona table progress.",
                    "retailPositioning": "Steady confidence in Míchel's tactical acumen."
                },
                "riskMitigation": "Hold into the final match of the month."
            }
        },
        {
            "id": "lal-m-10", "rank": 10,
            "title": "Will Vinícius Júnior finish in the Top 3 of the La Liga goalscoring charts at month end?",
            "slug": "vinicius-junior-top-3-goalscoring-charts-month",
            "volume": "$24,200,000", "volumeRaw": 24200000, "volumeLabel": "30-Day Volume",
            "liquidity": "$5,300,000", "endDate": "End of Month 11:59 PM CET",
            "outcomes": [{"name": "YES", "price": 0.68, "pct": 68}, {"name": "NO", "price": 0.32, "pct": 32}],
            "hedgeFundAdvisory": {
                "recommendation": "BET YES", "conviction": "HIGH CONVICTION",
                "confidencePct": 87, "evEdge": "+12.2% EV+", "impliedProb": 68, "fairValueProb": 78.5,
                "targetExit": "$0.83 (+22.0% gain)", "stopLoss": "$0.54",
                "macroStrategy": "Vinícius currently sits tied for 2nd with Ayoze Pérez at 7 goals. With Real Madrid's favorable upcoming fixtures and Vini taking penalties alongside Mbappé, his top-3 position is statistically protected.",
                "newsCatalyst": {
                    "headline": "Diario AS: Vinícius conversion rate jumps to 24% as Ancelotti isolates him in one-on-one wide channels",
                    "source": "Diario AS Madrid", "time": "7d ago", "impact": "GOAL EFFICIENCY"
                },
                "socialMediaRadar": {
                    "platform": "Vini Jr Official / Real Madrid Zone",
                    "sentimentScore": 86, "sentimentTrend": "+20% Top-3 scorer certainty",
                    "whaleFlows": "Spanish prop funds locking Vini top-3 placement.",
                    "retailPositioning": "Complete alignment across Spanish and Brazilian supporters."
                },
                "riskMitigation": "Redeem upon completion of final matchday of the month."
            }
        }
    ]
}
