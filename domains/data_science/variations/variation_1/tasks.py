# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "ds_v1_001",
        "instruction": "Ensure to document a Coos Bay intake baseline. Final state: config 'Coos Bay' (UTC); geocoding 43.3670,-124.2170; proximity includes '9432780' set primary; observed water levels include '2025-05-03T02:00:00Z' = 1.02 (m); tide predictions include '2025-05-03T02:00:00Z' = 1.09 (m); merged artifact at 'processed_data/merged_timeseries_coosbay.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Coos Bay",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Coos Bay",
                    "latitude": 43.367,
                    "longitude": -124.217
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 43.367,
                    "query_longitude": -124.217,
                    "station_ids": [
                        "9432780"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9432780"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9432780",
                    "timestamps": [
                        "2025-05-03T02:00:00Z"
                    ],
                    "water_level_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9432780",
                    "timestamps": [
                        "2025-05-03T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_coosbay.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_002",
        "instruction": "Ensure to generate a Neah Bay intake baseline. Completion: config 'Neah Bay' (UTC); geocoding 48.3681,-124.6241; proximity includes '9443090' primary; observed '2025-05-05T00:00:00Z' = 0.97 (m); predictions '2025-05-05T00:00:00Z' = 1.04 (m); merged at 'processed_data/merged_timeseries_neahbay.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Neah Bay",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Neah Bay",
                    "latitude": 48.3681,
                    "longitude": -124.6241
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 48.3681,
                    "query_longitude": -124.6241,
                    "station_ids": [
                        "9443090"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9443090"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9443090",
                    "timestamps": [
                        "2025-05-05T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.97
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9443090",
                    "timestamps": [
                        "2025-05-05T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.04
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_neahbay.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_003",
        "instruction": "It is necessary to register a Tacoma intake baseline. Conclude with: config 'Tacoma' (UTC); geocoding 47.2529,-122.4443; proximity includes '9448000' primary; observed '2025-05-06T03:00:00Z' = 0.99 (m); predictions '2025-05-06T03:00:00Z' = 1.05 (m); merged at 'processed_data/merged_timeseries_tacoma.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Tacoma",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Tacoma",
                    "latitude": 47.2529,
                    "longitude": -122.4443
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 47.2529,
                    "query_longitude": -122.4443,
                    "station_ids": [
                        "9448000"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9448000"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9448000",
                    "timestamps": [
                        "2025-05-06T03:00:00Z"
                    ],
                    "water_level_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9448000",
                    "timestamps": [
                        "2025-05-06T03:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_tacoma.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_004",
        "instruction": "It is required to create a Bellingham intake baseline. Finalize with: config 'Bellingham' (UTC); geocoding 48.7491,-122.4787; proximity includes '9449211' primary; observed '2025-05-07T00:00:00Z' = 1.02 (m); predictions '2025-05-07T00:00:00Z' = 1.09 (m); merged at 'processed_data/merged_timeseries_bellingham.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Bellingham",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Bellingham",
                    "latitude": 48.7491,
                    "longitude": -122.4787
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 48.7491,
                    "query_longitude": -122.4787,
                    "station_ids": [
                        "9449211"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9449211"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9449211",
                    "timestamps": [
                        "2025-05-07T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9449211",
                    "timestamps": [
                        "2025-05-07T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_bellingham.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_005",
        "instruction": "Handle the assembly of an Astoria modeling bundle. Final outcome: features should be at 'processed_data/features_astoria.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-05-09T09:05:00Z'); ensure the config is at 'processed_data/model_config_astoria.json' with classification_threshold_m 0.58 (created_ts '2025-05-09T09:06:00Z'); split data found at 'processed_data/split_astoria.json'; verify the model 'astoria_lr_v1' is saved at 'models/astoria_lr_v1.joblib'; predictions should be recorded at 'processed_data/preds_astoria_lr_v1.csv' (generated_ts '2025-05-09T10:30:00Z'); metrics must be captured at 'processed_data/metrics_astoria_lr_v1.csv' (auc 0.70); and ensure stakeholder references link to these artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_astoria.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-05-09T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_astoria.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-05-09T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_astoria.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "astoria_lr_v1",
                    "model_path": "models/astoria_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "astoria_lr_v1",
                    "predictions_csv_path": "processed_data/preds_astoria_lr_v1.csv",
                    "generated_ts": "2025-05-09T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "astoria_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_astoria_lr_v1.csv",
                    "auc_nullable": 0.7
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_astoria_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_astoria_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_006",
        "instruction": "Coordinate leaving the database in a reproducible Pacifica baseline. By the conclusion: ensure a configuration row displays target_city 'Pacifica' with timezone 'UTC'; a geocoding entry should position 'Pacifica' at 37.6138,-122.4869; results at those coordinates ought to include station '9414520', setting it as primary; observed water level for '9414520' must include '2025-02-01T00:00:00Z' = 1.05 (m); tide predictions for '9414520' must also include '2025-02-01T00:00:00Z' = 1.15 (m); and verify there is a processed artifact at 'processed_data/merged_timeseries_pacifica.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Pacifica",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Pacifica",
                    "latitude": 37.6138,
                    "longitude": -122.4869
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.6138,
                    "query_longitude": -122.4869,
                    "station_ids": [
                        "9414520"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414520"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414520",
                    "timestamps": [
                        "2025-02-01T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414520",
                    "timestamps": [
                        "2025-02-01T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.15
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_pacifica.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_007",
        "instruction": "Handle the capture of a baseline for Moss Landing. By the end: ensure the configuration displays target_city 'Moss Landing' with timezone 'UTC'; geocoding should pin 'Moss Landing' at 36.8067,-121.7896; a proximity record for those coordinates must include '9413450' which you set as primary; observed water levels for '9413450' should incorporate '2025-02-03T03:00:00Z' = 0.92 (m); tide predictions for '9413450' must include '2025-02-03T03:00:00Z' = 1.00 (m); and a processed artifact needs to be present at 'processed_data/merged_timeseries_moss.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Moss Landing",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Moss Landing",
                    "latitude": 36.8067,
                    "longitude": -121.7896
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 36.8067,
                    "query_longitude": -121.7896,
                    "station_ids": [
                        "9413450"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9413450"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9413450",
                    "timestamps": [
                        "2025-02-03T03:00:00Z"
                    ],
                    "water_level_m": [
                        0.92
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9413450",
                    "timestamps": [
                        "2025-02-03T03:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_moss.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_008",
        "instruction": "Coordinate the preparation of a baseline for Capitola. Final state: a configuration row must have target_city 'Capitola' and timezone 'UTC'; a geocoding record should place 'Capitola' at 36.9750,-121.9540; a proximity result at those coordinates is to include '9413830' with that station set as primary; observed water levels for '9413830' must include '2025-02-04T12:00:00Z' = 1.18 (m); tide predictions for '9413830' should incorporate '2025-02-04T12:00:00Z' = 1.22 (m); and a processed artifact must be registered at 'processed_data/merged_timeseries_capitola.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Capitola",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Capitola",
                    "latitude": 36.975,
                    "longitude": -121.954
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 36.975,
                    "query_longitude": -121.954,
                    "station_ids": [
                        "9413830"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9413830"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9413830",
                    "timestamps": [
                        "2025-02-04T12:00:00Z"
                    ],
                    "water_level_m": [
                        1.18
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9413830",
                    "timestamps": [
                        "2025-02-04T12:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.22
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_capitola.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_009",
        "instruction": "Handle the registration of a Pescadero intake. The final configuration indicates: target_city as 'Pescadero' with timezone 'UTC'; 'Pescadero' is geocoded at 37.2550,-122.3833; a proximity record at these coordinates includes '9415025' set as primary; observed water levels for '9415025' show '2025-02-06T02:00:00Z' = 0.85 (m); tide predictions for '9415025' are '2025-02-06T02:00:00Z' = 0.90 (m); and there is a processed artifact located at 'processed_data/merged_timeseries_pescadero.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Pescadero",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Pescadero",
                    "latitude": 37.255,
                    "longitude": -122.3833
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.255,
                    "query_longitude": -122.3833,
                    "station_ids": [
                        "9415025"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9415025"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9415025",
                    "timestamps": [
                        "2025-02-06T02:00:00Z"
                    ],
                    "water_level_m": [
                        0.85
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9415025",
                    "timestamps": [
                        "2025-02-06T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.9
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_pescadero.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_010",
        "instruction": "Coordinate the capture of an Aptos intake. The resulting state should display: configuration with target_city 'Aptos' and timezone 'UTC'; geocoding assigns 'Aptos' to 36.9772,-121.9009; proximity record for these coordinates lists '9413748' as primary; observed water levels for '9413748' indicate '2025-02-08T01:00:00Z' = 1.05 (m); tide predictions for '9413748' are '2025-02-08T01:00:00Z' = 1.12 (m); and a processed artifact exists at 'processed_data/merged_timeseries_aptos.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Aptos",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Aptos",
                    "latitude": 36.9772,
                    "longitude": -121.9009
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 36.9772,
                    "query_longitude": -121.9009,
                    "station_ids": [
                        "9413748"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9413748"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9413748",
                    "timestamps": [
                        "2025-02-08T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9413748",
                    "timestamps": [
                        "2025-02-08T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.12
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_aptos.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_011",
        "instruction": "Register a Santa Barbara baseline. In the end state: the configuration displays target_city 'Santa Barbara' and timezone 'UTC'; geocoding identifies 'Santa Barbara' at 34.4208,-119.6982; a proximity record at those coordinates incorporates '9411340' which is established as primary; observed water levels for '9411340' encompass '2025-02-09T00:00:00Z' = 0.88 (m); tide predictions for '9411340' encompass '2025-02-09T00:00:00Z' = 0.95 (m); and a processed artifact is found at 'processed_data/merged_timeseries_sb.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Santa Barbara",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Santa Barbara",
                    "latitude": 34.4208,
                    "longitude": -119.6982
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.4208,
                    "query_longitude": -119.6982,
                    "station_ids": [
                        "9411340"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411340"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411340",
                    "timestamps": [
                        "2025-02-09T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.88
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411340",
                    "timestamps": [
                        "2025-02-09T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.95
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sb.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_012",
        "instruction": "Complete a Ventura baseline. At the finalized state: the configuration lists target_city 'Ventura' with timezone 'UTC'; geocoding sets 'Ventura' at 34.2746,-119.2290; a proximity entry at those coordinates incorporates '9411188' which is designated primary; observed water levels for '9411188' mention '2025-02-10T04:00:00Z' = 0.91 (m); tide predictions for '9411188' mention '2025-02-10T04:00:00Z' = 0.98 (m); and a processed artifact is located at 'processed_data/merged_timeseries_ventura.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Ventura",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Ventura",
                    "latitude": 34.2746,
                    "longitude": -119.229
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.2746,
                    "query_longitude": -119.229,
                    "station_ids": [
                        "9411188"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411188"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411188",
                    "timestamps": [
                        "2025-02-10T04:00:00Z"
                    ],
                    "water_level_m": [
                        0.91
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411188",
                    "timestamps": [
                        "2025-02-10T04:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.98
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_ventura.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_013",
        "instruction": "Ensure that a Monterey modeling bundle is recorded. The outcome should include: features located at 'processed_data/features_mry.csv' containing ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] with generated_ts '2025-02-13T09:05:00Z'; a configuration file at 'processed_data/model_config_mry.json' with a classification_threshold_m of 0.55 and created_ts '2025-02-13T09:06:00Z'; a split summary in 'processed_data/split_mry.json'; a model registered as 'mry_lr_v1' in 'models/mry_lr_v1.joblib'; predictions stored at 'processed_data/preds_mry_lr_v1.csv' with a generated_ts of '2025-02-13T10:30:00Z'; metrics available at 'processed_data/metrics_mry_lr_v1.csv' showing an auc of 0.73; and references for stakeholders to those predictions and metrics.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_mry.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-13T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_mry.json",
                    "classification_threshold_m_nullable": 0.55,
                    "created_ts": "2025-02-13T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_mry.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "mry_lr_v1",
                    "model_path": "models/mry_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "mry_lr_v1",
                    "predictions_csv_path": "processed_data/preds_mry_lr_v1.csv",
                    "generated_ts": "2025-02-13T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "mry_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_mry_lr_v1.csv",
                    "auc_nullable": 0.73
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_mry_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_mry_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_014",
        "instruction": "You are required to archive a Santa Cruz modeling bundle. The final result should consist of: features saved at 'processed_data/features_sc.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and a generated_ts of '2025-02-14T09:05:00Z'; a configuration at 'processed_data/model_config_sc.json' with classification_threshold_m 0.60 and a created_ts of '2025-02-14T09:06:00Z'; a split summary in 'processed_data/split_sc.json'; a model named 'sc_lr_v2' placed in 'models/sc_lr_v2.joblib'; predictions captured at 'processed_data/preds_sc_lr_v2.csv' with a generated_ts of '2025-02-14T10:30:00Z'; metrics recorded at 'processed_data/metrics_sc_lr_v2.csv' with an accuracy of 0.69; and stakeholder references tied to these specific artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_sc.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-14T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_sc.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-02-14T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_sc.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "sc_lr_v2",
                    "model_path": "models/sc_lr_v2.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "sc_lr_v2",
                    "predictions_csv_path": "processed_data/preds_sc_lr_v2.csv",
                    "generated_ts": "2025-02-14T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "sc_lr_v2",
                    "metrics_csv_path": "processed_data/metrics_sc_lr_v2.csv",
                    "accuracy_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_sc_lr_v2.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_sc_lr_v2.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_015",
        "instruction": "Ensure to keep a Pacifica modeling bundle. The final outcome includes: features situated at 'processed_data/features_pac.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-15T09:05:00Z'; configuration located at 'processed_data/model_config_pac.json' with classification_threshold_m 0.58 and created_ts '2025-02-15T09:06:00Z'; split summary stored at 'processed_data/split_pac.json'; model 'pac_rf_v1' at 'models/pac_rf_v1.joblib'; predictions housed at 'processed_data/preds_pac_rf_v1.csv' (generated_ts '2025-02-15T10:30:00Z'); metrics found at 'processed_data/metrics_pac_rf_v1.csv' (auc 0.71); stakeholder references point to those paths.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_pac.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-15T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_pac.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-02-15T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_pac.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "pac_rf_v1",
                    "model_path": "models/pac_rf_v1.joblib",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "pac_rf_v1",
                    "predictions_csv_path": "processed_data/preds_pac_rf_v1.csv",
                    "generated_ts": "2025-02-15T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "pac_rf_v1",
                    "metrics_csv_path": "processed_data/metrics_pac_rf_v1.csv",
                    "auc_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_pac_rf_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_pac_rf_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_016",
        "instruction": "Ensure to catalog a Half Moon Bay modeling bundle. Final state includes: features stored at 'processed_data/features_hmb.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-16T09:05:00Z'; configuration available at 'processed_data/model_config_hmb.json' with classification_threshold_m 0.57 and created_ts '2025-02-16T09:06:00Z'; split summary at 'processed_data/split_hmb.json'; model 'hmb_lr_v1' located at 'models/hmb_lr_v1.joblib'; predictions lodged at 'processed_data/preds_hmb_lr_v1.csv' (generated_ts '2025-02-16T10:30:00Z'); metrics located at 'processed_data/metrics_hmb_lr_v1.csv' (accuracy 0.68); and stakeholder references to those artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_hmb.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-16T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_hmb.json",
                    "classification_threshold_m_nullable": 0.57,
                    "created_ts": "2025-02-16T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_hmb.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "hmb_lr_v1",
                    "model_path": "models/hmb_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "hmb_lr_v1",
                    "predictions_csv_path": "processed_data/preds_hmb_lr_v1.csv",
                    "generated_ts": "2025-02-16T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "hmb_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_hmb_lr_v1.csv",
                    "accuracy_nullable": 0.68
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_hmb_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_hmb_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_017",
        "instruction": "Handle the storage of a Davenport modeling bundle. Final state: features at 'processed_data/features_dvp.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-17T09:05:00Z'; configuration at 'processed_data/model_config_dvp.json' with classification_threshold_m 0.59 and created_ts '2025-02-17T09:06:00Z'; split summary at 'processed_data/split_dvp.json'; model 'dvp_lr_v1' at 'models/dvp_lr_v1.joblib'; predictions at 'processed_data/preds_dvp_lr_v1.csv' (generated_ts '2025-02-17T10:30:00Z'); metrics at 'processed_data/metrics_dvp_lr_v1.csv' (auc 0.72); and stakeholder references pointing to those paths.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_dvp.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-17T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_dvp.json",
                    "classification_threshold_m_nullable": 0.59,
                    "created_ts": "2025-02-17T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_dvp.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "dvp_lr_v1",
                    "model_path": "models/dvp_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "dvp_lr_v1",
                    "predictions_csv_path": "processed_data/preds_dvp_lr_v1.csv",
                    "generated_ts": "2025-02-17T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "dvp_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_dvp_lr_v1.csv",
                    "auc_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_dvp_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_dvp_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_018",
        "instruction": "Coordinate the assembly of a Santa Barbara modeling bundle. Finalized state: features at 'processed_data/features_sb.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-18T09:05:00Z'; configuration at 'processed_data/model_config_sb.json' with classification_threshold_m 0.61 and created_ts '2025-02-18T09:06:00Z'; split summary at 'processed_data/split_sb.json'; model 'sb_lr_v1' at 'models/sb_lr_v1.joblib'; predictions at 'processed_data/preds_sb_lr_v1.csv' (generated_ts '2025-02-18T10:30:00Z'); metrics at 'processed_data/metrics_sb_lr_v1.csv' (accuracy 0.70); and stakeholder references to those paths.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_sb.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-18T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_sb.json",
                    "classification_threshold_m_nullable": 0.61,
                    "created_ts": "2025-02-18T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_sb.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "sb_lr_v1",
                    "model_path": "models/sb_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "sb_lr_v1",
                    "predictions_csv_path": "processed_data/preds_sb_lr_v1.csv",
                    "generated_ts": "2025-02-18T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "sb_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_sb_lr_v1.csv",
                    "accuracy_nullable": 0.7
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_sb_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_sb_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_019",
        "instruction": "Handle the registration of a Ventura modeling bundle. Final state: features located at 'processed_data/features_ven.csv' containing ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-19T09:05:00Z'; configuration found at 'processed_data/model_config_ven.json' with classification_threshold_m 0.62 and created_ts '2025-02-19T09:06:00Z'; include split summary at 'processed_data/split_ven.json'; utilize model 'ven_lr_v1' stored at 'models/ven_lr_v1.joblib'; predictions should be available in 'processed_data/preds_ven_lr_v1.csv' (generated_ts '2025-02-19T10:30:00Z'); metrics located at 'processed_data/metrics_ven_lr_v1.csv' (auc 0.70); and stakeholder references need to be linked to these artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_ven.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-19T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_ven.json",
                    "classification_threshold_m_nullable": 0.62,
                    "created_ts": "2025-02-19T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_ven.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "ven_lr_v1",
                    "model_path": "models/ven_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "ven_lr_v1",
                    "predictions_csv_path": "processed_data/preds_ven_lr_v1.csv",
                    "generated_ts": "2025-02-19T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "ven_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_ven_lr_v1.csv",
                    "auc_nullable": 0.7
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_ven_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_ven_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_020",
        "instruction": "Coordinate the finalization of a Morro Bay modeling bundle. End state: features placed at 'processed_data/features_morro.csv' including ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts '2025-02-20T09:05:00Z'; configuration located at 'processed_data/model_config_morro.json' with classification_threshold_m 0.63 and created_ts '2025-02-20T09:06:00Z'; summary of the split at 'processed_data/split_morro.json'; model 'morro_lr_v1' should be saved at 'models/morro_lr_v1.joblib'; predictions are to be found in 'processed_data/preds_morro_lr_v1.csv' (generated_ts '2025-02-20T10:30:00Z'); metrics stored at 'processed_data/metrics_morro_lr_v1.csv' (accuracy 0.67); ensure stakeholder references connect to these paths.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_morro.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-20T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_morro.json",
                    "classification_threshold_m_nullable": 0.63,
                    "created_ts": "2025-02-20T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_morro.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "morro_lr_v1",
                    "model_path": "models/morro_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "morro_lr_v1",
                    "predictions_csv_path": "processed_data/preds_morro_lr_v1.csv",
                    "generated_ts": "2025-02-20T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "morro_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_morro_lr_v1.csv",
                    "accuracy_nullable": 0.67
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_morro_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_morro_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_021",
        "instruction": "Handle the establishment of an Avila Beach modeling bundle. Final outcome: features stored at 'processed_data/features_avila.csv' including ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] with a generated_ts of '2025-02-21T09:05:00Z'; configuration located at 'processed_data/model_config_avila.json' set with classification_threshold_m 0.56 and a created_ts of '2025-02-21T09:06:00Z'; split summary documented in 'processed_data/split_avila.json'; the model 'avila_lr_v1' placed in 'models/avila_lr_v1.joblib'; predictions found at 'processed_data/preds_avila_lr_v1.csv' (created with generated_ts '2025-02-21T10:30:00Z'); metric data available at 'processed_data/metrics_avila_lr_v1.csv' indicating an auc of 0.74; references for stakeholders directed to those specified paths.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_avila.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-21T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_avila.json",
                    "classification_threshold_m_nullable": 0.56,
                    "created_ts": "2025-02-21T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_avila.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "avila_lr_v1",
                    "model_path": "models/avila_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "avila_lr_v1",
                    "predictions_csv_path": "processed_data/preds_avila_lr_v1.csv",
                    "generated_ts": "2025-02-21T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "avila_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_avila_lr_v1.csv",
                    "auc_nullable": 0.74
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_avila_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_avila_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_022",
        "instruction": "Coordinate the setup of a coastal meta-modeling bundle. Target outcome: features recorded at 'processed_data/features_meta.csv' containing ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] with a generated_ts of '2025-02-22T09:05:00Z'; configuration found in 'processed_data/model_config_meta.json' defined with classification_threshold_m 0.60 and created_ts '2025-02-22T09:06:00Z'; split summary available at 'processed_data/split_meta.json'; model 'coast_meta_v1' positioned at 'models/coast_meta_v1.joblib'; predictions stored at 'processed_data/preds_coast_meta_v1.csv' (created with generated_ts '2025-02-22T10:30:00Z'); metrics are archived at 'processed_data/metrics_coast_meta_v1.csv' capturing an accuracy of 0.71; ensure references point to these predictions/metrics.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_meta.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-02-22T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_meta.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-02-22T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_meta.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "coast_meta_v1",
                    "model_path": "models/coast_meta_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "coast_meta_v1",
                    "predictions_csv_path": "processed_data/preds_coast_meta_v1.csv",
                    "generated_ts": "2025-02-22T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "coast_meta_v1",
                    "metrics_csv_path": "processed_data/metrics_coast_meta_v1.csv",
                    "accuracy_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_coast_meta_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_coast_meta_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_023",
        "instruction": "Register literature for 'storm surge machine learning'. End state: search query 'storm surge machine learning' lists result_item_ids ['ZOT-2001','ZOT-2002'] with search_ts '2025-02-24T12:00:00Z'; metadata titles ['Garcia 2019 Surge ML','Chen 2021 Ensemble Surge'] with fetched_ts '2025-02-24T12:10:00Z'; fulltext paths ['docs/lit/2001.pdf','docs/lit/2002.pdf'] with fetched_ts '2025-02-24T12:12:00Z'; and a manifest at 'docs/lit/manifest_surge.txt' contains 'storm surge ML references'.",
        "actions": [
            {
                "name": "ZoteroSearchItems",
                "arguments": {
                    "query": "storm surge machine learning",
                    "result_item_ids": [
                        "ZOT-2001",
                        "ZOT-2002"
                    ],
                    "search_ts": "2025-02-24T12:00:00Z"
                },
            },
            {
                "name": "ZoteroItemMetadata",
                "arguments": {
                    "item_ids": [
                        "ZOT-2001",
                        "ZOT-2002"
                    ],
                    "titles": [
                        "Garcia 2019 Surge ML",
                        "Chen 2021 Ensemble Surge"
                    ],
                    "fetched_ts": "2025-02-24T12:10:00Z"
                },
            },
            {
                "name": "ZoteroItemFulltext",
                "arguments": {
                    "item_ids": [
                        "ZOT-2001",
                        "ZOT-2002"
                    ],
                    "file_paths": [
                        "docs/lit/2001.pdf",
                        "docs/lit/2002.pdf"
                    ],
                    "fetched_ts": "2025-02-24T12:12:00Z"
                },
            },
            {
                "name": "WriteFileText",
                "arguments": {
                    "path": "docs/lit/manifest_surge.txt",
                    "content": "storm surge ML references"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_024",
        "instruction": "Record literature for 'sensor fusion coastal buoys'. End state: a search record with query 'sensor fusion coastal buoys' lists ['ZOT-4001','ZOT-4003'] and search_ts '2025-02-26T12:00:00Z'; metadata has titles ['Diaz 2021 Multi\u2011Sensor Buoys','Singh 2024 Fusion at Sea'] with fetched_ts '2025-02-26T12:10:00Z'; fulltext paths are ['docs/lit/4001.pdf','docs/lit/4003.pdf'] with fetched_ts '2025-02-26T12:12:00Z'; and a manifest 'docs/lit/manifest_sensors.txt' contains 'sensor fusion buoy references'.",
        "actions": [
            {
                "name": "ZoteroSearchItems",
                "arguments": {
                    "query": "sensor fusion coastal buoys",
                    "result_item_ids": [
                        "ZOT-4001",
                        "ZOT-4003"
                    ],
                    "search_ts": "2025-02-26T12:00:00Z"
                },
            },
            {
                "name": "ZoteroItemMetadata",
                "arguments": {
                    "item_ids": [
                        "ZOT-4001",
                        "ZOT-4003"
                    ],
                    "titles": [
                        "Diaz 2021 Multi‑Sensor Buoys",
                        "Singh 2024 Fusion at Sea"
                    ],
                    "fetched_ts": "2025-02-26T12:10:00Z"
                },
            },
            {
                "name": "ZoteroItemFulltext",
                "arguments": {
                    "item_ids": [
                        "ZOT-4001",
                        "ZOT-4003"
                    ],
                    "file_paths": [
                        "docs/lit/4001.pdf",
                        "docs/lit/4003.pdf"
                    ],
                    "fetched_ts": "2025-02-26T12:12:00Z"
                },
            },
            {
                "name": "WriteFileText",
                "arguments": {
                    "path": "docs/lit/manifest_sensors.txt",
                    "content": "sensor fusion buoy references"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_025",
        "instruction": "Ensure the database is left in a reproducible Crescent City baseline. By the conclusion: a configuration row must display target_city 'Crescent City' with timezone 'UTC'; a geocoding entry should locate 'Crescent City' at 41.7558,-124.2017; a proximity result at the specified coordinates must include station '9419750', which you designate as the primary; observed water levels for '9419750' should incorporate the point '2025-03-01T00:00:00Z' = 1.02 (m); tide predictions for '9419750' must feature the point '2025-03-01T00:00:00Z' = 1.08 (m); and a processed artifact should exist at 'processed_data/merged_timeseries_cc.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Crescent City",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Crescent City",
                    "latitude": 41.7558,
                    "longitude": -124.2017
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 41.7558,
                    "query_longitude": -124.2017,
                    "station_ids": [
                        "9419750"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9419750"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9419750",
                    "timestamps": [
                        "2025-03-01T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9419750",
                    "timestamps": [
                        "2025-03-01T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.08
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_cc.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_026",
        "instruction": "Establish a Point Reyes intake baseline. The final state requires: configuration to display target_city 'Point Reyes' (timezone 'UTC'); geocoding must place 'Point Reyes' at 38.0690,-122.8100; a proximity record at that location must include station '9415020', which you set as primary; observed water levels for '9415020' should contain '2025-03-03T06:00:00Z' = 1.11 (m); tide predictions for '9415020' must include '2025-03-03T06:00:00Z' = 1.16 (m); and ensure a processed artifact resides at 'processed_data/merged_timeseries_pointreyes.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Point Reyes",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Point Reyes",
                    "latitude": 38.069,
                    "longitude": -122.81
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.069,
                    "query_longitude": -122.81,
                    "station_ids": [
                        "9415020"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9415020"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9415020",
                    "timestamps": [
                        "2025-03-03T06:00:00Z"
                    ],
                    "water_level_m": [
                        1.11
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9415020",
                    "timestamps": [
                        "2025-03-03T06:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.16
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_pointreyes.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_027",
        "instruction": "Ensure to store a San Mateo intake baseline. Final result: the configuration lists target_city 'San Mateo' with timezone 'UTC'; geocoding identifies 'San Mateo' at 37.5629,-122.3255; ensure a proximity result includes '9414521', marked as primary; observed water levels for '9414521' include '2025-03-04T07:00:00Z' = 0.99 (m); tide predictions for '9414521' cover '2025-03-04T07:00:00Z' = 1.05 (m); and address a processed artifact at 'processed_data/merged_timeseries_sanmateo.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "San Mateo",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "San Mateo",
                    "latitude": 37.5629,
                    "longitude": -122.3255
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.5629,
                    "query_longitude": -122.3255,
                    "station_ids": [
                        "9414521"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414521"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414521",
                    "timestamps": [
                        "2025-03-04T07:00:00Z"
                    ],
                    "water_level_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414521",
                    "timestamps": [
                        "2025-03-04T07:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sanmateo.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_028",
        "instruction": "Register a Santa Monica intake. Upon completion: the configuration displays target_city 'Santa Monica' (timezone 'UTC'); geocoding places 'Santa Monica' at 34.0195,-118.4912; include in the proximity record '9410840', setting it as primary; observed water levels for '9410840' cover '2025-03-05T12:00:00Z' = 1.07 (m); tide predictions incorporate '2025-03-05T12:00:00Z' = 1.15 (m); and a processed artifact located at 'processed_data/merged_timeseries_sm.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Santa Monica",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Santa Monica",
                    "latitude": 34.0195,
                    "longitude": -118.4912
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.0195,
                    "query_longitude": -118.4912,
                    "station_ids": [
                        "9410840"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410840"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410840",
                    "timestamps": [
                        "2025-03-05T12:00:00Z"
                    ],
                    "water_level_m": [
                        1.07
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410840",
                    "timestamps": [
                        "2025-03-05T12:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.15
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sm.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_029",
        "instruction": "Handle the assembly of a Sacramento modeling bundle. Desired output: features located at 'processed_data/features_sd.csv' including ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-13T09:05:00Z'); a model configuration at 'processed_data/model_config_sd.json' with a classification_threshold_m of 0.58 (created_ts '2025-03-13T09:06:00Z'); a summary of splits at 'processed_data/split_sd.json'; model 'sd_lr_v1' saved at 'models/sd_lr_v1.joblib'; predictions saved at 'processed_data/preds_sd_lr_v1.csv' (generated_ts '2025-03-13T10:30:00Z'); metrics saved at 'processed_data/metrics_sd_lr_v1.csv' (auc 0.72); along with stakeholder references aligning with those predictions and metrics.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_sd.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-13T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_sd.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-03-13T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_sd.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "sd_lr_v1",
                    "model_path": "models/sd_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "sd_lr_v1",
                    "predictions_csv_path": "processed_data/preds_sd_lr_v1.csv",
                    "generated_ts": "2025-03-13T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "sd_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_sd_lr_v1.csv",
                    "auc_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_sd_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_sd_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_030",
        "instruction": "Handle the storage of a Sacramento modeling bundle. Expected outcome: features located at 'processed_data/features_la.csv' including ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-13T11:05:00Z'); a configuration at 'processed_data/model_config_la.json' with a classification_threshold_m of 0.62 (created_ts '2025-03-13T11:06:00Z'); summary of splits saved at 'processed_data/split_la.json'; model 'la_rf_v1' (type 'random_forest') stored at 'models/la_rf_v1.joblib'; predictions stored at 'processed_data/preds_la_rf_v1.csv' (generated_ts '2025-03-13T12:30:00Z'); metrics saved at 'processed_data/metrics_la_rf_v1.csv' (accuracy 0.71); along with stakeholder references for those artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_la.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-13T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_la.json",
                    "classification_threshold_m_nullable": 0.62,
                    "created_ts": "2025-03-13T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_la.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "la_rf_v1",
                    "model_path": "models/la_rf_v1.joblib",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "la_rf_v1",
                    "predictions_csv_path": "processed_data/preds_la_rf_v1.csv",
                    "generated_ts": "2025-03-13T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "la_rf_v1",
                    "metrics_csv_path": "processed_data/metrics_la_rf_v1.csv",
                    "accuracy_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_la_rf_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_la_rf_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_031",
        "instruction": "Ensure a Sacramento intake baseline is captured. Final configuration should display target_city 'Sacramento' (UTC); geocoding should locate 'Sacramento' at 32.7157,-117.1611; a proximity result at those coordinates must include '9410170' which you designate as primary; observed water levels for '9410170' are to include '2025-03-15T00:00:00Z' = 0.98 (m); tide predictions must list '2025-03-15T00:00:00Z' = 1.05 (m); and a processed artifact should be available at 'processed_data/merged_timeseries_sd.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Sacramento",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Sacramento",
                    "latitude": 32.7157,
                    "longitude": -117.1611
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 32.7157,
                    "query_longitude": -117.1611,
                    "station_ids": [
                        "9410170"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410170"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410170",
                    "timestamps": [
                        "2025-03-15T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.98
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410170",
                    "timestamps": [
                        "2025-03-15T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sd.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_032",
        "instruction": "Make sure to record a La Jolla intake baseline. The configuration at completion should show target_city 'La Jolla' (UTC); geocoding must situate 'La Jolla' at 32.8328,-117.2713; a proximity record must list station '9410230' as primary; observed water levels for '9410230' should include '2025-03-16T01:00:00Z' = 1.01 (m); tide predictions must include '2025-03-16T01:00:00Z' = 1.09 (m); and a processed artifact should be located at 'processed_data/merged_timeseries_lajolla.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "La Jolla",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "La Jolla",
                    "latitude": 32.8328,
                    "longitude": -117.2713
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 32.8328,
                    "query_longitude": -117.2713,
                    "station_ids": [
                        "9410230"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410230"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410230",
                    "timestamps": [
                        "2025-03-16T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410230",
                    "timestamps": [
                        "2025-03-16T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_lajolla.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_033",
        "instruction": "Log a compact anomaly check for station '9413830'. The final outcome: an anomaly metrics row, derived from water_level_series [1.3,1.4,1.5] and tide_prediction_series [1.2,1.3,1.4], is saved at 'processed_data/anomaly_9413830_20250318.csv' (generated_ts '2025-03-18T09:00:00Z'); a QC figure is documented at 'figures/qc/anomaly_9413830.png'; and the terminal log reads 'QC: anomaly complete'.",
        "actions": [
            {
                "name": "ComputeTideAnomalySummary",
                "arguments": {
                    "station_id": "9413830",
                    "water_level_series": [
                        1.3,
                        1.4,
                        1.5
                    ],
                    "tide_prediction_series": [
                        1.2,
                        1.3,
                        1.4
                    ],
                    "metrics_csv_path": "processed_data/anomaly_9413830_20250318.csv",
                    "generated_ts": "2025-03-18T09:00:00Z"
                },
            },
            {
                "name": "RegisterQcFigure",
                "arguments": {
                    "figure_path": "figures/qc/anomaly_9413830.png",
                    "description": "Max abs anomaly for 9413830"
                },
            },
            {
                "name": "AppendTerminalLog",
                "arguments": {
                    "command": "qc_anomaly:9413830",
                    "printed_message": "QC: anomaly complete"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_034",
        "instruction": "Publish release notes for the coastal model bundle (2025-03-19). The completed state includes: page 'PAGE-20250319-REL' named 'Coastal Model Release - 2025-03-19' is present (created_ts '2025-03-19T09:00:00Z'); sections ['Release Notes','Changelog','Artifacts'] are included (updated_ts '2025-03-19T09:05:00Z'); properties JSON is assigned to '{\"model\":\"models/coast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_coast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_coast_meta_v1.csv\"}' (updated_ts '2025-03-19T09:10:00Z'); and an email to ['team@coastallab.org'] is dispatched as 'MSG-20250319-REL' (draft '2025-03-19T09:20:00Z', sent '2025-03-19T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250319-REL",
                    "title": "Coastal Model Release - 2025-03-19",
                    "created_ts": "2025-03-19T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250319-REL",
                    "sections": [
                        "Release Notes",
                        "Changelog",
                        "Artifacts"
                    ],
                    "updated_ts": "2025-03-19T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250319-REL",
                    "properties_json": "{\"model\":\"models/coast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_coast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_coast_meta_v1.csv\"}",
                    "updated_ts": "2025-03-19T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250319-REL",
                    "subject": "Coastal Model Release - 2025-03-19",
                    "recipients": [
                        "team@coastallab.org"
                    ],
                    "created_ts": "2025-03-19T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250319-REL",
                    "message_id": "MSG-20250319-REL",
                    "sent_ts": "2025-03-19T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_035",
        "instruction": "Handle the compilation of a Crescent City modeling bundle. Final outcome: features located at 'processed_data/features_cc.csv' including ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-21T09:05:00Z'); with configuration file at 'processed_data/model_config_cc.json' featuring classification_threshold_m 0.57 (created_ts '2025-03-21T09:06:00Z'); split information can be found at 'processed_data/split_cc.json'; the model 'cc_lr_v1' situated at 'models/cc_lr_v1.joblib'; predictions stored at 'processed_data/preds_cc_lr_v1.csv' (generated_ts '2025-03-21T10:30:00Z'); metrics available at 'processed_data/metrics_cc_lr_v1.csv' (accuracy 0.66); plus ensure stakeholder references to these elements.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_cc.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-21T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_cc.json",
                    "classification_threshold_m_nullable": 0.57,
                    "created_ts": "2025-03-21T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_cc.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "cc_lr_v1",
                    "model_path": "models/cc_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "cc_lr_v1",
                    "predictions_csv_path": "processed_data/preds_cc_lr_v1.csv",
                    "generated_ts": "2025-03-21T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "cc_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_cc_lr_v1.csv",
                    "accuracy_nullable": 0.66
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_cc_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_cc_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_036",
        "instruction": "Coordinate the assembly of an Eureka modeling bundle. Desired result: features accessible at 'processed_data/features_eureka.csv' involving ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-21T11:05:00Z'); configuration file found at 'processed_data/model_config_eureka.json' with classification_threshold_m 0.59 (created_ts '2025-03-21T11:06:00Z'); split details located at 'processed_data/split_eureka.json'; model 'eureka_lr_v1' residing at 'models/eureka_lr_v1.joblib'; prediction outputs at 'processed_data/preds_eureka_lr_v1.csv' (generated_ts '2025-03-21T12:30:00Z'); metrics can be reviewed at 'processed_data/metrics_eureka_lr_v1.csv' (auc 0.69); and ensure stakeholder references to these directories.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_eureka.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-21T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_eureka.json",
                    "classification_threshold_m_nullable": 0.59,
                    "created_ts": "2025-03-21T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_eureka.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "eureka_lr_v1",
                    "model_path": "models/eureka_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "eureka_lr_v1",
                    "predictions_csv_path": "processed_data/preds_eureka_lr_v1.csv",
                    "generated_ts": "2025-03-21T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "eureka_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_eureka_lr_v1.csv",
                    "auc_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_eureka_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_eureka_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_037",
        "instruction": "Handle the assembly of a Capitola modeling bundle. End state: features at 'processed_data/features_cap.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-22T11:05:00Z'); ensure the config is in 'processed_data/model_config_cap.json' with classification_threshold_m 0.58 (created_ts '2025-03-22T11:06:00Z'); split recorded at 'processed_data/split_cap.json'; model 'cap_lr_v1' stored at 'models/cap_lr_v1.joblib'; predictions filed at 'processed_data/preds_cap_lr_v1.csv' (generated_ts '2025-03-22T12:30:00Z'); metrics recorded in 'processed_data/metrics_cap_lr_v1.csv' (accuracy 0.68); ensuring stakeholders have references to these artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_cap.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-22T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_cap.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-03-22T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_cap.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "cap_lr_v1",
                    "model_path": "models/cap_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "cap_lr_v1",
                    "predictions_csv_path": "processed_data/preds_cap_lr_v1.csv",
                    "generated_ts": "2025-03-22T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "cap_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_cap_lr_v1.csv",
                    "accuracy_nullable": 0.68
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_cap_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_cap_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_038",
        "instruction": "Coordinate the registration of an experimental feature set along with a split plan. End state: features located at 'processed_data/features_experimental.csv' with ['precip_6h_mm','surge_12h_max_m','pressure_trend_12h_hpa'] (generated_ts '2025-03-25T09:05:00Z'); a config saved at 'processed_data/model_config_experimental.json' with test_split_fraction 0.25 (created_ts '2025-03-25T09:06:00Z'); and document a split summary in 'processed_data/split_experimental.json' with test_fraction 0.25 and counts 750/250 (split_ts '2025-03-25T09:07:00Z').",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_experimental.csv",
                    "feature_names": [
                        "precip_6h_mm",
                        "surge_12h_max_m",
                        "pressure_trend_12h_hpa"
                    ],
                    "generated_ts": "2025-03-25T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_experimental.json",
                    "test_split_fraction_nullable": 0.25,
                    "created_ts": "2025-03-25T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_experimental.json",
                    "test_fraction": 0.25,
                    "train_index_count": 750,
                    "test_index_count": 250,
                    "split_ts": "2025-03-25T09:07:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_039",
        "instruction": "Generate a Pacifica high\u2011tide briefing (2025-03-25). Final goal: a page 'PAGE-20250325-HT1' titled 'Pacifica High Tide - 2025-03-25' is in place (created_ts '2025-03-25T09:00:00Z'); sections ['Summary','Drivers','Next Steps'] are included (updated_ts '2025-03-25T09:05:00Z'); properties JSON matches '{\"predictions\":\"processed_data/preds_pac_rf_v1.csv\",\"metrics\":\"processed_data/metrics_pac_rf_v1.csv\",\"figure\":\"figures/qc/pac_high_tide.png\"}' (updated_ts '2025-03-25T09:10:00Z'); and an email to ['ops@pacifica.ca.us'] is dispatched as 'MSG-20250325-HT1' (draft '2025-03-25T09:20:00Z', sent '2025-03-25T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250325-HT1",
                    "title": "Pacifica High Tide - 2025-03-25",
                    "created_ts": "2025-03-25T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250325-HT1",
                    "sections": [
                        "Summary",
                        "Drivers",
                        "Next Steps"
                    ],
                    "updated_ts": "2025-03-25T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250325-HT1",
                    "properties_json": "{\"predictions\":\"processed_data/preds_pac_rf_v1.csv\",\"metrics\":\"processed_data/metrics_pac_rf_v1.csv\",\"figure\":\"figures/qc/pac_high_tide.png\"}",
                    "updated_ts": "2025-03-25T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250325-HT1",
                    "subject": "Pacifica High Tide Briefing - 2025-03-25",
                    "recipients": [
                        "ops@pacifica.ca.us"
                    ],
                    "created_ts": "2025-03-25T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250325-HT1",
                    "message_id": "MSG-20250325-HT1",
                    "sent_ts": "2025-03-25T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_040",
        "instruction": "Record a Redwood City micro\u2011run. Completion state: configuration displays target_city 'Redwood City' (UTC); geocoding establishes 37.4852,-122.2364 (canonical 'Redwood City, California'); a proximity record lists '9414523' and you mark it primary; recorded water levels for '9414523' add '2025-03-28T06:00:00Z' = 1.00 (m); tide predictions comprise '2025-03-28T06:00:00Z' = 1.06 (m); and a processed artifact is available at 'processed_data/merged_timeseries_rwc.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Redwood City",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Redwood City",
                    "latitude": 37.4852,
                    "longitude": -122.2364,
                    "canonical_name": "Redwood City, California"
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.4852,
                    "query_longitude": -122.2364,
                    "station_ids": [
                        "9414523"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414523"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414523",
                    "timestamps": [
                        "2025-03-28T06:00:00Z"
                    ],
                    "water_level_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414523",
                    "timestamps": [
                        "2025-03-28T06:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.06
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_rwc.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_041",
        "instruction": "Handle capturing a Long Beach intake baseline. Final outcome: configuration should reflect target_city 'Long Beach' (UTC); geocoding positions 'Long Beach' at 33.7701,-118.1937; ensure a proximity record there contains '9410669', and set it as primary; observed water levels for '9410669' should include '2025-03-01T03:00:00Z' = 0.97 (m); tide predictions must include '2025-03-01T03:00:00Z' = 1.02 (m); and ensure a processed artifact is available at 'processed_data/merged_timeseries_longbeach.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Long Beach",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Long Beach",
                    "latitude": 33.7701,
                    "longitude": -118.1937
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.7701,
                    "query_longitude": -118.1937,
                    "station_ids": [
                        "9410669"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410669"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410669",
                    "timestamps": [
                        "2025-03-01T03:00:00Z"
                    ],
                    "water_level_m": [
                        0.97
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410669",
                    "timestamps": [
                        "2025-03-01T03:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_longbeach.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_042",
        "instruction": "Coordinate registering a Bodega Bay intake baseline. Desired state: configuration should list target_city 'Bodega Bay' (UTC); geocoding places 'Bodega Bay' at 38.3337,-123.0486; ensure a proximity record includes station '9416841' set as primary; observed water levels should feature '2025-03-02T01:00:00Z' = 1.12 (m); tide predictions must contain '2025-03-02T01:00:00Z' = 1.18 (m); and confirm a processed artifact exists at 'processed_data/merged_timeseries_bodega.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Bodega Bay",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Bodega Bay",
                    "latitude": 38.3337,
                    "longitude": -123.0486
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.3337,
                    "query_longitude": -123.0486,
                    "station_ids": [
                        "9416841"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9416841"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9416841",
                    "timestamps": [
                        "2025-03-02T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.12
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9416841",
                    "timestamps": [
                        "2025-03-02T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.18
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_bodega.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_043",
        "instruction": "Ensure you capture a Point Arena intake baseline. End state: the configuration must display target_city 'Point Arena' (UTC); geocoding should locate 'Point Arena' at 38.9086,-123.7083; a proximity record must include '9416845' set as primary; observed water levels for '9416845' should include '2025-03-03T01:00:00Z' = 1.06 (m); tide predictions must include '2025-03-03T01:00:00Z' = 1.13 (m); and a processed artifact is located at 'processed_data/merged_timeseries_pointarena.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Point Arena",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Point Arena",
                    "latitude": 38.9086,
                    "longitude": -123.7083
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.9086,
                    "query_longitude": -123.7083,
                    "station_ids": [
                        "9416845"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9416845"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9416845",
                    "timestamps": [
                        "2025-03-03T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.06
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9416845",
                    "timestamps": [
                        "2025-03-03T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.13
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_pointarena.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_044",
        "instruction": "Ensure storage of a Fort Bragg intake baseline. End state: the configuration must show target_city 'Fort Bragg' (UTC); geocoding should anchor 39.4450,-123.8050; a proximity record must include '9416849' which is set as primary; observed water levels should include '2025-03-03T02:00:00Z' = 1.09 (m); tide predictions must include '2025-03-03T02:00:00Z' = 1.16 (m); and a processed artifact should exist at 'processed_data/merged_timeseries_fortbragg.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Fort Bragg",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Fort Bragg",
                    "latitude": 39.445,
                    "longitude": -123.805
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 39.445,
                    "query_longitude": -123.805,
                    "station_ids": [
                        "9416849"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9416849"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9416849",
                    "timestamps": [
                        "2025-03-03T02:00:00Z"
                    ],
                    "water_level_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9416849",
                    "timestamps": [
                        "2025-03-03T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.16
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_fortbragg.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_045",
        "instruction": "Ensure to document a San Pedro intake baseline. Final condition: the configuration displays target_city 'San Pedro' (UTC); geocoding places 33.7358,-118.2923; a proximity entry at those coordinates contains '9410660' which you designate as primary; observed water levels list '2025-03-04T00:00:00Z' = 0.95 (m); tide predictions state '2025-03-04T00:00:00Z' = 1.01 (m); and a processed artifact is located at 'processed_data/merged_timeseries_sanpedro.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "San Pedro",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "San Pedro",
                    "latitude": 33.7358,
                    "longitude": -118.2923
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.7358,
                    "query_longitude": -118.2923,
                    "station_ids": [
                        "9410660"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410660"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410660",
                    "timestamps": [
                        "2025-03-04T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.95
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410660",
                    "timestamps": [
                        "2025-03-04T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sanpedro.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_046",
        "instruction": "Ensure to record a Huntington Beach intake baseline. Conclusion state: configuration records target_city 'Huntington Beach' (UTC); geocoding fixes 33.6595,-117.9988; a proximity record holds '9410647' marked primary; observed water levels mention '2025-03-04T01:00:00Z' = 1.00 (m); tide predictions specify '2025-03-04T01:00:00Z' = 1.08 (m); and a merged artifact resides at 'processed_data/merged_timeseries_hb.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Huntington Beach",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Huntington Beach",
                    "latitude": 33.6595,
                    "longitude": -117.9988
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.6595,
                    "query_longitude": -117.9988,
                    "station_ids": [
                        "9410647"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410647"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410647",
                    "timestamps": [
                        "2025-03-04T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410647",
                    "timestamps": [
                        "2025-03-04T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.08
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_hb.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_047",
        "instruction": "Ensure the assembly of an Oceanside modeling bundle. Final outcome: have features at 'processed_data/features_oce.csv' using ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-05T09:05:00Z'); model configuration located at 'processed_data/model_config_oce.json' with classification_threshold_m 0.59 (created_ts '2025-03-05T09:06:00Z'); a summary of the split at 'processed_data/split_oce.json'; the model 'oce_lr_v1' stored at 'models/oce_lr_v1.joblib'; predictions to be found at 'processed_data/preds_oce_lr_v1.csv' (generated_ts '2025-03-05T10:30:00Z'); measurement data at 'processed_data/metrics_oce_lr_v1.csv' (auc 0.70); along with stakeholder references directed to these same artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_oce.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-05T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_oce.json",
                    "classification_threshold_m_nullable": 0.59,
                    "created_ts": "2025-03-05T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_oce.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "oce_lr_v1",
                    "model_path": "models/oce_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "oce_lr_v1",
                    "predictions_csv_path": "processed_data/preds_oce_lr_v1.csv",
                    "generated_ts": "2025-03-05T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "oce_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_oce_lr_v1.csv",
                    "auc_nullable": 0.7
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_oce_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_oce_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_048",
        "instruction": "Facilitate the storage of a Long Beach modeling bundle. Final result: ensure features at 'processed_data/features_lb.csv' using ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-05T11:05:00Z'); model configuration at 'processed_data/model_config_lb.json' with classification_threshold_m 0.61 (created_ts '2025-03-05T11:06:00Z'); a split summary located at 'processed_data/split_lb.json'; the model 'lb_lr_v1' accessible at 'models/lb_lr_v1.joblib'; predictions recorded at 'processed_data/preds_lb_lr_v1.csv' (generated_ts '2025-03-05T12:30:00Z'); metrics recorded in 'processed_data/metrics_lb_lr_v1.csv' (accuracy 0.69); along with stakeholder references linked to these artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_lb.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-05T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_lb.json",
                    "classification_threshold_m_nullable": 0.61,
                    "created_ts": "2025-03-05T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_lb.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "lb_lr_v1",
                    "model_path": "models/lb_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "lb_lr_v1",
                    "predictions_csv_path": "processed_data/preds_lb_lr_v1.csv",
                    "generated_ts": "2025-03-05T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "lb_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_lb_lr_v1.csv",
                    "accuracy_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_lb_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_lb_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_049",
        "instruction": "Assemble a Newport Beach modeling bundle. Final result: features located at 'processed_data/features_newport.csv' include ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-06T09:05:00Z'); configuration in 'processed_data/model_config_newport.json' with classification_threshold_m 0.58 (created_ts '2025-03-06T09:06:00Z'); split file at 'processed_data/split_newport.json'; model 'newport_rf_v1' (type 'random_forest') found in 'models/newport_rf_v1.joblib'; predictions detailed in 'processed_data/preds_newport_rf_v1.csv' (generated_ts '2025-03-06T10:30:00Z'); metrics available at 'processed_data/metrics_newport_rf_v1.csv' (auc 0.71); and stakeholder references provided.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_newport.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-06T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_newport.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-03-06T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_newport.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "newport_rf_v1",
                    "model_path": "models/newport_rf_v1.joblib",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "newport_rf_v1",
                    "predictions_csv_path": "processed_data/preds_newport_rf_v1.csv",
                    "generated_ts": "2025-03-06T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "newport_rf_v1",
                    "metrics_csv_path": "processed_data/metrics_newport_rf_v1.csv",
                    "auc_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_newport_rf_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_newport_rf_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_050",
        "instruction": "Compile a Bodega Bay modeling bundle. Final result: features found at 'processed_data/features_bodega.csv' (generated_ts '2025-03-06T11:05:00Z'); configuration in 'processed_data/model_config_bodega.json' with classification_threshold_m 0.60 (created_ts '2025-03-06T11:06:00Z'); split file at 'processed_data/split_bodega.json'; model 'bodega_lr_v1' located at 'models/bodega_lr_v1.joblib'; predictions recorded in 'processed_data/preds_bodega_lr_v1.csv' (generated_ts '2025-03-06T12:30:00Z'); metrics available at 'processed_data/metrics_bodega_lr_v1.csv' (accuracy 0.67); along with stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_bodega.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-06T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_bodega.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-03-06T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_bodega.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "model_path": "models/bodega_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "predictions_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                    "generated_ts": "2025-03-06T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_bodega_lr_v1.csv",
                    "accuracy_nullable": 0.67
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_bodega_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_051",
        "instruction": "Handle the registration of a Point Arena modeling bundle. End state: features must be available at 'processed_data/features_pa.csv' (generated_ts '2025-03-07T09:05:00Z'); configure file at 'processed_data/model_config_pa.json' with classification_threshold_m 0.62 (created_ts '2025-03-07T09:06:00Z'); split details to be at 'processed_data/split_pa.json'; store the model 'pa_lr_v1' at 'models/pa_lr_v1.joblib'; ensure predictions appear at 'processed_data/preds_pa_lr_v1.csv' (generated_ts '2025-03-07T10:30:00Z'); metrics should be logged at 'processed_data/metrics_pa_lr_v1.csv' (auc 0.69); and compile stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_pa.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-07T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_pa.json",
                    "classification_threshold_m_nullable": 0.62,
                    "created_ts": "2025-03-07T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_pa.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "pa_lr_v1",
                    "model_path": "models/pa_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "pa_lr_v1",
                    "predictions_csv_path": "processed_data/preds_pa_lr_v1.csv",
                    "generated_ts": "2025-03-07T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "pa_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_pa_lr_v1.csv",
                    "auc_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_pa_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_pa_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_052",
        "instruction": "Coordinate the preparation of stakeholder-facing material for Santa Monica (2025-03-07). End state: ensure a page 'PAGE-20250307-SM' titled 'Santa Monica Flood Risk - 2025-03-07' is present (created_ts '2025-03-07T09:00:00Z'); sections ['Summary','Drivers','Actions'] must be included (updated_ts '2025-03-07T09:05:00Z'); properties match the exact JSON '{\"predictions\":\"processed_data/preds_sm_v1.csv\",\"metrics\":\"processed_data/metrics_sm_v1.csv\",\"figure\":\"figures/qc/sm_overview.png\"}' (updated_ts '2025-03-07T09:10:00Z'); and finalize an email draft 'DRAFT-20250307-SM' to ['ops@santamonica.gov'] to be sent as 'MSG-20250307-SM' (draft '2025-03-07T09:20:00Z', sent '2025-03-07T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250307-SM",
                    "title": "Santa Monica Flood Risk - 2025-03-07",
                    "created_ts": "2025-03-07T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250307-SM",
                    "sections": [
                        "Summary",
                        "Drivers",
                        "Actions"
                    ],
                    "updated_ts": "2025-03-07T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250307-SM",
                    "properties_json": "{\"predictions\":\"processed_data/preds_sm_v1.csv\",\"metrics\":\"processed_data/metrics_sm_v1.csv\",\"figure\":\"figures/qc/sm_overview.png\"}",
                    "updated_ts": "2025-03-07T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250307-SM",
                    "subject": "Santa Monica Flood Risk - 2025-03-07",
                    "recipients": [
                        "ops@santamonica.gov"
                    ],
                    "attachments_paths": [
                        "figures/qc/sm_overview.png"
                    ],
                    "created_ts": "2025-03-07T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250307-SM",
                    "message_id": "MSG-20250307-SM",
                    "sent_ts": "2025-03-07T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_053",
        "instruction": "Handle packaging of stakeholder reporting for Sacramento Outer Harbor (2025-03-08). Outcome: page 'PAGE-20250308-LAOH' with the title 'LA Outer Harbor Flood Risk - 2025-03-08' is created (created_ts '2025-03-08T09:00:00Z'); sections ['Summary','Risks','Recommendations'] are included (updated_ts '2025-03-08T09:05:00Z'); properties precisely contain the JSON '{\"predictions\":\"processed_data/preds_laoh_v1.csv\",\"metrics\":\"processed_data/metrics_laoh_v1.csv\",\"artifacts\":\"artifacts/laoh_20250308.zip\"}' (updated_ts '2025-03-08T09:10:00Z'); and draft 'DRAFT-20250308-LAOH' emailed to ['harbor@lacity.org'] is sent as 'MSG-20250308-LAOH' with the artifact attached (draft '2025-03-08T09:20:00Z', sent '2025-03-08T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250308-LAOH",
                    "title": "LA Outer Harbor Flood Risk - 2025-03-08",
                    "created_ts": "2025-03-08T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250308-LAOH",
                    "sections": [
                        "Summary",
                        "Risks",
                        "Recommendations"
                    ],
                    "updated_ts": "2025-03-08T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250308-LAOH",
                    "properties_json": "{\"predictions\":\"processed_data/preds_laoh_v1.csv\",\"metrics\":\"processed_data/metrics_laoh_v1.csv\",\"artifacts\":\"artifacts/laoh_20250308.zip\"}",
                    "updated_ts": "2025-03-08T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250308-LAOH",
                    "subject": "LA Outer Harbor Flood Risk - 2025-03-08",
                    "recipients": [
                        "harbor@lacity.org"
                    ],
                    "attachments_paths": [
                        "artifacts/laoh_20250308.zip"
                    ],
                    "created_ts": "2025-03-08T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250308-LAOH",
                    "message_id": "MSG-20250308-LAOH",
                    "sent_ts": "2025-03-08T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_054",
        "instruction": "Coordinate the assembly of a Newport (OR) modeling bundle. Completion: features 'processed_data/features_newportor.csv' (generated_ts '2025-05-09T11:05:00Z'); configuration 'processed_data/model_config_newportor.json' with classification_threshold_m 0.59 (created_ts '2025-05-09T11:06:00Z'); dataset split 'processed_data/split_newportor.json'; model 'newportor_lr_v1' located at 'models/newportor_lr_v1.joblib'; predictions 'processed_data/preds_newportor_lr_v1.csv' (generated_ts '2025-05-09T12:30:00Z'); metrics 'processed_data/metrics_newportor_lr_v1.csv' (accuracy 0.69); stakeholder references are handled.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_newportor.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-05-09T11:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_newportor.json",
                    "classification_threshold_m_nullable": 0.59,
                    "created_ts": "2025-05-09T11:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_newportor.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "newportor_lr_v1",
                    "model_path": "models/newportor_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "newportor_lr_v1",
                    "predictions_csv_path": "processed_data/preds_newportor_lr_v1.csv",
                    "generated_ts": "2025-05-09T12:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "newportor_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_newportor_lr_v1.csv",
                    "accuracy_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_newportor_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_newportor_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_055",
        "instruction": "Handle the recording of a Sausalito intake baseline. Desired outcome: configuration indicates target_city 'Sausalito' (UTC); geocoding anchors 37.8591,-122.4853; a proximity record contains '9414291' set as primary; observed water levels feature '2025-03-13T00:00:00Z' = 1.03 (m); tide predictions involve '2025-03-13T00:00:00Z' = 1.10 (m); and a processed artifact located at 'processed_data/merged_timeseries_sausalito.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Sausalito",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Sausalito",
                    "latitude": 37.8591,
                    "longitude": -122.4853
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.8591,
                    "query_longitude": -122.4853,
                    "station_ids": [
                        "9414291"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414291"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414291",
                    "timestamps": [
                        "2025-03-13T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414291",
                    "timestamps": [
                        "2025-03-13T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.1
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sausalito.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_056",
        "instruction": "Coordinate the capture of a Foster City intake baseline. Desired outcome: configuration lists target_city 'Foster City' (UTC); geocoding identifies 37.5585,-122.2711; a proximity result includes '9414524' designated as primary; observed water levels incorporate '2025-03-13T01:00:00Z' = 0.98 (m); tide predictions involve '2025-03-13T01:00:00Z' = 1.04 (m); and a processed artifact is located at 'processed_data/merged_timeseries_fostercity.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Foster City",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Foster City",
                    "latitude": 37.5585,
                    "longitude": -122.2711
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.5585,
                    "query_longitude": -122.2711,
                    "station_ids": [
                        "9414524"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414524"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414524",
                    "timestamps": [
                        "2025-03-13T01:00:00Z"
                    ],
                    "water_level_m": [
                        0.98
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414524",
                    "timestamps": [
                        "2025-03-13T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.04
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_fostercity.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_057",
        "instruction": "Ensure stakeholder reporting for Richmond (2025-03-14) is prepared. End state: a page 'PAGE-20250314-RICH' titled 'Richmond Flood Risk - 2025-03-14' is created (created_ts '2025-03-14T09:00:00Z'); sections ['Summary','Results','Next Steps'] are included (updated_ts '2025-03-14T09:05:00Z'); properties JSON matches '{\"predictions\":\"processed_data/preds_rich_v1.csv\",\"metrics\":\"processed_data/metrics_rich_v1.csv\",\"figure\":\"figures/qc/rich_overview.png\"}' (updated_ts '2025-03-14T09:10:00Z'); and an email to ['harbor@ci.richmond.ca.us'] is dispatched as 'MSG-20250314-RICH' (draft '2025-03-14T09:20:00Z', sent '2025-03-14T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250314-RICH",
                    "title": "Richmond Flood Risk - 2025-03-14",
                    "created_ts": "2025-03-14T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250314-RICH",
                    "sections": [
                        "Summary",
                        "Results",
                        "Next Steps"
                    ],
                    "updated_ts": "2025-03-14T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250314-RICH",
                    "properties_json": "{\"predictions\":\"processed_data/preds_rich_v1.csv\",\"metrics\":\"processed_data/metrics_rich_v1.csv\",\"figure\":\"figures/qc/rich_overview.png\"}",
                    "updated_ts": "2025-03-14T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250314-RICH",
                    "subject": "Richmond Flood Risk - 2025-03-14",
                    "recipients": [
                        "harbor@ci.richmond.ca.us"
                    ],
                    "created_ts": "2025-03-14T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250314-RICH",
                    "message_id": "MSG-20250314-RICH",
                    "sent_ts": "2025-03-14T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_058",
        "instruction": "Ensure capture of a Benicia intake baseline. End state: configuration includes target_city 'Benicia' (UTC); geocoding uses anchors 38.0494,-122.1586; a proximity record sets '9415144' as primary; observed water levels record '2025-03-15T00:00:00Z' = 0.92 (m); tide predictions register '2025-03-15T00:00:00Z' = 0.99 (m); and a merged artifact is located at 'processed_data/merged_timeseries_benicia.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Benicia",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Benicia",
                    "latitude": 38.0494,
                    "longitude": -122.1586
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.0494,
                    "query_longitude": -122.1586,
                    "station_ids": [
                        "9415144"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9415144"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9415144",
                    "timestamps": [
                        "2025-03-15T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.92
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9415144",
                    "timestamps": [
                        "2025-03-15T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_benicia.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_059",
        "instruction": "Handle the compilation of an Alameda modeling bundle. Final outcome: features located at 'processed_data/features_alameda.csv' (generated_ts '2025-03-16T09:05:00Z'); configuration file at 'processed_data/model_config_alameda.json' with a classification_threshold_m of 0.56 (created_ts '2025-03-16T09:06:00Z'); data split found at 'processed_data/split_alameda.json'; model 'alameda_lr_v1' saved at 'models/alameda_lr_v1.joblib'; predictions available at 'processed_data/preds_alameda_lr_v1.csv' (generated_ts '2025-03-16T10:30:00Z'); metrics at 'processed_data/metrics_alameda_lr_v1.csv' with an auc of 0.72; along with stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_alameda.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-03-16T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_alameda.json",
                    "classification_threshold_m_nullable": 0.56,
                    "created_ts": "2025-03-16T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_alameda.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "alameda_lr_v1",
                    "model_path": "models/alameda_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "alameda_lr_v1",
                    "predictions_csv_path": "processed_data/preds_alameda_lr_v1.csv",
                    "generated_ts": "2025-03-16T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "alameda_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_alameda_lr_v1.csv",
                    "auc_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_alameda_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_alameda_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_060",
        "instruction": "Coordinate the publication of release notes for the South Coast model bundle dated (2025-03-17). The desired state: existence of page 'PAGE-20250317-SC-REL' titled 'South Coast Release - 2025-03-17' (created_ts '2025-03-17T09:00:00Z'); inclusion of sections ['Release Notes','Changelog','Artifacts'] (updated_ts '2025-03-17T09:05:00Z'); properties JSON established as '{\"model\":\"models/southcoast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_southcoast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_southcoast_meta_v1.csv\"}' (updated_ts '2025-03-17T09:10:00Z'); and dispatch an email to ['team@southcoastlab.org'] labeled 'MSG-20250317-SC-REL' (draft '2025-03-17T09:20:00Z', sent '2025-03-17T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250317-SC-REL",
                    "title": "South Coast Release - 2025-03-17",
                    "created_ts": "2025-03-17T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250317-SC-REL",
                    "sections": [
                        "Release Notes",
                        "Changelog",
                        "Artifacts"
                    ],
                    "updated_ts": "2025-03-17T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250317-SC-REL",
                    "properties_json": "{\"model\":\"models/southcoast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_southcoast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_southcoast_meta_v1.csv\"}",
                    "updated_ts": "2025-03-17T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250317-SC-REL",
                    "subject": "South Coast Model Release - 2025-03-17",
                    "recipients": [
                        "team@southcoastlab.org"
                    ],
                    "created_ts": "2025-03-17T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250317-SC-REL",
                    "message_id": "MSG-20250317-SC-REL",
                    "sent_ts": "2025-03-17T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_061",
        "instruction": "You need to set up a Oakland intake baseline. Final state: config indicates target_city 'Oakland' (UTC); geocoding pins 'Oakland' at 37.7749,-122.4194 (canonical 'San Francisco, California'); a proximity result at these coordinates includes station '9414291' which you designate as primary; observed water levels for '9414291' include '2025-04-01T06:00:00Z' = 1.03 (m); tide predictions for '9414291' include '2025-04-01T06:00:00Z' = 1.11 (m); and a processed artifact exists at 'processed_data/merged_timeseries_sf.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Oakland",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Oakland",
                    "latitude": 37.7749,
                    "longitude": -122.4194,
                    "canonical_name": "San Francisco, California"
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.7749,
                    "query_longitude": -122.4194,
                    "station_ids": [
                        "9414291"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414291"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414291",
                    "timestamps": [
                        "2025-04-01T06:00:00Z"
                    ],
                    "water_level_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414291",
                    "timestamps": [
                        "2025-04-01T06:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.11
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sf.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_062",
        "instruction": "You need to record a Long Beach intake baseline. Final state: configuration indicates target_city 'Long Beach' (UTC); geocoding at 33.7701,-118.1937 (canonical 'Long Beach, California'); proximity includes '9410660' set as primary; observed water levels for '9410660' include '2025-04-02T06:00:00Z' = 1.04 (m); tide predictions include '2025-04-02T06:00:00Z' = 1.15 (m); and a processed artifact at 'processed_data/merged_timeseries_lb.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Long Beach",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Long Beach",
                    "latitude": 33.7701,
                    "longitude": -118.1937,
                    "canonical_name": "Long Beach, California"
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.7701,
                    "query_longitude": -118.1937,
                    "station_ids": [
                        "9410660"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410660"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410660",
                    "timestamps": [
                        "2025-04-02T06:00:00Z"
                    ],
                    "water_level_m": [
                        1.04
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410660",
                    "timestamps": [
                        "2025-04-02T06:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.15
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_lb.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_063",
        "instruction": "Handle the creation of a Bodega Bay intake baseline. Final: config 'Bodega Bay' (UTC); geocoding 38.3338,-123.0486; set proximity to include '9416018' as primary; incorporate observed water levels: '2025-04-04T02:00:00Z' = 0.95 (m); integrate tide predictions: '2025-04-04T02:00:00Z' = 1.02 (m); consolidate at 'processed_data/merged_timeseries_bodega.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Bodega Bay",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Bodega Bay",
                    "latitude": 38.3338,
                    "longitude": -123.0486
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.3338,
                    "query_longitude": -123.0486,
                    "station_ids": [
                        "9416018"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9416018"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9416018",
                    "timestamps": [
                        "2025-04-04T02:00:00Z"
                    ],
                    "water_level_m": [
                        0.95
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9416018",
                    "timestamps": [
                        "2025-04-04T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_bodega.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_064",
        "instruction": "Coordinate the recording of a Fort Bragg intake baseline. Final: config 'Fort Bragg' (UTC); geocoding 39.4457,-123.8053; set proximity to include '9417541' as primary; incorporate observed water levels: '2025-04-05T02:00:00Z' = 0.93 (m); integrate tide predictions: '2025-04-05T02:00:00Z' = 1.01 (m); consolidate at 'processed_data/merged_timeseries_fortbragg.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Fort Bragg",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Fort Bragg",
                    "latitude": 39.4457,
                    "longitude": -123.8053
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 39.4457,
                    "query_longitude": -123.8053,
                    "station_ids": [
                        "9417541"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9417541"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9417541",
                    "timestamps": [
                        "2025-04-05T02:00:00Z"
                    ],
                    "water_level_m": [
                        0.93
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9417541",
                    "timestamps": [
                        "2025-04-05T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_fortbragg.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_065",
        "instruction": "Create a Carpinteria intake baseline. Finalize: config 'Carpinteria' (UTC); geocoding 34.3989,-119.5185; proximity includes '9411341' set as primary; observed water levels include '2025-04-08T04:00:00Z' = 0.92 (m); tide predictions include '2025-04-08T04:00:00Z' = 1.00 (m); merged artifact located at 'processed_data/merged_timeseries_carpinteria.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Carpinteria",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Carpinteria",
                    "latitude": 34.3989,
                    "longitude": -119.5185
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.3989,
                    "query_longitude": -119.5185,
                    "station_ids": [
                        "9411341"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411341"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411341",
                    "timestamps": [
                        "2025-04-08T04:00:00Z"
                    ],
                    "water_level_m": [
                        0.92
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411341",
                    "timestamps": [
                        "2025-04-08T04:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_carpinteria.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_066",
        "instruction": "Develop a Malibu intake baseline. Conclude: config 'Malibu' (UTC); geocoding 34.0259,-118.7798; proximity includes '9410841' primary; observed water levels consist of '2025-04-09T05:00:00Z' = 1.02 (m); tide predictions cover '2025-04-09T05:00:00Z' = 1.10 (m); merged artifact located at 'processed_data/merged_timeseries_malibu.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Malibu",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Malibu",
                    "latitude": 34.0259,
                    "longitude": -118.7798
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.0259,
                    "query_longitude": -118.7798,
                    "station_ids": [
                        "9410841"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410841"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410841",
                    "timestamps": [
                        "2025-04-09T05:00:00Z"
                    ],
                    "water_level_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410841",
                    "timestamps": [
                        "2025-04-09T05:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.1
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_malibu.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_067",
        "instruction": "Handle a registration for a Manhattan Beach intake. Finalize: config 'Manhattan Beach' (UTC); geocoding 33.8847,-118.4109; proximity includes '9410662' primary; observed water levels contain '2025-04-10T05:00:00Z' = 1.01 (m); tide predictions contain '2025-04-10T05:00:00Z' = 1.09 (m); merged artifact at 'processed_data/merged_timeseries_manhattan.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Manhattan Beach",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Manhattan Beach",
                    "latitude": 33.8847,
                    "longitude": -118.4109
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.8847,
                    "query_longitude": -118.4109,
                    "station_ids": [
                        "9410662"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410662"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410662",
                    "timestamps": [
                        "2025-04-10T05:00:00Z"
                    ],
                    "water_level_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410662",
                    "timestamps": [
                        "2025-04-10T05:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_manhattan.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_068",
        "instruction": "Coordinate the creation of an Oceanside intake baseline. Finalize: config 'Oceanside' (UTC); geocoding 33.1959,-117.3795; proximity includes '9410280' set primary; observed water levels contain '2025-04-11T01:00:00Z' = 1.00 (m); tide predictions contain '2025-04-11T01:00:00Z' = 1.08 (m); merged artifact at 'processed_data/merged_timeseries_oceanside.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Oceanside",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Oceanside",
                    "latitude": 33.1959,
                    "longitude": -117.3795
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.1959,
                    "query_longitude": -117.3795,
                    "station_ids": [
                        "9410280"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410280"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410280",
                    "timestamps": [
                        "2025-04-11T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410280",
                    "timestamps": [
                        "2025-04-11T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.08
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_oceanside.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_069",
        "instruction": "Handle the recording of a Carlsbad intake baseline. Final: config 'Carlsbad' (UTC); geocoding 33.1581,-117.3506; proximity includes '9410240' primary; observed water levels include '2025-04-12T01:00:00Z' = 0.99 (m); tide predictions include '2025-04-12T01:00:00Z' = 1.07 (m); merged artifact at 'processed_data/merged_timeseries_carlsbad.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Carlsbad",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Carlsbad",
                    "latitude": 33.1581,
                    "longitude": -117.3506
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.1581,
                    "query_longitude": -117.3506,
                    "station_ids": [
                        "9410240"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410240"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410240",
                    "timestamps": [
                        "2025-04-12T01:00:00Z"
                    ],
                    "water_level_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410240",
                    "timestamps": [
                        "2025-04-12T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.07
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_carlsbad.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_070",
        "instruction": "Coordinate the building of a Bodega Bay modeling bundle. Final: features 'processed_data/features_bodega.csv' (generated_ts '2025-04-18T09:05:00Z'); config 'processed_data/model_config_bodega.json' with classification_threshold_m 0.61 (created_ts '2025-04-18T09:06:00Z'); split 'processed_data/split_bodega.json'; model 'bodega_lr_v1' at 'models/bodega_lr_v1.joblib'; predictions 'processed_data/preds_bodega_lr_v1.csv' (generated_ts '2025-04-18T10:30:00Z'); metrics 'processed_data/metrics_bodega_lr_v1.csv' (accuracy 0.69); and stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_bodega.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-18T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_bodega.json",
                    "classification_threshold_m_nullable": 0.61,
                    "created_ts": "2025-04-18T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_bodega.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "model_path": "models/bodega_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "predictions_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                    "generated_ts": "2025-04-18T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "bodega_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_bodega_lr_v1.csv",
                    "accuracy_nullable": 0.69
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_bodega_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_071",
        "instruction": "Handle the creation of a San Pedro modeling bundle. Finalize: features 'processed_data/features_sanpedro.csv' (generated_ts '2025-04-20T09:05:00Z'); configuration 'processed_data/model_config_sanpedro.json' with classification_threshold_m 0.60 (created_ts '2025-04-20T09:06:00Z'); split 'processed_data/split_sanpedro.json'; model 'sanpedro_rf_v1' (type 'random_forest') located at 'models/sanpedro_rf_v1.joblib'; predictions 'processed_data/preds_sanpedro_rf_v1.csv' (generated_ts '2025-04-20T10:30:00Z'); metrics 'processed_data/metrics_sanpedro_rf_v1.csv' (accuracy 0.72); and include stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_sanpedro.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-20T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_sanpedro.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-04-20T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_sanpedro.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "sanpedro_rf_v1",
                    "model_path": "models/sanpedro_rf_v1.joblib",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "sanpedro_rf_v1",
                    "predictions_csv_path": "processed_data/preds_sanpedro_rf_v1.csv",
                    "generated_ts": "2025-04-20T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "sanpedro_rf_v1",
                    "metrics_csv_path": "processed_data/metrics_sanpedro_rf_v1.csv",
                    "accuracy_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_sanpedro_rf_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_sanpedro_rf_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_072",
        "instruction": "Coordinate the registration of an experimental 'gust/wave' feature set and split plan. Conclude: features located at 'processed_data/features_gustwave.csv' with ['gust_6h_ms','wave_height_12h_max_m','pressure_trend_24h_hpa'] (generated_ts '2025-04-26T09:05:00Z'); model configuration at 'processed_data/model_config_gustwave.json' with test_split_fraction 0.30 (created_ts '2025-04-26T09:06:00Z'); and a split summary 'processed_data/split_gustwave.json' with test_fraction 0.30 and counts 700/300 (split_ts '2025-04-26T09:07:00Z').",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_gustwave.csv",
                    "feature_names": [
                        "gust_6h_ms",
                        "wave_height_12h_max_m",
                        "pressure_trend_24h_hpa"
                    ],
                    "generated_ts": "2025-04-26T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_gustwave.json",
                    "test_split_fraction_nullable": 0.3,
                    "created_ts": "2025-04-26T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_gustwave.json",
                    "test_fraction": 0.3,
                    "train_index_count": 700,
                    "test_index_count": 300,
                    "split_ts": "2025-04-26T09:07:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_073",
        "instruction": "Ensure a Berkeley intake baseline is captured. Desired outcome: configuration indicates target_city 'Berkeley' with timezone 'UTC'; geocoding fixes 'Berkeley' at 37.8716,-122.2727; a proximity search at these coordinates lists station '9414762' as primary; observed water levels for '9414762' encompass '2025-04-01T00:00:00Z' = 0.97 (m); tide predictions contain '2025-04-01T00:00:00Z' = 1.03 (m); and a processed artifact is available at 'processed_data/merged_timeseries_berkeley.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Berkeley",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Berkeley",
                    "latitude": 37.8716,
                    "longitude": -122.2727
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.8716,
                    "query_longitude": -122.2727,
                    "station_ids": [
                        "9414762"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414762"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414762",
                    "timestamps": [
                        "2025-04-01T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.97
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414762",
                    "timestamps": [
                        "2025-04-01T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_berkeley.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_074",
        "instruction": "Ensure an Oakland intake baseline is recorded. Target result: configuration identifies target_city 'Oakland' (UTC); geocoding anchors 'Oakland' at 37.8044,-122.2711; a proximity entry records '9414764' as primary; observed water levels for '9414764' span '2025-04-02T02:00:00Z' = 1.02 (m); tide predictions encompass '2025-04-02T02:00:00Z' = 1.08 (m); and a processed artifact is present at 'processed_data/merged_timeseries_oakland.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Oakland",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Oakland",
                    "latitude": 37.8044,
                    "longitude": -122.2711
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.8044,
                    "query_longitude": -122.2711,
                    "station_ids": [
                        "9414764"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414764"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414764",
                    "timestamps": [
                        "2025-04-02T02:00:00Z"
                    ],
                    "water_level_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414764",
                    "timestamps": [
                        "2025-04-02T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.08
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_oakland.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_075",
        "instruction": "Handle a Daly City intake baseline. Desired outcome: configuration lists target_city 'Daly City' (UTC); geocoding anchors 37.6879,-122.4702; a proximity result includes '9414570' which you set primary; observed water levels incorporate '2025-04-02T03:00:00Z' = 1.01 (m); tide predictions feature '2025-04-02T03:00:00Z' = 1.07 (m); and a processed artifact at 'processed_data/merged_timeseries_dalycity.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Daly City",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Daly City",
                    "latitude": 37.6879,
                    "longitude": -122.4702
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.6879,
                    "query_longitude": -122.4702,
                    "station_ids": [
                        "9414570"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414570"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414570",
                    "timestamps": [
                        "2025-04-02T03:00:00Z"
                    ],
                    "water_level_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414570",
                    "timestamps": [
                        "2025-04-02T03:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.07
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_dalycity.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_076",
        "instruction": "Coordinate a Tiburon intake baseline. Final result: configuration shows target_city 'Tiburon' (UTC); geocoding places 37.8735,-122.4569; a proximity record includes '9414444' set primary; observed water levels cover '2025-04-02T04:00:00Z' = 0.99 (m); tide predictions consist of '2025-04-02T04:00:00Z' = 1.05 (m); and a processed artifact exists at 'processed_data/merged_timeseries_tiburon.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Tiburon",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Tiburon",
                    "latitude": 37.8735,
                    "longitude": -122.4569
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.8735,
                    "query_longitude": -122.4569,
                    "station_ids": [
                        "9414444"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414444"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414444",
                    "timestamps": [
                        "2025-04-02T04:00:00Z"
                    ],
                    "water_level_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414444",
                    "timestamps": [
                        "2025-04-02T04:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.05
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_tiburon.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_077",
        "instruction": "Handle the capture of a San Rafael intake baseline. The final state should include: configuration lists with target_city 'San Rafael' (UTC); geocoding fixed at 37.9735,-122.5311; a proximity result containing '9415071' set as primary; observed water levels marked as '2025-04-03T01:00:00Z' = 0.96 (m); tide predictions listed as '2025-04-03T01:00:00Z' = 1.02 (m); and a merged artifact located at 'processed_data/merged_timeseries_sanrafael.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "San Rafael",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "San Rafael",
                    "latitude": 37.9735,
                    "longitude": -122.5311
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.9735,
                    "query_longitude": -122.5311,
                    "station_ids": [
                        "9415071"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9415071"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9415071",
                    "timestamps": [
                        "2025-04-03T01:00:00Z"
                    ],
                    "water_level_m": [
                        0.96
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9415071",
                    "timestamps": [
                        "2025-04-03T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.02
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sanrafael.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_078",
        "instruction": "Coordinate the recording of a Vallejo intake baseline. Ensure the end state includes: configuration documenting target_city 'Vallejo' (UTC); geocoding set at 38.1041,-122.2566; a proximity record that includes '9415142' marked as primary; observed water levels noted as '2025-04-03T02:00:00Z' = 0.94 (m); tide predictions indicated as '2025-04-03T02:00:00Z' = 1.00 (m); and a processed artifact found at 'processed_data/merged_timeseries_vallejo.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Vallejo",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Vallejo",
                    "latitude": 38.1041,
                    "longitude": -122.2566
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 38.1041,
                    "query_longitude": -122.2566,
                    "station_ids": [
                        "9415142"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9415142"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9415142",
                    "timestamps": [
                        "2025-04-03T02:00:00Z"
                    ],
                    "water_level_m": [
                        0.94
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9415142",
                    "timestamps": [
                        "2025-04-03T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_vallejo.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_079",
        "instruction": "Handle capturing a Port Hueneme intake baseline. Goal: ensure configuration lists target_city 'Port Hueneme' (UTC); geocoding anchors 34.1478,-119.1951; a proximity record includes '9411230' set primary; observed water levels include '2025-04-03T03:00:00Z' = 0.93 (m); tide predictions encompass '2025-04-03T03:00:00Z' = 0.99 (m); and a merged artifact is located at 'processed_data/merged_timeseries_porthueneme.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Port Hueneme",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Port Hueneme",
                    "latitude": 34.1478,
                    "longitude": -119.1951
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.1478,
                    "query_longitude": -119.1951,
                    "station_ids": [
                        "9411230"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411230"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411230",
                    "timestamps": [
                        "2025-04-03T03:00:00Z"
                    ],
                    "water_level_m": [
                        0.93
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411230",
                    "timestamps": [
                        "2025-04-03T03:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.99
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_porthueneme.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_080",
        "instruction": "Coordinate the registration of an Oxnard intake baseline. Required outcome: configuration indicates target_city 'Oxnard' (UTC); geocoding places 34.1975,-119.1771; a proximity result includes '9411231' which you assign as primary; observed water levels feature '2025-04-03T04:00:00Z' = 0.95 (m); tide predictions highlight '2025-04-03T04:00:00Z' = 1.01 (m); and a processed artifact is present at 'processed_data/merged_timeseries_oxnard.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Oxnard",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Oxnard",
                    "latitude": 34.1975,
                    "longitude": -119.1771
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.1975,
                    "query_longitude": -119.1771,
                    "station_ids": [
                        "9411231"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411231"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411231",
                    "timestamps": [
                        "2025-04-03T04:00:00Z"
                    ],
                    "water_level_m": [
                        0.95
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411231",
                    "timestamps": [
                        "2025-04-03T04:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_oxnard.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_081",
        "instruction": "Handle the capture of a Carpinteria intake baseline. End state: configuration lists target_city 'Carpinteria' (UTC); geocoding anchors 34.3989,-119.5185; a proximity record includes '9411370' set primary; observed water levels include '2025-04-04T00:00:00Z' = 0.90 (m); tide predictions include '2025-04-04T00:00:00Z' = 0.96 (m); and a merged artifact exists at 'processed_data/merged_timeseries_carpinteria.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Carpinteria",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Carpinteria",
                    "latitude": 34.3989,
                    "longitude": -119.5185
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.3989,
                    "query_longitude": -119.5185,
                    "station_ids": [
                        "9411370"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9411370"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9411370",
                    "timestamps": [
                        "2025-04-04T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.9
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9411370",
                    "timestamps": [
                        "2025-04-04T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        0.96
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_carpinteria.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_082",
        "instruction": "Coordinate the capture of a Malibu intake baseline. End state: configuration shows target_city 'Malibu' (UTC); geocoding places 34.0259,-118.7798; a proximity record includes '9410844' set primary; observed water levels include '2025-04-04T01:00:00Z' = 1.04 (m); tide predictions include '2025-04-04T01:00:00Z' = 1.10 (m); and a processed artifact at 'processed_data/merged_timeseries_malibu.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Malibu",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Malibu",
                    "latitude": 34.0259,
                    "longitude": -118.7798
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 34.0259,
                    "query_longitude": -118.7798,
                    "station_ids": [
                        "9410844"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410844"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410844",
                    "timestamps": [
                        "2025-04-04T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.04
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410844",
                    "timestamps": [
                        "2025-04-04T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.1
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_malibu.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_083",
        "instruction": "Handle the registration of a Dana Point intake baseline. End state: configuration displays target_city 'Dana Point' (UTC); geocoding pins 33.4669,-117.6981; a proximity record marks '9410667' as primary; observed water levels contain '2025-04-05T00:00:00Z' = 1.00 (m); tide predictions show '2025-04-05T00:00:00Z' = 1.06 (m); and a merged artifact is available at 'processed_data/merged_timeseries_danapoint.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Dana Point",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Dana Point",
                    "latitude": 33.4669,
                    "longitude": -117.6981
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 33.4669,
                    "query_longitude": -117.6981,
                    "station_ids": [
                        "9410667"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410667"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410667",
                    "timestamps": [
                        "2025-04-05T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.0
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410667",
                    "timestamps": [
                        "2025-04-05T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.06
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_danapoint.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_084",
        "instruction": "Coordinate the capture of a Del Mar intake baseline. End state: configuration displays target_city 'Del Mar' (UTC); geocoding locates 32.9595,-117.2653; a proximity record lists '9410240' as primary; observed water levels note '2025-04-05T01:00:00Z' = 1.03 (m); tide predictions report '2025-04-05T01:00:00Z' = 1.09 (m); and a processed artifact is present at 'processed_data/merged_timeseries_delmar.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Del Mar",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Del Mar",
                    "latitude": 32.9595,
                    "longitude": -117.2653
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 32.9595,
                    "query_longitude": -117.2653,
                    "station_ids": [
                        "9410240"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410240"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410240",
                    "timestamps": [
                        "2025-04-05T01:00:00Z"
                    ],
                    "water_level_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410240",
                    "timestamps": [
                        "2025-04-05T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.09
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_delmar.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_085",
        "instruction": "Handle the recording of an Imperial Beach intake baseline. Final state: configuration lists target_city 'Imperial Beach' (UTC); geocoding anchors 32.5839,-117.1131; a proximity result includes '9410055' set primary; observed water levels include '2025-04-05T02:00:00Z' = 0.98 (m); tide predictions include '2025-04-05T02:00:00Z' = 1.04 (m); and a processed artifact at 'processed_data/merged_timeseries_imperialbeach.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Imperial Beach",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Imperial Beach",
                    "latitude": 32.5839,
                    "longitude": -117.1131
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 32.5839,
                    "query_longitude": -117.1131,
                    "station_ids": [
                        "9410055"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9410055"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9410055",
                    "timestamps": [
                        "2025-04-05T02:00:00Z"
                    ],
                    "water_level_m": [
                        0.98
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9410055",
                    "timestamps": [
                        "2025-04-05T02:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.04
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_imperialbeach.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_086",
        "instruction": "Coordinate the assembly of a Berkeley modeling bundle. End result: features at 'processed_data/features_berk.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-04-06T09:05:00Z'); config at 'processed_data/model_config_berk.json' with classification_threshold_m 0.59 (created_ts '2025-04-06T09:06:00Z'); split summary at 'processed_data/split_berk.json'; model 'berk_lr_v1' at 'models/berk_lr_v1.joblib'; predictions at 'processed_data/preds_berk_lr_v1.csv' (generated_ts '2025-04-06T10:30:00Z'); metrics at 'processed_data/metrics_berk_lr_v1.csv' (auc 0.71); and stakeholder references to those artifacts.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_berk.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-06T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_berk.json",
                    "classification_threshold_m_nullable": 0.59,
                    "created_ts": "2025-04-06T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_berk.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "berk_lr_v1",
                    "model_path": "models/berk_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "berk_lr_v1",
                    "predictions_csv_path": "processed_data/preds_berk_lr_v1.csv",
                    "generated_ts": "2025-04-06T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "berk_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_berk_lr_v1.csv",
                    "auc_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_berk_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_berk_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_087",
        "instruction": "Handle the assembly of a Vallejo modeling bundle. End state: features at 'processed_data/features_val.csv' (generated_ts '2025-04-08T09:05:00Z'); config at 'processed_data/model_config_val.json' with classification_threshold_m 0.58 (created_ts '2025-04-08T09:06:00Z'); split at 'processed_data/split_val.json'; model 'val_lr_v1' at 'models/val_lr_v1.joblib'; predictions at 'processed_data/preds_val_lr_v1.csv' (generated_ts '2025-04-08T10:30:00Z'); metrics at 'processed_data/metrics_val_lr_v1.csv' (auc 0.70); and stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_val.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-08T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_val.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-04-08T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_val.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "val_lr_v1",
                    "model_path": "models/val_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "val_lr_v1",
                    "predictions_csv_path": "processed_data/preds_val_lr_v1.csv",
                    "generated_ts": "2025-04-08T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "val_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_val_lr_v1.csv",
                    "auc_nullable": 0.7
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_val_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_val_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_088",
        "instruction": "Coordinate the compilation of a Port Hueneme modeling bundle. End state: features at 'processed_data/features_ph.csv' (generated_ts '2025-04-09T09:05:00Z'); config at 'processed_data/model_config_ph.json' with classification_threshold_m 0.57 (created_ts '2025-04-09T09:06:00Z'); split at 'processed_data/split_ph.json'; model 'ph_lr_v1' at 'models/ph_lr_v1.joblib'; predictions at 'processed_data/preds_ph_lr_v1.csv' (generated_ts '2025-04-09T10:30:00Z'); metrics at 'processed_data/metrics_ph_lr_v1.csv' (accuracy 0.67); and stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_ph.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-09T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_ph.json",
                    "classification_threshold_m_nullable": 0.57,
                    "created_ts": "2025-04-09T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_ph.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "ph_lr_v1",
                    "model_path": "models/ph_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "ph_lr_v1",
                    "predictions_csv_path": "processed_data/preds_ph_lr_v1.csv",
                    "generated_ts": "2025-04-09T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "ph_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_ph_lr_v1.csv",
                    "accuracy_nullable": 0.67
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_ph_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_ph_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_089",
        "instruction": "Construct a Malibu modeling bundle. Finalize with: features at 'processed_data/features_mal.csv' (generated_ts '2025-04-10T09:05:00Z'); configuration at 'processed_data/model_config_mal.json' with classification_threshold_m 0.60 (created_ts '2025-04-10T09:06:00Z'); split definition at 'processed_data/split_mal.json'; model 'mal_rf_v1' (type 'random_forest') stored at 'models/mal_rf_v1.joblib'; predictions placed at 'processed_data/preds_mal_rf_v1.csv' (generated_ts '2025-04-10T10:30:00Z'); metrics located at 'processed_data/metrics_mal_rf_v1.csv' (auc 0.72); along with stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_mal.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-10T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_mal.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-04-10T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_mal.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "mal_rf_v1",
                    "model_path": "models/mal_rf_v1.joblib",
                    "model_type": "random_forest"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "mal_rf_v1",
                    "predictions_csv_path": "processed_data/preds_mal_rf_v1.csv",
                    "generated_ts": "2025-04-10T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "mal_rf_v1",
                    "metrics_csv_path": "processed_data/metrics_mal_rf_v1.csv",
                    "auc_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_mal_rf_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_mal_rf_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_090",
        "instruction": "Coordinate the registration of an SF Bay meta\u2011model bundle. Conclude with: features at 'processed_data/features_sfbay_meta.csv' featuring ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-04-11T09:05:00Z'); configuration at 'processed_data/model_config_sfbay_meta.json' with classification_threshold_m 0.60 (created_ts '2025-04-11T09:06:00Z'); split summary at 'processed_data/split_sfbay_meta.json'; model 'sfbay_meta_v1' located at 'models/sfbay_meta_v1.joblib'; predictions found at 'processed_data/preds_sfbay_meta_v1.csv' (generated_ts '2025-04-11T10:30:00Z'); metrics at 'processed_data/metrics_sfbay_meta_v1.csv' (accuracy 0.72); and stakeholder references.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_sfbay_meta.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-11T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_sfbay_meta.json",
                    "classification_threshold_m_nullable": 0.6,
                    "created_ts": "2025-04-11T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_sfbay_meta.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "sfbay_meta_v1",
                    "model_path": "models/sfbay_meta_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "sfbay_meta_v1",
                    "predictions_csv_path": "processed_data/preds_sfbay_meta_v1.csv",
                    "generated_ts": "2025-04-11T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "sfbay_meta_v1",
                    "metrics_csv_path": "processed_data/metrics_sfbay_meta_v1.csv",
                    "accuracy_nullable": 0.72
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_sfbay_meta_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_sfbay_meta_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_091",
        "instruction": "Compile a Richmond modeling bundle, ensuring the following are present: features at 'processed_data/features_rich.csv' (generated_ts '2025-04-12T09:05:00Z'); the configuration at 'processed_data/model_config_rich.json' with classification_threshold_m 0.58 (created_ts '2025-04-12T09:06:00Z'); split information at 'processed_data/split_rich.json'; the model 'rich_lr_v1' located at 'models/rich_lr_v1.joblib'; predictions in 'processed_data/preds_rich_lr_v1.csv' (generated_ts '2025-04-12T10:30:00Z'); metrics within 'processed_data/metrics_rich_lr_v1.csv' (auc 0.71); and references for stakeholders.",
        "actions": [
            {
                "name": "StoreFeatures",
                "arguments": {
                    "csv_path": "processed_data/features_rich.csv",
                    "feature_names": [
                        "precip_24h_mm",
                        "tide_anomaly_6h_max_m",
                        "pressure_drop_6h_hpa"
                    ],
                    "generated_ts": "2025-04-12T09:05:00Z"
                },
            },
            {
                "name": "WriteModelConfig",
                "arguments": {
                    "saved_json_path": "processed_data/model_config_rich.json",
                    "classification_threshold_m_nullable": 0.58,
                    "created_ts": "2025-04-12T09:06:00Z"
                },
            },
            {
                "name": "CreateTimeBasedSplit",
                "arguments": {
                    "split_summary_json_path": "processed_data/split_rich.json"
                },
            },
            {
                "name": "RegisterModel",
                "arguments": {
                    "model_name": "rich_lr_v1",
                    "model_path": "models/rich_lr_v1.joblib"
                },
            },
            {
                "name": "StorePredictions",
                "arguments": {
                    "model_name": "rich_lr_v1",
                    "predictions_csv_path": "processed_data/preds_rich_lr_v1.csv",
                    "generated_ts": "2025-04-12T10:30:00Z"
                },
            },
            {
                "name": "StoreMetrics",
                "arguments": {
                    "model_name": "rich_lr_v1",
                    "metrics_csv_path": "processed_data/metrics_rich_lr_v1.csv",
                    "auc_nullable": 0.71
                },
            },
            {
                "name": "RecordStakeholderOutputs",
                "arguments": {
                    "predictions_final_csv_path": "processed_data/preds_rich_lr_v1.csv",
                    "metrics_summary_csv_path": "processed_data/metrics_rich_lr_v1.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_092",
        "instruction": "Prepare the stakeholder reporting documents for Berkeley on 2025-04-10. Ensure the following: a page 'PAGE-20250410-BERK' entitled 'Berkeley Flood Risk - 2025-04-10' is available (created_ts '2025-04-10T09:00:00Z'); sections ['Summary','Results','Actions'] are included (updated_ts '2025-04-10T09:05:00Z'); properties match the specific JSON '{\"predictions\":\"processed_data/preds_berk_lr_v1.csv\",\"metrics\":\"processed_data/metrics_berk_lr_v1.csv\",\"figure\":\"figures/qc/berkeley_overview.png\"}' (updated_ts '2025-04-10T09:10:00Z'); and an email draft 'DRAFT-20250410-BERK' addressed to ['publicworks@cityofberkeley.info'] is dispatched as 'MSG-20250410-BERK' (draft '2025-04-10T09:20:00Z', sent '2025-04-10T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250410-BERK",
                    "title": "Berkeley Flood Risk - 2025-04-10",
                    "created_ts": "2025-04-10T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250410-BERK",
                    "sections": [
                        "Summary",
                        "Results",
                        "Actions"
                    ],
                    "updated_ts": "2025-04-10T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250410-BERK",
                    "properties_json": "{\"predictions\":\"processed_data/preds_berk_lr_v1.csv\",\"metrics\":\"processed_data/metrics_berk_lr_v1.csv\",\"figure\":\"figures/qc/berkeley_overview.png\"}",
                    "updated_ts": "2025-04-10T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250410-BERK",
                    "subject": "Berkeley Flood Risk - 2025-04-10",
                    "recipients": [
                        "publicworks@cityofberkeley.info"
                    ],
                    "attachments_paths": [
                        "figures/qc/berkeley_overview.png"
                    ],
                    "created_ts": "2025-04-10T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250410-BERK",
                    "message_id": "MSG-20250410-BERK",
                    "sent_ts": "2025-04-10T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_093",
        "instruction": "Ensure stakeholder reporting preparation for Oakland (2025-04-11). Final condition: a page 'PAGE-20250411-OAK' with the title 'Oakland Flood Risk - 2025-04-11' must be available (created_ts '2025-04-11T09:00:00Z'); sections ['Summary','Drivers','Next Steps'] should be included (updated_ts '2025-04-11T09:05:00Z'); properties must exactly match the JSON '{\"predictions\":\"processed_data/preds_oak_rf_v1.csv\",\"metrics\":\"processed_data/metrics_oak_rf_v1.csv\",\"figure\":\"figures/qc/oak_overview.png\"}' (updated_ts '2025-04-11T09:10:00Z'); and an email draft 'DRAFT-20250411-OAK' addressed to ['resilience@oaklandca.gov'] should be sent under 'MSG-20250411-OAK' (draft '2025-04-11T09:20:00Z', sent '2025-04-11T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250411-OAK",
                    "title": "Oakland Flood Risk - 2025-04-11",
                    "created_ts": "2025-04-11T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250411-OAK",
                    "sections": [
                        "Summary",
                        "Drivers",
                        "Next Steps"
                    ],
                    "updated_ts": "2025-04-11T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250411-OAK",
                    "properties_json": "{\"predictions\":\"processed_data/preds_oak_rf_v1.csv\",\"metrics\":\"processed_data/metrics_oak_rf_v1.csv\",\"figure\":\"figures/qc/oak_overview.png\"}",
                    "updated_ts": "2025-04-11T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250411-OAK",
                    "subject": "Oakland Flood Risk - 2025-04-11",
                    "recipients": [
                        "resilience@oaklandca.gov"
                    ],
                    "attachments_paths": [
                        "figures/qc/oak_overview.png"
                    ],
                    "created_ts": "2025-04-11T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250411-OAK",
                    "message_id": "MSG-20250411-OAK",
                    "sent_ts": "2025-04-11T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_094",
        "instruction": "Guarantee the publication of release notes for the SF Bay model bundle (2025-04-12). Final outcome: a page 'PAGE-20250412-SFBAY-REL' with the title 'SF Bay Release - 2025-04-12' should be present (created_ts '2025-04-12T09:00:00Z'); sections ['Release Notes','Changelog','Artifacts'] must be included (updated_ts '2025-04-12T09:05:00Z'); properties JSON must be configured to '{\"model\":\"models/sfbay_meta_v1.joblib\",\"predictions\":\"processed_data/preds_sfbay_meta_v1.csv\",\"metrics\":\"processed_data/metrics_sfbay_meta_v1.csv\"}' (updated_ts '2025-04-12T09:10:00Z'); and an email to ['team@sfbaylab.org'] has to be sent as 'MSG-20250412-SFBAY-REL' (draft '2025-04-12T09:20:00Z', sent '2025-04-12T09:25:00Z').",
        "actions": [
            {
                "name": "NotionCreatePage",
                "arguments": {
                    "page_id": "PAGE-20250412-SFBAY-REL",
                    "title": "SF Bay Release - 2025-04-12",
                    "created_ts": "2025-04-12T09:00:00Z"
                },
            },
            {
                "name": "NotionAppendSections",
                "arguments": {
                    "page_id": "PAGE-20250412-SFBAY-REL",
                    "sections": [
                        "Release Notes",
                        "Changelog",
                        "Artifacts"
                    ],
                    "updated_ts": "2025-04-12T09:05:00Z"
                },
            },
            {
                "name": "NotionUpdatePageProperties",
                "arguments": {
                    "page_id": "PAGE-20250412-SFBAY-REL",
                    "properties_json": "{\"model\":\"models/sfbay_meta_v1.joblib\",\"predictions\":\"processed_data/preds_sfbay_meta_v1.csv\",\"metrics\":\"processed_data/metrics_sfbay_meta_v1.csv\"}",
                    "updated_ts": "2025-04-12T09:10:00Z"
                },
            },
            {
                "name": "GmailDraftEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250412-SFBAY-REL",
                    "subject": "SF Bay Model Release - 2025-04-12",
                    "recipients": [
                        "team@sfbaylab.org"
                    ],
                    "created_ts": "2025-04-12T09:20:00Z"
                },
            },
            {
                "name": "GmailSendEmail",
                "arguments": {
                    "draft_id": "DRAFT-20250412-SFBAY-REL",
                    "message_id": "MSG-20250412-SFBAY-REL",
                    "sent_ts": "2025-04-12T09:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_095",
        "instruction": "Ensure to register literature for 'coastal inundation LiDAR'. End state: a search query 'coastal inundation LiDAR' displays result_item_ids ['ZOT-6001','ZOT-6005'] with search_ts '2025-04-12T12:00:00Z'; metadata titles ['Smith 2020 LiDAR Coastal Mapping','Lee 2022 High-Res DEMs'] with fetched_ts '2025-04-12T12:10:00Z'; fulltext paths ['docs/lit/6001.pdf','docs/lit/6005.pdf'] with fetched_ts '2025-04-12T12:12:00Z'; and a manifest located at 'docs/lit/manifest_lidar.txt' comprises 'LiDAR inundation mapping references'.",
        "actions": [
            {
                "name": "ZoteroSearchItems",
                "arguments": {
                    "query": "coastal inundation LiDAR",
                    "result_item_ids": [
                        "ZOT-6001",
                        "ZOT-6005"
                    ],
                    "search_ts": "2025-04-12T12:00:00Z"
                },
            },
            {
                "name": "ZoteroItemMetadata",
                "arguments": {
                    "item_ids": [
                        "ZOT-6001",
                        "ZOT-6005"
                    ],
                    "titles": [
                        "Smith 2020 LiDAR Coastal Mapping",
                        "Lee 2022 High-Res DEMs"
                    ],
                    "fetched_ts": "2025-04-12T12:10:00Z"
                },
            },
            {
                "name": "ZoteroItemFulltext",
                "arguments": {
                    "item_ids": [
                        "ZOT-6001",
                        "ZOT-6005"
                    ],
                    "file_paths": [
                        "docs/lit/6001.pdf",
                        "docs/lit/6005.pdf"
                    ],
                    "fetched_ts": "2025-04-12T12:12:00Z"
                },
            },
            {
                "name": "WriteFileText",
                "arguments": {
                    "path": "docs/lit/manifest_lidar.txt",
                    "content": "LiDAR inundation mapping references"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_096",
        "instruction": "Make sure to record literature for 'ensemble downscaling coastal extremes'. End state: a search record using query 'ensemble downscaling coastal extremes' shows ['ZOT-6101','ZOT-6108'] (search_ts '2025-04-12T12:20:00Z'); metadata includes titles ['Martinez 2020 Downscaling Extremes','Zhao 2023 Multi\u2011Model Coastal Ensemble'] (fetched_ts '2025-04-12T12:30:00Z'); fulltexts located at ['docs/lit/6101.pdf','docs/lit/6108.pdf'] (fetched_ts '2025-04-12T12:32:00Z'); and a manifest 'docs/lit/manifest_downscaling.txt' holds 'ensemble downscaling references'.",
        "actions": [
            {
                "name": "ZoteroSearchItems",
                "arguments": {
                    "query": "ensemble downscaling coastal extremes",
                    "result_item_ids": [
                        "ZOT-6101",
                        "ZOT-6108"
                    ],
                    "search_ts": "2025-04-12T12:20:00Z"
                },
            },
            {
                "name": "ZoteroItemMetadata",
                "arguments": {
                    "item_ids": [
                        "ZOT-6101",
                        "ZOT-6108"
                    ],
                    "titles": [
                        "Martinez 2020 Downscaling Extremes",
                        "Zhao 2023 Multi-Model Coastal Ensemble"
                    ],
                    "fetched_ts": "2025-04-12T12:30:00Z"
                },
            },
            {
                "name": "ZoteroItemFulltext",
                "arguments": {
                    "item_ids": [
                        "ZOT-6101",
                        "ZOT-6108"
                    ],
                    "file_paths": [
                        "docs/lit/6101.pdf",
                        "docs/lit/6108.pdf"
                    ],
                    "fetched_ts": "2025-04-12T12:32:00Z"
                },
            },
            {
                "name": "WriteFileText",
                "arguments": {
                    "path": "docs/lit/manifest_downscaling.txt",
                    "content": "ensemble downscaling references"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_097",
        "instruction": "Ensure you capture a Marin City intake baseline. End objective: configuration shows target_city 'Marin City' (UTC); geocoding anchors 37.8686,-122.5089; a proximity record includes '9414255' set primary; observed water levels include '2025-04-14T00:00:00Z' = 0.95 (m); tide predictions include '2025-04-14T00:00:00Z' = 1.01 (m); and a processed artifact exists at 'processed_data/merged_timeseries_marincity.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Marin City",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Marin City",
                    "latitude": 37.8686,
                    "longitude": -122.5089
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.8686,
                    "query_longitude": -122.5089,
                    "station_ids": [
                        "9414255"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414255"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414255",
                    "timestamps": [
                        "2025-04-14T00:00:00Z"
                    ],
                    "water_level_m": [
                        0.95
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414255",
                    "timestamps": [
                        "2025-04-14T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.01
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_marincity.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_098",
        "instruction": "Be sure to record a Richmond intake baseline. Desired state: configuration shows target_city 'Richmond' (UTC); geocoding places 37.9358,-122.3477; a proximity record includes '9414763' set primary; observed water levels include '2025-04-14T01:00:00Z' = 0.97 (m); tide predictions include '2025-04-14T01:00:00Z' = 1.03 (m); and a processed artifact at 'processed_data/merged_timeseries_richmond.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Richmond",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Richmond",
                    "latitude": 37.9358,
                    "longitude": -122.3477
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.9358,
                    "query_longitude": -122.3477,
                    "station_ids": [
                        "9414763"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414763"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414763",
                    "timestamps": [
                        "2025-04-14T01:00:00Z"
                    ],
                    "water_level_m": [
                        0.97
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414763",
                    "timestamps": [
                        "2025-04-14T01:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_richmond.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_099",
        "instruction": "Handle the capture of a Oakland intake baseline. End state: configuration lists target_city 'Oakland' (UTC); geocoding anchors 37.7749,-122.4194; a proximity record includes '9414292' set primary; observed water levels include '2025-04-15T00:00:00Z' = 1.06 (m); tide predictions include '2025-04-15T00:00:00Z' = 1.12 (m); and a processed artifact exists at 'processed_data/merged_timeseries_sf.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Oakland",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Oakland",
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 37.7749,
                    "query_longitude": -122.4194,
                    "station_ids": [
                        "9414292"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9414292"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9414292",
                    "timestamps": [
                        "2025-04-15T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.06
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9414292",
                    "timestamps": [
                        "2025-04-15T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.12
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_sf.csv"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "ds_v1_100",
        "instruction": "Coordinate the establishment of an Astoria intake baseline. End state: configuration shows target_city 'Astoria' (timezone 'UTC'); geocoding places 'Astoria' at 46.1879,-123.8313; a proximity result at those coordinates includes station '9439040' which is set primary; observed water levels for '9439040' include '2025-05-01T00:00:00Z' = 1.03 (m); tide predictions include '2025-05-01T00:00:00Z' = 1.10 (m); and a processed artifact exists at 'processed_data/merged_timeseries_astoria.csv'.",
        "actions": [
            {
                "name": "SetProjectConfig",
                "arguments": {
                    "target_city": "Astoria",
                    "timezone_default": "UTC"
                },
            },
            {
                "name": "StoreGeocodingResult",
                "arguments": {
                    "query_city": "Astoria",
                    "latitude": 46.1879,
                    "longitude": -123.8313
                },
            },
            {
                "name": "StoreNoaaStationSearch",
                "arguments": {
                    "query_latitude": 46.1879,
                    "query_longitude": -123.8313,
                    "station_ids": [
                        "9439040"
                    ]
                },
            },
            {
                "name": "SetPrimaryStation",
                "arguments": {
                    "station_id": "9439040"
                },
            },
            {
                "name": "StoreWaterLevels",
                "arguments": {
                    "station_id": "9439040",
                    "timestamps": [
                        "2025-05-01T00:00:00Z"
                    ],
                    "water_level_m": [
                        1.03
                    ],
                    "units": "m"
                },
            },
            {
                "name": "StoreTidePredictions",
                "arguments": {
                    "station_id": "9439040",
                    "timestamps": [
                        "2025-05-01T00:00:00Z"
                    ],
                    "tide_pred_m": [
                        1.1
                    ],
                    "units": "m"
                },
            },
            {
                "name": "ComputeAndStoreMergedTimeseries",
                "arguments": {
                    "csv_path": "processed_data/merged_timeseries_astoria.csv"
                }
            }
        ],
        "outputs": []
    }
]
