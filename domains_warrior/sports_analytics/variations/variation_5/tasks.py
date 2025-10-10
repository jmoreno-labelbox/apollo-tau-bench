from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="saaish2",
        user_id="task_001",
        instruction=(
            "You are a lead analyst in the player development department for Team 3 (Blue Jays). Your objective is to "
            "produce and finalize the weekly development packages for all 'Active' roster players for the week of 2025-08-11. "
            "The final deliverable for each player must include a development report with an approved goal and two specific video playlists. "
            "For Scott Arnold, the goal is 'Improve two-strike approach' (coach ID 28), his 'Positive Reinforcement' playlist must have 4 clips, and his 'Teaching Moments' playlist must have 3. "
            "For Daniel Davis, the goal is 'Increase contact rate on high fastballs' (coach ID 33), his 'Positive Reinforcement' playlist must have 5 clips, and his 'Teaching Moments' playlist must have 2. "
            "The target review date for both goals is '2025-09-15'. "
            "The entire batch process should be logged as a single workflow run with a start time of '2025-08-11T10:00:00Z' and an end time of '2025-08-11T11:30:00Z'. "
            "Return the unique `run_id` for the completed workflow."
        ),
        actions=[
            Action(name="get_active_roster", kwargs={"team_id": 3}),
            Action(name="create_player_dev_report", kwargs={"player_id": 3, "week_of_date": "2025-08-11"}),
            Action(
                name="create_player_dev_goal",
                kwargs={
                    "dev_report_id": 11,
                    "player_id": 3,
                    "goal_text": "Improve two-strike approach",
                    "coach_id": 28,
                    "target_review_date": "2025-09-15",
                },
            ),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(
                name="create_video_playlist",
                kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3},
            ),
            Action(name="create_player_dev_report", kwargs={"player_id": 8, "week_of_date": "2025-08-11"}),
            Action(
                name="create_player_dev_goal",
                kwargs={
                    "dev_report_id": 12,
                    "player_id": 8,
                    "goal_text": "Increase contact rate on high fastballs",
                    "coach_id": 33,
                    "target_review_date": "2025-09-15",
                },
            ),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(
                name="create_video_playlist",
                kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 5},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 2},
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "weekly_player_development",
                    "status": "success",
                    "start_time_utc": "2025-08-11T10:00:00Z",
                    "end_time_utc": "2025-08-11T11:30:00Z",
                    "log_s3_path": "s3://logs/dev_reports/batch_run_2025-08-11.log",
                },
            ),
        ],
        outputs=["1"],
    ),

    Task(
        annotator="saaish2",
        user_id="task_002",
        instruction=(
            "You are finalizing a coach-facing post-game review for our home game. Upstream ingestion/QC are approved and the game is complete.\n"
            "Acceptance criteria (terminal database state):\n"
            "• The game record for game_pk 2024000008 is confirmed complete (Final) before any post-game artifacts exist.\n"
            "• Exactly five pitch-execution evaluations are stored for this game with the following intent/actual quadrants and miss distances (inches):\n"
            "  – pitch_id 29: intended down_away, actual down_middle, miss 2.4\n"
            "  – pitch_id 33: intended up_in, actual middle_in, miss 6.8\n"
            "  – pitch_id 46: intended down_away, actual down_away, miss 1.2\n"
            "  – pitch_id 17: intended up_away, actual up_middle, miss 4.1\n"
            "  – pitch_id 45: intended down_in, actual middle_in, miss 5.0\n"
            "• A post-game scouting brief exists for game_pk 2024000008 with core narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Four video playlists are attached to that brief: two named Positive Reinforcement with 3 clips each, and two named Teaching Moments with 2 clips each.\n"
            "• The workflow ledger shows a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc == end_time_utc == 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.\n"
            "No additional outputs are required."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: use the required key 'playlist_name'
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review_packet",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_003",
        instruction=(
            "You are the analytics coordinator for Team 10. Deliver a pre-series package for Team 10’s next scheduled game on/after 2024-07-23.\n"
            "\nAcceptance criteria (single, deterministic terminal state):"
            "\n1) Exactly one scouting report exists for that game with: report_type='Pre-Game', core_narrative_text='pre_series_policy_v1', "
            "gslides_link set by the canonical pattern 'https://slides.example.org/pre/{game_pk}', and s3_pdf_path set by the canonical pattern "
            "'s3://reports/scouting/pre/{game_date}_g{game_pk}_team10_vs{opponent_team_id}.pdf'."
            "\n2) Exactly two curated insights are attached to that report, both using the required template '{category}_{metric}_{bucket}' and allowed types: "
            "(player_id=1, insight_type='tendency', insight_text='tendency_chaserate_high', supporting_stat_value=0.412) and "
            "(player_id=4, insight_type='predictability', insight_text='predictability_firstpitchswing_low', supporting_stat_value=0.193)."
            "\n3) Exactly two video playlists are attached to that report with these precise properties: "
            "('Positive Reinforcement', clip_count=5) and ('Teaching Moments', clip_count=3)."
            "\n4) One workflow run is logged for this package with dag_name='pre_series_package', status='success', "
            "start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and "
            "log_s3_path='s3://workflows/pre_series/{game_pk}.log'."
            "\n5) Trend filtering has been materialized once for auditability with the policy thresholds "
            "min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.\n"
            "Return nothing."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date": "2024-07-23"}),
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk": 2024000011, "team_id": 10}),

            # Persist policy-governed trend thresholds (EB+FDR gate recorded deterministically)
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),

            # Create the pre-game scouting report with canonical naming derived from resolved identifiers
            Action(name="create_scouting_report", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf"
            }),  # -> {"report_id": 13}

            # Attach the two curated insights (template-enforced text and allowed types)
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 1,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.412
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "predictability_firstpitchswing_low",
                "insight_type": "predictability",
                "supporting_stat_value": 0.193
            }),

            # Create the two standard playlists; links are provided by the system if omitted; clip counts are explicit per policy
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 5
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 3
            }),

            # Log the workflow run deterministically
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_package",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://workflows/pre_series/2024000011.log"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_004",
        instruction=(
            "You furnish a pre-game scouting packet for our club (team_id 10) targeting the first scheduled game on or after 2024-07-23. "
            "Evaluate success solely by the presence of the following end-state components, without implying any particular method: "
            "• A pre-game report whose identifiers are exactly: narrative 'pre_game_series_context', slides URL https://docs.google.com/presentation/d/pre_game_series_context, "
            "and PDF s3://reports/scouting/pre_game/2024000011.pdf tied to the correct game. "
            "• Two curated insights included verbatim: player 1 → 'tendency_firstpitch_low' with value 0.62; player 4 → 'execution_slider_away' with value 0.71. "
            "• One playlist named 'Opponent Pitcher Tendencies' containing 4 clips. "
            "• Pitch-location metadata represented in the club’s 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0), stored with the packet. "
            "• A single activity record labeled 'pre_game_scouting' at 2025-08-14T00:00:00Z with its log at "
            "s3://logs/workflows/pre_game_scouting/2025-08-14/run.json."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date": "2024-07-23", "team_id": 10}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000011}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000011,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_game_series_context",
                "gslides_link": "https://docs.google.com/presentation/d/pre_game_series_context",
                "s3_pdf_path": "s3://reports/scouting/pre_game/2024000011.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 1,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.62
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.71
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_game_scouting",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/pre_game_scouting/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_005",
        instruction=(
            "You deliver a post-game analytics packet for game 2024000008, judged only by the final artifacts and metadata below (no specific method implied): "
            "• A post-game report identified by narrative 'post_game_review' with links https://docs.google.com/presentation/d/post_game_review and "
            "s3://reports/scouting/post_game/2024000008.pdf for the correct game. "
            "• Three execution grades recorded exactly as follows: pitch 29 intended 'down_away' vs actual 'down_middle' (miss 2.4 in); "
            "pitch 33 intended 'up_in' vs actual 'middle_in' (miss 6.8 in); pitch 46 intended 'down_away' vs actual 'down_away' (miss 1.2 in). "
            "• Two curated insights included verbatim: player 8 → 'situational_risp_success' 0.54; player 4 → 'execution_breakingball_high' 0.67. "
            "• Two coaching playlists titled 'Positive Reinforcement' (5 clips) and 'Teaching Moments' (3 clips). "
            "• Pitch-location metadata stored in the club’s 12×12 catcher-view representation (x −1.5..1.5, z 1.0..4.0). "
            "• A strict >1.5 leverage roll-up available for the game. "
            "• One activity record labeled 'post_game_review' at 2025-08-14T00:00:00Z with its log at s3://logs/workflows/post_game_review/2025-08-14/run.json."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.67
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/post_game_review/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_006",
        instruction=(
            "You are accountable for Team 10’s series build anchored to the first scheduled game on or after 2024-06-01. Provide a single terminal state "
            "that is validated entirely by the recorded content: the anchor game shows a single pre-game scouting packet whose narrative reads "
            "pre_series_policy_v1, whose slide deck is stored at https://slides.example.org/pre/2024000006, and whose archived PDF is "
            "s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf; the opponent is captured and no more than two probables are listed for that "
            "opponent; a 12×12 strike-zone lattice for the anchor is persisted over a lateral span of −0.95 to 0.95 and a vertical span of 1.5 to 3.5; the "
            "trend review on file documents empirical-Bayes shrinkage with FDR control at thresholds of at least 50 pitches, 30 swings, and 25 batted balls "
            "(α=0.1); an ingestion log referencing the probables feed reports status 204 with zero records; and a successful pre-series run labeled "
            "pre_series_build appears for game 2024000006 with start and end timestamps of 2025-08-14T00:00:00Z and a log at "
            "s3://logs/pre_series/2024000006/2025-08-14.json."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date": "2024-06-01"}),
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk": 2024000006, "team_id": 10}),
            Action(name="log_ingestion_event", kwargs={"source_name": "probables_feed", "status_code": 204, "records_ingested": 0}),
            Action(name="list_probable_pitchers", kwargs={"team_id": 9, "limit": 2, "order_by": "full_name ASC"}),
            Action(name="create_scouting_report", kwargs={"report_type": "Pre-Game", "game_pk": 2024000006, "core_narrative_text": "pre_series_policy_v1", "gslides_link": "https://slides.example.org/pre/2024000006", "s3_pdf_path": "s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf"}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000006, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="log_workflow_run", kwargs={"dag_name": "pre_series_build", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/pre_series/2024000006/2025-08-14.json", "game_pk": 2024000006}),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_007",
        instruction=(
            "You provide a pre-game scouting packet for our club (team_id 10) tied to the first scheduled game on or after 2024-07-23. "
            "Your work is accepted only if the database’s terminal state, for that game, contains exactly: "
            "• one pre-game report identified by narrative 'pre_game_series_context' with slide link https://docs.google.com/presentation/d/pre_game_series_context "
            "and PDF s3://reports/scouting/pre_game/2024000011.pdf; "
            "• two curated items recorded as player 1 → 'tendency_firstpitch_low' with value 0.62 and player 4 → 'execution_slider_away' with value 0.71; "
            "• one playlist named 'Opponent Pitcher Tendencies' with 4 clips; "
            "• pitch-location data expressed in the club’s 12×12 catcher-view convention (x −1.5..1.5, z 1.0..4.0); and "
            "• one activity record labeled 'pre_game_scouting' with start=end 2025-08-14T00:00:00Z at s3://logs/workflows/pre_game_scouting/2025-08-14/run.json. "
            "No method is prescribed—only this end state matters."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date": "2024-07-23", "team_id": 10}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000011}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000011,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_game_series_context",
                "gslides_link": "https://docs.google.com/presentation/d/pre_game_series_context",
                "s3_pdf_path": "s3://reports/scouting/pre_game/2024000011.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 1,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.62
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.71
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_game_scouting",
                "game_pk": 2024000011,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/pre_game_scouting/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_008",
        instruction=(
            "You provide an opponent series plan for game 2024000004 focused on our club (team_id 6). "
            "Acceptance hinges only on the final database state that, for that game, contains: "
            "• one pre-game report with narrative 'series_pitching_plan' and links https://docs.google.com/presentation/d/series_pitching_plan "
            "and s3://reports/scouting/opponent_analysis/2024000004.pdf; "
            "• two curated items recorded exactly as player 5 → 'tendency_firstpitch_low' (0.58) and player 7 → 'execution_slider_away' (0.73); "
            "• two playlists—'Opponent Pitcher Tendencies' (4 clips) and 'Baserunning Alerts' (3 clips); "
            "• pitch-location data stored in the club’s 12×12 catcher-view convention (x −1.5..1.5, z 1.0..4.0); and "
            "• one activity record labeled 'series_pitching_plan' with start=end 2025-08-14T00:00:00Z at "
            "s3://logs/workflows/series_pitching_plan/2025-08-14/run.json. No procedure is prescribed."
        ),
        actions=[
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk": 2024000004, "team_id": 6}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000004}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000004,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.58
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 7,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.73
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Baserunning Alerts", "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "series_pitching_plan",
                "game_pk": 2024000004,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/series_pitching_plan/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_009",
        instruction=(
            "You deliver a coach-visible in-game highlights package for game 2024000007. "
            "Acceptance is strictly based on the end state: the database shows exactly two coach-visible high-impact moments at 2025-08-14T00:00:00Z "
            "(pitch 5, leverage 2.40, label 'HR_to_LF_spike'; pitch 6, leverage 2.74, label 'BasesLoaded_K'), plus one coach-visible bench note "
            "'mound_visit_recommendation' at leverage 0.00; pitch-location data expressed in the club’s 12×12 catcher-view convention "
            "(x −1.5..1.5, z 1.0..4.0); and a single activity record labeled 'in_game_highlights' with start=end 2025-08-14T00:00:00Z at "
            "s3://logs/workflows/in_game_highlights/2025-08-14/run.json. The method is not prescribed—only this terminal state matters."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000007}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000007,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_auto_bookmark_event", kwargs={
                "game_pk": 2024000007, "pitch_id": 5, "leverage_index": 2.40, "narration": "HR_to_LF_spike",
                "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True, "is_manual_alert": False
            }),
            Action(name="create_auto_bookmark_event", kwargs={
                "game_pk": 2024000007, "pitch_id": 6, "leverage_index": 2.74, "narration": "BasesLoaded_K",
                "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True, "is_manual_alert": False
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000007, "suggestion_text": "mound_visit_recommendation", "leverage_index": 0.00,
                "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 15, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "in_game_highlights",
                "game_pk": 2024000007,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/in_game_highlights/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_010",
        instruction=(
            "You deliver a post-game analytics packet for game 2024000008. "
            "The packet is accepted only if the database contains: one post-game report identified by narrative 'post_game_review' with links "
            "https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf; "
            "three execution grades recorded precisely as pitch 29 intended 'down_away' vs actual 'down_middle' (miss 2.4 in), "
            "pitch 33 intended 'up_in' vs actual 'middle_in' (miss 6.8 in), and pitch 46 intended 'down_away' vs actual 'down_away' (miss 1.2 in); "
            "two curated items recorded as player 8 → 'situational_risp_success' (0.54) and player 4 → 'execution_breakingball_high' (0.67); "
            "two coaching playlists—'Positive Reinforcement' (5 clips) and 'Teaching Moments' (3 clips); "
            "pitch-location data expressed in the club’s 12×12 catcher-view convention (x −1.5..1.5, z 1.0..4.0); and "
            "a single activity record whose fields unambiguously include dag_name 'post_game_review', game_pk 2024000008, status 'completed', "
            "start=end 2025-08-14T00:00:00Z, and log path s3://logs/workflows/post_game_review/2025-08-14/run.json. "
            "No procedure is prescribed—only this terminal state."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.67
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "game_pk": 2024000008,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/post_game_review/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_011",
        instruction=(
            "You compile a two-hitter post-game focus packet for game 2024000008. "
            "The packet is accepted only if the database reflects: one post-game report with narrative 'two_hitter_focus' and links "
            "https://docs.google.com/presentation/d/two_hitter_focus and s3://reports/scouting/post_game/2024000008_two_hitter_focus.pdf; "
            "four curated items recorded exactly as player 2 → 'situational_risp_success' (0.42) and 'execution_slider_away' (0.66), "
            "player 9 → 'tendency_firstpitch_low' (0.59) and 'execution_breakingball_high' (0.61); "
            "two coaching playlists—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips); "
            "pitch-location data expressed in the club’s 12×12 catcher-view convention (x −1.5..1.5, z 1.0..4.0); and "
            "one activity record labeled 'two_hitter_focus' with start=end 2025-08-14T00:00:00Z at s3://logs/workflows/two_hitter_focus/2025-08-14/run.json. "
            "Only the terminal state matters; no method is prescribed."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "two_hitter_focus",
                "gslides_link": "https://docs.google.com/presentation/d/two_hitter_focus",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008_two_hitter_focus.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.42
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.66
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 9,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.59
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 9,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.61
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "two_hitter_focus",
                "game_pk": 2024000008,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/two_hitter_focus/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_012",
        instruction=(
            "You complete a single, policy-compliant post-game review for game_pk 2024000008 that resolves to one uniquely determined final state. "
            "Acceptance criteria: the review exists with narrative tag 'umpire_exec_review_v1', slides https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; "
            "a trends QC pass uses empirical-Bayes shrinkage with FDR control at 0.10 (min_pitches 50, min_swings 30, min_bbe 25); "
            "a catcher-view 12×12 strike-zone representation is computed for x∈[−0.95,0.95], z∈[1.5,3.5] (no persistence); "
            "two curated playlists are attached to that review exactly as required: Positive Reinforcement (3 clips) and Teaching Moments (2 clips); "
            "a high-leverage summary uses threshold 1.5; "
            "and the run is recorded as successful with start/end 2025-08-14T00:00:00Z and log s3://logs/post_game/2025-08-14_g2024000008.json. Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": False
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "leverage_threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008.json",
                "game_pk": 2024000008
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_013",
        instruction=(
            "You are the analytics coordinator for Team 10. Deliver a deterministic post-game package for game_pk=2024000007 (games.game_status=='Final').\n"
            "\nAcceptance criteria (single, deterministic terminal state):\n"
            "1) One scouting report exists for that game with exactly: report_type='post-game', s3_pdf_path='s3://reports/scouting/post/2024-06-14_g2024000007_team10.pdf', gslides_link='https://slides.example.org/post/2024000007', core_narrative_text='post_game_policy_v1'.\n"
            "2) Exactly two curated insights are attached to that report: (player_id=2, insight_type='tendency', insight_text='tendency_chaserate_high', supporting_stat_value=0.412) and (player_id=11, insight_type='predictability', insight_text='predictability_firstpitchswing_low', supporting_stat_value=0.193). Insight text format strictly '[category]_[metric]_[bucket]' with lowercase/digits only.\n"
            "3) Exactly two video playlists exist for that report: ('Positive Reinforcement', clip_count=5) and ('Teaching Moments', clip_count=3).\n"
            "4) Pitch data was canonicalized and a 12x12 catcher-view zone encoding was computed and persisted using bounds min_x=-0.95, max_x=0.95, min_z=1.5, max_z=3.5.\n"
            "5) A leverage summary is computed for game_pk=2024000007 with strict threshold >1.5.\n"
            "6) A workflow run is recorded as status='success' with dag_name='post_game_pkg', start_time_utc='2025-08-14T11:00:00Z', end_time_utc='2025-08-14T11:09:00Z', log_s3_path='s3://ops/logs/post_game_pkg/2025-08-14_g2024000007.json'.\n"
            "\nNote: The s3_pdf_path above is a fixed backfill artifact name for audit reproducibility; do not derive its date segment from game_date.\n"
            "\nPolicy references you must honor:\n"
            "• Post-game reports require games.game_status=='Final'.\n"
            "• Canonicalize raw pitch types before spatial encodings; 12x12 bounds must be explicit; use persist=True when writing back.\n"
            "• Dev playlist categories enforce clip ranges: Positive Reinforcement ∈[3,5], Teaching Moments ∈[2,3].\n"
            "• 'High leverage' uses strict >1.5.\n"
            "Return no values."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000007}),
            Action(name="canonicalize_pitch_types", kwargs={"scope": "all"}),
            Action(name="grid_encode_pitch_locations", kwargs={"min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000007, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000007", "s3_pdf_path": "s3://reports/scouting/post/2024-06-14_g2024000007_team10.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.412}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "predictability_firstpitchswing_low", "insight_type": "predictability", "supporting_stat_value": 0.193}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000007, "threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_pkg", "status": "success", "start_time_utc": "2025-08-14T11:00:00Z", "end_time_utc": "2025-08-14T11:09:00Z", "log_s3_path": "s3://ops/logs/post_game_pkg/2025-08-14_g2024000007.json", "game_pk": 2024000007})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_014",
        instruction=(
            "You assemble a single pre-series scouting packet for game_pk 2024000011 that resolves to one uniquely determined final state, without naming any tools. "
            "Acceptance criteria (goal-oriented, policy-guided, tool-agnostic): "
            "• Game context reflects that the matchup is Scheduled for 2024-07-23 (home_team_id=10 vs. away_team_id=8). "
            "• A data-ingestion checkpoint is recorded exactly as: source_name='probables_feed', status_code=200, records_ingested=2, ingested_at_utc='2025-08-14T00:00:00Z'. "
            "• A catcher-view 12×12 strike-zone representation for this game is generated and persisted for x∈[−0.95,0.95], z∈[1.5,3.5] (no hidden defaults). "
            "• Trends QC is explicitly run with empirical-Bayes shrinkage under FDR control at 0.10 and minima (min_pitches=50, min_swings=30, min_bbe=25). "
            "• One pre-game scouting document exists for this game with core_narrative_text='pre_series_policy_v1', slide link https://slides.example.org/pre/2024000011, and PDF path s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf. "
            "• That document includes a single curated insight tied to player_id=7 using insight_text='tendency_trendflags_fdr10', insight_type='tendency', and supporting_stat_value=0.1. "
            "• The run is logged as status='success' under dag name 'pre_series_packet' with start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', log_s3_path='s3://logs/pre_series/2025-08-14_g2024000011.json', and associated to this game. "
            "Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000011}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000011,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_trendflags_fdr10",
                "insight_type": "tendency",
                "supporting_stat_value": 0.1
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_packet",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/pre_series/2025-08-14_g2024000011.json",
                "game_pk": 2024000011
            })
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_015",
        instruction=(
            "You deliver a single, post-game officiating and pitch-execution review for game_pk 2024000008 that resolves to one uniquely determined final state without naming specific tools. "
            "Acceptance criteria (goal-oriented, policy-guided, tool-agnostic): "
            "• Game context reflects that the game is Final. "
            "• An officiating calibration entry exists for the plate umpire assigned to this game, explicitly umpire_id=2 from the provided data, with zone_shift_x=−0.05, zone_shift_z=0.07, calibration_error_pct=2.3, and confidence_interval='90%'. "
            "• Pitch-execution evaluations exist for exactly three pitches in this game: "
            "  – pitch_id=28: intended=glove-side-high, actual=glove-side-high, miss_distance_inches=2.5; "
            "  – pitch_id=29: intended=arm-side-low,  actual=arm-side-mid,  miss_distance_inches=6.8; "
            "  – pitch_id=31: intended=down-middle,    actual=down-middle,    miss_distance_inches=1.9. "
            "• A catcher-view 12×12 strike-zone representation for this game is generated and persisted for x∈[−0.95,0.95], z∈[1.5,3.5]. "
            "• One post-game scouting document exists for this game with core_narrative_text='umpire_exec_review_v1', a slide link https://slides.example.org/post/2024000008, and a PDF path s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; this document is the one to which any media is attached. "
            "• Exactly two curated video playlists are attached to that same document using policy-compliant names and clip counts: "
            "  'Positive Reinforcement' with clip_count=3 and 'Teaching Moments' with clip_count=2. "
            "• A leverage summary for this game is computed using an explicit threshold of 1.5 (no hidden defaults). "
            "• The run is logged as status='success' under dag name 'post_game_review' with start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://logs/post_game/2025-08-14_g2024000008.json'. "
            "Return nothing."
        ),
        actions=[
            # Confirm game is Final (policy gate)
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),

            # Record the plate-umpire calibration deterministically
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),

            # Three deterministic pitch-execution grades
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),

            # Persist the catcher-view 12x12 zone encoding for this game
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),

            # Create the post-game scouting document with deterministic content
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),

            # Attach policy-compliant curated playlists to the created report (first report_id in a clean reset is 13)
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),

            # Compute leverage summary with explicit threshold (no hidden default)
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),

            # Deterministic run log
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008.json",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_016",
        instruction=(
            "You complete Monday player-development check-ins for the week of 2025-08-11 for players 11 and 12. "
            "Only the terminal database state is evaluated, and it must show: "
            "one weekly development PDF per player at the stated paths (player 11 → s3://reports/player_dev/11/2025-08-11.pdf; "
            "player 12 → s3://reports/player_dev/12/2025-08-11.pdf); "
            "one Approved goal per player with target review date 2025-08-25 "
            "(player 11 → 'dev_goal_contact_quality' by coach 22; player 12 → 'dev_goal_zone_control' by coach 23); "
            "for game 2024000002, a development packet per player—player 11 narrative 'dev_weekly_packet_2025_08_11_p11' with links "
            "(slides https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11, PDF s3://reports/dev_packages/11/2025-08-11.pdf) "
            "and player 12 narrative 'dev_weekly_packet_2025_08_11_p12' with links "
            "(slides https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11, PDF s3://reports/dev_packages/12/2025-08-11.pdf); "
            "each packet contains exactly two playlists: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). "
            "A single workflow activity labeled 'weekly_dev_checkins' is recorded for game_pk 2024000002 with start=end 2025-08-14T00:00:00Z "
            "and log path s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json."
        ),
        actions=[
            Action(name="create_player_dev_report", kwargs={
                "player_id": 11,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/11/2025-08-11.pdf"
            }),
            Action(name="create_player_dev_report", kwargs={
                "player_id": 12,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/12/2025-08-11.pdf"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 11,
                "player_id": 11,
                "goal_text": "dev_goal_contact_quality",
                "coach_id": 22,
                "target_review_date": "2025-08-25"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 12,
                "player_id": 12,
                "goal_text": "dev_goal_zone_control",
                "coach_id": 23,
                "target_review_date": "2025-08-25"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p11",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/11/2025-08-11.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p12",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/12/2025-08-11.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 14, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 14, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "weekly_dev_checkins",
                "game_pk": 2024000002,
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_017",
        instruction=(
            "You are finalizing the post-game packet for game_pk 2024000008. "
            "Acceptance criteria (final database state): "
            "• The referenced game is in status 'Final'. "
            "• Pitch locations for this game are persisted in the standard catcher-view 12×12 grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0]. "
            "• Execution grading exists for exactly these five pitches with the stated fields: "
            "(29, intended down_away, actual down_middle, miss 2.4in), "
            "(33, intended up_in, actual middle_in, miss 6.8in), "
            "(46, intended down_away, actual down_away, miss 1.2in), "
            "(17, intended up_away, actual up_middle, miss 4.1in), "
            "(45, intended down_in, actual middle_in, miss 5.0in). "
            "• Exactly one post-game scouting report is linked to game_pk 2024000008 with narrative 'post_game_review' and links "
            "https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf. "
            "• That report has exactly two curated entries: situational_risp_high with value 0.54 for player 8, and execution_fastball_high with value 0.67 for player 4. "
            "• Two video playlists exist for the report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). "
            "• One workflow run exists for dag_name 'post_game_review' and game_pk 2024000008 with status 'success', "
            "start_time_utc == end_time_utc == '2025-08-13T00:00:00Z', and log path s3://workflow/logs/post_game_review/2024000008/2025-08-13.log. "
            "No additional output."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.67
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-13T00:00:00Z",
                "end_time_utc": "2025-08-13T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-13.log"
            })
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_018",
        instruction=(
            "You are compiling the post-game analysis packet for game_pk 2024000008. "
            "Acceptance criteria (final database state): "
            "• The referenced game is 'Final'. "
            "• Pitch locations for this game are persisted in the catcher-view 12×12 grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0]. "
            "• Execution grading exists for exactly these three pitches with the stated fields: "
            "(29, intended down_away, actual down_middle, miss 2.4in), "
            "(33, intended up_in, actual middle_in, miss 6.8in), "
            "(46, intended down_away, actual down_away, miss 1.2in). "
            "• Exactly one post-game report is linked to game_pk 2024000008 with narrative 'post_game_review' and links "
            "https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf. "
            "• That report has exactly two curated entries: situational_risp_high with value 0.54 for player 8, and execution_fastball_high with value 0.67 for player 4. "
            "• Two video playlists exist for the report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). "
            "• One workflow run exists for dag_name 'post_game_review' and game_pk 2024000008 with status 'success', "
            "start_time_utc == end_time_utc == '2025-08-13T00:00:00Z', and log path s3://workflow/logs/post_game_review/2024000008/2025-08-13.log. "
            "No other outputs are required."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.67
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-13T00:00:00Z",
                "end_time_utc": "2025-08-13T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-13.log"
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_019",
        instruction=(
            "You are the pre-series scouting lead for Team 10. Build a spatially standardized opponent scouting package using the next scheduled game on/after 2024-07-23. "
            "Acceptance criteria (single, deterministic terminal state, outcome-based):"
            "\n• Game selection anchored at current_date '2024-07-23' resolves to game_pk 2024000011 (Team 10 vs opponent_team_id 8)."
            "\n• Pitch data are harmonized to the house pitch-type schema prior to any spatial encodings."
            "\n• The pitch-location grid representation is stored at 12×12 resolution with bounds min_x=-0.95, max_x=0.95, min_z=1.5, max_z=3.5 and is persisted back to pitch records."
            "\n• One pre-game scouting report for that game records: report_type 'Pre-Game', "
            "s3_pdf_path 's3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf', "
            "gslides_link 'https://slides.example.org/pre/2024000011', and core_narrative_text 'pre_series_spatial_v1'."
            "\n• Exactly two curated insights are attached using the deterministic template strings: "
            "player_id 2 → 'tendency_groundballrate_high' (type 'tendency', supporting_stat_value 0.531); "
            "player_id 7 → 'situational_twooutswing_low' (type 'situational', supporting_stat_value 0.274)."
            "\n• Two general playlists exist for the report with clip counts 5 and 4, titled 'Opponent Heatmap Overview' and 'Zone Exploits Plan'."
            "\n• Workflow metadata shows a successful run for dag 'pre_series_spatial_pipeline' with start_time_utc and end_time_utc set to '2025-08-14T00:00:00Z' and the log path "
            "'s3://workflows/pre_series_spatial_pipeline/g2024000011/2025-08-14.json'."
            "\nPolicy references: explicit date anchor; canonicalization precedes spatial work; fixed grid bounds and deterministic artifacts; acceptance criteria avoid prescribing API steps."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date":"2024-07-23"}),
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk":2024000011,"team_id":10}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk":2024000011}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk":2024000011,"min_x":-0.95,"max_x":0.95,"min_z":1.5,"max_z":3.5,"persist":True}),
            Action(name="create_scouting_report", kwargs={"report_type":"Pre-Game","game_pk":2024000011,"core_narrative_text":"pre_series_spatial_v1","gslides_link":"https://slides.example.org/pre/2024000011","s3_pdf_path":"s3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id":13,"player_id":2,"insight_text":"tendency_groundballrate_high","insight_type":"tendency","supporting_stat_value":0.531}),
            Action(name="add_curated_insight", kwargs={"report_id":13,"player_id":7,"insight_text":"situational_twooutswing_low","insight_type":"situational","supporting_stat_value":0.274}),
            Action(name="create_video_playlist", kwargs={"report_id":13,"playlist_name":"Opponent Heatmap Overview","clip_count":5}),
            Action(name="create_video_playlist", kwargs={"report_id":13,"playlist_name":"Zone Exploits Plan","clip_count":4}),
            Action(name="log_workflow_run", kwargs={"dag_name":"pre_series_spatial_pipeline","game_pk":2024000011,"status":"success","start_time_utc":"2025-08-14T00:00:00Z","end_time_utc":"2025-08-14T00:00:00Z","log_s3_path":"s3://workflows/pre_series_spatial_pipeline/g2024000011/2025-08-14.json"})
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_020",
        instruction=(
            "You are assembling a pre-series opponent scouting packet. Treat upstream ingestion as complete.\n"
            "Acceptance criteria (terminal database state):\n"
            "• The packet targets game_pk 2024000004 and includes a pre-game brief whose core narrative is series_pitching_plan with links https://docs.google.com/presentation/d/series_pitching_plan and s3://reports/scouting/opponent_analysis/2024000004.pdf.\n"
            "• To meet proposal realism, the underlying pitch data for this target game reflects: (i) harmonized pitch-type labels across the dataset and (ii) pitch locations discretized into a catcher-view 12×12 strike-zone grid using bounds x∈[-1.5,1.5] and z∈[1.0,4.0], with the encoded zone cell persisted.\n"
            "• Four curated insights are attached to that brief using the required key template with these values: situational_risp_high (0.50) for player_id 2; predictability_firstpitch_high (0.36) for player_id 4; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8.\n"
            "• Two curated video playlists are attached to that brief: Positive Reinforcement (3 clips) and Teaching Moments (2 clips).\n"
            "• The workflow ledger records a successful run for this packet with start_time_utc == end_time_utc == 2025-08-18T00:00:00Z at s3://workflow/logs/pre_series_scouting_packet/2024000004/2025-08-18.log.\n"
            "No additional outputs are required."
        ),
        actions=[
            # Proposal realism/QC/modeling coverage (harmonization + grid encoding persisted)
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000004}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000004,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            # Pre-game brief
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            # Curated insights (policy-compliant keys)
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.50
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.36
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            # Playlists (correct arg key)
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            # Workflow record
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_scouting_packet",
                "game_pk": 2024000004,
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/pre_series_scouting_packet/2024000004/2025-08-18.log"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_021",
        instruction=(
            "You are finalizing a compact post-game mini-review for our completed home game.\n"
            "Acceptance criteria (terminal database state):\n"
            "• The post-game brief targets game_pk 2024000008, carries core narrative post_game_review, and includes the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• The database reflects three specific pitch-execution evaluations for this game, covering pitch_ids 29, 33, and 46 with their respective intended/actual quadrants and miss distances (inches) as follows: (29, down_away → down_middle, 2.4), (33, up_in → middle_in, 6.8), (46, down_away → down_away, 1.2).\n"
            "• To satisfy policy for post-game communication, two curated video playlists are attached to that brief: Positive Reinforcement (3 clips) and Teaching Moments (2 clips).\n"
            "No additional outputs are required."
        ),
        actions=[
            # Gate on the completed game context
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            # Three execution evaluations (deterministic, policy-compliant fields)
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            # Post-game brief
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: attach required curated playlists (correct key: playlist_name)
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_022",
        instruction=(
            "You are finalizing a coach-facing post-game review for our home game. Assume upstream ingestion/QC are already approved and the game is complete.\n"
            "Acceptance criteria (terminal database state):\n"
            "• A post-game scouting brief exists for game_pk 2024000008 with core narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Execution evaluation is recorded for exactly five pitches from this game with the following intent/actual quadrants and miss distances (inches):\n"
            "  – pitch_id 29: intended down_away, actual down_middle, miss 2.4\n"
            "  – pitch_id 33: intended up_in, actual middle_in, miss 6.8\n"
            "  – pitch_id 46: intended down_away, actual down_away, miss 1.2\n"
            "  – pitch_id 17: intended up_away, actual up_middle, miss 4.1\n"
            "  – pitch_id 45: intended down_in, actual middle_in, miss 5.0\n"
            "• Four curated insights are attached to that brief using the required key template and values: \n"
            "  situational_risp_high (0.55) for player_id 8; predictability_firstpitch_high (0.31) for player_id 2; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8.\n"
            "• Four video playlists are attached to the brief: two named Positive Reinforcement with 3 clips each, and two named Teaching Moments with 2 clips each.\n"
            "• The workflow ledger records a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc == end_time_utc == 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.\n"
            "No additional outputs are required."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            # FIX: use the correct key 'playlist_name' (not 'name')
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review_packet",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_023",
        instruction=(
            "Your objective is to leave the database in a single, uniquely determined state for game_pk 2024000008 (a completed game on 2024-03-05). "
            "Acceptance criteria (policy-guided, tool-agnostic; describe only the final state): "
            "• The plate-umpire for this review is umpire_id=2, and exactly one calibration record for this game exists with zone_shift_x=-0.05, zone_shift_z=0.07, calibration_error_pct=2.3, confidence_interval='90%'. "
            "• Exactly three execution assessments exist for this game with these fields: "
            "  – pitch_id=28, intended='glove-side-high', actual='glove-side-high', miss_distance_inches=2.5; "
            "  – pitch_id=29, intended='arm-side-low', actual='arm-side-mid', miss_distance_inches=6.8; "
            "  – pitch_id=31, intended='down-middle', actual='down-middle', miss_distance_inches=1.9. "
            "• A catcher-view 12×12 strike-zone mapping is computed for x∈[-0.95,0.95], z∈[1.5,3.5] without persisting it. "
            "• Exactly one post-game scouting document for this game exists with core_narrative_text='post_game_policy_v1', slide link https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf. "
            "• Exactly two curated playlists are linked to that document: 'Positive Reinforcement' with clip_count=4 and 'Teaching Moments' with clip_count=2. "
            "• One workflow run is logged as status='success' under dag_name='post_game_exec_review' with start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://logs/post_game/2025-08-14_g2024000008.json', associated to this game. "
            "Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": False
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 4
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_exec_review",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008.json",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_024",
        instruction=(
            "You are finalizing a deterministic player-development update. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without describing steps or naming tools:\n"
            "• Exactly six development goals exist—two for development report 10 (player 11), two for development report 6 (player 10), plus two additional goals again for those same report/player pairs—each recorded with coach 501 and target review date 2024-05-06.\n"
            "• For dev_report_id 10 and player_id 11, the goals present are:\n"
            "  – raise_chase_swing_decisions_10pct\n"
            "  – optimize_two_strike_approach\n"
            "  – improve_line_drive_rate_5pct\n"
            "• For dev_report_id 6 and player_id 10, the goals present are:\n"
            "  – improve_zone_coverage_inner_third\n"
            "  – shorten_load_timing\n"
            "  – improve_baserun_jump_reads\n"
            "• All six goals appear exactly once and have status 'Approved'. No other goals are created or modified.\n"
            "• A trends QC pass is recorded using empirical-Bayes shrinkage with FDR control at 0.10 and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• A single workflow run record exists with dag name 'player_development_goals', status 'success', start and end timestamps set to 2024-05-06T00:00:00Z, and log path 's3://logs/dev/2024-05-06_objectives.json'. No other records are changed."
        ),
        actions=[
            # Create two initial goals (dev_report 10/player 11; dev_report 6/player 10)
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "raise_chase_swing_decisions_10pct", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "improve_zone_coverage_inner_third", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve the two initial goals (goal_ids are deterministic in this snapshot)
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),

            # Create two additional goals for the same report/player pairs (dependent on prior approvals' dev_report_id/player_id values)
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "optimize_two_strike_approach", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "shorten_load_timing", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve those two goals
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 22}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 23}),

            # Create a third goal for each same report/player pair
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "improve_line_drive_rate_5pct", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "improve_baserun_jump_reads", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve the final two goals
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 24}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 25}),

            # Trends QC (EB shrinkage, FDR 0.10, with required minima)
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "use_eb_shrinkage": True, "control": "FDR"}),

            # Workflow bookkeeping
            Action(name="log_workflow_run", kwargs={"dag_name": "player_development_goals", "status": "success", "start_time_utc": "2024-05-06T00:00:00Z", "end_time_utc": "2024-05-06T00:00:00Z", "log_s3_path": "s3://logs/dev/2024-05-06_objectives.json"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_025",
        instruction=(
            "Your objective is to produce a single, uniquely determined post-game calling and execution memo for game_pk 2024000008. "
            "Acceptance criteria (final-state only, no procedure): "
            "• The review targets plate-umpire umpire_id=2 and the database contains exactly one calibration entry for this game with zone_shift_x=-0.04, zone_shift_z=0.05, calibration_error_pct=1.8, confidence_interval='90%'. "
            "• Exactly two execution assessments exist for this game: "
            "  – pitch_id=14 with intended='arm-side-high', actual='arm-side-high', miss_distance_inches=2.2; "
            "  – pitch_id=15 with intended='glove-side-low', actual='glove-side-mid', miss_distance_inches=5.6. "
            "• A catcher-view 12×12 zone mapping for x∈[-0.95,0.95], z∈[1.5,3.5] is persisted. "
            "• Exactly one post-game memo document exists with core_narrative_text='post_game_calling_review_v1', slide link https://slides.example.org/post/2024000008_calling, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_calling.pdf. "
            "• Exactly two curated playlists are linked to that document: 'Positive Reinforcement' with clip_count=3 and 'Teaching Moments' with clip_count=3. "
            "• Exactly one workflow run is logged with dag_name='post_game_calling_memo', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', log_s3_path='s3://logs/post_game/2025-08-14_g2024000008_calling.json', associated to this game. "
            "Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.04,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.8,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 14,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-high",
                "actual_quadrant": "arm-side-high",
                "miss_distance_inches": 2.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 15,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-low",
                "actual_quadrant": "glove-side-mid",
                "miss_distance_inches": 5.6
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_calling_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008_calling",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_calling.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_calling_memo",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008_calling.json",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_26",
        instruction=(
            "You are publishing a post-game addendum for a completed contest. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without describing steps or naming tools:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest (Final).\n"
            "• A single ingest record exists for this run with: source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-03-05T00:00:00Z'.\n"
            "• Trend anomalies are filtered using a false-discovery rate of 0.10 with empirical-Bayes shrinkage and minimums of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated using bounds x∈[−0.95, 0.95] and z∈[1.5, 3.5] and is persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000008 with:\n"
            "  – core narrative text: post_game_policy_v1\n"
            "  – slide link: https://slides.example.org/post/2024000008\n"
            "  – PDF path: s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf\n"
            "• Two curated insights are added to the report for player_id 7 using deterministic, policy-compliant values:\n"
            "  – insight_text: predictability_firstpitchstrike_high, insight_type: predictability, supporting_stat_value: 0.68\n"
            "  – insight_text: situational_rispcontact_high, insight_type: situational, supporting_stat_value: 0.29\n"
            "• Exactly two curated video playlists are attached to this same report:\n"
            "  – “Positive Reinforcement” with 3 clips\n"
            "  – “Teaching Moments” with 2 clips\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a leverage threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.29
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_addendum",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_addendum.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_027",
        instruction=(
            "Your objective is to finalize an integrated post-game analysis packet for game_pk 2024000008, resolving to one uniquely determined database state. "
            "Acceptance criteria (outcome-only, tool-agnostic): "
            "• The review targets plate umpire umpire_id=2 and the database holds exactly one calibration record for this game with zone_shift_x=-0.03, zone_shift_z=0.06, calibration_error_pct=2.1, confidence_interval='90%'. "
            "• Exactly three execution assessments exist for this game with these values: "
            "  – pitch_id=28, intended='glove-side-high', actual='glove-side-high', miss_distance_inches=2.5; "
            "  – pitch_id=29, intended='arm-side-low', actual='arm-side-mid', miss_distance_inches=6.8; "
            "  – pitch_id=31, intended='down-middle', actual='down-middle', miss_distance_inches=1.9. "
            "• A catcher-view 12×12 zone mapping for x∈[-0.95,0.95], z∈[1.5,3.5] is persisted. "
            "• Exactly one post-game document exists with core_narrative_text='post_game_integrated_v1', slide link https://slides.example.org/post/2024000008_integrated, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_integrated.pdf. "
            "• Exactly two curated insights are linked to that document: "
            "  – player_id=9 with insight_text='situational_rispcontact_low', insight_type='situational', supporting_stat_value=0.24; "
            "  – player_id=7 with insight_text='execution_edgehit_high', insight_type='execution', supporting_stat_value=0.78. "
            "• Exactly two curated playlists are linked to that document: 'Positive Reinforcement' with clip_count=5 and 'Teaching Moments' with clip_count=2. "
            "• Exactly one workflow run is logged with dag_name='post_game_integrated', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://logs/post_game/2025-08-14_g2024000008_integrated.json', associated to this game. "
            "Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 2.1,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_integrated_v1",
                "gslides_link": "https://slides.example.org/post/2024000008_integrated",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_integrated.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 9,
                "insight_text": "situational_rispcontact_low",
                "insight_type": "situational",
                "supporting_stat_value": 0.24
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "execution_edgehit_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.78
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 5
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_integrated",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008_integrated.json",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_028",
        instruction=(
            "You are finalizing a post-game analytics packet for a completed game. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without describing steps or naming tools:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest (Final).\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated using bounds x∈[−0.95, 0.95] and z∈[1.5, 3.5] and is persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000008 with:\n"
            "  – core narrative text: post_game_policy_v1\n"
            "  – slide link: https://slides.example.org/post/2024000008\n"
            "  – PDF path: s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a leverage threshold of 1.5.\n"
            "• Two curated insights are added to the report for player_id 7 using deterministic, policy-compliant values:\n"
            "  – insight_text: tendency_chaserate_high, insight_type: tendency, supporting_stat_value: 0.31\n"
            "  – insight_text: predictability_firstpitchstrike_high, insight_type: predictability, supporting_stat_value: 0.68\n"
            "• Exactly two curated video playlists are attached to this same report:\n"
            "  – “Positive Reinforcement” with 3 clips\n"
            "  – “Teaching Moments” with 2 clips\n"
            "• A single workflow bookkeeping record is written with dag name 'post_game_review', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_029",
        instruction=(
            "You are preparing a concise opponent plan for game 2024000004. Publish a single pre-game scouting dossier for that game and return the report_id.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Upstream prep is reflected in the database for this game: pitch classifications are canonicalized and a persisted 12×12 catcher-view zone encoding exists with x∈[−1.5,1.5] and z∈[1.0,4.0].\n"
            "• The dossier uses the narrative label 'series_pitching_plan' and embeds the exact artifacts: "
            "  Google Slides at 'https://docs.google.com/presentation/d/series_pitching_plan' and "
            "  PDF at 's3://reports/scouting/opponent_analysis/2024000004.pdf'.\n"
            "• Exactly four curated insights are attached with these deterministic keys, subjects, and values: "
            "  situational_risp_high for player_id 2 at 0.52; predictability_firstpitch_high for player_id 4 at 0.36; "
            "  execution_fastball_high for player_id 4 at 0.61; execution_slider_low for player_id 8 at 0.58.\n"
            "• Two reference video playlists are associated to the same dossier with fixed names and clip counts: "
            "  'Pre-Game Examples' (3 clips) and 'Pre-Game Risks' (3 clips).\n"
            "• A planning workflow completion is recorded under the process name 'opponent_analysis' with frozen times "
            "  start=end='2025-08-18T00:00:00Z', log path "
            "  's3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log', and explicit attribution to game_pk 2024000004.\n"
            "• Return only the report_id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000004}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000004}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000004, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="create_scouting_report", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "core_narrative_text": "series_pitching_plan", "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan", "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.58}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Pre-Game Examples", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Pre-Game Risks", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={"dag_name": "opponent_analysis", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log", "game_pk": 2024000004})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_030",
        instruction=(
            "You are preparing a policy-compliant post-game dossier for game 2024000008.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized post-game scouting dossier exists for this game and it uses the organization’s standard values:\n"
            "  — narrative label: post_game_review\n"
            "  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review\n"
            "  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf\n"
            "• Execution evaluations and curated insights in the dossier comply with rules.py gating and thresholds, and all pitch types referenced in insight keys use canonical pitch codes (e.g., FF, SL) rather than colloquial names.\n"
            "• The dossier’s curated video support uses exactly the policy-mandated playlist set for post-game dossiers — “Positive Reinforcement” and “Teaching Moments” — each containing three clips and linked to the same report.\n"
            "• Workflow completion for the post-game process is recorded with frozen UTC times (start 2025-08-18T00:00:00Z, end 2025-08-18T00:20:00Z) and a deterministic S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.\n"
            "• Return the identifier of the finalized post-game dossier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),

            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),

            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),

            # Curated insights using canonical pitch codes (FF, SL)
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high", "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high", "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_sl_low", "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),

            # Policy-mandated playlists
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),

            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:20:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_031",
        instruction=(
            "You are delivering a post-game correction and reinforcement pack for game 2024000008. Publish a single report and return the report_id.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Release is gated on the game being Final; the narrative is 'post_game_review' with artifacts "
            "  'https://docs.google.com/presentation/d/post_game_review' and 's3://reports/scouting/post_game/2024000008.pdf'.\n"
            "• A 12×12 catcher-view zone map for this game is persisted with x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Execution grading includes the five-pitch benchmark set: "
            "  29 down_away→down_middle (2.4), 33 up_in→middle_in (6.8), 46 down_away→down_away (1.2), "
            "  17 up_away→up_middle (4.1), 45 down_in→middle_in (5.0).\n"
            "• Four curated insights are attached: "
            "  situational_risp_high (player_id 8, 0.55), predictability_firstpitch_high (player_id 2, 0.31), "
            "  execution_fastball_high (player_id 4, 0.60), execution_slider_low (player_id 8, 0.56).\n"
            "• Four playlists (3 clips each) are linked: 'Positive Reinforcement', 'Corrective Work', 'Two-Strike Wins', 'Leave-It Misses'.\n"
            "• A workflow completion entry exists for 'post_game_review' with start=end='2025-08-18T00:00:00Z', "
            "  log path 's3://workflow/logs/post_game_review/2024000008/2025-08-18.log', and attribution to game_pk 2024000008.\n"
            "• Return only the report_id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.31}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Corrective Work", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Two-Strike Wins", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Leave-It Misses", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_032",
        instruction=(
            "You are producing a pre-/in-series targeting dossier for game 2024000004. Publish a single dossier and return the report_id.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• The dossier is pre-game with narrative 'series_pitching_plan' and fixed artifacts "
            "  'https://docs.google.com/presentation/d/series_pitching_plan' and "
            "  's3://reports/scouting/opponent_analysis/2024000004.pdf'.\n"
            "• Four playlists (3 clips each) are linked: 'Pre-Game Examples', 'Pre-Game Risks', 'Left/Right Keys', 'Hot Zones'.\n"
            "• Exactly six curated insights are attached: "
            "  situational_risp_high (player_id 2, 0.52), predictability_firstpitch_high (player_id 4, 0.36), "
            "  execution_fastball_high (player_id 4, 0.61), execution_slider_low (player_id 8, 0.58), "
            "  situational_risp_high (player_id 8, 0.55), predictability_firstpitch_high (player_id 2, 0.31).\n"
            "• A planning workflow completion exists for 'opponent_analysis' with start=end='2025-08-18T00:00:00Z', "
            "  log path 's3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log', and attribution to game_pk 2024000004.\n"
            "• Return only the report_id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000004}),
            Action(name="create_scouting_report", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "core_narrative_text": "series_pitching_plan", "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan", "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Pre-Game Examples", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Pre-Game Risks", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Left/Right Keys", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Hot Zones", "clip_count": 3, "report_id": 13}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.58}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.31}),
            Action(name="log_workflow_run", kwargs={"dag_name": "opponent_analysis", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log", "game_pk": 2024000004})
        ],
        outputs=[13]
    ),




    Task(
        annotator="saaish2",
        user_id="task_033",
        instruction=(
            "You are finalizing an umpire and execution review for a completed game. Deliver one uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest.\n"
            "• A per-game umpire calibration record exists for the home plate assignment with: umpire_id 2, zone_shift_x −0.05, zone_shift_z 0.07, calibration_error_pct 2.3, confidence_interval '90%'.\n"
            "• Exactly two pitch-level execution assessments are recorded for game_pk 2024000008:\n"
            "  – pitch_id 28: intended quadrant 'glove-side-high', actual quadrant 'glove-side-high', miss_distance_inches 2.5\n"
            "  – pitch_id 29: intended quadrant 'arm-side-low',  actual quadrant 'arm-side-mid',  miss_distance_inches 6.8\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated with bounds x∈[−0.95,0.95], z∈[1.5,3.5] and persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000008 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.\n"
            "• The report contains one curated insight for player_id 7 with: insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31.\n"
            "• Exactly two curated video playlists are attached to this report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_umpire_exec', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_umpire_exec.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_umpire_exec",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_umpire_exec.json"
            }),
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_034",
        instruction=(
            "You are assembling a pre-series scouting packet for an upcoming contest. Deliver one uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The focal matchup is game_pk 2024000011 and it is a scheduled contest.\n"
            "• Two ingest records exist for this run, exactly:\n"
            "  – source_name 'probables_feed', status_code 200, records_ingested 2, ingested_at_utc '2024-07-23T00:00:00Z'\n"
            "  – source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-07-23T00:00:00Z'\n"
            "• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000011 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5] and persisted.\n"
            "• A single Pre-Game scouting report exists for game_pk 2024000011 with core narrative text 'pre_series_policy_v1', slide link 'https://slides.example.org/pre/2024000011', and PDF path 's3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf'.\n"
            "• The report contains exactly two curated insights for player_id 7:\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.68\n"
            "  – insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31\n"
            "• Exactly two curated video playlists are attached: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000011 is recorded using a threshold of 1.5.\n"
            "• The opponent for team_id 10 in this game is deterministically resolved and relied upon internally (no output required).\n"
            "• A workflow bookkeeping record is written with dag name 'pre_series_packet', game_pk 2024000011, status 'success', start_time_utc '2024-07-23T00:00:00Z', end_time_utc '2024-07-23T00:00:00Z', and log path 's3://logs/pre/2024-07-23_g2024000011_packet.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000011}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2024-07-23T00:00:00Z"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-07-23T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000011,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000011, "threshold": 1.5}),
            Action(name="get_opponent_for_team_in_game", kwargs={"team_id": 10, "game_pk": 2024000011}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_packet",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2024-07-23T00:00:00Z",
                "end_time_utc": "2024-07-23T00:00:00Z",
                "log_s3_path": "s3://logs/pre/2024-07-23_g2024000011_packet.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_035",
        instruction=(
            "You must produce a single, uniquely determined terminal database state for a completed game using the fixed IDs, bounds, threshold, names, and file paths defined here—without listing steps or naming any APIs. Acceptance criteria:\n"
            "• Exactly one Post-Game scouting report exists for game_pk 2024000008 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.\n"
            "• The catcher-view 12×12 strike-zone mapping is persisted for this game using x∈[−0.95,0.95], z∈[1.5,3.5] and a 12×12 grid.\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a threshold of 1.5; the resulting counts are whatever the system canonically computes from the existing play-by-play under that threshold.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_addendum",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_addendum.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_036",
        instruction=(
            "You are completing a dual-track update in which post-game insights drive actionable development objectives. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• Post-game context: game_pk 2024000008 is a completed contest; a single Post-Game report exists for this game with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.\n"
            "• The catcher-view 12×12 strike-zone mapping for this game is generated with bounds x∈[−0.95,0.95], z∈[1.5,3.5] and persisted; leverage summary recorded with threshold 1.5.\n"
            "• The report contains exactly two curated insights: for player_id 7 ('situational_rispcontact_high', type 'situational', value 0.29) and for player_id 11 ('predictability_firstpitchstrike_high', type 'predictability', value 0.66).\n"
            "• Development track: two development goals are created and approved with deterministic details:\n"
            "  – dev_report_id 10, player_id 11, goal_text 'raise_chaserate_decisions_10pct', coach_id 501, target_review_date '2024-05-06'\n"
            "  – dev_report_id 6,  player_id 10, goal_text 'improve_zone_coverage_inner_third', coach_id 501, target_review_date '2024-05-06'\n"
            "• Exactly two curated video playlists are attached to the Post-Game report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A single ingest record exists for this run with: source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-03-05T00:00:00Z'.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_to_dev_bridge', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_to_dev.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.29
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 10,
                "player_id": 11,
                "goal_text": "raise_chaserate_decisions_10pct",
                "coach_id": 501,
                "target_review_date": "2024-05-06"
            }),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 6,
                "player_id": 10,
                "goal_text": "improve_zone_coverage_inner_third",
                "coach_id": 501,
                "target_review_date": "2024-05-06"
            }),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_to_dev_bridge",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_to_dev.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_037",
        instruction=(
            "You are producing a policy-compliant, end-to-end post-game review focused on calibration, execution, mapping, and curation. Deliver one uniquely determined terminal database state that satisfies all the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000003 and it is a completed contest.\n"
            "• Exactly one ingest record exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.\n"
            "• A per-game umpire calibration record exists with: umpire_id 2, zone_shift_x −0.03, zone_shift_z 0.06, calibration_error_pct 1.9, confidence_interval '90%'.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000003 is generated with bounds x∈[−0.95,0.95], z∈[1.5,3.5] and persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.\n"
            "• The report contains exactly two curated insights for player_id 10: 'tendency_chaserate_high' (type 'tendency', value 0.30) and 'predictability_firstpitchstrike_high' (type 'predictability', value 0.65).\n"
            "• Exactly two curated video playlists are attached: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000003 is recorded using threshold 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_curation', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_curation.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000003,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 10,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.30
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 10,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.65
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_curation",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_curation.json"
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_038",
        instruction=(
            "You present an opponent analysis aligned to a completed matchup (game 2024000008), expressed as outcome criteria only. "
            "The final state evidences standardized pitch labels scoped to the game; 12×12 catcher-view encoding (x −1.5..1.5, z 1.0..4.0) persisted; "
            "an opponent-analysis report using 'series_pitching_plan' with links "
            "https://docs.google.com/presentation/d/series_pitching_plan and s3://reports/scouting/opponent_analysis/2024000008.pdf; "
            "two templated insights (player 5: 'tendency_chaserate_high' 0.18; player 14: 'predictability_changeup_high' 0.64); "
            "two coaching playlists ('Positive Reinforcement' 3 clips; 'Teaching Moments' 2 clips); verification that both insights and both playlists exist; "
            "and a workflow record labeled 'opponent_analysis_series' at 2025-08-14T00:00:00Z stored at "
            "s3://logs/workflows/opponent_analysis_series/2025-08-14/run.json."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "opponent-analysis",
                "game_pk": 2024000008,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.18
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 14,
                "insight_text": "predictability_changeup_high", "insight_type": "predictability", "supporting_stat_value": 0.64
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="list_curated_insights", kwargs={"report_id": 13}),
            Action(name="list_video_playlists", kwargs={"report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "opponent_analysis_series",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/opponent_analysis_series/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_039",
        instruction=(
            "You are authoring a full post-game review packet for game 2024000008 that conforms to policy and persists all derived assets.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized post-game scouting dossier exists using the organization’s standard values:\n"
            "  — narrative label: post_game_review\n"
            "  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review\n"
            "  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf\n"
            "• Pitch-type labels are standardized and strike-zone spatial features are persisted using the org’s standard 12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Execution evaluations use the game’s canonical five-pitch sample with frozen quadrant targets and miss distances as recorded in the dataset; do not infer or recompute.\n"
            "• Curated insights satisfy rules.py gates, collapse redundant bullets, and are ordered by supporting_stat_value DESC then player_id ASC, using canonical keys.\n"
            "• Curated video support consists of exactly the policy-mandated playlist set — “Positive Reinforcement” and “Teaching Moments” — each with three clips and linked to the dossier.\n"
            "• Workflow completion for the post-game process is recorded with frozen UTC times (start 2025-08-18T00:00:00Z, end 2025-08-18T00:30:00Z) and a deterministic S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.\n"
            "• Return the identifier of the finalized post-game dossier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicates and sort by supporting_stat_value DESC then player_id ASC
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:30:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_040",
        instruction=(
            "You are compiling a comprehensive pre-series scouting packet for game 2024000004 that standardizes pitch labels, persists spatial features, and captures opponent tendencies.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized pre-game scouting dossier exists using the organization’s standard values:\n"
            "  — narrative label: series_pitching_plan\n"
            "  — Google Slides artifact: https://docs.google.com/presentation/d/series_pitching_plan\n"
            "  — PDF artifact: s3://reports/scouting/opponent_analysis/2024000004.pdf\n"
            "• Pitch-type labels are canonicalized and strike-zone spatial features are persisted using the org’s standard 12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Curated insights meet rules.py gates, collapse redundant bullets, and are ordered by supporting_stat_value DESC then player_id ASC, using canonical keys across situational, predictability, execution, and tendency themes.\n"
            "• Workflow completion for the pre-series process is recorded with frozen UTC times (start 2025-08-18T11:00:00Z, end 2025-08-18T11:30:00Z) and a deterministic S3 log path: s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log.\n"
            "• Return the identifier of the finalized pre-game dossier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000004}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000004}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000004, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            # FIX: collapse duplicate 'situational_risp_high' and sort DESC by supporting_stat_value then player_id ASC
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_high", "insight_type": "tendency", "supporting_stat_value": 0.45}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.35}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "opponent_analysis",
                "status": "success",
                "start_time_utc": "2025-08-18T11:00:00Z",
                "end_time_utc": "2025-08-18T11:30:00Z",
                "log_s3_path": "s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log",
                "game_pk": 2024000004
            })
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_041",
        instruction=(
            "You are delivering a comprehensive post-game scouting dossier for game 2024000008 that standardizes pitch labels, materializes spatial features, captures policy-compliant insights, and includes the mandated video support.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized post-game scouting dossier exists using the organization’s standard values:\n"
            "  — narrative label: post_game_review\n"
            "  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review\n"
            "  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf\n"
            "• All nomenclature and spatial features conform to policy (12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0]).\n"
            "• Execution evaluations use the game’s canonical five-pitch sample with frozen quadrant targets and miss distances as recorded in the dataset; do not infer or recompute.\n"
            "• Curated insights pass rules.py gates, collapse redundant bullets, and are ordered by supporting_stat_value DESC then player_id ASC, using canonical keys.\n"
            "• Curated video support uses exactly the policy-mandated playlist set — “Positive Reinforcement” and “Teaching Moments” — each with three clips linked to the dossier.\n"
            "• Workflow completion is recorded with frozen UTC times (start 2025-08-18T01:10:00Z, end 2025-08-18T01:40:00Z) and a deterministic S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.\n"
            "• Return the identifier of the finalized post-game dossier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicate insights and enforce deterministic ordering (DESC by value, then player_id ASC)
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review", "status": "success",
                "start_time_utc": "2025-08-18T01:10:00Z", "end_time_utc": "2025-08-18T01:40:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[13]
    ),


    Task(
        annotator="saaish2",
        user_id="task_042",
        instruction=(
            "You are assembling a compact pre-series scouting packet. Deliver a single, uniquely determined terminal database state that satisfies all of the following checks without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000011 and it is not yet played (scheduled).\n"
            "• Collection provenance shows one ingest record for this run with: source_name 'probables_feed', status_code 200, records_ingested 2, ingested_at_utc '2025-08-14T00:00:00Z'.\n"
            "• Trends are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• Exactly one Pre-Game scouting report exists for game_pk 2024000011 with core narrative text 'pre_series_policy_v1', slide link 'https://slides.example.org/pre/2024000011', and PDF path 's3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf'.\n"
            "• That report contains exactly four curated insights for player_id 7, ordered by supporting_stat_value DESC:\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.61\n"
            "  – insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.50\n"
            "  – insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.36\n"
            "  – insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.22\n"
            "• Workflow bookkeeping records indicate: dag name 'pre_series_packet', game_pk 2024000011, status 'success', start_time_utc '2024-07-23T00:00:00Z', end_time_utc '2024-07-23T00:00:00Z', and log path 's3://logs/pre/2024-07-23_g2024000011_packet.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000011}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.50
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.36
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.22
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_packet",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2024-07-23T00:00:00Z",
                "end_time_utc": "2024-07-23T00:00:00Z",
                "log_s3_path": "s3://logs/pre/2024-07-23_g2024000011_packet.json"
            }),
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_043",
        instruction=(
            "You are finalizing a concise post-game addendum. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.\n"
            "• Exactly one Post-Game scouting report exists for game_pk 2024000008 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.\n"
            "• That report contains exactly two curated insights for player_id 7:\n"
            "  – insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.66\n"
            "• Exactly two curated video playlists are attached to that same report: 'Positive Reinforcement' with 3 clips and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_addendum",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_addendum.json"
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_044",
        instruction=(
            "You are completing a post-game model + execution QC packet. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest.\n"
            "• One ingest record for this run exists with: source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'.\n"
            "• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• A per-game umpire calibration record exists with: umpire_id 2, zone_shift_x −0.05, zone_shift_z 0.07, calibration_error_pct 2.3, confidence_interval '90%'.\n"
            "• Exactly three pitch execution assessments are recorded for game_pk 2024000008:\n"
            "  – pitch_id 28 intended 'glove-side-high' matched actual 'glove-side-high' with miss_distance_inches 2.5\n"
            "  – pitch_id 29 intended 'arm-side-low' landed 'arm-side-mid' with miss_distance_inches 6.8\n"
            "  – pitch_id 31 intended 'down-middle' matched actual 'down-middle' with miss_distance_inches 1.9\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000008 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.\n"
            "• The report contains exactly two curated insights for player_id 7, ordered by supporting_stat_value DESC:\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.66\n"
            "  – insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31\n"
            "• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_model_exec_qc', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_qc.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered by supporting_stat_value DESC per policy
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_model_exec_qc",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_qc.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_045",
        instruction=(
            "You are finalizing a comprehensive post-game scouting and QC packet. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000003 and it is a completed contest.\n"
            "• One ingest record for this run exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.\n"
            "• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000003 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.\n"
            "• The report contains exactly three curated insights for player_id 11, ordered by supporting_stat_value DESC:\n"
            "  – insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30\n"
            "  – insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.19\n"
            "• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            # Insights in DESC order by supporting_stat_value per policy
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_046",
        instruction=(
            "You are assembling a comprehensive post-game analytics packet. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000003 and it is a completed contest.\n"
            "• Two player development goals already exist for the relevant development report and must remain unchanged in this run; do not create, approve, or modify any development goals.\n"
            "• One ingest record for this run exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.\n"
            "• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.\n"
            "• The catcher-view strike-zone mapping for game_pk 2024000003 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.\n"
            "• A single Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.\n"
            "• The report contains exactly three curated insights for player_id 11, ordered by supporting_stat_value DESC:\n"
            "  – insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34\n"
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30\n"
            "  – insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.19\n"
            "• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.\n"
            "• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            # Curated insights in strict DESC order by supporting_stat_value
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_047",
        instruction=(
            "You are preparing a policy-compliant post-game dossier for game 2024000008.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• A single finalized post-game dossier exists for this game with: narrative label post_game_review, Google Slides https://docs.google.com/presentation/d/post_game_review, and PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Any strike-zone feature engineering persists a 12×12 catcher-view grid using fixed bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Trends are surfaced only after EB shrinkage with FDR control using thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10; acceptance requires those thresholds (or stricter) be applied.\n"
            "• Curated insights attached to the dossier use canonical insight_text keys, are unique (no duplicates), and are ordered by supporting_stat_value DESC then player_id ASC.\n"
            "• Exactly two policy-mandated video playlists are attached to the dossier: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• Workflow completion is recorded with frozen UTC times (start 2025-08-18T18:00:00Z, end 2025-08-18T18:20:00Z) and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log.\n"
            "• Return the dossier identifier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Curated insights (unique, sorted by value DESC then player_id ASC)
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            # Playlists (policy-mandated names)
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:00:00Z", "end_time_utc": "2025-08-18T18:20:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_048",
        instruction=(
            "You are delivering a post-game improvement packet for game 2024000008.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• A finalized dossier exists with: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• If strike-zone features are persisted, use a 12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Trend surfacing applies EB shrinkage with FDR control using thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.\n"
            "• Curated insights are canonical, non-duplicative, sorted by supporting_stat_value DESC then player_id ASC, and attached to the dossier.\n"
            "• Attach the policy-mandated video playlists only: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• Record workflow completion with frozen times (start 2025-08-18T18:25:00Z, end 2025-08-18T18:45:00Z) and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log.\n"
            "• Return the dossier identifier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Curated insights (unique, sorted)
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.51}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.35}),
            # Playlists
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:25:00Z", "end_time_utc": "2025-08-18T18:45:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_049",
        instruction=(
            "You are producing a comprehensive, policy-compliant post-game review packet for game 2024000008.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized dossier exists with: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Persist a 12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Record execution evaluations for exactly these five pitches (deterministic specification):\n"
            "  (29: intended=down_away, actual=down_middle, miss_in=2.4), (33: intended=up_in, actual=middle_in, miss_in=6.8),\n"
            "  (46: intended=down_away, actual=down_away, miss_in=1.2), (17: intended=up_away, actual=up_middle, miss_in=4.1),\n"
            "  (45: intended=down_in, actual=middle_in, miss_in=5.0).\n"
            "• Surface trends only after EB shrinkage with FDR control using thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.\n"
            "• Attach exactly six curated insights using canonical keys, no duplicates, ordered by supporting_stat_value DESC then player_id ASC with these tuples (player_id, key, value):\n"
            "  (4, execution_ff_high, 0.66), (8, execution_sl_low, 0.60), (8, situational_risp_high, 0.58), (2, predictability_firstpitch_high, 0.49), (2, execution_ch_low, 0.43), (4, predictability_sequencing_low, 0.41).\n"
            "• Attach only the policy-mandated video playlists: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• Record workflow completion with frozen UTC times (start 2025-08-18T18:30:00Z, end 2025-08-18T18:55:00Z) and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log.\n"
            "• Return the dossier identifier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Six insights (unique, sorted)
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.66}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.58}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.49}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ch_low", "insight_type": "execution", "supporting_stat_value": 0.43}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_sequencing_low", "insight_type": "predictability", "supporting_stat_value": 0.41}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:30:00Z", "end_time_utc": "2025-08-18T18:55:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),



    Task(
        annotator="saaish2",
        user_id="task_050",
        instruction=(
            "You are creating an end-to-end post-game briefing for game 2024000008 with deterministic execution grading and ranked insights.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• A finalized dossier exists with: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Persist 12×12 catcher-view grid features using bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Record execution evaluations for these exact five pitches (id, intended→actual, miss_in): 29 (down_away→down_middle, 2.4), 33 (up_in→middle_in, 6.8), 46 (down_away→down_away, 1.2), 17 (up_away→up_middle, 4.1), 45 (down_in→middle_in, 5.0).\n"
            "• Prior to attaching insights, apply EB shrinkage with FDR control thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.\n"
            "• Attach six canonical, non-duplicative insights sorted by supporting_stat_value DESC then player_id ASC with these tuples: (2, execution_ff_high, 0.67), (4, execution_sl_low, 0.61), (8, situational_risp_high, 0.59), (2, predictability_firstpitch_high, 0.48), (4, execution_ch_low, 0.45), (8, predictability_sequencing_low, 0.41).\n"
            "• Attach only the policy-mandated playlists: “Positive Reinforcement” (3) and “Teaching Moments” (3).\n"
            "• Log workflow completion with frozen UTC times (start 2025-08-18T20:00:00Z, end 2025-08-18T20:25:00Z) and path s3://workflow/logs/post_game_review/2024000008/2025-08-18-5.log.\n"
            "• Return the dossier identifier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            # Explicit audit log entry for draft_status transition (fix from judge)
            Action(name="log_ingestion_event", kwargs={
                "source_name": "scouting_reports",
                "status_code": 200,
                "records_ingested": 1,
                "timestamp_utc": "2025-08-18T20:25:00Z",
                "message": "report_published report_id=13 draft_status=published",
                "game_pk": 2024000008
            }),
            # Insights in required order and canonicalized
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.67}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.59}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.48}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ch_low", "insight_type": "execution", "supporting_stat_value": 0.45}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_sequencing_low", "insight_type": "predictability", "supporting_stat_value": 0.41}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T20:00:00Z",
                "end_time_utc": "2025-08-18T20:25:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-5.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[13]  # Explicit return of dossier identifier as required
    ),


    Task(
        annotator="saaish2",
        user_id="task051",
        instruction=(
            "You are finalizing a post-game dossier for game_pk 2024000003 (a completed contest). "
            "Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs: "
            "• Exactly one ingestion record exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'. "
            "• Trend anomalies have been screened using false-discovery rate q=0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events. "
            "• One Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'. "
            "• The report contains exactly two curated insights for player_id 11, ordered by supporting_stat_value descending: "
            "  – insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34 "
            "  – insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30 "
            "• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips. "
            "• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5. "
            "• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. "
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_052",
        instruction=(
            "You compile a single, policy-compliant post-game analyst packet for game_pk 2024000008 that resolves to a uniquely determined state. "
            "Acceptance criteria: calibrated officiating for umpire_id 2 with x shift −0.02, z shift 0.05, 1.9% error, 90% interval; "
            "execution assessments persisted for pitch_id 28 (glove-side-high→glove-side-high, 2.5 in miss) and pitch_id 31 (down-middle→down-middle, 1.9 in miss); "
            "a 12×12 zone artifact for x∈[−0.95,0.95], z∈[1.5,3.5] and persisted; "
            "a post-game packet exists with narrative 'umpire_exec_review_v1', slides https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; "
            "two curated playlists are attached to that packet exactly as required: Positive Reinforcement (3 clips) and Teaching Moments (2 clips); "
            "and the run is recorded successful with start/end 2025-08-14T00:00:00Z and log s3://logs/post_game/2025-08-14_g2024000008.json. Return nothing."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.02,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28, "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31, "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/post_game/2025-08-14_g2024000008.json",
                "game_pk": 2024000008
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_053",
        instruction=(
            "You are producing a policy-compliant post-game dossier for game_pk 2024000008 (a completed contest). "
            "Your objective is to leave the database in a single, uniquely determined terminal state where the system reflects one successful statcast ingestion "
            "(source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); "
            "trend screening has been applied using false-discovery rate q=0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "exactly one Post-Game scouting report is present for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', "
            "and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; "
            "the report contains precisely two curated insights for player_id 7 with supporting values 0.31 for 'situational_rispcontact_high' (type 'situational') and 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'), "
            "and it is associated with two curated video playlists titled 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "a leverage summary exists for game_pk 2024000008 using threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', "
            "and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. "
            "Do not list steps or name any APIs. No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_054",
        instruction=(
            "You are assembling a full post-game analytics dossier. In the terminal state, the database reflects a completed contest for game_pk 2024000003; exactly one ingest record is present (source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'); trend anomalies have been filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events; a per-game umpire calibration exists with umpire_id 2, zone_shift_x −0.03, zone_shift_z 0.06, calibration_error_pct 1.9, confidence_interval '90%'; three pitch-execution assessments exist for the game with (pitch_id 28, intended 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5), (pitch_id 29, intended 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8), and (pitch_id 31, intended 'down-middle', actual 'down-middle', miss_distance_inches 1.9); a catcher-view strike-zone mapping is persisted for game_pk 2024000003 using bounds x∈[−0.95,0.95], z∈[1.5,3.5] with 12×12 grid dimensions; a single Post-Game scouting report exists for this game with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'; the report contains exactly three curated insights for player_id 11 ordered by supporting_stat_value DESC (situational_rispcontact_high 0.34; predictability_firstpitchstrike_high 0.30; execution_zonerate_low 0.19) and exactly two curated video playlists ('Positive Reinforcement' with 3 clips and 'Teaching Moments' with 2 clips); a leverage summary exists for game_pk 2024000003 using threshold 1.5; and a workflow record exists with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000003,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000003,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000003,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000003,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_055",
        instruction=(
            "You are finalizing a post-game development alignment for a completed contest. Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs:\n"
            "• The game under review is game_pk 2024000008 and it is a completed contest (Final).\n"
            "• Two player development goals are persisted and end in status 'Approved':\n"
            "  – dev_report_id 10 for player_id 11 with goal_text 'raise_chase_swing_decisions_10pct', coach_id 501, target_review_date '2024-03-06'.\n"
            "  – dev_report_id 6 for player_id 10 with goal_text 'improve_zone_coverage_inner_third', coach_id 501, target_review_date '2024-03-06'.\n"
            "• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events; the resulting flags table name is exactly 'trend_flags_p50_s30_b25_fdr0.1'.\n"
            "• Three pitch execution assessments are recorded for the same game_pk with these exact values:\n"
            "  – pitch_id 28, intended_quadrant_model 'glove-side-high', actual_quadrant 'glove-side-high', miss_distance_inches 2.5.\n"
            "  – pitch_id 29, intended_quadrant_model 'arm-side-low', actual_quadrant 'arm-side-mid', miss_distance_inches 6.8.\n"
            "  – pitch_id 31, intended_quadrant_model 'down-middle', actual_quadrant 'down-middle', miss_distance_inches 1.9.\n"
            "• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is generated using bounds x∈[−0.95,0.95], z∈[1.5,3.5], dimensions cells_x=12 and cells_z=12, and is persisted.\n"
            "• A leverage summary for game_pk 2024000008 is recorded using a threshold of 1.5.\n"
            "• A workflow bookkeeping record is written with dag name 'post_game_dev_alignment', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_dev_alignment.json'.\n"
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 10,
                "player_id": 11,
                "goal_text": "raise_chase_swing_decisions_10pct",
                "coach_id": 501,
                "target_review_date": "2024-03-06"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 6,
                "player_id": 10,
                "goal_text": "improve_zone_coverage_inner_third",
                "coach_id": 501,
                "target_review_date": "2024-03-06"
            }),
            # Approve the two goals created above (IDs are deterministic in this snapshot: 20, 21)
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_dev_alignment",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_dev_alignment.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_056",
        instruction=(
            "You are producing a policy-compliant post-game dossier for game_pk 2024000008 (a completed contest). "
            "Your objective is to leave the database in a single, uniquely determined terminal state where the system reflects one successful statcast ingestion "
            "(source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); "
            "trend screening has been applied using false-discovery rate q=0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "exactly one Post-Game scouting report is present for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', "
            "and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; "
            "the report contains precisely two curated insights for player_id 7 with supporting values 0.31 for 'situational_rispcontact_high' (type 'situational') and 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'), "
            "and it is associated with two curated video playlists titled 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "a leverage summary exists for game_pk 2024000008 using threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', "
            "and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. "
            "Do not list steps or name any APIs. No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_full.json"
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_057",
        instruction=(
            "You are producing a policy-compliant post-game dossier for a completed contest. "
            "Your objective is to leave the database in a single, uniquely determined terminal state meeting these acceptance criteria without listing steps or naming any APIs: "
            "the game under review is game_pk 2024000008 and it is final; "
            "the system reflects one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); "
            "trend screening is applied using empirical-Bayes shrinkage with FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "there is exactly one Post-Game scouting report for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; "
            "the report contains exactly two curated insights for player_id 7 ordered by supporting value descending: "
            "supporting_stat_value 0.31 for 'situational_rispcontact_high' (type 'situational') then 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "the report is associated with playlists 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "a leverage summary exists for game_pk 2024000008 with threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. "
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_058",
        instruction=(
            "You are assembling a post-game review dossier for game 2024000008.\n\n"
            "Your objective is to deliver a published dossier and audit trail that meet all of the following outcomes (non-procedural, acceptance-only):\n"
            "• The dossier is published and contains the narrative label 'post_game_review', the Google Slides URL https://docs.google.com/presentation/d/post_game_review, and a PDF stored at s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• The pitch-location appendix presents a 12×12 catcher-view grid covering horizontal −1.5 to 1.5 feet and vertical 1.0 to 4.0 feet, and those encodings are persisted.\n"
            "• Trend flags incorporated in the dossier come from EB-shrunk estimates under FDR q=0.10 using minimum samples of 50 pitches, 30 swings, and 25 batted balls.\n"
            "• The curated insight list contains exactly three canonical, non-duplicative bullets ordered by supporting_stat_value (DESC) then player_id (ASC): (player 4, execution_ff_high, 0.60), (player 8, situational_risp_high, 0.55), (player 2, predictability_firstpitch_high, 0.31).\n"
            "• Exactly two curated video playlists are included, titled 'Positive Reinforcement' and 'Teaching Moments', each containing three clips.\n"
            "• A publication audit record exists as a manual alert titled 'publication_audit' with frozen timestamp 2025-08-18T18:20:00Z and message 'report_published report_id=13 draft_status=published' (the suggestion text matches the message).\n"
            "• The workflow run is recorded as 'success' with start 2025-08-18T18:05:00Z, end 2025-08-18T18:20:00Z, and logs stored at s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5,
                "max_x": 1.5,
                "min_z": 1.0,
                "max_z": 4.0,
                "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "use_eb_shrinkage": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_ff_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T18:05:00Z",
                "end_time_utc": "2025-08-18T18:20:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_059",
        instruction=(
            "You are building an end-to-end post-game dossier with integrated trend vetting for game 2024000008.\n\n"
            "Acceptance-only outcomes:\n"
            "• Published dossier: label 'post_game_review', Slides https://docs.google.com/presentation/d/post_game_review, PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Persisted 12×12 catcher-view grid over −1.5..1.5 ft (x) and 1.0..4.0 ft (z).\n"
            "• Trend flags are derived using EB shrinkage with FDR q=0.10 and minimums of 50 pitches, 30 swings, and 25 batted balls; these are the only trends referenced in insights.\n"
            "• Exactly four curated insights, non-duplicative and ordered by supporting_stat_value DESC then player_id ASC: "
            "(player 4, execution_ff_high, 0.61), (player 3, tendency_chase_high, 0.58), (player 8, situational_risp_high, 0.55), (player 2, predictability_firstpitch_low, 0.34).\n"
            "• Two playlists exist: 'Positive Reinforcement' and 'Teaching Moments', each with exactly three clips tied to the dossier.\n"
            "• A publication audit exists as a manual alert 'publication_audit' at 2025-08-18T18:20:00Z with message 'report_published report_id=13 draft_status=published' (suggestion text matches) and flagged as manual.\n"
            "• The workflow run is recorded as success from 2025-08-18T18:05:00Z to 2025-08-18T18:20:00Z with logs s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 3, "insight_text": "tendency_chase_high", "insight_type": "tendency", "supporting_stat_value": 0.58
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_low", "insight_type": "predictability", "supporting_stat_value": 0.34
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T18:05:00Z",
                "end_time_utc": "2025-08-18T18:20:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_060",
        instruction=(
            "You are assembling the definitive post-game review packet for a completed contest. "
            "Your objective is to leave the database in a single, uniquely determined terminal state that meets the following acceptance criteria (do not list steps or name any APIs): "
            "the game under review is game_pk 2024000003 and it is final; "
            "the system reflects one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'); "
            "trend screening is applied via empirical-Bayes shrinkage with FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "there is exactly one Post-Game scouting report for game_pk 2024000003 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'; "
            "the report contains exactly two curated insights for player_id 11 ordered by supporting value descending: "
            "supporting_stat_value 0.34 for 'situational_rispcontact_high' (type 'situational') then 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "the report is associated with playlists 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "a leverage summary is recorded for game_pk 2024000003 with threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000003, start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. "
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000003,
                "status": "success",
                "start_time_utc": "2024-07-22T00:00:00Z",
                "end_time_utc": "2024-07-22T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-07-22_g2024000003_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_061",
        instruction=(
            "You are delivering a full post-game analytic package for a completed contest. "
            "Your objective is to leave the database in a single, uniquely determined terminal state that satisfies all of the following acceptance criteria (do not list steps or name any APIs): "
            "the game under review is game_pk 2024000008 and it is final; "
            "one successful statcast ingestion exists (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); "
            "trend screening is applied with empirical-Bayes shrinkage, FDR q=0.10, and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "exactly one Post-Game scouting report is present for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; "
            "the report contains exactly four curated insights ordered by supporting value descending across all entries: "
            "supporting_stat_value 0.66 for player_id 11 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "then 0.61 for player_id 7 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "then 0.34 for player_id 11 'situational_rispcontact_high' (type 'situational'); "
            "then 0.30 for player_id 7 'situational_rispcontact_high' (type 'situational'); "
            "two curated video playlists are attached to the same report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "pitch execution assessments are recorded for three pitches in the same game: "
            "pitch_id 28 graded as intended_quadrant 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5; "
            "pitch_id 29 graded as intended_quadrant 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8; "
            "pitch_id 31 graded as intended_quadrant 'down-middle', actual 'down-middle', miss_distance_inches 1.9; "
            "a leverage summary is stored for game_pk 2024000008 with threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. "
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered by supporting_stat_value DESC across all entries
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_full.json"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_062",
        instruction=(
            "You are producing a post-game execution and first-pitch predictability dossier for game 2024000008 for internal distribution.\n\n"
            "Acceptance outcomes (deterministic end-state):\n"
            "• A published scouting dossier exists for this game using the organization’s standard narrative label ('post_game_review'), slide deck link (https://docs.google.com/presentation/d/post_game_review), and PDF location (s3://reports/scouting/post_game/2024000008.pdf).\n"
            "• The appendix includes the organization’s catcher-view 12×12 strike-zone location grid persisted over x ∈ [−1.5, 1.5] ft and z ∈ [1.0, 4.0] ft.\n"
            "• Trends referenced in the dossier are vetted per policy with empirical-Bayes shrinkage, FDR q=0.10, and sample minimums of 50 pitches, 30 swings, and 25 batted balls.\n"
            "• Curated insights contain no redundant directives; specifically, if a first-pitch predictability signal exists it appears exactly once as 'predictability_firstpitchstrike_high'.\n"
            "• Two video playlists tied to the dossier exist titled 'Positive Reinforcement' and 'Teaching Moments', each containing three clips.\n"
            "• A manual publication audit exists at 2025-08-18T18:20:00Z capturing the dossier’s published state for this report.\n"
            "• The workflow run is recorded as 'success' for the fixed interval 2025-08-18T18:05:00Z→2025-08-18T18:20:00Z with logs at s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5,
                "max_x": 1.5,
                "min_z": 1.0,
                "max_z": 4.0,
                "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "use_eb_shrinkage": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            # Curated insights — ensure NO duplicates of 'predictability_firstpitchstrike_high'
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.57
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_ff_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 3,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.52
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T18:05:00Z",
                "end_time_utc": "2025-08-18T18:20:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_063",
        instruction=(
            "You are generating a complete, policy-aligned post-game deliverable for a completed contest. "
            "Your objective is to leave the database in a single, uniquely determined terminal state that satisfies the following acceptance criteria (do not list steps or name any APIs): "
            "the game under review is game_pk 2024000008 and it is final; "
            "two successful ingestions exist for the same game day: "
            "one with source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z', "
            "and one with source_name 'spraychart_feed', status_code 200, records_ingested 180, ingested_at_utc '2024-03-05T00:00:00Z'; "
            "trend screening is applied using empirical-Bayes shrinkage with FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted-ball events; "
            "exactly one Post-Game scouting report exists for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; "
            "the report contains exactly four curated insights ordered by supporting value descending across all entries: "
            "supporting_stat_value 0.66 for player_id 11 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "then 0.61 for player_id 7 'predictability_firstpitchstrike_high' (type 'predictability'); "
            "then 0.34 for player_id 11 'situational_rispcontact_high' (type 'situational'); "
            "then 0.30 for player_id 7 'situational_rispcontact_high' (type 'situational'); "
            "two curated video playlists are attached to the same report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "pitch execution assessments are recorded for three pitches in the game with the following values: "
            "pitch_id 28 (intended 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5), "
            "pitch_id 29 (intended 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8), "
            "pitch_id 31 (intended 'down-middle', actual 'down-middle', miss_distance_inches 1.9); "
            "a leverage summary is stored for game_pk 2024000008 with threshold 1.5; "
            "and workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. "
            "No other records are created or modified."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "spraychart_feed",
                "status_code": 200,
                "records_ingested": 180,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="filter_trends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered DESC
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.30
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_review",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2024-03-05T00:00:00Z",
                "end_time_utc": "2024-03-05T00:00:00Z",
                "log_s3_path": "s3://logs/post/2024-03-05_g2024000008_full.json"
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_064",
        instruction=(
            "You are producing a concise post-game quicklook dossier for game 2024000008 for the pitching group.\n\n"
            "Acceptance outcomes (deterministic end-state):\n"
            "• A published dossier exists for this game with organization label 'post_game_quicklook_v1', slide deck https://docs.google.com/presentation/d/post_game_quicklook_v1, and PDF s3://reports/scouting/post_game_quicklook_v1/2024000008.pdf.\n"
            "• A persisted catcher-view 12×12 location grid over x∈[−1.5,1.5] ft and z∈[1.0,4.0] ft is included.\n"
            "• Trend vetting applies empirical-Bayes shrinkage with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.\n"
            "• Exactly two unique curated insights (no redundancy) are attached to the dossier using the organization’s code format.\n"
            "• One video playlist tied to the dossier exists named 'Quick Hits' with 3 clips.\n"
            "• A manual publication audit exists at 2025-08-20T17:20:00Z; store the exact publication message as both the audit message and the operator note for that alert.\n"
            "• The workflow run is recorded successful for 2025-08-20T17:05:00Z→2025-08-20T17:20:00Z with logs at s3://workflow/logs/post_game_quicklook_v1/2024000008/2025-08-20-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={
                    "game_pk": 2024000008,
                    "min_x": -1.5,
                    "max_x": 1.5,
                    "min_z": 1.0,
                    "max_z": 4.0,
                    "persist": True,
                },
            ),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008,
                    "min_pitches": 50,
                    "min_swings": 30,
                    "min_bbe": 25,
                    "fdr_threshold": 0.10,
                    "use_eb_shrinkage": True,
                },
            ),
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game",
                    "game_pk": 2024000008,
                    "core_narrative_text": "post_game_quicklook_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_quicklook_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_quicklook_v1/2024000008.pdf",
                    "draft_status": "published",
                },
            ),
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008,
                    "timestamp_utc": "2025-08-20T17:20:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "report_published report_id=13 draft_status=published",
                    "is_manual_alert": True,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.60,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.57,
                },
            ),
            Action(
                name="create_video_playlist",
                kwargs={
                    "playlist_name": "Quick Hits",
                    "clip_count": 3,
                    "report_id": 13,
                },
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_quicklook_v1",
                    "status": "success",
                    "start_time_utc": "2025-08-20T17:05:00Z",
                    "end_time_utc": "2025-08-20T17:20:00Z",
                    "log_s3_path": "s3://workflow/logs/post_game_quicklook_v1/2024000008/2025-08-20-1.log",
                    "game_pk": 2024000008,
                },
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="saaish2",
        user_id="task_065",
        instruction=(
            "You are building a teaching-focused post-game dossier for game 2024000008 for player development. Drive to the following terminal database state without prescribing the implementation sequence.\n\n"
            "Acceptance outcomes (must all be true at completion):\n"
            "• A published dossier exists labeled 'post_game_teachpack_v1' with slide link https://docs.google.com/presentation/d/post_game_teachpack_v1 and PDF s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf.\n"
            "• A persisted catcher-view 12×12 grid over x∈[−1.5,1.5] ft and z∈[1.0,4.0] ft is included.\n"
            "• Trend vetting applies empirical-Bayes shrinkage with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.\n"
            "• Exactly four unique curated insights (no redundancy) using valid codes are attached to the dossier.\n"
            "• Two video playlists exist tied to the dossier: 'Reinforce Strengths' (3 clips) and 'Adjustments' (3 clips).\n"
            "• A manual publication audit exists at 2025-08-20T21:10:00Z with the publication message recorded verbatim and stored as the operator note.\n"
            "• The workflow run is recorded successful for 2025-08-20T20:55:00Z→2025-08-20T21:10:00Z with logs at s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={
                    "game_pk": 2024000008,
                    "min_x": -1.5,
                    "max_x": 1.5,
                    "min_z": 1.0,
                    "max_z": 4.0,
                    "persist": True,
                },
            ),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008,
                    "min_pitches": 50,
                    "min_swings": 30,
                    "min_bbe": 25,
                    "fdr_threshold": 0.10,
                    "use_eb_shrinkage": True,
                },
            ),
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game",
                    "game_pk": 2024000008,
                    "core_narrative_text": "post_game_teachpack_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_teachpack_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf",
                    "draft_status": "published",
                },
            ),
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008,
                    "timestamp_utc": "2025-08-20T21:10:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "report_published report_id=13 draft_status=published",
                    "is_manual_alert": True,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.62,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.34,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.56,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.53,
                },
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Reinforce Strengths", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Adjustments", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_teachpack_v1",
                    "status": "success",
                    "start_time_utc": "2025-08-20T20:55:00Z",
                    "end_time_utc": "2025-08-20T21:10:00Z",
                    "log_s3_path": "s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log",
                    "game_pk": 2024000008,
                },
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="saaish2",
        user_id="task_066",
        instruction=(
            "You are delivering an end-to-end post-game leverage dossier for game 2024000008 for the big-league coaching staff. Drive to the terminal state below; do not describe how to achieve it.\n\n"
            "Acceptance outcomes (deterministic end-state):\n"
            "• A published dossier exists labeled 'post_game_leverage_v1' with slide link https://docs.google.com/presentation/d/post_game_leverage_v1 and PDF s3://reports/scouting/post_game_leverage_v1/2024000008.pdf.\n"
            "• A persisted catcher-view 12×12 grid over x∈[−1.5,1.5] ft and z∈[1.0,4.0] ft is included.\n"
            "• Analysis scope is high-leverage only (leverage_index>1.5); leverage is summarized at threshold 1.5, and trend vetting applies empirical-Bayes shrinkage with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.\n"
            "• Six unique curated insights (no redundancy) using valid codes are attached to the dossier and mapped to appropriate players.\n"
            "• Three playlists tied to the dossier exist: 'Positive Reinforcement' (3 clips), 'Teaching Moments' (3 clips), and 'Leverage Review' (3 clips).\n"
            "• A manual publication audit exists at 2025-08-20T22:25:00Z; the publication message is recorded verbatim and duplicated as the operator note.\n"
            "• The workflow run is recorded successful for 2025-08-20T22:10:00Z→2025-08-20T22:25:00Z with logs at s3://workflow/logs/post_game_leverage_v1/2024000008/2025-08-20-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={
                    "game_pk": 2024000008,
                    "min_x": -1.5,
                    "max_x": 1.5,
                    "min_z": 1.0,
                    "max_z": 4.0,
                    "persist": True,
                },
            ),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008,
                    "min_pitches": 50,
                    "min_swings": 30,
                    "min_bbe": 25,
                    "fdr_threshold": 0.10,
                    "use_eb_shrinkage": True,
                },
            ),
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game",
                    "game_pk": 2024000008,
                    "core_narrative_text": "post_game_leverage_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_leverage_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_leverage_v1/2024000008.pdf",
                    "draft_status": "published",
                },
            ),
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008,
                    "timestamp_utc": "2025-08-20T22:25:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "report_published report_id=13 draft_status=published",
                    "is_manual_alert": True,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.61,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.58,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.55,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.33,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 6,
                    "insight_text": "stamina_b2b_low",
                    "insight_type": "stamina",
                    "supporting_stat_value": 0.40,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 7,
                    "insight_text": "predictability_sequencing_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.59,
                },
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Leverage Review", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_leverage_v1",
                    "status": "success",
                    "start_time_utc": "2025-08-20T22:10:00Z",
                    "end_time_utc": "2025-08-20T22:25:00Z",
                    "log_s3_path": "s3://workflow/logs/post_game_leverage_v1/2024000008/2025-08-20-1.log",
                    "game_pk": 2024000008,
                },
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="saaish2",
        user_id="task_067",
        instruction=(
            "You are producing a post-game platoon and predictability dossier for game 2024000008 for series planning. Deliver only the end-state facts; avoid any step narration.\n\n"
            "Acceptance outcomes (deterministic end-state):\n"
            "• A published dossier exists labeled 'post_game_platoon_pred_v1' with slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1 and PDF s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf.\n"
            "• A persisted catcher-view 12×12 grid over x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft is included.\n"
            "• Trend vetting applies empirical-Bayes shrinkage with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.\n"
            "• Six unique curated insights (no redundancy) using valid codes are attached to the dossier.\n"
            "• Three playlists tied to the dossier exist: 'Platoon Review' (3 clips), 'Sequencing Notes' (3 clips), and 'Execution Focus' (3 clips).\n"
            "• A manual publication audit exists at 2025-08-21T00:45:00Z; record the publication message verbatim and set suggestion_text to the same value.\n"
            "• The workflow run is recorded successful for 2025-08-21T00:30:00Z→2025-08-21T00:45:00Z with logs at s3://workflow/logs/post_game_platoon_pred_v1/2024000008/2025-08-21-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={
                    "game_pk": 2024000008,
                    "min_x": -0.95,
                    "max_x": 0.95,
                    "min_z": 1.5,
                    "max_z": 3.5,
                    "persist": True,
                },
            ),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008,
                    "min_pitches": 50,
                    "min_swings": 30,
                    "min_bbe": 25,
                    "fdr_threshold": 0.10,
                    "use_eb_shrinkage": True,
                },
            ),
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game",
                    "game_pk": 2024000008,
                    "core_narrative_text": "post_game_platoon_pred_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_platoon_pred_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf",
                    "draft_status": "published",
                },
            ),
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008,
                    "timestamp_utc": "2025-08-21T00:45:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "report_published report_id=13 draft_status=published",
                    "is_manual_alert": True,
                },
            ),
            # Six curated insights, all unique
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.63,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.57,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.52,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.35,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 6,
                    "insight_text": "stamina_b2b_low",
                    "insight_type": "stamina",
                    "supporting_stat_value": 0.41,
                },
            ),
            Action(
                name="add_curated_insight",
                kwargs={
                    "report_id": 13,
                    "player_id": 7,
                    "insight_text": "predictability_sequencing_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.60,
                },
            ),
            # Playlists
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Platoon Review", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Sequencing Notes", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="create_video_playlist",
                kwargs={"playlist_name": "Execution Focus", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_platoon_pred_v1",
                    "status": "success",
                    "start_time_utc": "2025-08-21T00:30:00Z",
                    "end_time_utc": "2025-08-21T00:45:00Z",
                    "log_s3_path": "s3://workflow/logs/post_game_platoon_pred_v1/2024000008/2025-08-21-1.log",
                    "game_pk": 2024000008,
                },
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="saaish2",
        user_id="task_068",
        instruction=(
            "You are the analytics coordinator for Team 10. Deliver a pre-series package for the next scheduled game on/after 2024-06-13. "
            "Acceptance criteria (single, deterministic terminal state):"
            "\n1) Next scheduled game selection anchored at current_date='2024-06-13' resolves to game_pk=2024000006 (Team 10 vs opponent_team_id=9)."
            "\n2) Pitch types are canonicalized prior to any spatial or reporting work (idempotent if already canonical)."
            "\n3) Exactly one scouting report exists for that game with: "
            "report_type='Pre-Game', s3_pdf_path='s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf', "
            "gslides_link='https://slides.example.org/pre/2024000006', core_narrative_text='pre_series_policy_v1'."
            "\n4) Exactly two curated insights are attached to that report using the deterministic template '{category}_{metric}_{bucket}': "
            "(player_id=7, insight_text='tendency_chaserate_high', insight_type='tendency', supporting_stat_value=0.412) and "
            "(player_id=9, insight_text='predictability_firstpitchswing_low', insight_type='predictability', supporting_stat_value=0.193)."
            "\n5) Exactly two video playlists exist for the same report with deterministic links and counts: "
            "('Opponent Tendencies', clip_count=4, internal_portal_link='https://portal.example/internal/playlist/ot_2024000006') and "
            "('Miss Locations', clip_count=3, internal_portal_link='https://portal.example/internal/playlist/ml_2024000006')."
            "\n6) A workflow_runs row is recorded: dag_name='pre_series_package', game_pk=2024000006, status='success', "
            "start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', "
            "log_s3_path='s3://workflows/pre_series_package/g2024000006/2025-08-14.json'."
            "\nPolicy references: explicit date anchor for next-game selection; deterministic insight template; stable ordering/links; pre-processing step aligns with the domain proposal."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date":"2024-06-13"}),
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk":2024000006,"team_id":10}),
            Action(name="canonicalize_pitch_types", kwargs={}),
            Action(name="create_scouting_report", kwargs={"report_type":"Pre-Game","game_pk":2024000006,"core_narrative_text":"pre_series_policy_v1","gslides_link":"https://slides.example.org/pre/2024000006","s3_pdf_path":"s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id":13,"player_id":7,"insight_text":"tendency_chaserate_high","insight_type":"tendency","supporting_stat_value":0.412}),
            Action(name="add_curated_insight", kwargs={"report_id":13,"player_id":9,"insight_text":"predictability_firstpitchswing_low","insight_type":"predictability","supporting_stat_value":0.193}),
            Action(name="create_video_playlist", kwargs={"report_id":13,"playlist_name":"Opponent Tendencies","clip_count":4,"internal_portal_link":"https://portal.example/internal/playlist/ot_2024000006"}),
            Action(name="create_video_playlist", kwargs={"report_id":13,"playlist_name":"Miss Locations","clip_count":3,"internal_portal_link":"https://portal.example/internal/playlist/ml_2024000006"}),
            Action(name="log_workflow_run", kwargs={"dag_name":"pre_series_package","game_pk":2024000006,"status":"success","start_time_utc":"2025-08-14T00:00:00Z","end_time_utc":"2025-08-14T00:00:00Z","log_s3_path":"s3://workflows/pre_series_package/g2024000006/2025-08-14.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_069",
        instruction=(
            "You are finalizing the post-game analytics snapshot for game 2024000003. Deliver a single terminal database state that meets ALL of the following acceptance criteria without creating unrelated records:\n"
            "• The work is anchored to this completed game; any derived artifacts reference game 2024000003.\n"
            "• Pitch data for the game is stored using the organization’s canonical pitch-type taxonomy.\n"
            "• Trend screening for this game reflects the policy parameters (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage and FDR control at 0.10; the resulting flags are the ones referenced by the brief.\n"
            "• A 12×12 catcher-view pitch-location grid is persisted for this game with bounds x∈[−0.95,0.95], z∈[1.5,3.5]. If any per-pitch mapping rows are produced by tooling, treat them strictly as intermediate (they are not part of what you return); the acceptance check looks only for the persisted grid state.\n"
            "• A published post-game scouting brief exists for this game with core narrative text “post_game_policy_v1”, slide deck link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.\n"
            "• A leverage summary for this game is recorded using threshold 1.5.\n"
            "• A publication audit event records the message “report_published report_id=<that brief’s id> draft_status=published” at 2025-08-18T18:20:00Z with suggestion_text “acknowledge_and_distribute”.\n"
            "• Do not enumerate or return any intermediate row-level mappings; at the end, return only the brief’s report id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000003}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True, "return_rows": True}),
            Action(name="create_scouting_report", kwargs={"report_type": "Post-Game", "game_pk": 2024000003, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "message": "report_published report_id=13 draft_status=published", "is_manual_alert": True, "suggestion_text": "acknowledge_and_distribute"}),
        ],
        outputs=[
            "13"
        ]
    ),


    Task(
        annotator="saaish2",
        user_id="task_070",
        instruction=(
            "You are finalizing a comprehensive post-game dossier for game 2024000008. In the terminal database state, the following facts must hold (this is an acceptance checklist, not a procedure):\n"
            "• The record of analytics inputs shows two entries: statcast_daily (status 200, records=3600, ingested_at_utc=2024-03-05T00:00:00Z) and hawkeye_quality_audit (status 200, records=61, ingested_at_utc=2024-03-05T01:00:00Z).\n"
            "• Pitch types are stored under the canonical taxonomy and trend-screening reflects EB shrinkage with FDR=0.10 (min_pitches=50, min_swings=30, min_bbe=25).\n"
            "• A persisted 12×12 catcher-view grid with x∈[−0.95,0.95], z∈[1.5,3.5] exists for this game; any per-pitch mapping rows produced by tooling are intermediate and not part of what you return.\n"
            "• Umpire calibration for umpire_id=2 reads zone_shift_x=−0.05, zone_shift_z=0.07, calibration_error_pct=2.3 with a 90% interval.\n"
            "• Execution grading exists for pitches 28 (glove-side-high→glove-side-high, 2.5in), 29 (arm-side-low→arm-side-mid, 6.8in), 31 (down-middle→down-middle, 1.9in), 30 (glove-side-high→glove-side-mid, 4.2in), 33 (arm-side-high→arm-side-high, 2.1in).\n"
            "• A published brief exists with core narrative “post_game_policy_v1”, slide deck https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf; attached to it are exactly two curated insights: (player_id=11, situational_rispcontact_high, 0.34) and (player_id=11, predictability_firstpitchstrike_high, 0.30).\n"
            "• Exactly two curated video playlists are linked to that brief: “PutAway_2Strikes” and “FirstPitch_Strikes”, each with exactly 3 clips.\n"
            "• A leverage summary uses threshold 1.5; a publication audit event at 2025-08-18T18:20:00Z stores “report_published report_id=<that brief’s id> draft_status=published” with suggestion_text “acknowledge_and_distribute”; and a successful workflow run named “post_game_package” exists with dag_name “analytics_post_game_v1”, start_time_utc=2025-08-18T18:20:30Z, end_time_utc=2025-08-18T18:22:00Z, timestamp_utc=2025-08-18T18:22:00Z, and log_s3_path s3://workflow/post_game_package/2024-03-05_g2024000008.log.\n"
            "• Return only the brief’s report id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="log_ingestion_event", kwargs={"source_name": "statcast_daily", "status_code": 200, "records_ingested": 3600, "ingested_at_utc": "2024-03-05T00:00:00Z"}),
            Action(name="log_ingestion_event", kwargs={"source_name": "hawkeye_quality_audit", "status_code": 200, "records_ingested": 61, "ingested_at_utc": "2024-03-05T01:00:00Z"}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="write_umpire_game_model", kwargs={"game_pk": 2024000008, "umpire_id": 2, "zone_shift_x": -0.05, "zone_shift_z": 0.07, "calibration_error_pct": 2.3, "confidence_interval": "90%"}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 28, "game_pk": 2024000008, "intended_quadrant_model": "glove-side-high", "actual_quadrant": "glove-side-high", "miss_distance_inches": 2.5}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "arm-side-low", "actual_quadrant": "arm-side-mid", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 31, "game_pk": 2024000008, "intended_quadrant_model": "down-middle", "actual_quadrant": "down-middle", "miss_distance_inches": 1.9}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 30, "game_pk": 2024000008, "intended_quadrant_model": "glove-side-high", "actual_quadrant": "glove-side-mid", "miss_distance_inches": 4.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "arm-side-high", "actual_quadrant": "arm-side-high", "miss_distance_inches": 2.1}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True, "return_rows": True}),
            Action(name="create_scouting_report", kwargs={"report_type": "Post-Game", "game_pk": 2024000008, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000008", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "situational_rispcontact_high", "insight_type": "situational", "supporting_stat_value": 0.34}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.30}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "PutAway_2Strikes", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "FirstPitch_Strikes", "clip_count": 3}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-18T18:20:00Z", "message": "report_published report_id=13 draft_status=published", "is_manual_alert": True, "suggestion_text": "acknowledge_and_distribute"}),
            Action(name="log_workflow_run", kwargs={"workflow_name": "post_game_package", "dag_name": "analytics_post_game_v1", "game_pk": 2024000008, "status": "success", "timestamp_utc": "2025-08-18T18:22:00Z", "start_time_utc": "2025-08-18T18:20:30Z", "end_time_utc": "2025-08-18T18:22:00Z", "log_s3_path": "s3://workflow/post_game_package/2024-03-05_g2024000008.log"}),
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_071",
        instruction=(
            "You are assembling an end-to-end post-game analytics packet for game 2024000008, ensuring standardized labels, persisted spatial features, policy-compliant insights, and the mandated video support.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Exactly one finalized post-game scouting dossier exists using the organization’s standard values:\n"
            "  — narrative label: post_game_review\n"
            "  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review\n"
            "  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf\n"
            "• Pitch-type labels are standardized and strike-zone spatial features are persisted using the org’s standard 12×12 catcher-view grid with bounds x∈[−1.5,1.5], z∈[1.0,4.0].\n"
            "• Execution evaluations use the game’s canonical five-pitch sample with frozen quadrant targets and miss distances as recorded in the dataset; do not infer or recompute.\n"
            "• Curated insights satisfy rules.py gates, collapse redundant bullets, and are ordered by supporting_stat_value DESC then player_id ASC, using canonical keys.\n"
            "• Curated video support uses exactly the policy-mandated playlist set — “Positive Reinforcement” and “Teaching Moments” — each with three clips linked to the dossier.\n"
            "• Workflow completion is recorded with frozen UTC times (start 2025-08-18T00:35:00Z, end 2025-08-18T01:05:00Z) and a deterministic S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.\n"
            "• Return the identifier of the finalized post-game dossier."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicates and sort curated insights by supporting_stat_value DESC then player_id ASC
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review", "status": "success",
                "start_time_utc": "2025-08-18T00:35:00Z", "end_time_utc": "2025-08-18T01:05:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_072",
        instruction=(
            "You are the pitcher development coordinator for Team 10. Prepare week-of 2025-08-11 development materials for Kevin Holmes (player_id=7) and Johnny Gonzalez (player_id=9) and immediately approve goals.\n"
            "\nAcceptance criteria (single, deterministic terminal state):\n"
            "1) Two player development reports exist with: (player_id=7, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/7/2025-08-11.pdf') and (player_id=9, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/9/2025-08-11.pdf').\n"
            "2) Exactly one goal per pitcher exists, each linked to its dev_report_id, with coach_id=1010, target_review_date='2025-09-08', and goal_text values 'execution_fastball_glove_side' (for player_id=7) and 'sequencing_tunnel_changeup' (for player_id=9). Both goals are 'Approved'.\n"
            "3) For each dev report, exactly two playlists exist: ('Positive Reinforcement', 5) and ('Teaching Moments', 3).\n"
            "4) Trend flags table was generated using min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10 after canonicalizing pitch types.\n"
            "5) A single workflow run is recorded as status='success' with dag_name='dev_weekly_pkg', start_time_utc='2025-08-14T12:00:00Z', end_time_utc='2025-08-14T12:12:00Z', log_s3_path='s3://ops/logs/dev_weekly_pkg/2025-08-14_team10.json'.\n"
            "\nPolicy references you must honor:\n"
            "• Canonicalize raw pitch types before trend computation; trend flags require min samples + EB shrinkage + FDR (record parameters deterministically).\n"
            "• Dev playlist categories enforce clip ranges: Positive Reinforcement ∈[3,5], Teaching Moments ∈[2,3].\n"
            "Return no values."
        ),
        actions=[
            Action(name="get_player_details", kwargs={"player_id": 7}),
            Action(name="get_player_details", kwargs={"player_id": 9}),
            Action(name="canonicalize_pitch_types", kwargs={"scope": "all"}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_player_dev_report", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="create_player_dev_report", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "execution_fastball_glove_side", "coach_id": 1010, "target_review_date": "2025-09-08"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "sequencing_tunnel_changeup", "coach_id": 1010, "target_review_date": "2025-09-08"}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="log_workflow_run", kwargs={"dag_name": "dev_weekly_pkg", "status": "success", "start_time_utc": "2025-08-14T12:00:00Z", "end_time_utc": "2025-08-14T12:12:00Z", "log_s3_path": "s3://ops/logs/dev_weekly_pkg/2025-08-14_team10.json"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_073",
        instruction=(
            "You are compiling an end-to-end analytics packet for game 2024000008 suitable for coaching distribution.\n\n"
            "Acceptance criteria (goal-oriented, non-procedural):\n"
            "• Packet is finalized as published with narrative label post_game_review, Google Slides link https://docs.google.com/presentation/d/post_game_review, and PDF s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Canonical pitch typing and persistent 12×12 catcher-view grid encoding (min_x=−1.5, max_x=1.5, min_z=1.0, max_z=4.0) are completed.\n"
            "• Trends are filtered with EB shrinkage and FDR q=0.10 at thresholds min_pitches=50, min_swings=30, min_bbe=25.\n"
            "• Curated insights are canonical, non-duplicative, and sorted by supporting_stat_value DESC then player_id ASC; use exactly: (2, execution_ff_high, 0.60), (4, execution_sl_low, 0.54), (8, situational_risp_high, 0.50), (2, predictability_firstpitch_high, 0.46).\n"
            "• Two support playlists exist: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (3 clips).\n"
            "• Publication audit recorded at 2025-08-18T18:25:00Z with message 'report_published report_id=13 draft_status=published'.\n"
            "• Workflow completion recorded with start_time_utc=2025-08-18T18:05:00Z, end_time_utc=2025-08-18T18:25:00Z, and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-3.log.\n"
            "• Do not list tool/API names or steps; deliver only the final state meeting these criteria."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "scouting_reports",
                "status_code": 200,
                "records_ingested": 1,
                "timestamp_utc": "2025-08-18T18:25:00Z",
                "message": "report_published report_id=13 draft_status=published",
                "game_pk": 2024000008
            }),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.54}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.50}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.46}),
            Action(name="list_curated_insights", kwargs={"report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="list_video_playlists", kwargs={"report_id": 13}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review",
                "status": "success",
                "start_time_utc": "2025-08-18T18:05:00Z",
                "end_time_utc": "2025-08-18T18:25:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-3.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_074",
        instruction=(
            "You ensure the Monday player-development check-ins for the week of 2025-08-11 are fully represented in the system for players 11 and 12. "
            "Your work is accepted only if, upon completion, the database corroborates all of the following deliverables—without prescribing any particular method or sequence—"
            "for game 2024000002 and those players: "
            "• exactly one weekly development report per player at the stated paths (player 11 → s3://reports/player_dev/11/2025-08-11.pdf; "
            "player 12 → s3://reports/player_dev/12/2025-08-11.pdf); "
            "• exactly one development goal per player in Approved state with target review date 2025-08-25 "
            "(player 11 → 'dev_goal_contact_quality' by coach 22; player 12 → 'dev_goal_zone_control' by coach 23); "
            "• one development packet per player with the following identifiers and links kept intact—"
            "player 11 narrative 'dev_weekly_packet_2025_08_11_p11' (slides https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11, "
            "PDF s3://reports/dev_packages/11/2025-08-11.pdf) and player 12 narrative 'dev_weekly_packet_2025_08_11_p12' "
            "(slides https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11, PDF s3://reports/dev_packages/12/2025-08-11.pdf)—"
            "each packet containing two playlists named 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "• one workflow activity labeled 'weekly_dev_checkins' recorded with start=end 2025-08-14T00:00:00Z and log path "
            "s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json. "
            "No additional outputs are required; only this terminal state is evaluated."
        ),
        actions=[
            Action(name="create_player_dev_report", kwargs={
                "player_id": 11,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/11/2025-08-11.pdf"
            }),
            Action(name="create_player_dev_report", kwargs={
                "player_id": 12,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/12/2025-08-11.pdf"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 11,
                "player_id": 11,
                "goal_text": "dev_goal_contact_quality",
                "coach_id": 22,
                "target_review_date": "2025-08-25"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 12,
                "player_id": 12,
                "goal_text": "dev_goal_zone_control",
                "coach_id": 23,
                "target_review_date": "2025-08-25"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p11",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/11/2025-08-11.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p12",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/12/2025-08-11.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 14, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 14, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "weekly_dev_checkins",
                "status": "completed",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_075",
        instruction=(
            "You are delivering a comprehensive post-game series-setup dossier for game 2024000008 for multi-day planning.\n\n"
            "Acceptance outcomes (deterministic end-state):\n"
            "• A published dossier exists labeled 'post_game_series_setup_v1' with slide deck https://slides.series/setup/2024000008 and PDF s3://reports/scouting/series_setup_v1/2024000008.pdf.\n"
            "• Pitch types are canonicalized; a persisted 12×12 catcher-view grid exists over x∈[−1.5,1.5] ft and z∈[1.0,4.0] ft.\n"
            "• Trend vetting applies empirical-Bayes shrinkage with FDR q=0.10 and minima 50/30/25; a leverage summary is recorded using threshold 1.5.\n"
            "• Six unique curated insights are attached (player→code→value): 4→execution_ff_high→0.62; 8→predictability_firstpitchstrike_high→0.57; 3→situational_risp_high→0.54; 5→tendency_chase_low→0.34; 6→stamina_b2b_low→0.40; 7→predictability_sequencing_high→0.60.\n"
            "• Three playlists tied to the dossier exist with 3 clips each: 'Positive Reinforcement', 'Teaching Moments', and 'Pattern Review'.\n"
            "• A manual publication audit exists at 2025-08-21T04:50:00Z with message 'report_published report_id=<that dossier id> draft_status=published' and suggestion_text 'acknowledge_and_distribute'.\n"
            "• The workflow run is recorded successful for 2025-08-21T04:35:00Z→2025-08-21T04:50:00Z at s3://workflow/logs/series_setup_v1/2024000008/2025-08-21-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True
            }),
            Action(name="compute_game_leverage_summary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_series_setup_v1",
                "gslides_link": "https://slides.series/setup/2024000008",
                "s3_pdf_path": "s3://reports/scouting/series_setup_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-21T04:50:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "is_manual_alert": True
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 5, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 6, "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.40
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Pattern Review", "clip_count": 3, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "series_setup_v1",
                "status": "success",
                "start_time_utc": "2025-08-21T04:35:00Z",
                "end_time_utc": "2025-08-21T04:50:00Z",
                "log_s3_path": "s3://workflow/logs/series_setup_v1/2024000008/2025-08-21-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_076",
        instruction=(
            "You are authoring the post-game package for gamePk 2024000007 (game_status Final). "
            "Acceptance requires the following final state:\n"
            "• A plate-umpire calibration record is present for this game with exactly: umpire_id=2, zone_shift_x=0.20, zone_shift_z=-0.10, calibration_error_pct=2.4, confidence_interval=0.90.\n"
            "• A persisted 12×12 zone grid exists for pitches using bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 (cells written back to the pitches table).\n"
            "• Three pitch execution grades exist for this game with these exact values and policy-consistent grades: (pitch_id=1, miss_distance_inches=10.2 ⇒ 'Major miss', intended_quadrant_model='down_middle', actual_quadrant='up_middle'); (pitch_id=3, miss_distance_inches=5.0 ⇒ 'Minor miss', intended_quadrant_model='away_edge', actual_quadrant='just_off_away'); (pitch_id=4, miss_distance_inches=2.0 ⇒ 'Executed', intended_quadrant_model='up_in', actual_quadrant='up_in').\n"
            "• Exactly one new post-game scouting report exists for 2024000007 with core_narrative_text 'postgame_core_thesis_execution_and_leverage', gslides_link 'https://slides.postgame/2024000007', s3_pdf_path 's3://reports/post_game/2024000007.pdf'.\n"
            "• Two curated insights are attached to that report with exactly: (player_id=7, insight_type='execution', insight_text='execution_gloveside_miss', supporting_stat_value=0.42) and (player_id=9, insight_type='situational', insight_text='situational_risp_late', supporting_stat_value=0.58).\n"
            "• One highlight playlist linked to the same report exists with playlist_name 'Game Highlights - Postgame Pulls' and clip_count 10.\n"
            "• A completed workflow run exists with dag_name 'post_game_report_build', game_pk 2024000007, status 'success', start_time_utc=end_time_utc='2025-08-14T00:00:00Z', log_s3_path 's3://logs/workflows/post_game_report_build_2024000007.log'; and an ingestion log exists with source_name 's3_event_log_upload', status_code 200, records_ingested 1."
        ),
        actions=[
            Action(name="write_umpire_game_model", kwargs={"game_pk": 2024000007, "umpire_id": 2, "zone_shift_x": 0.20, "zone_shift_z": -0.10, "calibration_error_pct": 2.4, "confidence_interval": 0.90}),
            Action(name="grid_encode_pitch_locations", kwargs={"min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 1, "game_pk": 2024000007, "intended_quadrant_model": "down_middle", "actual_quadrant": "up_middle", "miss_distance_inches": 10.2}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 3, "game_pk": 2024000007, "intended_quadrant_model": "away_edge", "actual_quadrant": "just_off_away", "miss_distance_inches": 5.0}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 4, "game_pk": 2024000007, "intended_quadrant_model": "up_in", "actual_quadrant": "up_in", "miss_distance_inches": 2.0}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000007, "core_narrative_text": "postgame_core_thesis_execution_and_leverage", "gslides_link": "https://slides.postgame/2024000007", "s3_pdf_path": "s3://reports/post_game/2024000007.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "execution_gloveside_miss", "insight_type": "execution", "supporting_stat_value": 0.42}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 9, "insight_text": "situational_risp_late", "insight_type": "situational", "supporting_stat_value": 0.58}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Game Highlights - Postgame Pulls", "clip_count": 10}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_report_build", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/post_game_report_build_2024000007.log"}),
            Action(name="log_ingestion_event", kwargs={"source_name": "s3_event_log_upload", "status_code": 200, "records_ingested": 1})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_077",
        instruction=(
            "You are producing a pre-series scouting package for the scheduled gamePk 2024000011 and must leave a single, auditable database state consistent with internal policy. "
            "To be accepted, verification must find: a persisted 12×12 pitch-location grid bounded at min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5; "
            "one pre-series scouting report for 2024000011 with core_narrative_text 'pre_series_thesis_attack_zones_and_baserunning', gslides_link 'https://slides.prep/2024000011', and s3_pdf_path 's3://reports/pre_series/2024000011.pdf' (which resolves to report_id 13 here and all child records must link to it); "
            "exactly three curated insights attached to that report — (player_id=11, 'tendency_hi_fb', type 'tendency', value 0.61), (player_id=12, 'predictability_first_pitch', type 'predictability', value 0.44), (player_id=7, 'execution_edge_low', type 'execution', value 0.38); "
            "two development-category playlists — 'Positive Reinforcement' with 4 clips and 'Teaching Moments' with 3 clips; "
            "and audit logs capturing a successful 'pre_series_package_build' workflow and a 'park_factors_ingest' tick with status_code 200 and records_ingested 2, both timestamped at '2025-08-14T00:00:00Z'."
        ),
        actions=[
            Action(name="grid_encode_pitch_locations", kwargs={"min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "persist": True}),
            Action(name="create_scouting_report", kwargs={"report_type": "pre-series", "game_pk": 2024000011, "core_narrative_text": "pre_series_thesis_attack_zones_and_baserunning", "gslides_link": "https://slides.prep/2024000011", "s3_pdf_path": "s3://reports/pre_series/2024000011.pdf"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "tendency_hi_fb", "insight_type": "tendency", "supporting_stat_value": 0.61}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 12, "insight_text": "predictability_first_pitch", "insight_type": "predictability", "supporting_stat_value": 0.44}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "execution_edge_low", "insight_type": "execution", "supporting_stat_value": 0.38}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="log_workflow_run", kwargs={"dag_name": "pre_series_package_build", "game_pk": 2024000011, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/pre_series_package_build_2024000011.log"}),
            Action(name="log_ingestion_event", kwargs={"source_name": "park_factors_ingest", "status_code": 200, "records_ingested": 2, "request_timestamp_utc": "2025-08-14T00:00:00Z"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_078",
        instruction=(
            "You complete a coach-visible in-game moments package for game 2024000007 with clear auditability, framed as acceptance criteria. "
            "Pitch data are normalized and discretized to the club’s 12×12 catcher-view grid using bounds x −1.5..1.5, z 1.0..4.0 with persistence. "
            "Exactly two coach-visible high-leverage bookmarks exist at 2025-08-14T00:00:00Z — (pitch 5 → 2.40, 'HR_to_LF_spike') and (pitch 6 → 2.74, 'BasesLoaded_K') — "
            "and exactly one coach-visible manual bench note exists ('mound_visit_recommendation', leverage 0.00) at the same clock. "
            "A published-only manual-note view for this game is available. "
            "The audit trail contains one source entry ('in_game_events_auto', status 200, records 2, 2025-08-14T00:00:00Z) and one workflow record labeled 'in_game_events_auto' "
            "with start=end 2025-08-14T00:00:00Z stored at s3://logs/workflows/in_game_events_auto/2025-08-14/run.json."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000007}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000007,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="create_auto_bookmark_event", kwargs={
                "game_pk": 2024000007, "pitch_id": 5, "leverage_index": 2.40, "narration": "HR_to_LF_spike",
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="create_auto_bookmark_event", kwargs={
                "game_pk": 2024000007, "pitch_id": 6, "leverage_index": 2.74, "narration": "BasesLoaded_K",
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000007, "suggestion_text": "mound_visit_recommendation", "leverage_index": 0.00,
                "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 15, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="list_game_day_events", kwargs={
                "game_pk": 2024000007, "is_manual_alert": True, "draft_status": "published"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "in_game_events_auto", "status_code": 200, "records_ingested": 2,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "in_game_events_auto",
                "game_pk": 2024000007,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/in_game_events_auto/2025-08-14/run.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_079",
        instruction=(
            "You are responsible for an auditable in-game bench alert for gamePk 2024000007 that also satisfies core standardization policy. "
            "Acceptance requires the database to unambiguously reflect all of the following end-state facts (no step listing is implied): "
            "(1) exactly one manual bench alert exists for this game with suggestion_text 'bench_reminder_slide_step', leverage_index 1.20, pitch_id set to null, is_manual_alert true, created at timestamp_utc '2025-08-14T00:00:00Z', and it is in published status at completion (with a recorded status-change time of '2025-08-14T00:00:00Z'); "
            "(2) the game’s pitch labels are unified under the organization’s canonical schema; "
            "(3) pitch locations are standardized into the organization’s canonical 12×12 strike-zone lattice with fixed bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 and persisted back; "
            "(4) the run is auditable via one successful job record 'bench_alert_publish' and one ingestion tick 'live_alerts_bus' with status_code 200 and records_ingested 1, both at '2025-08-14T00:00:00Z'."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000007}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000007,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000007,
                "pitch_id": None,
                "suggestion_text": "bench_reminder_slide_step",
                "leverage_index": 1.20,
                "draft_status": "draft",
                "is_manual_alert": True,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 13,
                "draft_status": "published",
                "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "bench_alert_publish",
                "game_pk": 2024000007,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/bench_alert_publish_2024000007.log"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "live_alerts_bus",
                "status_code": 200,
                "records_ingested": 1,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_080",
        instruction=(
            "You will deliver opponent-prep materials for the scheduled gamePk 2024000012 that meet collection policy without hidden defaults. "
            "Verification succeeds only if the final state shows: unified pitch labeling for this game; spatial standardization to the organization’s canonical 12×12 lattice with fixed bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5, persisted; "
            "and exactly one pre-series report for 2024000012 with core_narrative_text 'tendency_contact_upper_half', gslides_link 'https://slides.prep/2024000012', and s3_pdf_path 's3://reports/pre_series/2024000012.pdf'. "
            "Attach exactly two development-category playlists to that report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips)."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000012}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000012,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-series",
                "game_pk": 2024000012,
                "core_narrative_text": "tendency_contact_upper_half",
                "gslides_link": "https://slides.prep/2024000012",
                "s3_pdf_path": "s3://reports/pre_series/2024000012.pdf"
            }),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_081",
        instruction=(
            "You must deliver a weekly development check-in for player_id 7 for the week of 2024-07-29, with a fully specified, deterministic footprint. "
            "Acceptance requires: one and only one player development report for player_id 7 with week_of_date '2024-07-29' and s3_pdf_path 's3://reports/player_dev/7/2024-07-29.pdf'; "
            "a single micro-goal linked to that report with goal_text 'raise_swstr_rate_ff_top_third_2pct', coach_id 28, target_review_date '2024-08-05', reaching Approved status by completion; "
            "and exactly two development playlists attached to that report — 'Positive Reinforcement' clip_count 4 and 'Teaching Moments' clip_count 3. "
            "Also record a successful workflow run 'weekly_dev_reports' with start_time_utc=end_time_utc='2025-08-14T00:00:00Z' and log_s3_path 's3://logs/workflows/weekly_dev_reports_2024-07-29.log'. "
            "No unrelated ingestion ticks may be logged."
        ),
        actions=[
            Action(name="create_player_dev_report", kwargs={
                "player_id": 7,
                "week_of_date": "2024-07-29",
                "s3_pdf_path": "s3://reports/player_dev/7/2024-07-29.pdf"
            }),
            Action(name="create_player_dev_goal", kwargs={
                "dev_report_id": 11,
                "player_id": 7,
                "goal_text": "raise_swstr_rate_ff_top_third_2pct",
                "coach_id": 28,
                "target_review_date": "2024-08-05"
            }),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "weekly_dev_reports",
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/weekly_dev_reports_2024-07-29.log"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_082",
        instruction=(
            "You must leave a single, policy-compliant post-game package for gamePk 2024000002. "
            "Evaluation is based only on the final database state, not the steps taken. "
            "Auditors must be able to verify, from stored records alone and with no hidden defaults, that:\n"
            "• A pitch-type canonicalization pass was executed for this game (the pass itself is recorded as applied for gamePk 2024000002 even if zero rows required relabeling).\n"
            "• Pitch locations for this game are expressed on the organization’s canonical 12×12 strike-zone lattice using bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 and are persisted back to the pitches table.\n"
            "• A plate-umpire calibration exists for this game with exactly: umpire_id 3, zone_shift_x −0.08, zone_shift_z 0.05, calibration_error_pct 1.9, confidence_interval 0.95.\n"
            "• Three execution QC evaluations tied to this game exist with these precise tuples: "
            "(pitch_id=1, intended='down_middle', actual='up_middle', miss_distance_inches=9.5), "
            "(pitch_id=3, intended='away_edge', actual='just_off_away', miss_distance_inches=5.0), "
            "(pitch_id=4, intended='up_in', actual='up_in', miss_distance_inches=2.0).\n"
            "• A post-game scouting report exists for this game with core_narrative_text 'execution_gloveside_miss', "
            "gslides_link 'https://slides.postgame/2024000002', and s3_pdf_path 's3://reports/post_game/2024000002.pdf'.\n"
            "• Exactly two development playlists are linked to that report: 'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips).\n"
            "• An auditable workflow ledger entry exists for this game with dag_name 'post_game_full_pkg', status 'success', "
            "start_time_utc '2025-08-14T00:00:00Z', end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/post_game_full_pkg_2024000002.log'."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000002}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000002}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000002,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000002,
                "umpire_id": 3,
                "zone_shift_x": -0.08,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": 0.95
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 1, "game_pk": 2024000002,
                "intended_quadrant_model": "down_middle",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 9.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 3, "game_pk": 2024000002,
                "intended_quadrant_model": "away_edge",
                "actual_quadrant": "just_off_away",
                "miss_distance_inches": 5.0
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 4, "game_pk": 2024000002,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "up_in",
                "miss_distance_inches": 2.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000002,
                "core_narrative_text": "execution_gloveside_miss",
                "gslides_link": "https://slides.postgame/2024000002",
                "s3_pdf_path": "s3://reports/post_game/2024000002.pdf"
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_pkg",
                "game_pk": 2024000002,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/post_game_full_pkg_2024000002.log"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_083",
        instruction=(
            "You are executing the Phase-1 execution-QC subset for gamePk 2024000007—this is the minimal, policy-anchored standardization and evaluation block that precedes longer-form scouting and reporting. "
            "Acceptance requires a single, uniquely verifiable state showing: unified pitch labeling for the game; pitch locations standardized to a 12×12 grid at fixed bounds (min_x −2.0, max_x 2.0, min_z 1.0, max_z 3.5); "
            "and two deterministic execution evaluations recorded (pitch_id 1: intended 'down_middle' → actual 'up_middle', miss 9.5 in; pitch_id 3: intended 'away_edge' → actual 'just_off_away', miss 5.0 in). "
            "Record the successful job run with the fixed timestamp '2025-08-14T00:00:00Z'."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000007}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000007, "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 1, "game_pk": 2024000007, "intended_quadrant_model": "down_middle", "actual_quadrant": "up_middle", "miss_distance_inches": 9.5}),
            Action(name="write_pitch_execution_grade", kwargs={"pitch_id": 3, "game_pk": 2024000007, "intended_quadrant_model": "away_edge", "actual_quadrant": "just_off_away", "miss_distance_inches": 5.0}),
            Action(name="log_workflow_run", kwargs={"dag_name": "exec_qc_pipeline", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/exec_qc_pipeline_2024000007.log"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_084",
        instruction=(
            "You are validating in-game decision support for gamePk 2024000007 with explicit leverage and auditability. "
            "A compliant end state must show: one high-leverage auto bookmark (pitch_id 9, leverage_index 2.10, narration 'late_risp_ff_up') and one bench alert (suggestion_text 'hold_runner_first_third', leverage_index 0.00), "
            "both finalized as published with pitch_id null for the bench alert and is_manual_alert true. "
            "Spatial data must be standardized to a 12×12 grid at fixed bounds (min_x −2.0, max_x 2.0, min_z 1.0, max_z 3.5), and the run must be auditable with unified pitch labeling plus a successful job and a live-alerts ingestion tick at '2025-08-14T00:00:00Z'. "
            "No summaries or extraneous artifacts are permitted beyond these acceptance facts."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000007}),
            Action(name="create_auto_bookmark_event", kwargs={"game_pk": 2024000007, "pitch_id": 9, "leverage_index": 2.10, "narration": "late_risp_ff_up", "draft_status": "draft", "is_manual_alert": False, "timestamp_utc": "2025-08-14T00:00:00Z"}),
            Action(name="update_event_status", kwargs={"event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000007, "pitch_id": None, "suggestion_text": "hold_runner_first_third", "leverage_index": 0.0, "draft_status": "draft", "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z"}),
            Action(name="update_event_status", kwargs={"event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000007, "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True}),
            Action(name="log_workflow_run", kwargs={"dag_name": "in_game_event_validation", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/in_game_event_validation_2024000007.log"}),
            Action(name="log_ingestion_event", kwargs={"source_name": "live_alerts_bus", "status_code": 200, "records_ingested": 2, "request_timestamp_utc": "2025-08-14T00:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_085",
        instruction=(
            "You are accountable for a deterministic, audit-ready pre-series package for the scheduled gamePk 2024000011. "
            "Only the terminal database state matters; no particular sequence is implied. Auditors must be able to verify from stored records that: "
            "(1) this game’s pitch labels conform to the organization’s canonical schema and there is explicit evidence that the label-unification step was applied for this game—even if no rows required relabeling; "
            "(2) pitch locations are expressed on the organization’s canonical 12×12 strike-zone lattice using bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 and are persisted to the pitches table; "
            "(3) exactly one opponent report exists for this game with core_narrative_text 'predictability_first_pitch', gslides_link 'https://slides.prep/2024000011', and s3_pdf_path 's3://reports/pre_series/2024000011.pdf' (child records reference this same report, which resolves to report_id 13 in this dataset); "
            "(4) three player insights are attached to that report with the exact tuples: (player_id=11, type 'tendency', text 'tendency_hi_fb', value 0.61), (player_id=12, type 'predictability', text 'predictability_first_pitch', value 0.44), and (player_id=7, type 'execution', text 'execution_edge_low', value 0.38); "
            "(5) two development playlists are linked to that report—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips); "
            "(6) a successful pre-series workflow ledger entry exists for this game with dag_name 'pre_series_package_build', start_time_utc=end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/pre_series_package_build_2024000011.log'; "
            "and (7) one ingestion tick 'park_factors_ingest' is present at the same timestamp with status_code 200 and records_ingested 2."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000011}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000011,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "pre-series",
                "game_pk": 2024000011,
                "core_narrative_text": "predictability_first_pitch",
                "gslides_link": "https://slides.prep/2024000011",
                "s3_pdf_path": "s3://reports/pre_series/2024000011.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 11, "insight_text": "tendency_hi_fb",
                "insight_type": "tendency", "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 12, "insight_text": "predictability_first_pitch",
                "insight_type": "predictability", "supporting_stat_value": 0.44
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 7, "insight_text": "execution_edge_low",
                "insight_type": "execution", "supporting_stat_value": 0.38
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "pre_series_package_build",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/pre_series_package_build_2024000011.log"
            }),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "park_factors_ingest",
                "status_code": 200,
                "records_ingested": 2,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_086",
        instruction=(
            "You are accountable for leaving a complete, audit-ready post-game package for gamePk 2024000002 (Final). "
            "Evaluation considers only the terminal database state and not the means. Auditors must be able to verify, from stored records alone, that: "
            "the game’s pitch locations are expressed using the organization’s canonical strike-zone lattice (12×12 at bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5); "
            "the plate-umpire calibration on this game reflects exactly umpire_id 3 with zone_shift_x −0.08, zone_shift_z 0.05, calibration_error_pct 1.9, confidence_interval 0.95; "
            "execution QC records exist for the organization’s three designated checks on pitches 1, 3, and 4 with tuples "
            "(1: intended='down_middle', actual='up_middle', miss=9.5 in), "
            "(3: intended='away_edge', actual='just_off_away', miss=5.0 in), "
            "(4: intended='up_in', actual='up_in', miss=2.0 in); "
            "a post-game scouting report for this game exists with core_narrative_text 'execution_gloveside_miss', gslides_link 'https://slides.postgame/2024000002', and s3_pdf_path 's3://reports/post_game/2024000002.pdf'; "
            "the curated insight module for that report contains exactly three entries with (player_id=5, type 'tendency', text 'tendency_low_offspeed', value 0.47), "
            "(player_id=11, type 'execution', text 'execution_edge_up', value 0.52), and (player_id=2, type 'situational', text 'situational_two_strike', value 0.41); "
            "and the development media attached to the report consists of the two standard playlists—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips). "
            "Include a successful workflow ledger entry for this game bearing dag_name 'post_game_full_pkg' with start_time_utc=end_time_utc='2025-08-14T00:00:00Z' and log_s3_path 's3://logs/workflows/post_game_full_pkg_2024000002.log'. "
            "No specific sequence or tooling is implied—only this verifiable end state."
        ),
        actions=[
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000002,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="write_umpire_game_model", kwargs={
                "game_pk": 2024000002,
                "umpire_id": 3,
                "zone_shift_x": -0.08,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": 0.95
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 1, "game_pk": 2024000002,
                "intended_quadrant_model": "down_middle",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 9.5
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 3, "game_pk": 2024000002,
                "intended_quadrant_model": "away_edge",
                "actual_quadrant": "just_off_away",
                "miss_distance_inches": 5.0
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 4, "game_pk": 2024000002,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "up_in",
                "miss_distance_inches": 2.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000002,
                "core_narrative_text": "execution_gloveside_miss",
                "gslides_link": "https://slides.postgame/2024000002",
                "s3_pdf_path": "s3://reports/post_game/2024000002.pdf"
            }),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_low_offspeed", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "execution_edge_up", "insight_type": "execution", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_two_strike", "insight_type": "situational", "supporting_stat_value": 0.41}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_full_pkg",
                "game_pk": 2024000002,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/post_game_full_pkg_2024000002.log"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_087",
        instruction=(
            "You are accountable for a deterministic, audit-ready post-game summary for gamePk 2024000007 (Final). "
            "Only the terminal database state matters—no specific sequencing or API usage is implied. "
            "Auditors must be able to verify from stored records that: "
            "the game’s pitch locations are expressed using the organization’s canonical strike-zone lattice (12×12 at bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5) and persisted; "
            "exactly one post-game report exists for this game with core_narrative_text 'execution_edge_low', gslides_link 'https://slides.postgame/2024000007', and s3_pdf_path 's3://reports/post_game/2024000007.pdf'; "
            "two curated insights are attached to that report with the exact tuples (player_id=11, type 'tendency', text 'tendency_fb_hi', value 0.61) and "
            "(player_id=7, type 'predictability', text 'predictability_firstpitch_zone1', value 0.44); "
            "the development media attached to the report consists of exactly the two standard playlists—'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); "
            "one high-leverage bookmark exists on pitch_id 10 with leverage_index 2.20 and text 'late_game_ff_up', stored on the event and published with changed_at_utc '2025-08-14T00:00:00Z'; "
            "and a successful workflow ledger entry exists with dag_name 'series_summary_postgame', start_time_utc=end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/series_summary_postgame_2024000007.log'."
        ),
        actions=[
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000007,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000007,
                "core_narrative_text": "execution_edge_low",
                "gslides_link": "https://slides.postgame/2024000007",
                "s3_pdf_path": "s3://reports/post_game/2024000007.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "tendency_fb_hi",
                "insight_type": "tendency",
                "supporting_stat_value": 0.61
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitch_zone1",
                "insight_type": "predictability",
                "supporting_stat_value": 0.44
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="create_video_playlist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="create_auto_bookmark_event", kwargs={
                "game_pk": 2024000007,
                "pitch_id": 10,
                "leverage_index": 2.20,
                "narration": "late_game_ff_up",
                "draft_status": "draft",
                "is_manual_alert": False,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="update_event_status", kwargs={
                "event_id": 13,
                "draft_status": "published",
                "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "series_summary_postgame",
                "game_pk": 2024000007,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/series_summary_postgame_2024000007.log"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_088",
        instruction=(
            "You finalize a compact post-game snapshot for game 2024000003.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted with the organization’s standard bounds x∈[−0.95,0.95] ft, z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_policy_v1”, slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.\n"
            "• Exactly two coaching playlists are tied to the brief — “Positive Reinforcement” and “Teaching Moments” — each with exactly 3 clips per the organization’s post-game review checklist; any other clip count is unacceptable.\n"
            "• A publication audit (manual) is stored at 2025-08-18T18:20:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000003}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000003}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000003,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "min_effect_size": 0.05,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf",
                "draft_status": "published"
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000003,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "operator_note": "acknowledge_and_distribute",
                "is_manual_alert": True
            })
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_089",
        instruction=(
            "You deliver a teaching-focused post-game dossier for game 2024000008 that is policy-compliant and ready for staff use.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• Canonical pitch types and a persisted catcher-view grid (12×12; x∈[−0.95,0.95], z∈[1.5,3.5]).\n"
            "• Trend vetting recorded with EB shrinkage, FDR q=0.10, practical-effect ≥0.05, and minima 50/30/25.\n"
            "• A published dossier labeled for teaching use (core narrative “post_game_teachpack_v1”) with slide link https://docs.google.com/presentation/d/post_game_teachpack_v1 and PDF s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf.\n"
            "• Four unique curated insights mapped to appropriate roster players (no duplicate codes).\n"
            "• Exactly the two policy-mandated coaching playlists are tied to the dossier with 3 clips each: “Positive Reinforcement” and “Teaching Moments”.\n"
            "• A manual publication audit at 2025-08-20T21:10:00Z records the publication message verbatim, stores suggestion_text “acknowledge_and_distribute”, and saves the same publication message as the operator note.\n"
            "• The workflow run for this job is logged successful from 2025-08-20T20:55:00Z to 2025-08-20T21:10:00Z at s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "min_effect_size": 0.05,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "label": "post_game_teachpack_v1",
                "core_narrative_text": "post_game_teachpack_v1",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_teachpack_v1",
                "s3_pdf_path": "s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-20T21:10:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "operator_note": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            # Four curated insights (all unique codes)
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.34
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 3,
                "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.56
            }),
            # Policy playlists
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_teachpack_v1",
                "status": "success",
                "start_time_utc": "2025-08-20T20:55:00Z",
                "end_time_utc": "2025-08-20T21:10:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_090",
        instruction=(
            "You are finalizing a coach-facing post-game review for our home game. Assume upstream ingestion/QC are already approved and the game is complete.\n"
            "Acceptance criteria (terminal database state):\n"
            "• A post-game scouting brief exists for game_pk 2024000008 with core narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.\n"
            "• Execution evaluation is recorded for exactly five pitches from this game with the following intent/actual quadrants and miss distances (inches):\n"
            "  – pitch_id 29: intended down_away, actual down_middle, miss 2.4\n"
            "  – pitch_id 33: intended up_in, actual middle_in, miss 6.8\n"
            "  – pitch_id 46: intended down_away, actual down_away, miss 1.2\n"
            "  – pitch_id 17: intended up_away, actual up_middle, miss 4.1\n"
            "  – pitch_id 45: intended down_in, actual middle_in, miss 5.0\n"
            "• Six curated insights are attached to that brief using the required key template and values: \n"
            "  situational_risp_high (0.55) for player_id 8; predictability_firstpitch_high (0.31) for player_id 2; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8; situational_risp_high (0.52) for player_id 2; predictability_firstpitch_high (0.36) for player_id 4.\n"
            "• Four video playlists are attached to the brief: two named Positive Reinforcement with 3 clips each, and two named Teaching Moments with 2 clips each.\n"
            "• The workflow ledger records a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc == end_time_utc == 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.\n"
            "No additional outputs are required."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="write_pitch_execution_grade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.52
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.36
            }),
            # FIX: use the correct key 'playlist_name'
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_review_packet",
                "game_pk": 2024000008,
                "status": "success",
                "start_time_utc": "2025-08-18T00:00:00Z",
                "end_time_utc": "2025-08-18T00:00:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_091",
        instruction=(
            "You ship an execution-focused post-game dossier for game 2024000008 suitable for MLB coaching review.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• Pitch types are canonical; a 12×12 catcher-view grid is persisted with policy bounds x∈[−0.95,0.95], z∈[1.5,3.5].\n"
            "• Trends are vetted with EB shrinkage, FDR q=0.10, practical-effect ≥0.05, minima 50/30/25; a leverage summary is recorded at threshold 1.5.\n"
            "• Execution grading evidence includes three audited pitches using the standard quadrant model (catcher_view_q4_v1): one Executed (UL, 2.1″), one Minor Miss (UR, 7.5″), and one Major Miss (LL, 10.2″), consistent with policy thresholds (Minor ≤9″, Major >9″).\n"
            "• A published dossier labeled 'post_game_exec_focus_v1' exists with slide link https://docs.google.com/presentation/d/post_game_exec_focus_v1 and PDF s3://reports/scouting/post_game_exec_focus_v1/2024000008.pdf.\n"
            "• Six curated insights are non-redundant (distinct by player and metric) and ordered by supporting strength; themes are balanced and may repeat only when the metrics differ.\n"
            "• Exactly the two policy-mandated playlists are attached with 3 clips each.\n"
            "• A manual publication audit at 2025-08-21T23:25:00Z stores the publication message verbatim, suggestion_text “acknowledge_and_distribute”, and duplicates the message as the operator note; the workflow run is logged successful for 2025-08-21T23:10:00Z→2025-08-21T23:25:00Z at s3://workflow/logs/post_game_exec_focus_v1/2024000008/2025-08-21-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}
            ),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                    "fdr_threshold": 0.10, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"
                }
            ),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            # Execution grades
            Action(
                name="write_pitch_execution_grade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 1,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL",
                    "miss_distance_inches": 2.1, "grade": "Executed"
                }
            ),
            Action(
                name="write_pitch_execution_grade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 2,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR",
                    "miss_distance_inches": 7.5, "grade": "Minor Miss"
                }
            ),
            Action(
                name="write_pitch_execution_grade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 3,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL",
                    "miss_distance_inches": 10.2, "grade": "Major Miss"
                }
            ),
            # Dossier
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game", "game_pk": 2024000008,
                    "label": "post_game_exec_focus_v1",
                    "core_narrative_text": "post_game_exec_focus_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_exec_focus_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_exec_focus_v1/2024000008.pdf",
                    "draft_status": "published"
                }
            ),
            # Six curated insights (metrics/theme tokens comply with validator)
            Action(
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.64}
            ),
            Action(
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.58}
            ),
            Action(
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.56}
            ),
            Action(  # platoon-style content expressed within allowed theme set
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 7, "insight_text": "tendency_lhh_high", "insight_type": "tendency", "supporting_stat_value": 0.55}
            ),
            Action(
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.39}
            ),
            Action(
                name="add_curated_insight",
                kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.32}
            ),
            # Policy playlists
            Action(name="create_video_playlist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="create_video_playlist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            # Publication audit + workflow log
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008, "timestamp_utc": "2025-08-21T23:25:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "acknowledge_and_distribute",
                    "operator_note": "report_published report_id=13 draft_status=published",
                    "is_manual_alert": True
                }
            ),
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_exec_focus_v1", "status": "success",
                    "start_time_utc": "2025-08-21T23:10:00Z",
                    "end_time_utc": "2025-08-21T23:25:00Z",
                    "log_s3_path": "s3://workflow/logs/post_game_exec_focus_v1/2024000008/2025-08-21-1.log",
                    "game_pk": 2024000008
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_092",
        instruction=(
            "You assemble and publish a post-game development dossier for game 2024000008.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted with the organization’s standard bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_platoon_pred_v1”, slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1, and PDF s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf.\n"
            "• Exactly six curated insights are attached to the brief—exactly these six rows and in this order (no other curated insights are attached):\n"
            "   1) player_id=4, insight_text=execution_ff_high,              insight_type=execution,      supporting_stat_value=0.63\n"
            "   2) player_id=7, insight_text=predictability_sequencing_high, insight_type=predictability, supporting_stat_value=0.60\n"
            "   3) player_id=8, insight_text=tendency_chase_low,             insight_type=tendency,       supporting_stat_value=0.57\n"
            "   4) player_id=3, insight_text=situational_risp_high,          insight_type=situational,    supporting_stat_value=0.52\n"
            "   5) player_id=6, insight_text=stamina_lategame_low,           insight_type=stamina,        supporting_stat_value=0.49\n"
            "   6) player_id=2, insight_text=tendency_bunt_low,              insight_type=tendency,       supporting_stat_value=0.47\n"
            "• Two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) is stored at 2025-08-22T01:40:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n"
            "• A completed workflow run record exists with dag_name “post_game_platoon_pred_v1”, game_pk 2024000008, status “success”, start_time_utc 2025-08-22T01:39:00Z, end_time_utc 2025-08-22T01:41:00Z, and log_s3_path s3://workflow-runs/post_game_platoon_pred_v1/2024000008/2025-08-22T01:39:00Z.log.\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(
                name="grid_encode_pitch_locations",
                kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}
            ),
            Action(
                name="filter_trends",
                kwargs={
                    "game_pk": 2024000008,
                    "min_pitches": 50,
                    "min_swings": 30,
                    "min_bbe": 25,
                    "fdr_threshold": 0.1,
                    "min_effect_size": 0.05,
                    "use_eb_shrinkage": True,
                    "control": "FDR"
                }
            ),
            Action(
                name="create_scouting_report",
                kwargs={
                    "report_type": "post-game",
                    "game_pk": 2024000008,
                    "label": "post_game_platoon_pred_v1",
                    "core_narrative_text": "post_game_platoon_pred_v1",
                    "gslides_link": "https://docs.google.com/presentation/d/post_game_platoon_pred_v1",
                    "s3_pdf_path": "s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf",
                    "draft_status": "published"
                }
            ),
            # Curated insights (exactly the six rows, in order)
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high",               "insight_type": "execution",      "supporting_stat_value": 0.63}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high",   "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low",               "insight_type": "tendency",       "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high",            "insight_type": "situational",    "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low",             "insight_type": "stamina",        "supporting_stat_value": 0.49}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low",                "insight_type": "tendency",       "supporting_stat_value": 0.47}),
            # Required coaching playlists
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments",       "clip_count": 3}),
            # Publication audit (manual)
            Action(
                name="create_manual_alert_event",
                kwargs={
                    "game_pk": 2024000008,
                    "timestamp_utc": "2025-08-22T01:40:00Z",
                    "title": "publication_audit",
                    "message": "report_published report_id=13 draft_status=published",
                    "suggestion_text": "acknowledge_and_distribute",
                    "operator_note": "acknowledge_and_distribute",
                    "is_manual_alert": True
                }
            ),
            # Workflow run record (policy requirement)
            Action(
                name="log_workflow_run",
                kwargs={
                    "dag_name": "post_game_platoon_pred_v1",
                    "game_pk": 2024000008,
                    "status": "success",
                    "start_time_utc": "2025-08-22T01:39:00Z",
                    "end_time_utc": "2025-08-22T01:41:00Z",
                    "log_s3_path": "s3://workflow-runs/post_game_platoon_pred_v1/2024000008/2025-08-22T01:39:00Z.log"
                }
            )
        ],
        outputs=["13"]
    ),

    Task(
        annotator="saaish2",
        user_id="task_093",
        instruction=(
            "You finalize a high-leverage, teaching-ready post-game dossier for game 2024000008 that adheres strictly to policy and yields a single deterministic DB state.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• Canonical pitch types; persisted 12×12 catcher-view grid at policy bounds x∈[−0.95,0.95], z∈[1.5,3.5].\n"
            "• Policy trend vetting (EB shrinkage; FDR q=0.10; practical-effect ≥0.05; minima 50/30/25) and a high-leverage summary at threshold 1.5 are recorded.\n"
            "• A published dossier labeled 'post_game_highlev_teach_v1' exists with slide link https://docs.google.com/presentation/d/post_game_highlev_teach_v1 and PDF s3://reports/scouting/post_game_highlev_teach_v1/2024000008.pdf.\n"
            "• Six unique curated insights (no redundancy), with no duplicate theme entries for predictability; players are correctly mapped and insights ordered by supporting strength.\n"
            "• Exactly the two policy-mandated playlists are attached with 3 clips each.\n"
            "• A manual publication audit at 2025-08-22T01:40:00Z stores the standard publication message, suggestion_text “acknowledge_and_distribute”, and the same text in operator note; the workflow run is logged successful for 2025-08-22T01:25:00Z→2025-08-22T01:40:00Z at s3://workflow/logs/post_game_highlev_teach_v1/2024000008/2025-08-22-1.log."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000008}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={
                "game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True
            }),
            Action(name="filter_trends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                "fdr_threshold": 0.10, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"
            }),
            # Create dossier first, then record publication audit, then compute leverage summary so manual activity is captured
            Action(name="create_scouting_report", kwargs={
                "report_type": "post-game", "game_pk": 2024000008,
                "label": "post_game_highlev_teach_v1",
                "core_narrative_text": "post_game_highlev_teach_v1",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_highlev_teach_v1",
                "s3_pdf_path": "s3://reports/scouting/post_game_highlev_teach_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:40:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "operator_note": "acknowledge_and_distribute",
                "is_manual_alert": True
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            # Curated insights (ordered by supporting_stat_value desc; no duplicate 'predictability')
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 7,
                "insight_text": "tendency_platoonlhh_high", "insight_type": "tendency", "supporting_stat_value": 0.59
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 3,
                "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 6,
                "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.41
            }),
            Action(name="add_curated_insight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.33
            }),
            # Policy playlists
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="create_video_playlist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            # Workflow log
            Action(name="log_workflow_run", kwargs={
                "dag_name": "post_game_highlev_teach_v1", "status": "success",
                "start_time_utc": "2025-08-22T01:25:00Z",
                "end_time_utc": "2025-08-22T01:40:00Z",
                "log_s3_path": "s3://workflow/logs/post_game_highlev_teach_v1/2024000008/2025-08-22-1.log",
                "game_pk": 2024000008
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_094",
        instruction=(
            "You finalize a compact post-game snapshot for game 2024000003.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-18T18:10:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_policy_v1”, slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.\n"
            "• Exactly two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) is stored at 2025-08-18T18:20:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:10:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000003}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_policy_v1", "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_095",
        instruction=(
            "You publish a concise post-game snapshot for game 2024000003.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The pitch dataset is normalized to the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 grid is persisted at standard bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded with EB shrinkage and FDR q=0.10 (min_pitches=50, min_swings=30, min_bbe=25, practical-effect≥0.05).\n"
            "• A published post-game brief exists with core narrative “post_game_snapshot_v1”, slide link https://slides.example.org/post/2024000003_snapshot, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_snapshot.pdf.\n"
            "• Exactly two curated insights are attached—these two only, in order:\n"
            "   1) player_id=7, insight_text=predictability_firstpitch_high, insight_type=predictability, supporting_stat_value=0.58\n"
            "   2) player_id=8, insight_text=tendency_chase_low,             insight_type=tendency,       supporting_stat_value=0.47\n"
            "• One coaching playlist is tied: “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) is stored at 2025-08-18T18:20:00Z with message “report_published report_id=<id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000003}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_snapshot_v1", "core_narrative_text": "post_game_snapshot_v1", "gslides_link": "https://slides.example.org/post/2024000003_snapshot", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_snapshot.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.58}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=["13"]
    ),

    Task(
        annotator="saaish2",
        user_id="task_096",
        instruction=(
            "You complete a platoon/predictability post-game briefing for game 2024000008.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-22T03:30:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_platoon_pred_v1”, slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_platoon_pred.pdf.\n"
            "• Five curated insights (unique categories, order preserved) are tied to the brief: execution_ff_high [execution, 0.63] for player 4; predictability_sequencing_high [predictability, 0.60] for player 7; tendency_chase_low [tendency, 0.57] for player 8; situational_risp_high [situational, 0.52] for player 3; stamina_lategame_low [stamina, 0.49] for player 6.\n"
            "• Two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) exists at 2025-08-22T03:40:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T03:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_platoon_pred_v1", "core_narrative_text": "post_game_platoon_pred_v1", "gslides_link": "https://docs.google.com/presentation/d/post_game_platoon_pred_v1", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_platoon_pred.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.63}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T03:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_097",
        instruction=(
            "You compile a two-strike approach post-game brief for game 2024000008.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-22T02:00:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_two_strike_v1”, slide link https://slides.example.org/post/2024000008_two_strike, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_two_strike.pdf.\n"
            "• Three curated insights (order preserved) are tied to the brief: execution_ff_high [execution, 0.62] for player 4; predictability_sequencing_high [predictability, 0.59] for player 7; situational_risp_high [situational, 0.52] for player 3.\n"
            "• Two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) exists at 2025-08-22T02:10:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:00:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_two_strike_v1", "core_narrative_text": "post_game_two_strike_v1", "gslides_link": "https://slides.example.org/post/2024000008_two_strike", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_two_strike.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:10:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_098",
        instruction=(
            "You deliver a baserunning/control post-game brief for game 2024000008.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-22T02:30:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• Any pitch execution grading in this deliverable uses only the allowed labels: Executed, Minor miss, Major miss.\n"
            "• A published post-game brief exists with core narrative “post_game_baserun_ctrl_v1”, slide link https://slides.example.org/post/2024000008_baserun_ctrl, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_baserun_ctrl.pdf.\n"
            "• Four curated insights (order preserved) are tied to the brief: tendency_bunt_low [tendency, 0.47] for player 2; execution_ff_high [execution, 0.61] for player 4; predictability_firstpitchstrike_high [predictability, 0.57] for player 8; situational_risp_high [situational, 0.51] for player 3.\n"
            "• Two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) exists at 2025-08-22T02:40:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 1, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 2.0, "grade": "Executed"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 2, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR", "miss_distance_inches": 7.0, "grade": "Minor miss"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 3, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL", "miss_distance_inches": 10.0, "grade": "Major miss"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_baserun_ctrl_v1", "core_narrative_text": "post_game_baserun_ctrl_v1", "gslides_link": "https://slides.example.org/post/2024000008_baserun_ctrl", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_baserun_ctrl.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.51}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_099",
        instruction=(
            "You deliver a comprehensive mixed-model post-game brief for game 2024000008.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-22T01:30:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_mixed_model_v1”, slide link https://slides.example.org/post/2024000008_mixed_model, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_mixed_model.pdf.\n"
            "• Six curated insights (themes unique, order preserved) are tied to the brief: execution_ff_high [execution, 0.63] for player 4; predictability_sequencing_high [predictability, 0.60] for player 7; tendency_chase_low [tendency, 0.57] for player 8; situational_risp_high [situational, 0.52] for player 3; stamina_lategame_low [stamina, 0.49] for player 6; tendency_bunt_low [tendency, 0.47] for player 2.\n"
            "• Two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) exists at 2025-08-22T01:40:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n"
            "• A workflow run record exists with dag_name “post_game_mixed_model_v1”, status “success”, start_time_utc 2025-08-22T01:39:00Z, end_time_utc 2025-08-22T01:41:00Z, and log_s3_path s3://workflow-runs/post_game_mixed_model_v1/2024000008/2025-08-22T01:39:00Z.log.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_mixed_model_v1", "core_narrative_text": "post_game_mixed_model_v1", "gslides_link": "https://slides.example.org/post/2024000008_mixed_model", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_mixed_model.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.63}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.57}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_mixed_model_v1", "game_pk": 2024000008, "status": "success", "start_time_utc": "2025-08-22T01:39:00Z", "end_time_utc": "2025-08-22T01:41:00Z", "log_s3_path": "s3://workflow-runs/post_game_mixed_model_v1/2024000008/2025-08-22T01:39:00Z.log"})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_100",
        instruction=(
            "You assemble and publish a post-game two-strike approach brief for game 2024000008 including graded execution, curated insights, playlists, and full audit.\n\n"
            "Acceptance outcomes:\n"
            "• Canonical pitch types; a catcher-view 12×12 location grid is persisted with the organization’s standard bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trends are vetted with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05 using thresholds (min_pitches=50, min_swings=30, min_bbe=25).\n"
            "• Leverage summary recorded at threshold 1.5.\n"
            "• Four execution grades are stored using intended_quadrant_model “catcher_view_q4_v1”: (1→Executed UL 2.0”), (2→Minor Miss UR 7.0”), (3→Major Miss LL 10.0”), (4→Executed UL 1.8”).\n"
            "• A published brief exists with core narrative “post_game_two_strike_v1”, slide link https://slides.example.org/post/2024000008_two_strike, and PDF s3://reports/scouting/post/2024-08-01_g2024000008_two_strike.pdf.\n"
            "• Exactly five curated insights—these only, in order:\n"
            "   1) player_id=4, insight_text=execution_ff_high,              insight_type=execution,      supporting_stat_value=0.62\n"
            "   2) player_id=7, insight_text=predictability_sequencing_high, insight_type=predictability, supporting_stat_value=0.59\n"
            "   3) player_id=3, insight_text=situational_risp_high,          insight_type=situational,    supporting_stat_value=0.52\n"
            "   4) player_id=6, insight_text=stamina_lategame_low,           insight_type=stamina,        supporting_stat_value=0.49\n"
            "   5) player_id=8, insight_text=tendency_chase_low,             insight_type=tendency,       supporting_stat_value=0.45\n"
            "• Two playlists tied: “Positive Reinforcement” (3) and “Teaching Moments” (3).\n"
            "• Manual publication audit at 2025-08-22T02:30:00Z with message “report_published report_id=<id> draft_status=published”, suggestion_text/operator_note “acknowledge_and_distribute”.\n"
            "• Workflow run recorded with dag_name “post_game_two_strike_v1”, status “success”, start_time_utc 2025-08-22T02:29:00Z, end_time_utc 2025-08-22T02:31:00Z, log s3://workflow-runs/post_game_two_strike_v1/2024000008/2025-08-22T02:29:00Z.log.\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000008}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 1, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 2.0, "grade": "Executed"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 2, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR", "miss_distance_inches": 7.0, "grade": "Minor Miss"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 3, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL", "miss_distance_inches": 10.0, "grade": "Major Miss"}),
            Action(name="write_pitch_execution_grade", kwargs={"game_pk": 2024000008, "pitch_id": 4, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 1.8, "grade": "Executed"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_two_strike_v1", "core_narrative_text": "post_game_two_strike_v1", "gslides_link": "https://slides.example.org/post/2024000008_two_strike", "s3_pdf_path": "s3://reports/scouting/post/2024-08-01_g2024000008_two_strike.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.45}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:30:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_two_strike_v1", "game_pk": 2024000008, "status": "success", "start_time_utc": "2025-08-22T02:29:00Z", "end_time_utc": "2025-08-22T02:31:00Z", "log_s3_path": "s3://workflow-runs/post_game_two_strike_v1/2024000008/2025-08-22T02:29:00Z.log"})
        ],
        outputs=["13"]
    ),

    Task(
        annotator="saaish2",
        user_id="task_101",
        instruction=(
            "You deliver an organization-compliance post-game brief for game 2024000003 that meets policy gates and publication standards.\n\n"
            "Acceptance outcomes (terminal DB state):\n"
            "• The game is confirmed Final prior to any post-game writes; this gate is evidenced by a manual audit at 2025-08-18T18:10:00Z with title “status_gate_check”, message “game_status=Final”, suggestion_text “gate_ok”, and the same text saved as operator_note.\n"
            "• The game’s pitch data uses the organization’s canonical pitch-type taxonomy.\n"
            "• A catcher-view 12×12 location grid is persisted using bounds x∈[−0.95,0.95] ft and z∈[1.5,3.5] ft.\n"
            "• Trend vetting is recorded using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.\n"
            "• A published post-game brief exists with core narrative “post_game_policy_v1”, slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.\n"
            "• Exactly four curated insights (order preserved) are tied to the brief: execution_ff_high [execution, 0.62] for player 4; predictability_sequencing_high [predictability, 0.59] for player 7; situational_risp_high [situational, 0.53] for player 3; tendency_bunt_low [tendency, 0.47] for player 2.\n"
            "• Exactly two coaching playlists are tied to the brief: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).\n"
            "• A publication audit (manual) is stored at 2025-08-18T18:20:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the same text saved as operator note.\n"
            "• A workflow run record exists with dag_name “post_game_policy_v1”, status “success”, start_time_utc 2025-08-18T18:19:00Z, end_time_utc 2025-08-18T18:21:00Z, and log_s3_path s3://workflow-runs/post_game_policy_v1/2024000003/2025-08-18T18:19:00Z.log.\n\n"
            "Return only the brief’s report id."
        ),
        actions=[
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:10:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000003}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="filter_trends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="create_scouting_report", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_policy_v1", "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="log_workflow_run", kwargs={"dag_name": "post_game_policy_v1", "game_pk": 2024000003, "status": "success", "start_time_utc": "2025-08-18T18:19:00Z", "end_time_utc": "2025-08-18T18:21:00Z", "log_s3_path": "s3://workflow-runs/post_game_policy_v1/2024000003/2025-08-18T18:19:00Z.log"})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_102",
        instruction=(
            "You support in-game comms for gamePk 2024000012 (Scheduled). Your objective is to bring the game’s alerting and auditing state into policy — one high-priority manual alert on record for the game, leverage accounting recomputed at the strict >1.5 threshold, and deterministic audit artifacts captured — without prescribing how you achieve it.\n\n"
            "Terminal acceptance state (outcomes only):\n"
            "• The event ledger for this game contains exactly one high-priority manual alert with suggestion_text='shift outfield two steps opposite field', is_manual_alert=true, draft_status='published', leverage_index=1.6, timestamp_utc='2025-08-14T00:00:00Z'.\n"
            "• A leverage summary for the game exists using threshold=1.5 (strict high-leverage policy).\n"
            "• Audit artifacts exist for this operation: an ingestion log (source_name='in_game_alert_manual', status_code=200, records_ingested=1, request_timestamp_utc='2025-08-14T00:00:00Z') and a workflow run record (dag_name='in_game_alert', game_pk=2024000012, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:02:00Z', log_s3_path='s3://workflow/in_game_alert/2024000012/log.json')."
        ),
        actions=[
            Action(name="get_game_details", kwargs={"game_pk": 2024000012}),
            Action(name="list_game_day_events", kwargs={"game_pk": 2024000012}),
            Action(name="create_manual_alert_event", kwargs={
                "game_pk": 2024000012,
                "suggestion_text": "shift outfield two steps opposite field",
                "leverage_index": 1.6,
                "draft_status": "published",
                "is_manual_alert": True,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000012, "threshold": 1.5}),
            Action(name="log_ingestion_event", kwargs={
                "source_name": "in_game_alert_manual",
                "status_code": 200,
                "records_ingested": 1,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="log_workflow_run", kwargs={
                "dag_name": "in_game_alert",
                "game_pk": 2024000012,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:02:00Z",
                "log_s3_path": "s3://workflow/in_game_alert/2024000012/log.json"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_103",
        instruction=(
            "You own the weekly development cadence for player_id=8 (Daniel Davis). Your objective is to deliver a finalized one-page development brief and an approved micro-goal, attach the two required development review playlists, persist the organization’s trend-filter policy, and record a deterministic run log. "
            "Acceptance state: a new development brief exists for week_of_date='2025-08-11' at s3://reports/player_dev/8/2025-08-11.pdf; an approved micro-goal exists for that brief with goal_text='increase_slider_usage_3pct', coach_id=902, target_review_date='2025-08-18'; the brief is accompanied by exactly two playlists — 'Positive Reinforcement' (clip_count=4, link 'https://portal.internal/videos/report/11/positive') and 'Teaching Moments' (clip_count=3, link 'https://portal.internal/videos/report/11/teaching'); trend filter parameters are persisted exactly as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10; and a workflow run is recorded with dag_name='player_dev', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:01:00Z', log_s3_path='s3://workflow/player_dev/8/2025-08-11/log.json'."
        ),
        actions=[
            Action(name="create_player_dev_report", kwargs={"player_id": 8, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/8/2025-08-11.pdf"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 11, "player_id": 8, "goal_text": "increase_slider_usage_3pct", "coach_id": 902, "target_review_date": "2025-08-18"}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/11/positive"}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/11/teaching"}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="log_workflow_run", kwargs={"dag_name": "player_dev", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:01:00Z", "log_s3_path": "s3://workflow/player_dev/8/2025-08-11/log.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_104",
        instruction=(
            "You are responsible for the pre-game scouting deliverable for team_id=6 covering the next scheduled game on/after 2024-08-30. Your objective is to deliver the artifact that conforms to the org’s Pre-Game Package Spec v1 and data-prep policy, with a single unambiguous terminal state.\n\n"
            "Acceptance criteria (terminal state only — describe outcomes, not steps):\n"
            "• The next scheduled game is resolved and the opponent for team 6 is identified.\n"
            "• Exactly one pre-game scouting report exists for that game with report_type='pre-game', s3_pdf_path='s3://reports/scouting/pre/2024-08-31_g2024000004_team6.pdf', gslides_link='https://slides.example.org/pre/2024000004', core_narrative_text='pre_game_policy_v1'.\n"
            "• Exactly one curated insight is attached to that report: (player_id=5, insight_type='tendency', insight_text='tendency_firstpitchstrike_low', supporting_stat_value=0.321).\n"
            "• Two video playlists exist for that report — 'Opponent Pitcher Tendencies' (clip_count=4, link 'https://portal.internal/videos/report/13/tendencies_pre') and 'Opponent Miss Locations' (clip_count=3, link 'https://portal.internal/videos/report/13/miss_locations_pre').\n"
            "• For that game, pitch types are in the canonical schema and a 12×12 catcher-view grid representation of plate_x/plate_z has been generated with bounds −2.0..2.0 (x) and 0.0..4.0 (z) without persisting the grid back to storage.\n"
            "• Trend filtering parameters are persisted as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.\n"
            "• One workflow run record exists with dag_name='pre_game', game_pk=2024000004, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:05:00Z', log_s3_path='s3://workflow/pre_game/2024000004/log.json'."
        ),
        actions=[
            Action(name="find_next_scheduled_game", kwargs={"current_date": "2024-08-30"}),
            Action(name="get_opponent_for_team_in_game", kwargs={"game_pk": 2024000004, "team_id": 6}),
            Action(name="canonicalize_pitch_types", kwargs={"game_pk": 2024000004}),
            Action(name="grid_encode_pitch_locations", kwargs={"game_pk": 2024000004, "min_x": -2.0, "max_x": 2.0, "min_z": 0.0, "max_z": 4.0, "persist": False}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="create_scouting_report", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "s3_pdf_path": "s3://reports/scouting/pre/2024-08-31_g2024000004_team6.pdf", "gslides_link": "https://slides.example.org/pre/2024000004", "core_narrative_text": "pre_game_policy_v1"}),
            Action(name="add_curated_insight", kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_firstpitchstrike_low", "insight_type": "tendency", "supporting_stat_value": 0.321}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/13/tendencies_pre"}),
            Action(name="create_video_playlist", kwargs={"report_id": 13, "playlist_name": "Opponent Miss Locations", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/13/miss_locations_pre"}),
            Action(name="log_workflow_run", kwargs={"dag_name": "pre_game", "game_pk": 2024000004, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:05:00Z", "log_s3_path": "s3://workflow/pre_game/2024000004/log.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_105",
        instruction=(
            "You are responsible for the off-day two-player development roll-up for team_id=10. Your objective is to deliver finalized one-page briefs and approved micro-goals for both active players on that roster snapshot, ensure the organization’s trend-filter policy is in force (min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10), provide the required review playlists, and document the week’s process.\n\n"
            "Terminal acceptance state (outcomes only):\n"
            "• The database contains two finalized development briefs for week_of_date='2025-08-11' stored at s3://reports/player_dev/7/2025-08-11.pdf and s3://reports/player_dev/9/2025-08-11.pdf.\n"
            "• Each corresponding micro-goal is present and approved: for player_id=7, goal_text='improve_two_strike_battle_rate' with coach_id=501 and target_review_date='2025-08-18'; for player_id=9, goal_text='tighten_inner_third_swing_decisions' with coach_id=501 and target_review_date='2025-08-18'.\n"
            "• The organization’s trend filter settings are persisted exactly as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.\n"
            "• Each brief is associated with exactly two review playlists: for the brief tied to dev_report_id=11 → 'Positive Reinforcement' (clip_count=3, link https://portal.internal/videos/report/11/positive) and 'Teaching Moments' (clip_count=2, link https://portal.internal/videos/report/11/teaching); for the brief tied to dev_report_id=12 → 'Positive Reinforcement' (clip_count=4, link https://portal.internal/videos/report/12/positive) and 'Teaching Moments' (clip_count=3, link https://portal.internal/videos/report/12/teaching).\n"
            "• A weekly process record shows a successful run with dag_name='weekly_dev', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:04:00Z', and log_s3_path='s3://workflow/weekly_dev/2025-08-11/log.json'."
        ),
        actions=[
            Action(name="get_active_roster", kwargs={"team_id": 10, "include_il": False}),
            Action(name="create_player_dev_report", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "improve_two_strike_battle_rate", "coach_id": 501, "target_review_date": "2025-08-18"}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 20}),
            Action(name="create_player_dev_report", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "tighten_inner_third_swing_decisions", "coach_id": 501, "target_review_date": "2025-08-18"}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 21}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/11/positive"}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 2, "internal_portal_link": "https://portal.internal/videos/report/11/teaching"}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/12/positive"}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/12/teaching"}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="log_workflow_run", kwargs={"dag_name": "weekly_dev", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:04:00Z", "log_s3_path": "s3://workflow/weekly_dev/2025-08-11/log.json"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_106",
        instruction=(
            "You are the analytics coordinator. Augment the existing pre-game package tied to report_id=8 deterministically."
            " Acceptance criteria (single terminal state):"
            "\n1) Exactly two additional curated insights exist on report_id=8 with these exact fields:"
            " (player_id=2, insight_text='tendency_chaserate_high', insight_type='tendency', supporting_stat_value=0.412)"
            " and (player_id=11, insight_text='predictability_firstpitchswing_low', insight_type='predictability', supporting_stat_value=0.193)."
            " The insight_texts must follow '{category}_{metric}_{bucket}' using only lowercase letters/digits in each token."
            "\n2) One new playlist is attached to report_id=8 with playlist_name='Scouting Focus: Top 5 ABs', internal_portal_link='https://portal.example.org/videos/report/8/focus_top5', clip_count=5."
            "\n3) A leverage summary is persisted for game_pk=2024000001 using threshold=1.5."
            "\n4) One pre-game note exists for game_pk=2024000001 with suggestion_text='Travel & rest plan confirmed', leverage_index=0.0, draft_status='archived'."
            "\n5) One workflow run is logged with dag_name='pre_game_curations', game_pk=2024000001, status='success',"
            " start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:10:00Z', log_s3_path='s3://logs/pre_game/2024000001/curations_run.log'."
            "\n6) One ingestion log exists for source_name='pre_game_curations_assets', status_code=200, records_ingested=27, request_timestamp_utc='2025-08-14T00:26:00Z'."
            "\nAll arguments must be explicit; no hidden defaults."
        ),
        actions=[
            Action(name="add_curated_insight", kwargs={"report_id": 8, "player_id": 2, "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.412}),
            Action(name="add_curated_insight", kwargs={"report_id": 8, "player_id": 11, "insight_text": "predictability_firstpitchswing_low", "insight_type": "predictability", "supporting_stat_value": 0.193}),
            Action(name="create_video_playlist", kwargs={"report_id": 8, "playlist_name": "Scouting Focus: Top 5 ABs", "internal_portal_link": "https://portal.example.org/videos/report/8/focus_top5", "clip_count": 5}),
            Action(name="compute_game_leverage_summary", kwargs={"game_pk": 2024000001, "threshold": 1.5}),
            Action(name="create_manual_alert_event", kwargs={"game_pk": 2024000001, "suggestion_text": "Travel & rest plan confirmed", "leverage_index": 0.0, "draft_status": "archived", "is_manual_alert": True}),
            Action(name="log_workflow_run", kwargs={"dag_name": "pre_game_curations", "game_pk": 2024000001, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:10:00Z", "log_s3_path": "s3://logs/pre_game/2024000001/curations_run.log"}),
            Action(name="log_ingestion_event", kwargs={"source_name": "pre_game_curations_assets", "status_code": 200, "records_ingested": 27, "request_timestamp_utc": "2025-08-14T00:26:00Z"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_107",
        instruction=(
            "You are the pitching development coordinator. Finalize a weekly development snapshot for Twins hitters Kevin Holmes (player_id=7) and Johnny Gonzalez (player_id=9) for week_of_date='2025-08-11'."
            " Acceptance criteria (single terminal state):"
            "\n1) Two new player development reports exist with exact fields:"
            " (player_id=7, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/7/2025-08-11.pdf') and"
            " (player_id=9, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/9/2025-08-11.pdf')."
            "\n2) A new development goal exists for player_id=7 linked to the new dev report with goal_text='Improve swing decisions (OOZ chase −5pp)', coach_id=501, target_review_date='2025-08-18' and goal_status='Proposed'."
            "\n3) A new development goal exists for player_id=9 linked to the new dev report with goal_text='Elevate hard-hit% (95+ EV +3pp)', coach_id=502, target_review_date='2025-08-18' and goal_status='Proposed'."
            "\n4) Existing goal_id=19 is set to goal_status='Approved'."
            "\n5) Trend filtering parameters are persisted with min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.1."
            "\n6) For each of the two new player development reports, exactly two playlists exist with policy-conforming clip counts:"
            " 'Positive Reinforcement' (clip_count=4) and 'Teaching Moments' (clip_count=3)."
            "\n7) A workflow run is logged with dag_name='weekly_dev_reports', status='success', start_time_utc='2025-08-14T01:00:00Z', end_time_utc='2025-08-14T01:08:00Z', log_s3_path='s3://logs/dev/2025-08-11/weekly_run.log'."
            "\nExplicit arguments only; no hidden defaults."
        ),
        actions=[
            Action(name="create_player_dev_report", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="create_player_dev_report", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "Improve swing decisions (OOZ chase −5pp)", "coach_id": 501, "target_review_date": "2025-08-18", "goal_status": "Proposed"}),
            Action(name="create_player_dev_goal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "Elevate hard-hit% (95+ EV +3pp)", "coach_id": 502, "target_review_date": "2025-08-18", "goal_status": "Proposed"}),
            Action(name="approve_player_dev_goal", kwargs={"goal_id": 19}),
            Action(name="filter_trends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1}),
            # Dev report playlists (policy-enforced names and clip counts)
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="create_video_playlist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="create_video_playlist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="log_workflow_run", kwargs={"dag_name": "weekly_dev_reports", "status": "success", "start_time_utc": "2025-08-14T01:00:00Z", "end_time_utc": "2025-08-14T01:08:00Z", "log_s3_path": "s3://logs/dev/2025-08-11/weekly_run.log"})
        ],
        outputs=[]
    ),

]
