from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="saaish2",
        user_id="task_001",
        instruction=(
            """
            You hold the position of lead analyst in the player development department for Team 3 (Blue Jays). Your task is to generate and complete the weekly development packages for every 'Active' roster player for the week commencing on 2025-08-11. Each player's final output must encompass a development report with an authorized goal and two distinct video playlists. In the case of Scott Arnold, the objective is 'Improve two-strike approach' (coach ID 28), with his 'Positive Reinforcement' playlist comprising 4 clips, and his 'Teaching Moments' playlist containing 3. Regarding James Brown, the aim is 'Increase contact rate on high fastballs' (coach ID 33), with his 'Positive Reinforcement' playlist including 5 clips, and his 'Teaching Moments' playlist featuring 2. The intended review date for both objectives is '2025-09-15'. Document the entire batch process as a single workflow execution with a starting time of '2025-08-11T10:00:00Z' and a concluding time of '2025-08-11T11:30:00Z'. Provide the unique `run_id` for the finalized workflow.
            """
        ),
        actions=[
            Action(name="GetActiveRoster", kwargs={"team_id": 3}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 3, "week_of_date": "2025-08-11"}),
            Action(
                name="CreatePlayerDevGoal",
                kwargs={
                    "dev_report_id": 11,
                    "player_id": 3,
                    "goal_text": "Improve two-strike approach",
                    "coach_id": 28,
                    "target_review_date": "2025-09-15",
                },
            ),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3},
            ),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 8, "week_of_date": "2025-08-11"}),
            Action(
                name="CreatePlayerDevGoal",
                kwargs={
                    "dev_report_id": 12,
                    "player_id": 8,
                    "goal_text": "Increase contact rate on high fastballs",
                    "coach_id": 33,
                    "target_review_date": "2025-09-15",
                },
            ),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 5},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 2},
            ),
            Action(
                name="LogWorkflowRun",
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
            """
            You are completing a coach-facing post-game review for our home match. The upstream ingestion/QC is approved, and the match is finished.
Acceptance criteria (terminal database state):
• The game record for game_pk 2024000008 is verified as complete (Final) before any post-game materials are present.
• Precisely five pitch-execution evaluations are stored for this game with the following intent/actual quadrants and miss distances (inches):
  - pitch_id 29: intended down_away, actual down_middle, miss 2.4
  - pitch_id 33: intended up_in, actual middle_in, miss 6.8
  - pitch_id 46: intended down_away, actual down_away, miss 1.2
  - pitch_id 17: intended up_away, actual up_middle, miss 4.1
  - pitch_id 45: intended down_in, actual middle_in, miss 5.0
• A post-game scouting brief is available for game_pk 2024000008 with core narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.
• Four video playlists are appended to that brief: two titled Positive Reinforcement with 3 clips each, and two titled Teaching Moments with 2 clips each.
• The workflow ledger displays a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc == end_time_utc == 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.
No additional outputs are necessary.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: use the required key 'playlist_name'
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            As the analytics coordinator for Team 10, prepare a pre-series package for the upcoming scheduled game on or after 2024-07-23.

Acceptance criteria (single, deterministic terminal state):
1) Ensure there is precisely one scouting report for that game, featuring: report_type='Pre-Game', core_narrative_text='pre_series_policy_v1', gslides_link formatted by the canonical pattern 'https://slides.example.org/pre/{game_pk}', and s3_pdf_path following the canonical pattern 's3://reports/scouting/pre/{game_date}_g{game_pk}_team10_vs{opponent_team_id}.pdf'.
2) Attach exactly two curated insights to that report, both conforming to the template '{category}_{metric}_{bucket}' and permitted types: (player_id=1, insight_type='tendency', insight_text='tendency_chaserate_high', supporting_stat_value=0.412) and (player_id=4, insight_type='predictability', insight_text='predictability_firstpitchswing_low', supporting_stat_value=0.193).
3) Include exactly two video playlists with that report, having these specific properties: ('Positive Reinforcement', clip_count=5) and ('Teaching Moments', clip_count=3).
4) Record a single workflow run for this package with dag_name='pre_series_package', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://workflows/pre_series/{game_pk}.log'.
5) Execute trend filtering once for audit purposes with the policy thresholds min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.
Provide no additional output.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date": "2024-07-23"}),
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk": 2024000011, "team_id": 10}),

            # Persist policy-governed trend thresholds (EB+FDR gate recorded deterministically)
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),

            # Create the pre-game scouting report with canonical naming derived from resolved identifiers
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf"
            }),  # -> {"report_id": 13}

            # Attach the two curated insights (template-enforced text and allowed types)
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 1,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.412
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "predictability_firstpitchswing_low",
                "insight_type": "predictability",
                "supporting_stat_value": 0.193
            }),

            # Create the two standard playlists; links are provided by the system if omitted; clip counts are explicit per policy
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 5
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 3
            }),

            # Log the workflow run deterministically
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Provide a pre-game scouting packet for our club (team_id 10) focusing on the initial scheduled game happening on or post 2024-07-23. Determine success strictly by the presence of these final-state elements, without suggesting any specific process: • A pre-game report containing precisely the identifiers: narrative 'pre_game_series_context', slides URL https://docs.google.com/presentation/d/pre_game_series_context, and PDF s3://reports/scouting/pre_game/2024000011.pdf linked to the correct game. • Two curated insights included exactly: player 1 → 'tendency_firstpitch_low' with a value of 0.62; player 4 → 'execution_slider_away' having a value of 0.71. • One playlist titled 'Opponent Pitcher Tendencies' that includes 4 clips. • Pitch-location metadata depicted in the club's 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0), saved with the packet. • An individual activity record marked 'pre_game_scouting' at 2025-08-14T00:00:00Z with its log stored at s3://logs/workflows/pre_game_scouting/2025-08-14/run.json.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date": "2024-07-23", "team_id": 10}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000011}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000011,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_game_series_context",
                "gslides_link": "https://docs.google.com/presentation/d/pre_game_series_context",
                "s3_pdf_path": "s3://reports/scouting/pre_game/2024000011.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 1,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.62
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.71
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You handle the delivery of a post-game analytics packet for game 2024000008, evaluated solely by the final artifacts and metadata listed below (no specific method is suggested): • A post-game report with the narrative 'post_game_review' and links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf for the appropriate game. • Three execution grades precisely recorded as follows: pitch 29 intended 'down_away' vs actual 'down_middle' (miss 2.4 in); pitch 33 intended 'up_in' vs actual 'middle_in' (miss 6.8 in); pitch 46 intended 'down_away' vs actual 'down_away' (miss 1.2 in). • Two curated insights included verbatim: player 8 → 'situational_risp_success' 0.54; player 4 → 'execution_breakingball_high' 0.67. • Two coaching playlists called 'Positive Reinforcement' (5 clips) and 'Teaching Moments' (3 clips). • Pitch-location metadata preserved in the club's 12×12 catcher-view representation (x −1.5..1.5, z 1.0..4.0). • A strict >1.5 leverage roll-up available for the game. • One activity record identified as 'post_game_review' at 2025-08-14T00:00:00Z with its log at s3://logs/workflows/post_game_review/2025-08-14/run.json.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.67
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are responsible for managing Team 10's series build anchored to the first scheduled game on or after 2024-06-01. Ensure a single terminal state validated solely by the recorded content: the anchor game displays a single pre-game scouting packet which narrative is 'pre_series_policy_v1', with its slide deck located at https://slides.example.org/pre/2024000006, and its archived PDF at s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf; the opponent is noted and not more than two probables are listed for that opponent; a 12×12 strike-zone lattice for the anchor is maintained over a lateral span of −0.95 to 0.95 and a vertical span of 1.5 to 3.5; the trend review on file documents empirical-Bayes shrinkage with FDR control at thresholds of at least 50 pitches, 30 swings, and 25 batted balls (α=0.1); an ingestion log referring to the probables feed reports status 204 with zero records; and a successful pre-series run labeled pre_series_build appears for game 2024000006 with start and end timestamps of 2025-08-14T00:00:00Z and a log at s3://logs/pre_series/2024000006/2025-08-14.json.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date": "2024-06-01"}),
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk": 2024000006, "team_id": 10}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "probables_feed", "status_code": 204, "records_ingested": 0}),
            Action(name="ListProbablePitchers", kwargs={"team_id": 9, "limit": 2, "order_by": "full_name ASC"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "Pre-Game", "game_pk": 2024000006, "core_narrative_text": "pre_series_policy_v1", "gslides_link": "https://slides.example.org/pre/2024000006", "s3_pdf_path": "s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf"}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000006, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "pre_series_build", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/pre_series/2024000006/2025-08-14.json", "game_pk": 2024000006}),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_007",
        instruction=(
            """
            Deliver a pre-game scouting packet for our club (team_id 10) associated with the inaugural scheduled game on or following 2024-07-23. Your task is considered complete only if the database’s final state, for that game, includes exactly: • one pre-game report identified by narrative 'pre_game_series_context' including slide link https://docs.google.com/presentation/d/pre_game_series_context and PDF s3://reports/scouting/pre_game/2024000011.pdf; • two curated items registered as player 1 → 'tendency_firstpitch_low' with a value of 0.62 and player 4 → 'execution_slider_away' with a value of 0.71; • one playlist entitled 'Opponent Pitcher Tendencies' featuring 4 clips; • pitch-location data expressed in the club’s 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0); and • one activity record denoted 'pre_game_scouting' with start=end 2025-08-14T00:00:00Z located at s3://logs/workflows/pre_game_scouting/2025-08-14/run.json. The approach is at your discretion—only the desired final state is important.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date": "2024-07-23", "team_id": 10}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000011}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000011,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_game_series_context",
                "gslides_link": "https://docs.google.com/presentation/d/pre_game_series_context",
                "s3_pdf_path": "s3://reports/scouting/pre_game/2024000011.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 1,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.62
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.71
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Create an opponent series plan for game 2024000004 centered on our club (team_id 6). It will be accepted solely if the final database state for that contest includes: • one pre-game report with the narrative 'series_pitching_plan' and the following links: https://docs.google.com/presentation/d/series_pitching_plan and s3://reports/scouting/opponent_analysis/2024000004.pdf; • two curated items documented exactly as player 5 → 'tendency_firstpitch_low' (0.58) and player 7 → 'execution_slider_away' (0.73); • two playlists—'Opponent Pitcher Tendencies' (4 clips) and 'Baserunning Alerts' (3 clips); • pitch-location data stored in the club’s 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0); and • one activity record labeled 'series_pitching_plan' with start=end 2025-08-14T00:00:00Z located at s3://logs/workflows/series_pitching_plan/2025-08-14/run.json. No specific procedure is outlined.
            """
        ),
        actions=[
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk": 2024000004, "team_id": 6}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000004}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000004,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.58
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 7,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.73
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Baserunning Alerts", "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the delivery of a coach-visible in-game highlights package for game 2024000007. It is crucial that acceptance depends solely on achieving the following end state: the database must show exactly two high-impact moments visible to the coach at 2025-08-14T00:00:00Z (pitch 5, leverage 2.40, label 'HR_to_LF_spike'; pitch 6, leverage 2.74, label 'BasesLoaded_K'), along with one bench note 'mound_visit_recommendation' at leverage 0.00; all pitch-location data should adhere to the club's 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0); and there must be one activity record labeled 'in_game_highlights' where start=end 2025-08-14T00:00:00Z at s3://logs/workflows/in_game_highlights/2025-08-14/run.json. No specific method is required—only reaching this terminal state is needed.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000007}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000007,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateAutoBookmarkEvent", kwargs={
                "game_pk": 2024000007, "pitch_id": 5, "leverage_index": 2.40, "narration": "HR_to_LF_spike",
                "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True, "is_manual_alert": False
            }),
            Action(name="CreateAutoBookmarkEvent", kwargs={
                "game_pk": 2024000007, "pitch_id": 6, "leverage_index": 2.74, "narration": "BasesLoaded_K",
                "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True, "is_manual_alert": False
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000007, "suggestion_text": "mound_visit_recommendation", "leverage_index": 0.00,
                "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z", "coach_visible": True
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 15, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the delivery of a post-game analytics packet for game 2024000008. Acceptance is solely contingent upon the database including: one post-game report identified with the narrative 'post_game_review' containing links to https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf; exactly three execution grades specified as pitch 29 intended 'down_away' vs actual 'down_middle' (miss 2.4 in), pitch 33 aimed 'up_in' vs real 'middle_in' (miss 6.8 in), and pitch 46 expected 'down_away' vs actual 'down_away' (miss 1.2 in); two curated items duly noted as player 8 → 'situational_risp_success' (0.54) and player 4 → 'execution_breakingball_high' (0.67); two coaching playlists—'Positive Reinforcement' (5 clips) and 'Teaching Moments' (3 clips); pitch-location data must be formatted in the club’s 12×12 catcher-view convention (x −1.5..1.5, z 1.0..4.0); and one activity record that unambiguously encompasses dag_name 'post_game_review', game_pk 2024000008, status 'completed', start=end 2025-08-14T00:00:00Z, and log path s3://logs/workflows/post_game_review/2025-08-14/run.json. No specific process is required—achieving only this final state is necessary.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.67
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate a two-hitter post-game focus packet for game 2024000008. The packet is approved only if the database includes: one post-game report with 'two_hitter_focus' narrative and links https://docs.google.com/presentation/d/two_hitter_focus and s3://reports/scouting/post_game/2024000008_two_hitter_focus.pdf; four meticulously recorded items exactly as player 2 → 'situational_risp_success' (0.42) and 'execution_slider_away' (0.66), player 9 → 'tendency_firstpitch_low' (0.59) and 'execution_breakingball_high' (0.61); two coaching playlists—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips); pitch-location data displayed in the club’s 12×12 catcher-view format (x −1.5..1.5, z 1.0..4.0); and one activity record titled 'two_hitter_focus' with start=end 2025-08-14T00:00:00Z at s3://logs/workflows/two_hitter_focus/2025-08-14/run.json. Only the final state is relevant; no specific method is required.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "two_hitter_focus",
                "gslides_link": "https://docs.google.com/presentation/d/two_hitter_focus",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008_two_hitter_focus.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_success", "insight_type": "situational", "supporting_stat_value": 0.42
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "execution_slider_away", "insight_type": "execution", "supporting_stat_value": 0.66
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 9,
                "insight_text": "tendency_firstpitch_low", "insight_type": "tendency", "supporting_stat_value": 0.59
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 9,
                "insight_text": "execution_breakingball_high", "insight_type": "execution", "supporting_stat_value": 0.61
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle a single, policy-compliant post-game review for game_pk 2024000008 that concludes in one distinct final state. Acceptance conditions: the review is present with narrative tag 'umpire_exec_review_v1', slides https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; a trends QC pass applies empirical-Bayes shrinkage with an FDR control at 0.10 (min_pitches 50, min_swings 30, min_bbe 25); a catcher-view 12×12 strike-zone representation is computed for x∈[−0.95,0.95], z∈[1.5,3.5] (no persistence); two curated playlists are attached exactly as required: Positive Reinforcement (3 clips) and Teaching Moments (2 clips); a high-leverage summary employs threshold 1.5; and the run is documented as successful with start/end 2025-08-14T00:00:00Z and log s3://logs/post_game/2025-08-14_g2024000008.json. Provide no output.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": False
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "leverage_threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            As the analytics coordinator for Team 10, furnish a deterministic post-game package for game_pk=2024000007 once the games' status reaches 'Final'.

Acceptance criteria (single, deterministic terminal state):
1) Ensure there is one scouting report for that game containing: report_type='post-game', s3_pdf_path='s3://reports/scouting/post/2024-06-14_g2024000007_team10.pdf', gslides_link='https://slides.example.org/post/2024000007', core_narrative_text='post_game_policy_v1'.
2) Attach precisely two curated insights to that report: (player_id=2, insight_type='tendency', insight_text='tendency_chaserate_high', supporting_stat_value=0.412) and (player_id=11, insight_type='predictability', insight_text='predictability_firstpitchswing_low', supporting_stat_value=0.193). Follow the format '[category]_[metric]_[bucket]' in lowercase/digits only.
3) Ensure exactly two video playlists are available for that report: ('Positive Reinforcement', clip_count=5) and ('Teaching Moments', clip_count=3).
4) Canonicalize the pitch data, compute, and store a 12x12 catcher-view zone encoding with boundaries min_x=-0.95, max_x=0.95, min_z=1.5, max_z=3.5.
5) Derive a leverage summary for game_pk=2024000007 adhering to a strict threshold >1.5.
6) Capture a workflow run logged with status='success' under dag_name='post_game_pkg', start_time_utc='2025-08-14T11:00:00Z', end_time_utc='2025-08-14T11:09:00Z', log_s3_path='s3://ops/logs/post_game_pkg/2025-08-14_g2024000007.json'.

Note: Retain the s3_pdf_path as a fixed backfill artifact for audit reproducibility; avoid using the game_date to derive the date segment.

Adhere to relevant policies:
• Post-game reports necessitate games.game_status=='Final'.
• Always canonicalize raw pitch types prior to spatial encoding; establish 12x12 explicit bounds; apply persist=True on storage.
• Development playlists impose clip count: Positive Reinforcement ∈[3,5], Teaching Moments ∈[2,3].
• 'High leverage' adopts a strict >1.5 criterion.
Convey no additional values.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000007}),
            Action(name="CanonicalizePitchTypes", kwargs={"scope": "all"}),
            Action(name="GridEncodePitchLocations", kwargs={"min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000007, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000007", "s3_pdf_path": "s3://reports/scouting/post/2024-06-14_g2024000007_team10.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.412}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "predictability_firstpitchswing_low", "insight_type": "predictability", "supporting_stat_value": 0.193}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000007, "threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_pkg", "status": "success", "start_time_utc": "2025-08-14T11:00:00Z", "end_time_utc": "2025-08-14T11:09:00Z", "log_s3_path": "s3://ops/logs/post_game_pkg/2025-08-14_g2024000007.json", "game_pk": 2024000007})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_014",
        instruction=(
            """
            Prepare a singular pre-series scouting packet for game_pk 2024000011 leading to an undeniably determined final state, avoiding tool names. Acceptance criteria (goal-oriented, policy-guided, tool-agnostic): • Ensure the game context reflects a matchup Scheduled for 2024-07-23 (home_team_id=10 vs. away_team_id=8). • Log a data-ingestion checkpoint exactly as: source_name='probables_feed', status_code=200, records_ingested=2, ingested_at_utc='2025-08-14T00:00:00Z'. • Generate and store a catcher-view 12×12 strike-zone depiction for this game with dimensions x∈[−0.95,0.95], z∈[1.5,3.5] (no defaults hidden). • Execute Trends QC with empirical-Bayes shrinkage under FDR control at 0.10 with minimum values (min_pitches=50, min_swings=30, min_bbe=25). • One pre-game scouting document is present for the game containing core_narrative_text='pre_series_policy_v1', slide link https://slides.example.org/pre/2024000011, and PDF path s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf. • Incorporate a single curated insight linked to player_id=7 using insight_text='tendency_trendflags_fdr10', insight_type='tendency', and supporting_stat_value=0.1. • The process should be logged as status='success' under dag name 'pre_series_packet' with start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', log_s3_path='s3://logs/pre_series/2025-08-14_g2024000011.json', and associated to this game. Provide no outcomes.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000011}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000011,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_trendflags_fdr10",
                "insight_type": "tendency",
                "supporting_stat_value": 0.1
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the delivery of a single officiating and pitch-execution review post-game for game_pk 2024000008, resolving to one definitive final state without naming specific tools. Acceptance criteria (goal-oriented, policy-guided, tool-agnostic): • Game context reflects that the game is Final. • An officiating calibration entry exists for the plate umpire assigned to this game, specifically umpire_id=2 from the provided data, with zone_shift_x=−0.05, zone_shift_z=0.07, calibration_error_pct=2.3, and confidence_interval='90%'. • Pitch-execution evaluations exist for exactly three pitches in this game:   – pitch_id=28: intended=glove-side-high, actual=glove-side-high, miss_distance_inches=2.5;   – pitch_id=29: intended=arm-side-low,  actual=arm-side-mid,  miss_distance_inches=6.8;   – pitch_id=31: intended=down-middle,    actual=down-middle,    miss_distance_inches=1.9. • A catcher-view 12×12 strike-zone representation for this game is generated and persisted for x∈[−0.95,0.95], z∈[1.5,3.5]. • One post-game scouting document exists for this game with core_narrative_text='umpire_exec_review_v1', a slide link https://slides.example.org/post/2024000008, and a PDF path s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; this document is the one to which any media is attached. • Exactly two curated video playlists are attached to that same document using policy-compliant names and clip counts:   'Positive Reinforcement' with clip_count=3 and 'Teaching Moments' with clip_count=2. • A leverage summary for this game is computed using an explicit threshold of 1.5 (no hidden defaults). • The run is logged as status='success' under dag name 'post_game_review' with start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://logs/post_game/2025-08-14_g2024000008.json'. Return nothing.
            """
        ),
        actions=[
            # Confirm game is Final (policy gate)
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),

            # Record the plate-umpire calibration deterministically
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),

            # Three deterministic pitch-execution grades
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),

            # Persist the catcher-view 12x12 zone encoding for this game
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),

            # Create the post-game scouting document with deterministic content
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),

            # Attach policy-compliant curated playlists to the created report (first report_id in a clean reset is 13)
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),

            # Compute leverage summary with explicit threshold (no hidden default)
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),

            # Deterministic run log
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the completion of Monday player-development check-ins for the week of 2025-08-11 for players 11 and 12. Only the final state of the database should be evaluated, and it must show: one weekly development PDF per player at the specified paths (player 11 → s3://reports/player_dev/11/2025-08-11.pdf; player 12 → s3://reports/player_dev/12/2025-08-11.pdf); one Approved goal per player with target review date 2025-08-25 (player 11 → 'dev_goal_contact_quality' by coach 22; player 12 → 'dev_goal_zone_control' by coach 23); for game 2024000002, a development packet per player—player 11 narrative 'dev_weekly_packet_2025_08_11_p11' with links (slides https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11, PDF s3://reports/dev_packages/11/2025-08-11.pdf) and player 12 narrative 'dev_weekly_packet_2025_08_11_p12' with links (slides https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11, PDF s3://reports/dev_packages/12/2025-08-11.pdf); each packet contains exactly two playlists: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). A single workflow activity labeled 'weekly_dev_checkins' is recorded for game_pk 2024000002 with start=end 2025-08-14T00:00:00Z and log path s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json.
            """
        ),
        actions=[
            Action(name="CreatePlayerDevReport", kwargs={
                "player_id": 11,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/11/2025-08-11.pdf"
            }),
            Action(name="CreatePlayerDevReport", kwargs={
                "player_id": 12,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/12/2025-08-11.pdf"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 11,
                "player_id": 11,
                "goal_text": "dev_goal_contact_quality",
                "coach_id": 22,
                "target_review_date": "2025-08-25"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 12,
                "player_id": 12,
                "goal_text": "dev_goal_zone_control",
                "coach_id": 23,
                "target_review_date": "2025-08-25"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p11",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/11/2025-08-11.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p12",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/12/2025-08-11.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 14, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 14, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the completion of the post-game packet for game_pk 2024000008. Acceptance criteria (final database state): • The referenced game is in status 'Final'. • Pitch locations for this game are maintained in the standard catcher-view 12×12 grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0]. • Execution grading exists for exactly these five pitches with the stated fields: (29, intended down_away, actual down_middle, miss 2.4in), (33, intended up_in, actual middle_in, miss 6.8in), (46, intended down_away, actual down_away, miss 1.2in), (17, intended up_away, actual up_middle, miss 4.1in), (45, intended down_in, actual middle_in, miss 5.0in). • There is exactly one post-game scouting report linked to game_pk 2024000008 with narrative 'post_game_review' and links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf. • That report includes exactly two curated entries: situational_risp_high with value 0.54 for player 8, and execution_fastball_high with value 0.67 for player 4. • Two video playlists are available for the report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). • One workflow run is present for dag_name 'post_game_review' and game_pk 2024000008 with status 'success', start_time_utc == end_time_utc == '2025-08-13T00:00:00Z', and log path s3://workflow/logs/post_game_review/2024000008/2025-08-13.log. No additional output.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.67
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the assembly of the post-game analysis packet for game_pk 2024000008. Acceptance criteria (final database state): • The referenced game is 'Final'. • Pitch locations for this game are maintained in the catcher-view 12×12 grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0]. • Execution grading exists for exactly these three pitches with the stated fields: (29, intended down_away, actual down_middle, miss 2.4in), (33, intended up_in, actual middle_in, miss 6.8in), (46, intended down_away, actual down_away, miss 1.2in). • There is exactly one post-game report linked to game_pk 2024000008 with narrative 'post_game_review' and links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf. • That report features exactly two curated entries: situational_risp_high with value 0.54 for player 8, and execution_fastball_high with value 0.67 for player 4. • Two video playlists are included for the report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). • One workflow run is available for dag_name 'post_game_review' and game_pk 2024000008 with status 'success', start_time_utc == end_time_utc == '2025-08-13T00:00:00Z', and log path s3://workflow/logs/post_game_review/2024000008/2025-08-13.log. No other outputs are required.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.67
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            As the scouting lead for Team 10 in pre-series preparation, handle the creation of a spatially standardized opponent scouting package utilizing the next scheduled game on/after 2024-07-23. Acceptance requirements (definite terminal state based on outcomes):
• Selection of the game anchored at current_date '2024-07-23' should resolve to game_pk 2024000011 (Team 10 vs opponent_team_id 8).
• Ensure pitch data conform to the house pitch-type schema before any spatial encoding steps.
• Maintain the pitch-location grid representation at a 12×12 resolution within bounds min_x=-0.95, max_x=0.95, min_z=1.5, max_z=3.5, and save it back to pitch records.
• Prepare one pre-game scouting report for that game with details: report_type 'Pre-Game', s3_pdf_path 's3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf', gslides_link 'https://slides.example.org/pre/2024000011', and core_narrative_text 'pre_series_spatial_v1'.
• Attach exactly two curated insights with deterministic template strings: for player_id 2 → 'tendency_groundballrate_high' (type 'tendency', supporting_stat_value 0.531); for player_id 7 → 'situational_twooutswing_low' (type 'situational', supporting_stat_value 0.274).
• Generate two general playlists for the report named 'Opponent Heatmap Overview' and 'Zone Exploits Plan' with clip counts of 5 and 4, respectively.
• Verify that workflow metadata indicates a successful run for dag 'pre_series_spatial_pipeline', with start_time_utc and end_time_utc at '2025-08-14T00:00:00Z' and the log file path 's3://workflows/pre_series_spatial_pipeline/g2024000011/2025-08-14.json'.
Policy considerations: explicit date anchoring; canonicalization precedes spatial activities; fixed grid boundaries and deterministic contents; acceptance criteria should not prescribe API operations.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date":"2024-07-23"}),
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk":2024000011,"team_id":10}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk":2024000011}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk":2024000011,"min_x":-0.95,"max_x":0.95,"min_z":1.5,"max_z":3.5,"persist":True}),
            Action(name="CreateScoutingReport", kwargs={"report_type":"Pre-Game","game_pk":2024000011,"core_narrative_text":"pre_series_spatial_v1","gslides_link":"https://slides.example.org/pre/2024000011","s3_pdf_path":"s3://reports/scouting/pre/2024-07-23_g2024000011_team10_vs8.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id":13,"player_id":2,"insight_text":"tendency_groundballrate_high","insight_type":"tendency","supporting_stat_value":0.531}),
            Action(name="AddCuratedInsight", kwargs={"report_id":13,"player_id":7,"insight_text":"situational_twooutswing_low","insight_type":"situational","supporting_stat_value":0.274}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id":13,"playlist_name":"Opponent Heatmap Overview","clip_count":5}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id":13,"playlist_name":"Zone Exploits Plan","clip_count":4}),
            Action(name="LogWorkflowRun", kwargs={"dag_name":"pre_series_spatial_pipeline","game_pk":2024000011,"status":"success","start_time_utc":"2025-08-14T00:00:00Z","end_time_utc":"2025-08-14T00:00:00Z","log_s3_path":"s3://workflows/pre_series_spatial_pipeline/g2024000011/2025-08-14.json"})
        ],
        outputs=[]
    ),



    Task(
        annotator="saaish2",
        user_id="task_020",
        instruction=(
            """
            While assembling a pre-series opponent scouting packet, consider upstream ingestion as finalized.
Acceptance requirements (terminal state in the database):
• Target the packet for game_pk 2024000004, including a pre-game brief centered on series_pitching_plan with links: https://docs.google.com/presentation/d/series_pitching_plan and s3://reports/scouting/opponent_analysis/2024000004.pdf.
• To ensure proposal accuracy, ensure the pitch data for this game reflects: (i) harmonized pitch-type labels throughout the dataset and (ii) pitch locations discretized into a catcher-view 12×12 strike-zone grid within the bounds x∈[-1.5,1.5] and z∈[1.0,4.0], with cells encoded and preserved.
• Attach four curated insights to that brief using the specified key template with these values: situational_risp_high (0.50) for player_id 2; predictability_firstpitch_high (0.36) for player_id 4; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8.
• Attach two curated video playlists to that brief: Positive Reinforcement (3 clips) and Teaching Moments (2 clips).
• Confirm the workflow ledger notes a successful execution for this packet with start_time_utc == end_time_utc == 2025-08-18T00:00:00Z at s3://workflow/logs/pre_series_scouting_packet/2024000004/2025-08-18.log.
No further outputs are needed.
            """
        ),
        actions=[
            # Proposal realism/QC/modeling coverage (harmonization + grid encoding persisted)
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000004}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000004,
                "min_x": -1.5, "max_x": 1.5,
                "min_z": 1.0,  "max_z": 4.0,
                "persist": True
            }),
            # Pre-game brief
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            # Curated insights (policy-compliant keys)
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.50
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.36
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            # Playlists (correct arg key)
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            # Workflow record
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete the preparation of a concise post-game mini-review for our finished home game.
Acceptance criteria (final database state):
• The post-game brief is specified for game_pk 2024000008, featuring the main narrative post_game_review, and incorporates the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.
• The database contains three particular pitch-execution evaluations for this game, including pitch_ids 29, 33, and 46 with their intended/actual quadrants and miss distances (inches) as follows: (29, down_away → down_middle, 2.4), (33, up_in → middle_in, 6.8), (46, down_away → down_away, 1.2).
• To comply with the policy for post-game communication, two curated video playlists must accompany that brief: Positive Reinforcement (3 clips) and Teaching Moments (2 clips).
No additional outputs are required.
            """
        ),
        actions=[
            # Gate on the completed game context
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            # Three execution evaluations (deterministic, policy-compliant fields)
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            # Post-game brief
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: attach required curated playlists (correct key: playlist_name)
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_022",
        instruction=(
            """
            Handle the finalization of a coach-oriented post-game review for our home game. Assume the upstream ingestion/QC is pre-approved and the game has concluded.
Acceptance criteria (final database state):
• There exists a post-game scouting brief for game_pk 2024000008 containing the main narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.
• Execution evaluation is logged for exactly five pitches from this game with the following intended/actual quadrants and miss distances (inches):
  - pitch_id 29: intended down_away, actual down_middle, miss 2.4
  - pitch_id 33: intended up_in, actual middle_in, miss 6.8
  - pitch_id 46: intended down_away, actual down_away, miss 1.2
  - pitch_id 17: intended up_away, actual up_middle, miss 4.1
  - pitch_id 45: intended down_in, actual middle_in, miss 5.0
• Four curated insights should be attached to this brief using the necessary key template and values: 
  situational_risp_high (0.55) for player_id 8; predictability_firstpitch_high (0.31) for player_id 2; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8.
• Attach four video playlists to the brief: two bearing the name Positive Reinforcement with 3 clips each, and two named Teaching Moments with 2 clips each.
• The workflow ledger records a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc == end_time_utc == 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.
No additional outputs are required.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            # FIX: use the correct key 'playlist_name' (not 'name')
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Ensure that the database reflects a single, distinctly defined state for game_pk 2024000008 (concluded on 2024-03-05). Acceptance criteria (guided by policy, tool-neutral—state only the final configuration): • The designated plate-umpire for this evaluation is umpire_id=2, with exactly one calibration entry for this game recorded as zone_shift_x=-0.05, zone_shift_z=0.07, calibration_error_pct=2.3, and confidence_interval='90%'. • Three specific execution assessments must exist for this game with these details:   – pitch_id=28, intended='glove-side-high', actual='glove-side-high', miss_distance_inches=2.5;   – pitch_id=29, intended='arm-side-low', actual='arm-side-mid', miss_distance_inches=6.8;   – pitch_id=31, intended='down-middle', actual='down-middle', miss_distance_inches=1.9. • Compute a catcher-view 12×12 strike-zone mapping for x∈[-0.95,0.95], z∈[1.5,3.5], ensuring it is not stored. • Ensure a post-game scouting document for this game is available, featuring core_narrative_text='post_game_policy_v1', slide link https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf. • Associate exactly two specially crafted playlists with that document: 'Positive Reinforcement' with clip_count=4 and 'Teaching Moments' with clip_count=2. • A workflow run must be logged with status='success' under dag_name='post_game_exec_review', starting and ending at '2025-08-14T00:00:00Z', with log_s3_path='s3://logs/post_game/2025-08-14_g2024000008.json', linked to this game. Output nothing.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": False
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 4
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete a definitive player-development update. Establish a single, distinct terminal database state meeting all the acceptance criteria below without describing methodologies or naming tools:
• There exist exactly six development goals—two corresponding to development report 10 (player 11), another two for development report 6 (player 10), and two additional goals for the same report/player combinations—each entry marked with coach 501 and schedule the target review date for 2024-05-06.
• For dev_report_id 10 and player_id 11, include these goals:
  - raise_chase_swing_decisions_10pct
  - optimize_two_strike_approach
  - improve_line_drive_rate_5pct
• For dev_report_id 6 and player_id 10, include these goals:
  - improve_zone_coverage_inner_third
  - shorten_load_timing
  - improve_baserun_jump_reads
• All six goals must appear exactly once with a status of 'Approved'. No additional goals should be created or altered.
• A trends quality control pass is implemented using empirical-Bayes shrinkage with FDR control at 0.10 and minimums of 50 pitches, 30 swings, and 25 batted-ball events.
• Ensure the presence of one workflow run record with the dag name 'player_development_goals', marked as 'success', with start and end timestamps of 2024-05-06T00:00:00Z, and logging path 's3://logs/dev/2024-05-06_objectives.json'. Ensure no other records are altered.
            """
        ),
        actions=[
            # Create two initial goals (dev_report 10/player 11; dev_report 6/player 10)
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "raise_chase_swing_decisions_10pct", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "improve_zone_coverage_inner_third", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve the two initial goals (goal_ids are deterministic in this snapshot)
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),

            # Create two additional goals for the same report/player pairs (dependent on prior approvals' dev_report_id/player_id values)
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "optimize_two_strike_approach", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "shorten_load_timing", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve those two goals
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 22}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 23}),

            # Create a third goal for each same report/player pair
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 10, "player_id": 11, "goal_text": "improve_line_drive_rate_5pct", "coach_id": 501, "target_review_date": "2024-05-06"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 6, "player_id": 10, "goal_text": "improve_baserun_jump_reads", "coach_id": 501, "target_review_date": "2024-05-06"}),

            # Approve the final two goals
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 24}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 25}),

            # Trends QC (EB shrinkage, FDR 0.10, with required minima)
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "use_eb_shrinkage": True, "control": "FDR"}),

            # Workflow bookkeeping
            Action(name="LogWorkflowRun", kwargs={"dag_name": "player_development_goals", "status": "success", "start_time_utc": "2024-05-06T00:00:00Z", "end_time_utc": "2024-05-06T00:00:00Z", "log_s3_path": "s3://logs/dev/2024-05-06_objectives.json"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_025",
        instruction=(
            """
            Your task is to create a single, uniquely determined post-game calling and execution memo for game_pk 2024000008. Acceptance criteria (final-state only, no procedure): • The review concentrates on plate-umpire umpire_id=2 and the database includes exactly one calibration entry for this game with zone_shift_x=-0.04, zone_shift_z=0.05, calibration_error_pct=1.8, confidence_interval='90%'. • There are exactly two execution assessments for this game: – pitch_id=14 with intended='arm-side-high', actual='arm-side-high', miss_distance_inches=2.2; – pitch_id=15 with intended='glove-side-low', actual='glove-side-mid', miss_distance_inches=5.6. • A catcher-view 12×12 zone mapping for x∈[-0.95,0.95], z∈[1.5,3.5] is maintained. • Precisely one post-game memo document is present with core_narrative_text='post_game_calling_review_v1', slide link https://slides.example.org/post/2024000008_calling, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_calling.pdf. • Exactly two curated playlists are linked to that document: 'Positive Reinforcement' with clip_count=3 and 'Teaching Moments' with clip_count=3. • Exactly one workflow run is recorded with dag_name='post_game_calling_memo', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', log_s3_path='s3://logs/post_game/2025-08-14_g2024000008_calling.json', related to this game. Do not return anything.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.04,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.8,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 14,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-high",
                "actual_quadrant": "arm-side-high",
                "miss_distance_inches": 2.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 15,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-low",
                "actual_quadrant": "glove-side-mid",
                "miss_distance_inches": 5.6
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_calling_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008_calling",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_calling.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            In your role, you are to publish a post-game addendum for a finished contest. Provide a single, uniquely determined terminal database state meeting all the following acceptance criteria without detailing steps or naming tools:
• The game reviewed is game_pk 2024000008 and it is a finished contest (Final).
• Ensure there is a single ingest record for this run containing: source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-03-05T00:00:00Z'.
• Trend anomalies are sorted using a false-discovery rate of 0.10 incorporating empirical-Bayes shrinkage and minimums of 50 pitches, 30 swings, and 25 batted-ball events.
• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is created using bounds x∈[-0.95, 0.95] and z∈[1.5, 3.5] and is stored.
• Include a single Post-Game scouting report for game_pk 2024000008 with:
  - core narrative text: post_game_policy_v1
  - slide link: https://slides.example.org/post/2024000008
  - PDF path: s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf
• Two curated insights are incorporated into the report for player_id 7 using deterministic, policy-compliant values:
  - insight_text: predictability_firstpitchstrike_high, insight_type: predictability, supporting_stat_value: 0.68
  - insight_text: situational_rispcontact_high, insight_type: situational, supporting_stat_value: 0.29
• Precisely two curated video playlists are attached to the same report:
  - 'Positive Reinforcement' with 3 clips
  - 'Teaching Moments' with 2 clips
• Record a leverage summary for game_pk 2024000008 employing a leverage threshold of 1.5.
• Note a workflow bookkeeping record with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.
No other records may be created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.29
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Your task is to complete an integrated post-game analysis packet for game_pk 2024000008, ensuring a uniquely determined database condition. Acceptance criteria (outcome-only, tool-neutral): • The review focuses on plate umpire umpire_id=2 and the database contains exactly one calibration entry for this game with zone_shift_x=-0.03, zone_shift_z=0.06, calibration_error_pct=2.1, confidence_interval='90%'. • Precisely three execution assessments are recorded for this game with these specifications:   – pitch_id=28, intended='glove-side-high', actual='glove-side-high', miss_distance_inches=2.5;   – pitch_id=29, intended='arm-side-low', actual='arm-side-mid', miss_distance_inches=6.8;   – pitch_id=31, intended='down-middle', actual='down-middle', miss_distance_inches=1.9. • A catcher-view 12×12 zone mapping for x∈[-0.95,0.95], z∈[1.5,3.5] is maintained. • Exactly one post-game document is available with core_narrative_text='post_game_integrated_v1', slide link https://slides.example.org/post/2024000008_integrated, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_integrated.pdf. • Exactly two curated insights are attached to that document:   – player_id=9 with insight_text='situational_rispcontact_low', insight_type='situational', supporting_stat_value=0.24;   – player_id=7 with insight_text='execution_edgehit_high', insight_type='execution', supporting_stat_value=0.78. • Exactly two curated playlists are linked to that document: 'Positive Reinforcement' with clip_count=5 and 'Teaching Moments' with clip_count=2. • Exactly one workflow run is recorded with dag_name='post_game_integrated', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', and log_s3_path='s3://logs/post_game/2025-08-14_g2024000008_integrated.json', connected to this game. Return nothing.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 2.1,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_integrated_v1",
                "gslides_link": "https://slides.example.org/post/2024000008_integrated",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_integrated.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 9,
                "insight_text": "situational_rispcontact_low",
                "insight_type": "situational",
                "supporting_stat_value": 0.24
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "execution_edgehit_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.78
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 5
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Your responsibility is to complete a post-game analytics packet for a concluded game. Ensure a single, uniquely defined final database state meeting all these acceptance criteria without outlining procedures or specifying tools:
• The game being evaluated is game_pk 2024000008 and it is a concluded contest (Final).
• The catcher-view 12×12 strike-zone mapping for game_pk 2024000008 is created using bounds x∈[-0.95, 0.95] and z∈[1.5, 3.5] and remains stored.
• One Post-Game scouting report is available for game_pk 2024000008 with:
  - core narrative text: post_game_policy_v1
  - slide link: https://slides.example.org/post/2024000008
  - PDF path: s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf
• A leverage summary for game_pk 2024000008 is documented using a leverage threshold of 1.5.
• Two curated insights are included in the report for player_id 7 using deterministic, policy-compliant values:
  - insight_text: tendency_chaserate_high, insight_type: tendency, supporting_stat_value: 0.31
  - insight_text: predictability_firstpitchstrike_high, insight_type: predictability, supporting_stat_value: 0.68
• Exactly two curated video playlists are associated with this report:
  - "Positive Reinforcement" with 3 clips
  - "Teaching Moments" with 2 clips
• A lone workflow bookkeeping entry is created with dag name 'post_game_review', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008.json'.
No other records are created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the preparation of an opponent plan for game 2024000004. Ensure a single pre-game scouting dossier is published for this game and provide back the report_id.

Acceptance criteria (goal-oriented, non-procedural):
• The upstream preparation must be documented in the database for this game: pitch classifications need to be canonicalized, and there should be a persisted 12×12 catcher-view zone encoding existing with x∈[-1.5,1.5] and z∈[1.0,4.0].
• Utilize the narrative label 'series_pitching_plan' for the dossier and incorporate the precise artifacts: Google Slides at 'https://docs.google.com/presentation/d/series_pitching_plan' and PDF at 's3://reports/scouting/opponent_analysis/2024000004.pdf'.
• There are exactly four curated insights attached with these specific keys, subjects, and values: situational_risp_high for player_id 2 at 0.52; predictability_firstpitch_high for player_id 4 at 0.36; execution_fastball_high for player_id 4 at 0.61; execution_slider_low for player_id 8 at 0.58.
• Two reference video playlists must be linked to the dossier, both having fixed titles and number of clips: 'Pre-Game Examples' (3 clips) and 'Pre-Game Risks' (3 clips).
• Record the completion of the planning workflow under the process 'opponent_analysis', marking the unchanged times start=end='2025-08-18T00:00:00Z', log path 's3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log', and explicitly link it to game_pk 2024000004.
• Provide only the report_id.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000004}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000004}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000004, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "core_narrative_text": "series_pitching_plan", "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan", "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.58}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Pre-Game Examples", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Pre-Game Risks", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "opponent_analysis", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log", "game_pk": 2024000004})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_030",
        instruction=(
            """
            Handle the creation of a post-game dossier that adheres to policy for game 2024000008.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is strictly one finalized post-game scouting dossier for this game, reflecting the organization's standard values:
  — narrative label: post_game_review
  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review
  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf
• Confirm that execution evaluations and curated insights in the dossier align with rules.py gating and thresholds, and that all pitch types mentioned in insight keys employ canonical pitch codes (e.g., FF, SL) instead of informal names.
• The dossier's curated video support must strictly use the policy-required playlist set designated for post-game dossiers — "Positive Reinforcement" and "Teaching Moments" — each comprising three clips and tied to the same report.
• Log the conclusion of the post-game process, capturing the immutable UTC times (start 2025-08-18T00:00:00Z, end 2025-08-18T00:20:00Z), along with a fixed S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.
• Return the identifier of the completed post-game dossier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),

            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away", "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),

            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),

            # Curated insights using canonical pitch codes (FF, SL)
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high", "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high", "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_sl_low", "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),

            # Policy-mandated playlists
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),

            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are tasked with delivering a post-game correction and reinforcement pack for game 2024000008. Submit one report and send back the report_id.

Acceptance criteria (goal-oriented, non-procedural):
• The release depends on the game being Final; use the narrative 'post_game_review' with artifacts 'https://docs.google.com/presentation/d/post_game_review' and 's3://reports/scouting/post_game/2024000008.pdf'.
• Maintain a 12×12 catcher-view zone map for this game with x∈[-1.5,1.5], z∈[1.0,4.0].
• Grading of execution involves the five-pitch benchmark set: 29 down_away→down_middle (2.4), 33 up_in→middle_in (6.8), 46 down_away→down_away (1.2), 17 up_away→up_middle (4.1), 45 down_in→middle_in (5.0).
• Attach four curated insights: situational_risp_high (player_id 8, 0.55), predictability_firstpitch_high (player_id 2, 0.31), execution_fastball_high (player_id 4, 0.60), execution_slider_low (player_id 8, 0.56).
• Link four playlists (3 clips each): 'Positive Reinforcement', 'Corrective Work', 'Two-Strike Wins', 'Leave-It Misses'.
• Ensure a workflow completion entry exists for 'post_game_review' with start=end='2025-08-18T00:00:00Z', log path 's3://workflow/logs/post_game_review/2024000008/2025-08-18.log', and link to game_pk 2024000008.
• Deliver only the report_id.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.31}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Corrective Work", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Two-Strike Wins", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Leave-It Misses", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_032",
        instruction=(
            """
            Your role involves creating a pre-/in-series targeting dossier for game 2024000004. Submit a single dossier and provide the report_id.

Acceptance criteria (goal-oriented, non-procedural):
• The dossier is set to pre-game with the narrative 'series_pitching_plan' and specified artifacts 'https://docs.google.com/presentation/d/series_pitching_plan' and 's3://reports/scouting/opponent_analysis/2024000004.pdf'.
• Link four playlists (3 clips each): 'Pre-Game Examples', 'Pre-Game Risks', 'Left/Right Keys', 'Hot Zones'.
• Exactly six curated insights must be attached: situational_risp_high (player_id 2, 0.52), predictability_firstpitch_high (player_id 4, 0.36), execution_fastball_high (player_id 4, 0.61), execution_slider_low (player_id 8, 0.58), situational_risp_high (player_id 8, 0.55), predictability_firstpitch_high (player_id 2, 0.31).
• Confirm a planning workflow completion for 'opponent_analysis' with start=end='2025-08-18T00:00:00Z', log path 's3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log', and association with game_pk 2024000004.
• Submit only the report_id.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000004}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "core_narrative_text": "series_pitching_plan", "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan", "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Pre-Game Examples", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Pre-Game Risks", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Left/Right Keys", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Hot Zones", "clip_count": 3, "report_id": 13}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_fastball_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_slider_low", "insight_type": "execution", "supporting_stat_value": 0.58}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.31}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "opponent_analysis", "status": "success", "start_time_utc": "2025-08-18T00:00:00Z", "end_time_utc": "2025-08-18T00:00:00Z", "log_s3_path": "s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log", "game_pk": 2024000004})
        ],
        outputs=[13]
    ),




    Task(
        annotator="saaish2",
        user_id="task_033",
        instruction=(
            """
            Complete and finalize your review of umpire and execution related to a past game. Provide an exclusive database state that meets each of the following acceptance standards without detailing procedures or mentioning any APIs:
• The game being evaluated is game_pk 2024000008, designated as a finalized match.
• A specific umpire calibration entry is available for the home plate duty with these attributes: umpire_id 2, zone_shift_x -0.05, zone_shift_z 0.07, calibration_error_pct 2.3, confidence_interval '90%'.
• Precisely two pitch-level execution evaluations are documented for game_pk 2024000008:
  - pitch_id 28: intended quadrant 'glove-side-high', actual quadrant 'glove-side-high', miss_distance_inches 2.5
  - pitch_id 29: intended quadrant 'arm-side-low',  actual quadrant 'arm-side-mid',  miss_distance_inches 6.8
• Generate and retain the 12×12 strike-zone mapping from the catcher's perspective for game_pk 2024000008, with specified limits x∈[-0.95,0.95], z∈[1.5,3.5].
• There exists a singular Post-Game scouting document for game_pk 2024000008 containing core content 'post_game_policy_v1', a slide URL 'https://slides.example.org/post/2024000008', and a PDF file path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.
• This document includes one specially selected insight for player_id 7 described by: insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31.
• Attach two distinct video playlists to this document: 'Positive Reinforcement' consisting of 3 clips, and 'Teaching Moments' containing 2 clips.
• Record a leverage summary for game_pk 2024000008 using a 1.5 threshold.
• Draft a workflow record with the following details, dag name 'post_game_umpire_exec', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_umpire_exec.json'.
Do not create or alter any additional records.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Organize a scouting packet for the commencement of a series. Supply a single exclusive database state fulfilling the entire set of acceptance criteria below without outlining procedures or citing any APIs:
• The primary matchup is game_pk 2024000011, listed as an upcoming game.
• Include precisely two ingest records for this process:
  - source_name 'probables_feed', status_code 200, records_ingested 2, ingested_at_utc '2024-07-23T00:00:00Z'
  - source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-07-23T00:00:00Z'
• Screen trend anomalies using a false-discovery rate of 0.10, with empirical-Bayes shrinkage, and minimums of 50 pitches, 30 swings, and 25 batted-ball events.
• Generate the 12×12 catcher-view strike-zone mapping for game_pk 2024000011, adhering to bounds x∈[-0.95,0.95], z∈[1.5,3.5], and ensure it is saved.
• There is one Pre-Game scouting report for game_pk 2024000011, featuring primary narrative content 'pre_series_policy_v1', a slide link 'https://slides.example.org/pre/2024000011', and a PDF path 's3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf'.
• This report holds exactly two tailored insights for player_id 7:
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.68
  - insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31
• Attach precisely two tailored video playlists: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• Log a leverage summary for game_pk 2024000011 using a threshold of 1.5.
• Identify and internally utilize the opponent for team_id 10 in this game, keeping details within internal processes (no output required).
• Compose a workflow record with these attributes: dag name 'pre_series_packet', game_pk 2024000011, status 'success', start_time_utc '2024-07-23T00:00:00Z', end_time_utc '2024-07-23T00:00:00Z', and log path 's3://logs/pre/2024-07-23_g2024000011_packet.json'.
Do not produce or change any other records.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000011}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2024-07-23T00:00:00Z"
            }),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-07-23T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000011,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.68
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000011, "threshold": 1.5}),
            Action(name="GetOpponentForTeamInGame", kwargs={"team_id": 10, "game_pk": 2024000011}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Generate a single, uniquely determined terminal database state for a finished game utilizing the fixed IDs, bounds, threshold, names, and file paths specified here—without listing steps or naming any APIs. Acceptance criteria:
• Exactly one Post-Game scouting report is present for game_pk 2024000008 featuring core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.
• The catcher-view 12×12 strike-zone mapping is stored for this game using x∈[-0.95,0.95], z∈[1.5,3.5] and a 12×12 grid.
• A leverage summary for game_pk 2024000008 is documented using a threshold of 1.5; the resultant counts are whatever the system canonically computes from the existing play-by-play under that threshold.
• A workflow bookkeeping record is entered with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.
No other records are created or modified.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Execute a dual-track update where post-game insights guide actionable development objectives. Fulfill a single, uniquely determined terminal database state that meets all of the following acceptance criteria without listing steps or naming any APIs:
• Post-game context: game_pk 2024000008 is a completed contest; one Post-Game report exists for this game featuring core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.
• The catcher-view 12×12 strike-zone mapping for this game is generated with bounds x∈[-0.95,0.95], z∈[1.5,3.5] and preserved; leverage summary documented with threshold 1.5.
• The report includes exactly two curated insights: for player_id 7 ('situational_rispcontact_high', type 'situational', value 0.29) and for player_id 11 ('predictability_firstpitchstrike_high', type 'predictability', value 0.66).
• Development track: establish and approve two development goals with deterministic details:
  - dev_report_id 10, player_id 11, goal_text 'raise_chaserate_decisions_10pct', coach_id 501, target_review_date '2024-05-06'
  - dev_report_id 6,  player_id 10, goal_text 'improve_zone_coverage_inner_third', coach_id 501, target_review_date '2024-05-06'
• Attach exactly two curated video playlists to the Post-Game report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• A single ingest record is present for this run with: source_name 'statcast_daily', status_code 200, records_ingested 5000, ingested_at_utc '2024-03-05T00:00:00Z'.
• Enter a workflow bookkeeping record with dag name 'post_game_to_dev_bridge', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_to_dev.json'.
No other records are created or modified.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.29
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 5000,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 10,
                "player_id": 11,
                "goal_text": "raise_chaserate_decisions_10pct",
                "coach_id": 501,
                "target_review_date": "2024-05-06"
            }),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 6,
                "player_id": 10,
                "goal_text": "improve_zone_coverage_inner_third",
                "coach_id": 501,
                "target_review_date": "2024-05-06"
            }),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Ensure the creation of a compliant, comprehensive post-game review emphasizing calibration, execution, mapping, and curation. Submit one uniquely defined terminal database state that meets all the specified acceptance criteria, avoiding any step-by-step explanation or API naming:
• The reviewed game corresponds to game_pk 2024000003 and is a completed contest.
• There exists precisely one ingest record with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.
• Establish a per-game umpire calibration record with: umpire_id 2, zone_shift_x -0.03, zone_shift_z 0.06, calibration_error_pct 1.9, confidence_interval '90%'.
• Generate and persist the catcher-view 12×12 strike-zone mapping for game_pk 2024000003 with bounds x∈[-0.95,0.95], z∈[1.5,3.5].
• There is a sole Post-Game scouting report for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.
• The report integrates exactly two curated insights for player_id 10: 'tendency_chaserate_high' (type 'tendency', value 0.30) and 'predictability_firstpitchstrike_high' (type 'predictability', value 0.65).
• Indicate that precisely two curated video playlists are included: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• Record a leverage summary for game_pk 2024000003 using threshold 1.5.
• Log a workflow bookkeeping record with dag name 'post_game_curation', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_curation.json'.
No additional records should be created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000003,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 10,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.30
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 10,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.65
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Convey an opponent analysis consistent with a completed matchup (game 2024000008), articulated solely as outcome criteria. The conclusive state demonstrates standardized pitch labels specific to the game; 12×12 catcher-view encoding (x −1.5..1.5, z 1.0..4.0) maintained; an opponent-analysis report employing 'series_pitching_plan' with links https://docs.google.com/presentation/d/series_pitching_plan and s3://reports/scouting/opponent_analysis/2024000008.pdf; two predefined insights (player 5: 'tendency_chaserate_high' 0.18; player 14: 'predictability_changeup_high' 0.64); two coaching playlists ('Positive Reinforcement' 3 clips; 'Teaching Moments' 2 clips); verification that both insights as well as both playlists are present; and a workflow record marked 'opponent_analysis_series' on 2025-08-14T00:00:00Z filed at s3://logs/workflows/opponent_analysis_series/2025-08-14/run.json.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "opponent-analysis",
                "game_pk": 2024000008,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.18
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 14,
                "insight_text": "predictability_changeup_high", "insight_type": "predictability", "supporting_stat_value": 0.64
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="ListCuratedInsights", kwargs={"report_id": 13}),
            Action(name="ListVideoPlaylists", kwargs={"report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Draft a complete post-game review package for game 2024000008 that aligns with policy and saves all derived materials.

Acceptance criteria (goal-oriented, non-procedural):
• There must be precisely one finalized post-game scouting dossier that adheres to the organization's standard values:
  — narrative label: post_game_review
  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review
  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf
• Pitch-type labels must be standardized, and strike-zone spatial features should be preserved using the org's standard 12×12 catcher-view grid with limits x∈[-1.5,1.5], z∈[1.0,4.0].
• Execution evaluations are to refer to the game's official five-pitch sample with fixed quadrant targets and miss distances as recorded in the dataset; do not infer or recompute.
• Curated insights must pass rules.py checks, merge similar points, and are organized by supporting_stat_value DESC followed by player_id ASC, utilizing canonical keys.
• Curated video support includes only the policy-required playlist set — "Positive Reinforcement" and "Teaching Moments" — each containing three clips and linked to the dossier.
• Document the completion of the post-game process workflow with fixed UTC times (start 2025-08-18T00:00:00Z, end 2025-08-18T00:30:00Z) and a pre-defined S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.
• Provide the identifier of the completed post-game dossier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicates and sort by supporting_stat_value DESC then player_id ASC
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Put together an extensive pre-series scouting packet for game 2024000004 that ensures standardized pitch labels, maintains spatial features, and captures opposing team's tendencies.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is exactly one finalized pre-game scouting dossier using the organization's standard values:
  — narrative label: series_pitching_plan
  — Google Slides artifact: https://docs.google.com/presentation/d/series_pitching_plan
  — PDF artifact: s3://reports/scouting/opponent_analysis/2024000004.pdf
• Canonical pitch-type labels, and strike-zone spatial features must be retained using the org's standard 12×12 catcher-view grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0].
• Curated insights need to fulfill rules.py criteria, compress redundant points, and be ranked by supporting_stat_value DESC then player_id ASC, utilizing canonical keys across themes of situational, predictability, execution, and tendency.
• Register the completion of the pre-series process workflow with static UTC times (start 2025-08-18T11:00:00Z, end 2025-08-18T11:30:00Z) and a predetermined S3 log path: s3://workflow/logs/opponent_analysis/2024000004/2025-08-18.log.
• Supply the identifier of the finalized pre-game dossier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000004}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000004}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000004, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-game",
                "game_pk": 2024000004,
                "core_narrative_text": "series_pitching_plan",
                "gslides_link": "https://docs.google.com/presentation/d/series_pitching_plan",
                "s3_pdf_path": "s3://reports/scouting/opponent_analysis/2024000004.pdf"
            }),
            # FIX: collapse duplicate 'situational_risp_high' and sort DESC by supporting_stat_value then player_id ASC
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_high", "insight_type": "tendency", "supporting_stat_value": 0.45}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.35}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Carry out the delivery of a detailed post-game scouting dossier for game 2024000008, ensuring the standardization of pitch labels, realization of spatial features, acquisition of insights compliant with policy, and inclusion of the necessary video support.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is precisely one completed post-game scouting dossier using the organization's standard values:
  — narrative label: post_game_review
  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review
  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf
• Confirm all nomenclature and spatial features conform to policy (12×12 catcher-view grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0]).
• Execution evaluations must employ the game's canonical five-pitch sample with fixed quadrant targets and miss distances as recorded; do not infer or recalibrate.
• Curated insights must pass rules.py gates, eliminate redundant bullets, and be arranged by supporting_stat_value DESC, then player_id ASC, using standard keys.
• Curated video support utilizes exactly the policy-mandated playlist set — "Positive Reinforcement" and "Teaching Moments" — ensuring each has three clips linked to the dossier.
• Record the workflow completion with fixed UTC timestamps (start 2025-08-18T01:10:00Z, end 2025-08-18T01:40:00Z) and a pre-determined S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.
• Provide the identifier of the finalized post-game dossier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicate insights and enforce deterministic ordering (DESC by value, then player_id ASC)
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the assembly of a streamlined pre-series scouting packet, resulting in a uniquely established terminal database state that fulfills all listed conditions without detailing steps or identifying any APIs:
• The game being reviewed is game_pk 2024000011, yet to be played (scheduled).
• Collection provenance presents one ingestion record for this run including: source_name 'probables_feed', status_code 200, records_ingested 2, ingested_at_utc '2025-08-14T00:00:00Z'.
• Trends must be filtered using a false-discovery rate of 0.10 with empirical-Bayes shrinkage and minimal counts of 50 pitches, 30 swings, and 25 batted-ball events.
• Ensure a single Pre-Game scouting report exists for game_pk 2024000011 with core narrative text 'pre_series_policy_v1', slide link 'https://slides.example.org/pre/2024000011', and PDF path 's3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf'.
• That report should contain exactly four curated insights for player_id 7, ordered by supporting_stat_value DESC:
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.61
  - insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.50
  - insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.36
  - insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.22
• Workflow bookkeeping records must indicate: dag name 'pre_series_packet', game_pk 2024000011, status 'success', start_time_utc '2024-07-23T00:00:00Z', end_time_utc '2024-07-23T00:00:00Z', and log path 's3://logs/pre/2024-07-23_g2024000011_packet.json'.
No other records should be created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000011}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "probables_feed",
                "status_code": 200,
                "records_ingested": 2,
                "ingested_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Pre-Game",
                "game_pk": 2024000011,
                "core_narrative_text": "pre_series_policy_v1",
                "gslides_link": "https://slides.example.org/pre/2024000011",
                "s3_pdf_path": "s3://reports/scouting/pre/2024-07-23_g2024000011_pre.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.50
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.36
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.22
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete the creation of a succinct post-game addition. Ensure a singular, uniquely defined terminal database condition that meets all of the following acceptance criteria without enumerating steps or naming any APIs:
• The game in question is game_pk 2024000008, and it is finalized.
• Generate the catcher-view 12×12 strike-zone mapping for game_pk 2024000008 using bounds x∈[-0.95,0.95], z∈[1.5,3.5], with grid dimensions 12×12, and save it.
• One Post-Game scouting report must exist for game_pk 2024000008 featuring core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.
• The report includes two curated insights solely for player_id 7:
  - insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.66
• Attach exactly two curated video playlists to that report: 'Positive Reinforcement' with 3 clips and 'Teaching Moments' with 2 clips.
• Record a leverage summary for game_pk 2024000008 utilizing a threshold of 1.5.
• Log a workflow bookkeeping entry with dag name 'post_game_addendum', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_addendum.json'.
Avoid creating or modifying any additional records.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete a post-game model and execution QC packet. Ensure a single, uniquely defined terminal database state that adheres to all the following acceptance criteria without listing steps or naming any APIs:
• The reviewed game is game_pk 2024000008, which is a concluded contest.
• There is an ingest record for this run with: source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'.
• Filter trend anomalies using a false-discovery rate of 0.10 with empirical-Bayes shrinkage and a minimum of 50 pitches, 30 swings, and 25 batted-ball events.
• An umpire calibration record per game exists with: umpire_id 2, zone_shift_x -0.05, zone_shift_z 0.07, calibration_error_pct 2.3, confidence_interval '90%'.
• Document exactly three pitch execution assessments for game_pk 2024000008:
  - pitch_id 28 intended 'glove-side-high' matched actual 'glove-side-high' with miss_distance_inches 2.5
  - pitch_id 29 intended 'arm-side-low' landed 'arm-side-mid' with miss_distance_inches 6.8
  - pitch_id 31 intended 'down-middle' matched actual 'down-middle' with miss_distance_inches 1.9
• Produce and preserve the catcher-view 12×12 strike-zone mapping for game_pk 2024000008 using bounds x∈[-0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12.
• A solitary Post-Game scouting report exists for game_pk 2024000008 containing core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'.
• The report presents two curated insights for player_id 7, ordered by supporting_stat_value DESC:
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.66
  - insight_text 'tendency_chaserate_high', insight_type 'tendency', supporting_stat_value 0.31
• Attach exactly two curated video playlists to the report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• Record a leverage summary for game_pk 2024000008, utilizing a threshold of 1.5.
• Register a workflow bookkeeping entry with dag name 'post_game_model_exec_qc', game_pk 2024000008, status 'success', start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_qc.json'.
Refrain from creating or changing any other records.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.05,
                "zone_shift_z": 0.07,
                "calibration_error_pct": 2.3,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered by supporting_stat_value DESC per policy
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "tendency_chaserate_high",
                "insight_type": "tendency",
                "supporting_stat_value": 0.31
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Finalize a comprehensive post-game scouting and QC packet. Ensure a single, uniquely determined terminal database state that adheres to all these acceptance criteria, without detailing steps or naming any APIs:
• The game under review is game_pk 2024000003 and it is a completed contest.
• One ingest record for this run exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.
• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.
• The catcher-view 12×12 strike-zone mapping for game_pk 2024000003 is generated using bounds x∈[-0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.
• A single Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.
• The report contains exactly three curated insights for player_id 11, ordered by supporting_stat_value DESC:
  - insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30
  - insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.19
• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5.
• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'.
No other records are created or modified.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            # Insights in DESC order by supporting_stat_value per policy
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Assemble a thorough post-game analytics packet. Make sure a single, uniquely determined terminal database state meets all of these acceptance criteria without enumerating steps or naming any APIs:
• The game under review is game_pk 2024000003 and it is a completed contest.
• Two player development goals already exist for the relevant development report and must remain unchanged in this run; do not create, approve, or modify any development goals.
• One ingest record for this run exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'.
• Trend anomalies are filtered using false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events.
• The catcher-view strike-zone mapping for game_pk 2024000003 is generated using bounds x∈[-0.95,0.95], z∈[1.5,3.5], grid dimensions 12×12, and is persisted.
• A single Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'.
• The report contains exactly three curated insights for player_id 11, ordered by supporting_stat_value DESC:
  - insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34
  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30
  - insight_text 'execution_zonerate_low', insight_type 'execution', supporting_stat_value 0.19
• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips.
• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5.
• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'.
No other records are created or modified.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            # Curated insights in strict DESC order by supporting_stat_value
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the preparation of a policy-compliant post-game dossier for game 2024000008.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is a single finalized post-game dossier for this game that includes: narrative label post_game_review, Google Slides https://docs.google.com/presentation/d/post_game_review, and PDF s3://reports/scouting/post_game/2024000008.pdf.
• Maintain any strike-zone feature engineering by persisting a 12×12 catcher-view grid using preset bounds x∈[-1.5,1.5], z∈[1.0,4.0].
• Display trends only following EB shrinkage with FDR control using these thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10; ensure acceptance by applying these thresholds (or stricter).
• Attach curated insights to the dossier that utilize canonical insight_text keys, are unique (without duplicates), and are organized by supporting_stat_value DESC and then player_id ASC.
• Include exactly two policy-mandated video playlists in the dossier: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Log workflow completion with fixed UTC timestamps (start 2025-08-18T18:00:00Z, end 2025-08-18T18:20:00Z) and record log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log.
• Provide the dossier identifier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Curated insights (unique, sorted by value DESC then player_id ASC)
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            # Playlists (policy-mandated names)
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:00:00Z", "end_time_utc": "2025-08-18T18:20:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_048",
        instruction=(
            """
            Handle the delivery of a post-game improvement packet for game 2024000008.

Acceptance criteria (goal-oriented, non-procedural):
• Confirm a finalized dossier exists that includes: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.
• Preserve strike-zone features using a 12×12 catcher-view grid with the specified bounds x∈[-1.5,1.5], z∈[1.0,4.0], if applicable.
• Apply EB shrinkage with FDR control for trend surfacing using these thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.
• Make sure curated insights are canonical, non-duplicative, sorted by supporting_stat_value DESC and then player_id ASC, and included in the dossier.
• Attach only the policy-mandated video playlists: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Document workflow completion with fixed times (start 2025-08-18T18:25:00Z, end 2025-08-18T18:45:00Z) and record the log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log.
• Return the dossier identifier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Curated insights (unique, sorted)
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.51}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.35}),
            # Playlists
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:25:00Z", "end_time_utc": "2025-08-18T18:45:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),

    Task(
        annotator="saaish2",
        user_id="task_049",
        instruction=(
            """
            Create a comprehensive, policy-compliant post-game review packet for game 2024000008.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is exactly one finalized dossier with: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.
• Maintain a 12×12 catcher-view grid within bounds x∈[-1.5,1.5], z∈[1.0,4.0].
• Document execution evaluations for these five specified pitches (deterministic specification):
  (29: intended=down_away, actual=down_middle, miss_in=2.4), (33: intended=up_in, actual=middle_in, miss_in=6.8),
  (46: intended=down_away, actual=down_away, miss_in=1.2), (17: intended=up_away, actual=up_middle, miss_in=4.1),
  (45: intended=down_in, actual=middle_in, miss_in=5.0).
• Reveal trends only after applying EB shrinkage with FDR control using these thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.
• Include exactly six curated insights using canonical keys, without duplicates, ordered by supporting_stat_value DESC then player_id ASC with these tuples (player_id, key, value):
  (4, execution_ff_high, 0.66), (8, execution_sl_low, 0.60), (8, situational_risp_high, 0.58), (2, predictability_firstpitch_high, 0.49), (2, execution_ch_low, 0.43), (4, predictability_sequencing_low, 0.41).
• Include only the policy-mandated video playlists: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Log workflow completion with fixed UTC times (start 2025-08-18T18:30:00Z, end 2025-08-18T18:55:00Z) and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log.
• Provide the dossier identifier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review", "gslides_link": "https://docs.google.com/presentation/d/post_game_review", "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf", "draft_status": "published"}),
            # Six insights (unique, sorted)
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.66}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.58}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.49}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ch_low", "insight_type": "execution", "supporting_stat_value": 0.43}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_sequencing_low", "insight_type": "predictability", "supporting_stat_value": 0.41}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_review", "status": "success", "start_time_utc": "2025-08-18T18:30:00Z", "end_time_utc": "2025-08-18T18:55:00Z", "log_s3_path": "s3://workflow/logs/post_game_review/2024000008/2025-08-18-2.log", "game_pk": 2024000008})
        ],
        outputs=[13]
    ),



    Task(
        annotator="saaish2",
        user_id="task_050",
        instruction=(
            """
            Develop an end-to-end post-game briefing for game 2024000008 with deterministic execution grading and ranked insights.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure a finalized dossier exists with: narrative post_game_review; Google Slides https://docs.google.com/presentation/d/post_game_review; PDF s3://reports/scouting/post_game/2024000008.pdf.
• Preserve 12×12 catcher-view grid features within bounds x∈[-1.5,1.5], z∈[1.0,4.0].
• Log execution evaluations for these specific five pitches (id, intended→actual, miss_in): 29 (down_away→down_middle, 2.4), 33 (up_in→middle_in, 6.8), 46 (down_away→down_away, 1.2), 17 (up_away→up_middle, 4.1), 45 (down_in→middle_in, 5.0).
• Before attaching insights, apply EB shrinkage with FDR control thresholds: min_pitches=50, min_swings=30, min_bbe=25, FDR q=0.10.
• Include six canonical, non-duplicative insights sorted by supporting_stat_value DESC then player_id ASC with these tuples: (2, execution_ff_high, 0.67), (4, execution_sl_low, 0.61), (8, situational_risp_high, 0.59), (2, predictability_firstpitch_high, 0.48), (4, execution_ch_low, 0.45), (8, predictability_sequencing_low, 0.41).
• Include only the policy-mandated playlists: "Positive Reinforcement" (3) and "Teaching Moments" (3).
• Document workflow completion with fixed UTC times (start 2025-08-18T20:00:00Z, end 2025-08-18T20:25:00Z) and path s3://workflow/logs/post_game_review/2024000008/2025-08-18-5.log.
• Provide the dossier identifier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            # Explicit audit log entry for draft_status transition (fix from judge)
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "scouting_reports",
                "status_code": 200,
                "records_ingested": 1,
                "timestamp_utc": "2025-08-18T20:25:00Z",
                "message": "report_published report_id=13 draft_status=published",
                "game_pk": 2024000008
            }),
            # Insights in required order and canonicalized
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.67}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.59}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.48}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ch_low", "insight_type": "execution", "supporting_stat_value": 0.45}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_sequencing_low", "insight_type": "predictability", "supporting_stat_value": 0.41}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are finalizing a post-game dossier for game_pk 2024000003 (a completed contest). "
            "Deliver a single, uniquely determined terminal database state that satisfies all of the following acceptance criteria without listing steps or naming any APIs: "
            "• Exactly one ingestion record exists with: source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'. "
            "• Trend anomalies have been screened using false-discovery rate q=0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events. "
            "• One Post-Game scouting report exists for game_pk 2024000003 with core narrative text 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'. "
            "• The report contains exactly two curated insights for player_id 11, ordered by supporting_stat_value descending: "
            "  - insight_text 'situational_rispcontact_high', insight_type 'situational', supporting_stat_value 0.34 "
            "  - insight_text 'predictability_firstpitchstrike_high', insight_type 'predictability', supporting_stat_value 0.30 "
            "• Exactly two curated video playlists are attached to the same report: 'Positive Reinforcement' with 3 clips, and 'Teaching Moments' with 2 clips. "
            "• A leverage summary for game_pk 2024000003 is recorded using a threshold of 1.5. "
            "• A workflow bookkeeping record is written with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. "
            "No other records are created or modified.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Create a single, policy-compliant post-game analyst packet for game_pk 2024000008 that leads to a uniquely established state. Acceptance criteria include: calibrated officiating for umpire_id 2 with x shift −0.02, z shift 0.05, 1.9% error, 90% interval; execution assessments for pitch_id 28 (glove-side-high→glove-side-high, 2.5 in miss) and pitch_id 31 (down-middle→down-middle, 1.9 in miss); a 12×12 zone artifact for x∈[−0.95,0.95], z∈[1.5,3.5] is maintained; a post-game packet is available with narrative 'umpire_exec_review_v1', slides https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf; the packet includes exactly two curated playlists as specified: Positive Reinforcement (3 clips) and Teaching Moments (2 clips); and the run is logged as successful with start/end 2025-08-14T00:00:00Z and log s3://logs/post_game/2025-08-14_g2024000008.json. Do not return any output.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000008,
                "umpire_id": 2,
                "zone_shift_x": -0.02,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28, "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31, "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95, "max_x": 0.95,
                "min_z": 1.5,  "max_z": 3.5,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "umpire_exec_review_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_umpire_exec.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Prepare a policy-compliant post-game report for game_pk 2024000008 (a concluded event). Your goal is to ensure the database achieves a single, uniquely determined terminal state reflecting one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); trend screening has been executed using a false-discovery rate q=0.10 with empirical-Bayes shrinkage and minimums of 50 pitches, 30 swings, and 25 batted-ball events; there is precisely one Post-Game scouting report for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; the report includes exactly two curated insights for player_id 7 with supporting values 0.31 for 'situational_rispcontact_high' (type 'situational') and 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'), and it is linked with two curated video playlists titled 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); a leverage summary is available for game_pk 2024000008 using threshold 1.5; and workflow bookkeeping notes a successful execution under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. Avoid listing steps or naming any APIs. No other records are created or changed.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Compile a comprehensive post-game analytics report. In the final state, the database shows a completed match for game_pk 2024000003; there is exactly one ingest record (source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'); trend anomalies have been filtered using a false-discovery rate of 0.10 with empirical-Bayes shrinkage and minimums of 50 pitches, 30 swings, and 25 batted-ball events; a per-game umpire calibration is recorded with umpire_id 2, zone_shift_x −0.03, zone_shift_z 0.06, calibration_error_pct 1.9, confidence_interval '90%'; three pitch-execution assessments exist for the game with (pitch_id 28, intended 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5), (pitch_id 29, intended 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8), and (pitch_id 31, intended 'down-middle', actual 'down-middle', miss_distance_inches 1.9); a catcher-view strike-zone mapping is retained for game_pk 2024000003 using bounds x∈[−0.95,0.95], z∈[1.5,3.5] with 12×12 grid dimensions; one Post-Game scouting report is available for this game with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'; the report features exactly three curated insights for player_id 11 arranged by supporting_stat_value DESC (situational_rispcontact_high 0.34; predictability_firstpitchstrike_high 0.30; execution_zonerate_low 0.19) and precisely two curated video playlists ('Positive Reinforcement' with 3 clips and 'Teaching Moments' with 2 clips); a leverage summary exists for game_pk 2024000003 using threshold 1.5; and a workflow record is present with dag name 'post_game_full_review', game_pk 2024000003, status 'success', start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. No other records are created or changed.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000003,
                "umpire_id": 2,
                "zone_shift_x": -0.03,
                "zone_shift_z": 0.06,
                "calibration_error_pct": 1.9,
                "confidence_interval": "90%"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000003,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000003,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000003,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "execution_zonerate_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.19
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Ensure the delivery of a single, uniquely defined terminal database state that meets all the following acceptance criteria, without detailing steps or referencing any APIs: 
• The subject game is game_pk 2024000008, denoted as a completed contest (Final).
• Persist two player development goals, each ending in the 'Approved' status:
  - For dev_report_id 10 associated with player_id 11, with goal_text 'raise_chase_swing_decisions_10pct', coach_id 501, and target_review_date '2024-03-06'.
  - For dev_report_id 6 associated with player_id 10, with goal_text 'improve_zone_coverage_inner_third', coach_id 501, and target_review_date '2024-03-06'.
• Employ false-discovery rate 0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events for filtering trend anomalies; the name of the resulting flags table is 'trend_flags_p50_s30_b25_fdr0.1'.
• For the same game_pk, record exactly three pitch execution assessments with these specified values:
  - pitch_id 28, intended_quadrant_model 'glove-side-high', actual_quadrant 'glove-side-high', miss_distance_inches 2.5.
  - pitch_id 29, intended_quadrant_model 'arm-side-low', actual_quadrant 'arm-side-mid', miss_distance_inches 6.8.
  - pitch_id 31, intended_quadrant_model 'down-middle', actual_quadrant 'down-middle', miss_distance_inches 1.9.
• Generate and persist the 12×12 strike-zone mapping from the catcher's perspective for game_pk 2024000008, utilizing bounds x∈[-0.95,0.95], z∈[1.5,3.5], with dimensions cells_x=12 and cells_z=12.
• Record a leverage summary for game_pk 2024000008 using a threshold of 1.5.
• Draft a workflow bookkeeping record under the dag name 'post_game_dev_alignment' with game_pk 2024000008, marked status 'success', with start_time_utc '2024-03-05T00:00:00Z', and end_time_utc '2024-03-05T00:00:00Z', recording log path 's3://logs/post/2024-03-05_g2024000008_dev_alignment.json'.
No other records should be established or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 10,
                "player_id": 11,
                "goal_text": "raise_chase_swing_decisions_10pct",
                "coach_id": 501,
                "target_review_date": "2024-03-06"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 6,
                "player_id": 10,
                "goal_text": "improve_zone_coverage_inner_third",
                "coach_id": 501,
                "target_review_date": "2024-03-06"
            }),
            # Approve the two goals created above (IDs are deterministic in this snapshot: 20, 21)
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "cells_x": 12,
                "cells_z": 12,
                "persist": True
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Prepare a policy-compliant post-game dossier for game_pk 2024000008, representing a completed competition. Your aim is to ensure the database remains in a singular, uniquely resolved terminal state where the system includes one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); initiate trend screening using false-discovery rate q=0.10 with empirical-Bayes shrinkage and minima of 50 pitches, 30 swings, and 25 batted-ball events. Ensure exactly one Post-Game scouting report is available for game_pk 2024000008, featuring the core narrative 'post_game_policy_v1', a slide link 'https://slides.example.org/post/2024000008', and a PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'. The report must contain precisely two curated insights for player_id 7 with supporting values: 0.31 for 'situational_rispcontact_high' (type 'situational') and 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'), and link to two curated video playlists named 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips). A leverage summary should exist for game_pk 2024000008 using a 1.5 threshold. Workflow bookkeeping should document a successful execution under the dag name 'post_game_full_review' for game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. Refrain from listing steps or referencing any APIs. Ensure no other records are created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Craft a policy-compliant post-game dossier for a concluded contest. Ensure the database achieves a single, well-defined final state, adhering strictly to these acceptance criteria, without enumerating steps or mentioning any APIs: the game under analysis is game_pk 2024000008 and it is finalized; the system displays a successful statcast data ingestion (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); employ trend screening using empirical-Bayes shrinkage with FDR q=0.10 and minimum of 50 pitches, 30 swings, and 25 batted-ball events; there is a solitary Post-Game scouting report for game_pk 2024000008 labeled with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; ensconce in the document exactly two curated insights for player_id 7, with supporting values in descending order: supporting_stat_value 0.31 for 'situational_rispcontact_high' (type 'situational') followed by 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'); the report is linked to playlists 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); establish a leverage summary for game_pk 2024000008 with a threshold of 1.5; and record a successful workflow run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and record log path 's3://logs/post/2024-03-05_g2024000008_full.json'. No other records are created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the assembly of a post-game review dossier for game 2024000008.

Your task is to present a completed dossier and audit trail that fulfill all the following outcomes (non-procedural, acceptance-only):
• The dossier is published featuring the narrative label 'post_game_review', the Google Slides URL https://docs.google.com/presentation/d/post_game_review, and a PDF located at s3://reports/scouting/post_game/2024000008.pdf.
• The pitch-location appendix includes a 12×12 catcher-view grid covering horizontal -1.5 to 1.5 feet and vertical 1.0 to 4.0 feet, ensuring these encodings are maintained.
• Integrate trend flags into the dossier derived from EB-shrunk estimates under FDR q=0.10 with minimum samples of 50 pitches, 30 swings, and 25 batted balls.
• The curated insight list contains precisely three canonical, non-duplicative bullets ordered by supporting_stat_value (DESC) then player_id (ASC): (player 4, execution_ff_high, 0.60), (player 8, situational_risp_high, 0.55), (player 2, predictability_firstpitch_high, 0.31).
• Include exactly two curated video playlists titled 'Positive Reinforcement' and 'Teaching Moments', each with three clips.
• A publication audit record appears as a manual alert named 'publication_audit' with frozen timestamp 2025-08-18T18:20:00Z and message 'report_published report_id=13 draft_status=published' (the suggestion text aligns with the message).
• The workflow execution is documented as 'success' with start 2025-08-18T18:05:00Z, end 2025-08-18T18:20:00Z, and logs preserved at s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5,
                "max_x": 1.5,
                "min_z": 1.0,
                "max_z": 4.0,
                "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "use_eb_shrinkage": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_ff_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are developing a comprehensive post-game dossier that integrates trend vetting for game 2024000008.

Outcomes for acceptance only:
• A dossier is published with the label 'post_game_review', and available at Slides https://docs.google.com/presentation/d/post_game_review, PDF s3://reports/scouting/post_game/2024000008.pdf.
• A 12×12 catcher-view grid is maintained over -1.5..1.5 ft (x) and 1.0..4.0 ft (z).
• Trend flags are generated using EB shrinkage with FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted balls; only these trends are referenced in insights.
• There are precisely four curated insights, non-repetitive and organized by supporting_stat_value DESC then player_id ASC: (player 4, execution_ff_high, 0.61), (player 3, tendency_chase_high, 0.58), (player 8, situational_risp_high, 0.55), (player 2, predictability_firstpitch_low, 0.34).
• Two playlists are created: 'Positive Reinforcement' and 'Teaching Moments', with each containing exactly three clips linked to the dossier.
• A publication audit is manually flagged with 'publication_audit' as an alert at 2025-08-18T18:20:00Z, including the message 'report_published report_id=13 draft_status=published' (suggestion text matches) and identified as manual.
• The workflow run is logged as successful from 2025-08-18T18:05:00Z to 2025-08-18T18:20:00Z with logs s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 3, "insight_text": "tendency_chase_high", "insight_type": "tendency", "supporting_stat_value": 0.58
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_low", "insight_type": "predictability", "supporting_stat_value": 0.34
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are organizing the definitive post-game review packet for a concluded match. Your goal is to ensure the database reaches a singular, uniquely determined final state that satisfies these acceptance criteria (avoid listing steps or naming any APIs): the reviewed game is game_pk 2024000003 and it has concluded; the system shows one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 4200, ingested_at_utc '2024-07-22T00:00:00Z'); trend screening is conducted via empirical-Bayes shrinkage with FDR q=0.10 and minimums of 50 pitches, 30 swings, and 25 batted-ball events; there is exactly one Post-Game scouting report for game_pk 2024000003 with the core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000003', and PDF path 's3://reports/scouting/post/2024-07-22_g2024000003_post.pdf'; the report includes precisely two curated insights for player_id 11 sorted by supporting value descending: supporting_stat_value 0.34 for 'situational_rispcontact_high' (type 'situational') followed by 0.30 for 'predictability_firstpitchstrike_high' (type 'predictability'); the report associates with playlists 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); a leverage summary is documented for game_pk 2024000003 with threshold 1.5; and workflow records indicate a successful execution under the dag name 'post_game_full_review' with game_pk 2024000003, start_time_utc '2024-07-22T00:00:00Z', end_time_utc '2024-07-22T00:00:00Z', and log path 's3://logs/post/2024-07-22_g2024000003_full.json'. No additional records are created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 4200,
                "ingested_at_utc": "2024-07-22T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000003,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the delivery of a comprehensive post-game analytic package for a completed contest. Aim to configure the database to a single, uniquely determined final state that meets all the following acceptance criteria (avoid listing steps or naming any APIs): the game under review is game_pk 2024000008 and it is final; there is one successful statcast ingestion (source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z'); apply trend screening with empirical-Bayes shrinkage, FDR q=0.10, and a minimum of 50 pitches, 30 swings, and 25 batted-ball events; ensure there is exactly one Post-Game scouting report for game_pk 2024000008 with core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; the report includes four curated insights, ranked by supporting value in descending order: supporting_stat_value 0.66 for player_id 11 'predictability_firstpitchstrike_high' (type 'predictability'); then 0.61 for player_id 7 'predictability_firstpitchstrike_high' (type 'predictability'); then 0.34 for player_id 11 'situational_rispcontact_high' (type 'situational'); and finally 0.30 for player_id 7 'situational_rispcontact_high' (type 'situational'); attach two curated video playlists to the same report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); record pitch execution assessments for three pitches in the same game: pitch_id 28 assessed as intended_quadrant 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5; pitch_id 29 assessed as intended_quadrant 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8; pitch_id 31 assessed as intended_quadrant 'down-middle', actual 'down-middle', miss_distance_inches 1.9; maintain a leverage summary for game_pk 2024000008 with a threshold of 1.5; and ensure workflow bookkeeping records a successful run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. No additional records should be created or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered by supporting_stat_value DESC across all entries
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Coordinate the creation of a post-game execution and first-pitch predictability dossier for game 2024000008 intended for internal use.

Acceptance outcomes (deterministic end-state):
• Ensure there is a published scouting dossier for this game using the organization's standard narrative label ('post_game_review'), slide deck link (https://docs.google.com/presentation/d/post_game_review), and PDF location (s3://reports/scouting/post_game/2024000008.pdf).
• The appendix must include the organization's catcher-view 12×12 strike-zone location grid, extended over x ∈ [-1.5, 1.5] ft and z ∈ [1.0, 4.0] ft.
• Trends cited in the dossier should be vetted in accordance with policy using empirical-Bayes shrinkage, FDR q=0.10, and minimums of 50 pitches, 30 swings, and 25 batted balls.
• Curated insights should avoid redundant directives; specifically, if a first-pitch predictability signal is present, it must appear exactly once as 'predictability_firstpitchstrike_high'.
• Ensure existence of two video playlists attached to the dossier named 'Positive Reinforcement' and 'Teaching Moments', each containing three clips.
• Document a manual publication audit at 2025-08-18T18:20:00Z, capturing the dossier’s published state for this report.
• Record the workflow run as 'success' for the fixed interval 2025-08-18T18:05:00Z→2025-08-18T18:20:00Z with logs at s3://workflow/logs/post_game_review/2024000008/2025-08-18-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -1.5,
                "max_x": 1.5,
                "min_z": 1.0,
                "max_z": 4.0,
                "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "use_eb_shrinkage": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-18T18:20:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            # Curated insights — ensure NO duplicates of 'predictability_firstpitchstrike_high'
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 8,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.57
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 4,
                "insight_text": "execution_ff_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 3,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.52
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments",
                "clip_count": 3,
                "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete the creation of a policy-compliant post-game deliverable for the finished contest. Ensure the database reaches a uniquely determined final state that adheres to the acceptance criteria: the game being reviewed is game_pk 2024000008 and should be final; there are two successful ingestions from the same game day: one with source_name 'statcast_daily', status_code 200, records_ingested 3600, ingested_at_utc '2024-03-05T00:00:00Z', and another from source_name 'spraychart_feed', status_code 200, records_ingested 180, ingested_at_utc '2024-03-05T00:00:00Z'; apply trend screening with empirical-Bayes shrinkage method at FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted-ball events; ensure exactly one Post-Game scouting report for game_pk 2024000008 with the core narrative 'post_game_policy_v1', slide link 'https://slides.example.org/post/2024000008', and PDF path 's3://reports/scouting/post/2024-03-05_g2024000008_post.pdf'; the report should include exactly four curated insights ordered by descending supporting value: supporting_stat_value 0.66 for player_id 11 'predictability_firstpitchstrike_high' (type 'predictability'); then 0.61 for player_id 7 'predictability_firstpitchstrike_high' (type 'predictability'); then 0.34 for player_id 11 'situational_rispcontact_high' (type 'situational'); and then 0.30 for player_id 7 'situational_rispcontact_high' (type 'situational'); attach two curated video playlists to the same report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); record pitch execution assessments for three pitches with these values: pitch_id 28 (intended 'glove-side-high', actual 'glove-side-high', miss_distance_inches 2.5), pitch_id 29 (intended 'arm-side-low', actual 'arm-side-mid', miss_distance_inches 6.8), pitch_id 31 (intended 'down-middle', actual 'down-middle', miss_distance_inches 1.9); store a leverage summary for game_pk 2024000008 with threshold 1.5; and log a successful workflow run under dag name 'post_game_full_review' with game_pk 2024000008, start_time_utc '2024-03-05T00:00:00Z', end_time_utc '2024-03-05T00:00:00Z', and log path 's3://logs/post/2024-03-05_g2024000008_full.json'. Ensure no other records are generated or altered.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "statcast_daily",
                "status_code": 200,
                "records_ingested": 3600,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "spraychart_feed",
                "status_code": 200,
                "records_ingested": 180,
                "ingested_at_utc": "2024-03-05T00:00:00Z"
            }),
            Action(name="FilterTrends", kwargs={
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.1,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000008",
                "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf"
            }),
            # Insights ordered DESC
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.66
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitchstrike_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "situational_rispcontact_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.30
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 28,
                "game_pk": 2024000008,
                "intended_quadrant_model": "glove-side-high",
                "actual_quadrant": "glove-side-high",
                "miss_distance_inches": 2.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29,
                "game_pk": 2024000008,
                "intended_quadrant_model": "arm-side-low",
                "actual_quadrant": "arm-side-mid",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 31,
                "game_pk": 2024000008,
                "intended_quadrant_model": "down-middle",
                "actual_quadrant": "down-middle",
                "miss_distance_inches": 1.9
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008,
                "threshold": 1.5
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Craft a brief post-game quicklook dossier for game 2024000008 targeting the pitching team.

Required outcomes for completion:
• Ensure a published dossier is available for this game with the organization label 'post_game_quicklook_v1', which includes a slide deck at https://docs.google.com/presentation/d/post_game_quicklook_v1 and a PDF at s3://reports/scouting/post_game_quicklook_v1/2024000008.pdf.
• Include a 12×12 location grid for catcher-view over x∈[-1.5,1.5] ft and z∈[1.0,4.0] ft.
• Apply trend validation using empirical-Bayes shrinkage with an FDR q=0.10 and minima of 50 pitches, 30 swings, and 25 batted balls.
• Attach precisely two unique curated insights to the dossier while following the organization's code format, ensuring there is no duplication.
• Associate one video playlist with the dossier, titled 'Quick Hits' containing 3 clips.
• Conduct a manual publication audit logged at 2025-08-20T17:20:00Z; ensure the publication message is recorded as both the audit message and the operator note for this alert.
• Log a successful workflow run for 2025-08-20T17:05:00Z–2025-08-20T17:20:00Z with files at s3://workflow/logs/post_game_quicklook_v1/2024000008/2025-08-20-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
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
                name="FilterTrends",
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
                name="CreateScoutingReport",
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
                name="CreateManualAlertEvent",
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
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.60,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.57,
                },
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={
                    "playlist_name": "Quick Hits",
                    "clip_count": 3,
                    "report_id": 13,
                },
            ),
            Action(
                name="LogWorkflowRun",
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
            """
            Develop a teaching-focused post-game dossier for game 2024000008 aimed at enhancing player skills. Transition the system to the specified terminal state without detailing the specific steps.

Acceptance criteria (must be fulfilled at the end):
• A published dossier labeled 'post_game_teachpack_v1' should be present, including a slide link https://docs.google.com/presentation/d/post_game_teachpack_v1 and PDF s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf.
• Retain a persisted catcher-view 12×12 grid over x∈[-1.5,1.5] ft and z∈[1.0,4.0] ft.
• Use empirical-Bayes shrinkage for trend vetting with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.
• Ensure four unique curated insights (no repetition) with valid codes are included in the dossier.
• Two video playlists should be associated with the dossier: 'Reinforce Strengths' (3 clips) and 'Adjustments' (3 clips).
• Conduct a manual publication audit at 2025-08-20T21:10:00Z with the publication message saved verbatim as the operator note.
• Document the workflow run as successful from 2025-08-20T20:55:00Z to 2025-08-20T21:10:00Z with the log file located at s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
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
                name="FilterTrends",
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
                name="CreateScoutingReport",
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
                name="CreateManualAlertEvent",
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
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.62,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.34,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.56,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.53,
                },
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Reinforce Strengths", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Adjustments", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="LogWorkflowRun",
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
            """
            Complete an end-to-end post-game leverage dossier for game 2024000008 intended for the big-league coaching staff. Progress to the specified terminal outcome without providing a step-by-step execution.

End-state acceptance (deterministic):
• There must be a published dossier labeled 'post_game_leverage_v1' with a slide link https://docs.google.com/presentation/d/post_game_leverage_v1 and PDF s3://reports/scouting/post_game_leverage_v1/2024000008.pdf.
• Ensure inclusion of a persisted catcher-view 12×12 grid over x∈[-1.5,1.5] ft and z∈[1.0,4.0] ft.
• Focus analysis scope on high-leverage scenarios only (leverage_index>1.5); leverage should be aggregated at a threshold of 1.5, applying empirical-Bayes shrinkage for trend vetting with FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.
• Incorporate six unique curated insights (no redundancy) using valid codes into the dossier and associate them with relevant players.
• Ensure three playlists tied to the dossier: 'Positive Reinforcement' (3 clips), 'Teaching Moments' (3 clips), and 'Leverage Review' (3 clips).
• Facilitate a manual publication audit at 2025-08-20T22:25:00Z, recording the publication message verbatim as the operator note.
• Record the workflow run as successful from 2025-08-20T22:10:00Z to 2025-08-20T22:25:00Z with logs stored at s3://workflow/logs/post_game_leverage_v1/2024000008/2025-08-20-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
                kwargs={
                    "game_pk": 2024000008,
                    "min_x": -1.5,
                    "max_x": 1.5,
                    "min_z": 1.0,
                    "max_z": 4.0,
                    "persist": True,
                },
            ),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(
                name="FilterTrends",
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
                name="CreateScoutingReport",
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
                name="CreateManualAlertEvent",
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
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.61,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.58,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.55,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.33,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 6,
                    "insight_text": "stamina_b2b_low",
                    "insight_type": "stamina",
                    "supporting_stat_value": 0.40,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 7,
                    "insight_text": "predictability_sequencing_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.59,
                },
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Leverage Review", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="LogWorkflowRun",
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
            """
            Handle the creation of a post-game platoon and predictability dossier for game 2024000008 as part of the series planning. Focus exclusively on delivering the final facts; omit any discussion of steps.

Acceptance outcomes (deterministic end-state):
• A published dossier labeled 'post_game_platoon_pred_v1' is available with slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1 and PDF at s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf.
• Include a persisted catcher-view 12×12 grid spanning x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Apply trend vetting with empirical-Bayes shrinkage, employing FDR q=0.10 and minima: 50 pitches, 30 swings, 25 batted balls.
• Attach six distinct curated insights to the dossier, ensuring no duplication and using valid codes.
• Maintain three playlists associated with the dossier: 'Platoon Review' (3 clips), 'Sequencing Notes' (3 clips), and 'Execution Focus' (3 clips).
• A manual audit for publication at 2025-08-21T00:45:00Z is required; capture the publication message verbatim and set this as suggestion_text.
• Confirm a successful workflow run for the duration 2025-08-21T00:30:00Z→2025-08-21T00:45:00Z, with logs located at s3://workflow/logs/post_game_platoon_pred_v1/2024000008/2025-08-21-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
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
                name="FilterTrends",
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
                name="CreateScoutingReport",
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
                name="CreateManualAlertEvent",
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
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 4,
                    "insight_text": "execution_ff_high",
                    "insight_type": "execution",
                    "supporting_stat_value": 0.63,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 8,
                    "insight_text": "predictability_firstpitchstrike_high",
                    "insight_type": "predictability",
                    "supporting_stat_value": 0.57,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 3,
                    "insight_text": "situational_risp_high",
                    "insight_type": "situational",
                    "supporting_stat_value": 0.52,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 5,
                    "insight_text": "tendency_chase_low",
                    "insight_type": "tendency",
                    "supporting_stat_value": 0.35,
                },
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={
                    "report_id": 13,
                    "player_id": 6,
                    "insight_text": "stamina_b2b_low",
                    "insight_type": "stamina",
                    "supporting_stat_value": 0.41,
                },
            ),
            Action(
                name="AddCuratedInsight",
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
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Platoon Review", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Sequencing Notes", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="CreateVideoPlaylist",
                kwargs={"playlist_name": "Execution Focus", "clip_count": 3, "report_id": 13},
            ),
            Action(
                name="LogWorkflowRun",
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
            """
            Oversee the assembly of a pre-series package for Team 10's upcoming scheduled game on or after 2024-06-13. Acceptance criteria (single, deterministic terminal state):
1) Determine the next scheduled game based on current_date='2024-06-13', resolving to game_pk=2024000006 (Team 10 vs opponent_team_id=9).
2) Ensure pitch types are canonicalized before any spatial or reporting tasks (is idempotent if already canonical).
3) There must be exactly one scouting report for this game with details: report_type='Pre-Game', s3_pdf_path='s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf', gslides_link='https://slides.example.org/pre/2024000006', core_narrative_text='pre_series_policy_v1'.
4) Attach precisely two curated insights to that report utilizing the deterministic template '{category}_{metric}_{bucket}': (player_id=7, insight_text='tendency_chaserate_high', insight_type='tendency', supporting_stat_value=0.412) and (player_id=9, insight_text='predictability_firstpitchswing_low', insight_type='predictability', supporting_stat_value=0.193).
5) Two determined video playlists must exist for the given report with fixed links and counts: ('Opponent Tendencies', clip_count=4, internal_portal_link='https://portal.example/internal/playlist/ot_2024000006') and ('Miss Locations', clip_count=3, internal_portal_link='https://portal.example/internal/playlist/ml_2024000006').
6) A row in workflow_runs should be documented with: dag_name='pre_series_package', game_pk=2024000006, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:00:00Z', log_s3_path='s3://workflows/pre_series_package/g2024000006/2025-08-14.json'.
Policy references include: explicit date anchor for next-game selection, deterministic insight template, stable ordering/links, and the pre-processing step aligning with the domain proposal.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date":"2024-06-13"}),
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk":2024000006,"team_id":10}),
            Action(name="CanonicalizePitchTypes", kwargs={}),
            Action(name="CreateScoutingReport", kwargs={"report_type":"Pre-Game","game_pk":2024000006,"core_narrative_text":"pre_series_policy_v1","gslides_link":"https://slides.example.org/pre/2024000006","s3_pdf_path":"s3://reports/scouting/pre/2024-06-13_g2024000006_team10_vs9.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id":13,"player_id":7,"insight_text":"tendency_chaserate_high","insight_type":"tendency","supporting_stat_value":0.412}),
            Action(name="AddCuratedInsight", kwargs={"report_id":13,"player_id":9,"insight_text":"predictability_firstpitchswing_low","insight_type":"predictability","supporting_stat_value":0.193}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id":13,"playlist_name":"Opponent Tendencies","clip_count":4,"internal_portal_link":"https://portal.example/internal/playlist/ot_2024000006"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id":13,"playlist_name":"Miss Locations","clip_count":3,"internal_portal_link":"https://portal.example/internal/playlist/ml_2024000006"}),
            Action(name="LogWorkflowRun", kwargs={"dag_name":"pre_series_package","game_pk":2024000006,"status":"success","start_time_utc":"2025-08-14T00:00:00Z","end_time_utc":"2025-08-14T00:00:00Z","log_s3_path":"s3://workflows/pre_series_package/g2024000006/2025-08-14.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_069",
        instruction=(
            """
            Handle the finalization of the post-game analytics snapshot for game 2024000003. Ensure that a single terminal database state is provided, meeting all of the following acceptance criteria while avoiding the creation of unrelated records:
• Base the work on the completed game; artifacts that are derived should reference game 2024000003.
• Store the game's pitch data using the organization's standard pitch-type taxonomy.
• Ensure trend screening for this game aligns with the policy parameters (min_pitches=50, min_swings=30, min_bbe=25) incorporating EB shrinkage and FDR control at 0.10; use the resulting flags referenced in the brief.
• Maintain a 12×12 catcher-view pitch-location grid for this game with bounds x∈[-0.95,0.95], z∈[1.5,3.5]. Treat any per-pitch mapping rows generated by tooling as intermediate; only the persisted grid state matters for acceptance.
• A published post-game scouting brief is available for this game with the core narrative text "post_game_policy_v1", a slide deck link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.
• Record a leverage summary for this game using a threshold of 1.5.
• Log a publication audit event with the message “report_published report_id=<that brief’s id> draft_status=published” at 2025-08-18T18:20:00Z, including suggestion_text “acknowledge_and_distribute”.
• Do not include or return any intermediate row-level mappings; only return the report id of the brief at the conclusion.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000003}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True, "return_rows": True}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "Post-Game", "game_pk": 2024000003, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000003, "threshold": 1.5}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "message": "report_published report_id=13 draft_status=published", "is_manual_alert": True, "suggestion_text": "acknowledge_and_distribute"}),
        ],
        outputs=[
            "13"
        ]
    ),


    Task(
        annotator="saaish2",
        user_id="task_070",
        instruction=(
            """
            Coordinate the completion of a comprehensive post-game dossier for game 2024000008. In the final state of the database, ensure the following conditions are met (consider this an acceptance checklist, not a step-by-step procedure):
• The analytics input record must show two entries: statcast_daily (status 200, records=3600, ingested_at_utc=2024-03-05T00:00:00Z) and hawkeye_quality_audit (status 200, records=61, ingested_at_utc=2024-03-05T01:00:00Z).
• Ensure pitch types are stored using the canonical taxonomy and trend-screening reflects EB shrinkage with FDR=0.10 (min_pitches=50, min_swings=30, min_bbe=25).
• A 12×12 catcher-view grid with x∈[-0.95,0.95], z∈[1.5,3.5] must be present for this game; any per-pitch mapping rows generated by tooling are intermediate and should not be included in your return.
• Umpire calibration for umpire_id=2 should indicate zone_shift_x=-0.05, zone_shift_z=0.07, calibration_error_pct=2.3 with a 90% interval.
• Execution grading must exist for pitches 28 (glove-side-high→glove-side-high, 2.5in), 29 (arm-side-low→arm-side-mid, 6.8in), 31 (down-middle→down-middle, 1.9in), 30 (glove-side-high→glove-side-mid, 4.2in), 33 (arm-side-high→arm-side-high, 2.1in).
• A published brief must exist with the core narrative “post_game_policy_v1”, slide deck https://slides.example.org/post/2024000008, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf; attached are exactly two curated insights: (player_id=11, situational_rispcontact_high, 0.34) and (player_id=11, predictability_firstpitchstrike_high, 0.30).
• There are exactly two curated video playlists linked to that brief: “PutAway_2Strikes” and “FirstPitch_Strikes”, each containing exactly 3 clips.
• Use a threshold of 1.5 for the leverage summary; log a publication audit event at 2025-08-18T18:20:00Z with “report_published report_id=<that brief’s id> draft_status=published”, and suggestion_text “acknowledge_and_distribute”; a successful workflow run named “post_game_package” should exist with dag_name “analytics_post_game_v1”, start_time_utc=2025-08-18T18:20:30Z, end_time_utc=2025-08-18T18:22:00Z, timestamp_utc=2025-08-18T18:22:00Z, and log_s3_path s3://workflow/post_game_package/2024-03-05_g2024000008.log.
• Return only the brief’s report id.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "statcast_daily", "status_code": 200, "records_ingested": 3600, "ingested_at_utc": "2024-03-05T00:00:00Z"}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "hawkeye_quality_audit", "status_code": 200, "records_ingested": 61, "ingested_at_utc": "2024-03-05T01:00:00Z"}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="WriteUmpireGameModel", kwargs={"game_pk": 2024000008, "umpire_id": 2, "zone_shift_x": -0.05, "zone_shift_z": 0.07, "calibration_error_pct": 2.3, "confidence_interval": "90%"}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 28, "game_pk": 2024000008, "intended_quadrant_model": "glove-side-high", "actual_quadrant": "glove-side-high", "miss_distance_inches": 2.5}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "arm-side-low", "actual_quadrant": "arm-side-mid", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 31, "game_pk": 2024000008, "intended_quadrant_model": "down-middle", "actual_quadrant": "down-middle", "miss_distance_inches": 1.9}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 30, "game_pk": 2024000008, "intended_quadrant_model": "glove-side-high", "actual_quadrant": "glove-side-mid", "miss_distance_inches": 4.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "arm-side-high", "actual_quadrant": "arm-side-high", "miss_distance_inches": 2.1}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True, "return_rows": True}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "Post-Game", "game_pk": 2024000008, "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000008", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_post.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "situational_rispcontact_high", "insight_type": "situational", "supporting_stat_value": 0.34}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.30}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "PutAway_2Strikes", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "FirstPitch_Strikes", "clip_count": 3}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-18T18:20:00Z", "message": "report_published report_id=13 draft_status=published", "is_manual_alert": True, "suggestion_text": "acknowledge_and_distribute"}),
            Action(name="LogWorkflowRun", kwargs={"workflow_name": "post_game_package", "dag_name": "analytics_post_game_v1", "game_pk": 2024000008, "status": "success", "timestamp_utc": "2025-08-18T18:22:00Z", "start_time_utc": "2025-08-18T18:20:30Z", "end_time_utc": "2025-08-18T18:22:00Z", "log_s3_path": "s3://workflow/post_game_package/2024-03-05_g2024000008.log"}),
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_071",
        instruction=(
            """
            Coordinate the compilation of a comprehensive post-game analytics packet for game 2024000008, ensuring standardized labeling, persisted spatial features, insights compliant with policies, and mandated video content support.

Acceptance criteria (goal-oriented, non-procedural):
• Ensure there is precisely one completed post-game scouting dossier adhering to the organization's standard specifications:
  — narrative label: post_game_review
  — Google Slides artifact: https://docs.google.com/presentation/d/post_game_review
  — PDF artifact: s3://reports/scouting/post_game/2024000008.pdf
• Standardize pitch-type labels and maintain strike-zone spatial features using the organization's established 12×12 catcher-view grid with bounds x∈[-1.5,1.5], z∈[1.0,4.0].
• Conduct execution evaluations utilizing the game's canonical five-pitch sample with original quadrant targets and miss distances as documented in the dataset; do not infer or recompute.
• Curated insights need to pass through rules.py filters, eliminate redundant bullets, and be arranged by supporting_stat_value DESC followed by player_id ASC, using standardized keys.
• Ensure curated video content includes precisely the policy-mandated playlists — "Positive Reinforcement" and "Teaching Moments" — each with three clips attached to the dossier.
• Record the workflow completion with fixed UTC times (start 2025-08-18T00:35:00Z, end 2025-08-18T01:05:00Z) and a consistent S3 log path: s3://workflow/logs/post_game_review/2024000008/2025-08-18.log.
• Return the identifier of the finalized post-game dossier.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 29, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_middle", "miss_distance_inches": 2.4}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 33, "game_pk": 2024000008, "intended_quadrant_model": "up_in", "actual_quadrant": "middle_in", "miss_distance_inches": 6.8}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 46, "game_pk": 2024000008, "intended_quadrant_model": "down_away", "actual_quadrant": "down_away", "miss_distance_inches": 1.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 17, "game_pk": 2024000008, "intended_quadrant_model": "up_away", "actual_quadrant": "up_middle", "miss_distance_inches": 4.1}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 45, "game_pk": 2024000008, "intended_quadrant_model": "down_in", "actual_quadrant": "middle_in", "miss_distance_inches": 5.0}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game", "game_pk": 2024000008, "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            # FIX: collapse duplicates and sort curated insights by supporting_stat_value DESC then player_id ASC
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.56}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.55}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.36}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Manage the preparation of development materials for the week starting 2025-08-11 for Alexander Taylor (player_id=7) and Charlotte Johnson (player_id=9), and approve their goals immediately.

Acceptance criteria (single, deterministic terminal state):
1) Ensure that there are two player development reports available: (player_id=7, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/7/2025-08-11.pdf') and (player_id=9, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/9/2025-08-11.pdf').
2) Each pitcher must have exactly one goal linked to its respective dev_report_id, with coach_id=1010, target_review_date='2025-09-08', and goal_text values 'execution_fastball_glove_side' (for player_id=7) and 'sequencing_tunnel_changeup' (for player_id=9). Both goals need to be 'Approved'.
3) Ensure the existence of exactly two playlists for each dev report: ('Positive Reinforcement', 5) and ('Teaching Moments', 3).
4) Generate the trend flags table using min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10 after standardizing pitch types.
5) Log a single workflow run with status='success', dag_name='dev_weekly_pkg', starting at '2025-08-14T12:00:00Z' and ending at '2025-08-14T12:12:00Z', log_s3_path='s3://ops/logs/dev_weekly_pkg/2025-08-14_team10.json'.

Policy references you must honor:
• Ensure raw pitch types are standardized before computing trends; trend flags necessitate minimum samples + EB shrinkage + FDR (record parameters deterministically).
• Dev playlist categories maintain clip ranges: Positive Reinforcement ∈[3,5], Teaching Moments ∈[2,3].
Do not return any values.
            """
        ),
        actions=[
            Action(name="GetPlayerDetails", kwargs={"player_id": 7}),
            Action(name="GetPlayerDetails", kwargs={"player_id": 9}),
            Action(name="CanonicalizePitchTypes", kwargs={"scope": "all"}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "execution_fastball_glove_side", "coach_id": 1010, "target_review_date": "2025-09-08"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "sequencing_tunnel_changeup", "coach_id": 1010, "target_review_date": "2025-09-08"}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 5}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "dev_weekly_pkg", "status": "success", "start_time_utc": "2025-08-14T12:00:00Z", "end_time_utc": "2025-08-14T12:12:00Z", "log_s3_path": "s3://ops/logs/dev_weekly_pkg/2025-08-14_team10.json"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_073",
        instruction=(
            """
            Coordinate an end-to-end analytics packet for game 2024000008 to be suitable for coaching distribution.

Acceptance criteria (goal-oriented, non-procedural):
• Packet is finalized as published with narrative label post_game_review, Google Slides link https://docs.google.com/presentation/d/post_game_review, and PDF s3://reports/scouting/post_game/2024000008.pdf.
• Ensure completion of canonical pitch typing and persistent 12×12 catcher-view grid encoding (min_x=-1.5, max_x=1.5, min_z=1.0, max_z=4.0).
• Trends must be filtered utilizing EB shrinkage and FDR q=0.10 at thresholds min_pitches=50, min_swings=30, min_bbe=25.
• Curate insights that are canonical, non-duplicative, and sorted by supporting_stat_value DESC then player_id ASC; utilize exactly: (2, execution_ff_high, 0.60), (4, execution_sl_low, 0.54), (8, situational_risp_high, 0.50), (2, predictability_firstpitch_high, 0.46).
• Two support playlists should exist: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (3 clips).
• Audit the publication with a record on 2025-08-18T18:25:00Z with message 'report_published report_id=13 draft_status=published'.
• Confirm workflow completion recorded with start_time_utc=2025-08-18T18:05:00Z, end_time_utc=2025-08-18T18:25:00Z, and log path s3://workflow/logs/post_game_review/2024000008/2025-08-18-3.log.
• Avoid listing tool/API names or steps; present only the final state fulfilling these criteria.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "scouting_reports",
                "status_code": 200,
                "records_ingested": 1,
                "timestamp_utc": "2025-08-18T18:25:00Z",
                "message": "report_published report_id=13 draft_status=published",
                "game_pk": 2024000008
            }),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_sl_low", "insight_type": "execution", "supporting_stat_value": 0.54}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.50}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.46}),
            Action(name="ListCuratedInsights", kwargs={"report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            Action(name="ListVideoPlaylists", kwargs={"report_id": 13}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the Monday player-development check-ins for the week of 2025-08-11 to ensure they are fully represented in the system for players 11 and 12. Your work will be accepted if, upon completion, the database verifies all of the following deliverables—without dictating any specific method or order—for game 2024000002 and those players: • exactly one weekly development report per player at the stated paths (player 11 → s3://reports/player_dev/11/2025-08-11.pdf; player 12 → s3://reports/player_dev/12/2025-08-11.pdf); • exactly one development goal per player in Approved state with the target review date 2025-08-25 (player 11 → 'dev_goal_contact_quality' by coach 22; player 12 → 'dev_goal_zone_control' by coach 23); • one development packet per player with the following identifiers and links intact—player 11 narrative 'dev_weekly_packet_2025_08_11_p11' (slides https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11, PDF s3://reports/dev_packages/11/2025-08-11.pdf) and player 12 narrative 'dev_weekly_packet_2025_08_11_p12' (slides https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11, PDF s3://reports/dev_packages/12/2025-08-11.pdf)—each packet containing two playlists named 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); • one workflow activity labeled 'weekly_dev_checkins' recorded with start=end 2025-08-14T00:00:00Z and log path s3://logs/workflows/weekly_dev_checkins/2025-08-14/run.json. No further outputs are necessary; only this terminal state is considered.
            """
        ),
        actions=[
            Action(name="CreatePlayerDevReport", kwargs={
                "player_id": 11,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/11/2025-08-11.pdf"
            }),
            Action(name="CreatePlayerDevReport", kwargs={
                "player_id": 12,
                "week_of_date": "2025-08-11",
                "s3_pdf_path": "s3://reports/player_dev/12/2025-08-11.pdf"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 11,
                "player_id": 11,
                "goal_text": "dev_goal_contact_quality",
                "coach_id": 22,
                "target_review_date": "2025-08-25"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 12,
                "player_id": 12,
                "goal_text": "dev_goal_zone_control",
                "coach_id": 23,
                "target_review_date": "2025-08-25"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p11",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_11_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/11/2025-08-11.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "player-development",
                "game_pk": 2024000002,
                "core_narrative_text": "dev_weekly_packet_2025_08_11_p12",
                "gslides_link": "https://docs.google.com/presentation/d/dev_pkg_12_2025-08-11",
                "s3_pdf_path": "s3://reports/dev_packages/12/2025-08-11.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 14, "playlist_name": "Positive Reinforcement", "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 14, "playlist_name": "Teaching Moments", "clip_count": 2
            }),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are responsible for delivering a detailed post-game series-setup dossier for game 2024000008 for multi-day planning.

Acceptance outcomes (deterministic end-state):
• A published dossier must exist labeled 'post_game_series_setup_v1' with slide deck https://slides.series/setup/2024000008 and PDF s3://reports/scouting/series_setup_v1/2024000008.pdf.
• Pitch types should be canonicalized; a persisted 12×12 catcher-view grid must be available over x∈[-1.5,1.5] ft and z∈[1.0,4.0] ft.
• Trend vetting should apply empirical-Bayes shrinkage with FDR q=0.10 and minima 50/30/25; a leverage summary should be recorded with a threshold of 1.5.
• Six unique curated insights must be attached (player→code→value): 4→execution_ff_high→0.62; 8→predictability_firstpitchstrike_high→0.57; 3→situational_risp_high→0.54; 5→tendency_chase_low→0.34; 6→stamina_b2b_low→0.40; 7→predictability_sequencing_high→0.60.
• Three playlists must be associated with the dossier, each containing 3 clips: 'Positive Reinforcement', 'Teaching Moments', and 'Pattern Review'.
• A manual publication audit is required on 2025-08-21T04:50:00Z with message 'report_published report_id=<that dossier id> draft_status=published' and suggestion_text 'acknowledge_and_distribute'.
• The workflow run must be logged as successful from 2025-08-21T04:35:00Z to 2025-08-21T04:50:00Z at s3://workflow/logs/series_setup_v1/2024000008/2025-08-21-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008, "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10, "use_eb_shrinkage": True
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={
                "game_pk": 2024000008, "threshold": 1.5
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_series_setup_v1",
                "gslides_link": "https://slides.series/setup/2024000008",
                "s3_pdf_path": "s3://reports/scouting/series_setup_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-21T04:50:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "is_manual_alert": True
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 5, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 6, "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.40
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Pattern Review", "clip_count": 3, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are tasked with creating the post-game package for gamePk 2024000007 (game_status Final). Acceptance requires achieving the following final state:
• A plate-umpire calibration record must be present for this game with precisely: umpire_id=2, zone_shift_x=0.20, zone_shift_z=-0.10, calibration_error_pct=2.4, confidence_interval=0.90.
• A 12×12 zone grid should be persisted for pitches using bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 (cells documented in the pitches table).
• Three pitch execution grades should exist for this game with exact values and policy-consistent grades: (pitch_id=1, miss_distance_inches=10.2 ⇒ 'Major miss', intended_quadrant_model='down_middle', actual_quadrant='up_middle'); (pitch_id=3, miss_distance_inches=5.0 ⇒ 'Minor miss', intended_quadrant_model='away_edge', actual_quadrant='just_off_away'); (pitch_id=4, miss_distance_inches=2.0 ⇒ 'Executed', intended_quadrant_model='up_in', actual_quadrant='up_in').
• Exactly one new post-game scouting report must exist for 2024000007 with core_narrative_text 'postgame_core_thesis_execution_and_leverage', gslides_link 'https://slides.postgame/2024000007', s3_pdf_path 's3://reports/post_game/2024000007.pdf'.
• Two curated insights should be attached to that report with precisely: (player_id=7, insight_type='execution', insight_text='execution_gloveside_miss', supporting_stat_value=0.42) and (player_id=9, insight_type='situational', insight_text='situational_risp_late', supporting_stat_value=0.58).
• One highlight playlist linked to the same report must be present with playlist_name 'Game Highlights - Postgame Pulls' and clip_count 10.
• A completed workflow run is required with dag_name 'post_game_report_build', game_pk 2024000007, status 'success', start_time_utc=end_time_utc='2025-08-14T00:00:00Z', log_s3_path 's3://logs/workflows/post_game_report_build_2024000007.log'; and an ingestion log should exist with source_name 's3_event_log_upload', status_code 200, records_ingested 1.
            """
        ),
        actions=[
            Action(name="WriteUmpireGameModel", kwargs={"game_pk": 2024000007, "umpire_id": 2, "zone_shift_x": 0.20, "zone_shift_z": -0.10, "calibration_error_pct": 2.4, "confidence_interval": 0.90}),
            Action(name="GridEncodePitchLocations", kwargs={"min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 1, "game_pk": 2024000007, "intended_quadrant_model": "down_middle", "actual_quadrant": "up_middle", "miss_distance_inches": 10.2}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 3, "game_pk": 2024000007, "intended_quadrant_model": "away_edge", "actual_quadrant": "just_off_away", "miss_distance_inches": 5.0}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 4, "game_pk": 2024000007, "intended_quadrant_model": "up_in", "actual_quadrant": "up_in", "miss_distance_inches": 2.0}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000007, "core_narrative_text": "postgame_core_thesis_execution_and_leverage", "gslides_link": "https://slides.postgame/2024000007", "s3_pdf_path": "s3://reports/post_game/2024000007.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "execution_gloveside_miss", "insight_type": "execution", "supporting_stat_value": 0.42}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 9, "insight_text": "situational_risp_late", "insight_type": "situational", "supporting_stat_value": 0.58}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Game Highlights - Postgame Pulls", "clip_count": 10}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_report_build", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/post_game_report_build_2024000007.log"}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "s3_event_log_upload", "status_code": 200, "records_ingested": 1})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_077",
        instruction=(
            """
            Coordinate the creation of a pre-series scouting package for the upcoming gamePk 2024000011 and ensure the database state is a single, audit-compliant version consistent with internal guidelines. For acceptance, verification needs to confirm: a 12×12 pitch-location grid sustained within boundaries at min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5; a pre-series scouting report for 2024000011 containing core_narrative_text 'pre_series_thesis_attack_zones_and_baserunning', gslides_link 'https://slides.prep/2024000011', and s3_pdf_path 's3://reports/pre_series/2024000011.pdf' (associated with report_id 13, and all related child records must reference it); precisely three curated insights linked to the report — (player_id=11, 'tendency_hi_fb', type 'tendency', value 0.61), (player_id=12, 'predictability_first_pitch', type 'predictability', value 0.44), (player_id=7, 'execution_edge_low', type 'execution', value 0.38); two development-category playlists — 'Positive Reinforcement' featuring 4 clips and 'Teaching Moments' featuring 3 clips; and audit logs recording a 'pre_series_package_build' workflow and a 'park_factors_ingest' tick, both successful with status_code 200 and records_ingested 2, timestamped '2025-08-14T00:00:00Z'.
            """
        ),
        actions=[
            Action(name="GridEncodePitchLocations", kwargs={"min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "persist": True}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "pre-series", "game_pk": 2024000011, "core_narrative_text": "pre_series_thesis_attack_zones_and_baserunning", "gslides_link": "https://slides.prep/2024000011", "s3_pdf_path": "s3://reports/pre_series/2024000011.pdf"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "tendency_hi_fb", "insight_type": "tendency", "supporting_stat_value": 0.61}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 12, "insight_text": "predictability_first_pitch", "insight_type": "predictability", "supporting_stat_value": 0.44}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "execution_edge_low", "insight_type": "execution", "supporting_stat_value": 0.38}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "pre_series_package_build", "game_pk": 2024000011, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/pre_series_package_build_2024000011.log"}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "park_factors_ingest", "status_code": 200, "records_ingested": 2, "request_timestamp_utc": "2025-08-14T00:00:00Z"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_078",
        instruction=(
            """
            Prepare a coach-visible package of in-game moments for game 2024000007 with comprehensive auditability, structured as acceptance criteria. Normalize and discretize pitch data using the club's 12×12 catcher-view grid, bounded by x -1.5..1.5, z 1.0..4.0 with sustained persistence. There are exactly two high-leverage coach-visible bookmarks present at 2025-08-14T00:00:00Z — (pitch 5 → 2.40, 'HR_to_LF_spike') and (pitch 6 → 2.74, 'BasesLoaded_K') — and exactly one coach-visible manual bench note ('mound_visit_recommendation', leverage 0.00) documented at the same timestamp. A manual-note view for this game that is only published is accessible. The audit trail includes one source entry ('in_game_events_auto', status 200, records 2, 2025-08-14T00:00:00Z) and one workflow record under the label 'in_game_events_auto' with start=end 2025-08-14T00:00:00Z available at s3://logs/workflows/in_game_events_auto/2025-08-14/run.json.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000007}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000007,
                "min_x": -1.5, "max_x": 1.5, "min_z": 1.0, "max_z": 4.0, "persist": True
            }),
            Action(name="CreateAutoBookmarkEvent", kwargs={
                "game_pk": 2024000007, "pitch_id": 5, "leverage_index": 2.40, "narration": "HR_to_LF_spike",
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="CreateAutoBookmarkEvent", kwargs={
                "game_pk": 2024000007, "pitch_id": 6, "leverage_index": 2.74, "narration": "BasesLoaded_K",
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000007, "suggestion_text": "mound_visit_recommendation", "leverage_index": 0.00,
                "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 15, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="ListGameDayEvents", kwargs={
                "game_pk": 2024000007, "is_manual_alert": True, "draft_status": "published"
            }),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "in_game_events_auto", "status_code": 200, "records_ingested": 2,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are tasked with managing an auditable in-game bench alert for gamePk 2024000007 that also adheres to core standardization policy. To accept, ensure the database clearly reflects all the following end-state facts (no step listing implied): (1) a single manual bench alert is created for this game with suggestion_text 'bench_reminder_slide_step', leverage_index 1.20, pitch_id set as null, is_manual_alert true, created at timestamp_utc '2025-08-14T00:00:00Z', and it must be in published status at completion (with the status-change time recorded as '2025-08-14T00:00:00Z'); (2) the game’s pitch labels are aligned under the organization’s canonical schema; (3) pitch locations are standardized into the organization’s canonical 12×12 strike-zone lattice with set bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5, and they are persisted back; (4) the run is auditable through one successful job record 'bench_alert_publish' and one ingestion tick 'live_alerts_bus' with status_code 200 and records_ingested 1, both completed at '2025-08-14T00:00:00Z'.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000007}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000007,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000007,
                "pitch_id": None,
                "suggestion_text": "bench_reminder_slide_step",
                "leverage_index": 1.20,
                "draft_status": "draft",
                "is_manual_alert": True,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 13,
                "draft_status": "published",
                "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="LogWorkflowRun", kwargs={
                "dag_name": "bench_alert_publish",
                "game_pk": 2024000007,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/bench_alert_publish_2024000007.log"
            }),
            Action(name="LogIngestionEvent", kwargs={
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
            """
            Coordinate the delivery of opponent-prep materials for the upcoming gamePk 2024000012 that adhere to collection policy without concealed defaults. Verification is successful only if the final state reveals: unified pitch labeling for this game; spatial standardization to the organization’s canonical 12×12 lattice with set bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5, and that it is persisted; plus exactly one pre-series report for 2024000012 with core_narrative_text 'tendency_contact_upper_half', gslides_link 'https://slides.prep/2024000012', and s3_pdf_path 's3://reports/pre_series/2024000012.pdf'. Attach precisely two development-category playlists to that report: 'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips).
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000012}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000012,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-series",
                "game_pk": 2024000012,
                "core_narrative_text": "tendency_contact_upper_half",
                "gslides_link": "https://slides.prep/2024000012",
                "s3_pdf_path": "s3://reports/pre_series/2024000012.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 2})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_081",
        instruction=(
            """
            Ensure the delivery of a weekly development check-in for player_id 7 during the week of 2024-07-29, presented with a fully defined, deterministic footprint. To gain acceptance, provide: one and only one player development report for player_id 7 with week_of_date '2024-07-29' and s3_pdf_path 's3://reports/player_dev/7/2024-07-29.pdf'; a single micro-goal linked to this report with goal_text 'raise_swstr_rate_ff_top_third_2pct', coach_id 28, target_review_date '2024-08-05', and achieving Approved status by the time of completion; and exactly two development playlists associated with the report — 'Positive Reinforcement' clip_count 4 and 'Teaching Moments' clip_count 3. Additionally, document a successful workflow execution of 'weekly_dev_reports' with start_time_utc=end_time_utc='2025-08-14T00:00:00Z' and log_s3_path 's3://logs/workflows/weekly_dev_reports_2024-07-29.log'. Avoid logging any unrelated ingestion ticks.
            """
        ),
        actions=[
            Action(name="CreatePlayerDevReport", kwargs={
                "player_id": 7,
                "week_of_date": "2024-07-29",
                "s3_pdf_path": "s3://reports/player_dev/7/2024-07-29.pdf"
            }),
            Action(name="CreatePlayerDevGoal", kwargs={
                "dev_report_id": 11,
                "player_id": 7,
                "goal_text": "raise_swstr_rate_ff_top_third_2pct",
                "coach_id": 28,
                "target_review_date": "2024-08-05"
            }),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Leave a single post-game package that complies with policy for gamePk 2024000002. The assessment relies solely on the final state of the database, rather than the procedure followed. Auditors must verify from the stored records alone, with no hidden defaults, that:
• A pitch-type canonicalization pass was conducted for this game (the pass is noted as applied for gamePk 2024000002 even if no rows needed relabeling).
• Pitch locations for this game are expressed on the organization's canonical 12×12 strike-zone lattice with bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5 and are restored to the pitches table.
• A plate-umpire calibration for this game includes exactly: umpire_id 3, zone_shift_x -0.08, zone_shift_z 0.05, calibration_error_pct 1.9, confidence_interval 0.95.
• Three execution QC evaluations associated with this game exist with these exact tuples: (pitch_id=1, intended='down_middle', actual='up_middle', miss_distance_inches=9.5), (pitch_id=3, intended='away_edge', actual='just_off_away', miss_distance_inches=5.0), (pitch_id=4, intended='up_in', actual='up_in', miss_distance_inches=2.0).
• A post-game scouting report is available for this game with core_narrative_text 'execution_gloveside_miss', gslides_link 'https://slides.postgame/2024000002', and s3_pdf_path 's3://reports/post_game/2024000002.pdf'.
• Precisely two development playlists are connected to that report: 'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips).
• An auditable workflow ledger record pertains to this game with dag_name 'post_game_full_pkg', status 'success', start_time_utc '2025-08-14T00:00:00Z', end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/post_game_full_pkg_2024000002.log'.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000002}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000002}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000002,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000002,
                "umpire_id": 3,
                "zone_shift_x": -0.08,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": 0.95
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 1, "game_pk": 2024000002,
                "intended_quadrant_model": "down_middle",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 9.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 3, "game_pk": 2024000002,
                "intended_quadrant_model": "away_edge",
                "actual_quadrant": "just_off_away",
                "miss_distance_inches": 5.0
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 4, "game_pk": 2024000002,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "up_in",
                "miss_distance_inches": 2.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000002,
                "core_narrative_text": "execution_gloveside_miss",
                "gslides_link": "https://slides.postgame/2024000002",
                "s3_pdf_path": "s3://reports/post_game/2024000002.pdf"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Handle the Phase-1 execution-QC subset for gamePk 2024000007—this involves minimal, policy-based standardization and evaluation that comes before extended scouting and reporting. Approval necessitates a single, uniquely verifiable condition displaying: unified pitch labeling for the game; pitches standardized to a 12×12 grid with set boundaries (min_x −2.0, max_x 2.0, min_z 1.0, max_z 3.5); and two deterministic execution assessments documented (pitch_id 1: intended 'down_middle' → actual 'up_middle', deviation 9.5 in; pitch_id 3: intended 'away_edge' → actual 'just_off_away', deviation 5.0 in). Log the completed job run with the fixed timestamp '2025-08-14T00:00:00Z'.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000007}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000007, "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 1, "game_pk": 2024000007, "intended_quadrant_model": "down_middle", "actual_quadrant": "up_middle", "miss_distance_inches": 9.5}),
            Action(name="WritePitchExecutionGrade", kwargs={"pitch_id": 3, "game_pk": 2024000007, "intended_quadrant_model": "away_edge", "actual_quadrant": "just_off_away", "miss_distance_inches": 5.0}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "exec_qc_pipeline", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/exec_qc_pipeline_2024000007.log"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_084",
        instruction=(
            """
            Coordinate the validation of in-game decision support for gamePk 2024000007 with explicit leverage and traceability. An acceptable final state must illustrate: one high-leverage auto bookmark (pitch_id 9, leverage_index 2.10, narration 'late_risp_ff_up') and one bench alert (suggestion_text 'hold_runner_first_third', leverage_index 0.00), both completed as finalized with pitch_id null for the bench alert and is_manual_alert true. Spatial data should conform to a 12×12 grid with fixed boundaries (min_x −2.0, max_x 2.0, min_z 1.0, max_z 3.5), and the task must be verifiable with unified pitch labeling in addition to a successful job and a live-alerts ingestion tick at '2025-08-14T00:00:00Z'. No summaries or additional artifacts are allowed outside of these acceptance criteria.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000007}),
            Action(name="CreateAutoBookmarkEvent", kwargs={"game_pk": 2024000007, "pitch_id": 9, "leverage_index": 2.10, "narration": "late_risp_ff_up", "draft_status": "draft", "is_manual_alert": False, "timestamp_utc": "2025-08-14T00:00:00Z"}),
            Action(name="UpdateEventStatus", kwargs={"event_id": 13, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000007, "pitch_id": None, "suggestion_text": "hold_runner_first_third", "leverage_index": 0.0, "draft_status": "draft", "is_manual_alert": True, "timestamp_utc": "2025-08-14T00:00:00Z"}),
            Action(name="UpdateEventStatus", kwargs={"event_id": 14, "draft_status": "published", "changed_at_utc": "2025-08-14T00:00:00Z"}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000007, "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5, "cells_x": 12, "cells_z": 12, "persist": True}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "in_game_event_validation", "game_pk": 2024000007, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:00:00Z", "log_s3_path": "s3://logs/workflows/in_game_event_validation_2024000007.log"}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "live_alerts_bus", "status_code": 200, "records_ingested": 2, "request_timestamp_utc": "2025-08-14T00:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_085",
        instruction=(
            """
            Ensure responsible delivery of a deterministic, audit-ready pre-series package for the planned gamePk 2024000011. The focus is solely on the final state of the database; sequence is not a consideration. Auditors must confirm from stored records that: (1) the game's pitch labels align with the organization’s canonical schema, with clear evidence of the label-unification step for this game—even if relabeling wasn’t necessary; (2) pitch locations are represented on the organization’s canonical 12×12 strike-zone lattice, using bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5, and are recorded in the pitches table; (3) there is exactly one opponent report for this game containing core_narrative_text 'predictability_first_pitch', gslides_link 'https://slides.prep/2024000011', and s3_pdf_path 's3://reports/pre_series/2024000011.pdf' (child records reference the same report, identified as report_id 13 in this data); (4) three player insights are associated with that report with precise tuples: (player_id=11, type 'tendency', text 'tendency_hi_fb', value 0.61), (player_id=12, type 'predictability', text 'predictability_first_pitch', value 0.44), and (player_id=7, type 'execution', text 'execution_edge_low', value 0.38); (5) two development playlists are connected to that report—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips); (6) a valid pre-series workflow ledger entry exists for this game with dag_name 'pre_series_package_build', start_time_utc=end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/pre_series_package_build_2024000011.log'; and (7) one ingestion tick 'park_factors_ingest' occurs simultaneously with status_code 200 and records_ingested 2.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000011}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000011,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "pre-series",
                "game_pk": 2024000011,
                "core_narrative_text": "predictability_first_pitch",
                "gslides_link": "https://slides.prep/2024000011",
                "s3_pdf_path": "s3://reports/pre_series/2024000011.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 11, "insight_text": "tendency_hi_fb",
                "insight_type": "tendency", "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 12, "insight_text": "predictability_first_pitch",
                "insight_type": "predictability", "supporting_stat_value": 0.44
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 7, "insight_text": "execution_edge_low",
                "insight_type": "execution", "supporting_stat_value": 0.38
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3
            }),
            Action(name="LogWorkflowRun", kwargs={
                "dag_name": "pre_series_package_build",
                "game_pk": 2024000011,
                "status": "success",
                "start_time_utc": "2025-08-14T00:00:00Z",
                "end_time_utc": "2025-08-14T00:00:00Z",
                "log_s3_path": "s3://logs/workflows/pre_series_package_build_2024000011.log"
            }),
            Action(name="LogIngestionEvent", kwargs={
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
            """
            Take charge of assembling a comprehensive, audit-ready post-game package for gamePk 2024000002 (Final). Assessment focuses on the terminal state of the database, excluding methods. Auditors must substantiate, through stored records, that: pitch locations for the game adhere to the organization’s canonical strike-zone lattice (12×12 with bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5); plate-umpire calibration for this match corresponds precisely to umpire_id 3 with zone_shift_x −0.08, zone_shift_z 0.05, calibration_error_pct 1.9, confidence_interval 0.95; execution QC records are present for the organization’s three designated checks on pitches 1, 3, and 4 detailed as (1: intended='down_middle', actual='up_middle', miss=9.5 in), (3: intended='away_edge', actual='just_off_away', miss=5.0 in), (4: intended='up_in', actual='up_in', miss=2.0 in); a post-game scouting report for this game exists with core_narrative_text 'execution_gloveside_miss', gslides_link 'https://slides.postgame/2024000002', and s3_pdf_path 's3://reports/post_game/2024000002.pdf'; the curated insight module for the report includes exactly three entries with (player_id=5, type 'tendency', text 'tendency_low_offspeed', value 0.47), (player_id=11, type 'execution', text 'execution_edge_up', value 0.52), and (player_id=2, type 'situational', text 'situational_two_strike', value 0.41); and the development media attached comprises the two standard playlists—'Positive Reinforcement' (4 clips) and 'Teaching Moments' (3 clips). Confirm a successful workflow ledger entry for this game containing dag_name 'post_game_full_pkg', with start_time_utc=end_time_utc='2025-08-14T00:00:00Z' and log_s3_path 's3://logs/workflows/post_game_full_pkg_2024000002.log'. The emphasis is on this verifiable terminal state, not the means or tools applied.
            """
        ),
        actions=[
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000002,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="WriteUmpireGameModel", kwargs={
                "game_pk": 2024000002,
                "umpire_id": 3,
                "zone_shift_x": -0.08,
                "zone_shift_z": 0.05,
                "calibration_error_pct": 1.9,
                "confidence_interval": 0.95
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 1, "game_pk": 2024000002,
                "intended_quadrant_model": "down_middle",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 9.5
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 3, "game_pk": 2024000002,
                "intended_quadrant_model": "away_edge",
                "actual_quadrant": "just_off_away",
                "miss_distance_inches": 5.0
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 4, "game_pk": 2024000002,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "up_in",
                "miss_distance_inches": 2.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000002,
                "core_narrative_text": "execution_gloveside_miss",
                "gslides_link": "https://slides.postgame/2024000002",
                "s3_pdf_path": "s3://reports/post_game/2024000002.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_low_offspeed", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 11, "insight_text": "execution_edge_up", "insight_type": "execution", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "situational_two_strike", "insight_type": "situational", "supporting_stat_value": 0.41}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            You are responsible for producing a deterministic, audit-compliant summary after the game for gamePk 2024000007 (Final). The only important factor is the final state of the database—no particular sequence or API usage is inferred. Auditors must confirm through the stored records that: the game's pitch locations are represented using the organization's official strike-zone lattice (12×12 with bounds min_x=-2.0, max_x=2.0, min_z=1.0, max_z=3.5) and stored; there exists exactly one post-game report for this game containing core_narrative_text 'execution_edge_low', gslides_link 'https://slides.postgame/2024000007', and s3_pdf_path 's3://reports/post_game/2024000007.pdf'; two curated insights are linked to that report precisely as the tuples (player_id=11, type 'tendency', text 'tendency_fb_hi', value 0.61) and (player_id=7, type 'predictability', text 'predictability_firstpitch_zone1', value 0.44); the development media associated with the report includes exactly two standard playlists—'Positive Reinforcement' (3 clips) and 'Teaching Moments' (2 clips); one high-leverage bookmark is present on pitch_id 10 having leverage_index 2.20 and text 'late_game_ff_up', maintained on the event and published with changed_at_utc '2025-08-14T00:00:00Z'; and a successful workflow ledger entry is in place with dag_name 'series_summary_postgame', start_time_utc=end_time_utc '2025-08-14T00:00:00Z', and log_s3_path 's3://logs/workflows/series_summary_postgame_2024000007.log'.
            """
        ),
        actions=[
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000007,
                "min_x": -2.0, "max_x": 2.0, "min_z": 1.0, "max_z": 3.5,
                "cells_x": 12, "cells_z": 12,
                "persist": True
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000007,
                "core_narrative_text": "execution_edge_low",
                "gslides_link": "https://slides.postgame/2024000007",
                "s3_pdf_path": "s3://reports/post_game/2024000007.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 11,
                "insight_text": "tendency_fb_hi",
                "insight_type": "tendency",
                "supporting_stat_value": 0.61
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13,
                "player_id": 7,
                "insight_text": "predictability_firstpitch_zone1",
                "insight_type": "predictability",
                "supporting_stat_value": 0.44
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Positive Reinforcement",
                "clip_count": 3
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "report_id": 13,
                "playlist_name": "Teaching Moments",
                "clip_count": 2
            }),
            Action(name="CreateAutoBookmarkEvent", kwargs={
                "game_pk": 2024000007,
                "pitch_id": 10,
                "leverage_index": 2.20,
                "narration": "late_game_ff_up",
                "draft_status": "draft",
                "is_manual_alert": False,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="UpdateEventStatus", kwargs={
                "event_id": 13,
                "draft_status": "published",
                "changed_at_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Conclude a streamlined post-game snapshot for game 2024000003.

Acceptance outcomes (final DB state):
• Game pitch data must adhere to the organization's official pitch-type taxonomy.
• A 12×12 catcher-view location grid should be stored abiding by the organization's standard bounds x∈[-0.95,0.95] ft, z∈[1.5,3.5] ft.
• Trend evaluation must be documented with policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• A sanctioned post-game brief must be present with core narrative “post_game_policy_v1”, slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.
• Exactly two coaching playlists are attached to the brief — “Positive Reinforcement” and “Teaching Moments” — each must contain precisely 3 clips according to the organization’s post-game review checklist; any deviation in clip count is unacceptable.
• A manual publication audit is recorded at 2025-08-18T18:20:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the identical text stored as an operator note.
Return only the brief’s report id.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000003}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000003}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000003,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000003,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "min_effect_size": 0.05,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "Post-Game",
                "game_pk": 2024000003,
                "core_narrative_text": "post_game_policy_v1",
                "gslides_link": "https://slides.example.org/post/2024000003",
                "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateManualAlertEvent", kwargs={
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
            """
            Handle the creation of a teaching-focused post-game dossier for game 2024000008 ensuring it complies with policy and is ready for staff utilization.

Acceptance outcomes (terminal DB state):
• Canonical pitch types and a persisted catcher-view grid (12×12; x∈[-0.95,0.95], z∈[1.5,3.5]).
• Trend vetting documented with EB shrinkage, FDR q=0.10, practical-effect ≥0.05, and minima 50/30/25.
• A published dossier labeled for teaching use (core narrative "post_game_teachpack_v1") with slide link https://docs.google.com/presentation/d/post_game_teachpack_v1 and PDF s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf.
• Four unique curated insights mapped to appropriate roster players (no duplicate codes).
• Exactly the two policy-mandated coaching playlists are associated with the dossier with 3 clips each: “Positive Reinforcement” and “Teaching Moments”.
• A manual publication audit on 2025-08-20T21:10:00Z logs the publication message verbatim, retains suggestion_text “acknowledge_and_distribute”, and keeps the same publication message as the operator note.
• The workflow run for this task is documented as successful from 2025-08-20T20:55:00Z to 2025-08-20T21:10:00Z at s3://workflow/logs/post_game_teachpack_v1/2024000008/2025-08-20-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008,
                "min_x": -0.95,
                "max_x": 0.95,
                "min_z": 1.5,
                "max_z": 3.5,
                "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008,
                "min_pitches": 50,
                "min_swings": 30,
                "min_bbe": 25,
                "fdr_threshold": 0.10,
                "min_effect_size": 0.05,
                "use_eb_shrinkage": True,
                "control": "FDR"
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "label": "post_game_teachpack_v1",
                "core_narrative_text": "post_game_teachpack_v1",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_teachpack_v1",
                "s3_pdf_path": "s3://reports/scouting/post_game_teachpack_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008,
                "timestamp_utc": "2025-08-20T21:10:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "operator_note": "report_published report_id=13 draft_status=published",
                "is_manual_alert": True
            }),
            # Four curated insights (all unique codes)
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.34
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 3,
                "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.56
            }),
            # Policy playlists
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete a coach-facing post-game review for our home game. Assume that upstream ingestion/QC have already been approved and the game has concluded.
Acceptance criteria (terminal database state):
• A post-game scouting brief is present for game_pk 2024000008 with core narrative post_game_review and the links https://docs.google.com/presentation/d/post_game_review and s3://reports/scouting/post_game/2024000008.pdf.
• Execution evaluation is noted for exactly five pitches from this game with the following intent/actual quadrants and miss distances (inches):
  - pitch_id 29: intended down_away, actual down_middle, miss 2.4
  - pitch_id 33: intended up_in, actual middle_in, miss 6.8
  - pitch_id 46: intended down_away, actual down_away, miss 1.2
  - pitch_id 17: intended up_away, actual up_middle, miss 4.1
  - pitch_id 45: intended down_in, actual middle_in, miss 5.0
• Six curated insights are appended to that brief using the prescribed key template and values: 
  situational_risp_high (0.55) for player_id 8; predictability_firstpitch_high (0.31) for player_id 2; execution_fastball_high (0.60) for player_id 4; execution_slider_low (0.56) for player_id 8; situational_risp_high (0.52) for player_id 2; predictability_firstpitch_high (0.36) for player_id 4.
• Four video playlists are affixed to the brief: two titled Positive Reinforcement with 3 clips each, and two titled Teaching Moments with 2 clips each.
• The workflow registry logs a completed run with dag_name post_game_review_packet and game_pk 2024000008, status success, start_time_utc matched with end_time_utc at 2025-08-18T00:00:00Z, and log path s3://workflow/logs/post_game_review_packet/2024000008/2025-08-18.log.
No extra outputs are needed.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 29, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_middle",
                "miss_distance_inches": 2.4
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 33, "game_pk": 2024000008,
                "intended_quadrant_model": "up_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 6.8
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 46, "game_pk": 2024000008,
                "intended_quadrant_model": "down_away",
                "actual_quadrant": "down_away",
                "miss_distance_inches": 1.2
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 17, "game_pk": 2024000008,
                "intended_quadrant_model": "up_away",
                "actual_quadrant": "up_middle",
                "miss_distance_inches": 4.1
            }),
            Action(name="WritePitchExecutionGrade", kwargs={
                "pitch_id": 45, "game_pk": 2024000008,
                "intended_quadrant_model": "down_in",
                "actual_quadrant": "middle_in",
                "miss_distance_inches": 5.0
            }),
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game",
                "game_pk": 2024000008,
                "core_narrative_text": "post_game_review",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_review",
                "s3_pdf_path": "s3://reports/scouting/post_game/2024000008.pdf"
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.55
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.31
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_fastball_high",
                "insight_type": "execution",
                "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "execution_slider_low",
                "insight_type": "execution",
                "supporting_stat_value": 0.56
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 2,
                "insight_text": "situational_risp_high",
                "insight_type": "situational",
                "supporting_stat_value": 0.52
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "predictability_firstpitch_high",
                "insight_type": "predictability",
                "supporting_stat_value": 0.36
            }),
            # FIX: use the correct key 'playlist_name'
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 2, "report_id": 13
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Dispatch an execution-focused post-game report for game 2024000008 designed for MLB coaching evaluation.

End-state criteria (terminal DB state):
• Pitch types adhere to canonical form; a 12×12 catcher-view grid is maintained with policy limits x∈[-0.95,0.95], z∈[1.5,3.5].
• Trends undergo verification with EB shrinkage, FDR q=0.10, practical-effect ≥0.05, and minimum counts of 50/30/25; a leverage rundown is documented at threshold 1.5.
• Evidence of execution grading includes an audit of three pitches using the standard quadrant model (catcher_view_q4_v1): one Executed (UL, 2.1″), one Minor Miss (UR, 7.5″), and one Major Miss (LL, 10.2″), aligning with policy thresholds (Minor ≤9″, Major >9″).
• A released dossier tagged 'post_game_exec_focus_v1' is accessible with slide link https://docs.google.com/presentation/d/post_game_exec_focus_v1 and PDF s3://reports/scouting/post_game_exec_focus_v1/2024000008.pdf.
• Six curated insights are unique (distinct by player and metric) and prioritized by supporting strength; themes are evenly distributed and may recur only when metrics differ.
• Exactly the two policy-required playlists are included with 3 clips each.
• A manual publication audit on 2025-08-21T23:25:00Z archives the publication message word-for-word, suggestion_text “acknowledge_and_distribute”, and duplicates the message as the operator note; the workflow operation is documented as successful for 2025-08-21T23:10:00Z→2025-08-21T23:25:00Z in s3://workflow/logs/post_game_exec_focus_v1/2024000008/2025-08-21-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
                kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}
            ),
            Action(
                name="FilterTrends",
                kwargs={
                    "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                    "fdr_threshold": 0.10, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"
                }
            ),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            # Execution grades
            Action(
                name="WritePitchExecutionGrade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 1,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL",
                    "miss_distance_inches": 2.1, "grade": "Executed"
                }
            ),
            Action(
                name="WritePitchExecutionGrade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 2,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR",
                    "miss_distance_inches": 7.5, "grade": "Minor Miss"
                }
            ),
            Action(
                name="WritePitchExecutionGrade",
                kwargs={
                    "game_pk": 2024000008, "pitch_id": 3,
                    "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL",
                    "miss_distance_inches": 10.2, "grade": "Major Miss"
                }
            ),
            # Dossier
            Action(
                name="CreateScoutingReport",
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
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.64}
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.58}
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.56}
            ),
            Action(  # platoon-style content expressed within allowed theme set
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 7, "insight_text": "tendency_lhh_high", "insight_type": "tendency", "supporting_stat_value": 0.55}
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.39}
            ),
            Action(
                name="AddCuratedInsight",
                kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.32}
            ),
            # Policy playlists
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13}),
            Action(name="CreateVideoPlaylist", kwargs={"playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13}),
            # Publication audit + workflow log
            Action(
                name="CreateManualAlertEvent",
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
                name="LogWorkflowRun",
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
            """
            Compile and disseminate a post-game development report for game 2024000008.

End-state criteria (terminal DB state):
• The game's pitch data employs the organization's canonical pitch-type classification.
• A catcher-view grid of 12×12 is maintained with standard organizational limits x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Trend authentication is conducted using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• A published post-game summary exists with main narrative "post_game_platoon_pred_v1", slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1, and PDF s3://reports/scouting/post_game_platoon_pred_v1/2024000008.pdf.
• Precisely six curated insights accompany the summary—only these six entries and in this sequence (no additional curated insights are linked):
   1) player_id=4, insight_text=execution_ff_high,              insight_type=execution,      supporting_stat_value=0.63
   2) player_id=7, insight_text=predictability_sequencing_high, insight_type=predictability, supporting_stat_value=0.60
   3) player_id=8, insight_text=tendency_chase_low,             insight_type=tendency,       supporting_stat_value=0.57
   4) player_id=3, insight_text=situational_risp_high,          insight_type=situational,    supporting_stat_value=0.52
   5) player_id=6, insight_text=stamina_lategame_low,           insight_type=stamina,        supporting_stat_value=0.49
   6) player_id=2, insight_text=tendency_bunt_low,              insight_type=tendency,       supporting_stat_value=0.47
• Two coaching playlists are related to the summary: “Positive Reinforcement” (3 clips) and “Teaching Moments” (3 clips).
• An audit of the publication (manual) is logged at 2025-08-22T01:40:00Z with message “report_published report_id=<the brief’s id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and the identical text captured as an operator note.
• A workflow run completion record exists with dag_name “post_game_platoon_pred_v1”, game_pk 2024000008, status “success”, start_time_utc 2025-08-22T01:39:00Z, end_time_utc 2025-08-22T01:41:00Z, and log_s3_path s3://workflow-runs/post_game_platoon_pred_v1/2024000008/2025-08-22T01:39:00Z.log.
Return only the report id of the summary.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(
                name="GridEncodePitchLocations",
                kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}
            ),
            Action(
                name="FilterTrends",
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
                name="CreateScoutingReport",
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
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high",               "insight_type": "execution",      "supporting_stat_value": 0.63}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high",   "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low",               "insight_type": "tendency",       "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high",            "insight_type": "situational",    "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low",             "insight_type": "stamina",        "supporting_stat_value": 0.49}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low",                "insight_type": "tendency",       "supporting_stat_value": 0.47}),
            # Required coaching playlists
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments",       "clip_count": 3}),
            # Publication audit (manual)
            Action(
                name="CreateManualAlertEvent",
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
                name="LogWorkflowRun",
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
            """
            Complete the creation of a high-leverage, teaching-ready post-game report for game 2024000008 that follows policy and results in a single fixed DB state.

Acceptance results (final DB state):
• Standard pitch types; saved 12×12 catcher-view grid at policy boundaries x∈[-0.95,0.95], z∈[1.5,3.5].
• Review of policy trends (EB shrinkage; FDR q=0.10; practical effect threshold ≥0.05; minimum 50/30/25) and a high-leverage summary at level 1.5 are captured.
• A released report named 'post_game_highlev_teach_v1' is available with slide link https://docs.google.com/presentation/d/post_game_highlev_teach_v1 and PDF s3://reports/scouting/post_game_highlev_teach_v1/2024000008.pdf.
• Six distinct curated insights (no repetition), with no duplicated themes for predictability; players are properly assigned and insights ordered by supporting strength.
• Precisely the two required playlists by policy are included, each featuring 3 clips.
• Conduct a manual publication check at 2025-08-22T01:40:00Z to save the standard publication message, suggestion_text “acknowledge_and_distribute”, and the same text in operator note; log the workflow run as successful for 2025-08-22T01:25:00Z→2025-08-22T01:40:00Z at s3://workflow/logs/post_game_highlev_teach_v1/2024000008/2025-08-22-1.log.
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000008}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={
                "game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True
            }),
            Action(name="FilterTrends", kwargs={
                "game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25,
                "fdr_threshold": 0.10, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"
            }),
            # Create dossier first, then record publication audit, then compute leverage summary so manual activity is captured
            Action(name="CreateScoutingReport", kwargs={
                "report_type": "post-game", "game_pk": 2024000008,
                "label": "post_game_highlev_teach_v1",
                "core_narrative_text": "post_game_highlev_teach_v1",
                "gslides_link": "https://docs.google.com/presentation/d/post_game_highlev_teach_v1",
                "s3_pdf_path": "s3://reports/scouting/post_game_highlev_teach_v1/2024000008.pdf",
                "draft_status": "published"
            }),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:40:00Z",
                "title": "publication_audit",
                "message": "report_published report_id=13 draft_status=published",
                "suggestion_text": "acknowledge_and_distribute",
                "operator_note": "acknowledge_and_distribute",
                "is_manual_alert": True
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            # Curated insights (ordered by supporting_stat_value desc; no duplicate 'predictability')
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 4,
                "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.60
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 7,
                "insight_text": "tendency_platoonlhh_high", "insight_type": "tendency", "supporting_stat_value": 0.59
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 8,
                "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 3,
                "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.54
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 6,
                "insight_text": "stamina_b2b_low", "insight_type": "stamina", "supporting_stat_value": 0.41
            }),
            Action(name="AddCuratedInsight", kwargs={
                "report_id": 13, "player_id": 5,
                "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.33
            }),
            # Policy playlists
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Positive Reinforcement", "clip_count": 3, "report_id": 13
            }),
            Action(name="CreateVideoPlaylist", kwargs={
                "playlist_name": "Teaching Moments", "clip_count": 3, "report_id": 13
            }),
            # Workflow log
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Complete the concise post-game snapshot for game 2024000003.

Acceptance results (final DB state):
• Confirm the game is marked Final before any post-game entries; this checkpoint is verified via a manual audit at 2025-08-18T18:10:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and the same text saved as operator_note.
• The game's pitch data adheres to the organization's canonical pitch-type framework.
• A catcher-view 12×12 position grid is maintained within bounds x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Document trend analysis based on policy criteria (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect threshold of 0.05.
• A post-game brief is published with the main narrative "post_game_policy_v1", slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.
• Include exactly two coaching playlists with the brief: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Store a manual publication check at 2025-08-18T18:20:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and the identical text saved as operator note.

Return only the report id of the brief.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:10:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000003}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_policy_v1", "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_095",
        instruction=(
            """
            Handle the publication of a concise post-game snapshot for game 2024000003.

Acceptance outcomes (terminal DB state):
• Ensure the pitch dataset aligns with the organization's canonical pitch-type taxonomy.
• Maintain a catcher-view 12×12 grid with standard bounds x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Document trend vetting recorded with EB shrinkage and FDR q=0.10 (min_pitches=50, min_swings=30, min_bbe=25, practical-effect≥0.05).
• Validate the existence of a published post-game brief with core narrative "post_game_snapshot_v1", slide link https://slides.example.org/post/2024000003_snapshot, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_snapshot.pdf.
• Attach exactly two curated insights in this specific order:
   1) player_id=7, insight_text=predictability_firstpitch_high, insight_type=predictability, supporting_stat_value=0.58
   2) player_id=8, insight_text=tendency_chase_low,             insight_type=tendency,       supporting_stat_value=0.47
• Link one coaching playlist: “Teaching Moments” (3 clips).
• Store a publication audit (manual) at 2025-08-18T18:20:00Z with message “report_published report_id=<id> draft_status=published”, suggestion_text “acknowledge_and_distribute”, and save the same text as an operator note.
Return only the brief’s report id.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000003}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_snapshot_v1", "core_narrative_text": "post_game_snapshot_v1", "gslides_link": "https://slides.example.org/post/2024000003_snapshot", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_snapshot.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_firstpitch_high", "insight_type": "predictability", "supporting_stat_value": 0.58}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=["13"]
    ),

    Task(
        annotator="saaish2",
        user_id="task_096",
        instruction=(
            """
            Coordinate the completion of a platoon/predictability post-game briefing for game 2024000008.

Acceptance outcomes (terminal DB state):
• Confirm the game is marked Final before any post-game entries; this gate is validated by a manual audit at 2025-08-22T03:30:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and the same text saved as operator_note.
• Ensure the game's pitch data corresponds with the organization's canonical pitch-type taxonomy.
• Preserve a catcher-view 12×12 location grid with bounds x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Record trend vetting using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• Confirm a published post-game brief with core narrative "post_game_platoon_pred_v1", slide link https://docs.google.com/presentation/d/post_game_platoon_pred_v1, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_platoon_pred.pdf.
• Attach five curated insights (unique categories, order preserved): execution_ff_high [execution, 0.63] for player 4; predictability_sequencing_high [predictability, 0.60] for player 7; tendency_chase_low [tendency, 0.57] for player 8; situational_risp_high [situational, 0.52] for player 3; stamina_lategame_low [stamina, 0.49] for player 6.
• Tie two coaching playlists to the brief: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Document a publication audit (manual) at 2025-08-22T03:40:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and store the same text as an operator note.

Return only the brief’s report id.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T03:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_platoon_pred_v1", "core_narrative_text": "post_game_platoon_pred_v1", "gslides_link": "https://docs.google.com/presentation/d/post_game_platoon_pred_v1", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_platoon_pred.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.63}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T03:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_097",
        instruction=(
            """
            Handle the compilation of a two-strike approach post-game summary for game 2024000008.

Expected outcomes (terminal DB state):
• Confirm the game as Final before any post-game entries; verify this through a manual audit at 2025-08-22T02:00:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and save the same text as operator_note.
• Use the organization's canonical pitch-type taxonomy for the game's pitch data.
• Maintain a catcher-view 12×12 location grid with bounds x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Record trend vetting using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• Ensure there is a published post-game summary with core narrative "post_game_two_strike_v1", slide link https://slides.example.org/post/2024000008_two_strike, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_two_strike.pdf.
• Link three curated insights (keeping the order) to the summary: execution_ff_high [execution, 0.62] for player 4; predictability_sequencing_high [predictability, 0.59] for player 7; situational_risp_high [situational, 0.52] for player 3.
• Attach two coaching playlists to the summary: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Conduct a manual publication audit at 2025-08-22T02:10:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and save the same text as operator note.

Only provide the summary report id.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:00:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_two_strike_v1", "core_narrative_text": "post_game_two_strike_v1", "gslides_link": "https://slides.example.org/post/2024000008_two_strike", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_two_strike.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:10:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_098",
        instruction=(
            """
            Coordinate the delivery of a baserunning/control post-game summary for game 2024000008.

Expected outcomes (terminal DB state):
• Confirm the game as Final before any post-game entries; verify this through a manual audit at 2025-08-22T02:30:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and save the same text as operator_note.
• Use the organization's canonical pitch-type taxonomy for the game's pitch data.
• Maintain a catcher-view 12×12 location grid with bounds x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Record trend vetting using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• Limit any pitch execution grading in this deliverable to the labels: Executed, Minor miss, Major miss.
• Ensure there is a published post-game summary with core narrative "post_game_baserun_ctrl_v1", slide link https://slides.example.org/post/2024000008_baserun_ctrl, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_baserun_ctrl.pdf.
• Link four curated insights (keeping the order) to the summary: tendency_bunt_low [tendency, 0.47] for player 2; execution_ff_high [execution, 0.61] for player 4; predictability_firstpitchstrike_high [predictability, 0.57] for player 8; situational_risp_high [situational, 0.51] for player 3.
• Attach two coaching playlists to the summary: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Conduct a manual publication audit at 2025-08-22T02:40:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and save the same text as operator note.

Only provide the summary report id.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 1, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 2.0, "grade": "Executed"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 2, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR", "miss_distance_inches": 7.0, "grade": "Minor miss"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 3, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL", "miss_distance_inches": 10.0, "grade": "Major miss"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_baserun_ctrl_v1", "core_narrative_text": "post_game_baserun_ctrl_v1", "gslides_link": "https://slides.example.org/post/2024000008_baserun_ctrl", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_baserun_ctrl.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.61}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "predictability_firstpitchstrike_high", "insight_type": "predictability", "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.51}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_099",
        instruction=(
            """
            Coordinate the delivery of a detailed mixed-model post-game summary for game 2024000008.

Required outcomes (final database state):
• The game must be verified as Final before any post-game entries; this checkpoint is confirmed by a manual review on 2025-08-22T01:30:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and the same information stored as operator_note.
• The game's pitch information adheres to the organization's standard pitch-type classification.
• A catcher-view 12×12 position grid is established using boundaries x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Trend verification is documented using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect threshold of 0.05.
• A post-game summary is published featuring the core narrative "post_game_mixed_model_v1", slide link https://slides.example.org/post/2024000008_mixed_model, and PDF s3://reports/scouting/post/2024-03-05_g2024000008_mixed_model.pdf.
• Six tailored insights (themes distinct, order unchanged) are linked to the summary: execution_ff_high [execution, 0.63] for player 4; predictability_sequencing_high [predictability, 0.60] for player 7; tendency_chase_low [tendency, 0.57] for player 8; situational_risp_high [situational, 0.52] for player 3; stamina_lategame_low [stamina, 0.49] for player 6; tendency_bunt_low [tendency, 0.47] for player 2.
• Two coaching playlists are associated with the summary: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• A publication review (manual) takes place at 2025-08-22T01:40:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and the same information stored as operator note.
• A workflow execution record is available with dag_name "post_game_mixed_model_v1", status "success", start_time_utc 2025-08-22T01:39:00Z, end_time_utc 2025-08-22T01:41:00Z, and log_s3_path s3://workflow-runs/post_game_mixed_model_v1/2024000008/2025-08-22T01:39:00Z.log.

Return solely the report id of the summary.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:30:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_mixed_model_v1", "core_narrative_text": "post_game_mixed_model_v1", "gslides_link": "https://slides.example.org/post/2024000008_mixed_model", "s3_pdf_path": "s3://reports/scouting/post/2024-03-05_g2024000008_mixed_model.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.63}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.60}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.57}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T01:40:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_mixed_model_v1", "game_pk": 2024000008, "status": "success", "start_time_utc": "2025-08-22T01:39:00Z", "end_time_utc": "2025-08-22T01:41:00Z", "log_s3_path": "s3://workflow-runs/post_game_mixed_model_v1/2024000008/2025-08-22T01:39:00Z.log"})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_100",
        instruction=(
            """
            Handle the preparation and issuance of a post-game two-strike approach summary for game 2024000008 encompassing graded execution, customized insights, playlists, and a comprehensive audit.

Required outcomes:
• Standard pitch types; a catcher-view 12×12 position grid is saved with the organization's defined boundaries x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Trends undergo verification using EB shrinkage, FDR q=0.10, and a practical-effect threshold of 0.05 following the thresholds (min_pitches=50, min_swings=30, min_bbe=25).
• Leverage summary is documented at threshold 1.5.
• Four execution ratings are recorded utilizing intended_quadrant_model "catcher_view_q4_v1": (1→Executed UL 2.0"), (2→Minor Miss UR 7.0"), (3→Major Miss LL 10.0"), (4→Executed UL 1.8").
• A published summary exists with core narrative "post_game_two_strike_v1", slide link https://slides.example.org/post/2024000008_two_strike, and PDF s3://reports/scouting/post/2024-08-01_g2024000008_two_strike.pdf.
• Exactly five distinct insights—in this order:
   1) player_id=4, insight_text=execution_ff_high, insight_type=execution, supporting_stat_value=0.62
   2) player_id=7, insight_text=predictability_sequencing_high, insight_type=predictability, supporting_stat_value=0.59
   3) player_id=3, insight_text=situational_risp_high, insight_type=situational, supporting_stat_value=0.52
   4) player_id=6, insight_text=stamina_lategame_low, insight_type=stamina, supporting_stat_value=0.49
   5) player_id=8, insight_text=tendency_chase_low, insight_type=tendency, supporting_stat_value=0.45
• Two playlists associated: “Positive Reinforcement” (3) and “Teaching Moments” (3).
• Manual publication review at 2025-08-22T02:30:00Z with message “report_published report_id=<id> draft_status=published”, suggestion_text/operator_note “acknowledge_and_distribute”.
• Workflow execution is logged with dag_name “post_game_two_strike_v1”, status “success”, start_time_utc 2025-08-22T02:29:00Z, end_time_utc 2025-08-22T02:31:00Z, log s3://workflow-runs/post_game_two_strike_v1/2024000008/2025-08-22T02:29:00Z.log.
Return solely the report id of the summary.
            """
        ),
        actions=[
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000008}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000008, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000008, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000008, "threshold": 1.5}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 1, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 2.0, "grade": "Executed"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 2, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UR", "miss_distance_inches": 7.0, "grade": "Minor Miss"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 3, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "LL", "miss_distance_inches": 10.0, "grade": "Major Miss"}),
            Action(name="WritePitchExecutionGrade", kwargs={"game_pk": 2024000008, "pitch_id": 4, "intended_quadrant_model": "catcher_view_q4_v1", "actual_quadrant": "UL", "miss_distance_inches": 1.8, "grade": "Executed"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000008, "label": "post_game_two_strike_v1", "core_narrative_text": "post_game_two_strike_v1", "gslides_link": "https://slides.example.org/post/2024000008_two_strike", "s3_pdf_path": "s3://reports/scouting/post/2024-08-01_g2024000008_two_strike.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.52}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 6, "insight_text": "stamina_lategame_low", "insight_type": "stamina", "supporting_stat_value": 0.49}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 8, "insight_text": "tendency_chase_low", "insight_type": "tendency", "supporting_stat_value": 0.45}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000008, "timestamp_utc": "2025-08-22T02:30:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_two_strike_v1", "game_pk": 2024000008, "status": "success", "start_time_utc": "2025-08-22T02:29:00Z", "end_time_utc": "2025-08-22T02:31:00Z", "log_s3_path": "s3://workflow-runs/post_game_two_strike_v1/2024000008/2025-08-22T02:29:00Z.log"})
        ],
        outputs=["13"]
    ),

    Task(
        annotator="saaish2",
        user_id="task_101",
        instruction=(
            """
            Handle the delivery of an organization-compliance post-game brief for game 2024000003 that aligns with policy gates and publication standards.

Final acceptance conditions (terminal DB state):
• Ensure the game is confirmed as Final before any post-game entries; this is validated by a manual audit conducted at 2025-08-18T18:10:00Z with title "status_gate_check", message "game_status=Final", suggestion_text "gate_ok", and identical text recorded as operator_note.
• The game's pitch data adheres to the organization's standard pitch-type taxonomy.
• A catcher-view 12×12 location grid is saved with boundaries x∈[-0.95,0.95] ft and z∈[1.5,3.5] ft.
• Conduct trend vetting using policy thresholds (min_pitches=50, min_swings=30, min_bbe=25) with EB shrinkage, FDR q=0.10, and a practical-effect minimum of 0.05.
• Ensure there is a published post-game brief with core narrative "post_game_policy_v1", slide link https://slides.example.org/post/2024000003, and PDF s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf.
• The brief includes exactly four curated insights (order preserved): execution_ff_high [execution, 0.62] for player 4; predictability_sequencing_high [predictability, 0.59] for player 7; situational_risp_high [situational, 0.53] for player 3; tendency_bunt_low [tendency, 0.47] for player 2.
• Tie exactly two coaching playlists to the brief: "Positive Reinforcement" (3 clips) and "Teaching Moments" (3 clips).
• Perform a publication audit (manual) logged at 2025-08-18T18:20:00Z with message "report_published report_id=<the brief's id> draft_status=published", suggestion_text "acknowledge_and_distribute", and the same text recorded as operator note.
• Record a workflow run with dag_name "post_game_policy_v1", status "success", start_time_utc 2025-08-18T18:19:00Z, end_time_utc 2025-08-18T18:21:00Z, and log_s3_path s3://workflow-runs/post_game_policy_v1/2024000003/2025-08-18T18:19:00Z.log.

Return solely the brief’s report id.
            """
        ),
        actions=[
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:10:00Z", "title": "status_gate_check", "message": "game_status=Final", "suggestion_text": "gate_ok", "operator_note": "gate_ok", "is_manual_alert": True}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000003}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000003, "min_x": -0.95, "max_x": 0.95, "min_z": 1.5, "max_z": 3.5, "persist": True}),
            Action(name="FilterTrends", kwargs={"game_pk": 2024000003, "min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1, "min_effect_size": 0.05, "use_eb_shrinkage": True, "control": "FDR"}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "post-game", "game_pk": 2024000003, "label": "post_game_policy_v1", "core_narrative_text": "post_game_policy_v1", "gslides_link": "https://slides.example.org/post/2024000003", "s3_pdf_path": "s3://reports/scouting/post/2024-07-22_g2024000003_post.pdf", "draft_status": "published"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 4, "insight_text": "execution_ff_high", "insight_type": "execution", "supporting_stat_value": 0.62}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 7, "insight_text": "predictability_sequencing_high", "insight_type": "predictability", "supporting_stat_value": 0.59}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 3, "insight_text": "situational_risp_high", "insight_type": "situational", "supporting_stat_value": 0.53}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 2, "insight_text": "tendency_bunt_low", "insight_type": "tendency", "supporting_stat_value": 0.47}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Positive Reinforcement", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000003, "timestamp_utc": "2025-08-18T18:20:00Z", "title": "publication_audit", "message": "report_published report_id=13 draft_status=published", "suggestion_text": "acknowledge_and_distribute", "operator_note": "acknowledge_and_distribute", "is_manual_alert": True}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "post_game_policy_v1", "game_pk": 2024000003, "status": "success", "start_time_utc": "2025-08-18T18:19:00Z", "end_time_utc": "2025-08-18T18:21:00Z", "log_s3_path": "s3://workflow-runs/post_game_policy_v1/2024000003/2025-08-18T18:19:00Z.log"})
        ],
        outputs=[
            "13"
        ]
    ),

    Task(
        annotator="saaish2",
        user_id="task_102",
        instruction=(
            """
            Assist with in-game comms for gamePk 2024000012 (Scheduled). Your task is to ensure the game’s alerting and auditing state aligns with policy—having one high-priority manual alert documented for the game, leveraging calculations recomputed at the strict >1.5 threshold, and deterministic audit artifacts captured—without defining the means to achieve it.

Terminal acceptance outcome (results only):
• The event ledger for this game documents exactly one high-priority manual alert with suggestion_text='shift outfield two steps opposite field', is_manual_alert=true, draft_status='published', leverage_index=1.6, timestamp_utc='2025-08-14T00:00:00Z'.
• There is a leverage summary for the game using threshold=1.5 (rigorous high-leverage policy).
• Ensure audit artifacts are recorded for this operation: an ingestion log (source_name='in_game_alert_manual', status_code=200, records_ingested=1, request_timestamp_utc='2025-08-14T00:00:00Z') and a workflow run record (dag_name='in_game_alert', game_pk=2024000012, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:02:00Z', log_s3_path='s3://workflow/in_game_alert/2024000012/log.json').
            """
        ),
        actions=[
            Action(name="GetGameDetails", kwargs={"game_pk": 2024000012}),
            Action(name="ListGameDayEvents", kwargs={"game_pk": 2024000012}),
            Action(name="CreateManualAlertEvent", kwargs={
                "game_pk": 2024000012,
                "suggestion_text": "shift outfield two steps opposite field",
                "leverage_index": 1.6,
                "draft_status": "published",
                "is_manual_alert": True,
                "timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000012, "threshold": 1.5}),
            Action(name="LogIngestionEvent", kwargs={
                "source_name": "in_game_alert_manual",
                "status_code": 200,
                "records_ingested": 1,
                "request_timestamp_utc": "2025-08-14T00:00:00Z"
            }),
            Action(name="LogWorkflowRun", kwargs={
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
            """
            Take charge of the weekly development cycle for player_id=8 (James Brown). Your goal is to produce a finalized one-page development brief and get a micro-goal approved, attach the two requisite development review playlists, maintain the organization’s trend-filter policy, and document a deterministic run log. Acceptance condition: a new development brief should be available for week_of_date='2025-08-11' at s3://reports/player_dev/8/2025-08-11.pdf; an approved micro-goal should be in place for that brief with goal_text='increase_slider_usage_3pct', coach_id=902, target_review_date='2025-08-18'; the brief must be accompanied by exactly two playlists — 'Positive Reinforcement' (clip_count=4, link 'https://portal.internal/videos/report/11/positive') and 'Teaching Moments' (clip_count=3, link 'https://portal.internal/videos/report/11/teaching'); trend filter parameters should be preserved exactly as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10; and a workflow run needs to be logged with dag_name='player_dev', status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:01:00Z', log_s3_path='s3://workflow/player_dev/8/2025-08-11/log.json'.
            """
        ),
        actions=[
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 8, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/8/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 11, "player_id": 8, "goal_text": "increase_slider_usage_3pct", "coach_id": 902, "target_review_date": "2025-08-18"}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/11/positive"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/11/teaching"}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "player_dev", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:01:00Z", "log_s3_path": "s3://workflow/player_dev/8/2025-08-11/log.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_104",
        instruction=(
            """
            Oversee the pre-game scouting deliverable for team_id=6 for the next game scheduled on or after 2024-08-30. The goal is to produce the artifact that adheres to the org’s Pre-Game Package Spec v1 and data-prep policy, ensuring a single unambiguous terminal state.

Acceptance conditions (terminal state only — articulate outcomes, not steps):
• The next scheduled game is resolved, and the opponent for team 6 is pinpointed.
• Exactly one pre-game scouting report should be present for that game with report_type='pre-game', s3_pdf_path='s3://reports/scouting/pre/2024-08-31_g2024000004_team6.pdf', gslides_link='https://slides.example.org/pre/2024000004', core_narrative_text='pre_game_policy_v1'.
• There should be exactly one curated insight attached to that report: (player_id=5, insight_type='tendency', insight_text='tendency_firstpitchstrike_low', supporting_stat_value=0.321).
• Two video playlists are to be available for that report — 'Opponent Pitcher Tendencies' (clip_count=4, link 'https://portal.internal/videos/report/13/tendencies_pre') and 'Opponent Miss Locations' (clip_count=3, link 'https://portal.internal/videos/report/13/miss_locations_pre').
• Pitch types for that game must be in the canonical schema, and a 12×12 catcher-view grid representation of plate_x/plate_z should be generated with bounds -2.0..2.0 (x) and 0.0..4.0 (z) without storing the grid.
• Trend filtering parameters must be preserved as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.
• A single workflow run record must exist with dag_name='pre_game', game_pk=2024000004, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:05:00Z', log_s3_path='s3://workflow/pre_game/2024000004/log.json'.
            """
        ),
        actions=[
            Action(name="FindNextScheduledGame", kwargs={"current_date": "2024-08-30"}),
            Action(name="GetOpponentForTeamInGame", kwargs={"game_pk": 2024000004, "team_id": 6}),
            Action(name="CanonicalizePitchTypes", kwargs={"game_pk": 2024000004}),
            Action(name="GridEncodePitchLocations", kwargs={"game_pk": 2024000004, "min_x": -2.0, "max_x": 2.0, "min_z": 0.0, "max_z": 4.0, "persist": False}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="CreateScoutingReport", kwargs={"report_type": "pre-game", "game_pk": 2024000004, "s3_pdf_path": "s3://reports/scouting/pre/2024-08-31_g2024000004_team6.pdf", "gslides_link": "https://slides.example.org/pre/2024000004", "core_narrative_text": "pre_game_policy_v1"}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 13, "player_id": 5, "insight_text": "tendency_firstpitchstrike_low", "insight_type": "tendency", "supporting_stat_value": 0.321}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Opponent Pitcher Tendencies", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/13/tendencies_pre"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 13, "playlist_name": "Opponent Miss Locations", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/13/miss_locations_pre"}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "pre_game", "game_pk": 2024000004, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:05:00Z", "log_s3_path": "s3://workflow/pre_game/2024000004/log.json"})
        ],
        outputs=[]
    ),

    Task(
        annotator="saaish2",
        user_id="task_105",
        instruction=(
            """
            Handle the off-day two-player development roll-up for team_id=10. Aim to complete finalized one-page briefs and get approval for micro-goals for both active players in that roster snapshot. Ensure the organization’s trend-filter policy is adhered to (min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10), supply the necessary review playlists, and document this week’s process.

Final acceptance state (outcomes only):
• The database holds two finalized development briefs for week_of_date='2025-08-11' located at s3://reports/player_dev/7/2025-08-11.pdf and s3://reports/player_dev/9/2025-08-11.pdf.
• Each respective micro-goal is included and approved: for player_id=7, goal_text='improve_two_strike_battle_rate' with coach_id=501 and target_review_date='2025-08-18'; for player_id=9, goal_text='tighten_inner_third_swing_decisions' with coach_id=501 and target_review_date='2025-08-18'.
• The organization's trend filter settings are maintained exactly as min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.10.
• Each brief is linked to precisely two review playlists: for the brief related to dev_report_id=11 → 'Positive Reinforcement' (clip_count=3, link https://portal.internal/videos/report/11/positive) and 'Teaching Moments' (clip_count=2, link https://portal.internal/videos/report/11/teaching); for the brief related to dev_report_id=12 → 'Positive Reinforcement' (clip_count=4, link https://portal.internal/videos/report/12/positive) and 'Teaching Moments' (clip_count=3, link https://portal.internal/videos/report/12/teaching).
• Document a weekly process that confirms a successful run with dag_name='weekly_dev', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:04:00Z', and log_s3_path='s3://workflow/weekly_dev/2025-08-11/log.json'.
            """
        ),
        actions=[
            Action(name="GetActiveRoster", kwargs={"team_id": 10, "include_il": False}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "improve_two_strike_battle_rate", "coach_id": 501, "target_review_date": "2025-08-18"}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 20}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "tighten_inner_third_swing_decisions", "coach_id": 501, "target_review_date": "2025-08-18"}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 21}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/11/positive"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 2, "internal_portal_link": "https://portal.internal/videos/report/11/teaching"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 4, "internal_portal_link": "https://portal.internal/videos/report/12/positive"}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3, "internal_portal_link": "https://portal.internal/videos/report/12/teaching"}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.10}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "weekly_dev", "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:04:00Z", "log_s3_path": "s3://workflow/weekly_dev/2025-08-11/log.json"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_106",
        instruction=(
            """
            As the analytics coordinator, enhance the existing pre-game package tied to report_id=8 in a deterministic manner. Terminal acceptance criteria:
1) There are exactly two additional curated insights on report_id=8 with these precise fields: (player_id=2, insight_text='tendency_chaserate_high', insight_type='tendency', supporting_stat_value=0.412) and (player_id=11, insight_text='predictability_firstpitchswing_low', insight_type='predictability', supporting_stat_value=0.193). The insight_texts must conform to '{category}_{metric}_{bucket}' using only lowercase letters/digits in each token.
2) Attach one new playlist to report_id=8 with playlist_name='Scouting Focus: Top 5 ABs', internal_portal_link='https://portal.example.org/videos/report/8/focus_top5', clip_count=5.
3) Ensure a leverage summary is retained for game_pk=2024000001 with threshold=1.5.
4) Have one pre-game note in place for game_pk=2024000001 with suggestion_text='Travel & rest plan confirmed', leverage_index=0.0, draft_status='archived'.
5) Log one workflow execution with dag_name='pre_game_curations', game_pk=2024000001, status='success', start_time_utc='2025-08-14T00:00:00Z', end_time_utc='2025-08-14T00:10:00Z', log_s3_path='s3://logs/pre_game/2024000001/curations_run.log'.
6) Ensure there is one ingestion log for source_name='pre_game_curations_assets', status_code=200, records_ingested=27, request_timestamp_utc='2025-08-14T00:26:00Z'.
All arguments must be clearly stated; no hidden defaults are allowed.
            """
        ),
        actions=[
            Action(name="AddCuratedInsight", kwargs={"report_id": 8, "player_id": 2, "insight_text": "tendency_chaserate_high", "insight_type": "tendency", "supporting_stat_value": 0.412}),
            Action(name="AddCuratedInsight", kwargs={"report_id": 8, "player_id": 11, "insight_text": "predictability_firstpitchswing_low", "insight_type": "predictability", "supporting_stat_value": 0.193}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 8, "playlist_name": "Scouting Focus: Top 5 ABs", "internal_portal_link": "https://portal.example.org/videos/report/8/focus_top5", "clip_count": 5}),
            Action(name="ComputeGameLeverageSummary", kwargs={"game_pk": 2024000001, "threshold": 1.5}),
            Action(name="CreateManualAlertEvent", kwargs={"game_pk": 2024000001, "suggestion_text": "Travel & rest plan confirmed", "leverage_index": 0.0, "draft_status": "archived", "is_manual_alert": True}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "pre_game_curations", "game_pk": 2024000001, "status": "success", "start_time_utc": "2025-08-14T00:00:00Z", "end_time_utc": "2025-08-14T00:10:00Z", "log_s3_path": "s3://logs/pre_game/2024000001/curations_run.log"}),
            Action(name="LogIngestionEvent", kwargs={"source_name": "pre_game_curations_assets", "status_code": 200, "records_ingested": 27, "request_timestamp_utc": "2025-08-14T00:26:00Z"})
        ],
        outputs=[]
    ),


    Task(
        annotator="saaish2",
        user_id="task_107",
        instruction=(
            """
            As the coordinator for pitching development, handle the finalization of a weekly development snapshot for Twins hitters Alexander Taylor (player_id=7) and Charlotte Johnson (player_id=9) for week_of_date='2025-08-11'. Acceptance criteria (single terminal state):
1) Ensure the creation of two new player development reports with precise fields: (player_id=7, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/7/2025-08-11.pdf') and (player_id=9, week_of_date='2025-08-11', s3_pdf_path='s3://reports/player_dev/9/2025-08-11.pdf').
2) A new development goal for player_id=7 must be linked to the new dev report with the goal_text='Improve swing decisions (OOZ chase -5pp)', coach_id=501, target_review_date='2025-08-18' and goal_status='Proposed'.
3) A new development goal for player_id=9 must be linked to the new dev report with the goal_text='Elevate hard-hit% (95+ EV +3pp)', coach_id=502, target_review_date='2025-08-18' and goal_status='Proposed'.
4) Update existing goal_id=19 to goal_status='Approved'.
5) Ensure persistence of trend filtering parameters with min_pitches=50, min_swings=30, min_bbe=25, fdr_threshold=0.1.
6) For each of the two new player development reports, there should be exactly two playlists with policy-conforming clip counts: 'Positive Reinforcement' (clip_count=4) and 'Teaching Moments' (clip_count=3).
7) Log a workflow run with dag_name='weekly_dev_reports', status='success', start_time_utc='2025-08-14T01:00:00Z', end_time_utc='2025-08-14T01:08:00Z', log_s3_path='s3://logs/dev/2025-08-11/weekly_run.log'.
Explicit arguments only; no hidden defaults.
            """
        ),
        actions=[
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 7, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/7/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevReport", kwargs={"player_id": 9, "week_of_date": "2025-08-11", "s3_pdf_path": "s3://reports/player_dev/9/2025-08-11.pdf"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 11, "player_id": 7, "goal_text": "Improve swing decisions (OOZ chase -5pp)", "coach_id": 501, "target_review_date": "2025-08-18", "goal_status": "Proposed"}),
            Action(name="CreatePlayerDevGoal", kwargs={"dev_report_id": 12, "player_id": 9, "goal_text": "Elevate hard-hit% (95+ EV +3pp)", "coach_id": 502, "target_review_date": "2025-08-18", "goal_status": "Proposed"}),
            Action(name="ApprovePlayerDevGoal", kwargs={"goal_id": 19}),
            Action(name="FilterTrends", kwargs={"min_pitches": 50, "min_swings": 30, "min_bbe": 25, "fdr_threshold": 0.1}),
            # Dev report playlists (policy-enforced names and clip counts)
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 11, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Positive Reinforcement", "clip_count": 4}),
            Action(name="CreateVideoPlaylist", kwargs={"report_id": 12, "playlist_name": "Teaching Moments", "clip_count": 3}),
            Action(name="LogWorkflowRun", kwargs={"dag_name": "weekly_dev_reports", "status": "success", "start_time_utc": "2025-08-14T01:00:00Z", "end_time_utc": "2025-08-14T01:08:00Z", "log_s3_path": "s3://logs/dev/2025-08-11/weekly_run.log"})
        ],
        outputs=[]
    ),

]
