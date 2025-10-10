from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "You are responsible for San Francisco (NOAA station 9414290). "
            "Execute the Merge Window Protocol (MWP) with parameters: "
            "city='San Francisco', station_id='9414290', "
            "analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z, "
            "water-level lookback=2024-02-14T00:00:00Z..2024-03-15T00:00:00Z. "
            "After the MWP completes, report the stored AUC and Accuracy for model_name='flood_risk_sf_v1'."
        ),
        actions=[
            Action(name="get_weather_forecast", kwargs={
                "city": "San Francisco",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="get_tide_predictions", kwargs={
                "station_id": "9414290",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="get_water_levels", kwargs={
                "station_id": "9414290",
                "start_ts": "2024-02-14T00:00:00Z",
                "end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240315.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                   "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[
            "run_id=etl_sf_20240315_20240322_merge_v1",
            "AUC=0.87",
            "Accuracy=0.82"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "You are responsible for San Francisco data preparation. "
            "Execute the Split Protocol (SP) for city='San Francisco' with method='time_based', "
            "test_fraction from '/config/model_config.json' and split_ts='2024-03-17T10:45:00Z'. "
            "Report the resulting train and test counts and the canonical split_summary_json_path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"
            }),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"
            }),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                "city_slug": "sf",
                "method": "time_based",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[
            "train=134",
            "test=34",
            "path=/data/splits/sf_time_based_split_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "You are responsible for Miami data preparation. Execute the Split Protocol (SP) for city='Miami' "
            "with method='time_based', using test_fraction from '/config/model_config.json', "
            "and split_ts='2024-02-03T10:45:00Z'. Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-03T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240203.json",
                "split_ts": "2024-02-03T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240203.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "You are responsible for Boston data preparation. Execute the Split Protocol (SP) for city='Boston' with method='time_based', "
            "using test_fraction from '/config/model_config.json' and split_ts='2024-03-04T10:45:00Z'. "
            "Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-04T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240304.json",
                "split_ts": "2024-03-04T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240304.json",
            "train=96",
            "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "You are responsible for Seattle ingestion. Execute the MWP for city='Seattle', station_id='9447130', analysis window=2024-02-01T00:00:00Z..2024-02-08T00:00:00Z "
            "with a water-level lookback 2024-01-15T00:00:00Z..2024-02-01T00:00:00Z. Report the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240201.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240201_20240208_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240201_20240208.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_700",
        instruction=(
            "You need a reproducible time-based split for San Francisco so late-March evaluation can be replayed consistently. "
            "Use the policy test fraction from '/config/model_config_v2.json' and anchor the split at 2024-03-14T16:45:00Z. "
            "Persist the canonical split summary for the San Francisco processed series and return the path with the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 126,
                "test_index_count": 42,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            }),
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240314.json",
            "train=126",
            "test=42"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "You are responsible for San Francisco data preparation. Execute SP for city='San Francisco' with method='time_based', "
            "using test_fraction from '/config/model_config.json' and split_ts='2024-03-20T10:45:00Z'. "
            "Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-20T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240320.json",
                "split_ts": "2024-03-20T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240320.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "You are responsible for San Francisco ingestion. Execute the Merge Window Protocol (MWP) for city='San Francisco', station_id='9414290', "
            "analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z with a water-level lookback ending at the window start "
            "(2024-02-14T00:00:00Z..2024-03-15T00:00:00Z). Report the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240315_20240322_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240315_20240322.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "You are responsible for Seattle data preparation. Execute the Split Protocol (SP) for city='Seattle' with method='time_based', "
            "using test_fraction from '/config/model_config.json' and split_ts='2024-02-04T10:45:00Z'. "
            "Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-04T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240204.json",
                "split_ts": "2024-02-04T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240204.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "You are responsible for Boston ingestion. Execute the Merge Window Protocol (MWP) for city='Boston', station_id='8443970', "
            "analysis window=2024-03-01T00:00:00Z..2024-03-06T00:00:00Z with a water-level lookback ending at the window start "
            "(2024-02-15T00:00:00Z..2024-03-01T00:00:00Z). Report the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-01T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": ["/data/raw/weather_boston_20240301.json", "/data/raw/tide_pred_8443970.json", "/data/raw/water_levels_8443970.json"],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240301_20240306.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_boston_20240301_20240306_merge_v1",
            "merged_path=/processed_data/merged_timeseries_boston_20240301_20240306.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "You are responsible for Miami data preparation. Execute the Split Protocol (SP) for city='Miami' with method='time_based', "
            "using test_fraction from '/config/model_config.json' and split_ts='2024-02-04T12:00:00Z'. "
            "Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-04T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240204.json",
                "split_ts": "2024-02-04T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240204.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "You must execute the Split Protocol (SP) for city='San Francisco' with method='time_based', using test_fraction from "
            "'/config/model_config.json' and split_ts='2024-03-21T10:45:00Z'. "
            "You must report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-21T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240321.json",
                "split_ts": "2024-03-21T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240321.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "You must execute the Split Protocol (SP) for city='Miami' with method='time_based', using test_fraction from "
            "'/config/model_config.json' and split_ts='2024-02-01T10:45:00Z'. "
            "You must report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json",
                "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240201.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "You must execute the Merge Window Protocol (MWP) for San Francisco, station_id='9414290', with analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z "
            "and a water-level lookback of 2024-02-14T00:00:00Z..2024-03-15T00:00:00Z. You must report the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240315_20240322_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240315_20240322.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "You are preparing a hydrometeorology ingest audit for Seattle. Build the merged analysis artifact using the Merge Window Protocol "
            "for city='Seattle' with station_id='9447130', the analysis window from '2024-02-01T00:00:00Z' to '2024-02-08T00:00:00Z', and a water-level lookback from "
            "'2024-01-15T00:00:00Z' up to '2024-02-01T00:00:00Z'. Your deliverable is the ETL run identifier and the merged CSV path named by the city slug and dates."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240201.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240201_20240208_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240201_20240208.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "You need an auditable time-based split for Miami to support backtesting. Use city='Miami' and method='time_based' with split_ts='2024-02-01T10:45:00Z'; "
            "derive the test fraction from '/config/model_config.json'. The underlying processed series for Miami has 96 hourly rows for this period, "
            "so the canonical split summary must record train=76 and test=20 under the path '/data/splits/miami_time_based_split_20240201.json'. Your deliverable is the split path and the two counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json",
                "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240201.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "You need a deterministic time-based split for San Francisco to support a compliance backtest. Use city='San Francisco' with method='time_based' and split_ts='2024-03-20T10:45:00Z'. "
            "The processed SF series for this period has 168 hourly rows; with the test fraction from '/config/model_config.json', "
            "the canonical split must record train=134 and test=34 under '/data/splits/sf_time_based_split_20240320.json'. Your deliverable is the split path and the two counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-20T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240320.json",
                "split_ts": "2024-03-20T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240320.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "You are documenting the Boston ingest state for a stakeholder handoff. Build the merged analysis artifact using the Merge Window Protocol for city='Boston' "
            "with station_id='8443970', the analysis window from '2024-03-01T00:00:00Z' to '2024-03-06T00:00:00Z', and a water-level lookback from "
            "'2024-02-15T00:00:00Z' up to '2024-03-01T00:00:00Z'. Your deliverable is the ETL run identifier and the merged CSV path named by the city slug and dates."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-01T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": ["/data/raw/weather_boston_20240301.json", "/data/raw/tide_pred_8443970.json", "/data/raw/water_levels_8443970.json"],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240301_20240306.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_boston_20240301_20240306_merge_v1",
            "merged_path=/processed_data/merged_timeseries_boston_20240301_20240306.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_410",
        instruction=(
            "You need a reproducible time-based split that locks Seattle’s mid-March evaluation for downstream training. "
            "Use the policy test fraction from '/config/model_config_v2.json' and anchor the split at 2024-03-14T16:45:00Z. "
            "Persist the canonical split summary for the Seattle processed series and return the path together with the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240314.json",
            "train=180",
            "test=60"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "You are producing a Seattle-only split catalog entry. Create a time-based split for city='Seattle' with split_ts='2024-02-03T12:00:00Z'. "
            "The processed Seattle series has 240 rows and the test fraction comes from '/config/model_config.json', so the split must record "
            "train=192 and test=48 at '/data/splits/seattle_time_based_split_20240203.json'. Your deliverable is the split path and the two counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-03T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240203.json",
                "split_ts": "2024-02-03T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240203.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "You are producing a Boston-only split record for reproducible evaluation. Use city='Boston' with method='time_based' and split_ts='2024-03-01T10:45:00Z'. "
            "The processed Boston series has 120 hourly rows; using the test fraction from '/config/model_config.json', the split must record "
            "train=96 and test=24 at '/data/splits/boston_time_based_split_20240301.json'. Your deliverable is the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240301.json",
            "train=96",
            "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "You are preparing a San Francisco ingestion-only proof for a data lineage review. Build the merged analysis artifact for city='San Francisco' with station_id='9414290', "
            "the analysis window from '2024-03-15T00:00:00Z' to '2024-03-22T00:00:00Z', and a water-level lookback from '2024-02-14T00:00:00Z' to '2024-03-15T00:00:00Z'. "
            "Your deliverable is the ETL run identifier and the merged CSV path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240315_20240322_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240315_20240322.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "You are validating Miami features for portability of a baseline model. Use the Feature Validation Protocol for city='Miami' and model_name='simple_model' "
            "against '/processed_data/features.csv' with validation timestamp '2024-03-17T10:15:00Z'. Report the coverage counts and the validation JSON path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_model_features", kwargs={
                "model_name": "simple_model"}),
            Action(name="build_features_csv_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "miami", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="build_feature_validation_run_id", kwargs={
                   "city_slug": "miami", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_miami_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_miami_simple_model_20240317.json"],
                "started_ts": "2024-03-17T10:20:00Z",
                "finished_ts_nullable": "2024-03-17T10:25:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_miami_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "present=3",
            "required=3",
            "missing_count=0",
            "validation_path=/processed_data/feature_validation_miami_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_403",
        instruction=(
            "You want a deterministic split snapshot for Boston to backtest early-March runs. "
            "Use the test fraction from '/processed_data/boston_model_config.json' and anchor the split at 2024-03-01T13:18:00Z. "
            "Persist the canonical split summary for the Boston processed series and return the path plus the train/test sizes."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240301.json",
            "train=90",
            "test=30"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "You are validating baseline features for Boston as part of a portability check. Use the Feature Validation Protocol for city='Boston' and model_name='simple_model' "
            "against '/processed_data/features.csv' with validation timestamp '2024-03-17T10:15:00Z'. Report the coverage counts and the validation JSON path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_model_features", kwargs={
                "model_name": "simple_model"}),
            Action(name="build_features_csv_path",
                   kwargs={"city_slug": "boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="build_feature_validation_run_id", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-17T10:20:00Z",
                "finished_ts_nullable": "2024-03-17T10:25:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "present=3",
            "required=3",
            "missing_count=0",
            "validation_path=/processed_data/feature_validation_boston_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "You are cataloging a San Francisco split-only artifact for late-window evaluation. Create a time-based split for city='San Francisco' with split_ts='2024-03-21T10:45:00Z'. "
            "The processed SF series has 168 rows; using the test fraction from '/config/model_config.json', the split must record train=134 and test=34 "
            "at '/data/splits/sf_time_based_split_20240321.json'. Your deliverable is the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-21T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240321.json",
                "split_ts": "2024-03-21T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240321.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "You are preparing an ingestion verification for San Francisco. Build the merged analysis artifact with the Merge Window Protocol for city='San Francisco' "
            "and station_id='9414290' across '2024-03-12T00:00:00Z' to '2024-03-16T00:00:00Z', using a water-level lookback from '2024-02-26T00:00:00Z' to '2024-03-12T00:00:00Z'. "
            "The merged file must be '/processed_data/merged_timeseries_sf_20240312_20240316.csv'. Record the ETL run as run_id='etl_sf_20240312_20240316_merge_v1' "
            "with started_ts='2024-03-18T09:00:00Z' and finished_ts='2024-03-18T09:18:00Z'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-26T00:00:00Z", "end_ts": "2024-03-12T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240312_20240316_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240312.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240312_20240316.csv"],
                "started_ts": "2024-03-18T09:00:00Z",
                "finished_ts_nullable": "2024-03-18T09:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-12..2024-03-16.",
                    "Attached observed water levels lookback 2024-02-26..2024-03-12.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240312_20240316_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240312_20240316.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "You are producing a Seattle ingestion artifact for a mid-week window. Build the merged file for city='Seattle' with station_id='9447130' from "
            "'2024-02-04T00:00:00Z' to '2024-02-08T00:00:00Z' and a water-level lookback '2024-01-20T00:00:00Z' to '2024-02-04T00:00:00Z'. "
            "Name the output '/processed_data/merged_timeseries_seattle_20240204_20240208.csv' (city_slug='seattle'), and record run_id='etl_seattle_20240204_20240208_merge_v1' "
            "with started_ts='2024-03-18T09:30:00Z' and finished_ts='2024-03-18T09:50:00Z'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-20T00:00:00Z", "end_ts": "2024-02-04T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240204_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240204.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240204_20240208.csv"],
                "started_ts": "2024-03-18T09:30:00Z",
                "finished_ts_nullable": "2024-03-18T09:50:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-04..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-20..2024-02-04.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240204_20240208_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240204_20240208.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "You need a San Francisco time-based split for a late-window review. Use method='time_based' and split_ts='2024-03-19T10:45:00Z' for city='San Francisco'. "
            "Given row_count=168 and test_fraction=0.2 from '/config/model_config.json', the split summary must record train=134 and test=34 at "
            "'/data/splits/sf_time_based_split_20240319.json'. Also use the metadata source '/data/processed/timeseries_sf_weather.csv'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-19T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240319.json",
                "split_ts": "2024-03-19T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240319.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "You need a Seattle time-based split for a 240-row series. For city='Seattle', method='time_based', and split_ts='2024-02-03T12:00:00Z', with test_fraction=0.2 "
            "and metadata at '/data/processed/timeseries_seattle_weather.csv', produce '/data/splits/seattle_time_based_split_20240203.json' with train=192 and test=48."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-03T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240203.json",
                "split_ts": "2024-02-03T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240203.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "You are preparing a Seattle ingestion artifact for audit. Build the merged analysis using the Merge Window Protocol for city='Seattle' "
            "with station_id='9447130', analysis window '2024-02-01T00:00:00Z'..'2024-02-08T00:00:00Z', and water-level lookback '2024-01-15T00:00:00Z'..'2024-02-01T00:00:00Z'. "
            "The merged file must be '/processed_data/merged_timeseries_seattle_20240201_20240208.csv' and the ETL run id must be 'etl_seattle_20240201_20240208_merge_v1' "
            "with started_ts='2024-03-19T09:00:00Z' and finished_ts='2024-03-19T09:18:00Z'. Report the ETL run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240201.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-19T09:00:00Z",
                "finished_ts_nullable": "2024-03-19T09:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240201_20240208_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240201_20240208.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "You are producing a Miami time-based split for reproducible evaluation. Use city='Miami', method='time_based', split_ts='2024-02-01T10:45:00Z', "
            "row_count=96 and test_fraction=0.2 from the configuration. The split summary path must be '/data/splits/miami_time_based_split_20240201.json'. "
            "Report the split path and the train/test counts (train=76, test=20)."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2, "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json", "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240201.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "You need an auditable merged dataset for Miami in early February. For city='Miami' with station_id='8723214', use the analysis window "
            "'2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z' and the water‑level lookback '2024-01-29T00:00:00Z'..'2024-02-02T00:00:00Z'. "
            "Save the artifact to '/processed_data/merged_timeseries_miami_20240202_20240206.csv' under ETL run id 'etl_miami_20240202_20240206_merge_v1' "
            "with started_ts='2024-03-20T08:00:00Z' and finished_ts='2024-03-20T08:18:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-01-29T00:00:00Z", "end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240202_20240206_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240202.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240202_20240206.csv"],
                "started_ts": "2024-03-20T08:00:00Z",
                "finished_ts_nullable": "2024-03-20T08:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-02..2024-02-06",
                    "Attached observed water levels lookback 2024-01-29..2024-02-02",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa"
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240202_20240206_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240202_20240206.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "You want a deterministic time‑based split for San Francisco to lock evaluation reproducibility. For city='San Francisco', set method='time_based' with "
            "split_ts='2024-03-19T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary must be "
            "'/data/splits/sf_time_based_split_20240319.json' with train=134 and test=34. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-19T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240319.json",
                "split_ts": "2024-03-19T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240319.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "You want a Seattle package that fixes the split accounting and confirms baseline coverage. For city='Seattle', set method='time_based' with "
            "split_ts='2024-02-06T12:00:00Z', row_count=240 and test_fraction=0.2 so that '/data/splits/seattle_time_based_split_20240206.json' records train=192 and test=48. "
            "Then validate model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' against the canonical features CSV '/processed_data/features.csv', saving "
            "'/processed_data/feature_validation_seattle_simple_model_20240317.json' under run_id 'fv_seattle_simple_model_20240317_v1' with started_ts='2024-03-20T11:15:00Z' "
            "and finished_ts='2024-03-20T11:17:00Z'. The required features are ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; the available features are the same. "
            "Report the split path and counts, plus present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240206.json",
                "split_ts": "2024-02-06T12:00:00Z"
            }),
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_seattle_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_seattle_simple_model_20240317.json"],
                "started_ts": "2024-03-20T11:15:00Z",
                "finished_ts_nullable": "2024-03-20T11:17:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_seattle_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240206.json",
            "train=192",
            "test=48",
            "present=3",
            "required=3",
            "missing_count=0",
            "validation_path=/processed_data/feature_validation_seattle_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction=(
            "You need an auditable merged dataset for Miami in mid‑February. For city='Miami' with station_id='8723214', use the analysis window "
            "'2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and the water‑level lookback '2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_miami_20240206_20240210.csv' under ETL run id 'etl_miami_20240206_20240210_merge_v1' with "
            "started_ts='2024-03-21T08:10:00Z' and finished_ts='2024-03-21T08:29:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240206.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240206_20240210.csv"],
                "started_ts": "2024-03-21T08:10:00Z",
                "finished_ts_nullable": "2024-03-21T08:29:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-02-02..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240206_20240210_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240206_20240210.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "You are curating Boston artifacts for a migration checklist. For city='Boston', create a time‑based split at split_ts='2024-03-05T10:45:00Z' with "
            "row_count=120 and test_fraction=0.2 so that '/data/splits/boston_time_based_split_20240305.json' records train=96 and test=24. Then validate "
            "model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' against '/processed_data/features.csv', saving "
            "'/processed_data/feature_validation_boston_simple_model_20240317.json' under run_id='fv_boston_simple_model_20240317_v1' with "
            "started_ts='2024-03-21T11:00:00Z' and finished_ts='2024-03-21T11:02:00Z'. Report the split path and counts, plus present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-05T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240305.json",
                "split_ts": "2024-03-05T10:45:00Z"
            }),
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-21T11:00:00Z",
                "finished_ts_nullable": "2024-03-21T11:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240305.json",
            "train=96",
            "test=24",
            "present=3",
            "required=3",
            "missing_count=0",
            "validation_path=/processed_data/feature_validation_boston_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "You want a Boston time‑based split to freeze an early‑March evaluation. For city='Boston', set method='time_based' with split_ts='2024-03-06T10:45:00Z', "
            "row_count=120 and test_fraction=0.2. The split summary must be '/data/splits/boston_time_based_split_20240306.json' with train=96 and test=24. "
            "Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-06T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240306.json",
                "split_ts": "2024-03-06T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240306.json",
            "train=96",
            "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "You need an auditable merged dataset for Miami in mid‑February. For city='Miami' with station_id='8723214', use the analysis window "
            "'2024-02-08T00:00:00Z'..'2024-02-12T00:00:00Z' and the water‑level lookback '2024-02-04T00:00:00Z'..'2024-02-08T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_miami_20240208_20240212.csv' as the output under ETL run id 'etl_miami_20240208_20240212_merge_v1' with "
            "started_ts='2024-03-22T08:05:00Z' and finished_ts='2024-03-22T08:24:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240208_20240212_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240208.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240208_20240212.csv"],
                "started_ts": "2024-03-22T08:05:00Z",
                "finished_ts_nullable": "2024-03-22T08:24:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-08..2024-02-12.",
                    "Attached observed water levels lookback 2024-02-04..2024-02-08.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240208_20240212_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240208_20240212.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "You want a deterministic time‑based split for Boston to freeze an early‑March evaluation. For city='Boston', set method='time_based' with "
            "split_ts='2024-03-03T10:45:00Z', row_count=120 and test_fraction=0.2. The split summary must be "
            "'/data/splits/boston_time_based_split_20240303.json' with train=96 and test=24. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json",
                "split_ts": "2024-03-03T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240303.json",
            "train=96",
            "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_306",
        instruction=(
            "You need a reproducible time-based split that locks Seattle’s mid-March evaluation for downstream training. "
            "Use the policy test fraction from '/config/model_config_v2.json' and anchor the split at 2024-03-14T16:45:00Z. "
            "Persist the canonical split summary for the Seattle processed series and return the path together with the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240314.json",
            "train=180",
            "test=60"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "You are preparing Boston artifacts for a portfolio review that pairs a frozen split with baseline coverage. For city='Boston', create a time‑based split at "
            "split_ts='2024-03-03T10:45:00Z' with row_count=120 and test_fraction=0.2 so that '/data/splits/boston_time_based_split_20240303.json' records train=96 and test=24. "
            "Then validate model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' against '/processed_data/features.csv', saving "
            "'/processed_data/feature_validation_boston_simple_model_20240317.json' under run_id='fv_boston_simple_model_20240317_v1' with started_ts='2024-03-22T12:00:00Z' "
            "and finished_ts='2024-03-22T12:02:00Z'. Report the split path and counts, plus present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2, "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json", "split_ts": "2024-03-03T10:45:00Z"
            }),
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-22T12:00:00Z",
                "finished_ts_nullable": "2024-03-22T12:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240303.json",
            "train=96",
            "test=24",
            "present=3",
            "required=3",
            "missing_count=0",
            "validation_path=/processed_data/feature_validation_boston_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "You need an ingestion‑only proof for San Francisco covering the mid‑March lead‑in. For city='San Francisco' with station_id='9414290', merge the "
            "analysis window '2024-03-11T00:00:00Z'..'2024-03-15T00:00:00Z' with a water‑level lookback '2024-02-25T00:00:00Z'..'2024-03-11T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_sf_20240311_20240315.csv' under run id 'etl_sf_20240311_20240315_merge_v1' with "
            "started_ts='2024-03-22T14:00:00Z' and finished_ts='2024-03-22T14:18:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-25T00:00:00Z", "end_ts": "2024-03-11T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240311_20240315_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240311.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240311_20240315.csv"],
                "started_ts": "2024-03-22T14:00:00Z",
                "finished_ts_nullable": "2024-03-22T14:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-11..2024-03-15.",
                    "Attached observed water levels lookback 2024-02-25..2024-03-11.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240311_20240315_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240311_20240315.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "You are the data scientist responsible for producing a time-based dataset split for San Francisco."
            "Use the model configuration file at /config/model_config.json to obtain test_split_fraction "
            "Use the processed time series at /data/processed/timeseries_sf_weather.csv "
            "(168 rows; 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z) as the source dataset for the split."
            "Create the split summary at /data/splits/sf_time_based_split_20240322.json with method='time_based' "
            "and split_ts='2024-03-22T10:45:00Z'. The resulting split must have train_index_count=134 and"
            "test_index_count=34."
            "Return the split_summary_json_path, train_index_count, test_index_count, and test_fraction as outputs. "
            "Follow the Split Protocol (SP) in the policy."
        ),
        actions=[
            Action(
                name="get_model_config_param",
                kwargs={"saved_json_path": "/config/model_config.json"}
            ),
            Action(
                name="get_processed_timeseries_metadata",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(
                name="create_split_summary_record",
                kwargs={
                    "method": "time_based",
                    "test_fraction": 0.2,
                    "train_index_count": 134,
                    "test_index_count": 34,
                    "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                    "split_ts": "2024-03-22T10:45:00Z"
                }
            ),
        ],
        outputs={
            "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
            "train_index_count": 134,
            "test_index_count": 34,
            "test_fraction": 0.2
        },
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "You are producing a Miami split‑only artifact to support backtesting near the mid‑month. For city='Miami', set method='time_based' with "
            "split_ts='2024-02-05T10:45:00Z', row_count=96 and test_fraction=0.2. The split summary must be '/data/splits/miami_time_based_split_20240205.json' "
            "with train=76 and test=20. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-05T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240205.json",
                "split_ts": "2024-02-05T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240205.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_414",
        instruction=(
            "You need a Miami split record aligned with the baseline policy for the early-February window. "
            "Use the test fraction from '/config/model_config.json' and anchor the split at 2024-02-10T11:00:00Z. "
            "Persist the canonical split summary for the Miami processed series and return the path and the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240210.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "You need an auditable merged dataset for Miami in early February. For city='Miami' with station_id='8723214', use the analysis window "
            "'2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and the water‑level lookback '2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_miami_20240206_20240210.csv' under ETL run id 'etl_miami_20240206_20240210_merge_v1' with "
            "started_ts='2024-03-23T08:10:00Z' and finished_ts='2024-03-23T08:27:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240206.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240206_20240210.csv"],
                "started_ts": "2024-03-23T08:10:00Z",
                "finished_ts_nullable": "2024-03-23T08:27:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-02-02..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240206_20240210_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240206_20240210.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "You want a deterministic time‑based split for Seattle to anchor a mid‑window evaluation. For city='Seattle', set method='time_based' with "
            "split_ts='2024-02-05T12:00:00Z', row_count=240 and test_fraction=0.2. The split summary must be "
            "'/data/splits/seattle_time_based_split_20240205.json' with train=192 and test=48. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-05T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240205.json",
                "split_ts": "2024-02-05T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240205.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_404",
        instruction=(
            "You need a Miami split record that aligns with the baseline policy for the early-February window. "
            "Use the test fraction from '/config/model_config.json' and anchor the split at 2024-02-10T11:00:00Z. "
            "Persist the canonical split summary for the Miami processed series and provide the path and the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240210.json",
            "train=76",
            "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "You need to confirm feature portability for San Francisco before reusing a baseline. Validate city='San Francisco' with model_name='simple_model' "
            "against '/processed_data/features.csv' using created_ts='2024-03-17T10:15:00Z'. Required features are "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; available features are the same. Save to "
            "'/processed_data/feature_validation_sf_simple_model_20240317.json' under run_id='fv_sf_simple_model_20240317_v1' with "
            "started_ts='2024-03-23T09:00:00Z' and finished_ts='2024-03-23T09:02:00Z'. Report present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "sf", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_sf_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_sf_simple_model_20240317.json"],
                "started_ts": "2024-03-23T09:00:00Z",
                "finished_ts_nullable": "2024-03-23T09:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_sf_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "present=3", "required=3", "missing_count=0",
            "validation_path=/processed_data/feature_validation_sf_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "You want to document a San Francisco v2 training run on the late‑March slice. Train model_name='flood_risk_sf_v2' for city='San Francisco' on "
            "'2024-03-15T00:00:00Z'..'2024-03-22T00:00:00Z' using the merged series '/processed_data/merged_timeseries_sf_20240315_20240322.csv' and the time‑based split "
            "'/data/splits/sf_time_based_split_20240320.json' (train=134, test=34). Save the model to '/models/flood_risk_sf_v2.pkl' under run_id "
            "'mt_sf_flood_risk_sf_v2_20240315_20240322_v1' with started_ts='2024-03-23T10:00:00Z' and finished_ts='2024-03-23T10:38:00Z'. "
            "Persist '/processed_data/metrics_summary_flood_risk_sf_v2_20240322.csv'. Report the training run id, model path, and the stored AUC and Accuracy."
        ),
        actions=[
            Action(name="create_etl_run_record", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v2_20240315_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240320.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v2.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v2_20240322.csv"
                ],
                "started_ts": "2024-03-23T10:00:00Z",
                "finished_ts_nullable": "2024-03-23T10:38:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v2.pkl"
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                "model_name": "flood_risk_sf_v2"})
        ],
        outputs=[
            "mt_run_id=mt_sf_flood_risk_sf_v2_20240315_20240322_v1",
            "model_path=/models/flood_risk_sf_v2.pkl",
            "AUC=0.89", "Accuracy=0.85"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "You are curating Boston ingestion artifacts for an audit trail. For city='Boston' with station_id='8443970', use the analysis window "
            "'2024-03-02T00:00:00Z'..'2024-03-06T00:00:00Z' and the water‑level lookback '2024-02-15T00:00:00Z'..'2024-03-02T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_boston_20240302_20240306.csv' under ETL run id 'etl_boston_20240302_20240306_merge_v1' with "
            "started_ts='2024-03-23T11:00:00Z' and finished_ts='2024-03-23T11:20:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_boston_20240302_20240306_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240302.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240302_20240306.csv"],
                "started_ts": "2024-03-23T11:00:00Z",
                "finished_ts_nullable": "2024-03-23T11:20:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-02..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-02.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_boston_20240302_20240306_merge_v1",
            "merged_path=/processed_data/merged_timeseries_boston_20240302_20240306.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "You are validating baseline features for Seattle before a model handoff. For city='Seattle' with model_name='simple_model', validate against "
            "the canonical '/processed_data/features.csv' using created_ts='2024-03-17T10:15:00Z'. Required features are "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; available features are the same. Save "
            "'/processed_data/feature_validation_seattle_simple_model_20240317.json' under run_id='fv_seattle_simple_model_20240317_v1' with "
            "started_ts='2024-03-23T11:45:00Z' and finished_ts='2024-03-23T11:47:00Z'. Report present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="compute_feature_coverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="build_feature_validation_path", kwargs={
                   "city_slug": "seattle", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "fv_seattle_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_seattle_simple_model_20240317.json"],
                "started_ts": "2024-03-23T11:45:00Z",
                "finished_ts_nullable": "2024-03-23T11:47:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_seattle_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[
            "present=3", "required=3", "missing_count=0",
            "validation_path=/processed_data/feature_validation_seattle_simple_model_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_400",
        instruction=(
            "You need a reproducible time-based split that freezes Seattle’s mid-March evaluation for downstream training. "
            "Use the policy test fraction from '/config/model_config_v2.json' and anchor the split at 2024-03-14T16:45:00Z. "
            "Persist the canonical split summary for the Seattle processed series and return the path together with the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240314.json",
            "train=180",
            "test=60"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "You want a San Francisco v1 retraining record on a fixed mid‑March slice. Train model_name='flood_risk_sf_v1' for city='San Francisco' on "
            "'2024-03-12T00:00:00Z'..'2024-03-16T00:00:00Z' using '/processed_data/merged_timeseries_sf_20240312_20240316.csv' and the split "
            "'/data/splits/sf_time_based_split_20240319.json' (train=134, test=34). Save '/models/flood_risk_sf_v1.pkl' under run_id "
            "'mt_sf_flood_risk_sf_v1_20240312_20240316_v1' with started_ts='2024-03-23T12:00:00Z' and finished_ts='2024-03-23T12:30:00Z', and persist "
            "'/processed_data/metrics_summary_flood_risk_sf_v1_20240316.csv'. Report the run id, model path, and the stored AUC and Accuracy."
        ),
        actions=[
            Action(name="create_etl_run_record", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240312_20240316_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240312_20240316.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240319.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240316.csv"
                ],
                "started_ts": "2024-03-23T12:00:00Z",
                "finished_ts_nullable": "2024-03-23T12:30:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[
            "mt_run_id=mt_sf_flood_risk_sf_v1_20240312_20240316_v1",
            "model_path=/models/flood_risk_sf_v1.pkl",
            "AUC=0.87", "Accuracy=0.82"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "You need a Seattle merged artifact centered on a late‑look window. For city='Seattle' with station_id='9447130', use the analysis window "
            "'2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and the water‑level lookback '2024-01-22T00:00:00Z'..'2024-02-06T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_seattle_20240206_20240210.csv' under run id 'etl_seattle_20240206_20240210_merge_v1' with "
            "started_ts='2024-03-23T13:00:00Z' and finished_ts='2024-03-23T13:18:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-22T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240206.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240206_20240210.csv"],
                "started_ts": "2024-03-23T13:00:00Z",
                "finished_ts_nullable": "2024-03-23T13:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-01-22..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240206_20240210_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240206_20240210.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "You need a San Francisco time‑based split to freeze a mid‑March evaluation. For city='San Francisco', set method='time_based' with "
            "split_ts='2024-03-18T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary must be '/data/splits/sf_time_based_split_20240318.json' "
            "with train=134 and test=34. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-18T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240318.json",
                "split_ts": "2024-03-18T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240318.json",
            "train=134", "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "You want a regulator‑ready Miami merge for a mid‑February window. For city='Miami' (station_id='8723214'), use the analysis window "
            "'2024-02-10T00:00:00Z'..'2024-02-14T00:00:00Z' and the water‑level lookback '2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z'. Persist "
            "'/processed_data/merged_timeseries_miami_20240210_20240214.csv' under run id 'etl_miami_20240210_20240214_merge_v1' with "
            "started_ts='2024-03-23T14:00:00Z' and finished_ts='2024-03-23T14:19:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240210_20240214_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240210.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240210_20240214.csv"],
                "started_ts": "2024-03-23T14:00:00Z",
                "finished_ts_nullable": "2024-03-23T14:19:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-10..2024-02-14.",
                    "Attached observed water levels lookback 2024-02-06..2024-02-10.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240210_20240214_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240210_20240214.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "You want a Boston time‑based split to freeze an early‑March evaluation. For city='Boston', set method='time_based' with split_ts='2024-03-06T10:45:00Z', "
            "row_count=120 and test_fraction=0.2. The split summary must be '/data/splits/boston_time_based_split_20240306.json' with train=96 and test=24. "
            "Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-06T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240306.json",
                "split_ts": "2024-03-06T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240306.json",
            "train=96", "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "You need a Seattle merged artifact for an early‑February window. For city='Seattle' with station_id='9447130', use the analysis window "
            "'2024-02-04T00:00:00Z'..'2024-02-08T00:00:00Z' and the water‑level lookback '2024-01-20T00:00:00Z'..'2024-02-04T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_seattle_20240204_20240208.csv' under run id 'etl_seattle_20240204_20240208_merge_v1' with "
            "started_ts='2024-03-23T15:50:00Z' and finished_ts='2024-03-23T16:08:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-20T00:00:00Z", "end_ts": "2024-02-04T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240204_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240204.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240204_20240208.csv"],
                "started_ts": "2024-03-23T15:50:00Z",
                "finished_ts_nullable": "2024-03-23T16:08:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-04..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-20..2024-02-04.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_seattle_20240204_20240208_merge_v1",
            "merged_path=/processed_data/merged_timeseries_seattle_20240204_20240208.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
            "You are assembling a Boston merged artifact for a shorter early‑March window. For city='Boston' with station_id='8443970', use the analysis window "
            "'2024-03-02T00:00:00Z'..'2024-03-05T00:00:00Z' and the water‑level lookback '2024-02-15T00:00:00Z'..'2024-03-02T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_boston_20240302_20240305.csv' under run id 'etl_boston_20240302_20240305_merge_v1' with "
            "started_ts='2024-03-23T17:20:00Z' and finished_ts='2024-03-23T17:36:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_boston_20240302_20240305_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240302.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240302_20240305.csv"],
                "started_ts": "2024-03-23T17:20:00Z",
                "finished_ts_nullable": "2024-03-23T17:36:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-02..2024-03-05.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-02.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_boston_20240302_20240305_merge_v1",
            "merged_path=/processed_data/merged_timeseries_boston_20240302_20240305.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "You need a San Francisco split catalog entry at the tail of the analysis period. For city='San Francisco', set method='time_based' with "
            "split_ts='2024-03-22T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary must be '/data/splits/sf_time_based_split_20240322.json' "
            "with train=134 and test=34. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-22T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                "split_ts": "2024-03-22T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240322.json",
            "train=134", "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "You are assembling a Miami merged artifact aligned to a late‑mid‑month window. For city='Miami' (station_id='8723214'), use the analysis window "
            "'2024-02-12T00:00:00Z'..'2024-02-16T00:00:00Z' with water‑level lookback '2024-02-08T00:00:00Z'..'2024-02-12T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_miami_20240212_20240216.csv' under 'etl_miami_20240212_20240216_merge_v1' with "
            "started_ts='2024-03-23T18:00:00Z' and finished_ts='2024-03-23T18:19:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240212_20240216_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240212.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240212_20240216.csv"],
                "started_ts": "2024-03-23T18:00:00Z",
                "finished_ts_nullable": "2024-03-23T18:19:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-12..2024-02-16.",
                    "Attached observed water levels lookback 2024-02-08..2024-02-12.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240212_20240216_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240212_20240216.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "You want a Seattle split artifact centered near February 7. For city='Seattle', set method='time_based' with split_ts='2024-02-07T12:00:00Z', "
            "row_count=240 and test_fraction=0.2. The split summary must be '/data/splits/seattle_time_based_split_20240207.json' with train=192 and test=48. "
            "Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-07T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240207.json",
                "split_ts": "2024-02-07T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240207.json",
            "train=192", "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "You need a Boston split artifact for the second week of March. For city='Boston', set method='time_based' with split_ts='2024-03-07T10:45:00Z', "
            "row_count=120 and test_fraction=0.2. The split summary must be '/data/splits/boston_time_based_split_20240307.json' with train=96 and test=24. "
            "Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-07T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240307.json",
                "split_ts": "2024-03-07T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240307.json",
            "train=96", "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "You are producing a Miami split‑only artifact for a backtest near February 8. For city='Miami', set method='time_based' with "
            "split_ts='2024-02-08T10:45:00Z', row_count=96 and test_fraction=0.2. The split summary must be '/data/splits/miami_time_based_split_20240208.json' "
            "with train=76 and test=20. Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-08T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240208.json",
                "split_ts": "2024-02-08T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240208.json",
            "train=76", "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "You want a Boston split artifact that locks the early‑March pivot. For city='Boston', set method='time_based' with split_ts='2024-03-05T10:45:00Z', "
            "row_count=120 and test_fraction=0.2. The split summary must be '/data/splits/boston_time_based_split_20240305.json' with train=96 and test=24. "
            "Report the split path and the counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-05T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240305.json",
                "split_ts": "2024-03-05T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240305.json",
            "train=96", "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "You are finalizing a San Francisco v1 training record on the full late‑March week. Train model_name='flood_risk_sf_v1' on "
            "'2024-03-16T00:00:00Z'..'2024-03-22T00:00:00Z' using '/processed_data/merged_timeseries_sf_20240316_20240322.csv' and the split "
            "'/data/splits/sf_time_based_split_20240321.json' (train=134, test=34). Save '/models/flood_risk_sf_v1.pkl' under run_id "
            "'mt_sf_flood_risk_sf_v1_20240316_20240322_v1' with started_ts='2024-03-23T20:10:00Z' and finished_ts='2024-03-23T20:42:00Z', and persist "
            "'/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv'. Report the training run id, model path, and the stored AUC and Accuracy."
        ),
        actions=[
            Action(name="create_etl_run_record", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240316_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240316_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240321.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv"
                ],
                "started_ts": "2024-03-23T20:10:00Z",
                "finished_ts_nullable": "2024-03-23T20:42:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[
            "mt_run_id=mt_sf_flood_risk_sf_v1_20240316_20240322_v1",
            "model_path=/models/flood_risk_sf_v1.pkl",
            "AUC=0.87", "Accuracy=0.82"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "You need an auditable merged dataset for Miami in early February. For city='Miami' with station_id='8723214', use the analysis window "
            "'2024-02-08T00:00:00Z'..'2024-02-12T00:00:00Z' and the water‑level lookback '2024-02-04T00:00:00Z'..'2024-02-08T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_miami_20240208_20240212.csv' under ETL run id 'etl_miami_20240208_20240212_merge_v1' with "
            "started_ts='2024-03-23T20:55:00Z' and finished_ts='2024-03-23T21:14:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "Miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_miami_20240208_20240212_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240208.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240208_20240212.csv"],
                "started_ts": "2024-03-23T20:55:00Z",
                "finished_ts_nullable": "2024-03-23T21:14:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-08..2024-02-12.",
                    "Attached observed water levels lookback 2024-02-04..2024-02-08.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_miami_20240208_20240212_merge_v1",
            "merged_path=/processed_data/merged_timeseries_miami_20240208_20240212.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="You need a deterministic time‑based split for San Francisco to compare against a late‑March backtest. Use city='San Francisco', method='time_based', split_ts='2024-03-18T10:45:00Z'; the processed series has 168 hourly rows and the test fraction comes from '/config/model_config.json' (0.2). Return the canonical split path and the train/test counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-18T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240318.json",
                "split_ts": "2024-03-18T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240318.json",
            "train=134", "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction="You want a reproducible evaluation split for Seattle. Use city='Seattle', method='time_based', split_ts='2024-02-05T12:00:00Z'; the processed series has 240 rows and the test fraction is 0.2 from '/config/model_config.json'. Report the canonical split path and the train/test counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-05T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240205.json",
                "split_ts": "2024-02-05T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240205.json",
            "train=192", "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction="You need a Boston backtest split built from the time axis. Use city='Boston', method='time_based', split_ts='2024-03-03T10:45:00Z'; row_count=120 and test_fraction=0.2 from '/config/model_config.json'. Return the split path and counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json",
                "split_ts": "2024-03-03T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240303.json",
            "train=96", "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction="You need a Miami time‑based split for a 96‑row period used in downstream audits. Use city='Miami', method='time_based', split_ts='2024-02-03T10:45:00Z'; test_fraction=0.2 from '/config/model_config.json'. Report the canonical split path and the counts (train/test).",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-03T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240203.json",
                "split_ts": "2024-02-03T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240203.json",
            "train=76", "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction="You need a late‑window split for San Francisco to align with a regulatory replay. Use method='time_based' with split_ts='2024-03-22T10:45:00Z' on a 168‑row series and a 0.2 test fraction from '/config/model_config.json'. Return the split path and counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-22T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                "split_ts": "2024-03-22T10:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240322.json",
            "train=134", "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction="You need to catalog a Seattle split centered on '2024‑02‑06'. Use method='time_based', split_ts='2024-02-06T12:00:00Z', row_count=240, and 0.2 test fraction from '/config/model_config.json'. Report the split path and counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-06T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240206.json",
                "split_ts": "2024-02-06T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240206.json",
            "train=192", "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction="You want a Boston time‑based split aligned with an early‑March scenario. Use split_ts='2024-03-02T10:00:00Z', row_count=120 and test_fraction 0.2 from '/config/model_config.json'. Return the canonical split path and counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-02T10:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240302.json",
                "split_ts": "2024-03-02T10:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240302.json",
            "train=96", "test=24"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction="You need a Miami split variation centered on '2024‑02‑04'. Use method='time_based' with split_ts='2024-02-04T12:00:00Z' on a 96‑row series and test_fraction=0.2 from '/config/model_config.json'. Provide the split path and counts.",
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-04T12:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240204.json",
                "split_ts": "2024-02-04T12:00:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240204.json",
            "train=76", "test=20"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "You need an ingestion‑only proof for San Francisco covering the mid‑March lead‑in. For city='San Francisco' with station_id='9414290', merge the "
            "analysis window '2024-03-11T00:00:00Z'..'2024-03-15T00:00:00Z' with a water‑level lookback '2024-02-25T00:00:00Z'..'2024-03-11T00:00:00Z'. "
            "Persist '/processed_data/merged_timeseries_sf_20240311_20240315.csv' under run id 'etl_sf_20240311_20240315_merge_v1' with "
            "started_ts='2024-03-23T19:10:00Z' and finished_ts='2024-03-23T19:28:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-25T00:00:00Z", "end_ts": "2024-03-11T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240311_20240315_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240311.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240311_20240315.csv"],
                "started_ts": "2024-03-23T19:10:00Z",
                "finished_ts_nullable": "2024-03-23T19:28:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-11..2024-03-15.",
                    "Attached observed water levels lookback 2024-02-25..2024-03-11.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[
            "mw_run_id=etl_sf_20240311_20240315_merge_v1",
            "merged_path=/processed_data/merged_timeseries_sf_20240311_20240315.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "You are the coastal analyst for Boston (NOAA station 8443970). "
            "Execute the Merge Window Protocol (MWP) for city='Boston' using the analysis window "
            "2024-03-01T00:00:00Z..2024-03-06T00:00:00Z and a water-level lookback from "
            "2024-02-15T00:00:00Z to 2024-03-01T00:00:00Z. After the merge completes, report the stored "
            "AUC and Accuracy for model_name='boston_harbor_model'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="get_weather_forecast", kwargs={
                "city": "Boston",
                "start_ts": "2024-03-01T00:00:00Z",
                "end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="get_tide_predictions", kwargs={
                "station_id": "8443970",
                "start_ts": "2024-03-01T00:00:00Z",
                "end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="get_water_levels", kwargs={
                "station_id": "8443970",
                "start_ts": "2024-02-15T00:00:00Z",
                "end_ts": "2024-03-01T00:00:00Z"
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240301.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": [
                    "/processed_data/merged_timeseries_boston_20240301_20240306.csv"
                ],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                "model_name": "boston_harbor_model"})
        ],
        outputs=[
            "run_id=etl_boston_20240301_20240306_merge_v1",
            "AUC=0.73",
            "Accuracy=0.81"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You maintain Seattle's training data cadence. Execute the Split Protocol (SP) for city='Seattle' "
            "with method='time_based'. Use the test fraction defined in '/config/model_config_v2.json' "
            "(created 2024-03-14T16:45:00Z) and the processed timeseries at "
            "'/data/processed/timeseries_seattle_weather.csv'. Return the split record path and sample counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config_v2.json"
            }),
            Action(name="compute_split_counts", kwargs={
                "row_count": 240,
                "test_fraction": 0.25
            }),
            Action(name="build_split_summary_path", kwargs={
                "city_slug": "seattle",
                "method": "time_based",
                "split_ts": "2024-03-14T16:45:00Z"
            }),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240314.json",
            "train=180",
            "test=60"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "You run Miami's model training and evaluation (MTP) with model_name='flood_risk_miami_v1' over the analysis window "
            "2024-02-01T00:00:00Z..2024-02-05T00:00:00Z. Use the time-based split from 2024-02-02 "
            "at '/data/splits/miami_time_based_split_20240202.json' (train=72, test=24). "
            "After completion, return the run id, the model artifact path, and the stored AUC and Accuracy."
        ),
        actions=[
            Action(name="build_mtp_run_id", kwargs={
                "city_slug": "miami",
                "model_name": "flood_risk_miami_v1",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="build_merged_timeseries_path", kwargs={
                "city_slug": "miami",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="build_metrics_summary_path", kwargs={
                "model_name": "flood_risk_miami_v1",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="get_mtp_timestamps", kwargs={}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "mt_miami_flood_risk_miami_v1_20240201_20240205_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_miami_20240201_20240205.csv",
                    "/processed_data/features.csv",
                    "/data/splits/miami_time_based_split_20240202.json"
                ],
                "output_paths": [
                    "/models/flood_risk_miami_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_miami_v1_20240205.csv"
                ],
                "started_ts": "2024-03-17T09:30:00Z",
                "finished_ts_nullable": "2024-03-17T11:15:00Z",
                "messages": [
                    "Training samples: 72",
                    "Test samples: 24",
                    "Model saved to: /models/flood_risk_miami_v1.pkl"
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                "model_name": "flood_risk_miami_v1"})
        ],
        outputs=[
            "mt_run_id=mt_miami_flood_risk_miami_v1_20240201_20240205_v1",
            "model_path=/models/flood_risk_miami_v1.pkl",
            "AUC=0.73",
            "Accuracy=0.75"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "You’re preparing a time‑based holdout for San Francisco so stakeholders can compare week‑over‑week results. "
            "Honor the test split fraction defined in '/processed_data/model_config.json' and timestamp the split at '2024-03-17T10:45:00Z'. "
            "You need a canonical split summary JSON under /data/splits reflecting the San Francisco processed timeseries row count and only the required fields."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 134,
                   "test_index_count": 34, "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=["train=134", "test=34",
                 "path=/data/splits/sf_time_based_split_20240317.json"]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You are responsible for San Francisco (NOAA station 9414290). "
            "Execute the Merge Window Protocol (MWP) with parameters: "
            "city='San Francisco', station_id='9414290', "
            "analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z, "
            "water-level lookback=2024-02-14T00:00:00Z..2024-03-15T00:00:00Z. "
            "After the MWP completes, report the stored AUC and Accuracy for model_name='flood_risk_sf_v1'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="get_weather_forecast", kwargs={
                   "city": "San Francisco", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_tide_predictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_water_levels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="build_merged_timeseries_path", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240315.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                   "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[
            "auc: 0.87",
            "accuracy: 0.82",
        ]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "You manage dataset splitting for Seattle. Use the Split Protocol (SP) with method='time_based'. "
            "Derive train/test sizes from the processed timeseries at '/data/processed/timeseries_seattle_weather.csv' "
            "and the test fraction defined in '/config/model_config.json'. "
            "Write the split summary for city='Seattle' using split_ts='2024-03-17T10:45:00Z'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 192,
                   "test_index_count": 48, "split_summary_json_path": "/data/splits/seattle_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240317.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "You manage San Francisco's data split. Use the Split Protocol (SP) with method='time_based'. "
            "Take test_fraction and split_ts from '/processed_data/split_summary.json', "
            "and compute train/test counts from '/data/processed/timeseries_sf_weather.csv'. "
            "Persist the split summary for city='San Francisco' with split_ts='2024-03-17T10:45:00Z'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_split_summary_defaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 134,
                   "test_index_count": 34, "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=[
            "train=134",
            "test=34",
            "path=/data/splits/sf_time_based_split_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "You need a reproducible time‑based split for San Francisco that mirrors the published template saved at "
            "'/processed_data/split_summary.json' (created on 2024-03-17T10:45:00Z with a 20% test holdout for the 'high_risk_flag'). "
            "Use the existing processed hourly series for San Francisco to derive train/test counts, persist the canonical split record "
            "for the 2024-03-17T10:45:00Z cutoff, and return the canonical split path together with the two counts."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_split_summary_defaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240317.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You need to register a Seattle‑only time‑based split that matches the regression policy stored at "
            "'/config/regression_config.json' (created on 2024-03-01T09:20:00Z with a 30% test holdout). "
            "Use the existing processed hourly series for Seattle (240 rows) to compute the counts, persist the canonical split "
            "anchored at 2024-03-01T09:20:00Z, and return the canonical split path plus the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/regression_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.3}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-01T09:20:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.3,
                "train_index_count": 168,
                "test_index_count": 72,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240301.json",
                "split_ts": "2024-03-01T09:20:00Z"
            }),
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240301.json",
            "train=168",
            "test=72"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You need a San Francisco time‑based split that follows the method and naming used in the published template "
            "at '/processed_data/split_summary.json' but anchors the cutoff to the model config saved at "
            "'/processed_data/model_config.json' (created on 2024-03-17T10:30:00Z). Use the processed SF series (168 hourly rows), "
            "persist the canonical split at that cutoff, and return the canonical split path with the train/test totals."
        ),
        actions=[
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_split_summary_defaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:30:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:30:00Z"
            }),
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240317.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "You own the data readiness for Seattle. Create a time‑based split summary that downstream training can reuse: "
            "city='Seattle', method='time_based', test_fraction comes from '/config/model_config.json', and the split instant is "
            "2024-02-01T15:25:00Z. The summary must correspond to the processed series for Seattle and be stored under the canonical "
            "city/method/timestamp path so later jobs can reference it deterministically."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="get_model_config_param", kwargs={
                "saved_json_path": "/config/model_config.json"
            }),
            Action(name="compute_split_counts", kwargs={
                "row_count": 240,
                "test_fraction": 0.2
            }),
            Action(name="build_split_summary_path", kwargs={
                "city_slug": "seattle",
                "method": "time_based",
                "split_ts": "2024-02-01T15:25:00Z"
            }),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240201.json",
                "split_ts": "2024-02-01T15:25:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240201.json",
            "train=192",
            "test=48"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You are responsible for the March training cycle in San Francisco. Register a deterministic Model Training & Evaluation "
            "record for model_name='flood_risk_sf_v1' using the merged timeseries window 2024-03-15T00:00:00Z..2024-03-22T00:00:00Z "
            "and the time-based split anchored at 2024-03-17T09:30:00Z. Use the canonical MTP defaults for timestamps and artifacts, "
            "and ensure the run captures exactly the training/test sample counts and the saved model location."
        ),
        actions=[
            Action(name="build_merged_timeseries_path", kwargs={
                "city_slug": "sf",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="build_features_csv_path", kwargs={"city_slug": "sf"}),
            Action(name="build_split_summary_path", kwargs={
                "city_slug": "sf",
                "method": "time_based",
                "split_ts": "2024-03-17T09:30:00Z"
            }),
            Action(name="build_mtp_input_paths", kwargs={
                "merged_timeseries_path": "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                "features_csv_path": "/processed_data/features.csv",
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json"
            }),
            Action(name="build_metrics_summary_path", kwargs={
                "model_name": "flood_risk_sf_v1",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="build_mtp_messages", kwargs={
                "train_samples": 134,
                "test_samples": 34,
                "model_path": "/models/flood_risk_sf_v1.pkl"
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240315_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240317.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv"
                ],
                "started_ts": "2024-03-17T09:30:00Z",
                "finished_ts_nullable": "2024-03-17T11:15:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            })
        ],
        outputs=[
            "run_id=mt_sf_flood_risk_sf_v1_20240315_20240322_v1",
            "model_artifact=/models/flood_risk_sf_v1.pkl",
            "metrics_summary=/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_200",
        instruction=(
            "You oversee San Francisco data readiness. Execute the Split Protocol for city='San Francisco' "
            "with method='time_based', using test_fraction from '/config/model_config.json' and split_ts='2024-03-17T10:45:00Z'. "
            "Your goal is to persist the canonical split summary and make the train/test sample sizes and path clear."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[
            "train=134",
            "test=34",
            "path=/data/splits/sf_time_based_split_20240317.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_201",
        instruction=(
            "You manage the Miami time-based dataset split. For city='Miami', use the Split Protocol with "
            "test_fraction from '/config/model_config_v2.json' and split_ts='2024-02-02T15:45:00Z'. "
            "Ensure the persisted summary reflects the correct counts and canonical path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-02T15:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 72,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240202.json",
                "split_ts": "2024-02-02T15:45:00Z"
            }),
        ],
        outputs=[
            "train=72",
            "test=24",
            "path=/data/splits/miami_time_based_split_20240202.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_202",
        instruction=(
            "You are responsible for the Boston split artifact. Perform a time-based split for city='Boston' "
            "with test_fraction from '/processed_data/boston_model_config.json' and split_ts='2024-03-01T13:18:00Z'. "
            "Persist the split summary and surface the resulting counts and path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[
            "train=90",
            "test=30",
            "path=/data/splits/boston_time_based_split_20240301.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_203",
        instruction=(
            "You handle Seattle’s split governance. For city='Seattle', carry out a time-based split using "
            "test_fraction from '/config/regression_config.json' and split_ts='2024-02-01T15:25:00Z'. "
            "Record the canonical summary and make the counts and path explicit."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/regression_config.json"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.3}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-01T15:25:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.3,
                "train_index_count": 168,
                "test_index_count": 72,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240201.json",
                "split_ts": "2024-02-01T15:25:00Z"
            }),
        ],
        outputs=[
            "train=168",
            "test=72",
            "path=/data/splits/seattle_time_based_split_20240201.json"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_220",
        instruction=(
            "You need a reproducible time-based split for Seattle to lock a March evaluation window. "
            "Use the policy test fraction from '/config/model_config_v2.json' and anchor the split at 2024-03-14T16:45:00Z. "
            "Persist the canonical split record for the Seattle processed series and return the path plus the train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "seattle"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/seattle_time_based_split_20240314.json",
            "train=180",
            "test=60"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_503",
        instruction=(
            "You’re preparing an appendix for early‑February Miami that pairs a frozen split with a metrics export for reporting. "
            "Freeze a time‑based split using the baseline policy at 2024-02-10T11:00:00Z and then register a metrics‑only export for "
            "model_name='flood_risk_miami_v1' for the 2024-02-02 cutoff. Return the split path with train/test totals and the metrics summary path."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Miami"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "miami"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            }),
            Action(name="get_model_info", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="get_model_metrics", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="build_metrics_summary_path", kwargs={
                   "model_name": "flood_risk_miami_v1", "end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "me_miami_flood_risk_miami_v1_20240202_v1",
                "input_paths": [
                    "/models/flood_risk_miami_v1.pkl",
                    "/processed_data/features.csv",
                    "/processed_data/merged_timeseries_miami_20240201_20240202.csv"
                ],
                "output_paths": ["/processed_data/metrics_summary_flood_risk_miami_v1_20240202.csv"],
                "started_ts": "2024-03-18T15:45:00Z",
                "finished_ts_nullable": None,
                "messages": [
                    "AUC: 0.73",
                    "Accuracy: 0.75",
                    "Metrics saved to: /processed_data/metrics_summary_flood_risk_miami_v1_20240202.csv"
                ]
            })
        ],
        outputs=[
            "split_path=/data/splits/miami_time_based_split_20240210.json",
            "train=76",
            "test=20",
            "metrics_summary=/processed_data/metrics_summary_flood_risk_miami_v1_20240202.csv"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_800",
        instruction=(
            "You must capture a deterministic Boston split snapshot that will be referenced in early-March reports. "
            "Use the test fraction from '/processed_data/boston_model_config.json' and anchor the split at 2024-03-01T13:18:00Z. "
            "Provide the canonical split record path together with the train/test sizes."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Boston"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "boston"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[
            "split_path=/data/splits/boston_time_based_split_20240301.json",
            "train=90",
            "test=30"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_902",
        instruction=(
            "You need a San Francisco split snapshot to support a compliance replay. "
            "Use the test fraction from '/processed_data/model_config.json' and anchor the split at 2024-03-17T10:30:00Z. "
            "Persist the canonical split summary for the San Francisco processed series and return the path with train/test totals."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "San Francisco"}),
            Action(name="build_processed_timeseries_path",
                   kwargs={"city_slug": "sf"}),
            Action(name="get_processed_timeseries_metadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_model_config_param", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="compute_split_counts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="build_split_summary_path", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:30:00Z"}),
            Action(name="create_split_summary_record", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:30:00Z"
            })
        ],
        outputs=[
            "split_path=/data/splits/sf_time_based_split_20240317.json",
            "train=134",
            "test=34"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_950",
        instruction=(
            "You oversee a Charleston ingestion focused on a high‑tide window. For city='Charleston' and NOAA station '8665530', "
            "stage the Merge Window Protocol over 2024-01-22T00:00:00Z..2024-01-23T00:00:00Z with a water‑level lookback of "
            "2024-01-22T00:00:00Z..2024-01-22T02:00:00Z. The ETL record must reference the canonical raw inputs "
            "'/data/raw/weather_charleston_20240122.json', '/data/raw/tide_pred_8665530.json', '/data/raw/water_levels_8665530.json' "
            "and the merged output '/processed_data/merged_timeseries_charleston_20240122_20240123.csv', with run_id "
            "'etl_charleston_20240122_20240123_merge_v1'. Finally, report the stored AUC and Accuracy for model_name='simple_model'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Charleston"}),
            Action(name="get_weather_forecast", kwargs={
                "city": "Charleston",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-23T00:00:00Z"
            }),
            Action(name="get_tide_predictions", kwargs={
                "station_id": "8665530",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-23T00:00:00Z"
            }),
            Action(name="get_water_levels", kwargs={
                "station_id": "8665530",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-22T02:00:00Z"
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_charleston_20240122_20240123_merge_v1",
                "input_paths": [
                    "/data/raw/weather_charleston_20240122.json",
                    "/data/raw/tide_pred_8665530.json",
                    "/data/raw/water_levels_8665530.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_charleston_20240122_20240123.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-01-22..2024-01-23.",
                    "Attached observed water levels lookback 2024-01-22..2024-01-22.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                   "model_name": "simple_model"})
        ],
        outputs=[
            "run_id=etl_charleston_20240122_20240123_merge_v1",
            "AUC=0.79",
            "Accuracy=0.76"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_953",
        instruction=(
            "You need a Seattle ingestion snapshot centered on spring tides. For city='Seattle' and NOAA station '9447130', "
            "run the Merge Window Protocol over 2024-02-01T00:00:00Z..2024-02-08T00:00:00Z with a water-level lookback of "
            "2024-01-15T00:00:00Z..2024-02-01T00:00:00Z. The ETL record must reference the canonical raw inputs "
            "'/data/raw/weather_seattle_20240201.json', '/data/raw/tide_pred_9447130.json', '/data/raw/water_levels_9447130.json' "
            "and the merged output '/processed_data/merged_timeseries_seattle_20240201_20240208.csv', with run_id "
            "'etl_seattle_20240201_20240208_merge_v1'. Finally, report the stored AUC and Accuracy for model_name='simple_model'."
        ),
        actions=[
            Action(name="resolve_city_slug", kwargs={"city": "Seattle"}),
            Action(name="get_weather_forecast", kwargs={
                "city": "Seattle",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_tide_predictions", kwargs={
                "station_id": "9447130",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_water_levels", kwargs={
                "station_id": "9447130",
                "start_ts": "2024-01-15T00:00:00Z",
                "end_ts": "2024-02-01T00:00:00Z"
            }),
            Action(name="create_etl_run_record", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240201.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="get_model_metrics", kwargs={
                   "model_name": "simple_model"})
        ],
        outputs=[
            "run_id=etl_seattle_20240201_20240208_merge_v1",
            "AUC=0.79",
            "Accuracy=0.76"
        ]
    )
]
