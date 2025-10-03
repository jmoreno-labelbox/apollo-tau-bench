from tau_bench.types import Action, Task

TASKS = [








Task(
  annotator="0",
  user_id="task_80",
  instruction=(
            "Acting as an MLB Analyst, identify Lightning (KC) pitchers with **high-grade** performance (A-/A/A+/B-/B/B+) for the week of 2025-08-10 and establish reinforcement targets. Propose multiple improvement objectives for the players."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [2,13]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "KC",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "ingestion_log_id": 16,
      "dev_report_id": [11,12,],
      "goal_id": [20,21]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_81",
  instruction=(
            "Function as an MLB Analyst and compile an opponent scouting report titled 'Opponent pitch strengths and attack tendencies' for the forthcoming Cyclones game after 2024-06-10 and determine the venue name. Produce an Opponent Analysis scouting report for the designated opponent, supported by high-grade pitch evidence (A−/A/A+) from that team's pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-MIL side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_82",
  instruction=(
            "In your role as MLB Analyst, provide a dual-sided pitch-quality comparison for the Lightning vs Cyclones matchup, highlighting A-tier pitches (A+/A/A−) for each team's pitching staff, and formulate development reports for all players, listed in ascending order based on their IDs."
        ),
  actions=[
    # Teams
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),  # treat as home for this comparison
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),  # CIN players
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),  # COL players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CLE A-tier
    
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="AddNewHighlight", kwargs={
    #   "name": "Lightning vs Cyclones Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Lightning",
      "away_team": "Cyclones",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "Cyclones" : [
                    {
                    "grade_id": 3,
                    "pitch_id": 2,
                    "game_pk": 2024000007,
                    "intended_quadrant_model": 6,
                    "actual_quadrant": 7,
                    "miss_distance_inches": 5.37,
                    "execution_grade": "A"
                    }
                ],
        "Lightning":[
                    {
                    "grade_id": 11,
                    "pitch_id": 5,
                    "game_pk": 2024000007,
                    "intended_quadrant_model": 9,
                    "actual_quadrant": 1,
                    "miss_distance_inches": 0.46,
                    "execution_grade": "A+"
                    }
                ]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_83",
  instruction=(
            "As an MLB Analyst, evaluate Cyclones (MIL) pitcher Evelyn Martin’ pitches that are rated low (F and D). Present a highlight collection titled 'Cyclones bad pitches: Evelyn Martin' and draft a new development goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_84",
  instruction=(
            "In your capacity as an MLB Analyst, generate insights to Audit pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week of 2025-08-10 focused on 'Fastball–breaker' (2.3). Create a concise development goal and a 5-clip highlight."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_85",
  instruction=(
            "As a MLB Analyst, you need to compile an opponent scouting report, titled 'Opponent pitch strengths and attack tendencies', for the upcoming Cyclones game following 2024-07-20. Include the venue name. Present an Opponent Analysis scouting report for the chosen opponent, grounded in high-grade pitch data (A−/A/A+) from that team’s pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_86",
  instruction=(
            "Assuming the role of a MLB Analyst, compile an opponent scouting report titled 'Opponent pitch strengths and attack tendencies' for the subsequent Cyclones game post-2024-06-10 and provide the venue name. Submit an Opponent Analysis scouting report for the selected opponent, based on high-grade pitch evidence (A−/A/A+) from the team's pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-MIL side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_87",
  instruction=(
            "In your capacity as a MLB Analyst, examine the Lightning pitcher Isabella Davis by collecting all of her pitch grades, pinpoint the pitches with lower grades, and create analyst outputs: initialize a highlights reel titled 'Lightning bad pitches: Isabella Davis' using the poorly-graded pitches (F/D/C+/C-/C) with 6 clips. File a development report and include a coaching goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_88",
  instruction=(
            "Your task as a MLB Analyst is to evaluate pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week starting 2025-08-10, with a review on 2025-09-07, focusing on 'Fastball–breaker' (1.3). Measure how effectively the fastball complements the primary breaker within the decision window. Offer a brief scouting note with one development goal and create a 5-clip highlight montage titled 'Falcons tunneling audit: Sarah Williams'."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "ingestion_id": 16,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_89",
  instruction=(
            "As a MLB Analyst, you are to prepare an opponent scouting report called 'Opponent pitch strengths and attack tendencies' for the following Cyclones game after 2024-06-10, and specify the venue name. Provide an Opponent Analysis scouting report for the detailed opponent, supported by high-grade pitch data (A−/A/A+) from that team's pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-MIL side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_90",
  instruction=(
            "As a MLB Analyst, your goal is to examine Lightning pitcher James Brown by collecting all of his pitch grades, pinpoint the poorly graded pitches, and generate analyst deliverables: start a highlights reel named 'Lightning bad pitches: James Brown' using the pitches graded F and D, with 6 clips included, and compose a development report and attach a coaching goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "James Brown"}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [8]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [3,12,36,50],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 8, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: James Brown",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal for bad-graded set
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 8,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_91",
  instruction=(
            "As a MLB Analyst, your task is to evaluate Cyclones (MIL) pitcher Evelyn Martin' **low-grade cohort** (F and D) for the date 2025-08-10. Produce a highlight collection titled 'Cyclones bad pitches: Evelyn Martin'; and set up a new development goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_92",
  instruction=(
            "Being a MLB Analyst, your objective is to construct an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game following 2024-06-10 and provide the venue name. Compile an Opponent Analysis scouting report for the chosen opponent, based on high-grade pitch performance (A−/A/A+) from that team's pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_93",
  instruction=(
            "As a MLB Analyst, you are to create an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the forthcoming Cyclones game subsequent to 2024-07-20 and include the venue name. Produce an Opponent Analysis scouting report for the opponent's identified pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 10}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 10}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_94",
  instruction=(
            "As a MLB Analyst, your aim is to evaluate Lightning (STL) pitcher Isabella Davis's pitching performance for the week beginning 2025-08-10. Grade the ungraded pitches by comparing intended (5) versus actual quadrant (7) and calculating the miss distance (2.2), which results in a representative grade (B+). Deliver a concise scouting package: a montage of 6 clips titled 'Scott - Analysis', and establish a new goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Isabella Davis"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Isabella Davis
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 25,
        "game_pk": 2024000007,
        "intended_quadrant_model": 5,
        "actual_quadrant": 7,
        "miss_distance_inches": 2.2,
        "execution_grade": "B+"
      },
    ),

    # # WRITE: Initialize a K-montage highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "graded_pitch_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Scott - Analysis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_95",
  instruction=(
            "As an MLB Analyst, identify Lightning (KC) pitchers who demonstrated **high-grade** performance (A-/A/A+/B-/B/B+) during the week of 2025-08-10 and develop reinforcement objectives. Formulate several improvement targets for these players."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [2,13]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "KC",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": [11,12,],
      "goal_id": [20,21]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_96",
  instruction=(
            "Function as an MLB Analyst to compose an opponent scouting report titled 'Opponent pitch strengths and attack tendencies' for the next Cyclones game following 2024-07-20 and include the venue name. Present an Opponent Analysis scouting report for the designated opponent, based on high-grade pitch evidence (A−/A/A+) sourced from that team's pitchers."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_97",
  instruction=(
            "Take on the role of an MLB Analyst to generate an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game (away) post-2024-08-30 and specify the venue name. Provide an Opponent Analysis scouting report focusing on the selected opponent's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetTeamDetailsById", kwargs={"team_id":6}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 6}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [11]}),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [13,14,38]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_98",
  instruction=(
            "Act as an MLB Analyst to evaluate all pitch grades for Lightning pitcher James Brown, identifying the (D, B-) graded pitches, and generate analyst conclusions: create a highlights reel titled 'Lightning bad pitches: James Brown' with 5 clips and draft a development report featuring a development goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_99",
  instruction=(
            "Operate as an MLB Analyst to assess Lightning (STL) pitcher Isabella Davis’s average-grade pitches (C+) throughout the week of 2025-08-10. Intend to produce a highlight set named 'Lightning pitches: Isabella Davis' with 6 clips per pitch, showcasing the consistent patterns from the C+ category; complete a development report with a specified goal."
        ),
  actions=[
    # Start from get details by name
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Lightning pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "goal_id": 20,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_100",
  instruction=(
            "As an MLB Analyst, your role is to generate new insights into Audit pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week of 2025-08-10 for 'Fastball–breaker' (2.3). Formulate a clear development goal and provide a 5-clip highlight."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),

Task(
  annotator="0",
  user_id="task_01",
  instruction=(
            "Acting as an MLB Analyst, aim to Assess the Cyclones (MIL) roster, focusing on Evelyn Martin for the week of 2025-08-10. Supply a compact scouting package: a curated highlight set titled 'Cyclones roster focus' (3 clips), and devise a new improvement goal."
        ),
  actions=[
    # Start from get details by name (team), then proceed
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Cyclones"},
    ),
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 8},
    ),
    # Confirm focal player by exact name
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Evelyn Martin"},
    ),

    

    # WRITE: Log supporting data ingestion
    


    # WRITE: File   dev report for Evelyn Martin
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 1,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel context for this study
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Cyclones roster focus",
        "clip_count": 3,
        "report_id": 11
      },
    ),

    

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Track this analysis as a workflow run
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),

  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones roster focus",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 3,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),

Task(
  annotator="0",
  user_id="task_02",
  instruction=(
            "In the capacity of an MLB Analyst, your objective is to Review the Cyclones (COL) roster with a spotlight on Alexander Taylor for the week of 2025-08-10. Assemble a concise scouting package: present a curated highlight set titled 'Cyclones roster focus' (4 clips), along with a player-development goal."
        ),
  actions=[
    # Start from get details by name (team)
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Cyclones"},
    ),
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 10},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Alexander Taylor"},
    ),

    # WRITE: Log supporting data ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Alexander Taylor
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Cyclones roster focus",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 7,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "player": "Alexander Taylor",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones roster focus",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 4,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_03",
  instruction=(
            "Being an MLB Analyst, your task is to summarize all details for the game that was cancelled in Denver on 2024-07-28, including player information from both teams and umpire details within a 'Cancelled-Game' scouting report, with 'Game Cancelled' and a 5-clip highlight named 'Match Cancelled'."
        ),
  actions=[
    # Venue + games on the date
    Action(name="GetAllVenueInCity", kwargs={"city": "Denver"}),
    Action(name="FindGamesOnDate", kwargs={"date": "2024-07-28"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Resolve the specific game at any Portland venue
    # (Pick the first game whose venue_id is in the Portland venue list)
    Action(
      name="GetTeamDetailsById",
      kwargs={"team_id": 7},
    ),
    Action(
      name="GetTeamDetailsById",
      kwargs={"team_id": 6},
    ),

    # Rosters for both sides
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 7},
    ),
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 6},
    ),

    # Umpire model calibration for the selected game
    Action(
      name="GetModelDetailByGame",
      kwargs={"game_pk": 2024000001},
    ),
    Action(
      name="GetUmpiresDetailsById",
      kwargs={"umpire_id": 8},
    ),

    # Evidence logs per policy (roster/lookup → snowflake; model/video context → hawkeye)
    

    # Scouting report + highlights
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Cancelled-Game",
        "game_pk": 2024000001,
        "core_narrative_text": "Game Cancelled"
      },
    ),

    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Match Cancelled",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "city": "Denver",
      "date": "2024-07-28",
      "home_team": "Falcons",
      "away_team": "Falcons",
      "game_pk": 2024000001,
      "umpire_name": "William Anderson",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "s3_pdf_path": "s3://reports/scouting/13.pdf",
      "playlist_name": "Game Highlights - Match Cancelled",
      "clip_count": 5,
      "players_of_team":[{
          "team_id":7,
          "players":[
                            {
                              "player_id": 5,
                              "full_name": "Sarah Williams",
                              "primary_position": "CF",
                              "batting_handedness": "S",
                              "throwing_handedness": "R",
                              "current_team_id": 7,
                              "roster_status": "Active"
                            },
                            {
                              "player_id": 14,
                              "full_name": "Henry Williams",
                              "primary_position": "LF",
                              "batting_handedness": "L",
                              "throwing_handedness": "R",
                              "current_team_id": 7,
                              "roster_status": "IL-15"
                            }
                          ]},
      {
          "team_id":6,
          "players":[
                            {
                              "player_id": 11,
                              "full_name": "Oliver Thompson",
                              "primary_position": "LF",
                              "batting_handedness": "R",
                              "throwing_handedness": "R",
                              "current_team_id": 6,
                              "roster_status": "Active"
                            }
                          ]}],
    
    }
  ],
),
Task(
  annotator="0",
  user_id="task_04",
  instruction=(
            "As an MLB Analyst, you should Examine the Falcons (CIN) roster context focusing on Sarah Williams, and generate analyst outputs: initiate a highlights reel with 5 clips titled 'Falcons roster focus' and compile a development report featuring a development goal."
        ),
  actions=[
    # Start from get details by name (team)
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Falcons"},
    ),
    # Action(
    #   name="GetAllPlayersOfTeam",
    #   kwargs={"team_id": 7},
    # ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Sarah Williams"},
    ),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    # WRITE: Log supporting data ingestion


    # WRITE:   dev report for Sarah Williams
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Falcons roster focus",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 5,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Falcons roster focus",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_05",
  instruction=(
            "As an MLB Analyst, you aim to evaluate the pitch mix and execution during the week of 2025-08-10 for Cyclones (COL) pitcher Alexander Taylor. Compose a 4-clip montage titled 'Cyclones pitch study: Alexander Taylor'; include a development note with a new goal, and add a representative execution-grading entry for one pitch (with smallest pitch id) from this period to support the assessment. The intended quadrant model was 3 while the actual quadrant was 2, with a miss distance of 1.4 inches, resulting in an execution grade of A."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "COL"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Alexander Taylor"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [7]},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting pitch ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Alexander Taylor
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade one representative pitch from the dataset
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 6,
        "game_pk": 2024000007,
        "intended_quadrant_model": 3,
        "actual_quadrant": 2,
        "miss_distance_inches": 1.4,
        "execution_grade": "A"
      },
    ),

    # # WRITE: Initialize a highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Cyclones pitch study: Alexander Taylor",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 7,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "player": "Alexander Taylor",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "graded_pitch_id": 6,
      "playlist_name": "Game Highlights - Cyclones pitch study: Alexander Taylor",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 4,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_06",
  instruction=(
            "As an MLB Analyst, your task is to prepare a game-level pitch analysis and summary highlights for the match between the MIL at home and the PIT. Deliver an opponent-ready scouting note titled 'Game Summary' and a game summary montage named 'MIL vs PIT – Pitch Log Summary' with 5 clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_07",
  instruction=(
            "In your role as an MLB Analyst, assess Lightning (STL) pitcher Isabella Davis's pitches for the week of 2025-08-10. Grade all the ungraded pitches with the intended quadrant (5) versus the actual quadrant (7) and a miss distance (2.2) that results in a representative grade (B+). Deliver a compact scouting package: a 6-clip montage titled 'Scott - Analysis', and create a new goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Isabella Davis"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 25,
        "game_pk": 2024000007,
        "intended_quadrant_model": 5,
        "actual_quadrant": 7,
        "miss_distance_inches": 2.2,
        "execution_grade": "B+"
      },
    ),

    # # WRITE: Initialize a K-montage highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "graded_pitch_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Scott - Analysis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),

Task(
  annotator="0",
  user_id="task_08",
  instruction=(
            "As an MLB Analyst, evaluate all pitches by Falcons (CIN) pitcher Sarah Williams and deliver a highlight set titled 'Falcons best pitches: Sarah Williams' showcasing 'A' grade pitches, alongside a development note with the goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Falcons"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Sarah Williams"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [5]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A"]}
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # # WRITE: Log supporting aggregation/ingestion for this grade review
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Falcons best pitches: Sarah Williams",
        "clip_count": 1,
        "report_id": 11
      },
    ),

    # # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 5,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Falcons best pitches: Sarah Williams",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_09",
  instruction=(
            "As an MLB Analyst, analyze all pitch grades for Lightning pitcher James Brown and identify the pitches graded as (D, B-). Produce analyst outputs by initiating a highlights reel named 'Lightning bad pitches: James Brown' with 5 clips and filing a development report with a development goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_10",
  instruction=(
            "As an MLB Analyst, your task is to Profile the Lightning (STL) pitcher Isabella Davis's average-grade pitches (C+) during the week of 2025-08-10. You should develop a highlight set titled 'Lightning pitches: Isabella Davis' with 6 clips per pitch, demonstrating consistent patterns from the C+ category; and file a report focused on development with a specific goal."
        ),
  actions=[
    # Start from get details by name
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Lightning pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "goal_id": 20,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_11",
  instruction=(
            "As an MLB Analyst, your task is to Surface the Cyclones (MIL) low-grade pitches with grades (D/F) and establish improvement goals for the athletes."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["D", "F"]},
    ),

    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 4,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": [11,12],
      "goal_id": [20,21]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_12",
  instruction=(
            "As an MLB Analyst, your task is to Analyze the Falcons pitcher Sarah Williams by collecting all her pitch grades, identify the highest-graded pitches, and create analyst outputs: prepare a highlights reel named 'Falcons best pitches: Sarah Williams' featuring the top-graded pitches (A+ and A) and establish a new goal for the player."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A+","A"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons best pitches: Sarah Williams",
      "clip_count": 1,
      "report_id": 11
    }),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 5,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id":20,
      "playlist_name": "Game Highlights - Falcons best pitches: Sarah Williams",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_13",
  instruction=(
            "As an MLB Analyst, your task is to Analyze the Lightning pitcher James Brown by acquiring all his pitch grades, recognize the poorly-graded pitches, and generate analyst outputs: create a highlights reel named 'Lightning bad pitches: James Brown' featuring the poor-grade pitches (F and D) with 6 clips, and produce a development report and specify a coaching goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "James Brown"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [8]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [3,12,36,50],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 8, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: James Brown",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal for bad-graded set
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 8,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_14",
  instruction=(
            "As an MLB Analyst, your task is to Review Cyclones (MIL) pitcher Evelyn Martin' **low-grade cohort** (F and D) as of 2025-08-10. Create a highlight set titled 'Cyclones bad pitches: Evelyn Martin'; and set a new development goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_15",
  instruction=(
            "As a MLB Analyst, your goal is to Examine the Lightning pitcher Isabella Davis by collecting all of her pitch grades, determining the poorly-rated pitches, and generate analyst reports: create a highlights reel titled 'Lightning bad pitches: Isabella Davis' featuring the low-graded pitches (F/D/C+/C-/C) with 6 clips, compiling a development report and include a coaching strategy."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_16",
  instruction=(
            "Acting as a MLB Analyst, aim to Compile an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-07-20 and provide the venue name. Generate an Opponent Analysis scouting report for the specified opponent, supported by top-grade pitch data (A−/A/A+) from that team’s pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_17",
  instruction=(
            "In your role as a MLB Analyst, your task is to Pinpoint Cyclones (MIL) pitchers with **high-grade** performance (A-/A/A+/B-/B/B+) during the week of 2025-08-10 and outline a progress goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    # 

    # # # High-grade include list (keep only A/B tiers)
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),

    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
    }
  ],
),
Task(
  annotator="0",
  user_id="task_18",
  instruction=(
            "Serving as a MLB Analyst, your responsibility is to Highlight Lightning (KC) pitchers with **high-grade** execution (A-/A/A+/B-/B/B+) for the week of 2025-08-10 and establish reinforcement targets. Provide advancement goals for every player."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [2,13]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "KC",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": [11,12,],
      "goal_id": [20,21]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_19",
  instruction=(
            "In your capacity as a MLB Analyst, aim to Formulate an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game after 2024-08-30 and provide the venue name. Create an Opponent Analysis scouting report for the recognized opponent's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-08-30", "team_id": 7}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="GetTeamDetailsById", kwargs={"team_id":6}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 6}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [11]}),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [13,14,38]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_20",
  instruction=(
            "As a MLB Analyst, ensure to provide a comparative analysis of pitch quality from both sides for the Lightning vs Cyclones matchup. Highlight A-tier pitches (A+/A/A−) for each team's pitching staff, and compile development reports for all players in ascending order of their ids."
        ),
  actions=[
    # Teams
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),  # treat as home for this comparison
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),  # CLE players
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),  # MIN players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CIN A-tier
    
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="AddNewHighlight", kwargs={
    #   "name": "Lightning vs Cyclones Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Lightning",
      "away_team": "Cyclones",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "player_1_dev_report": 11,
      "player_2_dev_report": 12,
      "player_4_dev_report": 13,
      "player_13_dev_report": 14,
      "Cyclones" : [
                    {
                    "grade_id": 3,
                    "pitch_id": 2,
                    "game_pk": 2024000007,
                    "intended_quadrant_model": 6,
                    "actual_quadrant": 7,
                    "miss_distance_inches": 5.37,
                    "execution_grade": "A"
                    }
                ],
    "Lightning":[
                {
                "grade_id": 11,
                "pitch_id": 5,
                "game_pk": 2024000007,
                "intended_quadrant_model": 9,
                "actual_quadrant": 1,
                "miss_distance_inches": 0.46,
                "execution_grade": "A+"
                }
            ]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_21",
  instruction=(
            "Assuming the role of a MLB Analyst, assess the low-graded (F and D) pitches of Cyclones (MIL) pitcher Evelyn Martin. Present a highlight set named 'Cyclones bad pitches: Evelyn Martin' and define a new development goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_22",
  instruction=(
            "Take on the role of MLB Analyst to generate fresh insight on pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week of 2025-08-10, focusing on 'Fastball–breaker' (2.3). Formulate a clear development goal and compile a 5-clip highlight."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_23",
  instruction=(
            "In your capacity as a MLB Analyst, compile a comprehensive pitch analysis and summarize highlights for the game between MIL hosting PIT on 2024-03-05. Prepare a scouting note 'Game Summary' ready for opponents and curate a game summary montage titled 'MIL vs PIT – Pitch Log Summary' with 5 clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),

    


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_24",
  instruction=(
            "Your task as a MLB Analyst is to assemble an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game following 2024-06-10, including the venue name. Deliver an Opponent Analysis scouting report for the identified opponent, filtered for high-grade pitches of levels (A−/A/A+) from that opponent."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-MIL side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_25",
  instruction=(
            "You are a MLB Analyst and you intend to Compile an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game following 2024-06-10 and provide the venue name. Create an Opponent Analysis scouting report for the specified opponent by examining their pitches"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 6}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 7}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 7}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5,14]}),


    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004,}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CHC",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [11,16,20,26,35,48,53,58]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_26",
  instruction=(
            "You are a MLB Analyst and you aim to Develop an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game after 2024-07-20 and mention the venue name. Produce an Opponent Analysis scouting report for the determined opponent, supported by top-tier pitch evidence (A−/A/A+) from that team's pitches"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_27",
  instruction=(
            "You are a MLB Analyst and you plan to Create an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game after 2024-07-20 and provide the venue name. Generate an Opponent Analysis scouting report for the identified opponent's pitches"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 10}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 10}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [6,8,31,39,40,41,42,44,46,55,57,61]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_28",
  instruction=(
            "You are a MLB Analyst and your task is to Evaluate pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week of 2025-08-10 (review on 2025-09-07) for 'Fastball–breaker' (1.3), assessing how effectively the fastball complements the primary breaker within the decision window. Deliver a precise scouting note with one development objective and highlights accompanied by a 5-clip montage titled 'Falcons tunneling audit: Sarah Williams'"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_29",
  instruction=(
            "You are a MLB Analyst and you need to Formulate an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game after 2024-08-30 and specify the venue name. Produce an Opponent Analysis scouting report for the identified opponent's pitches"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetTeamDetailsById", kwargs={"team_id":6}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 6}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [11]}),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [13,14,38]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_30",
  instruction=(
            "As an MLB Analyst, you aim to generate a game-level pitch analysis and summary for the match where the Cyclones host the Cyclones. Provide a scouting report 'Game Summary' that is ready for the opponent, and create a game summary montage titled 'MIL vs PIT – Pitch Log Summary' including 5 clip highlights."
        ),
  actions=[
    # Teams & game context
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),     # home
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),  # away
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "s3_pdf_path": "s3://reports/scouting/13.pdf",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_31",
  instruction=(
            "Acting as an MLB Analyst, your task is to compile an opponent scouting report titled 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game happening after 2024-07-20, including the venue name. Submit an Opponent Analysis scouting report focused on the identified opponent, bolstered by high-grade pitch data (A−/A/A+) from pitches of that team."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),
    
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_32",
  instruction=(
            "Functioning as an MLB Analyst, intend to fabricate a detailed game-level pitch analysis and summary highlights for the game between MIL playing at their home against the PIT. Present an opponent-prepared scouting note 'Game Summary' and a game summary video titled 'MIL vs PIT – Pitch Log Summary' featuring 5 clip highlights."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_33",
  instruction=(
            "As someone analyzing MLB, you are to orchestrate a comprehensive game-level pitch analysis and summary highlights for the match where the Cyclones host COL. Offer a scouting note 'Game Summary' suitable for the opponent, and compose a game summary montage with the title 'LAD vs COL – Pitch Log Summary' including 5 clip highlights."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "LAD"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "COL"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 1, "away_id": 10},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000007},
    ),

    # # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000007,
        "core_narrative_text": "LAD vs COL – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "LAD vs COL – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000007,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000007,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - LAD vs COL – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_34",
  instruction=(
            "In your role as an MLB Analyst, set out to create a thorough game-level pitch analysis and highlight summary for the match where MIL is at home playing against the Cyclones. Deliver a scouting report 'Game Summary' prepared for the opponent and a game summary compilation titled 'MIL vs PIT – Pitch Log Summary' including 5 clip highlights."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_35",
  instruction=(
            "As an MLB Analyst, your task is to craft a game-level pitch analysis and highlight summary for the match where the Cyclones host the PIT. Provide an opponent-ready scouting note titled 'Game Summary' and produce a game summary montage called 'MIL vs PIT – Pitch Log Summary' including 5 clip highlights"
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_36",
  instruction=(
            "As an MLB Analyst, your objective is to compile an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game following 2024-07-20 and include the venue name. Submit an Opponent Analysis scouting report for the specific opponent, supported by top-tier pitch evidence (A−/A/A+) from that team's pitchers"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_37",
  instruction=(
            "Acting as an MLB Analyst, you should compile an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the forthcoming Falcons game post 2024-08-30 and provide the venue name. Submit an Opponent Analysis scouting report focusing on the identified opponent's pitching strategies."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetTeamDetailsById", kwargs={"team_id":6}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 6}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [11]}),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids":[13,14,38]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_38",
  instruction=(
            "In your role as an MLB Analyst, analyze Lightning pitcher Isabella Davis by collecting all her pitch grades, pinpointing poorly graded pitches, and produce analytical outputs: initiate a highlights reel titled 'Lightning bad pitches: Isabella Davis' using inferior and mediocre graded pitches (F/D/C+/C-/C) containing 6 clips, compile a development report, and include a coaching goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_39",
  instruction=(
            "Functioning as an MLB Analyst, your duty is to compose an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game scheduled after 2024-07-20 and include the venue name. Present an Opponent Analysis scouting report for the identified opponent, underpinned by high-grade pitch evidence (A−/A/A+) from that team’s pitchers"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_40",
  instruction=(
            "As a MLB Analyst, your task is to compile a scouting report on 'Opponent pitch strengths and attack tendencies' for the next Cyclones game following 2024-06-10, and include the venue name. Produce an Opponent Analysis report for the selected opponent, supported by high-grade pitch evidence (A−/A/A+) from that team’s pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-MIL side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_41",
  instruction=(
            "Being a MLB Analyst, coordinate an audit of pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week starting 2025-08-10, with a review date of 2025-09-07, focusing on 'Fastball–breaker' (1.3). Evaluate how effectively the fastball pairs with the main breaker in the decision window. Provide a brief scouting note that includes one development goal and specific highlights in a 5-clip montage titled 'Falcons tunneling audit: Sarah Williams'."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_42",
  instruction=(
            "In your role as a MLB Analyst, assess the performance of Cyclones hitter Evelyn Martin against various pitch sequences, and generate a highlights reel with 3 clips under the name 'Cyclones AB study: Evelyn Martin'. Submit a report including a development goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Cyclones"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Evelyn Martin"},
    ),
    # Pull all pitches faced by the hitter
    Action(
      name="GetAllPitchesByHitterIds",
      kwargs={"hitter_ids": [1]},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting ingestion for AB review
     

    # WRITE:   dev report for Jennifer Roberts
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 1,
        "week_of_date": "2025-08-10"
      },
    ),


    # WRITE: Initialize a highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Cyclones AB study: Evelyn Martin",
        "clip_count": 3,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones AB study: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 3,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_43",
  instruction=(
            "Functioning as a MLB Analyst, produce a comparative analysis of pitch quality for the Lightning vs Cyclones game, showcasing A-tier pitches (A+/A/A−) from each team’s pitching staff. Prepare development reports for all players, organized in ascending order based on their IDs."
        ),
  actions=[
    # Teams
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),  # treat as home for this comparison
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 9}),  # CLE players
    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),  # MIN players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CIN A-tier
    
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewReport", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="AddNewHighlight", kwargs={
    #   "name": "Lightning vs Cyclones Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Lightning",
      "away_team": "Cyclones",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "Cyclones" : [
                    {
                    "grade_id": 3,
                    "pitch_id": 2,
                    "game_pk": 2024000007,
                    "intended_quadrant_model": 6,
                    "actual_quadrant": 7,
                    "miss_distance_inches": 5.37,
                    "execution_grade": "A"
                    }
                ],
        "Lightning":[
                    {
                    "grade_id": 11,
                    "pitch_id": 5,
                    "game_pk": 2024000007,
                    "intended_quadrant_model": 9,
                    "actual_quadrant": 1,
                    "miss_distance_inches": 0.46,
                    "execution_grade": "A+"
                    }
                ]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_44",
  instruction=(
            "As a MLB Analyst, create a detailed pitch analysis and summary highlights for the game between MIL at home and PIT. Provide a scouting note tailored for opponents titled 'Game Summary' and a game summary montage named 'MIL vs PIT – Pitch Log Summary' complete with a 5-clip highlight."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    # Action(
    #   name="GetAllPitchesForGame",
    #   kwargs={"game_pk": 2024000008},
    # ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_45",
  instruction=(
            "As a MLB Analyst, aim to Compile an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game after 2024-06-10. Provide an Opponent Analysis scouting report for the specified opponent by examining their pitches and venue."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 6}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 7}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 7}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5,14]}),


    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004,}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CHC",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [11,16,20,26,35,48,53,58]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_46",
  instruction=(
            "As a MLB Analyst, strive to Develop an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game following 2024-07-20 and include the venue name. Generate an Opponent Analysis scouting report for the recognized opponent, supported by top-tier pitch evidence (A−/A/A+) from that club's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_47",
  instruction=(
            "As a MLB Analyst, work to Formulate an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-07-20 and include the venue name. Provide an Opponent Analysis scouting report focused on the specified opponent's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 10}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 10}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "pitch_ids": [6,8,31,39,40,41,42,44,46,55,57,61],
    }
  ],
),
Task(
  annotator="0",
  user_id="task_48",
  instruction=(
            "As a MLB Analyst, endeavor to Construct an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Falcons game after 2024-08-30 and include the venue name. Produce an Opponent Analysis scouting report centered on the identified opponent's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-08-30", "team_id": 6}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="GetTeamDetailsById", kwargs={"team_id":7}),
    Action(name="GetVenueById", kwargs={"venue_id": 3}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 7}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5,14]}),
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "home_team_name": "Falcons",
      "abbreviation": "CHC",
      "opponent_team_name": "Falcons",
      "venue_name": "Sacramento",
      "game_pk": 2024000004,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
      "opponent_pitch_ids": [11,16,20,26,35,48,53,58]
    }
  ],
),
Task(
  annotator="0",
  user_id="task_49",
  instruction=(
            "As a MLB Analyst, assess the Lightning pitcher James Brown by gathering all of his pitch grades, pinpoint the graded pitches, and generate analyst outputs: set up a highlights reel titled 'Lightning bad pitches: James Brown' using the graded pitches (D, B-) with 5 clips, and compile a development report with a goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
     

    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_50",
  instruction=(
            "As a MLB Analyst, coordinate the creation of a pitch analysis and game summary for the hometown match of the Cyclones versus the Cyclones. Provide a scouting note titled 'Game Summary' and a summary montage 'MIL vs PIT – Pitch Log Summary' featuring 5 highlight clips."
        ),
  actions=[
    # Teams & game context
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),     # home
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),  # away
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_51",
  instruction=(
            "Being a MLB Analyst, generate a pitch analysis and game summary highlights for the Cyclones versus the Cyclones at home. Supply a scouting note labeled 'Game Summary' and a montage titled 'LAD vs COL – Pitch Log Summary' with 5 selected highlight clips."
        ),
  actions=[
    # Teams & game context
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),     # home
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),  # away
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 1, "away_id": 10},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000007},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000007,
        "core_narrative_text": "LAD vs COL – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "LAD vs COL – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000007,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000007,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,

      "playlist_name": "Game Highlights - LAD vs COL – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_52",
  instruction=(
            "As a MLB Analyst, compile a game-level pitch analysis and summary highlights for the home match of the MIL versus the PIT. Issue a scouting note named 'Game Summary' and a montage titled 'MIL vs PIT – Pitch Log Summary' incorporating 5 highlight clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_53",
  instruction=(
            "In your role as a MLB Analyst, prepare a scouting report 'Opponent pitch strengths and attack tendencies' for the Cyclones' upcoming game after 2024-06-10, including the venue name. Deliver this as an Opponent Analysis scouting report for the chosen opponent, showcasing top-grade pitch evidence (A−/A/A+) from the team's pitches."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_54",
  instruction=(
            "In your capacity as a MLB Analyst, orchestrate a game-level pitch analysis and summary highlights for the match between the MIL at home and the Cyclones. Submit a scouting note titled 'Game Summary' and a montage called 'MIL vs PIT – Pitch Log Summary' with 5 selected highlight clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_55",
  instruction=(
            "As an MLB Analyst, compile a scouting report on 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-07-20 and provide the venue name. Submit an Opponent Analysis scouting report for the specified opponent, anchored by high-grade pitch evidence (A−/A/A+) from the team's pitchers"
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_56",
  instruction=(
            "You are a MLB Analyst required to create an opponent scouting report named 'Opponent pitch strengths and attack tendencies' for the ensuing Cyclones game after 2024-07-20 and list the venue. Provide an Opponent Analysis scouting report for the identified opponent, grounded in high-grade pitch evidence (A−/A/A+) from that club’s pitchers."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_57",
  instruction=(
            "As an MLB Analyst, compile a scouting report on 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-07-20 and provide the venue name. Submit an Opponent Analysis scouting report for the specified opponent, anchored by high-grade pitch evidence (A−/A/A+) from the team's pitchers."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_58",
  instruction=(
            "Serving as a MLB Analyst, your duty is to craft an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the forthcoming Cyclones game following 2024-07-20 and provide the venue name. Present an Opponent Analysis scouting report for the chosen opponent, supported by high-grade pitch evidence (A−/A/A+) from that team’s pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_59",
  instruction=(
            "As an MLB Analyst, compile a scouting report on 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-06-10 and return the venue name. Submit an Opponent Analysis scouting report for the specified opponent, anchored by high-grade pitch evidence (A−/A/A+) from the team's pitchers"
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
















Task(
  annotator="0",
  user_id="task_60",
  instruction=(
            "You are a MLB Analyst tasked with generating a pitch analysis at the game level and summary highlights for the match where MIL is hosting PIT. Provide a scouting note labeled 'Game Summary' suitable for opponents and assemble a summary montage of the game titled 'MIL vs PIT – Pitch Log Summary' featuring 5 highlight clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_61",
  instruction=(
            "You are a MLB Analyst required to assess pitch Tunneling for Falcons (CIN) pitcher Sarah Williams during the week of 2025-08-10 (with a review on 2025-09-07) focusing on 'Fastball–breaker' (1.3), measuring the fastball's pairing quality with the primary breaker at the decision window. Provide a clear scouting note including one development goal and create a 5-clip highlight montage titled 'Falcons tunneling audit: Sarah Williams'."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="CreateNewInsight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons tunneling audit: Sarah Williams",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "ingestion_id": 16,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Falcons tunneling audit: Sarah Williams",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_62",
  instruction=(
            "You are a MLB Analyst assigned to create a game-level pitch analysis and summary highlights for the match between MIL at home and PIT. Supply an opponent-ready scouting note entitled 'Game Summary' and a game summary montage called 'MIL vs PIT – Pitch Log Summary' with 5 clips."
        ),
  actions=[
    # Teams & game context
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "MIL"},
    ),
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "PIT"},
    ),
    Action(
      name="GetGameByHomeAway",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="GetAllPitchesForGame",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "MIL vs PIT – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "MIL vs PIT – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Cyclones",
      "away_team": "Cyclones",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - MIL vs PIT – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_63",
  instruction=(
            "You are a MLB Analyst tasked to compile a scouting report titled 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game following 2024-06-10 and specify the venue. Deliver an Opponent Analysis scouting report for the determined opponent, supported by high-grade pitch evidence (A−/A/A+) from that team’s pitchers."
        ),
  actions=[
    # Current team and next scheduled game
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="GetTeamDetailsById", kwargs={"team_id": 9}),
    Action(name="GetVenueById", kwargs={"venue_id": 10}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="GetAllPlayersOfTeam",
      kwargs={"team_id": 9},
    ),
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Lightning",
      "venue":"Baltimore",
      "game_pk": 2024000006,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),

Task(
  annotator="0",
  user_id="task_64",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    },
    {
      "grade_id": 3,
      "pitch_id": 2,
      "game_pk": 2024000007,
      "intended_quadrant_model": 6,
      "actual_quadrant": 7,
      "miss_distance_inches": 5.37,
      "execution_grade": "A"
    }
  ],
),
Task(
  annotator="0",
  user_id="task_65",
  instruction=(
            "As a MLB Analyst, your task is to evaluate the Lightning pitcher James Brown by accessing all of his pitch grades, determine the graded pitches, and generate analyst outcomes: set up a highlights reel named 'Lightning bad pitches: James Brown' utilizing the graded pitches (D, B-) with 5 clips, and submit a development report with a goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
     

    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "hawkeye_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_66",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Cyclones game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_67",
  instruction=(
            "Working as a MLB Analyst, your objective is to analyze pitch mix and execution for Cyclones (COL) pitcher Alexander Taylor during the week of 2025-08-10. Produce a 4-clip montage titled 'Cyclones pitch study: Alexander Taylor'; write a development note with a new goal; include a representative execution-grade entry for one pitch (with the smallest pitch id) from this timeframe to reinforce the assessment. The intended quadrant model was 3 while the actual quadrant was 2, with a deviation of 1.4 inches, resulting in an execution grade of A."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByAbbreviation",
      kwargs={"abbreviation": "COL"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Alexander Taylor"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [7]},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting pitch ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Alexander Taylor
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade one representative pitch from the dataset
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 6,
        "game_pk": 2024000007,
        "intended_quadrant_model": 3,
        "actual_quadrant": 2,
        "miss_distance_inches": 1.4,
        "execution_grade": "A"
      },
    ),

    # # WRITE: Initialize a highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Cyclones pitch study: Alexander Taylor",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 7,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "player": "Alexander Taylor",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "graded_pitch_id": 6,
      "playlist_name": "Game Highlights - Cyclones pitch study: Alexander Taylor",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 4,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_68",
  instruction=(
            "In your role as a MLB Analyst, arrange an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the upcoming Cyclones game after 2024-07-20 and include the venue name. Supply an Opponent Analysis scouting report for the pinpointed opponent, bolstered by high-grade pitch (A−/A/A+) from that team’s pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 8}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 8}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="GetFilteredGradesByPitchIds",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "COL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_69",
  instruction=(
            "As an MLB Analyst, you need to evaluate Lightning (STL) pitcher Isabella Davis’s pitches for the week of 2025-08-10, grade all ungraded pitches considering intended (5) versus actual quadrant (7) and miss distance (2.2) which produces a representative grade (B+). Offer a concise scouting package: a 6-clip montage titled 'Scott - Analysis', and establish a new goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Isabella Davis"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Isabella Davis
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 25,
        "game_pk": 2024000007,
        "intended_quadrant_model": 5,
        "actual_quadrant": 7,
        "miss_distance_inches": 2.2,
        "execution_grade": "B+"
      },
    ),

    # # WRITE: Initialize a K-montage highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "graded_pitch_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Scott - Analysis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),

Task(
  annotator="0",
  user_id="task_70",
  instruction=(
            "Act as an MLB Analyst to assess the pitch portfolio of Falcons (CIN) pitcher Sarah Williams and compile a succinct package: a highlight set named 'Falcons best pitches: Sarah Williams' to feature grade 'A' pitches; along with a development note including the intended goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Falcons"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Sarah Williams"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [5]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A"]}
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # # WRITE: Log supporting aggregation/ingestion for this grade review
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Falcons best pitches: Sarah Williams",
        "clip_count": 1,
        "report_id": 11
      },
    ),

    # # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 5,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Falcons best pitches: Sarah Williams",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_71",
  instruction=(
            "Function as an MLB Analyst to examine all pitch grades for Lightning pitcher James Brown. Identify pitches graded (D, B-), and generate analytical outputs: initiate a highlight reel titled 'Lightning bad pitches: James Brown' with 5 clips and provide a development report with a development goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_72",
  instruction=(
            "Operate as an MLB Analyst to profile Lightning (STL) pitcher Isabella Davis’s average-grade pitches (C+) during the week of 2025-08-10. Aim to generate a highlight set named 'Lightning pitches: Isabella Davis' with 6 clips per pitch, highlighting recurring patterns from the C+ range; and furnish a development report with a goal."
        ),
  actions=[
    # Start from get details by name
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Lightning pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "goal_id": 20,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_73",
  instruction=(
            "Work as an MLB Analyst to study all pitch grades of Lightning pitcher James Brown and identify those with (D, B-) grades. Produce analytical outputs by starting a highlight reel called 'Lightning bad pitches: James Brown' with 5 clips and documenting a development report with a development goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "James Brown"},
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Lightning bad pitches: James Brown",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 8,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation; only create_workflow exists)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "James Brown",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: James Brown",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 5,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_74",
  instruction=(
            "As an MLB Analyst, examine the pitching grades of Falcons pitcher Sarah Williams. Identify her highest-graded pitches and create analyst outputs: launch a highlight reel called 'Falcons best pitches: Sarah Williams' using top-graded pitches (A+ and A)."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Falcons"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Sarah Williams"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [5]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A+","A"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    
    Action(name="CreateNewReport", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Falcons best pitches: Sarah Williams",
      "clip_count": 1,
      "report_id": 11
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Falcons",
      "abbreviation": "CIN",
      "player": "Sarah Williams",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Falcons best pitches: Sarah Williams",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_75",
  instruction=(
            "As a MLB Analyst, examine Cyclones (MIL) pitcher Evelyn Martin’ **low-grade cohort** (F and D) for the date of 2025-08-10. Provide a highlight set titled 'Cyclones bad pitches: Evelyn Martin', and establish a new development goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_76",
  instruction=(
    "You are a MLB Analyst and you want to Review Cyclones (MIL) pitcher Evelyn Martin’ **low-grade cohort** (F and D) for of 2025-08-10. Deliver a highlight set titled 'Cyclones bad pitches: Evelyn Martin';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Evelyn Martin"}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [1]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Cyclones bad pitches: Evelyn Martin",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "player": "Evelyn Martin",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Cyclones bad pitches: Evelyn Martin",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 1,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_77",
  instruction=(
            "Serving as a MLB Analyst, evaluate Lightning pitcher Isabella Davis by compiling all of her pitch grades, identifying the poorly graded pitches, and produce analytical outputs: launch a highlights reel titled 'Lightning bad pitches: Isabella Davis' using the low-graded pitches (F/D/C+/C-/C) containing 6 clips, prepare a development report, and append a coaching goal."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Lightning"}),
    Action(name="GetPlayerDetailsByName", kwargs={"full_name": "Isabella Davis"}),

    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [3]}),
    Action(name="GetFilteredGradesByPitchIds", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="CreateIngestionLog", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="CreateNewReport", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="AddNewHighlight", kwargs={
      "name": "Lightning bad pitches: Isabella Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="CreateNewGoal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Lightning bad pitches: Isabella Davis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
Task(
  annotator="0",
  user_id="task_78",
  instruction=(
            "Acting as a MLB Analyst, compose an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the Cyclones' subsequent game post 2024-07-20 and specify the venue name. Deliver an Opponent Analysis scouting report for the selected opponent's pitches."
        ),
  actions=[
    Action(name="GetTeamDetailsByName", kwargs={"name": "Cyclones"}),
    Action(name="GetNextGame", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="GetTeamDetailsById", kwargs={"team_id": 10}),
    Action(name="GetVenueById", kwargs={"venue_id": 12}),

    Action(
      name="CreateScoutingReport",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="CreateIngestionLog",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="CreateIngestionLog", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="GetAllPlayersOfTeam", kwargs={"team_id": 10}),
    Action(name="GetAllPitchesByPitcherIds", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="CreateWorkflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Cyclones",
      "abbreviation": "MIL",
      "opponent_team_name": "Cyclones",
      "venue":"Charlotte",
      "game_pk": 2024000011,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "scouting_report_id": 13,
      "scouting_report_pdf": "s3://reports/scouting/13.pdf",
      "gslides_link": "https://docs.google.com/presentation/d/13",
    }
  ],
),
Task(
  annotator="0",
  user_id="task_79",
  instruction=(
            "In the role of a MLB Analyst, evaluate the Lightning (STL) pitcher Isabella Davis’s pitches for the week beginning 2025-08-10. Grade all ungraded pitches considering intended (5) vs. actual quadrant (7) and miss distance (2.2) resulting in a representative grade of (B+). Deliver a succinct scouting package: a 6-clip montage titled 'Scott - Analysis', and devise a new goal."
        ),
  actions=[
    # Start from get details by name
    Action(
      name="GetTeamDetailsByName",
      kwargs={"name": "Lightning"},
    ),
    Action(
      name="GetPlayerDetailsByName",
      kwargs={"full_name": "Isabella Davis"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="GetAllPitchesByPitcherIds",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="GetGradesByPitchIds",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="CreateIngestionLog",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="CreateNewReport",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="CreateNewGrade",
      kwargs={
        "pitch_id": 25,
        "game_pk": 2024000007,
        "intended_quadrant_model": 5,
        "actual_quadrant": 7,
        "miss_distance_inches": 2.2,
        "execution_grade": "B+"
      },
    ),

    # # WRITE: Initialize a K-montage highlights reel tied to the report
    Action(
      name="AddNewHighlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="CreateNewGoal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # # WRITE: Record the workflow run (success at creation)
    Action(
      name="CreateWorkflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Lightning",
      "abbreviation": "STL",
      "player": "Isabella Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "graded_pitch_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Scott - Analysis",
      "internal_portal_link": "https://internal.baseball.com/playlists/13",
      "clip_count": 6,
      "s3_pdf_path": "s3://reports/development/11.pdf"
    },
  ],
),
]



