from domains.dto import Action, Task

TASKS = [








Task(
  annotator="0",
  user_id="task_80",
  instruction=(
    "You are a MLB Analyst and you want to Surface Royals (KC) pitchers with **high-grade** execution (A-/A/A+/B-/B/B+) for the week of 2025-08-10 and set reinforcement objectives."
    " Deliver multiple improvement  goals for the players"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [2,13]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Royals",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and return venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to  deliver a dual-sided pitch-quality comparison For the Royals vs Tigers matchup "
    "show A-tier pitches (A+/A/A−) for each club’s pitching staff, and create development reports for all players in increasing order of the ids" 
  ),
  actions=[
    # Teams
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),  # treat as home for this comparison
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),  # CLE players
    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),  # MIN players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CLE A-tier
    
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="add_new_highlight", kwargs={
    #   "name": "Royals vs Tigers Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Royals",
      "away_team": "Tigers",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "Tigers" : [
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
        "Royals":[
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ low graded (F and D) pitches. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to create new insight for Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 for 'Fastball–breaker' (2.3)."
    " and Deliver a concise development goal and a 5-clip highlight"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_85",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Scott Arnold by retrieving all of her pitch grades, "
    "identifying the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Scott Arnold' using the bad-graded pitches  (F/D/C+/C-/C) with 6 clips, filing a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 (review on 2025-09-07) for 'Fastball–breaker' (1.3), "
    "quantifying how well the fastball pairs with the primary breaker through the decision window. Deliver a concise scouting note with one development goal and highlights with"
    "a 5-clip montage named 'Guardians tunneling audit: Rachel Crosby'"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "ingestion_id": 16,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_89",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give its venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis by retrieving all of his pitch grades, "
    "identify the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' using the bad-graded pitches (F and D) with 6 clips, and file a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Daniel Davis"}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [8]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [3,12,36,50],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 8, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Daniel Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal for bad-graded set
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 8,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ **low-grade cohort** (F and D) for of 2025-08-10. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Tigers game after 2024-07-20 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 10}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 10}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "opponent_team_name": "Twins",
      "venue":"Los Angeles Stadium",
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
     "You are a MLB Analyst and you want to Assess the Blue Jays (BLU) pitcher Scott Arnold’s pitch for the week of 2025-08-10, "
    "Grade all the ungraded pitches with intended (5) vs. actual quadrant (7) and miss distance (2.2) that yields a representative grade (B+). "
    "Deliver a compact scouting package: a 6-clip montage titled 'Scott - Analysis', and  create a new goal."
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Scott Arnold"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
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
    "You are a MLB Analyst and you want to Surface Royals (KC) pitchers with **high-grade** execution (A-/A/A+/B-/B/B+) for the week of 2025-08-10 and set reinforcement objectives."
    " Deliver multiple improvement  goals for the players"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [2,13]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Royals",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Guardians game (away) after 2024-08-30 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_team_details_by_id", kwargs={"team_id":6}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 6}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [11]}),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "opponent_team_name": "White Sox",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis's all pitch grades, and "
    "identifying the (D, B-) graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' with 5 clips and file a development report with a development goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Profile the Blue Jays (BLU) pitcher Scott Arnold’s average-grade pitches (C+) over the week of 2025-08-10. you want to create"
    " highlight set titled 'Blue Jays pitches: Scott Arnold' with 6 clips per pitch, illustrating repeatable patterns from the C+ band;" 
    "file a development report with a   goal"
  ),
  actions=[
    # Start from get details by name
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Blue Jays pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to create new insight for Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 for 'Fastball–breaker' (2.3)."
    " and Deliver a concise development goal and a 5-clip highlight"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),

Task(
  annotator="0",
  user_id="task_01",
  instruction=(
    "You are a MLB Analyst and you want to Evaluate the Tigers (DET) roster with emphasis on Jennifer Roberts for the week of 2025-08-10. Deliver a compact scouting package: a curated highlight set titled 'Tigers roster focus' (3clips);"
    " and create  new  improvement  goal"

  ),
  actions=[
    # Start from get details by name (team), then proceed
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Tigers"},
    ),
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 8},
    ),
    # Confirm focal player by exact name
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Jennifer Roberts"},
    ),

    

    # WRITE: Log supporting data ingestion
    


    # WRITE: File   dev report for Jennifer Roberts
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 1,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel context for this study
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Tigers roster focus",
        "clip_count": 3,
        "report_id": 11
      },
    ),

    

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),

  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers roster focus",
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
    "You are a MLB Analyst and you want to Evaluate the Twins (MIN) roster with emphasis on Kevin Holmes for the week of 2025-08-10. "
    "and Deliver a concise scouting package: a curated highlight set titled 'Twins roster focus' (4 clips), a   player-development goal."
  ),
  actions=[
    # Start from get details by name (team)
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Twins"},
    ),
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 10},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Kevin Holmes"},
    ),

    # WRITE: Log supporting data ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Kevin Holmes
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Twins roster focus",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "player": "Kevin Holmes",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Twins roster focus",
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
    "You are a MLB Analyst and you want to sumarize all the information For the game cancelled in Kansas City on 2024-07-28, get player information of both"
    " the teams and umpire details in a 'Cancelled-Game' scouting report with 'Game Cancelled' and 5 clip highlights named 'Match Cancelled'."
  ),
  actions=[
    # Venue + games on the date
    Action(name="get_all_venue_in_city", kwargs={"city": "Kansas City"}),
    Action(name="find_games_on_date", kwargs={"date": "2024-07-28"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Resolve the specific game at any Cleveland venue
    # (Pick the first game whose venue_id is in the Cleveland venue list)
    Action(
      name="get_team_details_by_id",
      kwargs={"team_id": 7},
    ),
    Action(
      name="get_team_details_by_id",
      kwargs={"team_id": 6},
    ),

    # Rosters for both sides
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 7},
    ),
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 6},
    ),

    # Umpire model calibration for the selected game
    Action(
      name="get_model_detail_by_game",
      kwargs={"game_pk": 2024000001},
    ),
    Action(
      name="get_umpires_details_by_id",
      kwargs={"umpire_id": 8},
    ),

    # Evidence logs per policy (roster/lookup → snowflake; model/video context → hawkeye)
    

    # Scouting report + highlights
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Cancelled-Game",
        "game_pk": 2024000001,
        "core_narrative_text": "Game Cancelled"
      },
    ),

    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Match Cancelled",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "city": "Kansas City",
      "date": "2024-07-28",
      "home_team": "Guardians",
      "away_team": "White Sox",
      "game_pk": 2024000001,
      "umpire_name": "Melissa Jackson",
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
                              "full_name": "Rachel Crosby",
                              "primary_position": "CF",
                              "batting_handedness": "S",
                              "throwing_handedness": "R",
                              "current_team_id": 7,
                              "roster_status": "Active"
                            },
                            {
                              "player_id": 14,
                              "full_name": "Joseph Hart",
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
                              "full_name": "Barbara Robles",
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
    "You are a MLB Analyst and you want to Analyze the Guardians (CLE) roster context with a focus on Rachel Crosby, "
    "and produce analyst outputs: initialize a highlights reel with 5 clips named 'Guardians roster focus', "
    "file a development report with a development goal"

  ),
  actions=[
    # Start from get details by name (team)
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Guardians"},
    ),
    # Action(
    #   name="get_all_players_of_team",
    #   kwargs={"team_id": 7},
    # ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Rachel Crosby"},
    ),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    # WRITE: Log supporting data ingestion


    # WRITE:   dev report for Rachel Crosby
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # WRITE: Initialize a highlights reel
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Guardians roster focus",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Guardians roster focus",
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
    "You are a MLB Analyst and you want to evaluate pitch mix and execution during the week of 2025-08-10, For Twins (MIN) pitcher Kevin Holmes, . "
    "you want to create a 4-clip montage titled 'Twins pitch study: Kevin Holmes'; "
    "a   development note with a new goal; "
    "a representative execution-grading entry for one pitch (with smallest pitch id) from this window to support the assessment with The intended quadrant model was 3 while the actual quadrant was 2,"
    " with a miss distance of 1.4 inches, resulting in an execution grade of A. "

  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "MIN"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Kevin Holmes"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [7]},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting pitch ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Kevin Holmes
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade one representative pitch from the dataset
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Twins pitch study: Kevin Holmes",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "player": "Kevin Holmes",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "graded_pitch_id": 6,
      "playlist_name": "Game Highlights - Twins pitch study: Kevin Holmes",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip;"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_07",
  instruction=(
     "You are a MLB Analyst and you want to Assess the Blue Jays (BLU) pitcher Scott Arnold’s pitch for the week of 2025-08-10, "
    "Grade all the ungraded pitches with intended (5) vs. actual quadrant (7) and miss distance (2.2) that yields a representative grade (B+). "
    "Deliver a compact scouting package: a 6-clip montage titled 'Scott - Analysis', and  create a new goal."
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Scott Arnold"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
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
    "You are a MLB Analyst and you want to  evaluate Guardians (CLE) pitcher Rachel Crosby’s all pitches and deliver a highlight set titled 'Guardians best pitches: Rachel Crosby' showcasing grade 'A' pitches; "
    "a development note with the   goal."

  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Guardians"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Rachel Crosby"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [5]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A"]}
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # # WRITE: Log supporting aggregation/ingestion for this grade review
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Guardians best pitches: Rachel Crosby",
        "clip_count": 1,
        "report_id": 11
      },
    ),

    # # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Guardians best pitches: Rachel Crosby",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis's all pitch grades, and "
    "identifying the (D, B-) graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' with 5 clips and file a development report with a development goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Profile the Blue Jays (BLU) pitcher Scott Arnold’s average-grade pitches (C+) over the week of 2025-08-10. you want to create"
    " highlight set titled 'Blue Jays pitches: Scott Arnold' with 6 clips per pitch, illustrating repeatable patterns from the C+ band;" 
    "file a development report with a   goal"
  ),
  actions=[
    # Start from get details by name
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Blue Jays pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Surface the Tigers (DET) low grade pitches of grades (D/F)  and create improvement goals for the players."

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["D", "F"]},
    ),

    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 4,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
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
    "You are a MLB Analyst and you want to Analyze the Guardians pitcher Rachel Crosby by retrieving all of her pitch grades, and"
    "identify the best-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Guardians best pitches: Rachel Crosby' using the top-graded pitches (A+ and A) and create new goal for the player"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A+","A"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Guardians best pitches: Rachel Crosby",
      "clip_count": 1,
      "report_id": 11
    }),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 5,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id":20,
      "playlist_name": "Game Highlights - Guardians best pitches: Rachel Crosby",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis by retrieving all of his pitch grades, "
    "identify the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' using the bad-graded pitches (F and D) with 6 clips, and file a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Daniel Davis"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [8]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [3,12,36,50],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 8, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Daniel Davis",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal for bad-graded set
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 8,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ **low-grade cohort** (F and D) for of 2025-08-10. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Scott Arnold by retrieving all of her pitch grades, "
    "identifying the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Scott Arnold' using the bad-graded pitches  (F/D/C+/C-/C) with 6 clips, filing a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches "
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to  Identify Tigers (DET) pitchers with **high-grade** execution (A-/A/A+/B-/B/B+) during the week of 2025-08-10 and articulate a improvement goal."

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    # 

    # # # High-grade include list (keep only A/B tiers)
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),

    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 1,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
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
    "You are a MLB Analyst and you want to Surface Royals (KC) pitchers with **high-grade** execution (A-/A/A+/B-/B/B+) for the week of 2025-08-10 and set reinforcement objectives."
    " Deliver improvement  goals for all the players"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [2,13]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-", "B+", "B", "B-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 2,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 12,
        "player_id": 13,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07",
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Royals",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Guardians game after 2024-08-30 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-08-30", "team_id": 7}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="get_team_details_by_id", kwargs={"team_id":6}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 6}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [11]}),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "opponent_team_name": "White Sox",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to deliver a dual-sided pitch-quality comparison For the Royals vs Tigers matchup,  "
    "show A-tier pitches (A+/A/A−) for each club’s pitching staff, and create development reports for all players in increasing order of the ids"
  ),
  actions=[
    # Teams
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),  # treat as home for this comparison
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),  # CLE players
    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),  # MIN players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CLE A-tier
    
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="add_new_highlight", kwargs={
    #   "name": "Royals vs Tigers Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Royals",
      "away_team": "Tigers",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "player_1_dev_report": 11,
      "player_2_dev_report": 12,
      "player_4_dev_report": 13,
      "player_13_dev_report": 14,
      "Tigers" : [
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
    "Royals":[
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ low graded (F and D) pitches. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to  create new insight for Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 for 'Fastball–breaker' (2.3)."
    " and Deliver a concise development goal and a 5-clip highlight"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 2.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_23",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI on 2024-03-05. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip;"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),

    


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_24",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, filtered by high-grade pitch of grades (A−/A/A+) from that opponent's pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next White Sox game after 2024-06-10 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent by analysing their pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "White Sox"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 6}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 7}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 7}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5,14]}),


    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004,}),
  ],
  outputs=[
    {
      "team": "White Sox",
      "abbreviation": "CHW",
      "opponent_team_name": "Guardians",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Tigers game after 2024-07-20 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 10}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 10}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "opponent_team_name": "Twins",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 (review on 2025-09-07) for 'Fastball–breaker' (1.3), "
    "quantifying how well the fastball pairs with the primary breaker through the decision window. Deliver a concise scouting note with one development goal and highlights with"
    "a 5-clip montage named 'Guardians tunneling audit: Rachel Crosby'"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_29",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Guardians game after 2024-08-30 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_team_details_by_id", kwargs={"team_id":6}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 6}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [11]}),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "opponent_team_name": "White Sox",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary for the match "
    "between the Tigers at home and the Orioles. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),     # home
    Action(name="get_team_details_by_name", kwargs={"name": "Orioles"}),  # away
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "s3_pdf_path": "s3://reports/scouting/13.pdf",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_31",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),
    
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "hawkeye_ingestion_id":17,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_33",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the Yankees at home and the MIN. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'YAN vs MIN – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "YAN"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "MIN"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 1, "away_id": 10},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000007},
    ),

    # # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000007,
        "core_narrative_text": "YAN vs MIN – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "YAN vs MIN – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000007,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Yankees",
      "away_team": "Twins",
      "game_pk": 2024000007,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - YAN vs MIN – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_34",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the Orioles. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(name="get_team_details_by_name", kwargs={"name": "Orioles"}),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_35",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the Tigers at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and "
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 cliphighlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_36",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Guardians game after 2024-08-30 and give venue name"
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-08-30", "team_id": 7}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_team_details_by_id", kwargs={"team_id":6}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 6}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [11]}),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "opponent_team_name": "White Sox",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Scott Arnold by retrieving all of her pitch grades, "
    "identifying the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Scott Arnold' using the bad-graded and average-graded pitches  (F/D/C+/C-/C) with 6 clips, filing a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and return venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 (review on 2025-09-07) for 'Fastball–breaker' (1.3), "
    "quantifying how well the fastball pairs with the primary breaker through the decision window. Deliver a concise scouting note with one development goal and highlights with"
    "a 5-clip montage named 'Guardians tunneling audit: Rachel Crosby'"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_42",
  instruction=(
    "You are a MLB Analyst and you want to Analyze the Tigers hitter Jennifer Roberts’ performance against all pitch sequences, "
    "and produce highlights reel with 3 clips named 'Tigers AB study: Jennifer Roberts', "
    "file a report with a development goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Tigers"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Jennifer Roberts"},
    ),
    # Pull all pitches faced by the hitter
    Action(
      name="get_all_pitches_by_hitter_ids",
      kwargs={"hitter_ids": [1]},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting ingestion for AB review
     

    # WRITE:   dev report for Jennifer Roberts
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 1,
        "week_of_date": "2025-08-10"
      },
    ),


    # WRITE: Initialize a highlights reel tied to the report
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Tigers AB study: Jennifer Roberts",
        "clip_count": 3,
        "report_id": 11
      },
    ),

    # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers AB study: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to deliver a dual-sided pitch-quality comparison For the Royals vs Tigers matchup,  "
    "show A-tier pitches (A+/A/A−) for each club’s pitching staff, and create development reports for all players in increasing order of the ids"
  ),
  actions=[
    # Teams
    Action(name="get_team_details_by_name", kwargs={"name": "Royals"}),  # treat as home for this comparison
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),      # away

    # Ingestion logs (roster → snowflake, pitch/vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye",   "status_code": 200, "records_ingested": 500}),

    # Roster for both sides
    Action(name="get_all_players_of_team", kwargs={"team_id": 9}),  # CLE players
    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),  # MIN players

    # Pitchers' pitches for both sides (IDs inferred by pitch presence)
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [1,4]},
    ),
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ), # CLE A-tier
    
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [2,10,15,18,19,21,27,49,59,60],
        "grades": ["A+", "A", "A-"]
      },
    ),
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 2, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 4, "week_of_date": "2025-08-10"}),
    Action(name="create_new_report", kwargs={"player_id": 13, "week_of_date": "2025-08-10"}),
    
    # Action(name="add_new_highlight", kwargs={
    #   "name": "Royals vs Tigers Highlights",
    #   "clip_count": 6,
    #   "report_id": 11
    # }),

    # Workflow
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "home_team": "Royals",
      "away_team": "Tigers",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id": 16,
      "hawkeye_ingestion_id": 17,
      "Tigers" : [
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
        "Royals":[
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    # Action(
    #   name="get_all_pitches_for_game",
    #   kwargs={"game_pk": 2024000008},
    # ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_45",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next White Sox game after 2024-06-10."
    "Deliver an Opponent Analysis scouting report for the identified opponent by analysing their pitches and venue"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "White Sox"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 6}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 7}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 7}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5,14]}),


    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004,}),
  ],
  outputs=[
    {
      "team": "White Sox",
      "abbreviation": "CHW",
      "opponent_team_name": "Guardians",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Tigers game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 10}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 10}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "opponent_team_name": "Twins",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next White Sox game after 2024-08-30 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "White Sox"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-08-30", "team_id": 6}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="get_team_details_by_id", kwargs={"team_id":7}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 3}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000004,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 7}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5,14]}),
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000004}),
  ],
  outputs=[
    {
      "home_team_name": "White Sox",
      "abbreviation": "CHW",
      "opponent_team_name": "Guardians",
      "venue_name": "Toronto Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis by retrieving all of his pitch grades, "
    "identify the graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' using the graded pitches (D, B-) with 5 clips, and file a development report with a goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
     

    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary for the match "
    "between the Tigers at home and the Orioles. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),     # home
    Action(name="get_team_details_by_name", kwargs={"name": "Orioles"}),  # away
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_51",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights for the match "
    "between the Yankees at home and the Twins. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'YAN vs MIN – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(name="get_team_details_by_name", kwargs={"name": "Yankees"}),     # home
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),  # away
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 1, "away_id": 10},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000007},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000007,
        "core_narrative_text": "YAN vs MIN – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "YAN vs MIN – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000007,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Yankees",
      "away_team": "Twins",
      "game_pk": 2024000007,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,

      "playlist_name": "Game Highlights - YAN vs MIN – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_52",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_53",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that teams’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the Orioles. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(name="get_team_details_by_name", kwargs={"name": "Orioles"}),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_55",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name"
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and return venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip highlight"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_61",
  instruction=(
    "You are a MLB Analyst and you want to Audit pitch Tunneling for Guardians (CLE) pitcher Rachel Crosby over the week of 2025-08-10 (review on 2025-09-07) for 'Fastball–breaker' (1.3), "
    "quantifying how well the fastball pairs with the primary breaker through the decision window. Deliver a concise scouting note with one development goal and highlights with"
    "a 5-clip montage named 'Guardians tunneling audit: Rachel Crosby'"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # Evidence logs (vision for pitch analytics)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # Report + insight + highlight + goal
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),
    Action(name="create_new_insight", kwargs={
      "report_id": 11,
      "player_id": 5,
      "insight_text": "Fastball–breaker",
      "insight_type": "Tunneling",
      "supporting_stat_value": 1.3
    }),
    Action(name="add_new_highlight", kwargs={
      "name": "Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5,
      "report_id": 11
    }),
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 5,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "ingestion_id": 16,
      "dev_report_id": 11,
      "insight_id": 29,
      "playlist_name": "Game Highlights - Guardians tunneling audit: Rachel Crosby",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_62",
  instruction=(
    "You are a MLB Analyst and you want to Produce a game-level pitch analysis and summary highlights  for the match "
    "between the DET at home and the ORI. Deliver an opponent-ready scouting note 'Game Summary' and"
    "a game summary montage titled 'DET vs ORI – Pitch Log Summary' with 5 clip;"
  ),
  actions=[
    # Teams & game context
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "DET"},
    ),
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "ORI"},
    ),
    Action(
      name="get_game_by_home_away",
      kwargs={"home_id": 8, "away_id": 4},
    ),

    # Ingestion logs per policy (roster/lookup → snowflake)
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull all pitches for the identified game
    Action(
      name="get_all_pitches_for_game",
      kwargs={"game_pk": 2024000008},
    ),

    # # Sensor/vision ingestion for pitch events → trackman
     

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Game Summary",
        "game_pk": 2024000008,
        "core_narrative_text": "DET vs ORI – Pitch Log Summary"
      },
    ),


    # # Game summary highlights (clip_count equals number of pitches)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "DET vs ORI – Pitch Log Summary",
        "clip_count": 5,
        "report_id": 13
      },
    ),

    # # Workflow bookkeeping
    Action(
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "game_pk": 2024000008,
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "home_team": "Tigers",
      "away_team": "Orioles",
      "game_pk": 2024000008,
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "snowflake_ingestion_id":16,
      "playlist_name": "Game Highlights - DET vs ORI – Pitch Log Summary",
      "clip_count": 5
    }
  ],
),
Task(
  annotator="0",
  user_id="task_63",
  instruction=(
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-06-10 and give its venue name. "
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    # Current team and next scheduled game
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-06-10", "team_id": 10}),

    # Opponent team context (pull both sides, then use the non-DET side as the opponent in reporting)
    Action(name="get_team_details_by_id", kwargs={"team_id": 9}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 10}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),    


    # # Scouting report for this matchup (opponent-focused)
    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000006,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    # # Vision ingestion for pitch/grade evidence
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500},
    ),

    # # Pull opponent pitchers' pitches (treat away club as opponent for determinism)
    Action(
      name="get_all_players_of_team",
      kwargs={"team_id": 9},
    ),
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [2,13]},
    ),

    # # Keep only high-grade (A-tier) executions to inform the scouting narrative
    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={
        "pitch_ids": [5,7,23,28,29,32,45,52,54],
        "grades": ["A+", "A", "A-"]
      },
    ),

    # # Workflow bookkeeping
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000006,}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Royals",
      "venue":"Minneapolis Stadium",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis by retrieving all of his pitch grades, "
    "identify the graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' using the graded pitches (D, B-) with 5 clips, and file a development report with a goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),
     

    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "hawkeye_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch evidence "
    "(A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
    "You are a MLB Analyst and you want to evaluate pitch mix and execution during the week of 2025-08-10 For Twins (MIN) pitcher Kevin Holmes . "
    "you want to create a 4-clip montage titled 'Twins pitch study: Kevin Holmes'; "
    "a   development note with a new goal goal; "
    "a representative execution-grading entry for one pitch (with smallest pitch id) from this window to support the assessment with The intended quadrant model was 3 while the actual quadrant was 2,"
    " with a miss distance of 1.4 inches, resulting in an execution grade of A. "

  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_abbreviation",
      kwargs={"abbreviation": "MIN"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Kevin Holmes"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [7]},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # WRITE: Log supporting pitch ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # WRITE:   dev report for Kevin Holmes
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 7,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade one representative pitch from the dataset
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Twins pitch study: Kevin Holmes",
        "clip_count": 4,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "player": "Kevin Holmes",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "graded_pitch_id": 6,
      "playlist_name": "Game Highlights - Twins pitch study: Kevin Holmes",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Twins game after 2024-07-20 and give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent, anchored by high-grade pitch (A−/A/A+) from that club’s pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Twins"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 10}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 8}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 8}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1,4]}),

    Action(
      name="get_filtered_grades_by_pitch_ids",
      kwargs={"pitch_ids": [2,10,15,18,19,21,27,49,59,60], "grades": ["A+", "A", "A-"]},
    ),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Twins",
      "abbreviation": "MIN",
      "opponent_team_name": "Tigers",
      "venue":"Los Angeles Stadium",
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
     "You are a MLB Analyst and you want to Assess the Blue Jays (BLU) pitcher Scott Arnold’s pitch for the week of 2025-08-10, "
    "Grade all the ungraded pitches with intended (5) vs. actual quadrant (7) and miss distance (2.2) that yields a representative grade (B+). "
    "Deliver a compact scouting package: a 6-clip montage titled 'Scott - Analysis', and  create a new goal."
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Scott Arnold"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
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
    "You are a MLB Analyst and you want to  evaluate Guardians (CLE) pitcher Rachel Crosby’s pitch portfolio and deliver a concise package: a highlight set titled 'Guardians best pitches: Rachel Crosby' showcasing grade 'A' pitches; "
    "a development note with the   goal."

  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Guardians"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Rachel Crosby"},
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [5]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A"]}
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    # # WRITE: Log supporting aggregation/ingestion for this grade review
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 5,
        "week_of_date": "2025-08-10"
      },
    ),

    # # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Guardians best pitches: Rachel Crosby",
        "clip_count": 1,
        "report_id": 11
      },
    ),

    # # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Guardians best pitches: Rachel Crosby",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis's all pitch grades, and "
    "identifying the (D, B-) graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' with 5 clips and file a development report with a development goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Profile the Blue Jays (BLU) pitcher Scott Arnold’s average-grade pitches (C+) over the week of 2025-08-10. you want to create"
    " highlight set titled 'Blue Jays pitches: Scott Arnold' with 6 clips per pitch, illustrating repeatable patterns from the C+ band;" 
    "file a development report with a   goal"
  ),
  actions=[
    # Start from get details by name
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    # Retrieve all pitches thrown by the player and grades for them
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["C+"]}),

    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    # # WRITE: Log supporting aggregation (vision → hawkeye)
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     

    # # (Optional) WRITE:   report to anchor highlights in reporting
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    # WRITE: Highlights for best-graded pitches
    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),
    Action(
      name="create_new_goal",
      kwargs={
        "dev_report_id": 11,
        "player_id": 3,
        "goal_text": "Need to improve",
        "coach_id": 10,
        "target_review_date": "2025-09-07"
      },
    ),

    # WRITE: Workflow run
    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Blue Jays pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Daniel Davis's all pitch grades, and "
    "identifying the (D, B-) graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Daniel Davis' with 5 clips and file a development report with a development goal"
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Daniel Davis"},
    ),
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # Retrieve all pitches thrown by the player
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [8]},
    ),

    # Retrieve grades for all of those pitch IDs
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [3,12,36,50],"grades":["D","B-"]}
    ),

    # # # WRITE: Log supporting aggregation/ingestion for this grade review (vision-related → hawkeye)
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # # WRITE:   player development report
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 8,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Initialize a highlights reel for the best-graded pitches (A+/A/A− or top-N)
    Action(
      name="add_new_highlight",
      kwargs={
        "name": "Blue Jays bad pitches: Daniel Davis",
        "clip_count": 5,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Daniel Davis",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Daniel Davis",
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
    "You are a MLB Analyst and you want to Analyze the Guardians pitcher Rachel Crosby by retrieving all of her pitch grades, and"
    "identify the best-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Guardians best pitches: Rachel Crosby' using the top-graded pitches (A+ and A)"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Guardians"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Rachel Crosby"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [5]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [11,16,20,35,53,58],"grades":["A+","A"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
    
    Action(name="create_new_report", kwargs={"player_id": 5, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Guardians best pitches: Rachel Crosby",
      "clip_count": 1,
      "report_id": 11
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Guardians",
      "abbreviation": "CLE",
      "player": "Rachel Crosby",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "playlist_name": "Game Highlights - Guardians best pitches: Rachel Crosby",
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ **low-grade cohort** (F and D) for of 2025-08-10. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to Review Tigers (DET) pitcher Jennifer Roberts’ **low-grade cohort** (F and D) for of 2025-08-10. Deliver a highlight set titled 'Tigers bad pitches: Jennifer Roberts';"
    " and  create a new development goal"

  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Jennifer Roberts"}),
    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [1]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [2,18,27,49,59,60],"grades":["F","D"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 1, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Tigers bad pitches: Jennifer Roberts",
      "clip_count": 1,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 1,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "player": "Jennifer Roberts",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "hawkeye_ingestion_log_id": 17,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Tigers bad pitches: Jennifer Roberts",
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
    "You are a MLB Analyst and you want to Analyze the Blue Jays pitcher Scott Arnold by retrieving all of her pitch grades, "
    "identifying the bad-graded pitches, and produce analyst outputs: initialize a highlights reel named "
    "'Blue Jays bad pitches: Scott Arnold' using the bad-graded pitches  (F/D/C+/C-/C) with 6 clips, filing a   development report and attach a coaching goal."
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Blue Jays"}),
    Action(name="get_player_details_by_name", kwargs={"full_name": "Scott Arnold"}),

    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [3]}),
    Action(name="get_filtered_grades_by_pitch_ids", kwargs={"pitch_ids": [25,30],"grades":["F","D","C+","C","C-"]}),

    Action(name="create_ingestion_log", kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500}),
    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),
     
    Action(name="create_new_report", kwargs={"player_id": 3, "week_of_date": "2025-08-10"}),

    Action(name="add_new_highlight", kwargs={
      "name": "Blue Jays bad pitches: Scott Arnold",
      "clip_count": 6,
      "report_id": 11
    }),

    # WRITE: Coaching goal
    Action(name="create_new_goal", kwargs={
      "dev_report_id": 11,
      "player_id": 3,
      "goal_text": "Need to improve",
      "coach_id": 10,
      "target_review_date": "2025-09-07"
    }),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success"}),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
      "workflow_run_id": "run_16",
      "workflow_status": "success",
      "log_s3_path": "s3://logs/workflows/run_16.log",
      "snowflake_ingestion_log_id": 16,
      "dev_report_id": 11,
      "goal_id": 20,
      "playlist_name": "Game Highlights - Blue Jays bad pitches: Scott Arnold",
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
    "You are a MLB Analyst and you want to Prepare an opponent scouting report 'Opponent pitch strengths and attack tendencies' for the next Tigers game after 2024-07-20 and  give venue name."
    "Deliver an Opponent Analysis scouting report for the identified opponent's pitches"
  ),
  actions=[
    Action(name="get_team_details_by_name", kwargs={"name": "Tigers"}),
    Action(name="get_next_game", kwargs={"current_date": "2024-07-20", "team_id": 8}),

    Action(name="get_team_details_by_id", kwargs={"team_id": 10}),
    Action(name="get_venue_by_id", kwargs={"venue_id": 12}),

    Action(
      name="create_scouting_report",
      kwargs={
        "report_type": "Opponent Analysis",
        "game_pk": 2024000011,
        "core_narrative_text": "Opponent pitch strengths and attack tendencies"
      },
    ),
    Action(
      name="create_ingestion_log",
      kwargs={"source_name": "snowflake", "status_code": 200, "records_ingested": 500},
    ),

    Action(name="create_ingestion_log", kwargs={"source_name": "hawkeye", "status_code": 200, "records_ingested": 500}),

    Action(name="get_all_players_of_team", kwargs={"team_id": 10}),
    Action(name="get_all_pitches_by_pitcher_ids", kwargs={"pitcher_ids": [7,9,10]}),

    Action(name="create_workflow", kwargs={"dag_name": "generate_reports", "status": "success","game_pk": 2024000011}),
  ],
  outputs=[
    {
      "team": "Tigers",
      "abbreviation": "DET",
      "opponent_team_name": "Twins",
      "venue":"Los Angeles Stadium",
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
     "You are a MLB Analyst and you want to Assess the Blue Jays (BLU) pitcher Scott Arnold’s pitch for the week of 2025-08-10, "
    "Grade all the ungraded pitches with intended (5) vs. actual quadrant (7) and miss distance (2.2) that yields a representative grade (B+). "
    "Deliver a compact scouting package: a 6-clip montage titled 'Scott - Analysis', and  create a new goal."
  ),
  actions=[
    # Start from get details by name
    Action(
      name="get_team_details_by_name",
      kwargs={"name": "Blue Jays"},
    ),
    Action(
      name="get_player_details_by_name",
      kwargs={"full_name": "Scott Arnold"},
    ),
    # Pull all pitches for the pitcher
    Action(
      name="get_all_pitches_by_pitcher_ids",
      kwargs={"pitcher_ids": [3]},
    ),
    # Retrieve details for a representative pitch (for context)
    Action(
      name="get_grades_by_pitch_ids",
      kwargs={"pitch_ids": [25,30]}
    ),

    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "snowflake",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),

    # # WRITE: Log supporting ingestion
    Action(
      name="create_ingestion_log",
      kwargs={
        "source_name": "hawkeye",
        "status_code": 200,
        "records_ingested": 500,
      },
    ),


    # # WRITE:   dev report for Scott Arnold
    Action(
      name="create_new_report",
      kwargs={
        "player_id": 3,
        "week_of_date": "2025-08-10"
      },
    ),

    # # WRITE: Grade a representative changeup
    Action(
      name="create_new_grade",
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
      name="add_new_highlight",
      kwargs={
        "name": "Scott - Analysis",
        "clip_count": 6,
        "report_id": 11
      },
    ),

    # # WRITE: Attach a   development goal
    Action(
      name="create_new_goal",
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
      name="create_workflow",
      kwargs={
        "dag_name": "generate_reports",
        "status": "success",
      },
    ),
  ],
  outputs=[
    {
      "team": "Blue Jays",
      "abbreviation": "BLU",
      "player": "Scott Arnold",
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



