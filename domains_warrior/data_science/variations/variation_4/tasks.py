from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="gokulsaireddy",
        user_id="task_001",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Seattle (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's tide predictions and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Seattle",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 47.6062, "longitude": -122.3321},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Seattle"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_002",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for New York City (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "New York",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New York"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 40.7128, "longitude": -74.006},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "New York"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_003",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of New Orleans.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New Orleans"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_004",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate MIAMI_V1, a flood-risk analysis model for the city of Miami, using existing predictions (no retraining), compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and create notion page and draft a email to stakeholders@city.gov later.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(name="GetModel", kwargs={"model_name": "MIAMI_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_MIAMI_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_MIAMI_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "MIAMI_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_005",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Charleston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Charleston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_006",
        instruction="You are a Data Science automation agent. Your primary objective is to develop BOSTON_V1, a flood-risk analysis model for the city of Boston. This model should be trained using the processed data found in /data/processed/timeseries_boston_weather.csv. The final model must be configured with a classification threshold of 1.8 meters and be validated using a 30% / 0.3 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 1.8, "test_split_fraction": 0.3},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.3},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib",
                        "/metrics/MODEL_BOSTON_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_BOSTON_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_007",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for BLR_V1, a flood-risk analysis model for the city of BLR. Using existing predictions and metrics (PRED_002, METRICS_002), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "BLR"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_002", "metrics_id": "METRICS_002"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "BLR_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "BLR_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_008",
        instruction="You are a Data Science automation agent. Your primary objective is to develop HOUSTON_V1, a flood-risk analysis logistic_regression model for the city of Houston. This model should be trained using the processed data found in /data/processed/timeseries_houston_weather.csv. The final model must be configured with a classification threshold of 2.7 meters and be validated using a 10% / 0.1 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Houston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Houston"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_houston_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.7, "test_split_fraction": 0.1},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.1},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "HOUSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_HOUSTON_V1.joblib",
                        "/metrics/MODEL_HOUSTON_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_HOUSTON_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_009",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of San Francisco (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "San Francisco",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 37.7749, "longitude": -122.4194},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "San Francisco"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_010",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of New Orleans by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New Orleans"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New Orleans"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "New Orleans"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "New Orleans",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_new_orleans.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_011",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Miami (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Miami",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 25.7617, "longitude": -80.1918},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Miami"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_012",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Jacksonville by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Jacksonville"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Jacksonville"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Jacksonville"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Jacksonville",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_jacksonville.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_013",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Savannah by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include both an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Savannah"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Savannah"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Savannah"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Savannah",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_savannah.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_014",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Portland by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an anomalies plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Portland"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Portland"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Portland"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "anomalies",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_portland.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_anomalies.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_015",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Los Angeles by running an ETL over newly acquired raw weather, tides data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Los Angeles"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Los Angeles"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 34.0522, "longitude": -118.2437},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Los Angeles"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Los Angeles",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_016",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Miami by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 25.7617, "longitude": -80.1918},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Miami"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Miami",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_017",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate BOSTON_V1, a flood-risk analysis model for the city of Boston, using existing predictions (no retraining), compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and create notion page and draft a email to stakeholders@city.gov later.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(name="GetModel", kwargs={"model_name": "BOSTON_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_BOSTON_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_BOSTON_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "BOSTON_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_018",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate SF_V1, a flood-risk analysis model for the city of San Francisco, using existing predictions (no retraining), geocoding context. Evaluation metrics and stakeholder-ready outputs should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and draft a email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(name="GetModel", kwargs={"model_name": "SF_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_SF_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_SF_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "SF_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_sf.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_019",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Jacksonville by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Jacksonville"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Jacksonville"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Jacksonville"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Jacksonville",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_jacksonville.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_020",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of San Diego.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Diego"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_021",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion report for the city of Boston.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_022",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of New York.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New York"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_023",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of San Diego by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Diego"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Diego"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "San Diego"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "San Diego",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_san_diego.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_024",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate SEATTLE_V1, a flood-risk analysis model for the city of Seattle, using existing predictions (no retraining), make geocoding context in the project record. The workflow must compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and draft a email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(name="GetModel", kwargs={"model_name": "SEATTLE_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_SEATTLE_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_SEATTLE_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "SEATTLE_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_seattle.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_025",
        instruction="You are a Data Science automation agent. Your primary objective is to develop SEATTLE_V1, a flood-risk random_forest analysis model for the city of Seattle.This model should be trained using the processed data found in /data/processed/timeseries_seattle_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 40% / 0.4 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.4},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.4},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib",
                        "/metrics/MODEL_SEATTLE_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SEATTLE_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_026",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Norfolk by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Norfolk"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Norfolk"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Norfolk"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Norfolk",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_norfolk.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_027",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Miami (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Miami",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 25.7617, "longitude": -80.1918},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Miami"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_028",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Norfolk.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Norfolk"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_029",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Boston by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 42.3601, "longitude": -71.0589},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Boston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Boston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_030",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Boston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's tide predictions. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Boston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 42.3601, "longitude": -71.0589},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Boston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_031",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Houston.Using existing prediction and metrics (PRED_001, METRICS_001) and summary plot for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Houston"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_032",
        instruction="You are a Data Science automation agent. Your primary objective is to train C2_V1, a flood-risk analysis model for the city of C2. This model should be trained using the processed data found in /data/processed/timeseries_C2_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 40% / 0.4 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "C2"}),
            Action(
                name="CreateFeatures",
                kwargs={"input_csv_path": "/data/processed/timeseries_C2_weather.csv"},
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.4},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.4},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "C2_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_C2_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_C2_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_033",
        instruction="You are a Data Science automation agent. Your primary objective is to develop CHICAGO_V1, a flood-risk analysis model for the city of Chicago. This model should be trained using the processed data found in /data/processed/timeseries_chicago_weather.csv. The final model must be configured with a classification threshold of 3.5 meters and be validated using a 35% / 0.35 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Chicago"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Chicago"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_chicago_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 3.5, "test_split_fraction": 0.35},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.35},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "CHICAGO_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_chicago.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_CHICAGO_V1.joblib",
                        "/metrics/MODEL_CHICAGO_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_CHICAGO_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_034",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Savannah by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Savannah"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Savannah"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Savannah"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Savannah",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_savannah.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_035",
        instruction="You are a Data Science automation agent. Your primary objective is to develop MIAMI_V1, a flood-risk analysis model for the city of Miami. This model should be trained using the processed data found in /data/processed/timeseries_miami_weather.csv. The final model must be configured with a classification threshold of 3.0 meters and be validated using a 25% / 0.25 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 3.0, "test_split_fraction": 0.25},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.25},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib",
                        "/metrics/MODEL_MIAMI_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_MIAMI_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_036",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of Boston. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_BOSTON_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_BOSTON_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_BOSTON_V1 - Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_BOSTON_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_037",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Seattle.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_038",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of Houston. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_HOUSTON_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Houston"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_HOUSTON_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_HOUSTON_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_HOUSTON_V1.png",
                        "/figures/summary_MODEL_HOUSTON_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_039",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for Chennai_V1, a flood-risk analysis model for the city of Chennai. Using existing predictions and metrics (PRED_003, METRICS_003), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Chennai"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_003", "metrics_id": "METRICS_003"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "Chennai_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "Chennai_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_040",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of New Orleans by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New Orleans"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New Orleans"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "New Orleans"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "New Orleans",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_new_orleans.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_041",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Houston by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Houston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Houston"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Houston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Houston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_042",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Charleston by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and registered in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Charleston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Charleston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_043",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Seattle (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Seattle",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 47.6062, "longitude": -122.3321},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Seattle"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_044",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Boston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Boston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 42.3601, "longitude": -71.0589},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Boston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_045",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of San Francisco.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_046",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for HYD_V1, a flood-risk analysis model for the city of HYD. Using existing predictions and metrics (PRED_002, METRICS_002), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "HYD"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_002", "metrics_id": "METRICS_002"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "HYD_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "HYD_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_047",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for New York City (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "New York",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New York"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 40.7128, "longitude": -74.006},
            ),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_048",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Tampa by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Tampa"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Tampa"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Tampa"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_tampa.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_049",
        instruction="You are a Data Science automation agent. Your primary objective is to train C1_V1, a flood-risk analysis model for the city of C1. This model should be trained using the processed data found in /data/processed/timeseries_C1_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "C1"}),
            Action(
                name="CreateFeatures",
                kwargs={"input_csv_path": "/data/processed/timeseries_C1_weather.csv"},
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "C1_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_C1_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_C1_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_050",
        instruction="You are a Data Science automation agent. Your primary objective is to develop BOSTON_V1, a flood-risk logistic_regression analysis model for the city of Boston.This model should be trained using the processed data found in /data/processed/timeseries_boston_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_BOSTON_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_051",
        instruction="You are a Data Science automation agent. Your primary objective is to develop SEATTLE_V1, a flood-risk logistic_regression analysis model for the city of Seattle.This model should be trained using the processed data found in /data/processed/timeseries_seattle_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SEATTLE_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_052",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Charleston.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Charleston"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_053",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Boston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels and tide predictions. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Boston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 42.3601, "longitude": -71.0589},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Boston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_054",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for SF_V1, a flood-risk analysis model for the city of San Francisco. Using existing predictions and metrics (PRED_002, METRICS_002), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_002", "metrics_id": "METRICS_002"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "SF_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "SF_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_055",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Boston by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 42.3601, "longitude": -71.0589},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Boston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Boston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_056",
        instruction="You are a Data Science automation agent. Your primary objective is to train MIAMI_V1, a flood-risk analysis model for the city of Miami. This model should be trained using the processed data found in /data/processed/timeseries_miami_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_MIAMI_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_MIAMI_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_057",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Los Angeles (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Los Angeles",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Los Angeles"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 34.0522, "longitude": -118.2437},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Los Angeles"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_058",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Los Angeles (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels and tide predictions. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Los Angeles",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Los Angeles"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 34.0522, "longitude": -118.2437},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Los Angeles"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_059",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for Delhi_V1, a flood-risk analysis model for the city of Delhi. Using existing predictions and metrics (PRED_001, METRICS_001), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Delhi"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "Delhi_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "Delhi_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_060",
        instruction="You are a Data Science automation agent. Your primary objective is to develop SEATTLE_V1, a flood-risk analysis model for the city of Seattle. This model should be trained using the processed data found in /data/processed/timeseries_seattle_weather.csv. The final model must be configured with a classification threshold of 2.2 meters and be validated using a 15% / 0.15 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.2, "test_split_fraction": 0.15},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.15},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib",
                        "/metrics/MODEL_SEATTLE_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SEATTLE_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_061",
        instruction="You are a Data Science automation agent. Your primary objective is to develop NEW_YORK_V1, a flood-risk analysis model for the city of New York. This model should be trained using the processed data found in /data/processed/timeseries_new_york_weather.csv. The final model must be configured with a classification threshold of 2.5 meters and be validated using a 20% / 0.2 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New York"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New York"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_new_york_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.5, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "NEW_YORK_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_NEW_YORK_V1.joblib",
                        "/metrics/MODEL_NEW_YORK_V1_train_metrics.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_NEW_YORK_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_062",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Galveston by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Galveston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Galveston"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Galveston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Galveston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_galveston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_063",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Charleston by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Charleston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Charleston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_064",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for SEATTLE_V1, a flood-risk analysis model for the city of Seattle. Using existing predictions and metrics (PRED_001, METRICS_001), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "SEATTLE_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "SEATTLE_V1 Flood-Risk Results",
                    "body_text": "Stakeholder summary for SEATTLE_V1 is available. Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_065",
        instruction="You are a Data Science automation agent. Your primary objective is to develop MIAMI_V1, a flood-risk logistic_regression analysis model for the city of Miami.This model should be trained using the processed data found in /data/processed/timeseries_miami_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_MIAMI_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_066",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of San Diego. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SAN_DIEGO_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Diego"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SAN_DIEGO_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SAN_DIEGO_V1 - Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_SAN_DIEGO_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SAN_DIEGO_V1.png",
                        "/figures/summary_MODEL_SAN_DIEGO_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_067",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for Miami_V1, a flood-risk analysis model for the city of Miami. Using existing predictions and metrics (PRED_002, METRICS_002), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_002", "metrics_id": "METRICS_002"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "Miami_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "Miami_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_068",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Seattle by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 47.6062, "longitude": -122.3321},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Seattle"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Seattle",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_069",
        instruction="You are a Data Science automation agent. Your primary objective is to develop MIAMI_V1, a flood-risk random_forest analysis model for the city of Miami.This model should be trained using the processed data found in /data/processed/timeseries_miami_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 40% / 0.4 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.4},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.4},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_MIAMI_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_070",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate BOSTON_V1, a flood-risk analysis model for the city of Boston, using existing predictions (no retraining), make geocoding context in the project record. The workflow must compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and draft a email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Boston"}),
            Action(name="GetModel", kwargs={"model_name": "BOSTON_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_BOSTON_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_BOSTON_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "BOSTON_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_071",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Norfolk by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include a overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Norfolk"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Norfolk"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Norfolk"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Norfolk",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_norfolk.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_gaps.png",
                        "/figures/qc_overview.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_072",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of San Francisco (28-day forecast horizon, a 100.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "San Francisco",
                    "forecast_horizon_days": 28,
                    "max_station_distance_km_nullable": 100.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 37.7749, "longitude": -122.4194},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "San Francisco"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_073",
        instruction="You are a Data Science automation agent. Your primary objective is to communicate the most recent evaluation results for LA_V1, a flood-risk analysis model for the city of LA. Using existing predictions and metrics (PRED_002, METRICS_002), package them into a Notion summary report and draft an email to stakeholders@city.gov. Finally, ensure that all report artifacts and communication drafts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "LA"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_002", "metrics_id": "METRICS_002"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "LA_V1 - Stakeholder Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "subject": "LA_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_074",
        instruction="You are a Data Science automation agent. Your primary objective is to develop SF_V1, a flood-risk random_forest analysis model for the city of San Francisco.This model should be trained using the processed data found in /data/processed/timeseries_sf_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 40% / 0.4 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(
                name="CreateFeatures",
                kwargs={"input_csv_path": "/data/processed/timeseries_sf_weather.csv"},
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.4},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.4},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SF_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SF_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_075",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate SEATTLE_V1, a flood-risk analysis model for the city of Seattle, using existing predictions (no retraining), compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and create notion page and draft a email to stakeholders@city.gov later.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="GetModel", kwargs={"model_name": "SEATTLE_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_SEATTLE_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_SEATTLE_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={"title": "SEATTLE_V1 Model Evaluation Results"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_076",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Miami.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_077",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Seattle by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Seattle"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 47.6062, "longitude": -122.3321},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Seattle"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Seattle",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_078",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Houston by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Houston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Houston"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Houston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Houston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_079",
        instruction="You are a Data Science automation agent. Your primary objective is to develop SF_V1, a flood-risk analysis model for the city of San Francisco.This model should be trained using the processed data found in /data/processed/timeseries_sf_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(
                name="CreateFeatures",
                kwargs={"input_csv_path": "/data/processed/timeseries_sf_weather.csv"},
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SF_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SF_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_080",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of New York (14-day forecast horizon, a 75.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "New York",
                    "forecast_horizon_days": 14,
                    "max_station_distance_km_nullable": 75.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "New York"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 40.7128, "longitude": -74.006},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "New York"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_081",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Portland by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Portland"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Portland"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Portland"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_portland.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_082",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of Miami. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_MIAMI_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_MIAMI_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_MIAMI_V1 - Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_MIAMI_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_083",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of New York. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_NEW_YORK_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "New York"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_NEW_YORK_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_NEW_YORK_V1 - Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_NEW_YORK_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_NEW_YORK_V1.png",
                        "/figures/summary_MODEL_NEW_YORK_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_084",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Annapolis by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Annapolis"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Annapolis"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Annapolis"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Annapolis",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_annapolis.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_085",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of San Francisco by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 37.7749, "longitude": -122.4194},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "San Francisco"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "San Francisco",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_086",
        instruction="You are a Data Science automation agent. Your primary objective is to create a Notion page report for the city of Tampa.Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1 . Makesure to include Executive Summary, Data & Methods in the report. and enrich References section sourced from Zotero metadata. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Tampa"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SF_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png",
                    },
                    "tags": ["Executive Summary", "Data & Methods"],
                },
            ),
            Action(
                name="EnrichNotion",
                kwargs={"model_id": "MODEL_SF_V1", "page_id": "NOTION_PAGE_001"},
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_087",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate SF_V1, a flood-risk analysis model for the city of San Francisco, using existing predictions (no retraining), compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and create notion page and draft a email to stakeholders@city.gov later.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(name="GetModel", kwargs={"model_name": "SF_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_SF_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_SF_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(name="CreateNotionPageJson", kwargs={"title": "SF_V1 Results"}),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion- /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_088",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of San Francisco by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include both a gaps plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "San Francisco"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 37.7749, "longitude": -122.4194},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "San Francisco"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "San Francisco",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "gaps",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_089",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Charleston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's tide predictions. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Charleston"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_090",
        instruction="You are a Data Science automation agent. Your objective is to create and set up a new flood-risk analysis project for the city of Charleston (7-day forecast horizon, a 50.0 km maximum station search radius). The final acquired dataset must include the city's geocoding, a complete weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the file paths for all newly acquired raw data are properly registered in the project's central file directory.",
        actions=[
            Action(
                name="SetProjectConfig",
                kwargs={
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0,
                },
            ),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city_name": "Charleston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetCoastalMeteorology", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_091",
        instruction="You are a Data Science automation agent. Your primary objective is to evaluate MIAMI_V1, a flood-risk analysis model for the city of Miami, using existing predictions (no retraining), make geocoding context in the project record. The workflow must compute evaluation metrics and prepare stakeholder-ready outputs, and it should produce the visualization artifact summarizing performance. Finally, ensure that the file paths for all newly created assets are registered in the project's central file directory and draft a email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(name="GetModel", kwargs={"model_name": "MIAMI_V1"}),
            Action(name="EvaluateModel", kwargs={"model_id": "MODEL_MIAMI_V1"}),
            Action(name="CreateSummaryPlots", kwargs={"model_id": "MODEL_MIAMI_V1"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(name="CreateNotionPageJson", kwargs={"title": "MIAMI_V1 Results"}),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_miami.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_092",
        instruction="You are a Data Science automation agent. Your primary objective is to create a concise Executive Summary report in Notion for the city of Seattle. Using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SEATTLE_V1. Make sure to include only an Executive Summary section. Finally, register the file paths for all resulting assets in the project’s central file directory and draft an email to stakeholders@city.gov.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="CreateSummaryPlots",
                kwargs={"model_id": "MODEL_SEATTLE_V1", "predictions_id": "PRED_001"},
            ),
            Action(
                name="CreateNotionPageJson",
                kwargs={
                    "title": "MODEL_SEATTLE_V1 - Executive Summary",
                    "tags": ["Executive Summary"],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_SEATTLE_V1.png"
                    },
                },
            ),
            Action(
                name="CreateGmailJson",
                kwargs={
                    "to": ["stakeholders@city.gov"],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": ["/notion/pages/NOTION_PAGE_001.json"],
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "PROJ_DIR_001",
            "STAKEHOLDER_OUTPUT_001",
            "NOTION_PAGE_001",
            "GMAIL_MSG_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_093",
        instruction="You are a Data Science automation agent. Your primary objective is to train BOSTON_V1, a flood-risk analysis model for the city of Boston. This model should be trained using the processed data found in /data/processed/timeseries_boston_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_BOSTON_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_BOSTON_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_094",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Tampa by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Tampa"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Tampa"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Tampa"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_tampa.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_095",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Baltimore by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include a overview plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Baltimore"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Baltimore"}),
            Action(name="FindNoaaStation", kwargs={"latitude": 55, "longitude": 55}),
            Action(name="SetWeatherForecast", kwargs={"city": "Baltimore"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Baltimore",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_baltimore.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_096",
        instruction="You are a Data Science automation agent. Your primary objective is to train SF_V1, a flood-risk analysis model for the city of San Francisco. This model should be trained using the processed data found in /data/processed/timeseries_sf_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "San Francisco"}),
            Action(
                name="CreateFeatures",
                kwargs={"input_csv_path": "/data/processed/timeseries_sf_weather.csv"},
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_SF_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SF_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_097",
        instruction="You are a Data Science automation agent. Your primary objective is to develop BOSTON_V1, a flood-risk random_forest analysis model for the city of Boston.This model should be trained using the processed data found in /data/processed/timeseries_boston_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 40% / 0.4 test split. Ensure that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Boston"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.4},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.4},
            ),
            Action(
                name="CreateModel",
                kwargs={
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest",
                },
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_BOSTON_V1",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_098",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Miami by running an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered, and quality-control figures produced for review. Finally, log the completion to the terminal and register everything in the central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Miami"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Miami"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 25.7617, "longitude": -80.1918},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Miami"}),
            Action(
                name="SetTidePredictions", kwargs={"station_id": "NOAA_STATION_001"}
            ),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Miami",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL run complete"}),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_099",
        instruction="You are a Data Science automation agent. Your primary objective is to train SEATTLE_V1, a flood-risk analysis model for the city of Seattle. This model should be trained using the processed data found in /data/processed/timeseries_seattle_weather.csv. The final model must be configured with a classification threshold of 2.0 meters and be validated using a 20% / 0.2 test split. The workflow must include model training, prediction generation, and evaluation metrics. Finally, ensure stakeholder-ready outputs are prepared and that the file paths for all newly created assets are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Seattle"}),
            Action(
                name="CreateFeatures",
                kwargs={
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            ),
            Action(
                name="SetModelConfig",
                kwargs={"classification_threshold_m": 2.0, "test_split_fraction": 0.2},
            ),
            Action(
                name="CreateDatasetSplit",
                kwargs={"features_id": "FEATURES_001", "test_fraction": 0.2},
            ),
            Action(
                name="TrainModel",
                kwargs={
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001",
                },
            ),
            Action(name="EvaluateModel", kwargs={"predictions_id": "PRED_001"}),
            Action(
                name="PrepareStakeholderOutputs",
                kwargs={"predictions_id": "PRED_001", "metrics_id": "METRICS_001"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_SEATTLE_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                    ]
                },
            ),
        ],
        outputs=[
            "CONFIG_001",
            "PROJ_DIR_001",
            "FEATURES_001",
            "MODEL_CONFIG_001",
            "SPLIT_001",
            "MODEL_SEATTLE_V1",
            "PRED_001",
            "METRICS_001",
            "STAKEHOLDER_OUTPUT_001",
        ],
    ),
    Task(
        annotator="gokulsaireddy",
        user_id="task_100",
        instruction="You are a Data Science automation agent. Your primary objective is to build a processed timeseries dataset for the city of Charleston by running an ETL over newly acquired raw weather and water-level data. The resulting dataset must be registered, with quality-control figures that include an anomalies plot. The workflow must also log the ETL start and completion messages in the terminal. Finally, ensure all artifacts are registered in the project’s central file directory.",
        actions=[
            Action(name="SetProjectConfig", kwargs={"target_city": "Charleston"}),
            Action(name="SetGeocodeCity", kwargs={"city_name": "Charleston"}),
            Action(
                name="FindNoaaStation",
                kwargs={"latitude": 32.7765, "longitude": -79.9311},
            ),
            Action(name="SetWeatherForecast", kwargs={"city": "Charleston"}),
            Action(name="SetWaterLevels", kwargs={"station_id": "NOAA_STATION_001"}),
            Action(name="AppendTerminalLog", kwargs={"message": "ETL started"}),
            Action(
                name="StartEtlRun",
                kwargs={
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json",
                },
            ),
            Action(
                name="RegisterProcessedTimeseries",
                kwargs={"processed_csv_path": "/data/processed/timeseries_ETL_001.csv"},
            ),
            Action(
                name="CreateQCFigures",
                kwargs={
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "anomalies",
                },
            ),
            Action(
                name="AppendTerminalLog",
                kwargs={"message": "ETL run complete", "type": "completed"},
            ),
            Action(
                name="SetProjectDirectories",
                kwargs={
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_anomalies.png",
                        "/figures/qc_gaps.png",
                    ]
                },
            ),
        ],
        outputs=["CONFIG_001", "ETL_001", "QC_FIG_001", "PROJ_DIR_001"],
    ),
]
