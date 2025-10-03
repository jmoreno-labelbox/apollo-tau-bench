# Copyright Sierra

tasks = [
    {
        "annotator": gokulsaireddy,
        "user_id": "task_001",
        "instruction": "As a Data Science automation agent, your task is to establish and configure a fresh flood-risk analysis project for the city of Portland (7-day forecast horizon, 50.0 km maximum station search radius). Make sure that the final dataset gathered encompasses the city's geocoding, a complete weather forecast, and includes tide predictions and coastal meteorology records from the primary NOAA station. Confirm that all file paths for the newly acquired raw data are accurately recorded in the project's main file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 47.6062,
                    "longitude": -122.3321
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_002",
        "instruction": "Being a Data Science automation agent, your role involves setting up and initiating a new flood-risk analysis project for Providence City (7-day forecast horizon, 50.0 km maximum station search radius). Ensure the comprehensive dataset obtained integrates the city's geocoding, a full weather forecast, and encloses the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Verify that all file paths for the newly acquired raw data are correctly documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 40.7128,
                    "longitude": -74.006
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_003",
        "instruction": "As a Data Science automation agent, your main task is to construct a Notion page report for New Orleans, utilizing existing predictions and metrics (PRED_001, METRICS_001) associated with the model MODEL_SF_V1. Ensure inclusion of an Executive Summary, Data & Methods in the report, and expand the References section using Zotero metadata. Finally, make sure to register the file paths for all resulting assets within the central file directory of the project and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "New Orleans"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_004",
        "instruction": "Serving as a Data Science automation agent, your principal goal is to assess MIAMI_V1, a flood-risk analysis model for Orlando, using existing predictions (no retraining), calculating evaluation metrics and preparing outputs suitable for stakeholders, while generating the visualization artifact that summarizes performance. Finally, ensure you register the file paths for all newly created assets in the project's central file directory, create a Notion page, and draft an email to stakeholders@city.gov afterwards.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "MIAMI_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_MIAMI_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_MIAMI_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MIAMI_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_005",
        "instruction": "As a Data Science automation agent, your task is to initiate and configure a new project on flood-risk analysis for the city of Charleston (7-day forecast horizon, a 50.0 km maximum station search radius). The dataset you gather should include the city's geocoding, a comprehensive weather forecast, and key data from the NOAA station, such as observed water levels, tide predictions, and coastal meteorological information. Ensure that all file paths for the newly acquired raw data are accurately registered in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_006",
        "instruction": "Being a Data Science automation agent, your main task is to construct BOSTON_V1, a flood-risk analysis model tailored for Providence. Utilize the processed data available at /data/processed/timeseries_boston_weather.csv for training. The model should be fine-tuned with a classification threshold of 1.8 meters and validated through a 30% / 0.3 test split. Confirm that the file paths for all newly developed assets are recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 1.8,
                    "test_split_fraction": 0.3
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.3
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib",
                        "/metrics/MODEL_BOSTON_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_BOSTON_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_007",
        "instruction": "You are a Data Science automation agent. Your chief task is to convey the latest evaluation results of BLR_V1, a flood-risk analysis model for the city of BLR. Utilizing existing predictions and metrics (PRED_002, METRICS_002), compile them into a Notion summary report and compose an email to stakeholders@city.gov. Lastly, confirm that all report artifacts and communication drafts are logged in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "BLR"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_002",
                    "metrics_id": "METRICS_002"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "BLR_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "BLR_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_008",
        "instruction": "You are a Data Science automation agent. Your main task is to create HOUSTON_V1, a flood-risk analysis logistic_regression model for the city of Austin. This model must be trained using the processed data located in /data/processed/timeseries_houston_weather.csv. The final model should be configured with a classification threshold of 2.7 meters and validated using a 10% / 0.1 test split. Ensure that the file paths for all newly created assets are logged in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Austin"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Austin"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_houston_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.7,
                    "test_split_fraction": 0.1
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.1
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "HOUSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_HOUSTON_V1.joblib",
                        "/metrics/MODEL_HOUSTON_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_HOUSTON_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_009",
        "instruction": "As a Data Science automation agent, your task is to initiate and configure a new flood-risk analysis project for the city of Oakland (7-day forecast horizon, a 50.0 km maximum station search radius). The ultimate dataset obtained should encompass the city's geocoding, a comprehensive weather forecast, and the main NOAA station's observed water levels, tide predictions, and coastal meteorology records. Verify that the file paths for all newly gathered raw data are accurately registered in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_010",
        "instruction": "As a Data Science automation agent, your main task is to establish a processed timeseries dataset for the city of New Orleans by executing an ETL on newly acquired raw weather and water-level data. The resulting dataset should be recorded, inclusive of quality-control figures that feature an overview plot. Additionally, the workflow must log start and completion messages of the ETL process in the terminal. Ensure that all artifacts are cataloged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "New Orleans"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "New Orleans"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "New Orleans"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "New Orleans",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_new_orleans.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_011",
        "instruction": "As a Data Science automation agent, your task is to initiate and configure a new flood-risk analysis project for the city of Orlando (with a 7-day forecast horizon and a 50.0 km maximum station search radius). The final dataset acquired should contain the city's geocoding, a comprehensive weather forecast, and the observed water levels and coastal meteorology records from the primary NOAA station. Verify that the file paths for all the newly obtained raw data are accurately recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 25.7617,
                    "longitude": -80.1918
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_012",
        "instruction": "Being a Data Science automation agent, your main goal is to create a processed timeseries dataset for the city of Tampa by executing an ETL over the newly obtained raw weather and water-level data. The resulting dataset should be logged, along with quality-control figures that include an overview plot. The workflow must also include logging messages for the ETL start and completion in the terminal. Ensure that all artifacts are archived in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Tampa"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Tampa"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Tampa"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_jacksonville.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_013",
        "instruction": "As a Data Science automation agent, your main goal is to create a processed timeseries dataset for the city of Savannah by executing an ETL on newly sourced raw weather and water-level data. The final dataset must be recorded, accompanied by quality-control figures that feature both an overview plot. Ensure that the workflow logs both ETL start and completion messages in the terminal. Ultimately, confirm that all artifacts are stored in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Savannah"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Savannah"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Savannah"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Savannah",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_savannah.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_014",
        "instruction": "As a Data Science automation agent, your primary task is to construct a processed timeseries dataset for the city of Portland by carrying out an ETL on newly acquired raw weather and water-level data. Record the resulting dataset, including quality-control figures with an anomalies plot. Make sure that the workflow logs ETL start and completion messages in the terminal. In the end, verify that all artifacts are stored in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Portland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "anomalies"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_portland.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_anomalies.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_015",
        "instruction": "Act as a Data Science automation agent. Your main task is to create a processed timeseries dataset for the city of Sacramento by executing an ETL on newly acquired raw weather, tides data. Ensure the resulting dataset is registered, and generate quality-control figures for review. Conclude by logging completion to the terminal and registering all materials in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 34.0522,
                    "longitude": -118.2437
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Sacramento"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Sacramento",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_016",
        "instruction": "Function as a Data Science automation agent. Your main goal is to construct a processed timeseries dataset for the city of Orlando by performing an ETL on newly acquired raw weather and water-level data. Make sure the resulting dataset is registered, along with quality-control figures that feature an overview plot. Additionally, the workflow should log ETL start and completion messages in the terminal. Lastly, confirm all artifacts are registered in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 25.7617,
                    "longitude": -80.1918
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Orlando"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Orlando",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_017",
        "instruction": "Handle the evaluation of BOSTON_V1, a flood-risk model for Providence, by using the current predictions (without retraining), compute evaluation metrics, and generate outputs suitable for stakeholders. Ensure it generates the visualization artifact summarizing its performance. Lastly, make sure to register all new asset file paths in the project's central directory, set up a notion page, and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "BOSTON_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_BOSTON_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_BOSTON_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "BOSTON_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_018",
        "instruction": "Coordinate the evaluation of SF_V1, a flood-risk model for Oakland, utilizing the current predictions (and not retraining) and geocoding context. Generate metrics and stakeholder-ready outputs, creating a visualization artifact that encapsulates its performance. Ensure all new asset file paths are logged in the project's central directory, and construct an email draft to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "SF_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_SF_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SF_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_sf.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_019",
        "instruction": "You are a Data Science automation agent. Your main task is to construct a processed timeseries dataset for the city of Tampa by executing an ETL process on the newly acquired raw weather and tide data. Ensure the resulting dataset is registered and that quality-control figures are generated for evaluation. Lastly, log the completion to the terminal and register all items in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Tampa"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Tampa"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Tampa"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_jacksonville.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_020",
        "instruction": "You are a Data Science automation agent. Your main task is to develop a Notion page report for the city of Sacramento using the existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1. Ensure that the report includes an Executive Summary, Data & Methods, and enhance the References section with sources from Zotero metadata. Finally, register the file paths for all resulting assets in the project\u2019s central file directory and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_021",
        "instruction": "As a Data Science automation agent, your main task is to generate a Notion report for the city of Providence. Utilize the existing prediction and metrics (PRED_001, METRICS_001) from the model MODEL_SF_V1. Ensure the report incorporates an Executive Summary, Data & Methods, and enhance the References section using Zotero metadata. Lastly, log the file paths for all derived assets in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_022",
        "instruction": "As a Data Science automation agent, your main task is to generate a Notion page report for the city of Providence. Utilize the existing prediction and metrics (PRED_001, METRICS_001) from the model MODEL_SF_V1. Ensure the report incorporates an Executive Summary, Data & Methods, and enhance the References section using Zotero metadata. Lastly, log the file paths for all derived assets in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_023",
        "instruction": "Act as a Data Science automation agent. Your main task is to construct a processed timeseries dataset for the city of Sacramento by executing an ETL on the newly obtained raw weather and water-level data. The resulting dataset should be registered and include quality-control figures with an overview plot. The workflow must log both ETL initiation and completion messages in the terminal. Lastly, ensure all artifacts are registered in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Sacramento"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Sacramento",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_san_diego.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_024",
        "instruction": "As a Data Science automation agent, your main goal is to assess SEATTLE_V1, a flood-risk analysis model for Portland, by using existing predictions without retraining and provide geocoding context in the project record. The workflow needs to calculate evaluation metrics and generate stakeholder-ready outputs, also creating a visualization artifact that summarizes performance. Finally, ensure that the file paths of all newly generated assets are registered in the project's central file directory and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "SEATTLE_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_SEATTLE_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SEATTLE_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SEATTLE_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_seattle.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_025",
        "instruction": "As a Data Science automation agent, your main goal is to create SEATTLE_V1, a flood-risk random_forest analysis model tailored for Portland. This model should utilize the processed dataset located at /data/processed/timeseries_seattle_weather.csv for training. Configure the final model with a classification threshold of 2.0 meters and ensure it is validated with a 40% / 0.4 test split. Make sure to register the file paths for all newly generated assets in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.4
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.4
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib",
                        "/metrics/MODEL_SEATTLE_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SEATTLE_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_026",
        "instruction": "Being a Data Science automation agent, your primary task is to construct a processed timeseries dataset for Norfolk by executing an ETL on the newly acquired raw weather and tide data. The final dataset must be registered and quality-control figures generated for review. Conclude by logging the completion to the terminal and registering all items in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Norfolk"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Norfolk"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Norfolk"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Norfolk",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_norfolk.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_027",
        "instruction": "You are a Data Science automation agent. Your task is to develop and establish a new flood-risk analysis project for the city of Orlando (7-day forecast horizon, a 50.0 km maximum station search radius). Make sure the final obtained dataset encompasses the city's geocoding, a comprehensive weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Verify that the file paths for all newly obtained raw data are correctly logged in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 25.7617,
                    "longitude": -80.1918
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_028",
        "instruction": "You are a Data Science automation agent. Your main goal is to generate a Notion page report for the city of Norfolk using existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SF_V1. Ensure to incorporate Executive Summary, Data & Methods in the report, and enhance the References section with sources from Zotero metadata. Conclude by logging the file paths for all resulting assets in the project\u2019s central file directory and composing an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Norfolk"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_029",
        "instruction": "As a Data Science automation agent, your main goal is to develop a processed timeseries dataset for Providence by conducting an ETL on new raw weather and tide data. Ensure the resulting dataset is registered and quality-control metrics are generated for evaluation. Lastly, document the completion in the terminal and register all items in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 42.3601,
                    "longitude": -71.0589
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Providence"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Providence",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_030",
        "instruction": "As a Data Science automation agent, your goal is to initiate and configure a new flood-risk analysis project for Providence (7-day forecast horizon, a 50.0 km maximum station search radius). The final dataset acquired should contain the city's geocoding, a comprehensive weather forecast, and tide predictions from the main NOAA station. Verify that paths for all newly acquired raw data are accurately recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 42.3601,
                    "longitude": -71.0589
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_031",
        "instruction": "You are a Data Science automation agent. Your main task is to develop a Notion page report for the city of Austin. Utilize existing predictions and metrics (PRED_001, METRICS_001) alongside the summary plot for model MODEL_SF_V1. Ensure the report comprises an Executive Summary, Data & Methods sections, and enhance the References section with sources from Zotero metadata. Finally, document the file paths for all resulting assets in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Austin"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_032",
        "instruction": "You are a Data Science automation agent. Your main task is to train C2_V1, a flood-risk analysis model intended for the city of C2. This model must be trained using the processed data located at /data/processed/timeseries_C2_weather.csv. The final configuration of the model should include a classification threshold of 2.0 meters and it must be validated using a 40% / 0.4 test split. The process must cover model training, prediction generation, and evaluation metrics. Lastly, make sure to prepare outputs suitable for stakeholders and register the file paths of all newly created assets in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "C2"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_C2_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.4
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.4
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "C2_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_C2_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_C2_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_033",
        "instruction": "Operate as a Data Science automation agent. Your main goal is the development of CHICAGO_V1, a flood-risk analysis model for the city of Milwaukee. Train this model using the processed data available in /data/processed/timeseries_chicago_weather.csv. The final model needs to be configured with a classification threshold of 3.5 meters and should be validated with a 35% / 0.35 test split. Make sure the file paths for all newly generated assets are documented in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Milwaukee"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Milwaukee"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_chicago_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 3.5,
                    "test_split_fraction": 0.35
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.35
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "CHICAGO_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_chicago.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_CHICAGO_V1.joblib",
                        "/metrics/MODEL_CHICAGO_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_CHICAGO_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_034",
        "instruction": "Act as a Data Science automation agent. Your main task is to construct a processed timeseries dataset for the city of Savannah by executing an ETL over newly acquired raw weather, tide data. The resulting dataset must be registered and quality-control figures must be produced for review. Finally, document the completion to the terminal and ensure everything is logged in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Savannah"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Savannah"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Savannah"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Savannah",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_savannah.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_035",
        "instruction": "Act as a Data Science automation agent. Your main task is to craft MIAMI_V1, which is a flood-risk analysis model for the city of Orlando. Train this model using the processed data located at /data/processed/timeseries_miami_weather.csv. The final model should have a classification threshold set at 3.0 meters and be validated with a 25% / 0.25 test split. Confirm that the file paths for any newly generated assets are documented in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 3.0,
                    "test_split_fraction": 0.25
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.25
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib",
                        "/metrics/MODEL_MIAMI_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_MIAMI_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_036",
        "instruction": "Function as a Data Science automation agent. Your primary task is to generate a succinct Executive Summary report in Notion for the city of Providence. Utilize the existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_BOSTON_V1. Ensure that only an Executive Summary section is included. Finally, make sure the file paths for all resulting assets are logged in the project\u2019s central file directory and prepare an email for stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_BOSTON_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_BOSTON_V1 - Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_BOSTON_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_037",
        "instruction": "You function as a Data Science automation agent. Your key task is to compile a Notion page report concerning the city of Portland. Utilize the provided prediction and metrics (PRED_001, METRICS_001) for the model MODEL_SF_V1. Ensure the report comprises an Executive Summary and Data & Methods section, and expand the References segment using Zotero metadata. Lastly, document the file paths for all produced assets in the project's main file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_038",
        "instruction": "You function as a Data Science automation agent. Your central task is to compile a brief Executive Summary report in Notion for the city of Austin. Employ the provided prediction and metrics (PRED_001, METRICS_001) for the model MODEL_HOUSTON_V1. Ensure that the report contains solely an Executive Summary section. Finally, document the file paths for all produced assets in the project's main file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Austin"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_HOUSTON_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_HOUSTON_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_HOUSTON_V1.png",
                        "/figures/summary_MODEL_HOUSTON_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_039",
        "instruction": "As a Data Science automation agent, your main task is to convey the latest evaluation outcomes for Chennai_V1, a flood-risk assessment model for Chennai. Compile the existing predictions and metrics (PRED_003, METRICS_003) into a Notion summary report and prepare an email draft to stakeholders@city.gov. Make sure all report artifacts and communication drafts are archived in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Chennai"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_003",
                    "metrics_id": "METRICS_003"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "Chennai_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "Chennai_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_040",
        "instruction": "Serving as a Data Science automation agent, your main responsibility is to create a processed time series dataset for New Orleans by executing an ETL on newly sourced raw weather and tide data. Make sure the resulting dataset is cataloged, and prepare quality-control graphics for evaluation. Conclude by noting the completion in the terminal and ensuring everything is stored in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "New Orleans"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "New Orleans"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "New Orleans"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "New Orleans",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_new_orleans.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_041",
        "instruction": "As a Data Science automation agent, focus on creating a processed timeseries dataset for the city of Austin by executing an ETL on newly obtained raw weather and tide data. Ensure the resulting dataset is registered, and generate quality-control figures for evaluation. Conclude by logging the completion in the terminal and registering all in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Austin"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Austin"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Austin"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Austin",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_042",
        "instruction": "Act as a Data Science automation agent with the main goal of constructing a processed timeseries dataset for the city of Charleston by performing an ETL on the newly received raw weather and tide data. Make sure the resulting dataset is registered and produce quality-control figures for review. Finally, log the completion to the terminal and ensure everything is registered in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Charleston"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_043",
        "instruction": "As a Data Science automation agent, your task is to initiate and configure a new flood-risk analysis project for the city of Portland (7-day forecast horizon, a 50.0 km maximum station search radius). The concluding dataset must encompass the city's geocoding, a comprehensive weather forecast, and the main NOAA station's observed water levels, tide predictions, and coastal meteorology records. Verify that the paths for all recently gathered raw data are correctly documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 47.6062,
                    "longitude": -122.3321
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_044",
        "instruction": "As a Data Science automation agent, your task is to initiate and configure a new flood-risk analysis project for the city of Providence (7-day forecast horizon, a 50.0 km maximum station search radius). The concluding dataset must encompass the city's geocoding, a comprehensive weather forecast, and the main NOAA station's observed water levels, tide predictions, and coastal meteorology records. Verify that the paths for all recently gathered raw data are correctly documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 42.3601,
                    "longitude": -71.0589
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_045",
        "instruction": "You are a Data Science automation agent. Your main goal is to compile a Notion page report focused on the city of Oakland. Utilize existing prediction and metrics (PRED_001, METRICS_001) for the model MODEL_SF_V1. Make sure the report includes an Executive Summary, Data & Methods section, and expand the References section using metadata from Zotero. Lastly, organize the file paths for all final assets in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_046",
        "instruction": "You are a Data Science automation agent. Your main task is to convey the latest evaluation results for HYD_V1, a model analyzing flood risk for the city of HYD. Employ existing predictions and metrics (PRED_002, METRICS_002) to prepare a Notion summary report and write an email to stakeholders@city.gov. Lastly, verify that all report elements and communication drafts are recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "HYD"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_002",
                    "metrics_id": "METRICS_002"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "HYD_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "HYD_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_047",
        "instruction": "You are a Data Science automation agent. Your goal is to initiate and configure a new flood-risk analysis project for Providence City (7-day forecast horizon, a 50.0 km maximum station search radius). The dataset you acquire should incorporate the city's geocoding along with the main NOAA station's observed water levels, tide predictions, and coastal meteorology records. Make certain that the file paths for all newly acquired raw data are accurately recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 40.7128,
                    "longitude": -74.006
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_048",
        "instruction": "You are a Data Science automation agent. Your main task is to develop a processed timeseries dataset for the city of Tampa by executing an ETL on newly obtained raw weather and water-level data. Ensure the resulting dataset is documented, including quality-control figures with an overview plot. The workflow should also track and display ETL start and completion messages in the terminal. Lastly, verify that all artifacts are documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Tampa"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Tampa"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Tampa"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_tampa.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_049",
        "instruction": "Handle the task of automating Data Science processes. Your main goal is to train C1_V1, a flood-risk analysis model tailored for the city of C1. Use the processed data located at /data/processed/timeseries_C1_weather.csv for model training. Configure the final model to have a classification threshold of 2.0 meters and validate it using a 20% / 0.2 test split. Your workflow should cover model training, prediction generation, and evaluation metrics. Conclude by preparing outputs suitable for stakeholders and recording the file paths of all newly generated assets in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "C1"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_C1_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "C1_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_C1_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_C1_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_050",
        "instruction": "Coordinate the development of a Data Science automation task. Your chief aim is to create BOSTON_V1, a flood-risk logistic_regression analysis model for Providence. Train this model with the processed data available at /data/processed/timeseries_boston_weather.csv. The model should be finalized with a classification threshold of 2.0 meters and validated using a 20% / 0.2 test split. Ensure the file paths for all newly generated assets are registered in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_BOSTON_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_051",
        "instruction": "As a Data Science automation agent, your main goal is to craft SEATTLE_V1, a flood-risk logistic_regression analysis model tailored for the city of Portland. This model needs to be trained using the processed dataset located at /data/processed/timeseries_seattle_weather.csv. The ultimate model should be configured with a classification threshold of 2.0 meters and validated with a 20% / 0.2 test split. Make certain to register file paths for all newly developed assets in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SEATTLE_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_052",
        "instruction": "As a Data Science automation agent, your core task is to develop a Notion page report for the city of Charleston, using the existing prediction and metrics (PRED_001, METRICS_001) for the model MODEL_SF_V1. Be sure to incorporate Executive Summary, Data & Methods in the report, and enhance the References section with sources from Zotero metadata. Lastly, ensure that file paths for all resulting assets are recorded in the project\u2019s central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_053",
        "instruction": "Act as a Data Science automation agent. Your task is to establish and configure a new flood-risk analysis initiative for the city of Providence (7-day forecast horizon, a 50.0 km maximum station search radius). The assembled dataset must incorporate the city's geocoding, a thorough weather forecast, and the main NOAA station's recorded water levels and tide predictions. Confirm that the file paths for all newly obtained raw data are correctly documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 42.3601,
                    "longitude": -71.0589
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_054",
        "instruction": "Act as a Data Science automation agent. The primary task is to disseminate the most up-to-date evaluation results for SF_V1, a flood-risk analysis model for the city of Oakland. With the available predictions and metrics (PRED_002, METRICS_002), compile them into a Notion summary report and prepare an email draft addressed to stakeholders@city.gov. Lastly, verify that all report materials and communication drafts are logged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_002",
                    "metrics_id": "METRICS_002"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SF_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "SF_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_055",
        "instruction": "Function as a Data Science automation agent. Your main task is to construct a processed timeseries dataset for the city of Providence by executing an ETL process on the recently obtained raw weather and water-level data. The finalized dataset needs to be documented, including quality-control metrics that feature an overview plot. The workflow should also record the ETL initiation and completion messages in the terminal. Lastly, make sure all artifacts are saved in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 42.3601,
                    "longitude": -71.0589
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Providence"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Providence",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_056",
        "instruction": "Operate as a Data Science automation agent. Your main assignment is to train MIAMI_V1, a flood-risk analysis model tailored for the city of Orlando. This model must be trained utilizing the processed data located in /data/processed/timeseries_miami_weather.csv. The ultimate model should be set with a classification threshold of 2.0 meters and evaluated using a 20% / 0.2 test split. The workflow should encompass model training, prediction creation, and assessment metrics. Finally, ensure outputs are stakeholder-ready, and file paths for all newly generated assets are logged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_MIAMI_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_MIAMI_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_057",
        "instruction": "Act as a Data Science automation agent. Your task is to design and configure a new flood-risk analysis initiative for the city of Sacramento (7-day forecast horizon, a 50.0 km maximum station search radius). The final dataset obtained must encompass the city's geocoding, a comprehensive weather forecast, and the main NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure the file paths for all newly acquired raw data are correctly logged in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 34.0522,
                    "longitude": -118.2437
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_058",
        "instruction": "Operate as a Data Science automation agent. Your task is to initiate and establish a new flood-risk analysis project for the city of Sacramento (7-day forecast horizon, a 50.0 km maximum station search radius). The ultimately acquired dataset must incorporate the city's geocoding, a thorough weather forecast, and the primary NOAA station's observed water levels and tide predictions. Ensure the file paths for all newly acquired raw data are correctly logged in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 34.0522,
                    "longitude": -118.2437
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Sacramento"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_la.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_059",
        "instruction": "You are a Data Science automation agent. Your main task is to convey the latest evaluation outcomes for Delhi_V1, a flood-risk assessment model for the city of Delhi. Using the current predictions and metrics (PRED_001, METRICS_001), compile them into a Notion summary report and compose an email to stakeholders@city.gov. Lastly, confirm that all report materials and communication drafts are catalogued in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Delhi"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "Delhi_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "Delhi_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_060",
        "instruction": "You are a Data Science automation agent. Your main goal is to create SEATTLE_V1, a flood-risk assessment model for the city of Portland. Train this model using the processed data located in /data/processed/timeseries_seattle_weather.csv. Configure the final model with a classification threshold of 2.2 meters and validate it using a 15% / 0.15 test split. Verify that the file paths for all newly generated assets are registered in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.2,
                    "test_split_fraction": 0.15
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.15
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SEATTLE_V1.joblib",
                        "/metrics/MODEL_SEATTLE_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SEATTLE_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_061",
        "instruction": "Function as a Data Science automation agent. Your primary task is to construct NEW_YORK_V1, a model for flood-risk analysis tailored for Providence City. This model necessitates training with the processed data located at /data/processed/timeseries_new_york_weather.csv. Configure the terminal model to a classification threshold of 2.5 meters and validate it with a 20% / 0.2 test split. Ensure the registration of file paths for all newly generated assets within the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_new_york_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.5,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "NEW_YORK_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_NEW_YORK_V1.joblib",
                        "/metrics/MODEL_NEW_YORK_V1_train_metrics.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_NEW_YORK_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_062",
        "instruction": "Act as a Data Science automation agent. Your main task is to devise a processed timeseries dataset for Galveston by conducting an ETL on the freshly acquired raw weather and tide data. The final dataset needs to be registered, and quality-control visuals should be generated for evaluation. In conclusion, record the completion in the terminal and document everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Galveston"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Galveston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Galveston"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Galveston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_galveston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_063",
        "instruction": "Acting as a Data Science automation agent, your main goal is to compile a processed timeseries dataset for Charleston by executing an ETL process on newly collected raw weather and tide data. Ensure the resulting dataset is registered and produce quality-control figures for review. Conclude by logging the completion to the terminal and recording everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Charleston"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_064",
        "instruction": "Serve as a Data Science automation agent with the primary aim of relaying the latest evaluation findings for SEATTLE_V1, a flood-risk analysis model for Portland. Consolidate existing predictions and metrics (PRED_001, METRICS_001) into a Notion summary report and prepare a draft email for stakeholders@city.gov. Lastly, confirm that all report content and communication drafts are documented in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SEATTLE_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "SEATTLE_V1 Flood-Risk Results",
                    "body_text": "Stakeholder summary for SEATTLE_V1 is available. Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_065",
        "instruction": "You act as a Data Science automation agent. Your main task is to build MIAMI_V1, a flood-risk logistic_regression analysis model for Orlando. This model should be trained with the processed data available at /data/processed/timeseries_miami_weather.csv. The final model configuration must include a classification threshold of 2.0 meters and be validated with a 20% / 0.2 test split. Be sure to record the file paths for all newly produced assets in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "logistic_regression"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_MIAMI_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_066",
        "instruction": "You function as a Data Science automation agent. Your main task is to generate a concise Executive Summary report in Notion for Sacramento. Utilize existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_SAN_DIEGO_V1. Ensure that only an Executive Summary section is included. Lastly, document the file paths for all resulting assets in the project\u2019s central file directory and prepare an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Sacramento"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SAN_DIEGO_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SAN_DIEGO_V1 - Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_SAN_DIEGO_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SAN_DIEGO_V1.png",
                        "/figures/summary_MODEL_SAN_DIEGO_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_067",
        "instruction": "As a Data Science automation agent, your main task is to deliver the latest assessment outcomes for Miami_V1, a flood-risk evaluation model for Orlando city. Using existing predictions and metrics (PRED_002, METRICS_002), assemble them into a Notion summary report and compose an email addressed to stakeholders@city.gov. Lastly, confirm that all report artifacts and communication drafts are recorded in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_002",
                    "metrics_id": "METRICS_002"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "Miami_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "Miami_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_068",
        "instruction": "Acting as a Data Science automation agent, your main responsibility is to develop a processed timeseries dataset for Portland by executing an ETL on newly gathered raw weather and tide data. Ensure that the resulting dataset is registered, and quality-control visuals are generated for evaluation. Finally, register the completion in the terminal and record everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 47.6062,
                    "longitude": -122.3321
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Portland"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_069",
        "instruction": "Act as a Data Science automation agent. Your main goal is to construct MIAMI_V1, a flood-risk random_forest analysis model meant for Orlando. Utilize processed data from /data/processed/timeseries_miami_weather.csv for training. Configure the final model with a classification threshold of 2.0 meters, and validate it with a test split of 40% / 0.4. Make certain to register the file paths of all new assets in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_miami_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.4
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.4
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "MIAMI_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_MIAMI_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_MIAMI_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_070",
        "instruction": "Function as a Data Science automation agent. Your main aim is to assess BOSTON_V1, a flood-risk analysis model for Providence, by employing existing predictions without retraining, and incorporate geocoding context into the project record. The workflow should calculate evaluation metrics, prepare stakeholder-ready outputs, and create a visualization artifact summarizing performance. Lastly, ensure all new asset file paths are entered in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "BOSTON_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_BOSTON_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_BOSTON_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "BOSTON_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_BOSTON_V1.png",
                        "/figures/summary_MODEL_BOSTON_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_071",
        "instruction": "As a Data Science automation agent, your key task is to construct a processed timeseries dataset for the city of Norfolk by executing an ETL on newly obtained raw weather and water-level data. The resulting dataset should be registered and include quality-control figures, such as an overview plot. The workflow must also document the ETL start and completion messages in the terminal. Lastly, make sure that all artifacts are saved in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Norfolk"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Norfolk"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Norfolk"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Norfolk",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_norfolk.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_gaps.png",
                        "/figures/qc_overview.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_072",
        "instruction": "In your role as a Data Science automation agent, your goal is to establish and configure a new flood-risk analysis project for the city of Oakland (28-day forecast horizon, a 100.0 km maximum station search radius). The final acquired dataset should comprise the city's geocoding, a comprehensive weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorology records. Ensure that the paths for all newly acquired raw data files are correctly recorded in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland",
                    "forecast_horizon_days": 28,
                    "max_station_distance_km_nullable": 100.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_073",
        "instruction": "As a Data Science automation agent, your main task is to convey the latest evaluation results for LA_V1, which is a flood-risk analysis model for Sacramento. Utilize the existing predictions and metrics (PRED_002, METRICS_002) to compile them into a summary report on Notion and compose an email addressed to stakeholders@city.gov. Lastly, make certain that all report artifacts and communication drafts are filed in the project's central directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "LA"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_002",
                    "metrics_id": "METRICS_002"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "LA_V1 - Stakeholder Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "subject": "LA_V1 Flood-Risk Results",
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_074",
        "instruction": "As a Data Science automation agent, your main goal is to create SF_V1, a flood-risk random_forest analysis model for Oakland. This model needs to be trained using the processed data located at /data/processed/timeseries_sf_weather.csv. The ultimate model should have a classification threshold of 2.0 meters and undergo validation with a 40% / 0.4 test split. Make sure all file paths for any newly created assets are documented in the project's central directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_sf_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.4
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.4
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SF_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SF_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_075",
        "instruction": "Acting as a Data Science automation agent, your main task is to assess the SEATTLE_V1 flood-risk analysis model for Portland by evaluating existing predictions (without retraining), calculating evaluation metrics, and generating outputs suitable for stakeholders, including a visualization depicting performance. Lastly, make sure that all file paths for newly developed assets are logged in the project's central directory, then create a Notion page and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "SEATTLE_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_SEATTLE_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SEATTLE_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SEATTLE_V1 Model Evaluation Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_076",
        "instruction": "As a Data Science automation agent, your core task is to assemble a Notion page report for Orlando city. Utilize the existing prediction and metrics (PRED_001, METRICS_001) for the MODEL_SF_V1, ensuring to incorporate an Executive Summary and Data & Methods in the report, along with enhancing the References section with inputs from Zotero metadata. Finally, document the file paths of all generated assets in the project's central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_077",
        "instruction": "As a Data Science automation agent, your main task is to create a processed timeseries dataset for the city of Portland by executing an ETL on the recently obtained raw weather and water-level data. The dataset produced must be documented, with quality-control metrics that include an overview plot. The process should also note the ETL initiation and end messages in the terminal. Lastly, confirm that all products are cataloged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 47.6062,
                    "longitude": -122.3321
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Portland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_seattle.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_078",
        "instruction": "As a Data Science automation agent, your main task is to create a processed timeseries dataset for the city of Austin by executing an ETL on the recently obtained raw weather and water-level data. The dataset produced must be documented, with quality-control metrics that include an overview plot. The process should also note the ETL initiation and end messages in the terminal. Lastly, confirm that all products are cataloged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Austin"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Austin"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Austin"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Austin",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "overview"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_houston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_079",
        "instruction": "As a Data Science automation agent, your main task is to construct SF_V1, a flood-risk analysis model for Oakland. Train this model using the processed data located at /data/processed/timeseries_sf_weather.csv. The final configuration must include a classification threshold of 2.0 meters, and validation should be performed using a 20% / 0.2 test split. Make sure to record the file paths for all newly created assets in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_sf_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_SF_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SF_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_080",
        "instruction": "Acting as a Data Science automation agent, your task is to establish a new flood-risk analysis project for Providence City (14-day forecast horizon, with a 75.0 km maximum station search radius). The final dataset must incorporate the city's geocoding, the full weather forecast, and records from the main NOAA station on water levels, tide predictions, and coastal meteorology. Ensure that file paths for all newly acquired raw data are accurately documented in the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence",
                    "forecast_horizon_days": 14,
                    "max_station_distance_km_nullable": 75.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 40.7128,
                    "longitude": -74.006
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Providence"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_nyc.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_081",
        "instruction": "As a Data Science automation agent, your main task is to develop a processed timeseries dataset for the city of Portland by executing an ETL on newly acquired raw weather and tide data. Ensure the resulting dataset is registered and produce quality-control figures for review. Conclude the process by logging the completion to the terminal and registering everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Portland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Portland"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Portland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_portland.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_082",
        "instruction": "Your function as a Data Science automation agent is to craft a concise Executive Summary report in Notion for the city of Orlando, utilizing the existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_MIAMI_V1. Ensure it contains only the Executive Summary section. Conclude by registering the file paths for all resulting assets in the project\u2019s central file directory and drafting an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_MIAMI_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_MIAMI_V1 - Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_MIAMI_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_083",
        "instruction": "You are a Data Science automation agent. Your main task is to develop a concise Executive Summary report in Notion for the city of Providence. Utilize the existing prediction and metrics (PRED_001, METRICS_001) for model MODEL_NEW_YORK_V1. Ensure that only an Executive Summary section is included. Lastly, log the file paths for all resulting assets in the project\u2019s central file directory and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_NEW_YORK_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_NEW_YORK_V1 - Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_NEW_YORK_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_NEW_YORK_V1.png",
                        "/figures/summary_MODEL_NEW_YORK_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_084",
        "instruction": "You are a Data Science automation agent. Your primary task is to create a processed timeseries dataset for the city of Annapolis by performing an ETL over the freshly acquired raw weather, tide data. The resulting dataset needs to be registered, and quality-control figures should be generated for evaluation. Finally, record the task completion in the terminal and document everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Annapolis"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Annapolis"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Annapolis"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Annapolis",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_annapolis.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_085",
        "instruction": "You are a Data Science automation agent. Your main task is to assemble a processed timeseries dataset for the city of Oakland by executing an ETL on the newly acquired raw weather and tide data. Ensure that the resulting dataset is registered and that quality-control figures are generated for examination. Ultimately, log the completion in the terminal and archive everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Oakland"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Oakland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_086",
        "instruction": "You are a Data Science automation agent. Your main task is to generate a Notion page report for the city of Tampa using the existing prediction and metrics (PRED_001, METRICS_001) for the model MODEL_SF_V1. Ensure that the report includes an Executive Summary and Data & Methods, and enrich the References section with information sourced from Zotero metadata. In conclusion, register the file paths for all resulting assets in the project\u2019s central file directory and prepare an email draft for stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Tampa"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SF_V1 - Report",
                    "properties": {
                        "PredictionsCSV": "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "MetricsJSON": "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "PrimaryFigure": "/figures/summary_MODEL_SF_V1.png"
                    },
                    "tags": [
                        "Executive Summary",
                        "Data & Methods"
                    ]
                },
            },
            {
                "name": "enrichNotion",
                "arguments": {
                    "model_id": "MODEL_SF_V1",
                    "page_id": "NOTION_PAGE_001"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_087",
        "instruction": "As a Data Science automation agent, your main goal is to assess SF_V1, the flood-risk analysis model for Oakland, utilizing current predictions (no retraining), calculate evaluation metrics, and create outputs that are ready for stakeholders. It should also generate a visual artifact summarizing its performance. Finally, ensure all new asset file paths are recorded in the project's central file directory and develop a Notion page while drafting an email to stakeholders@city.gov afterward.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "SF_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_SF_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SF_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "SF_V1 Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion- /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SF_V1.png",
                        "/figures/summary_MODEL_SF_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_088",
        "instruction": "Your role as a Data Science automation agent involves constructing a processed timeseries dataset for Oakland by running an ETL on newly obtained raw weather and water-level data. The final dataset must be logged, including quality-control visuals like a gaps plot. The process should also record the ETL beginning and completion messages in the terminal. Lastly, make sure all artifacts are documented in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Oakland"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Oakland"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Oakland",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "gaps"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_sf.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_089",
        "instruction": "Handle a Data Science automation task. Your goal is to initiate and organize a flood-risk analysis project for Charleston city (7-day forecast horizon, with a 50.0 km limit for station searches). The concluding dataset acquired should consist of the city's geocoding, a comprehensive weather forecast, and tide predictions from the principal NOAA station. Confirm that all file paths for the newly acquired raw data are correctly documented within the project's main file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_090",
        "instruction": "Coordinate a Data Science automation task. Your goal is to initiate and organize a flood-risk analysis project for Charleston city (7-day forecast horizon, with a 50.0 km limit for station searches). The concluding dataset acquired should consist of the city's geocoding, a comprehensive weather forecast, and the primary NOAA station's observed water levels, tide predictions, and coastal meteorological data. Confirm that all file paths for the newly acquired raw data are correctly documented within the project's main file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston",
                    "forecast_horizon_days": 7,
                    "max_station_distance_km_nullable": 50.0
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setCoastalMeteorology",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/raw/coastal_meteorology_NOAA_STATION_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_091",
        "instruction": "Your role is to operate as a Data Science automation agent. The primary task is to assess the MIAMI_V1 flood-risk analysis model for Orlando, employing existing predictions (avoid retraining), and incorporate geocoding context in the project record. The process must calculate evaluation metrics and create outputs suitable for stakeholders, generating a visualization artifact that summarizes the model's performance. Lastly, ensure the file paths for all new assets are logged in the project's central file directory, and compose an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "getModel",
                "arguments": {
                    "model_name": "MIAMI_V1"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "model_id": "MODEL_MIAMI_V1"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_MIAMI_V1"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MIAMI_V1 Results"
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ],
                    "body": "Notion: /notion/pages/NOTION_PAGE_001.json"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_MIAMI_V1.png",
                        "/figures/summary_MODEL_MIAMI_V1.png",
                        "/gmail/outbox/GMAIL_MSG_001.json",
                        "/data/raw/geocoding_miami.json",
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_092",
        "instruction": "Act as a Data Science automation agent. The main aim is to generate a succinct Executive Summary report in Notion for Portland. Utilizing existing predictions and metrics (PRED_001, METRICS_001) related to the MODEL_SEATTLE_V1, make certain to focus solely on the Executive Summary section. Lastly, log the file paths of all resulting assets into the project\u2019s central file directory and draft an email to stakeholders@city.gov.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "createSummaryPlots",
                "arguments": {
                    "model_id": "MODEL_SEATTLE_V1",
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "createNotionPageJson",
                "arguments": {
                    "title": "MODEL_SEATTLE_V1 - Executive Summary",
                    "tags": [
                        "Executive Summary"
                    ],
                    "properties": {
                        "PrimaryFigure": "/figures/summary_MODEL_SEATTLE_V1.png"
                    }
                },
            },
            {
                "name": "createGmailJson",
                "arguments": {
                    "to": [
                        "stakeholders@city.gov"
                    ],
                    "body_text": "Notion JSON: /notion/pages/NOTION_PAGE_001.json",
                    "attachments_paths": [
                        "/notion/pages/NOTION_PAGE_001.json"
                    ]
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json",
                        "/figures/risk_timeseries_MODEL_SEATTLE_V1.png",
                        "/figures/summary_MODEL_SEATTLE_V1.png",
                        "/notion/pages/NOTION_PAGE_001.json",
                        "/gmail/outbox/GMAIL_MSG_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "PROJ_DIR_001",
                "STAKEHOLDER_OUTPUT_001",
                "NOTION_PAGE_001",
                "GMAIL_MSG_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_093",
        "instruction": "As a Data Science automation agent, your main goal is to train BOSTON_V1, a model designed for flood-risk analysis in Providence. This training should utilize the processed dataset located at /data/processed/timeseries_boston_weather.csv. Configure the final model with a classification threshold of 2.0 meters, and validate using a test split of 20% or 0.2. The process must encompass model training, generation of predictions, and evaluation of metrics. Lastly, create stakeholder-ready outputs, and make sure to log the file paths of all new assets within the project's central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_BOSTON_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_BOSTON_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_094",
        "instruction": "As a Data Science automation agent, your main task is to construct a processed timeseries dataset for Tampa by performing an ETL on newly acquired raw weather and tide information. The finalized dataset must be recorded, and quality-control visualizations should be generated for analysis. Conclude by logging the completion in the terminal and registering all elements in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Tampa"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Tampa"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Tampa"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Tampa",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_tampa.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_095",
        "instruction": "Handle the creation of a processed timeseries dataset for Baltimore as a Data Science automation agent. Focus on executing an ETL process using the latest raw weather and water-level data. The final dataset should be documented, including quality-control metrics and a summary plot. Ensure the workflow logs ETL start and completion messages in the terminal and that all outputs are stored in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Baltimore"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Baltimore"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 55,
                    "longitude": 55
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Baltimore"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Baltimore",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_baltimore.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_096",
        "instruction": "Coordinate the training of SF_V1, a flood-risk analysis model for Oakland, as a Data Science automation agent. Use the processed data from /data/processed/timeseries_sf_weather.csv for training. Set the classification threshold at 2.0 meters and perform validation with a 20% / 0.2 test split. This workflow must encompass model training, prediction generation, and evaluation metrics. Lastly, prepare output suitable for stakeholders and register the file paths for all new assets in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Oakland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_sf_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "SF_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_SF_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SF_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_097",
        "instruction": "Acting as a Data Science automation agent, your main task is to create BOSTON_V1, a flood-risk random_forest analysis model for Providence. This model should utilize the processed data found at /data/processed/timeseries_boston_weather.csv for training. Ensure that the model is set with a classification threshold of 2.0 meters and is validated with a 40% / 0.4 test split. Make sure all file paths for newly generated assets are logged in the project\u2019s central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Providence"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_boston_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.4
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.4
                },
            },
            {
                "name": "createModel",
                "arguments": {
                    "model_name": "BOSTON_V1",
                    "features_id": "FEATURES_001",
                    "model_config_id": "MODEL_CONFIG_001",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/models/MODEL_BOSTON_V1.joblib"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_BOSTON_V1"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_098",
        "instruction": "As a Data Science automation agent, your main goal is to construct a processed timeseries dataset for Orlando by executing an ETL on freshly acquired raw weather and tide data. The resultant dataset should be documented, and quality-control figures need to be generated for evaluation. In the end, record the completion in the terminal and file everything in the central file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Orlando"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Orlando"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 25.7617,
                    "longitude": -80.1918
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Orlando"
                },
            },
            {
                "name": "setTidePredictions",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Orlando",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "tides_raw_path": "/data/raw/tide_predictions_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_miami.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/tide_predictions_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_overview.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_099",
        "instruction": "As a Data Science automation agent, your key task is to train the flood-risk analysis model SEATTLE_V1 for Portland. Utilize the processed data from /data/processed/timeseries_seattle_weather.csv for training. Configure the final model with a classification threshold of 2.0 meters and validate with a 20% / 0.2 test split. The workflow should include training the model, generating predictions, and assessing evaluation metrics. Finally, ensure outputs suitable for stakeholders are prepared, and record the file paths for all new assets in the project's centralized file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Portland"
                },
            },
            {
                "name": "createFeatures",
                "arguments": {
                    "input_csv_path": "/data/processed/timeseries_seattle_weather.csv"
                },
            },
            {
                "name": "setModelConfig",
                "arguments": {
                    "classification_threshold_m": 2.0,
                    "test_split_fraction": 0.2
                },
            },
            {
                "name": "createDatasetSplit",
                "arguments": {
                    "features_id": "FEATURES_001",
                    "test_fraction": 0.2
                },
            },
            {
                "name": "trainModel",
                "arguments": {
                    "model_name": "SEATTLE_V1",
                    "features_id": "FEATURES_001",
                    "config_id": "MODEL_CONFIG_001",
                    "split_id": "SPLIT_001"
                },
            },
            {
                "name": "evaluateModel",
                "arguments": {
                    "predictions_id": "PRED_001"
                },
            },
            {
                "name": "prepareStakeholderOutputs",
                "arguments": {
                    "predictions_id": "PRED_001",
                    "metrics_id": "METRICS_001"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/processed_data/features_001.csv",
                        "/configs/model_config_MODEL_CONFIG_001.json",
                        "/processed_data/split_summary_SPLIT_001.json",
                        "/predictions/PRED_MODEL_SEATTLE_V1.csv",
                        "/metrics/metrics_METRICS_001.json",
                        "/deliverables/final_predictions_STAKEHOLDER_OUTPUT_001.csv",
                        "/deliverables/final_metrics_STAKEHOLDER_OUTPUT_001.json"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "PROJ_DIR_001",
                "FEATURES_001",
                "MODEL_CONFIG_001",
                "SPLIT_001",
                "MODEL_SEATTLE_V1",
                "PRED_001",
                "METRICS_001",
                "STAKEHOLDER_OUTPUT_001"
        ]
    }
    ,
    {
        "annotator": gokulsaireddy,
        "user_id": "task_100",
        "instruction": "As a Data Science automation agent, your main goal is to construct a processed timeseries dataset for Charleston by executing an ETL process on new raw weather and water-level data. Ensure the resulting dataset is registered and includes a plot demonstrating quality-control figures such as anomalies. The workflow should also log messages indicating the ETL start and finish in the terminal. Lastly, ensure that all artifacts are documented in the project's centralized file directory.",
        "actions": [
            {
                "name": "setProjectConfig",
                "arguments": {
                    "target_city": "Charleston"
                },
            },
            {
                "name": "setGeocodeCity",
                "arguments": {
                    "city_name": "Charleston"
                },
            },
            {
                "name": "findNoaaStation",
                "arguments": {
                    "latitude": 32.7765,
                    "longitude": -79.9311
                },
            },
            {
                "name": "setWeatherForecast",
                "arguments": {
                    "city": "Charleston"
                },
            },
            {
                "name": "setWaterLevels",
                "arguments": {
                    "station_id": "NOAA_STATION_001"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL started"
                },
            },
            {
                "name": "startEtlRun",
                "arguments": {
                    "city_name": "Charleston",
                    "weather_raw_path": "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                    "water_levels_raw_path": "/data/raw/water_levels_NOAA_STATION_001.json"
                },
            },
            {
                "name": "registerProcessedTimeseries",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv"
                },
            },
            {
                "name": "createQcfigures",
                "arguments": {
                    "processed_csv_path": "/data/processed/timeseries_ETL_001.csv",
                    "figure_type": "anomalies"
                },
            },
            {
                "name": "appendTerminalLog",
                "arguments": {
                    "message": "ETL run complete",
                    "type": "completed"
                },
            },
            {
                "name": "setProjectDirectories",
                "arguments": {
                    "files": [
                        "/data/raw/geocoding_charleston.json",
                        "/data/raw/noaa_station_NOAA_STATION_001.json",
                        "/data/raw/weather_forecast_WEATHER_FORECAST_001.json",
                        "/data/raw/water_levels_NOAA_STATION_001.json",
                        "/data/processed/timeseries_ETL_001.csv",
                        "/figures/qc_anomalies.png",
                        "/figures/qc_gaps.png"
                    ]
                }
            }
        ],
        "outputs": [
                "CONFIG_001",
                "ETL_001",
                "QC_FIG_001",
                "PROJ_DIR_001"
        ]
    }
]
