
tasks = [
    {
        "annotator": 0,
        "user_id": "task1",
        "instruction": "Handle the responsibilities of the official scouting representative.. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', compile a pre-series scouting package that meets all required policy outcomes: create a per-pitcher insight set (five distinct policy-defined categories using deterministic templates with computed metric values); generate a persisted PDF report and a single video playlist linked by internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; make sure to distribute this to '#coaches-prep'; and log a readiness record under source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task2",
        "instruction": "Serve in the role of the official scouting representative.. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', deliver a pre-series scouting bundle that fulfills policy outcomes: a per-pitcher insight set (5 policy-defined types using deterministic templates with metric values derived from your computed metrics); a persisted PDF report and one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; distribute to '#coaches-prep'; and include a readiness log with source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Provide back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task3",
        "instruction": "Act as the pre-series analytics agent for the club.. For gamePk '2024000186' on date '2024-12-06', establish comprehensive in-game monitoring with real-time alerts (leverage_index 2.8, is_manual_alert False, suggestion_text 'situational response'), validate spatial data tracking with artifact '12x12_catcher_view' quality control, certify model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 88), and complete the monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000186"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-06"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-06"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000186",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000186",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000186",
                    "leverage_index": 2.8,
                    "is_manual_alert": false,
                    "suggestion_text": "situational response"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 88
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000186"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task4",
        "instruction": "Lead as the home club's analytics head.. Provide a pre-series scouting bundle for opponent team id 13 on date '2024-12-15' with gamePk '2024000195'. The package should fulfill these acceptance criteria: pitcher 101 has 5 observations (tendency_fastball_usage_0.62, execution_called_strike_rate_0.63, stamina_pitch_count_102, situational_pressure_era_3.3, predictability_location_score_0.47); pitcher 102 has 5 observations (tendency_changeup_usage_0.24, execution_contact_rate_0.71, stamina_pitch_count_95, situational_clutch_ops_0.718, predictability_approach_score_0.54); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'scouting_complete' (status_code 200, logs_ingested 49). Provide back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-15"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000195",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.63",
                    "supporting_stat_value": 0.63,
                    "game_pk": "2024000195",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_102",
                    "supporting_stat_value": 102,
                    "game_pk": "2024000195",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_era_3.3",
                    "supporting_stat_value": 3.3,
                    "game_pk": "2024000195",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.47",
                    "supporting_stat_value": 0.47,
                    "game_pk": "2024000195",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.24",
                    "supporting_stat_value": 0.24,
                    "game_pk": "2024000195",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.71",
                    "supporting_stat_value": 0.71,
                    "game_pk": "2024000195",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000195",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.718",
                    "supporting_stat_value": 0.718,
                    "game_pk": "2024000195",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.54",
                    "supporting_stat_value": 0.54,
                    "game_pk": "2024000195",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000195",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000195-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000195-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000195/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000195-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "scouting_complete",
                    "status_code": 200,
                    "logs_ingested": 49
                }
            }
        ],
        "outputs": [
                "RPT-2024000195-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task5",
        "instruction": "Assume responsibility for preparing the official scouting material.. Provide a pre-series scouting bundle for opponent team id 13 on date '2024-12-17' with gamePk '2024000197'. The package should fulfill these acceptance criteria: pitcher 101 has 5 observations (tendency_slider_usage_0.35, execution_swing_miss_rate_0.39, stamina_pitch_count_97, situational_lefty_era_4.9, predictability_velocity_score_0.43); pitcher 102 has 5 observations (tendency_curveball_usage_0.21, execution_strike_zone_rate_0.76, stamina_pitch_count_104, situational_runners_on_ops_0.759, predictability_timing_score_0.36); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'final_analysis' (status_code 200, logs_ingested 51). Provide back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-17"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.35",
                    "supporting_stat_value": 0.35,
                    "game_pk": "2024000197",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.39",
                    "supporting_stat_value": 0.39,
                    "game_pk": "2024000197",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_97",
                    "supporting_stat_value": 97,
                    "game_pk": "2024000197",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_era_4.9",
                    "supporting_stat_value": 4.9,
                    "game_pk": "2024000197",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.43",
                    "supporting_stat_value": 0.43,
                    "game_pk": "2024000197",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.21",
                    "supporting_stat_value": 0.21,
                    "game_pk": "2024000197",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_zone_rate_0.76",
                    "supporting_stat_value": 0.76,
                    "game_pk": "2024000197",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_104",
                    "supporting_stat_value": 104,
                    "game_pk": "2024000197",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runners_on_ops_0.759",
                    "supporting_stat_value": 0.759,
                    "game_pk": "2024000197",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.36",
                    "supporting_stat_value": 0.36,
                    "game_pk": "2024000197",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000197",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000197-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000197-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000197/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000197-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "final_analysis",
                    "status_code": 200,
                    "logs_ingested": 51
                }
            }
        ],
        "outputs": [
                "RPT-2024000197-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task6",
        "instruction": "Serving as the analytics liaison for the home organization, prepare a pre-series scouting package for opponent team id 13 on '2024-12-03' with gamePk '2024000183'. The package must adhere to these acceptance criteria: pitcher 101 includes 5 observations (tendency_cutter_usage_0.31, execution_whiff_rate_0.37, stamina_pitch_count_94, situational_bases_loaded_era_3.1, predictability_velocity_score_0.57); pitcher 102 contains 5 observations (tendency_fastball_usage_0.66, execution_strike_zone_rate_0.72, stamina_pitch_count_109, situational_lefty_ops_0.649, predictability_release_score_0.44); ensure internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' is included with clip_count 1; and record an ingestion log entry with source_name 'analytics_prep' (status_code 200, logs_ingested 37). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-03"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000183",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.37",
                    "supporting_stat_value": 0.37,
                    "game_pk": "2024000183",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_94",
                    "supporting_stat_value": 94,
                    "game_pk": "2024000183",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_3.1",
                    "supporting_stat_value": 3.1,
                    "game_pk": "2024000183",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.57",
                    "supporting_stat_value": 0.57,
                    "game_pk": "2024000183",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.66",
                    "supporting_stat_value": 0.66,
                    "game_pk": "2024000183",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_zone_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000183",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_109",
                    "supporting_stat_value": 109,
                    "game_pk": "2024000183",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.649",
                    "supporting_stat_value": 0.649,
                    "game_pk": "2024000183",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.44",
                    "supporting_stat_value": 0.44,
                    "game_pk": "2024000183",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000183",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000183-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000183-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000183/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000183-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "analytics_prep",
                    "status_code": 200,
                    "logs_ingested": 37
                }
            }
        ],
        "outputs": [
                "RPT-2024000183-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task7",
        "instruction": "Designated as the official scouting representative, assemble the pre-series scouting bundle for opponent team id 13 on '2024-07-24' with gamePk '2024000013' in line with policy: create per-pitcher insight sets (five required categories using deterministic templates and computed values); save both a PDF report and one video playlist at 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; distribute to '#coaches-prep'; and generate a readiness log with source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Report back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task8",
        "instruction": "Functioning as the designated scouting liaison, compile the required pre-series scouting deliverables for opponent team id 13 on '2024-07-24' with gamePk '2024000013': construct per-pitcher insights (five official categories using deterministic methods); record a PDF report and one video playlist (internal_portal_link 'portal://playlist/opponent_pitcher_tendencies', clip_count 1); submit to '#coaches-prep'; and ensure a readiness log entry exists (source_name 'dq_pre_series_day2', status_code 200, logs_ingested 0). Submit the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task9",
        "instruction": "Engaged as the official analytics resource for this club, deliver an in-game monitoring result for gamePk '2024000056' on '2024-09-16' that meets these standards: one logged alert with leverage_index 2.1, is_manual_alert True, suggestion_text 'bullpen activation'; keep live pitch tracking normalized, shown by the persisted artifact '12x12_catcher_view' and a passed quality check; confirm models for that date are certified fresh; ensure an ingestion log entry with source_name 'real_time_feed' (status_code 200, logs_ingested 75); and mark the real-time monitoring flow as complete. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000056"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-16"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-16"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000056",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000056",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000056",
                    "leverage_index": 2.1,
                    "is_manual_alert": true,
                    "suggestion_text": "bullpen activation"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "real_time_feed",
                    "status_code": 200,
                    "logs_ingested": 75
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000056"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task10",
        "instruction": "Act as the recognized analytics agent for the home squad, for opponent team id 10 on '2024-09-27' with gamePk '2024000067', create and distribute a pre-series scouting intelligence package with advanced statistical analysis using min_sample_size 40. Employ internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Post to channel '#coaches-prep' and provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task11",
        "instruction": "As the designated analytics operator for this club.. For gamePk '2024000158' on '2024-11-08', handle in-game monitoring that includes: real-time alerts (leverage_index 1.9, is_manual_alert False, suggestion_text 'pitch count awareness'), conduct spatial data artifact '12x12_catcher_view' QC validation, ensure model freshness certification, and log ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 54). Complete the workflow and return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000158"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-08"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-08"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000158",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000158",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000158",
                    "leverage_index": 1.9,
                    "is_manual_alert": false,
                    "suggestion_text": "pitch count awareness"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 54
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000158"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task12",
        "instruction": "In your role as the recognized scouting analytics agent.. For opponent team id 10 on the date '2024-09-27' with gamePk '2024000067', coordinate the creation of a pre-series scouting intelligence deliverable, applying statistical filters with a min_sample_size of 40. Produce one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Share results to '#coaches-prep' and provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task13",
        "instruction": "Operating as the official scouting delegate.. For opponent team id 13 on '2024-07-24' with gamePk '2024000013', compile a pre-series scouting package meeting all policy requirements: create a per-pitcher insight set (5 mandatory categories using deterministic templates with computed metric values); generate and save a PDF report plus one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; distribute results to '#coaches-prep'; and log readiness with source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task14",
        "instruction": "As the analytics lead for the home club.. For gamePk '2024000184' on '2024-12-04', initiate comprehensive in-game monitoring with provisions for real-time alerts (leverage_index 1.6, is_manual_alert False, suggestion_text 'execution monitoring'), validate quality for spatial data tracking artifact '12x12_catcher_view', ensure model freshness certification, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 62), and complete the workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000184"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-04"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-04"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000184",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000184",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000184",
                    "leverage_index": 1.6,
                    "is_manual_alert": false,
                    "suggestion_text": "execution monitoring"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 62
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000184"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task15",
        "instruction": "As the party responsible for scouting materials.. For gamePk '2024000180' on '2024-11-30', commence comprehensive in-game monitoring with real-time alert capabilities (leverage_index 3.0, is_manual_alert False, suggestion_text 'situational awareness'), quality validation for spatial data tracking artifact '12x12_catcher_view', confirm model freshness certification, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 99), and complete the monitoring workflow. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000180"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-30"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-30"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000180",
                    "time_window": "pitches_live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000180",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000180",
                    "leverage_index": 3.0,
                    "is_manual_alert": false,
                    "suggestion_text": "situational awareness"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 99
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000180"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task16",
        "instruction": "Handle the responsibility as the official scouting contact point. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', assemble a pre-series scouting deliverable that adheres to policy standards: develop per-pitcher insight sets (five essential categories with deterministic templates and calculated metric values); generate and save a PDF report along with a single video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; share to '#coaches-prep'; and log readiness with source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Output the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task17",
        "instruction": "Function as the appointed pre-series analytics contact for the club. For opponent team id 7 on '2024-07-25' with gamePk '2024000004', coordinate and communicate a pre-series scouting bundle with persistently stored deliverables. Incorporate a video playlist via internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Post the results to '#coaches-prep'. Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 7
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-25"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000004",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000004",
                    "s3_pdf_path": "s3://reports/2024000004/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000004-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000004-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000004/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000004-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000004-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task18",
        "instruction": "Fill the role of home team analytics representative. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', create a pre-series scouting package supported by advanced statistics requiring min_sample_size 40. A single video playlist must be provided via internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' (clip_count 1). Distribute the outcome to '#coaches-prep' and provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task19",
        "instruction": "Serve as the official analytics liaison. For opponent team id 7 on '2024-07-25' with gamePk '2024000004', compile a pre-series scouting package with stored artifacts. Deliver one playlist through internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1, share it in '#coaches-prep', and provide back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 7
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-25"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000004",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000004",
                    "s3_pdf_path": "s3://reports/2024000004/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000004-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000004-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000004/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000004-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000004-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task20",
        "instruction": "Operate as the recognized analytics agent for the home team. Provide a pre-series scouting bundle for opponent team id 13 on date '2024-11-29' with gamePk '2024000179'. Ensure the package meets these criteria: pitcher 101 has 5 observations (tendency_changeup_usage_0.27, execution_zone_rate_0.75, stamina_pitch_count_107, situational_lefty_era_4.6, predictability_velocity_score_0.42); pitcher 102 has 5 observations (tendency_curveball_usage_0.15, execution_first_strike_rate_0.67, stamina_pitch_count_98, situational_clutch_ops_0.798, predictability_location_score_0.51); include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'scout_report' (status_code 200, logs_ingested 33). Give back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-29"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.27",
                    "supporting_stat_value": 0.27,
                    "game_pk": "2024000179",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.75",
                    "supporting_stat_value": 0.75,
                    "game_pk": "2024000179",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_107",
                    "supporting_stat_value": 107,
                    "game_pk": "2024000179",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_era_4.6",
                    "supporting_stat_value": 4.6,
                    "game_pk": "2024000179",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.42",
                    "supporting_stat_value": 0.42,
                    "game_pk": "2024000179",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.15",
                    "supporting_stat_value": 0.15,
                    "game_pk": "2024000179",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.67",
                    "supporting_stat_value": 0.67,
                    "game_pk": "2024000179",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_98",
                    "supporting_stat_value": 98,
                    "game_pk": "2024000179",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.798",
                    "supporting_stat_value": 0.798,
                    "game_pk": "2024000179",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.51",
                    "supporting_stat_value": 0.51,
                    "game_pk": "2024000179",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000179",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000179-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000179-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000179/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000179-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "scout_report",
                    "status_code": 200,
                    "logs_ingested": 33
                }
            }
        ],
        "outputs": [
                "RPT-2024000179-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task21",
        "instruction": "Handle the role as the home squad\u2019s scouting analytics contact.. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', assemble a pre-series scouting report package. Apply advanced statistical analysis using min_sample_size 40. Deliver one playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' (clip_count 1). Send to '#coaches-prep' and return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task22",
        "instruction": "Coordinate operations as the official scouting representative.. Provide a pre-series scouting bundle for opponent team id 13 on date '2024-10-03' with gamePk '2024000073'. The package should meet these acceptance criteria: pitcher 101 has 5 observations (tendency_curveball_usage_0.18, execution_first_strike_rate_0.61, stamina_pitch_count_97, situational_bases_loaded_era_4.1, predictability_pattern_score_0.38); pitcher 102 has 5 observations (tendency_changeup_usage_0.24, execution_zone_rate_0.74, stamina_pitch_count_89, situational_late_inning_ops_0.683, predictability_timing_score_0.67); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'tactical_prep' (status_code 200, logs_ingested 12). Give back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-10-03"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.18",
                    "supporting_stat_value": 0.18,
                    "game_pk": "2024000073",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.61",
                    "supporting_stat_value": 0.61,
                    "game_pk": "2024000073",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_97",
                    "supporting_stat_value": 97,
                    "game_pk": "2024000073",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_4.1",
                    "supporting_stat_value": 4.1,
                    "game_pk": "2024000073",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.38",
                    "supporting_stat_value": 0.38,
                    "game_pk": "2024000073",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.24",
                    "supporting_stat_value": 0.24,
                    "game_pk": "2024000073",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.74",
                    "supporting_stat_value": 0.74,
                    "game_pk": "2024000073",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_89",
                    "supporting_stat_value": 89,
                    "game_pk": "2024000073",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_ops_0.683",
                    "supporting_stat_value": 0.683,
                    "game_pk": "2024000073",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.67",
                    "supporting_stat_value": 0.67,
                    "game_pk": "2024000073",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000073",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000073-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000073-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000073/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000073-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_prep",
                    "status_code": 200,
                    "logs_ingested": 12
                }
            }
        ],
        "outputs": [
                "RPT-2024000073-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task23",
        "instruction": "Conduct duties as the pre-series analytics agent for the club.. For opponent team id 7 on date '2024-07-25' with gamePk '2024000004', generate and distribute a pre-series scouting bundle with persisted artifacts. Use internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Post to '#coaches-prep'. Give back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 7
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-25"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000004",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000004",
                    "s3_pdf_path": "s3://reports/2024000004/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000004-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000004-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000004/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000004-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000004-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task24",
        "instruction": "Manage responsibilities in the role of the home club\u2019s analytics lead.. For opponent team id 8 on date '2024-09-23' and gamePk '2024000063', deliver a pre-series report that satisfies policy outcomes when no probable pitchers are returned: zero curated observations and no video clips using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 0; a persisted PDF report; distribution to '#coaches-prep'; a loged workflow run for the package; and a 'verification_check' log (status_code 200, logs_ingested 0). Give back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 8
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-23"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_table"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "pitches_canonical",
                        "key_metrics",
                        "flags_leverage"
                    ]
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": [],
                    "game_pk": "2024000063",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000063",
                    "s3_pdf_path": "s3://reports/2024000063/pre-series_report.pdf",
                    "insights_data": [],
                    "video_data": []
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000063-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 0
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000063-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000063/pre-series_report.pdf",
                    "playlist_links": [],
                    "report_id": "RPT-2024000063-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "verification_check",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000063-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task25",
        "instruction": "Oversee preparation of the official scouting material.. For gamePk '2024000160' on date '2024-11-10', establish comprehensive in-game monitoring with real-time alerts (leverage_index 3.1, is_manual_alert False, suggestion_text 'substitution analysis'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 87), and complete monitoring workflow lifecycle. Give back 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000160"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-10"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-10"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000160",
                    "time_window": "pitches_live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000160",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000160",
                    "leverage_index": 3.1,
                    "is_manual_alert": false,
                    "suggestion_text": "substitution analysis"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 87
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000160"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task26",
        "instruction": "Act as the analytics liaison for the home organization. For gamePk '2024000088' on date '2024-10-14', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 1.7, is_manual_alert False, suggestion_text 'velocity tracking'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 88), and conclude the complete monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000088"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-10-14"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-10-14"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000088",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000088",
                    "leverage_index": 1.7,
                    "is_manual_alert": false,
                    "suggestion_text": "velocity tracking"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 88
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000088"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task27",
        "instruction": "Function as the team\u2019s scouting and analytics agent. For gamePk '2024000176' on date '2024-11-26', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 2.4, is_manual_alert False, suggestion_text 'tactical adjustment'), spatial data tracking using artifact '12x12_catcher_view' for quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 71), and complete the monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000176"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-26"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-26"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000176",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000176",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000176",
                    "leverage_index": 2.4,
                    "is_manual_alert": false,
                    "suggestion_text": "tactical adjustment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 71
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000176"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task28",
        "instruction": "Serve as the analytics coordinator for the home side. Deliver a pre-series scouting package for opponent team id 13 on date '2024-12-09' with gamePk '2024000189'. Ensure the package fulfills these acceptance criteria: pitcher 101 with 5 observations (tendency_curveball_usage_0.22, execution_contact_rate_0.65, stamina_pitch_count_105, situational_day_game_era_4.1, predictability_location_score_0.35); pitcher 102 with 5 observations (tendency_changeup_usage_0.29, execution_first_strike_rate_0.74, stamina_pitch_count_89, situational_clutch_ops_0.786, predictability_approach_score_0.58); guarantee the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and register a log entry with source_name 'advanced_metrics' (status_code 200, logs_ingested 43). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-09"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.22",
                    "supporting_stat_value": 0.22,
                    "game_pk": "2024000189",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000189",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_105",
                    "supporting_stat_value": 105,
                    "game_pk": "2024000189",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_day_game_era_4.1",
                    "supporting_stat_value": 4.1,
                    "game_pk": "2024000189",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.35",
                    "supporting_stat_value": 0.35,
                    "game_pk": "2024000189",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.29",
                    "supporting_stat_value": 0.29,
                    "game_pk": "2024000189",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.74",
                    "supporting_stat_value": 0.74,
                    "game_pk": "2024000189",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_89",
                    "supporting_stat_value": 89,
                    "game_pk": "2024000189",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.786",
                    "supporting_stat_value": 0.786,
                    "game_pk": "2024000189",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000189",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000189",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000189-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000189-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000189/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000189-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "advanced_metrics",
                    "status_code": 200,
                    "logs_ingested": 43
                }
            }
        ],
        "outputs": [
                "RPT-2024000189-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task29",
        "instruction": "Serve as the official analytics resource for this club. For gamePk '2024000066' on date '2024-09-26', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 1.8, is_manual_alert False, suggestion_text 'pitcher fatigue check'), spatial data tracking via artifact '12x12_catcher_view' for quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 65), and close the complete monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000066"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-26"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-26"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000066",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000066",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000066",
                    "leverage_index": 1.8,
                    "is_manual_alert": false,
                    "suggestion_text": "pitcher fatigue check"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 65
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000066"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task30",
        "instruction": "Function as the official scouting liaison. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', compile the pre-series scouting package in accordance with policy: create per-pitcher insight bundles (five designated types using deterministic templates and computed values); maintain a PDF report and one video playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' and clip_count 1; distribute through '#coaches-prep'; and incorporate a readiness log from source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task31",
        "instruction": "Handle the role of real-time analytics coordinator.. For gamePk '2024000202' on date '2024-12-22', organize comprehensive in-game monitoring which includes a system alert (leverage_index 3.5, is_manual_alert False, suggestion_text 'focus on defensive alignment'), validated catcher-view artifact, model freshness run, ingestion log confirmation (source_name 'in_game_snapshot', status_code 200, logs_ingested 93), and ensure the completion of the in-game flow. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000202"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-22"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-22"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000202",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000202",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000202",
                    "leverage_index": 3.5,
                    "is_manual_alert": false,
                    "suggestion_text": "focus on defensive alignment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 93
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000202"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task32",
        "instruction": "Coordinate as the designated analytics coordinator for this club. For gamePk '2024000067' on date '2024-09-27', initiate in-game monitoring with real-time alerts (leverage_index 2.0, is_manual_alert True, suggestion_text 'bullpen readiness check'), validate spatial data artifact '12x12_catcher_view', verify model freshness, log ingestion activity (source_name 'in_game_snapshot', status_code 200, logs_ingested 70), and conclude the monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000067"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-27"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-27"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000067",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000067",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000067",
                    "leverage_index": 2.0,
                    "is_manual_alert": true,
                    "suggestion_text": "bullpen readiness check"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 70
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000067"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task33",
        "instruction": "Serve as the pre-series analytics agent for the club.. Deliver a pre-series scouting bundle for opponent team id 13 on date '2024-11-13' with gamePk '2024000163'. The package should fulfill these acceptance criteria: pitcher 101 has 5 observations (tendency_slider_usage_0.31, execution_whiff_rate_0.35, stamina_pitch_count_88, situational_clutch_era_2.7, predictability_timing_score_0.53); pitcher 102 has 5 observations (tendency_cutter_usage_0.27, execution_zone_rate_0.69, stamina_pitch_count_112, situational_runner_scoring_ops_0.748, predictability_velocity_score_0.41); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'performance_data' (status_code 200, logs_ingested 17). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-13"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000163",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.35",
                    "supporting_stat_value": 0.35,
                    "game_pk": "2024000163",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000163",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_era_2.7",
                    "supporting_stat_value": 2.7,
                    "game_pk": "2024000163",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.53",
                    "supporting_stat_value": 0.53,
                    "game_pk": "2024000163",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.27",
                    "supporting_stat_value": 0.27,
                    "game_pk": "2024000163",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.69",
                    "supporting_stat_value": 0.69,
                    "game_pk": "2024000163",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_112",
                    "supporting_stat_value": 112,
                    "game_pk": "2024000163",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runner_scoring_ops_0.748",
                    "supporting_stat_value": 0.748,
                    "game_pk": "2024000163",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000163",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000163",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000163-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000163-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000163/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000163-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "performance_data",
                    "status_code": 200,
                    "logs_ingested": 17
                }
            }
        ],
        "outputs": [
                "RPT-2024000163-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task34",
        "instruction": "Oversee operations as the analytics lead for the home team.. For opponent team id 10 on date '2024-09-27' with gamePk '2024000067', compile and distribute a pre-series scouting intelligence bundle utilizing advanced stats with min_sample_size 40. Include exactly one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Post to '#coaches-prep' and supply the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task35",
        "instruction": "Function as the analytics agent for the home side. For gamePk '2024000068' on date '2024-09-28', conduct full in-game monitoring with real-time alerting (leverage_index 2.3, is_manual_alert False, suggestion_text 'defensive shift review'), affirm catcher-view artifact quality, ensure model freshness validation, log ingestion activity (source_name 'in_game_snapshot', status_code 200, logs_ingested 65), and complete the monitoring lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000068"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-28"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-28"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000068",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000068",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000068",
                    "leverage_index": 2.3,
                    "is_manual_alert": false,
                    "suggestion_text": "defensive shift review"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 65
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000068"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task36",
        "instruction": "As the recognized analytics delegate, you are in charge. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', provide a pre-series scouting intelligence set, ensuring the application of advanced statistics with min_sample_size 40. Maintain one video playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1. Share on '#coaches-prep' and supply the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task37",
        "instruction": "You are acting as the team\u2019s scouting and analytics agent. Deliver a pre-series scouting bundle for opponent team id 13 on date '2024-12-13' with gamePk '2024000193'. The package must satisfy these acceptance criteria: pitcher 101 with 5 observations (tendency_cutter_usage_0.28, execution_zone_rate_0.71, stamina_pitch_count_108, situational_high_leverage_era_3.7, predictability_pattern_score_0.59); pitcher 102 with 5 observations (tendency_splitter_usage_0.18, execution_whiff_rate_0.43, stamina_pitch_count_84, situational_bases_loaded_ops_0.734, predictability_timing_score_0.41); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log with source_name 'tactical_data' (status_code 200, logs_ingested 47). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-13"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000193",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.71",
                    "supporting_stat_value": 0.71,
                    "game_pk": "2024000193",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_108",
                    "supporting_stat_value": 108,
                    "game_pk": "2024000193",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_era_3.7",
                    "supporting_stat_value": 3.7,
                    "game_pk": "2024000193",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000193",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_splitter_usage_0.18",
                    "supporting_stat_value": 0.18,
                    "game_pk": "2024000193",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.43",
                    "supporting_stat_value": 0.43,
                    "game_pk": "2024000193",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_84",
                    "supporting_stat_value": 84,
                    "game_pk": "2024000193",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_ops_0.734",
                    "supporting_stat_value": 0.734,
                    "game_pk": "2024000193",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000193",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000193",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000193-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000193-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000193/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000193-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_data",
                    "status_code": 200,
                    "logs_ingested": 47
                }
            }
        ],
        "outputs": [
                "RPT-2024000193-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task38",
        "instruction": "Assigned as the analytics coordinator for the home side, deliver a pre-series scouting bundle for opponent team id 13 on date '2024-11-21' with gamePk '2024000171'. The package needs to meet these acceptance criteria: pitcher 101 with 5 observations (tendency_cutter_usage_0.28, execution_whiff_rate_0.27, stamina_pitch_count_114, situational_lefty_era_5.3, predictability_velocity_score_0.33); pitcher 102 with 5 observations (tendency_sinker_usage_0.39, execution_contact_rate_0.71, stamina_pitch_count_89, situational_clutch_ops_0.767, predictability_pattern_score_0.56); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log with source_name 'situational_data' (status_code 200, logs_ingested 25). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-21"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000171",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.27",
                    "supporting_stat_value": 0.27,
                    "game_pk": "2024000171",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_114",
                    "supporting_stat_value": 114,
                    "game_pk": "2024000171",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_era_5.3",
                    "supporting_stat_value": 5.3,
                    "game_pk": "2024000171",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.33",
                    "supporting_stat_value": 0.33,
                    "game_pk": "2024000171",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.39",
                    "supporting_stat_value": 0.39,
                    "game_pk": "2024000171",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.71",
                    "supporting_stat_value": 0.71,
                    "game_pk": "2024000171",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_89",
                    "supporting_stat_value": 89,
                    "game_pk": "2024000171",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.767",
                    "supporting_stat_value": 0.767,
                    "game_pk": "2024000171",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.56",
                    "supporting_stat_value": 0.56,
                    "game_pk": "2024000171",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000171",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000171-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000171-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000171/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000171-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "situational_data",
                    "status_code": 200,
                    "logs_ingested": 25
                }
            }
        ],
        "outputs": [
                "RPT-2024000171-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task39",
        "instruction": "As the official analytics resource for this club, you are engaged to provide a pre-series scouting bundle for opponent team id 13 on date '2024-12-01' with gamePk '2024000181'. The package should fulfill these acceptance criteria: pitcher 101 with 5 observations (tendency_sinker_usage_0.39, execution_called_strike_rate_0.61, stamina_pitch_count_113, situational_runner_scoring_era_5.7, predictability_pattern_score_0.46); pitcher 102 with 5 observations (tendency_splitter_usage_0.20, execution_ground_ball_rate_0.56, stamina_pitch_count_85, situational_high_leverage_ops_0.856, predictability_approach_score_0.39); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record with source_name 'preparation_data' (status_code 200, logs_ingested 35). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-01"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.39",
                    "supporting_stat_value": 0.39,
                    "game_pk": "2024000181",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.61",
                    "supporting_stat_value": 0.61,
                    "game_pk": "2024000181",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_113",
                    "supporting_stat_value": 113,
                    "game_pk": "2024000181",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runner_scoring_era_5.7",
                    "supporting_stat_value": 5.7,
                    "game_pk": "2024000181",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.46",
                    "supporting_stat_value": 0.46,
                    "game_pk": "2024000181",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_splitter_usage_0.20",
                    "supporting_stat_value": 0.2,
                    "game_pk": "2024000181",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.56",
                    "supporting_stat_value": 0.56,
                    "game_pk": "2024000181",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_85",
                    "supporting_stat_value": 85,
                    "game_pk": "2024000181",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_ops_0.856",
                    "supporting_stat_value": 0.856,
                    "game_pk": "2024000181",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.39",
                    "supporting_stat_value": 0.39,
                    "game_pk": "2024000181",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000181",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000181-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000181-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000181/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000181-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "preparation_data",
                    "status_code": 200,
                    "logs_ingested": 35
                }
            }
        ],
        "outputs": [
                "RPT-2024000181-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task40",
        "instruction": "You are designated as the scouting representative. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', deliver the required pre-series scouting bundle: create per-pitcher insights (five mandated categories, deterministic templates, computed metrics); save the PDF report along with one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1; distribute this package to '#coaches-prep'; and record a readiness log entry for source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task41",
        "instruction": "Handle the duties as the team's designated scouting contact.. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', compile the pre-series scouting package to adhere to policy: curate per-pitcher insight sets (five categories via deterministic templates with metric values); generate and save a PDF report and one video playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1; transmit package to '#coaches-prep'; and record a readiness log (source_name 'dq_pre_series_day2', status_code 200, logs_ingested 0). Supply back the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task42",
        "instruction": "Coordinate as the designated scouting representative.. For gamePk '2024000168' on date '2024-11-18', construct comprehensive in-game monitoring with real-time alerts (leverage_index 1.8, is_manual_alert False, suggestion_text 'command evaluation'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 59), and finalize the monitoring workflow lifecycle. Provide back 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000168"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-18"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-18"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000168",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000168",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000168",
                    "leverage_index": 1.8,
                    "is_manual_alert": false,
                    "suggestion_text": "command evaluation"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 59
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000168"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task43",
        "instruction": "You are performing as the analytics agent for the home side.. For opponent team id 10 on date '2024-09-27' with gamePk '2024000067', produce the pre-series scouting package. Incorporate statistical validation with min_sample_size 40. Generate a single playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' (clip_count 1). Distribute package to '#coaches-prep' and return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task44",
        "instruction": "Act in the role of the home club's analytics lead.. For gamePk '2024000025' on date '2024-08-03', provide an in-game monitoring outcome satisfying these acceptance criteria: one logged alert with leverage_index 1.7, is_manual_alert False, suggestion_text 'monitor usage drift'; live pitch tracking is normalized and validated by the persisted artifact '12x12_catcher_view' with a passed quality check; models for that date are verified as fresh; an ingestion record entry exists with source_name 'in_game_snapshot' (status_code 200, logs_ingested 45); and the real-time monitoring flow is considered completed. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000025"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-08-03"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-08-03"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000025",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000025",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000025",
                    "leverage_index": 1.7,
                    "is_manual_alert": false,
                    "suggestion_text": "monitor usage drift"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 45
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000025"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task45",
        "instruction": "Prepare the official scouting materials.. For gamePk '2024000061' on date '2024-09-21', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 1.9, is_manual_alert False, suggestion_text 'tactical_adjustment'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 75), and conclude the monitoring workflow lifecycle. Provide back 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000061"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-21"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-21"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000061",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000061",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000061",
                    "leverage_index": 1.9,
                    "is_manual_alert": false,
                    "suggestion_text": "tactical_adjustment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 75
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000061"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task46",
        "instruction": "You are serving as the analytics liaison for the home organization.. For opponent team id 5 on date '2024-08-05' with gamePk '2024000027', handle the delivery of a pre-series scouting bundle that conforms to policy outcomes: a per-pitcher insight set (5 policy-defined types using deterministic templates with metric values obtained from computed metrics); ensure a persisted PDF report and one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; distribution to '#coaches-prep'; and a context log with source_name 'schedule_snapshot' (status_code 200, logs_ingested 2). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 5
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-08-05"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000027",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000027",
                    "s3_pdf_path": "s3://reports/2024000027/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000027-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000027-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000027/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000027-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "schedule_snapshot",
                    "status_code": 200,
                    "logs_ingested": 2
                }
            }
        ],
        "outputs": [
                "RPT-2024000027-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task47",
        "instruction": "You are serving in the role of the team\u2019s scouting and analytics agent.. Coordinate the provision of a pre-series scouting bundle for opponent team id 13 on date '2024-11-19' with gamePk '2024000169'. The package should fulfill these acceptance criteria: pitcher 101 has 5 observations (tendency_fastball_usage_0.61, execution_ground_ball_rate_0.55, stamina_pitch_count_96, situational_risp_era_3.4, predictability_approach_score_0.52); pitcher 102 has 5 observations (tendency_changeup_usage_0.25, execution_strike_zone_rate_0.73, stamina_pitch_count_103, situational_pressure_ops_0.695, predictability_release_score_0.37); include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'game_prep' (status_code 200, logs_ingested 23). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-19"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.61",
                    "supporting_stat_value": 0.61,
                    "game_pk": "2024000169",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.55",
                    "supporting_stat_value": 0.55,
                    "game_pk": "2024000169",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_96",
                    "supporting_stat_value": 96,
                    "game_pk": "2024000169",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.4",
                    "supporting_stat_value": 3.4,
                    "game_pk": "2024000169",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.52",
                    "supporting_stat_value": 0.52,
                    "game_pk": "2024000169",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.25",
                    "supporting_stat_value": 0.25,
                    "game_pk": "2024000169",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_zone_rate_0.73",
                    "supporting_stat_value": 0.73,
                    "game_pk": "2024000169",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_103",
                    "supporting_stat_value": 103,
                    "game_pk": "2024000169",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_ops_0.695",
                    "supporting_stat_value": 0.695,
                    "game_pk": "2024000169",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.37",
                    "supporting_stat_value": 0.37,
                    "game_pk": "2024000169",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000169",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000169-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000169-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000169/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000169-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "game_prep",
                    "status_code": 200,
                    "logs_ingested": 23
                }
            }
        ],
        "outputs": [
                "RPT-2024000169-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task48",
        "instruction": "You are designated as the analytics coordinator for the home side.. Coordinate the provision of a pre-series scouting bundle for opponent team id 13 on date '2024-08-08' with gamePk '2024000030'. The package should adhere to these acceptance criteria: pitcher 101 has 5 observations (tendency_fastball_usage_0.72, execution_strike_rate_0.68, stamina_pitch_count_102, situational_risp_era_2.8, predictability_sequence_score_0.51); pitcher 102 has 5 observations (tendency_slider_usage_0.32, execution_whiff_rate_0.28, stamina_pitch_count_95, situational_lefty_ops_0.792, predictability_count_leverage_0.59); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'tactical_prep' (status_code 200, logs_ingested 8). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-08-08"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000030",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000030",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_102",
                    "supporting_stat_value": 102,
                    "game_pk": "2024000030",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_2.8",
                    "supporting_stat_value": 2.8,
                    "game_pk": "2024000030",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.51",
                    "supporting_stat_value": 0.51,
                    "game_pk": "2024000030",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.32",
                    "supporting_stat_value": 0.32,
                    "game_pk": "2024000030",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000030",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000030",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.792",
                    "supporting_stat_value": 0.792,
                    "game_pk": "2024000030",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000030",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000030",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000030-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000030-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000030/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000030-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_prep",
                    "status_code": 200,
                    "logs_ingested": 8
                }
            }
        ],
        "outputs": [
                "RPT-2024000030-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task49",
        "instruction": "You are appointed as the official analytics resource for this club.. For opponent team id 6 on date '2024-10-02' with gamePk '2024000072', coordinate the delivery of a comprehensive pre-series scouting bundle. Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 6
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-10-02"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000072",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000072",
                    "s3_pdf_path": "s3://reports/2024000072/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000072-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000072-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000072/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000072-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000072-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task50",
        "instruction": "You are performing as the recognized analytics agent for the home squad.. For gamePk '2024000024' on date '2024-08-02', set up comprehensive in-game monitoring with real-time alerts (leverage_index 2.5, is_manual_alert False, suggestion_text 'strategic monitoring'), spatial data tracking with artifact '12x12_catcher_view' quality validation, certify model freshness, perform data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 67), and finalize the monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000024"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-08-02"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-08-02"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000024",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000024",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000024",
                    "leverage_index": 2.5,
                    "is_manual_alert": false,
                    "suggestion_text": "strategic monitoring"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 67
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000024"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task51",
        "instruction": "Act as the analytics agent for the home team. For opponent team id 6 on date '2024-08-06' with gamePk '2024000028', compile a complete pre-series scouting bundle. Provide the report id upon completion.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 6
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-08-06"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000028",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000028",
                    "s3_pdf_path": "s3://reports/2024000028/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000028-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000028-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000028/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000028-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000028-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task52",
        "instruction": "Your responsibility is to serve as the official scouting representative. Deliver a pre-series scouting bundle for opponent team id 13 on date '2024-11-07' with gamePk '2024000157'. The package must satisfy these acceptance conditions: pitcher 101 has 5 observations (tendency_slider_usage_0.35, execution_ground_ball_rate_0.52, stamina_pitch_count_86, situational_clutch_era_5.1, predictability_timing_score_0.39); pitcher 102 has 5 observations (tendency_fastball_usage_0.58, execution_whiff_rate_0.29, stamina_pitch_count_115, situational_late_inning_ops_0.756, predictability_velocity_score_0.61); include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log entry with source_name 'matchup_data' (status_code 200, logs_ingested 11). Provide the report id at the end.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-07"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.35",
                    "supporting_stat_value": 0.35,
                    "game_pk": "2024000157",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.52",
                    "supporting_stat_value": 0.52,
                    "game_pk": "2024000157",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_86",
                    "supporting_stat_value": 86,
                    "game_pk": "2024000157",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_era_5.1",
                    "supporting_stat_value": 5.1,
                    "game_pk": "2024000157",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.39",
                    "supporting_stat_value": 0.39,
                    "game_pk": "2024000157",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000157",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.29",
                    "supporting_stat_value": 0.29,
                    "game_pk": "2024000157",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_115",
                    "supporting_stat_value": 115,
                    "game_pk": "2024000157",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_ops_0.756",
                    "supporting_stat_value": 0.756,
                    "game_pk": "2024000157",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.61",
                    "supporting_stat_value": 0.61,
                    "game_pk": "2024000157",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000157",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000157-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000157-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000157/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000157-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "matchup_data",
                    "status_code": 200,
                    "logs_ingested": 11
                }
            }
        ],
        "outputs": [
                "RPT-2024000157-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task53",
        "instruction": "Assume the role of pre-series analytics agent for the club. For opponent team id 6 on date '2024-07-30' with gamePk '2024000018', prepare and submit a full pre-series scouting bundle. Deliver the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 6
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-30"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000018",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000018",
                    "s3_pdf_path": "s3://reports/2024000018/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000018-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000018-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000018/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000018-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000018-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task54",
        "instruction": "Function as the analytics point of contact for the home club. For gamePk '2024000089' on date '2024-10-15', activate in-game monitoring with real-time alerts (leverage_index 1.9, is_manual_alert True, suggestion_text 'defensive alignment check'), ensure the validity of the spatial artifact '12x12_catcher_view', then finish model freshness certification, log ingestion records (source_name 'in_game_snapshot', status_code 200, logs_ingested 90), and conclude the monitoring workflow lifecycle. Respond with 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000089"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000089",
                    "artifact_name": "12x12_catcher_view"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-10-15"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-10-15"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000089",
                    "leverage_index": 1.9,
                    "is_manual_alert": true,
                    "suggestion_text": "defensive alignment check"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 90
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000089"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task43",
        "instruction": "Operate as the designated analytics official. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', develop and complete a pre-series scouting report bundle with advanced filtering at min_sample_size 40. Include a video playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1. Share with '#coaches-prep' and provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task56",
        "instruction": "Acting as the analytics liaison for the home organization, handle the delivery of a pre-series scouting package for opponent team id 13 on date '2024-12-07' with gamePk '2024000187'. These acceptance criteria must be followed: pitcher 101 has 5 observations (tendency_knuckleball_usage_0.03, execution_swing_miss_rate_0.41, stamina_pitch_count_96, situational_late_inning_era_2.9, predictability_sequence_score_0.53); pitcher 102 has 5 observations (tendency_fastball_usage_0.68, execution_zone_rate_0.78, stamina_pitch_count_111, situational_bases_empty_ops_0.692, predictability_timing_score_0.37); make sure to include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'team_intel' (status_code 200, logs_ingested 41). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-07"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_knuckleball_usage_0.03",
                    "supporting_stat_value": 0.03,
                    "game_pk": "2024000187",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000187",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_96",
                    "supporting_stat_value": 96,
                    "game_pk": "2024000187",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_era_2.9",
                    "supporting_stat_value": 2.9,
                    "game_pk": "2024000187",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.53",
                    "supporting_stat_value": 0.53,
                    "game_pk": "2024000187",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000187",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.78",
                    "supporting_stat_value": 0.78,
                    "game_pk": "2024000187",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_111",
                    "supporting_stat_value": 111,
                    "game_pk": "2024000187",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_empty_ops_0.692",
                    "supporting_stat_value": 0.692,
                    "game_pk": "2024000187",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.37",
                    "supporting_stat_value": 0.37,
                    "game_pk": "2024000187",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000187",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000187-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000187-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000187/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000187-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "team_intel",
                    "status_code": 200,
                    "logs_ingested": 41
                }
            }
        ],
        "outputs": [
                "RPT-2024000187-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task57",
        "instruction": "As the team\u2019s scouting and analytics agent, orchestrate the provisioning of a pre-series scouting bundle for opponent team id 13 on date '2024-11-23' with gamePk '2024000173'. These acceptance criteria should be adhered to: pitcher 101 has 5 observations (tendency_slider_usage_0.34, execution_zone_rate_0.68, stamina_pitch_count_98, situational_runner_scoring_era_4.1, predictability_timing_score_0.46); pitcher 102 has 5 observations (tendency_changeup_usage_0.22, execution_first_strike_rate_0.65, stamina_pitch_count_106, situational_high_leverage_ops_0.789, predictability_approach_score_0.51); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'series_analysis' (status_code 200, logs_ingested 27). Deliver the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-23"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.34",
                    "supporting_stat_value": 0.34,
                    "game_pk": "2024000173",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000173",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_98",
                    "supporting_stat_value": 98,
                    "game_pk": "2024000173",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runner_scoring_era_4.1",
                    "supporting_stat_value": 4.1,
                    "game_pk": "2024000173",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.46",
                    "supporting_stat_value": 0.46,
                    "game_pk": "2024000173",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.22",
                    "supporting_stat_value": 0.22,
                    "game_pk": "2024000173",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000173",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_106",
                    "supporting_stat_value": 106,
                    "game_pk": "2024000173",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_ops_0.789",
                    "supporting_stat_value": 0.789,
                    "game_pk": "2024000173",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.51",
                    "supporting_stat_value": 0.51,
                    "game_pk": "2024000173",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000173",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000173-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000173-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000173/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000173-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "series_analysis",
                    "status_code": 200,
                    "logs_ingested": 27
                }
            }
        ],
        "outputs": [
                "RPT-2024000173-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task58",
        "instruction": "In your role as the analytics coordinator for the home side, facilitate the provision of a pre-series scouting bundle for opponent team id 13 on date '2024-11-15' with gamePk '2024000165'. The package should fulfill these acceptance conditions: pitcher 101 has 5 observations (tendency_sinker_usage_0.42, execution_contact_rate_0.67, stamina_pitch_count_105, situational_high_leverage_era_4.5, predictability_release_score_0.36); pitcher 102 has 5 observations (tendency_curveball_usage_0.18, execution_first_strike_rate_0.66, stamina_pitch_count_94, situational_late_inning_ops_0.712, predictability_pattern_score_0.59); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'tactical_intel' (status_code 200, logs_ingested 19). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-15"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.42",
                    "supporting_stat_value": 0.42,
                    "game_pk": "2024000165",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.67",
                    "supporting_stat_value": 0.67,
                    "game_pk": "2024000165",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_105",
                    "supporting_stat_value": 105,
                    "game_pk": "2024000165",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_era_4.5",
                    "supporting_stat_value": 4.5,
                    "game_pk": "2024000165",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.36",
                    "supporting_stat_value": 0.36,
                    "game_pk": "2024000165",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.18",
                    "supporting_stat_value": 0.18,
                    "game_pk": "2024000165",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.66",
                    "supporting_stat_value": 0.66,
                    "game_pk": "2024000165",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_94",
                    "supporting_stat_value": 94,
                    "game_pk": "2024000165",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_ops_0.712",
                    "supporting_stat_value": 0.712,
                    "game_pk": "2024000165",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000165",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000165",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000165-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000165-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000165/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000165-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_intel",
                    "status_code": 200,
                    "logs_ingested": 19
                }
            }
        ],
        "outputs": [
                "RPT-2024000165-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task59",
        "instruction": "As the designated analytics resource for this club, arrange for the establishment of comprehensive in-game monitoring for gamePk '2024000174' on date '2024-11-24', including real-time alerts (leverage_index 1.5, is_manual_alert False, suggestion_text 'approach adjustment'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 65), and completion of the full monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000174"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-24"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-24"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000174",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000174",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000174",
                    "leverage_index": 1.5,
                    "is_manual_alert": false,
                    "suggestion_text": "approach adjustment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 65
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000174"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task60",
        "instruction": "Functioning as the recognized analytics agent for the home squad, carry out the delivery of a pre-series scouting bundle for opponent team id 13 on date '2024-11-05' with gamePk '2024000155'. These acceptance criteria must be observed: pitcher 101 has 5 observations (tendency_cutter_usage_0.29, execution_first_strike_rate_0.64, stamina_pitch_count_99, situational_lefty_era_2.9, predictability_pattern_score_0.55); pitcher 102 has 5 observations (tendency_knuckleball_usage_0.12, execution_zone_rate_0.71, stamina_pitch_count_104, situational_pressure_ops_0.692, predictability_approach_score_0.43); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'opponent_analysis' (status_code 200, logs_ingested 9). Deliver the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-05"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.29",
                    "supporting_stat_value": 0.29,
                    "game_pk": "2024000155",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.64",
                    "supporting_stat_value": 0.64,
                    "game_pk": "2024000155",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_99",
                    "supporting_stat_value": 99,
                    "game_pk": "2024000155",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_era_2.9",
                    "supporting_stat_value": 2.9,
                    "game_pk": "2024000155",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.55",
                    "supporting_stat_value": 0.55,
                    "game_pk": "2024000155",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_knuckleball_usage_0.12",
                    "supporting_stat_value": 0.12,
                    "game_pk": "2024000155",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_zone_rate_0.71",
                    "supporting_stat_value": 0.71,
                    "game_pk": "2024000155",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_104",
                    "supporting_stat_value": 104,
                    "game_pk": "2024000155",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_ops_0.692",
                    "supporting_stat_value": 0.692,
                    "game_pk": "2024000155",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.43",
                    "supporting_stat_value": 0.43,
                    "game_pk": "2024000155",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000155",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000155-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000155-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000155/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000155-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "opponent_analysis",
                    "status_code": 200,
                    "logs_ingested": 9
                }
            }
        ],
        "outputs": [
                "RPT-2024000155-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task61",
        "instruction": "Act as the analytics agent for the home team. Compile a pre-series scouting package for opponent team id 13 scheduled for '2024-09-15' with gamePk '2024000055'. The package must fulfill these acceptance criteria: pitcher 101 has 5 observations (tendency_changeup_usage_0.42, execution_command_rate_0.68, stamina_pitch_count_102, situational_bases_loaded_era_4.1, predictability_tunnel_score_0.38); pitcher 102 has 5 observations (tendency_curveball_usage_0.31, execution_ground_ball_rate_0.55, stamina_pitch_count_94, situational_clutch_ops_0.765, predictability_timing_leverage_0.71); incorporate internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log entry with source_name 'advanced_metrics' (status_code 200, logs_ingested 2). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-15"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.42",
                    "supporting_stat_value": 0.42,
                    "game_pk": "2024000055",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_command_rate_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000055",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_102",
                    "supporting_stat_value": 102,
                    "game_pk": "2024000055",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_4.1",
                    "supporting_stat_value": 4.1,
                    "game_pk": "2024000055",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_tunnel_score_0.38",
                    "supporting_stat_value": 0.38,
                    "game_pk": "2024000055",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000055",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.55",
                    "supporting_stat_value": 0.55,
                    "game_pk": "2024000055",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_94",
                    "supporting_stat_value": 94,
                    "game_pk": "2024000055",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.765",
                    "supporting_stat_value": 0.765,
                    "game_pk": "2024000055",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_leverage_0.71",
                    "supporting_stat_value": 0.71,
                    "game_pk": "2024000055",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000055",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000055",
                    "s3_pdf_path": "s3://reports/2024000055/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000055-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000055-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000055/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000055-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "advanced_metrics",
                    "status_code": 200,
                    "logs_ingested": 2
                }
            }
        ],
        "outputs": [
                "RPT-2024000055-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task62",
        "instruction": "Your role involves acting as the official scouting representative. For the date '2024-08-04', generate and issue a comprehensive pre-series scouting intelligence package for the upcoming scheduled game. Use internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1, publish to the channel '#coaches-prep', and provide the report id.",
        "actions": [
            {
                "name": "findNext",
                "arguments": {
                    "current_date": "2024-08-04"
                },
            },
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 7
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-08-04"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_table"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000004",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000004",
                    "s3_pdf_path": "s3://reports/2024000004/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000004-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000004-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000004/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000004-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000004-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task63",
        "instruction": "Function as the in-game analytics agent for the club. For game_pk '2024000074' dated '2024-10-04', set up extensive in-game monitoring with real-time alerts (leverage_index 2.1, is_manual_alert False, suggestion_text 'timing evaluation'), spatial data tracking with artifact '12x12_catcher_view' quality control, certify model freshness, log data ingestion (source_name 'live_tracking', status_code 200, logs_ingested 75), and complete the monitoring workflow life cycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000074"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-10-04"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-10-04"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000074",
                    "time_window": "pitches_live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000074",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000074",
                    "leverage_index": 2.1,
                    "is_manual_alert": false,
                    "suggestion_text": "timing evaluation"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "live_tracking",
                    "status_code": 200,
                    "logs_ingested": 75
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000074"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task64",
        "instruction": "Serve as the home club\u2019s analytics lead. For gamePk '2024000154' on '2024-11-04', implement thorough in-game monitoring with real-time alerts (leverage_index 1.4, is_manual_alert False, suggestion_text 'defensive positioning'), ensure spatial data tracking with artifact '12x12_catcher_view' quality, validate model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 42), and execute the complete monitoring workflow cycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000154"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-04"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-04"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000154",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000154",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000154",
                    "leverage_index": 1.4,
                    "is_manual_alert": false,
                    "suggestion_text": "defensive positioning"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 42
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000154"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task65",
        "instruction": "Take responsibility for preparing the official scouting material. For gamePk '2024000075' on '2024-10-05', conduct comprehensive in-game monitoring with real-time alerts (leverage_index 1.9, is_manual_alert False, suggestion_text 'pitch sequence monitoring'), validate spatial data tracking with artifact '12x12_catcher_view' quality, certify model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 65), and carry out the full monitoring workflow cycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000075"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-10-05"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-10-05"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000075",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000075",
                    "leverage_index": 1.9,
                    "is_manual_alert": false,
                    "suggestion_text": "pitch sequence monitoring"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 65
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000075"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task66",
        "instruction": "As the liaison for analytics in the home organization, for the date '2024-07-24', create and share a complete pre-series scouting intelligence package for the upcoming game. Utilize internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1, post to channel '#coaches-prep', and provide the report id.",
        "actions": [
            {
                "name": "findNext",
                "arguments": {
                    "current_date": "2024-07-24"
                },
            },
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_table"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task67",
        "instruction": "Assume the role of the team's scouting and analytics agent.. For the opponent team id 7 on '2024-09-20' and gamePk '2024000060', compile and send out a pre-series scouting bundle with saved artifacts. Utilize internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Submit to '#coaches-prep'. Supply the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 7
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-20"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000060",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000060",
                    "s3_pdf_path": "s3://reports/2024000060/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000060-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000060-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000060/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000060-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000060-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task68",
        "instruction": "You are appointed as the analytics coordinator for the home team.. Prepare a pre-series scouting bundle for opponent team id 13 on '2024-11-03' with gamePk '2024000153'. The package must satisfy these criteria: pitcher 101 has 5 observations (tendency_splitter_usage_0.24, execution_called_strike_rate_0.59, stamina_pitch_count_107, situational_runner_scoring_era_3.7, predictability_location_score_0.41); pitcher 102 has 5 observations (tendency_sinker_usage_0.38, execution_swing_miss_rate_0.33, stamina_pitch_count_96, situational_high_leverage_ops_0.803, predictability_velocity_score_0.67); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log entry with source_name 'tactical_analysis' (status_code 200, logs_ingested 7). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-03"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_splitter_usage_0.24",
                    "supporting_stat_value": 0.24,
                    "game_pk": "2024000153",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000153",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_107",
                    "supporting_stat_value": 107,
                    "game_pk": "2024000153",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runner_scoring_era_3.7",
                    "supporting_stat_value": 3.7,
                    "game_pk": "2024000153",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000153",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.38",
                    "supporting_stat_value": 0.38,
                    "game_pk": "2024000153",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.33",
                    "supporting_stat_value": 0.33,
                    "game_pk": "2024000153",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_96",
                    "supporting_stat_value": 96,
                    "game_pk": "2024000153",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_ops_0.803",
                    "supporting_stat_value": 0.803,
                    "game_pk": "2024000153",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.67",
                    "supporting_stat_value": 0.67,
                    "game_pk": "2024000153",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000153",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000153-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000153-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000153/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000153-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_analysis",
                    "status_code": 200,
                    "logs_ingested": 7
                }
            }
        ],
        "outputs": [
                "RPT-2024000153-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task69",
        "instruction": "Fulfill your role as the official analytics resource for this club.. Produce a pre-series scouting bundle for opponent team id 13 on '2024-12-11' with gamePk '2024000191'. The package should satisfy the following criteria: pitcher 101 has 5 observations (tendency_slider_usage_0.37, execution_swing_miss_rate_0.38, stamina_pitch_count_99, situational_runners_on_era_5.2, predictability_velocity_score_0.45); pitcher 102 has 5 observations (tendency_sinker_usage_0.41, execution_ground_ball_rate_0.58, stamina_pitch_count_93, situational_late_inning_ops_0.827, predictability_release_score_0.33); ensure the addition of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and document an ingestion entry with source_name 'game_intelligence' (status_code 200, logs_ingested 45). Submit the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-11"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.37",
                    "supporting_stat_value": 0.37,
                    "game_pk": "2024000191",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.38",
                    "supporting_stat_value": 0.38,
                    "game_pk": "2024000191",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_99",
                    "supporting_stat_value": 99,
                    "game_pk": "2024000191",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runners_on_era_5.2",
                    "supporting_stat_value": 5.2,
                    "game_pk": "2024000191",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000191",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000191",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000191",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_93",
                    "supporting_stat_value": 93,
                    "game_pk": "2024000191",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_ops_0.827",
                    "supporting_stat_value": 0.827,
                    "game_pk": "2024000191",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.33",
                    "supporting_stat_value": 0.33,
                    "game_pk": "2024000191",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000191",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000191-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000191-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000191/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000191-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "game_intelligence",
                    "status_code": 200,
                    "logs_ingested": 45
                }
            }
        ],
        "outputs": [
                "RPT-2024000191-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task70",
        "instruction": "Function as the official scouting analytics contact.. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', generate the pre-series scouting package that fulfills the requirements: apply advanced statistics (min_sample_size 40), store a single video playlist at internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1, and submit to '#coaches-prep'. Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task71",
        "instruction": "In your role as the analytics agent for the home team, compile a pre-series scouting bundle for the opponent team id 13 on date '2024-07-24' with gamePk '2024000013'. The package must adhere to these acceptance criteria: pitcher 101 has 5 observations (tendency_fastball_usage_0.65, execution_strike_rate_0.72, stamina_pitch_count_95, situational_risp_era_3.2, predictability_sequence_score_0.45); pitcher 102 has 5 observations (tendency_slider_usage_0.28, execution_whiff_rate_0.31, stamina_pitch_count_88, situational_lefty_ops_0.875, predictability_count_leverage_0.62); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'precheck_day2' (status_code 200, logs_ingested 0). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "precheck_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task72",
        "instruction": "In your capacity as the official scouting representative, coordinate comprehensive in-game monitoring for gamePk '2024000057' on date '2024-09-17', with real-time alerts (leverage_index 1.8, is_manual_alert False, suggestion_text 'timing evaluation'), spatial data tracking validating artifact '12x12_catcher_view', model freshness certification, data ingestion logging (source_name 'live_tracking', status_code 200, logs_ingested 92), and complete monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000057"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-09-17"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-09-17"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000057",
                    "time_window": "pitches_live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "df__pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000057",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000057",
                    "leverage_index": 1.8,
                    "is_manual_alert": false,
                    "suggestion_text": "timing evaluation"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "live_tracking",
                    "status_code": 200,
                    "logs_ingested": 92
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000057"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task73",
        "instruction": "As the designated pre-series analytics agent for the club, assemble a pre-series scouting bundle for opponent team id 13 on date '2024-11-25' with gamePk '2024000175'. The package should comply with these acceptance criteria: pitcher 101 has 5 observations (tendency_curveball_usage_0.17, execution_called_strike_rate_0.62, stamina_pitch_count_111, situational_bases_loaded_era_6.2, predictability_location_score_0.31); pitcher 102 has 5 observations (tendency_fastball_usage_0.59, execution_swing_miss_rate_0.30, stamina_pitch_count_95, situational_late_inning_ops_0.823, predictability_velocity_score_0.49); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'final_prep' (status_code 200, logs_ingested 29). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-25"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.17",
                    "supporting_stat_value": 0.17,
                    "game_pk": "2024000175",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000175",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_111",
                    "supporting_stat_value": 111,
                    "game_pk": "2024000175",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_6.2",
                    "supporting_stat_value": 6.2,
                    "game_pk": "2024000175",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000175",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000175",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.30",
                    "supporting_stat_value": 0.3,
                    "game_pk": "2024000175",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000175",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_late_inning_ops_0.823",
                    "supporting_stat_value": 0.823,
                    "game_pk": "2024000175",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_velocity_score_0.49",
                    "supporting_stat_value": 0.49,
                    "game_pk": "2024000175",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000175",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000175-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000175-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000175/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000175-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "final_prep",
                    "status_code": 200,
                    "logs_ingested": 29
                }
            }
        ],
        "outputs": [
                "RPT-2024000175-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task74",
        "instruction": "Assigned as the home club's analytics lead, prepare a pre-series scouting bundle for opponent team id 13 on date '2024-07-24' with gamePk '2024000013', ensuring policy outcomes are satisfied: a per-pitcher insight set (5 policy-defined types using deterministic templates with metric-derived values), a persisted PDF report, and one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; distribution to '#coaches-prep'; and a context log with source_name 'schedule_snapshot' (status_code 200, logs_ingested 3). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "schedule_snapshot",
                    "status_code": 200,
                    "logs_ingested": 3
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task75",
        "instruction": "In the role of preparing the official scouting material, assemble a pre-series scouting bundle for opponent team id 13 on date '2024-11-01' with gamePk '2024000151'. The package should meet these acceptance criteria: pitcher 101 has 5 observations (tendency_changeup_usage_0.32, execution_contact_rate_0.68, stamina_pitch_count_103, situational_bases_loaded_era_4.8, predictability_timing_score_0.52); pitcher 102 has 5 observations (tendency_curveball_usage_0.19, execution_strike_zone_rate_0.77, stamina_pitch_count_91, situational_clutch_ops_0.724, predictability_release_score_0.38); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'scouting_prep' (status_code 200, logs_ingested 5). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-01"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.32",
                    "supporting_stat_value": 0.32,
                    "game_pk": "2024000151",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000151",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_103",
                    "supporting_stat_value": 103,
                    "game_pk": "2024000151",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_4.8",
                    "supporting_stat_value": 4.8,
                    "game_pk": "2024000151",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.52",
                    "supporting_stat_value": 0.52,
                    "game_pk": "2024000151",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_curveball_usage_0.19",
                    "supporting_stat_value": 0.19,
                    "game_pk": "2024000151",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_zone_rate_0.77",
                    "supporting_stat_value": 0.77,
                    "game_pk": "2024000151",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_91",
                    "supporting_stat_value": 91,
                    "game_pk": "2024000151",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.724",
                    "supporting_stat_value": 0.724,
                    "game_pk": "2024000151",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.38",
                    "supporting_stat_value": 0.38,
                    "game_pk": "2024000151",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000151",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000151-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000151-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000151/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000151-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "scouting_prep",
                    "status_code": 200,
                    "logs_ingested": 5
                }
            }
        ],
        "outputs": [
                "RPT-2024000151-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task76",
        "instruction": "Act as the analytics liaison for the home organization.. Present a pre-series scouting bundle for opponent team id 13 on date '2024-11-17' with gamePk '2024000167'. The package should fulfill these acceptance criteria: pitcher 101 includes 5 observations (tendency_splitter_usage_0.23, execution_swing_miss_rate_0.32, stamina_pitch_count_110, situational_bases_loaded_era_5.8, predictability_location_score_0.28); pitcher 102 has 5 observations (tendency_slider_usage_0.33, execution_called_strike_rate_0.58, stamina_pitch_count_87, situational_clutch_ops_0.834, predictability_timing_score_0.48); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'advance_scouting' (status_code 200, logs_ingested 21). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-17"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_splitter_usage_0.23",
                    "supporting_stat_value": 0.23,
                    "game_pk": "2024000167",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.32",
                    "supporting_stat_value": 0.32,
                    "game_pk": "2024000167",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_110",
                    "supporting_stat_value": 110,
                    "game_pk": "2024000167",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_era_5.8",
                    "supporting_stat_value": 5.8,
                    "game_pk": "2024000167",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000167",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.33",
                    "supporting_stat_value": 0.33,
                    "game_pk": "2024000167",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000167",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_87",
                    "supporting_stat_value": 87,
                    "game_pk": "2024000167",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_ops_0.834",
                    "supporting_stat_value": 0.834,
                    "game_pk": "2024000167",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.48",
                    "supporting_stat_value": 0.48,
                    "game_pk": "2024000167",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000167",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000167-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000167-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000167/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000167-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "advance_scouting",
                    "status_code": 200,
                    "logs_ingested": 21
                }
            }
        ],
        "outputs": [
                "RPT-2024000167-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task77",
        "instruction": "Function as the scouting representative.. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', compose a compliant pre-series scouting bundle: each pitcher must have an insight set across five required categories (deterministic templates, computed metrics); persist one PDF report and one video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; ensure distribution to '#coaches-prep'; and log readiness with source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task78",
        "instruction": "Serve as the analytics coordinator for the home side.. For gamePk '2024000172' on date '2024-11-22', organize comprehensive in-game monitoring with real-time alerts (leverage_index 2.0, is_manual_alert False, suggestion_text 'rhythm monitoring'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 73), and complete monitoring workflow lifecycle. Provide 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000172"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000172",
                    "artifact_name": "12x12_catcher_view"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-22"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-22"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000172",
                    "leverage_index": 2.0,
                    "is_manual_alert": false,
                    "suggestion_text": "rhythm monitoring"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 73
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000172",
                    "final_output": "ok"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task79",
        "instruction": "Engage as the official analytics resource for this club.. For gamePk '2024000182' on date '2024-12-02', arrange comprehensive in-game monitoring with real-time alerts (leverage_index 2.6, is_manual_alert False, suggestion_text 'momentum evaluation'), spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 77), and complete monitoring workflow lifecycle. Provide 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000182"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-02"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-02"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000182",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000182",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000182",
                    "leverage_index": 2.6,
                    "is_manual_alert": false,
                    "suggestion_text": "momentum evaluation"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 77
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000182"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task80",
        "instruction": "Operate as the recognized analytics agent for the home squad.. Present a pre-series scouting bundle for opponent team id 13 on date '2024-12-05' with gamePk '2024000185'. The package should fulfill these acceptance criteria: pitcher 101 includes 5 observations (tendency_slider_usage_0.33, execution_contact_rate_0.73, stamina_pitch_count_101, situational_clutch_era_4.3, predictability_location_score_0.48); pitcher 102 includes 5 observations (tendency_changeup_usage_0.26, execution_first_strike_rate_0.69, stamina_pitch_count_87, situational_pressure_ops_0.714, predictability_timing_score_0.56); ensure inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'intelligence_data' (status_code 200, logs_ingested 39). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-05"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.33",
                    "supporting_stat_value": 0.33,
                    "game_pk": "2024000185",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.73",
                    "supporting_stat_value": 0.73,
                    "game_pk": "2024000185",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_101",
                    "supporting_stat_value": 101,
                    "game_pk": "2024000185",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_era_4.3",
                    "supporting_stat_value": 4.3,
                    "game_pk": "2024000185",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.48",
                    "supporting_stat_value": 0.48,
                    "game_pk": "2024000185",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.26",
                    "supporting_stat_value": 0.26,
                    "game_pk": "2024000185",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.69",
                    "supporting_stat_value": 0.69,
                    "game_pk": "2024000185",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_87",
                    "supporting_stat_value": 87,
                    "game_pk": "2024000185",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_ops_0.714",
                    "supporting_stat_value": 0.714,
                    "game_pk": "2024000185",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.56",
                    "supporting_stat_value": 0.56,
                    "game_pk": "2024000185",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000185",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000185-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000185-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000185/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000185-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "intelligence_data",
                    "status_code": 200,
                    "logs_ingested": 39
                }
            }
        ],
        "outputs": [
                "RPT-2024000185-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task81",
        "instruction": "Function as the analytics agent for the home team. Compile a pre-series scouting bundle for opponent team id 13 on date '2024-10-21' with gamePk '2024000099'. Ensure the package meets these acceptance criteria: pitcher 101 should have 5 observations (tendency_sinker_usage_0.41, execution_ground_ball_rate_0.58, stamina_pitch_count_85, situational_runner_scoring_era_5.2, predictability_release_score_0.29); pitcher 102 should have 5 observations (tendency_cutter_usage_0.22, execution_called_strike_rate_0.31, stamina_pitch_count_112, situational_high_leverage_ops_0.821, predictability_approach_score_0.73); include the internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry from source_name 'tactical_prep' (status_code 200, logs_ingested 15). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-10-21"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.41",
                    "supporting_stat_value": 0.41,
                    "game_pk": "2024000099",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000099",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_85",
                    "supporting_stat_value": 85,
                    "game_pk": "2024000099",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_runner_scoring_era_5.2",
                    "supporting_stat_value": 5.2,
                    "game_pk": "2024000099",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.29",
                    "supporting_stat_value": 0.29,
                    "game_pk": "2024000099",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_cutter_usage_0.22",
                    "supporting_stat_value": 0.22,
                    "game_pk": "2024000099",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000099",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_112",
                    "supporting_stat_value": 112,
                    "game_pk": "2024000099",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_high_leverage_ops_0.821",
                    "supporting_stat_value": 0.821,
                    "game_pk": "2024000099",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.73",
                    "supporting_stat_value": 0.73,
                    "game_pk": "2024000099",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000099",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000099-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000099-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000099/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000099-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "tactical_prep",
                    "status_code": 200,
                    "logs_ingested": 15
                }
            }
        ],
        "outputs": [
                "RPT-2024000099-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task82",
        "instruction": "Operate as the official scouting representative. For opponent team id 13 on date '2024-09-19' with gamePk '2024000059', prepare and send out a complete pre-series scouting intelligence package. Utilize internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1, post to channel '#coaches-prep', and return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-19"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_table"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000059",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000059",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000059",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000059",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000059",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000059",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000059",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000059",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000059",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000059",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000059",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000059",
                    "s3_pdf_path": "s3://reports/2024000059/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000059-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000059-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000059/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000059-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000059-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task83",
        "instruction": "Serve as the pre-series analytics agent for the club. For gamePk '2024000194' on date '2024-12-14', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 1.8, is_manual_alert False, suggestion_text 'performance adjustment'), ensure spatial data tracking with artifact '12x12_catcher_view' quality validation, model freshness certification, data ingestion logging (source_name 'in_game_snapshot', status_code 200, logs_ingested 73), and complete the monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000194"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-14"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-14"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000194",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000194",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000194",
                    "leverage_index": 1.8,
                    "is_manual_alert": false,
                    "suggestion_text": "performance adjustment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 73
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000194"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task84",
        "instruction": "Act as the official scouting delegate for this series. For opponent team id 13 on date '2024-07-24' with gamePk '2024000013', produce a pre-series scouting package in line with policy: generate per-pitcher insights (five categories, deterministic templates, computed values); create and maintain a PDF report plus a single video playlist using internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1; dispatch to '#coaches-prep'; and conclude with a readiness log entry from source_name 'dq_pre_series_day2' (status_code 200, logs_ingested 0). The report id should be returned.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-07-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000013",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000013",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000013",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000013",
                    "s3_pdf_path": "s3://reports/2024000013/pre-series_report.pdf",
                    "insights_data": "flags_leverage",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000013-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000013/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000013-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "dq_pre_series_day2",
                    "status_code": 200,
                    "logs_ingested": 0
                }
            }
        ],
        "outputs": [
                "RPT-2024000013-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task85",
        "instruction": "Take charge of preparing the official scouting material. Assemble a pre-series scouting bundle for opponent team id 13 on date '2024-11-09' with gamePk '2024000159'. Ensure the package meets these acceptance criteria: pitcher 101 must have 5 observations (tendency_sinker_usage_0.44, execution_contact_rate_0.76, stamina_pitch_count_92, situational_risp_era_4.2, predictability_release_score_0.47); pitcher 102 must have 5 observations (tendency_splitter_usage_0.21, execution_called_strike_rate_0.63, stamina_pitch_count_108, situational_bases_loaded_ops_0.813, predictability_location_score_0.35); include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and log an ingestion record entry with source_name 'defensive_prep' (status_code 200, logs_ingested 13). Submit the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-09"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.44",
                    "supporting_stat_value": 0.44,
                    "game_pk": "2024000159",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.76",
                    "supporting_stat_value": 0.76,
                    "game_pk": "2024000159",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_92",
                    "supporting_stat_value": 92,
                    "game_pk": "2024000159",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_4.2",
                    "supporting_stat_value": 4.2,
                    "game_pk": "2024000159",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.47",
                    "supporting_stat_value": 0.47,
                    "game_pk": "2024000159",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_splitter_usage_0.21",
                    "supporting_stat_value": 0.21,
                    "game_pk": "2024000159",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_called_strike_rate_0.63",
                    "supporting_stat_value": 0.63,
                    "game_pk": "2024000159",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_108",
                    "supporting_stat_value": 108,
                    "game_pk": "2024000159",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_bases_loaded_ops_0.813",
                    "supporting_stat_value": 0.813,
                    "game_pk": "2024000159",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.35",
                    "supporting_stat_value": 0.35,
                    "game_pk": "2024000159",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000159",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000159-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000159-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000159/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000159-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "defensive_prep",
                    "status_code": 200,
                    "logs_ingested": 13
                }
            }
        ],
        "outputs": [
                "RPT-2024000159-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task86",
        "instruction": "As the analytics liaison for the home organization, handle the provision of a pre-series scouting bundle for opponent team id 13 on date '2024-11-27' using gamePk '2024000177'. The package must adhere to these acceptance criteria: pitcher 101 with 5 observations (tendency_fastball_usage_0.64, execution_swing_miss_rate_0.34, stamina_pitch_count_100, situational_pressure_era_3.8, predictability_approach_score_0.49); pitcher 102 with 5 observations (tendency_slider_usage_0.36, execution_contact_rate_0.69, stamina_pitch_count_92, situational_risp_ops_0.731, predictability_timing_score_0.55); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' containing clip_count 1; log an ingestion record with source_name 'competitive_analysis' (status_code 200, logs_ingested 31). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.64",
                    "supporting_stat_value": 0.64,
                    "game_pk": "2024000177",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_swing_miss_rate_0.34",
                    "supporting_stat_value": 0.34,
                    "game_pk": "2024000177",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_100",
                    "supporting_stat_value": 100,
                    "game_pk": "2024000177",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_era_3.8",
                    "supporting_stat_value": 3.8,
                    "game_pk": "2024000177",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.49",
                    "supporting_stat_value": 0.49,
                    "game_pk": "2024000177",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.36",
                    "supporting_stat_value": 0.36,
                    "game_pk": "2024000177",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_contact_rate_0.69",
                    "supporting_stat_value": 0.69,
                    "game_pk": "2024000177",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_92",
                    "supporting_stat_value": 92,
                    "game_pk": "2024000177",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_ops_0.731",
                    "supporting_stat_value": 0.731,
                    "game_pk": "2024000177",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_timing_score_0.55",
                    "supporting_stat_value": 0.55,
                    "game_pk": "2024000177",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000177",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000177-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000177-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000177/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000177-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "competitive_analysis",
                    "status_code": 200,
                    "logs_ingested": 31
                }
            }
        ],
        "outputs": [
                "RPT-2024000177-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task87",
        "instruction": "As the team's scouting and analytics agent, coordinate comprehensive in-game monitoring for gamePk '2024000156' on date '2024-11-06', including real-time alerts (leverage_index 2.8, is_manual_alert False, suggestion_text 'mound visit consideration'), spatial data tracking with '12x12_catcher_view' quality checks, ensure model freshness certification, log data ingestion activities (source_name 'in_game_snapshot', status_code 200, logs_ingested 78), and wrap up the complete monitoring workflow. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000156"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-06"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-06"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000156",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000156",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000156",
                    "leverage_index": 2.8,
                    "is_manual_alert": false,
                    "suggestion_text": "mound visit consideration"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 78
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000156"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task88",
        "instruction": "As the analytics representative for the home team, assemble a pre-series scouting intelligence output for opponent team id 10 on '2024-09-27' using gamePk '2024000067'. Implement advanced stat filtering with min_sample_size 40, include one playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' clip_count 1, and send the results to '#coaches-prep'. Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task89",
        "instruction": "As the official analytics resource for this club, deliver a pre-series scouting bundle for opponent team id 13 on date '2024-09-18' using gamePk '2024000058', meeting policy outcomes: a per-pitcher insight set (5 types as per policies using deterministic templates with metric values from your computed metrics); include a persisted PDF report and a video playlist with internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' and clip_count 1; distribute to '#coaches-prep'; and ensure a readiness log with source_name 'final_prep_check' (status_code 200, logs_ingested 1). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-18"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000058",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.72",
                    "supporting_stat_value": 0.72,
                    "game_pk": "2024000058",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_95",
                    "supporting_stat_value": 95,
                    "game_pk": "2024000058",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_risp_era_3.2",
                    "supporting_stat_value": 3.2,
                    "game_pk": "2024000058",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_sequence_score_0.45",
                    "supporting_stat_value": 0.45,
                    "game_pk": "2024000058",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_slider_usage_0.28",
                    "supporting_stat_value": 0.28,
                    "game_pk": "2024000058",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_whiff_rate_0.31",
                    "supporting_stat_value": 0.31,
                    "game_pk": "2024000058",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_88",
                    "supporting_stat_value": 88,
                    "game_pk": "2024000058",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.875",
                    "supporting_stat_value": 0.875,
                    "game_pk": "2024000058",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_count_leverage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000058",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_leverage"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000058",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000058-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000058-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000058/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000058-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "final_prep_check",
                    "status_code": 200,
                    "logs_ingested": 1
                }
            }
        ],
        "outputs": [
                "RPT-2024000058-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task90",
        "instruction": "Serving as the recognized analytics agent for the home squad, deliver an in-game monitoring outcome for gamePk '2024000016' on date '2024-07-26' that aligns with these acceptance criteria: log one alert with leverage_index 1.6, is_manual_alert False, suggestion_text 'monitor usage drift'; ensure live pitch tracking is normalized, with the persisted artifact '12x12_catcher_view' passing a quality check; models for the date are verified as fresh; confirm the existence of an ingestion record entry with source_name 'in_game_snapshot' (status_code 200, logs_ingested 50); and conclude with the real-time monitoring flow marked complete. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000016"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000016",
                    "artifact_name": "12x12_catcher_view"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-07-26"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-07-26"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000016",
                    "leverage_index": 1.6,
                    "is_manual_alert": false,
                    "suggestion_text": "monitor usage drift"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 50
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000016",
                    "final_output": "ok"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task91",
        "instruction": "Handle the role of analytics agent for the home team. For gamePk '2024000166' on date '2024-11-16', initiate comprehensive in-game monitoring with real-time alerts (leverage_index 2.7, is_manual_alert False, suggestion_text 'fatigue assessment'), and ensure spatial data tracking with artifact '12x12_catcher_view' quality validation. Certify model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 82), and manage the complete monitoring workflow lifecycle. Respond with 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000166"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-16"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-16"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000166",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000166",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000166",
                    "leverage_index": 2.7,
                    "is_manual_alert": false,
                    "suggestion_text": "fatigue assessment"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 82
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000166"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task92",
        "instruction": "Act as the designated analytics representative. For opponent team id 10 on date '2024-09-27' with gamePk '2024000067', develop a pre-series scouting intelligence deliverable. Conduct advanced statistical analysis with a minimum sample size of 40. Create a single playlist at internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Share in '#coaches-prep' and provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task93",
        "instruction": "Function as the home club's analytics lead. For opponent team id 10 on '2024-09-27' with gamePk '2024000067', compile a scouting package for pre-series intelligence. Employ statistical methods with a minimum sample size of 40. Deliver exactly one video playlist via internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Upload to '#coaches-prep' and return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-27"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 40,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000067",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000067",
                    "s3_pdf_path": "s3://reports/2024000067/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000067-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000067-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000067/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000067-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000067-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task94",
        "instruction": "Serve in the capacity of the home club's analytics lead. Deliver a pre-series scouting bundle for opponent team id 13 on date '2024-11-11' with gamePk '2024000161'. The package must meet these acceptance criteria: pitcher 101 with 5 observations (tendency_changeup_usage_0.26, execution_ground_ball_rate_0.49, stamina_pitch_count_101, situational_pressure_era_3.6, predictability_pattern_score_0.58); pitcher 102 with 5 observations (tendency_fastball_usage_0.62, execution_strike_rate_0.74, stamina_pitch_count_93, situational_lefty_ops_0.687, predictability_approach_score_0.44); ensure the inclusion of internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and record an ingestion log entry with source_name 'strategy_prep' (status_code 200, logs_ingested 15). Return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-11-11"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_changeup_usage_0.26",
                    "supporting_stat_value": 0.26,
                    "game_pk": "2024000161",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.49",
                    "supporting_stat_value": 0.49,
                    "game_pk": "2024000161",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_101",
                    "supporting_stat_value": 101,
                    "game_pk": "2024000161",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_era_3.6",
                    "supporting_stat_value": 3.6,
                    "game_pk": "2024000161",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_pattern_score_0.58",
                    "supporting_stat_value": 0.58,
                    "game_pk": "2024000161",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.62",
                    "supporting_stat_value": 0.62,
                    "game_pk": "2024000161",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_strike_rate_0.74",
                    "supporting_stat_value": 0.74,
                    "game_pk": "2024000161",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_93",
                    "supporting_stat_value": 93,
                    "game_pk": "2024000161",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_lefty_ops_0.687",
                    "supporting_stat_value": 0.687,
                    "game_pk": "2024000161",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_approach_score_0.44",
                    "supporting_stat_value": 0.44,
                    "game_pk": "2024000161",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000161",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000161-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000161-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000161/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000161-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "strategy_prep",
                    "status_code": 200,
                    "logs_ingested": 15
                }
            }
        ],
        "outputs": [
                "RPT-2024000161-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task95",
        "instruction": "Undertake the preparation of the official scouting material. For opponent team id 10 on date '2024-08-01' with gamePk '2024000023', create and distribute a pre-series scouting intelligence package utilizing advanced statistical analysis with a minimum sample size of 30. Utilize internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Post to the '#coaches-prep' channel and return the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 10
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 10,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-08-01"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 30,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000023",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000023",
                    "s3_pdf_path": "s3://reports/2024000023/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000023-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000023-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000023/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000023-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000023-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task96",
        "instruction": "Handle your role as the analytics liaison for the home organization.. For gamePk '2024000196' on date '2024-12-16', set up thorough in-game monitoring with real-time notifications (leverage_index 2.9, is_manual_alert False, suggestion_text 'execution focus'), carry out spatial data tracking with artifact '12x12_catcher_view' quality validation, confirm model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 81), and complete the entire monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000196"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-12-16"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-12-16"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000196",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000196",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000196",
                    "leverage_index": 2.9,
                    "is_manual_alert": false,
                    "suggestion_text": "execution focus"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 81
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000196"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task97",
        "instruction": "Coordinate your duties as the team's scouting and analytics agent.. For gamePk '2024000170' on date '2024-11-20', set up thorough in-game monitoring with real-time notifications (leverage_index 3.3, is_manual_alert False, suggestion_text 'matchup optimization'), carry out spatial data tracking with artifact '12x12_catcher_view' quality validation, confirm model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 96), and complete the entire monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000170"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-20"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-20"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000170",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000170",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000170",
                    "leverage_index": 3.3,
                    "is_manual_alert": false,
                    "suggestion_text": "matchup optimization"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 96
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000170"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task98",
        "instruction": "Tasked as the analytics coordinator for your home side.. For opponent team id 9 on date '2024-09-24' with gamePk '2024000064', compile tactical scouting intelligence using advanced statistical analysis with min_sample_size 35 and comprehensive video evidence collection. Utilize the internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1. Upload to the channel '#coaches-prep' and provide the tactical report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 9
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "team_id": 9,
                    "time_window": "last_6w_and_season"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-09-24"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "sizes",
                "arguments": {
                    "min_sample_size": 35,
                    "source_table": "flags_leverage"
                },
            },
            {
                "name": "vidMani",
                "arguments": {
                    "insights": "flags_filtered_sample"
                },
            },
            {
                "name": "makeVidList",
                "arguments": {
                    "manifest": "manifest_001",
                    "tool": "ffmpeg"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_filtered_sample",
                    "game_pk": "2024000064",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "report",
                "arguments": {
                    "report_type": "pre-series",
                    "game_pk": "2024000064",
                    "s3_pdf_path": "s3://reports/2024000064/pre-series_report.pdf",
                    "insights_data": "flags_filtered_sample",
                    "video_data": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ]
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000064-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000064-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000064/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000064-pre-series"
                }
            }
        ],
        "outputs": [
                "RPT-2024000064-pre-series"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task99",
        "instruction": "Engage as the official analytics resource for this club.. For gamePk '2024000158' on date '2024-11-08', set up thorough in-game monitoring with real-time notifications (leverage_index 1.9, is_manual_alert False, suggestion_text 'pitch count awareness'), carry out spatial data tracking with artifact '12x12_catcher_view' quality validation, confirm model freshness, log data ingestion (source_name 'in_game_snapshot', status_code 200, logs_ingested 54), and complete the entire monitoring workflow lifecycle. Return 'ok'.",
        "actions": [
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "running",
                    "game_pk": "2024000158"
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "date": "2024-11-08"
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "model_freshness",
                    "status": "success",
                    "report_id": "FRESH-2024-11-08"
                },
            },
            {
                "name": "getPitch",
                "arguments": {
                    "game_pk": "2024000158",
                    "time_window": "live"
                },
            },
            {
                "name": "norming",
                "arguments": {
                    "source_table": "pitches_live"
                },
            },
            {
                "name": "dataPoll",
                "arguments": {
                    "data_inputs": [
                        "12x12_catcher_view"
                    ]
                },
            },
            {
                "name": "spatArt",
                "arguments": {
                    "game_pk": "2024000158",
                    "artifact_name": "12x12_catcher_view",
                    "qc_status": "passed"
                },
            },
            {
                "name": "makeEvent",
                "arguments": {
                    "game_pk": "2024000158",
                    "leverage_index": 1.9,
                    "is_manual_alert": false,
                    "suggestion_text": "pitch count awareness"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "in_game_snapshot",
                    "status_code": 200,
                    "logs_ingested": 54
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "in_game",
                    "status": "completed",
                    "game_pk": "2024000158"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task100",
        "instruction": "Serve as the recognized analytics agent for the home squad.. Deliver a pre-series scouting bundle for opponent team id 13 on date '2024-12-19' with gamePk '2024000199'. Ensure the package aligns with these acceptance criteria: pitcher 101 has 5 observations (tendency_sinker_usage_0.42, execution_ground_ball_rate_0.59, stamina_pitch_count_106, situational_clutch_era_3.5, predictability_release_score_0.50); pitcher 102 has 5 observations (tendency_fastball_usage_0.65, execution_first_strike_rate_0.68, stamina_pitch_count_91, situational_pressure_ops_0.793, predictability_location_score_0.34); make certain to include internal_portal_link 'portal://playlist/opponent_pitcher_tendencies' with clip_count 1; and document an ingestion record entry with source_name 'series_finale' (status_code 200, logs_ingested 53). Provide the report id.",
        "actions": [
            {
                "name": "findPitch",
                "arguments": {
                    "team_id": 13
                },
            },
            {
                "name": "dbMod",
                "arguments": {
                    "tags": [
                        "pre_series_analysis"
                    ],
                    "date": "2024-12-19"
                },
            },
            {
                "name": "mappings",
                "arguments": {
                    "source_table": "historical_pitches"
                },
            },
            {
                "name": "getStats",
                "arguments": {
                    "source_table": "pitches_canonical"
                },
            },
            {
                "name": "rules",
                "arguments": {
                    "dbt_output_tables": [
                        "key_metrics"
                    ]
                },
            },
            {
                "name": "cutOut",
                "arguments": {
                    "source_table": "flags_table"
                },
            },
            {
                "name": "levCut",
                "arguments": {
                    "leverage_threshold": 1.5,
                    "source_table": "flags_actionable"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_sinker_usage_0.42",
                    "supporting_stat_value": 0.42,
                    "game_pk": "2024000199",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_ground_ball_rate_0.59",
                    "supporting_stat_value": 0.59,
                    "game_pk": "2024000199",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_106",
                    "supporting_stat_value": 106,
                    "game_pk": "2024000199",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_clutch_era_3.5",
                    "supporting_stat_value": 3.5,
                    "game_pk": "2024000199",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_release_score_0.50",
                    "supporting_stat_value": 0.5,
                    "game_pk": "2024000199",
                    "pitcher_id": "101"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "tendency",
                    "insight_text": "tendency_fastball_usage_0.65",
                    "supporting_stat_value": 0.65,
                    "game_pk": "2024000199",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "execution",
                    "insight_text": "execution_first_strike_rate_0.68",
                    "supporting_stat_value": 0.68,
                    "game_pk": "2024000199",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "stamina",
                    "insight_text": "stamina_pitch_count_91",
                    "supporting_stat_value": 91,
                    "game_pk": "2024000199",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "situational",
                    "insight_text": "situational_pressure_ops_0.793",
                    "supporting_stat_value": 0.793,
                    "game_pk": "2024000199",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makeIn",
                "arguments": {
                    "insight_type": "predictability",
                    "insight_text": "predictability_location_score_0.34",
                    "supporting_stat_value": 0.34,
                    "game_pk": "2024000199",
                    "pitcher_id": "102"
                },
            },
            {
                "name": "makePdf",
                "arguments": {
                    "insights": "flags_leverage",
                    "game_pk": "2024000199",
                    "report_type": "pre-series"
                },
            },
            {
                "name": "makeVid",
                "arguments": {
                    "report_id": "RPT-2024000199-pre-series",
                    "internal_portal_link": "portal://playlist/opponent_pitcher_tendencies",
                    "clip_count": 1
                },
            },
            {
                "name": "wrokingRun",
                "arguments": {
                    "dag_name": "scouting",
                    "status": "success",
                    "report_id": "RPT-2024000199-pre-series"
                },
            },
            {
                "name": "postings",
                "arguments": {
                    "channel": "#coaches-prep",
                    "report_link": "s3://reports/2024000199/pre-series_report.pdf",
                    "playlist_links": [
                        "portal://playlist/opponent_pitcher_tendencies"
                    ],
                    "report_id": "RPT-2024000199-pre-series"
                },
            },
            {
                "name": "makeLogs",
                "arguments": {
                    "source_name": "series_finale",
                    "status_code": 200,
                    "logs_ingested": 53
                }
            }
        ],
        "outputs": [
                "RPT-2024000199-pre-series"
        ]
    }
]
