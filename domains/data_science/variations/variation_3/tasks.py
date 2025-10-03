# Copyright Sierra

tasks = [
    {
        "annotator": R,
        "user_id": "ds_v3_1001",
        "instruction": "Establish a backfill cutoff for December-2025 and confirm readiness. Final conditions: project configuration includes backfill_cutoff '2025-12-22T20:00:00Z' and can be retrieved; terminal log event 'BACKFILL_CUTOFF_APPLIED' with message 'Backfill cutoff applied for end-of-year runs.' is present and viewable; a QC PDF bearing the label 'QC_CONFIG_BACKFILL_2025-12' with artifact_type 'pdf' is present and can be accessed.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "backfill_cutoff": "2025-12-22T20:00:00Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "backfill_cutoff"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_CUTOFF_APPLIED",
                    "message": "Backfill cutoff applied for end-of-year runs."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_CUTOFF_APPLIED"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-12"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-12",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-12"
                }
            }
        ],
        "outputs": [
                "config.backfill_cutoff=2025-12-22T20:00:00Z | log.event_type=BACKFILL_CUTOFF_APPLIED; log.message=Backfill cutoff applied for end-of-year runs. | qc.figure_label=QC_CONFIG_BACKFILL_2025-12; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1002",
        "instruction": "Establish a September-2025 backfill cutoff and confirm all is prepared. Final conditions: project configuration includes backfill_cutoff '2025-09-15T16:00:00Z' and is accessible; terminal log event 'BACKFILL_CUTOFF_CONFIRMED' with message 'September backfill cutoff completed successfully.' exists and can be retrieved; a QC PDF tagged as 'QC_CONFIG_BACKFILL_2025-09' with artifact_type 'pdf' is present and accessible.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "backfill_cutoff": "2025-09-15T16:00:00Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "backfill_cutoff"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_CUTOFF_CONFIRMED",
                    "message": "September backfill cutoff completed successfully."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_CUTOFF_CONFIRMED"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-09"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2025-09"
                }
            }
        ],
        "outputs": [
                "config.backfill_cutoff=2025-09-15T16:00:00Z | log.event_type=BACKFILL_CUTOFF_CONFIRMED; log.message=September backfill cutoff completed successfully. | qc.figure_label=QC_CONFIG_BACKFILL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1004",
        "instruction": "Handle the creation of a heatwave risk dataset 'heatwave_risk_v1' for 2025\u201108. Final condition: dataset 'heatwave_risk_v1' (version '1.0') with columns ['temperature','humidity','heat_risk'] is available and accessible; feature file '/features/heatwave_risk_v1.parquet' exists and can be read; a QC PDF with the label 'QC_HEATWAVE_RISK_2025-08' having artifact_type 'pdf' is obtainable; stakeholder report 'Heatwave Risk Aug 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "heatwave_risk_v1",
                    "version": "1.0",
                    "columns": [
                        "temperature",
                        "humidity",
                        "heat_risk"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "heatwave_risk_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/heatwave_risk_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/heatwave_risk_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_HEATWAVE_RISK_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_HEATWAVE_RISK_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_HEATWAVE_RISK_2025-08"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Heatwave Risk Aug 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Heatwave Risk Aug 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=heatwave_risk_v1; version=1.0; columns=temperature|humidity|heat_risk | file.path=/features/heatwave_risk_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_HEATWAVE_RISK_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf | stakeholder.output_label=Heatwave Risk Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1005",
        "instruction": "Coordinate the creation of a drought risk dataset 'drought_risk_v1' for 2025\u201109. Final condition: dataset 'drought_risk_v1' (version '1.0') with columns ['soil_moisture','temperature','drought_index'] is available and can be read; feature file '/features/drought_risk_v1.parquet' is present and obtainable; a QC PDF is present for the label 'QC_DROUGHT_RISK_2025-09' with artifact_type 'pdf'; stakeholder report 'Drought Risk Sep 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "drought_risk_v1",
                    "version": "1.0",
                    "columns": [
                        "soil_moisture",
                        "temperature",
                        "drought_index"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "drought_risk_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/drought_risk_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/drought_risk_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_DROUGHT_RISK_2025-09"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_DROUGHT_RISK_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_DROUGHT_RISK_2025-09"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Drought Risk Sep 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Drought Risk Sep 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=drought_risk_v1; version=1.0; columns=soil_moisture|temperature|drought_index | file.path=/features/drought_risk_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_DROUGHT_RISK_2025-09; qc.figure_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf | stakeholder.output_label=Drought Risk Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1006",
        "instruction": "Ensure completion of the quality control process for the sea surface temperature feature for June-2025. Final requirements: the dataset 'sst_features_v2' (version '2.1') with columns ['sst_mean','sst_max','sst_std'] should be documented and accessible; the feature file '/features/sst_features_v2.parquet' should be present and readable; create a QC PDF for the label 'QC_SST_FEATURES_2025-06' with type 'pdf' and ensure accessibility; the stakeholder deliverable 'SST QC June 2025' (audience 'oceanography_team') must link to 'https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf' and be accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "sst_features_v2",
                    "version": "2.1",
                    "columns": [
                        "sst_mean",
                        "sst_max",
                        "sst_std"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "sst_features_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/sst_features_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/sst_features_v2.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_FEATURES_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_FEATURES_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_FEATURES_2025-06"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "SST QC June 2025",
                    "audience": "oceanography_team",
                    "artifact_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "SST QC June 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=sst_features_v2; version=2.1; columns=sst_mean|sst_max|sst_std | file.path=/features/sst_features_v2.parquet; file.mime=application/parquet | qc.figure_label=QC_SST_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf | stakeholder.output_label=SST QC June 2025; audience=oceanography_team; artifact_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1007",
        "instruction": "Complete the ocean current feature quality control for July-2025. Final requirements: 'ocean_current_v1' dataset (version '1.5') with columns ['current_speed','current_dir','std_dev'] should be recorded and accessible; the feature file '/features/ocean_current_v1.parquet' must exist and be readable; prepare a QC PDF for the label 'QC_OCEAN_CURRENT_2025-07' with type 'pdf' ensuring it is accessible; the stakeholder deliverable 'Ocean Current QC July 2025' (audience 'marine_team') must reference 'https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf' and be available.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "ocean_current_v1",
                    "version": "1.5",
                    "columns": [
                        "current_speed",
                        "current_dir",
                        "std_dev"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "ocean_current_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/ocean_current_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/ocean_current_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_OCEAN_CURRENT_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_OCEAN_CURRENT_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_OCEAN_CURRENT_2025-07"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Ocean Current QC July 2025",
                    "audience": "marine_team",
                    "artifact_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Ocean Current QC July 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=ocean_current_v1; version=1.5; columns=current_speed|current_dir|std_dev | file.path=/features/ocean_current_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_OCEAN_CURRENT_2025-07; qc.figure_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf | stakeholder.output_label=Ocean Current QC July 2025; audience=marine_team; artifact_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1008",
        "instruction": "Handle the completion of ocean salinity feature QC for August-2025. End state: feature_set 'salinity_index_v1' (version '1.2') is documented with columns ['salinity_mean','salinity_max','salinity_std'] and remains accessible; feature file '/features/salinity_index_v1.parquet' is generated and available; a QC PDF is produced for label 'QC_SALINITY_INDEX_2025-08' with artifact_type 'pdf' and is obtainable; stakeholder output 'Salinity Index QC Aug 2025' (audience 'research_team') points to 'https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf' and is readable.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "salinity_index_v1",
                    "version": "1.2",
                    "columns": [
                        "salinity_mean",
                        "salinity_max",
                        "salinity_std"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "salinity_index_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/salinity_index_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/salinity_index_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SALINITY_INDEX_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SALINITY_INDEX_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SALINITY_INDEX_2025-08"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Index QC Aug 2025",
                    "audience": "research_team",
                    "artifact_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Index QC Aug 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=salinity_index_v1; version=1.2; columns=salinity_mean|salinity_max|salinity_std | file.path=/features/salinity_index_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_SALINITY_INDEX_2025-08; qc.figure_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf | stakeholder.output_label=Salinity Index QC Aug 2025; audience=research_team; artifact_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1010",
        "instruction": "Coordinate the onboarding of 'XGBoost_Rainfall_v1' and log a validation dataset for July-2025. End state: model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is saved; validation batch 'VAL_RAIN_2025-07' is documented with one entry ('2025-07-15T00:00:00Z', 124.3) and accessible; R\u00b2 score 0.93 is logged; a QC PDF report 'QC_RAIN_VAL_2025-07' is created and stored.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "model_type": "xgboost",
                    "framework": "xgboost",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_RAIN_2025-07",
                    "model_name": "XGBoost_Rainfall_v1",
                    "items": [
                        {
                            "timestamp": "2025-07-15T00:00:00Z",
                            "prediction": 124.3
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_RAIN_2025-07"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "metric_name": "R2",
                    "value": 0.93,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_VAL_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_VAL_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_VAL_2025-07"
                }
            }
        ],
        "outputs": [
                "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | pred.batch_name=VAL_RAIN_2025-07; pred.model=XGBoost_Rainfall_v1; rows=1; first_ts=2025-07-15T00:00:00Z; first_pred=124.3 | metric.model=XGBoost_Rainfall_v1; metric.name=R2; metric.value=0.93; split=validation | qc.figure_label=QC_RAIN_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1012",
        "instruction": "Set up a May-2025 model retrain window and confirm its validation. Final conditions: the project configuration should have retrain_window_start '2025-05-01T00:00:00Z' and retrain_window_end '2025-05-31T23:59:59Z' and be accessible; ensure the log event 'MODEL_RETRAIN_WINDOW_SET' appears with the message 'May retrain window applied.' and it is accessible; there must be a QC PDF with the label 'QC_CONFIG_RETRAIN_2025-05' stored as a figure record (artifact_type 'pdf') and accessible.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "retrain_window_start": "2025-05-01T00:00:00Z",
                        "retrain_window_end": "2025-05-31T23:59:59Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_start"
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_end"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET",
                    "message": "May retrain window applied."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-05"
                }
            }
        ],
        "outputs": [
                "config.retrain_window_start=2025-05-01T00:00:00Z; config.retrain_window_end=2025-05-31T23:59:59Z | log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=May retrain window applied. | qc.figure_label=QC_CONFIG_RETRAIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_1013",
        "instruction": "Set up a June-2025 model retrain window and confirm its validation. Final conditions: the project configuration should have retrain_window_start '2025-06-01T00:00:00Z' and retrain_window_end '2025-06-30T23:59:59Z' and be accessible; ensure the log event 'MODEL_RETRAIN_WINDOW_SET' appears with the message 'June retrain window applied.' and it is accessible; there must be a QC PDF with the label 'QC_CONFIG_RETRAIN_2025-06' stored as a figure record (artifact_type 'pdf') and accessible.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "retrain_window_start": "2025-06-01T00:00:00Z",
                        "retrain_window_end": "2025-06-30T23:59:59Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_start"
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_end"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET",
                    "message": "June retrain window applied."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-06"
                }
            }
        ],
        "outputs": [
                "config.retrain_window_start=2025-06-01T00:00:00Z; config.retrain_window_end=2025-06-30T23:59:59Z | log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=June retrain window applied. | qc.figure_label=QC_CONFIG_RETRAIN_2025-06; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_901",
        "instruction": "Establish a backfill cutoff for January-2026, check system readiness, and archive QC. Final condition: project config includes backfill_cutoff '2026-01-10T08:00:00Z'; terminal log shows 'BACKFILL_READY' with the message 'Early January backfill cutoff configured successfully.'; QC PDF 'QC_CONFIG_BACKFILL_2026-01.pdf' is archived.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "backfill_cutoff": "2026-01-10T08:00:00Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "backfill_cutoff"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_READY",
                    "message": "Early January backfill cutoff configured successfully."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "BACKFILL_READY"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2026-01"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2026-01",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_BACKFILL_2026-01"
                }
            }
        ],
        "outputs": [
                "config.backfill_cutoff=2026-01-10T08:00:00Z | log.event_type=BACKFILL_READY; log.message=Early January backfill cutoff configured successfully. | qc.figure_label=QC_CONFIG_BACKFILL_2026-01; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_903",
        "instruction": "Set up 'GradientBoosting_Wind_v3' and include a validation record for October-2025. Outcome: model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is added and visible; validation batch 'VAL_WD_2025-10' contains two entries [('2025-10-10T12:00:00Z', 15.3), ('2025-10-22T12:00:00Z', 14.8)] and is accessible; validation MAE 0.95 is stored and viewable; QC PNG labeled 'QC_WD_VAL_2025-10' is linked and available.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "GradientBoosting_Wind_v3",
                    "model_type": "gradient_boosting",
                    "framework": "sklearn",
                    "version": "3.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "GradientBoosting_Wind_v3"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_WD_2025-10",
                    "model_name": "GradientBoosting_Wind_v3",
                    "items": [
                        {
                            "timestamp": "2025-10-10T12:00:00Z",
                            "prediction": 15.3
                        },
                        {
                            "timestamp": "2025-10-22T12:00:00Z",
                            "prediction": 14.8
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_WD_2025-10"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "GradientBoosting_Wind_v3",
                    "metric_name": "MAE",
                    "value": 0.95,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "GradientBoosting_Wind_v3"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-10",
                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-10"
                }
            }
        ],
        "outputs": [
                "model.name=GradientBoosting_Wind_v3; type=gradient_boosting; framework=sklearn; version=3.0; status=staged | pred.batch_name=VAL_WD_2025-10; pred.model=GradientBoosting_Wind_v3; rows=2; first_ts=2025-10-10T12:00:00Z; first_pred=15.3 | metric.model=GradientBoosting_Wind_v3; metric.name=MAE; metric.value=0.95; split=validation | qc.figure_label=QC_WD_VAL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-10.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_906",
        "instruction": "Manage the publication of a sediment transport feature set 'sediment_transport_v3' for 2025\u201109. Desired outcome: feature set 'sediment_transport_v3' (version '3.0') with columns ['sediment_flux','current_speed','deposition_rate'] is documented and accessible; feature file '/features/sediment_transport_v3.parquet' is present and accessible; ensure a QC PDF for label 'QC_SEDIMENT_TRANSPORT_2025-09' is produced and stored (artifact_type 'pdf'); stakeholder output 'Sediment Transport Sep 2025' (audience 'internal') includes 'https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "sediment_transport_v3",
                    "version": "3.0",
                    "columns": [
                        "sediment_flux",
                        "current_speed",
                        "deposition_rate"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "sediment_transport_v3"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/sediment_transport_v3.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/sediment_transport_v3.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SEDIMENT_TRANSPORT_2025-09"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SEDIMENT_TRANSPORT_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SEDIMENT_TRANSPORT_2025-09"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Sediment Transport Sep 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Sediment Transport Sep 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=sediment_transport_v3; version=3.0; columns=sediment_flux|current_speed|deposition_rate | file.path=/features/sediment_transport_v3.parquet; file.mime=application/parquet | qc.figure_label=QC_SEDIMENT_TRANSPORT_2025-09; qc.figure_path=https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf | stakeholder.output_label=Sediment Transport Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_907",
        "instruction": "Coordinate the release of a coastal flood risk dataset 'flood_risk_v5' for 2025\u201110. Desired outcome: dataset 'flood_risk_v5' (version '5.0') with columns ['flood_probability','storm_surge_height','risk_index'] is documented and accessible; feature file '/features/flood_risk_v5.parquet' is present and accessible; ensure a QC PDF for label 'QC_FLOOD_RISK_2025-10' is produced and stored (artifact_type 'pdf'); stakeholder output 'Flood Risk Oct 2025' (audience 'internal') includes 'https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "flood_risk_v5",
                    "version": "5.0",
                    "columns": [
                        "flood_probability",
                        "storm_surge_height",
                        "risk_index"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "flood_risk_v5"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/flood_risk_v5.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/flood_risk_v5.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_RISK_2025-10"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_RISK_2025-10",
                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_RISK_2025-10"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Flood Risk Oct 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Flood Risk Oct 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=flood_risk_v5; version=5.0; columns=flood_probability|storm_surge_height|risk_index | file.path=/features/flood_risk_v5.parquet; file.mime=application/parquet | qc.figure_label=QC_FLOOD_RISK_2025-10; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf | stakeholder.output_label=Flood Risk Oct 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_908",
        "instruction": "Coordinate the release of a tidal variation dataset 'tidal_variation_v3' for 2025\u201111. End state: dataset 'tidal_variation_v3' (version '3.0') with columns ['high_tide','low_tide','tidal_range'] is recorded and readable; feature file '/features/tidal_variation_v3.parquet' exists and is readable; a QC PDF exists for label 'QC_TIDAL_VARIATION_2025-11' and is stored (artifact_type 'pdf'); stakeholder output 'Tidal Variation Nov 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf' and is readable.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "tidal_variation_v3",
                    "version": "3.0",
                    "columns": [
                        "high_tide",
                        "low_tide",
                        "tidal_range"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "tidal_variation_v3"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/tidal_variation_v3.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/tidal_variation_v3.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_VARIATION_2025-11"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_VARIATION_2025-11",
                    "figure_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_VARIATION_2025-11"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Tidal Variation Nov 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Tidal Variation Nov 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=tidal_variation_v3; version=3.0; columns=high_tide|low_tide|tidal_range | file.path=/features/tidal_variation_v3.parquet; file.mime=application/parquet | qc.figure_label=QC_TIDAL_VARIATION_2025-11; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf | stakeholder.output_label=Tidal Variation Nov 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_910",
        "instruction": "Carry out QC for a 40-year NOAA precipitation dataset. End state: processed series 'noaa_precip_qc_1980_2020' has summary points [('annual_avg', 1023.4), ('max_annual', 1820.1), ('min_annual', 540.2)] and is readable; a QC PDF exists for label 'QC_NOAA_PRECIP_1980_2020' and is stored (artifact_type 'pdf'); stakeholder output 'NOAA Precipitation QC 1980-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf' and is readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_precip_qc_1980_2020",
                    "items": [
                        {
                            "timestamp": "annual_avg",
                            "value": 1023.4
                        },
                        {
                            "timestamp": "max_annual",
                            "value": 1820.1
                        },
                        {
                            "timestamp": "min_annual",
                            "value": 540.2
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_precip_qc_1980_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_1980_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_1980_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_1980_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Precipitation QC 1980-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Precipitation QC 1980-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_precip_qc_1980_2020; points=3; p1.ts=annual_avg; p1.value=1023.4; p2.ts=max_annual; p2.value=1820.1; p3.ts=min_annual; p3.value=540.2 | qc.figure_label=QC_NOAA_PRECIP_1980_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf | stakeholder.output_label=NOAA Precipitation QC 1980-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_911",
        "instruction": "Handle a 20-year USGS groundwater level dataset for quality control. Final outcome: the series 'usgs_groundwater_qc_2005_2025' is processed with summary statistics [('mean_level', 15.7), ('lowest_level', 3.4), ('highest_level', 28.1)] and is accessible; a quality control PDF is available with the label 'QC_USGS_GW_2005_2025' and stored (artifact_type 'pdf'); the stakeholder report 'USGS Groundwater QC 2005-2025' (audience 'internal') points to 'https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "usgs_groundwater_qc_2005_2025",
                    "items": [
                        {
                            "timestamp": "mean_level",
                            "value": 15.7
                        },
                        {
                            "timestamp": "lowest_level",
                            "value": 3.4
                        },
                        {
                            "timestamp": "highest_level",
                            "value": 28.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "usgs_groundwater_qc_2005_2025"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_USGS_GW_2005_2025"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_USGS_GW_2005_2025",
                    "figure_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_USGS_GW_2005_2025"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "USGS Groundwater QC 2005-2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "USGS Groundwater QC 2005-2025"
                }
            }
        ],
        "outputs": [
                "series.name=usgs_groundwater_qc_2005_2025; points=3; p1.ts=mean_level; p1.value=15.7; p2.ts=lowest_level; p2.value=3.4; p3.ts=highest_level; p3.value=28.1 | qc.figure_label=QC_USGS_GW_2005_2025; qc.figure_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf | stakeholder.output_label=USGS Groundwater QC 2005-2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_913",
        "instruction": "Handle quality control for a Landsat-derived surface temperature dataset covering 1990\u20132020. Final state: the processed series 'landsat_surf_temp_qc_1990_2020' consists of [('avg_temp', 22.3), ('max_temp_day', 38.7), ('min_temp_day', -4.2)] and can be accessed; a quality control document (artifact_type 'pdf') with label 'QC_LANDSAT_TEMP_1990_2020' is available; the stakeholder report 'Landsat Surface Temp QC 1990-2020' (audience 'internal') links to 'https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "landsat_surf_temp_qc_1990_2020",
                    "items": [
                        {
                            "timestamp": "avg_temp",
                            "value": 22.3
                        },
                        {
                            "timestamp": "max_temp_day",
                            "value": 38.7
                        },
                        {
                            "timestamp": "min_temp_day",
                            "value": -4.2
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "landsat_surf_temp_qc_1990_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_LANDSAT_TEMP_1990_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_LANDSAT_TEMP_1990_2020",
                    "figure_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_LANDSAT_TEMP_1990_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Landsat Surface Temp QC 1990-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Landsat Surface Temp QC 1990-2020"
                }
            }
        ],
        "outputs": [
                "series.name=landsat_surf_temp_qc_1990_2020; points=3; p1.ts=avg_temp; p1.value=22.3; p2.ts=max_temp_day; p2.value=38.7; p3.ts=min_temp_day; p3.value=-4.2 | qc.figure_label=QC_LANDSAT_TEMP_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf | stakeholder.output_label=Landsat Surface Temp QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_914",
        "instruction": "Ensure the QC process for a TRMM satellite rainfall dataset from 1998 to 2018. Desired outcome: the processed dataset 'trmm_rainfall_qc_1998_2018' contains [('annual_avg', 105.7), ('max_daily_rain', 289.5), ('min_daily_rain', 0.0)] and is accessible; a QC report (artifact_type 'pdf') with the label 'QC_TRMM_RAINFALL_1998_2018' is available; stakeholder output 'TRMM Rainfall QC 1998-2018' (audience 'external') should link to 'https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "trmm_rainfall_qc_1998_2018",
                    "items": [
                        {
                            "timestamp": "annual_avg",
                            "value": 105.7
                        },
                        {
                            "timestamp": "max_daily_rain",
                            "value": 289.5
                        },
                        {
                            "timestamp": "min_daily_rain",
                            "value": 0.0
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "trmm_rainfall_qc_1998_2018"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TRMM_RAINFALL_1998_2018"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TRMM_RAINFALL_1998_2018",
                    "figure_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TRMM_RAINFALL_1998_2018"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "TRMM Rainfall QC 1998-2018",
                    "audience": "external",
                    "artifact_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "TRMM Rainfall QC 1998-2018"
                }
            }
        ],
        "outputs": [
                "series.name=trmm_rainfall_qc_1998_2018; points=3; p1.ts=annual_avg; p1.value=105.7; p2.ts=max_daily_rain; p2.value=289.5; p3.ts=min_daily_rain; p3.value=0.0 | qc.figure_label=QC_TRMM_RAINFALL_1998_2018; qc.figure_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf | stakeholder.output_label=TRMM Rainfall QC 1998-2018; audience=external; artifact_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_805",
        "instruction": "Set up a validation checkpoint for February 2026 and confirm readiness. Expected state: the project configuration includes a validation_checkpoint '2026-02-14T14:00:00Z' and is accessible; the terminal log records an event 'VALIDATION_CHECKPOINT_SET' with the message 'Validation checkpoint created for mid-February.' and is accessible; a QC PDF labeled 'QC_CONFIG_VALIDATION_2026-02' with a stored figure record (artifact_type 'pdf') is accessible.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "validation_checkpoint": "2026-02-14T14:00:00Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "validation_checkpoint"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "VALIDATION_CHECKPOINT_SET",
                    "message": "Validation checkpoint created for mid-February."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "VALIDATION_CHECKPOINT_SET"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_VALIDATION_2026-02"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_VALIDATION_2026-02",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_VALIDATION_2026-02"
                }
            }
        ],
        "outputs": [
                "config.validation_checkpoint=2026-02-14T14:00:00Z | log.event_type=VALIDATION_CHECKPOINT_SET; log.message=Validation checkpoint created for mid-February. | qc.figure_label=QC_CONFIG_VALIDATION_2026-02; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_701",
        "instruction": "Handle the publication of the May-2025 precipitation anomaly series with QC validation. End state: processed series 'precip_anom_2025-05' has three points [('2025-05-02T00:00:00Z', -12.5), ('2025-05-18T00:00:00Z', 8.3), ('2025-05-29T00:00:00Z', 3.1)] and is readable; a QC PDF exists for label 'QC_PRECIP_ANOM_2025-05' and is stored in artifact_type 'pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_anom_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-02T00:00:00Z",
                            "value": -12.5
                        },
                        {
                            "timestamp": "2025-05-18T00:00:00Z",
                            "value": 8.3
                        },
                        {
                            "timestamp": "2025-05-29T00:00:00Z",
                            "value": 3.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_anom_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-05"
                }
            }
        ],
        "outputs": [
                "series.name=precip_anom_2025-05; points=3; p1.ts=2025-05-02T00:00:00Z; p1.value=-12.5; p2.ts=2025-05-18T00:00:00Z; p2.value=8.3; p3.ts=2025-05-29T00:00:00Z; p3.value=3.1 | qc.figure_label=QC_PRECIP_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_702",
        "instruction": "Coordinate the publication of the June-2025 sea-level anomaly series with QC validation. End state: processed series 'sea_lvl_anom_2025-06' has three points [('2025-06-04T00:00:00Z', 0.12), ('2025-06-14T00:00:00Z', -0.05), ('2025-06-25T00:00:00Z', 0.22)] and is readable; a QC PDF exists for label 'QC_SEA_LVL_ANOM_2025-06' and is stored in artifact_type 'pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sea_lvl_anom_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-04T00:00:00Z",
                            "value": 0.12
                        },
                        {
                            "timestamp": "2025-06-14T00:00:00Z",
                            "value": -0.05
                        },
                        {
                            "timestamp": "2025-06-25T00:00:00Z",
                            "value": 0.22
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sea_lvl_anom_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SEA_LVL_ANOM_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SEA_LVL_ANOM_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SEA_LVL_ANOM_2025-06"
                }
            }
        ],
        "outputs": [
                "series.name=sea_lvl_anom_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=0.12; p2.ts=2025-06-14T00:00:00Z; p2.value=-0.05; p3.ts=2025-06-25T00:00:00Z; p3.value=0.22 | qc.figure_label=QC_SEA_LVL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_703",
        "instruction": "Handle the publication of the July-2025 wind-speed anomaly series, ensuring QC validation is completed. Final state: the processed series 'windspd_anom_2025-07' contains three points [('2025-07-07T00:00:00Z', 2.5), ('2025-07-16T00:00:00Z', -1.8), ('2025-07-28T00:00:00Z', 0.9)] and is accessible; a QC PDF labeled 'QC_WINDSPD_ANOM_2025-07' is available and saved under artifact_type 'pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "windspd_anom_2025-07",
                    "items": [
                        {
                            "timestamp": "2025-07-07T00:00:00Z",
                            "value": 2.5
                        },
                        {
                            "timestamp": "2025-07-16T00:00:00Z",
                            "value": -1.8
                        },
                        {
                            "timestamp": "2025-07-28T00:00:00Z",
                            "value": 0.9
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "windspd_anom_2025-07"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WINDSPD_ANOM_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WINDSPD_ANOM_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WINDSPD_ANOM_2025-07"
                }
            }
        ],
        "outputs": [
                "series.name=windspd_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=2.5; p2.ts=2025-07-16T00:00:00Z; p2.value=-1.8; p3.ts=2025-07-28T00:00:00Z; p3.value=0.9 | qc.figure_label=QC_WINDSPD_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_704",
        "instruction": "Handle the publication of the August-2025 humidity anomaly series with the required QC validation. Final state: the processed series 'humid_anom_2025-08' consists of three points [('2025-08-03T00:00:00Z', 4.0), ('2025-08-14T00:00:00Z', -2.7), ('2025-08-26T00:00:00Z', 1.5)] and is accessible; a QC PDF labeled 'QC_HUMID_ANOM_2025-08' is available and filed in artifact_type 'pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "humid_anom_2025-08",
                    "items": [
                        {
                            "timestamp": "2025-08-03T00:00:00Z",
                            "value": 4.0
                        },
                        {
                            "timestamp": "2025-08-14T00:00:00Z",
                            "value": -2.7
                        },
                        {
                            "timestamp": "2025-08-26T00:00:00Z",
                            "value": 1.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "humid_anom_2025-08"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_HUMID_ANOM_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_HUMID_ANOM_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_HUMID_ANOM_2025-08"
                }
            }
        ],
        "outputs": [
                "series.name=humid_anom_2025-08; points=3; p1.ts=2025-08-03T00:00:00Z; p1.value=4.0; p2.ts=2025-08-14T00:00:00Z; p2.value=-2.7; p3.ts=2025-08-26T00:00:00Z; p3.value=1.5 | qc.figure_label=QC_HUMID_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_705",
        "instruction": "Handle the registration of 'LSTM_Flood_v2' including validation metrics and model configuration. End state: model 'LSTM_Flood_v2' (type 'rnn', framework 'tensorflow', version '2.0', status 'staged') is recorded and readable; model_config 'seq_default' has hidden_units 128, dropout 0.3, and layers 3 and is readable; validation Accuracy 0.902 is stored and readable; artifact '/models/LSTM_Flood_v2_v2.0.h5' exists and is readable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "LSTM_Flood_v2",
                    "model_type": "rnn",
                    "framework": "tensorflow",
                    "version": "2.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "LSTM_Flood_v2"
                },
            },
            {
                "name": "UpsertModelConfig",
                "arguments": {
                    "model_name": "LSTM_Flood_v2",
                    "config_name": "seq_default",
                    "params": {
                        "hidden_units": 128,
                        "dropout": 0.3,
                        "layers": 3
                    }
                },
            },
            {
                "name": "GetModelConfig",
                "arguments": {
                    "model_name": "LSTM_Flood_v2",
                    "config_name": "seq_default"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "LSTM_Flood_v2",
                    "metric_name": "Accuracy",
                    "value": 0.902,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "LSTM_Flood_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/models/LSTM_Flood_v2_v2.0.h5",
                    "mime_type": "application/octet-stream"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/models/LSTM_Flood_v2_v2.0.h5"
                }
            }
        ],
        "outputs": [
                "model.name=LSTM_Flood_v2; type=rnn; framework=tensorflow; version=2.0; status=staged | config.model=LSTM_Flood_v2; config.name=seq_default; params.hidden_units=128; params.dropout=0.3; params.layers=3 | metric.model=LSTM_Flood_v2; metric.name=Accuracy; metric.value=0.902; split=validation | file.path=/models/LSTM_Flood_v2_v2.0.h5; file.mime=application/octet-stream"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_706",
        "instruction": "Coordinate the registration of 'Transformer_Climate_v3' along with artifacts and metrics. End state: model 'Transformer_Climate_v3' (type 'transformer', framework 'pytorch', version '3.1', status 'staged') is recorded and readable; model_config 'attention_default' has heads 8, d_model 256, and layers 6 and is readable; validation Loss 0.145 is stored and readable; artifact '/models/Transformer_Climate_v3_v3.1.pt' exists and is readable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "Transformer_Climate_v3",
                    "model_type": "transformer",
                    "framework": "pytorch",
                    "version": "3.1",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "Transformer_Climate_v3"
                },
            },
            {
                "name": "UpsertModelConfig",
                "arguments": {
                    "model_name": "Transformer_Climate_v3",
                    "config_name": "attention_default",
                    "params": {
                        "heads": 8,
                        "d_model": 256,
                        "layers": 6
                    }
                },
            },
            {
                "name": "GetModelConfig",
                "arguments": {
                    "model_name": "Transformer_Climate_v3",
                    "config_name": "attention_default"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "Transformer_Climate_v3",
                    "metric_name": "Loss",
                    "value": 0.145,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "Transformer_Climate_v3"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/models/Transformer_Climate_v3_v3.1.pt",
                    "mime_type": "application/octet-stream"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/models/Transformer_Climate_v3_v3.1.pt"
                }
            }
        ],
        "outputs": [
                "model.name=Transformer_Climate_v3; type=transformer; framework=pytorch; version=3.1; status=staged | config.model=Transformer_Climate_v3; config.name=attention_default; params.heads=8; params.d_model=256; params.layers=6 | metric.model=Transformer_Climate_v3; metric.name=Loss; metric.value=0.145; split=validation | file.path=/models/Transformer_Climate_v3_v3.1.pt; file.mime=application/octet-stream"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_708",
        "instruction": "Handle the registration of the surge-risk feature QC for April-2025. Final objective: the feature_set 'surge_risk_v2' (version '2.1') with the columns ['risk_index','exceedance_prob'] is logged and accessible; the feature file '/features/surge_risk_v2.parquet' is present and accessible; a QC PDF for the label 'QC_SURGE_RISK_2025-04' is available with the figure record stored (artifact_type 'pdf') and accessible; the output for stakeholders 'Surge Risk QC Apr 2025' (intended for 'regulators') cites 'https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "surge_risk_v2",
                    "version": "2.1",
                    "columns": [
                        "risk_index",
                        "exceedance_prob"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "surge_risk_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/surge_risk_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/surge_risk_v2.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RISK_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RISK_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RISK_2025-04"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Surge Risk QC Apr 2025",
                    "audience": "regulators",
                    "artifact_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Surge Risk QC Apr 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=surge_risk_v2; version=2.1; columns=risk_index|exceedance_prob | file.path=/features/surge_risk_v2.parquet; file.mime=application/parquet | qc.figure_label=QC_SURGE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf | stakeholder.output_label=Surge Risk QC Apr 2025; audience=regulators; artifact_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_709",
        "instruction": "Coordinate the completion of the wave-height anomaly feature QC for May-2025. Final condition: the feature_set 'wave_anomaly_v1' (version '1.3') with the columns ['hmean','hmax','stddev'] is recorded and accessible; the feature file '/features/wave_anomaly_v1.parquet' is available and accessible; a QC PDF for the label 'QC_WAVE_ANOMALY_2025-05' is created with the figure record stored (artifact_type 'pdf') and accessible; the stakeholder document 'Wave Anomaly QC May 2025' (for 'science_team') refers to 'https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "wave_anomaly_v1",
                    "version": "1.3",
                    "columns": [
                        "hmean",
                        "hmax",
                        "stddev"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "wave_anomaly_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/wave_anomaly_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/wave_anomaly_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOMALY_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOMALY_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOMALY_2025-05"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Wave Anomaly QC May 2025",
                    "audience": "science_team",
                    "artifact_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Wave Anomaly QC May 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=wave_anomaly_v1; version=1.3; columns=hmean|hmax|stddev | file.path=/features/wave_anomaly_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_WAVE_ANOMALY_2025-05; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf | stakeholder.output_label=Wave Anomaly QC May 2025; audience=science_team; artifact_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_710",
        "instruction": "Validate the rainfall-intensity feature quality control for June-2025. Desired outcome: feature_set 'rain_intensity_v3' (version '3.0') including columns ['avg_rate','peak_rate','duration'] is properly documented and accessible; feature file '/features/rain_intensity_v3.parquet' is present and accessible; a QC PDF for the label 'QC_RAIN_INTENSITY_2025-06' with a stored figure record (artifact_type 'pdf') is present and accessible; stakeholder document 'Rainfall Intensity QC Jun 2025' (intended for 'external_partners') links to 'https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "rain_intensity_v3",
                    "version": "3.0",
                    "columns": [
                        "avg_rate",
                        "peak_rate",
                        "duration"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "rain_intensity_v3"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/rain_intensity_v3.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/rain_intensity_v3.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_INTENSITY_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_INTENSITY_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_INTENSITY_2025-06"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall Intensity QC Jun 2025",
                    "audience": "external_partners",
                    "artifact_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall Intensity QC Jun 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=rain_intensity_v3; version=3.0; columns=avg_rate|peak_rate|duration | file.path=/features/rain_intensity_v3.parquet; file.mime=application/parquet | qc.figure_label=QC_RAIN_INTENSITY_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf | stakeholder.output_label=Rainfall Intensity QC Jun 2025; audience=external_partners; artifact_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_714",
        "instruction": "Set up the model retrain window for April-2025 and confirm its accuracy. Desired outcome: project configuration includes retrain_window_start '2025-04-01T00:00:00Z' and retrain_window_end '2025-04-30T23:59:59Z' and is accessible; terminal log event 'MODEL_RETRAIN_WINDOW_SET' with the message 'April retrain window applied.' is present and accessible; a QC PDF for the label 'QC_CONFIG_RETRAIN_2025-04' with a stored figure record (artifact_type 'pdf') is present and accessible.",
        "actions": [
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "retrain_window_start": "2025-04-01T00:00:00Z",
                        "retrain_window_end": "2025-04-30T23:59:59Z"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_start"
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "retrain_window_end"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET",
                    "message": "April retrain window applied."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "MODEL_RETRAIN_WINDOW_SET"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CONFIG_RETRAIN_2025-04"
                }
            }
        ],
        "outputs": [
                "config.retrain_window_start=2025-04-01T00:00:00Z; config.retrain_window_end=2025-04-30T23:59:59Z | log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=April retrain window applied. | qc.figure_label=QC_CONFIG_RETRAIN_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_600",
        "instruction": "Handle the publication of a September-2025 sea-surface temperature anomaly series with QC. End state: processed series 'sst_anom_2025-09' has three points [('2025-09-03T00:00:00Z', 0.25), ('2025-09-15T00:00:00Z', -0.12), ('2025-09-28T00:00:00Z', 0.08)] and is readable; a QC PDF exists for label 'QC_SST_ANOM_2025-09' and is readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sst_anom_2025-09",
                    "items": [
                        {
                            "timestamp": "2025-09-03T00:00:00Z",
                            "value": 0.25
                        },
                        {
                            "timestamp": "2025-09-15T00:00:00Z",
                            "value": -0.12
                        },
                        {
                            "timestamp": "2025-09-28T00:00:00Z",
                            "value": 0.08
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sst_anom_2025-09"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-09"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-09"
                }
            }
        ],
        "outputs": [
                "series.name=sst_anom_2025-09; points=3; p1.ts=2025-09-03T00:00:00Z; p1.value=0.25; p2.ts=2025-09-15T00:00:00Z; p2.value=-0.12; p3.ts=2025-09-28T00:00:00Z; p3.value=0.08 | qc.figure_label=QC_SST_ANOM_2025-09; qc.figure_path=https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_601",
        "instruction": "Coordinate the publication of an October-2025 chlorophyll anomaly series with QC. End state: processed series 'chl_anom_2025-10' has three points [('2025-10-01T00:00:00Z', 1.15), ('2025-10-12T00:00:00Z', -0.95), ('2025-10-25T00:00:00Z', 0.60)] and is readable; a QC PDF exists for label 'QC_CHL_ANOM_2025-10' and is readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "chl_anom_2025-10",
                    "items": [
                        {
                            "timestamp": "2025-10-01T00:00:00Z",
                            "value": 1.15
                        },
                        {
                            "timestamp": "2025-10-12T00:00:00Z",
                            "value": -0.95
                        },
                        {
                            "timestamp": "2025-10-25T00:00:00Z",
                            "value": 0.6
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "chl_anom_2025-10"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CHL_ANOM_2025-10"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CHL_ANOM_2025-10",
                    "figure_path": "https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CHL_ANOM_2025-10"
                }
            }
        ],
        "outputs": [
                "series.name=chl_anom_2025-10; points=3; p1.ts=2025-10-01T00:00:00Z; p1.value=1.15; p2.ts=2025-10-12T00:00:00Z; p2.value=-0.95; p3.ts=2025-10-25T00:00:00Z; p3.value=0.60 | qc.figure_label=QC_CHL_ANOM_2025-10; qc.figure_path=https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_602",
        "instruction": "Handle the publication of a November-2025 nitrate concentration anomaly series with QC. End state: processed series 'no3_anom_2025-11' has three points [('2025-11-05T00:00:00Z', 0.55), ('2025-11-16T00:00:00Z', -0.40), ('2025-11-29T00:00:00Z', 0.22)] and is readable; a QC PDF exists for label 'QC_NO3_ANOM_2025-11' and is readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "no3_anom_2025-11",
                    "items": [
                        {
                            "timestamp": "2025-11-05T00:00:00Z",
                            "value": 0.55
                        },
                        {
                            "timestamp": "2025-11-16T00:00:00Z",
                            "value": -0.4
                        },
                        {
                            "timestamp": "2025-11-29T00:00:00Z",
                            "value": 0.22
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "no3_anom_2025-11"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NO3_ANOM_2025-11"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NO3_ANOM_2025-11",
                    "figure_path": "https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NO3_ANOM_2025-11"
                }
            }
        ],
        "outputs": [
                "series.name=no3_anom_2025-11; points=3; p1.ts=2025-11-05T00:00:00Z; p1.value=0.55; p2.ts=2025-11-16T00:00:00Z; p2.value=-0.40; p3.ts=2025-11-29T00:00:00Z; p3.value=0.22 | qc.figure_label=QC_NO3_ANOM_2025-11; qc.figure_path=https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_603",
        "instruction": "Coordinate the curation and activation of feature set 'port_departure_metrics_v1' version 1.1. End state: feature_set 'port_departure_metrics_v1' with columns ['departure_count','avg_wait_time','max_wait_time'] is recorded; feature file '/features/port_departure_metrics_v1.parquet' exists and is readable; project config 'active_feature_set' equals 'port_departure_metrics_v1'; a QC PDF exists for label 'QC_PORT_DEPARTURE_2025-03' and is readable.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "port_departure_metrics_v1",
                    "version": "1.1",
                    "columns": [
                        "departure_count",
                        "avg_wait_time",
                        "max_wait_time"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "port_departure_metrics_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/port_departure_metrics_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/port_departure_metrics_v1.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "port_departure_metrics_v1"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_PORT_DEPARTURE_2025-03"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PORT_DEPARTURE_2025-03",
                    "figure_path": "https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PORT_DEPARTURE_2025-03"
                }
            }
        ],
        "outputs": [
                "feature_set.name=port_departure_metrics_v1; version=1.1; columns=departure_count|avg_wait_time|max_wait_time | file.path=/features/port_departure_metrics_v1.parquet; file.mime=application/parquet | config.active_feature_set=port_departure_metrics_v1 | qc.figure_label=QC_PORT_DEPARTURE_2025-03; qc.figure_path=https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_606",
        "instruction": "Manage the creation of a logistic regression wildfire risk dataset 'wildfire_risk_v1' for 2025\u201106. End state: dataset 'wildfire_risk_v1' (version '1.0') with columns ['temperature','humidity','fire_risk'] is documented and accessible; feature file '/features/wildfire_risk_v1.parquet' is present and accessible; a QC PDF exists for label 'QC_WILDFIRE_RISK_2025-06' with a figure record that is stored (artifact_type 'pdf') and accessible; stakeholder output 'Wildfire Risk Jun 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "wildfire_risk_v1",
                    "version": "1.0",
                    "columns": [
                        "temperature",
                        "humidity",
                        "fire_risk"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "wildfire_risk_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/wildfire_risk_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/wildfire_risk_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WILDFIRE_RISK_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WILDFIRE_RISK_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WILDFIRE_RISK_2025-06"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Wildfire Risk Jun 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Wildfire Risk Jun 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=wildfire_risk_v1; version=1.0; columns=temperature|humidity|fire_risk | file.path=/features/wildfire_risk_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_WILDFIRE_RISK_2025-06; qc.figure_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf | stakeholder.output_label=Wildfire Risk Jun 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_607",
        "instruction": "Facilitate the publication of a flood prediction dataset 'flood_forecast_v2' for 2025\u201105. End state: dataset 'flood_forecast_v2' (version '2.0') with columns ['rainfall','river_level','flood_probability'] is documented and accessible; feature file '/features/flood_forecast_v2.parquet' is present and readable; a QC PDF exists for label 'QC_FLOOD_FORECAST_2025-05' and is stored (artifact_type 'pdf'); stakeholder output 'Flood Forecast May 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "flood_forecast_v2",
                    "version": "2.0",
                    "columns": [
                        "rainfall",
                        "river_level",
                        "flood_probability"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "flood_forecast_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/flood_forecast_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/flood_forecast_v2.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_FORECAST_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_FORECAST_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOOD_FORECAST_2025-05"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Flood Forecast May 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Flood Forecast May 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=flood_forecast_v2; version=2.0; columns=rainfall|river_level|flood_probability | file.path=/features/flood_forecast_v2.parquet; file.mime=application/parquet | qc.figure_label=QC_FLOOD_FORECAST_2025-05; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf | stakeholder.output_label=Flood Forecast May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_608",
        "instruction": "Handle the curation of the air quality prediction dataset 'air_quality_index_v3' for 2025-07. Final outcome: the dataset 'air_quality_index_v3' (version '3.0') with columns ['PM2_5','PM10','AQI'] is documented and accessible; the feature file '/features/air_quality_index_v3.parquet' is present and can be accessed; a QC PDF for the label 'QC_AIR_QUALITY_2025-07' is available and stored (artifact_type 'pdf'); the stakeholder output 'Air Quality Jul 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "air_quality_index_v3",
                    "version": "3.0",
                    "columns": [
                        "PM2_5",
                        "PM10",
                        "AQI"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "air_quality_index_v3"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/air_quality_index_v3.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/air_quality_index_v3.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_AIR_QUALITY_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_AIR_QUALITY_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_AIR_QUALITY_2025-07"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Air Quality Jul 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Air Quality Jul 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=air_quality_index_v3; version=3.0; columns=PM2_5|PM10|AQI | file.path=/features/air_quality_index_v3.parquet; file.mime=application/parquet | qc.figure_label=QC_AIR_QUALITY_2025-07; qc.figure_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf | stakeholder.output_label=Air Quality Jul 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_609",
        "instruction": "Coordinate the publication of a coastal erosion prediction dataset 'coastal_erosion_v2' for 2025-08. Final outcome: the dataset 'coastal_erosion_v2' (version '2.0') with columns ['wave_height','shoreline_change','erosion_risk'] is documented and accessible; the feature file '/features/coastal_erosion_v2.parquet' is present and can be accessed; a QC PDF for the label 'QC_COASTAL_EROSION_2025-08' is available and stored (artifact_type 'pdf'); the stakeholder output 'Coastal Erosion Aug 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "coastal_erosion_v2",
                    "version": "2.0",
                    "columns": [
                        "wave_height",
                        "shoreline_change",
                        "erosion_risk"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "coastal_erosion_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/coastal_erosion_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/coastal_erosion_v2.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_EROSION_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_EROSION_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_EROSION_2025-08"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Coastal Erosion Aug 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Coastal Erosion Aug 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=coastal_erosion_v2; version=2.0; columns=wave_height|shoreline_change|erosion_risk | file.path=/features/coastal_erosion_v2.parquet; file.mime=application/parquet | qc.figure_label=QC_COASTAL_EROSION_2025-08; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf | stakeholder.output_label=Coastal Erosion Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_610",
        "instruction": "Coordinate the preparation of May-2025 tidal minima, verify QC, and publish a summary for coastal authorities. End state: processed series 'tide_min_2025-05' stores three points [('2025-05-03T00:00:00Z', 0.45), ('2025-05-17T00:00:00Z', 0.32), ('2025-05-30T00:00:00Z', 0.50)] and is retrievable; a QC figure 'QC_TIDE_MIN_2025-05' (artifact_type 'pdf') is stored and accessible; stakeholder output 'May 2025 Tide Min Report' (audience 'coastal') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_min_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-03T00:00:00Z",
                            "value": 0.45
                        },
                        {
                            "timestamp": "2025-05-17T00:00:00Z",
                            "value": 0.32
                        },
                        {
                            "timestamp": "2025-05-30T00:00:00Z",
                            "value": 0.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_min_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "May 2025 Tide Min Report",
                    "audience": "coastal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "May 2025 Tide Min Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_min_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=0.45; p2.ts=2025-05-17T00:00:00Z; p2.value=0.32; p3.ts=2025-05-30T00:00:00Z; p3.value=0.50 | qc.figure_label=QC_TIDE_MIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf | stakeholder.output_label=May 2025 Tide Min Report; audience=coastal; artifact_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_611",
        "instruction": "Handle the processing of June-2025 high tide series, validate QC, and release an executive briefing. End state: processed series 'tide_high_2025-06' stores three points [('2025-06-01T00:00:00Z', 3.55), ('2025-06-14T00:00:00Z', 3.78), ('2025-06-28T00:00:00Z', 3.61)] and is retrievable; a QC figure 'QC_TIDE_HIGH_2025-06' (artifact_type 'pdf') is stored and accessible; stakeholder output 'June 2025 Tide High Report' (audience 'executive') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_high_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-01T00:00:00Z",
                            "value": 3.55
                        },
                        {
                            "timestamp": "2025-06-14T00:00:00Z",
                            "value": 3.78
                        },
                        {
                            "timestamp": "2025-06-28T00:00:00Z",
                            "value": 3.61
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_high_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "June 2025 Tide High Report",
                    "audience": "executive",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "June 2025 Tide High Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_high_2025-06; points=3; p1.ts=2025-06-01T00:00:00Z; p1.value=3.55; p2.ts=2025-06-14T00:00:00Z; p2.value=3.78; p3.ts=2025-06-28T00:00:00Z; p3.value=3.61 | qc.figure_label=QC_TIDE_HIGH_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf | stakeholder.output_label=June 2025 Tide High Report; audience=executive; artifact_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_612",
        "instruction": "Handle the compilation of July-2025 tidal range data, ensure QC completion, and disseminate a municipal briefing. Final outcome: processed series 'tide_range_2025-07' contains three points [('2025-07-05T00:00:00Z', 2.67), ('2025-07-18T00:00:00Z', 3.02), ('2025-07-31T00:00:00Z', 2.88)] and is retrievable; a QC figure 'QC_TIDE_RANGE_2025-07' (artifact_type 'pdf') is stored and accessible; stakeholder output 'July 2025 Tide Range Report' (audience 'municipal') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_range_2025-07",
                    "items": [
                        {
                            "timestamp": "2025-07-05T00:00:00Z",
                            "value": 2.67
                        },
                        {
                            "timestamp": "2025-07-18T00:00:00Z",
                            "value": 3.02
                        },
                        {
                            "timestamp": "2025-07-31T00:00:00Z",
                            "value": 2.88
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_range_2025-07"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "July 2025 Tide Range Report",
                    "audience": "municipal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "July 2025 Tide Range Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_range_2025-07; points=3; p1.ts=2025-07-05T00:00:00Z; p1.value=2.67; p2.ts=2025-07-18T00:00:00Z; p2.value=3.02; p3.ts=2025-07-31T00:00:00Z; p3.value=2.88 | qc.figure_label=QC_TIDE_RANGE_2025-07; qc.figure_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf | stakeholder.output_label=July 2025 Tide Range Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_613",
        "instruction": "Coordinate the generation of August-2025 mean tide series, check QC, and share a briefing with state agencies. Final outcome: processed series 'tide_mean_2025-08' contains three points [('2025-08-04T00:00:00Z', 1.87), ('2025-08-17T00:00:00Z', 2.01), ('2025-08-30T00:00:00Z', 1.95)] and is retrievable; a QC figure 'QC_TIDE_MEAN_2025-08' (artifact_type 'pdf') is stored and accessible; stakeholder output 'August 2025 Mean Tide Report' (audience 'state') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_mean_2025-08",
                    "items": [
                        {
                            "timestamp": "2025-08-04T00:00:00Z",
                            "value": 1.87
                        },
                        {
                            "timestamp": "2025-08-17T00:00:00Z",
                            "value": 2.01
                        },
                        {
                            "timestamp": "2025-08-30T00:00:00Z",
                            "value": 1.95
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_mean_2025-08"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MEAN_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MEAN_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MEAN_2025-08"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "August 2025 Mean Tide Report",
                    "audience": "state",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "August 2025 Mean Tide Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_mean_2025-08; points=3; p1.ts=2025-08-04T00:00:00Z; p1.value=1.87; p2.ts=2025-08-17T00:00:00Z; p2.value=2.01; p3.ts=2025-08-30T00:00:00Z; p3.value=1.95 | qc.figure_label=QC_TIDE_MEAN_2025-08; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf | stakeholder.output_label=August 2025 Mean Tide Report; audience=state; artifact_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_614",
        "instruction": "Handle the preparation of May-2025 tidal minima, verify QC, and distribute a briefing for coastal management. End state: processed series 'tide_min_2025-05' stores three points [('2025-05-03T00:00:00Z', 0.42), ('2025-05-16T00:00:00Z', 0.35), ('2025-05-29T00:00:00Z', 0.50)] and is retrievable; a QC figure 'QC_TIDE_MIN_2025-05' (artifact_type 'pdf') is stored and accessible; stakeholder output 'May 2025 Tide Min Report' (audience 'coastal') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_min_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-03T00:00:00Z",
                            "value": 0.42
                        },
                        {
                            "timestamp": "2025-05-16T00:00:00Z",
                            "value": 0.35
                        },
                        {
                            "timestamp": "2025-05-29T00:00:00Z",
                            "value": 0.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_min_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MIN_2025-05"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "May 2025 Tide Min Report",
                    "audience": "coastal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "May 2025 Tide Min Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_min_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=0.42; p2.ts=2025-05-16T00:00:00Z; p2.value=0.35; p3.ts=2025-05-29T00:00:00Z; p3.value=0.50 | qc.figure_label=QC_TIDE_MIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf | stakeholder.output_label=May 2025 Tide Min Report; audience=coastal; artifact_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_615",
        "instruction": "Coordinate the preparation of the June-2025 high tide series, conduct QC validation, and issue an executive briefing. End state: processed series 'tide_high_2025-06' stores three points [('2025-06-02T00:00:00Z', 3.55), ('2025-06-15T00:00:00Z', 3.78), ('2025-06-28T00:00:00Z', 3.60)] and is retrievable; a QC figure 'QC_TIDE_HIGH_2025-06' (artifact_type 'pdf') is stored and accessible; stakeholder output 'June 2025 Tide High Report' (audience 'executive') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_high_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-02T00:00:00Z",
                            "value": 3.55
                        },
                        {
                            "timestamp": "2025-06-15T00:00:00Z",
                            "value": 3.78
                        },
                        {
                            "timestamp": "2025-06-28T00:00:00Z",
                            "value": 3.6
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_high_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_HIGH_2025-06"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "June 2025 Tide High Report",
                    "audience": "executive",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "June 2025 Tide High Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_high_2025-06; points=3; p1.ts=2025-06-02T00:00:00Z; p1.value=3.55; p2.ts=2025-06-15T00:00:00Z; p2.value=3.78; p3.ts=2025-06-28T00:00:00Z; p3.value=3.60 | qc.figure_label=QC_TIDE_HIGH_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf | stakeholder.output_label=June 2025 Tide High Report; audience=executive; artifact_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_616",
        "instruction": "Handle the generation of the July-2025 tidal range series, perform quality control, and disseminate a municipal briefing. End state: the processed series 'tide_range_2025-07' includes three data points [('2025-07-04T00:00:00Z', 2.65), ('2025-07-17T00:00:00Z', 3.01), ('2025-07-30T00:00:00Z', 2.87)] and remains accessible; a quality control document 'QC_TIDE_RANGE_2025-07' (artifact_type 'pdf') is stored and available; the stakeholder output 'July 2025 Tide Range Report' (audience 'municipal') is associated with the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_range_2025-07",
                    "items": [
                        {
                            "timestamp": "2025-07-04T00:00:00Z",
                            "value": 2.65
                        },
                        {
                            "timestamp": "2025-07-17T00:00:00Z",
                            "value": 3.01
                        },
                        {
                            "timestamp": "2025-07-30T00:00:00Z",
                            "value": 2.87
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_range_2025-07"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_RANGE_2025-07"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "July 2025 Tide Range Report",
                    "audience": "municipal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "July 2025 Tide Range Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_range_2025-07; points=3; p1.ts=2025-07-04T00:00:00Z; p1.value=2.65; p2.ts=2025-07-17T00:00:00Z; p2.value=3.01; p3.ts=2025-07-30T00:00:00Z; p3.value=2.87 | qc.figure_label=QC_TIDE_RANGE_2025-07; qc.figure_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf | stakeholder.output_label=July 2025 Tide Range Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_514",
        "instruction": "Coordinate quality control for a 25-year NOAA coastal wind dataset. End state: the processed series 'noaa_wind_qc_1995_2020' contains summary points [('mean_wind_speed', 12.4), ('max_wind_speed', 29.8)] and is accessible; a QC PDF is available for label 'QC_NOAA_WIND_1995_2020' and is stored (artifact_type 'pdf'); the stakeholder output 'NOAA Wind QC 1995-2020' (audience 'internal') links to 'https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_wind_qc_1995_2020",
                    "items": [
                        {
                            "timestamp": "mean_wind_speed",
                            "value": 12.4
                        },
                        {
                            "timestamp": "max_wind_speed",
                            "value": 29.8
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_wind_qc_1995_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_WIND_1995_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_WIND_1995_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_WIND_1995_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Wind QC 1995-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Wind QC 1995-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_wind_qc_1995_2020; points=2; p1.ts=mean_wind_speed; p1.value=12.4; p2.ts=max_wind_speed; p2.value=29.8 | qc.figure_label=QC_NOAA_WIND_1995_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf | stakeholder.output_label=NOAA Wind QC 1995-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_515",
        "instruction": "Handle a quality check for a 20-year NOAA river discharge dataset. Final goal: the processed series 'noaa_river_qc_2000_2020' contains summary points [('mean_discharge', 350.6), ('max_discharge', 1120.3)] and is accessible; a QC PDF labeled 'QC_NOAA_RIVER_2000_2020' is available and stored (artifact_type 'pdf'); the stakeholder document 'NOAA River QC 2000-2020' (audience 'internal') links to 'https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf' and can be accessed.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_river_qc_2000_2020",
                    "items": [
                        {
                            "timestamp": "mean_discharge",
                            "value": 350.6
                        },
                        {
                            "timestamp": "max_discharge",
                            "value": 1120.3
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_river_qc_2000_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_RIVER_2000_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_RIVER_2000_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_RIVER_2000_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA River QC 2000-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA River QC 2000-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_river_qc_2000_2020; points=2; p1.ts=mean_discharge; p1.value=350.6; p2.ts=max_discharge; p2.value=1120.3 | qc.figure_label=QC_NOAA_RIVER_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf | stakeholder.output_label=NOAA River QC 2000-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_516",
        "instruction": "Coordinate a quality check for a 15-year NOAA precipitation dataset. Final goal: the processed series 'noaa_precip_qc_2005_2020' contains summary points [('mean_precip', 102.7), ('max_precip_day', 210.5)] and is accessible; a QC PDF labeled 'QC_NOAA_PRECIP_2005_2020' is available and stored (artifact_type 'pdf'); the stakeholder document 'NOAA Precip QC 2005-2020' (audience 'internal') links to 'https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf' and can be accessed.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_precip_qc_2005_2020",
                    "items": [
                        {
                            "timestamp": "mean_precip",
                            "value": 102.7
                        },
                        {
                            "timestamp": "max_precip_day",
                            "value": 210.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_precip_qc_2005_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_2005_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_2005_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_PRECIP_2005_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Precip QC 2005-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Precip QC 2005-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_precip_qc_2005_2020; points=2; p1.ts=mean_precip; p1.value=102.7; p2.ts=max_precip_day; p2.value=210.5 | qc.figure_label=QC_NOAA_PRECIP_2005_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf | stakeholder.output_label=NOAA Precip QC 2005-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_517",
        "instruction": "Coordinate the QC process for a 10-year NOAA salinity dataset. End state: the processed series 'noaa_salinity_qc_2010_2020' includes summary points [('mean_salinity', 35.1), ('max_salinity', 36.7)] and is accessible; a QC PDF is available under the label 'QC_NOAA_SALINITY_2010_2020' and is stored (artifact_type 'pdf'); stakeholder output 'NOAA Salinity QC 2010-2020' (audience 'internal') refers to 'https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_salinity_qc_2010_2020",
                    "items": [
                        {
                            "timestamp": "mean_salinity",
                            "value": 35.1
                        },
                        {
                            "timestamp": "max_salinity",
                            "value": 36.7
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_salinity_qc_2010_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SALINITY_2010_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SALINITY_2010_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SALINITY_2010_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Salinity QC 2010-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Salinity QC 2010-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_salinity_qc_2010_2020; points=2; p1.ts=mean_salinity; p1.value=35.1; p2.ts=max_salinity; p2.value=36.7 | qc.figure_label=QC_NOAA_SALINITY_2010_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf | stakeholder.output_label=NOAA Salinity QC 2010-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_518",
        "instruction": "Handle the QC process for a 12-year NOAA sea surface temperature dataset. End state: the processed series 'noaa_sst_qc_2008_2020' contains summary points [('mean_sst', 18.5), ('max_sst', 29.2)] and is accessible; a QC PDF is available with the label 'QC_NOAA_SST_2008_2020' and is stored (artifact_type 'pdf'); stakeholder output 'NOAA SST QC 2008-2020' (audience 'internal') offers a reference to 'https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_sst_qc_2008_2020",
                    "items": [
                        {
                            "timestamp": "mean_sst",
                            "value": 18.5
                        },
                        {
                            "timestamp": "max_sst",
                            "value": 29.2
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_sst_qc_2008_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SST_2008_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SST_2008_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_SST_2008_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA SST QC 2008-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA SST QC 2008-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_sst_qc_2008_2020; points=2; p1.ts=mean_sst; p1.value=18.5; p2.ts=max_sst; p2.value=29.2 | qc.figure_label=QC_NOAA_SST_2008_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf | stakeholder.output_label=NOAA SST QC 2008-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_411",
        "instruction": "Handle summarization of the April\u20112025 sales ETL run and inform the finance team. Final state: ETL run 'sales_rollup_2025-04' (task 'monthly_sales_aggregation') status 'completed' with rows_processed 420 is documented and accessible; a QC PDF with the label 'QC_SALES_2025-04' is filed and accessible; terminal log event 'SALES_QC_DONE' containing the message 'April sales aggregation complete.' is available and viewable; send an email to 'finance-team@example.com' with the subject 'QC_SALES_2025-04', body 'Sales aggregation QC attached.' and the attachment URL.",
        "actions": [
            {
                "name": "RegisterEtlRun",
                "arguments": {
                    "run_name": "sales_rollup_2025-04",
                    "task": "monthly_sales_aggregation",
                    "status": "completed",
                    "rows_processed": 420
                },
            },
            {
                "name": "GetEtlRunDetails",
                "arguments": {
                    "run_name": "sales_rollup_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SALES_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SALES_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_SALES_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SALES_2025-04"
                },
            },
            {
                "name": "RecordTerminalLog",
                "arguments": {
                    "event_type": "SALES_QC_DONE",
                    "message": "April sales aggregation complete."
                },
            },
            {
                "name": "ListTerminalLog",
                "arguments": {
                    "event_type": "SALES_QC_DONE"
                },
            },
            {
                "name": "SendResultsEmail",
                "arguments": {
                    "to_address": "finance-team@example.com",
                    "subject": "QC_SALES_2025-04",
                    "body_text": "Sales aggregation QC attached.",
                    "attachment": "https://storage.example.com/reports/QC_SALES_2025-04.pdf"
                }
            }
        ],
        "outputs": [
                "etl.run_name=sales_rollup_2025-04; etl.task=monthly_sales_aggregation; etl.status=completed; etl.rows_processed=420 | qc.figure_label=QC_SALES_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SALES_2025-04.pdf | log.event_type=SALES_QC_DONE; log.message=April sales aggregation complete. | email.to=finance-team@example.com; email.subject=QC_SALES_2025-04; email.attachment=https://storage.example.com/reports/QC_SALES_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_300",
        "instruction": "Coordinate compilation of January-2025 precipitation totals with a QC review and share a summary with external partners. Final outcome: the processed series 'precip_total_2025-01' contains three points [('2025-01-05T00:00:00Z', 14.2), ('2025-01-18T00:00:00Z', 9.7), ('2025-01-30T00:00:00Z', 12.5)] and is accessible; a QC report PDF titled 'QC_PRECIP_2025-01' is stored and accessible; the stakeholder output 'Jan 2025 Precipitation Summary' (audience 'external') includes a reference to the QC report.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_total_2025-01",
                    "items": [
                        {
                            "timestamp": "2025-01-05T00:00:00Z",
                            "value": 14.2
                        },
                        {
                            "timestamp": "2025-01-18T00:00:00Z",
                            "value": 9.7
                        },
                        {
                            "timestamp": "2025-01-30T00:00:00Z",
                            "value": 12.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_total_2025-01"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-01"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-01",
                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-01"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Jan 2025 Precipitation Summary",
                    "audience": "external",
                    "artifact_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Jan 2025 Precipitation Summary"
                }
            }
        ],
        "outputs": [
                "series.name=precip_total_2025-01; points=3; p1.ts=2025-01-05T00:00:00Z; p1.value=14.2; p2.ts=2025-01-18T00:00:00Z; p2.value=9.7; p3.ts=2025-01-30T00:00:00Z; p3.value=12.5 | qc.figure_label=QC_PRECIP_2025-01; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf | stakeholder.output_label=Jan 2025 Precipitation Summary; audience=external; artifact_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_302",
        "instruction": "Handle the preparation of April-2025 tidal height maxima, ensure quality control is verified, and disseminate a brief update to municipal stakeholders. End state: processed series 'tide_max_2025-04' stores three points [('2025-04-02T00:00:00Z', 3.12), ('2025-04-15T00:00:00Z', 3.44), ('2025-04-29T00:00:00Z', 3.21)] and is retrievable; a QC figure 'QC_TIDE_MAX_2025-04' (artifact_type 'pdf') is stored and accessible; stakeholder output 'April 2025 Tide Max Report' (audience 'municipal') is linked to the QC document.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_max_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-02T00:00:00Z",
                            "value": 3.12
                        },
                        {
                            "timestamp": "2025-04-15T00:00:00Z",
                            "value": 3.44
                        },
                        {
                            "timestamp": "2025-04-29T00:00:00Z",
                            "value": 3.21
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_max_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MAX_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MAX_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_MAX_2025-04"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "April 2025 Tide Max Report",
                    "audience": "municipal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "April 2025 Tide Max Report"
                }
            }
        ],
        "outputs": [
                "series.name=tide_max_2025-04; points=3; p1.ts=2025-04-02T00:00:00Z; p1.value=3.12; p2.ts=2025-04-15T00:00:00Z; p2.value=3.44; p3.ts=2025-04-29T00:00:00Z; p3.value=3.21 | qc.figure_label=QC_TIDE_MAX_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf | stakeholder.output_label=April 2025 Tide Max Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_305",
        "instruction": "Coordinate the quality control of a merged coastal wind speed dataset covering 1995\u20132015. End state: processed series 'wind_qc_1995_2015' includes [('avg_wind', 12.4), ('max_wind_day', 68.0)] and is retrievable; a QC report (artifact_type 'pdf') exists with label 'QC_WIND_1995_2015'; stakeholder output 'Wind QC 1995-2015' (audience 'internal') references 'https://storage.example.com/reports/QC_WIND_1995_2015.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "wind_qc_1995_2015",
                    "items": [
                        {
                            "timestamp": "avg_wind",
                            "value": 12.4
                        },
                        {
                            "timestamp": "max_wind_day",
                            "value": 68.0
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "wind_qc_1995_2015"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WIND_1995_2015"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WIND_1995_2015",
                    "figure_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WIND_1995_2015"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Wind QC 1995-2015",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Wind QC 1995-2015"
                }
            }
        ],
        "outputs": [
                "series.name=wind_qc_1995_2015; points=2; p1.ts=avg_wind; p1.value=12.4; p2.ts=max_wind_day; p2.value=68.0 | qc.figure_label=QC_WIND_1995_2015; qc.figure_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf | stakeholder.output_label=Wind QC 1995-2015; audience=internal; artifact_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_201",
        "instruction": "Handle the setup for 'LSTM_StormSurge_v3' and include a validation record for July-2025. End state: model 'LSTM_StormSurge_v3' (type 'lstm', framework 'tensorflow', version '3.0', status 'staged') is inserted and visible; validation batch 'VAL_SS_2025-07' contains one row ('2025-07-15T03:00:00Z', 1.92) and is retrievable; validation MAE 0.15 is stored and readable; QC CSV labeled 'QC_SS_VAL_2025-07' is linked and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "LSTM_StormSurge_v3",
                    "model_type": "lstm",
                    "framework": "tensorflow",
                    "version": "3.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "LSTM_StormSurge_v3"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_SS_2025-07",
                    "model_name": "LSTM_StormSurge_v3",
                    "items": [
                        {
                            "timestamp": "2025-07-15T03:00:00Z",
                            "prediction": 1.92
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_SS_2025-07"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "LSTM_StormSurge_v3",
                    "metric_name": "MAE",
                    "value": 0.15,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "LSTM_StormSurge_v3"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SS_VAL_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_SS_VAL_2025-07.csv",
                    "artifact_type": "csv"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SS_VAL_2025-07"
                }
            }
        ],
        "outputs": [
                "model.name=LSTM_StormSurge_v3; type=lstm; framework=tensorflow; version=3.0; status=staged | pred.batch_name=VAL_SS_2025-07; pred.model=LSTM_StormSurge_v3; rows=1; first_ts=2025-07-15T03:00:00Z; first_pred=1.92 | metric.model=LSTM_StormSurge_v3; metric.name=MAE; metric.value=0.15; split=validation | qc.figure_label=QC_SS_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_SS_VAL_2025-07.csv"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_202",
        "instruction": "Coordinate the configuration of 'ARIMA_Precip_v1' and incorporate a validation record for August-2025. End state: model 'ARIMA_Precip_v1' (type 'arima', framework 'statsmodels', version '1.0', status 'staged') is inserted and visible; validation batch 'VAL_PC_2025-08' comprises one row ('2025-08-05T12:00:00Z', 5.7) and is retrievable; validation R\u00b2 0.89 is stored and readable; QC PDF with label 'QC_PC_VAL_2025-08' is linked and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "ARIMA_Precip_v1",
                    "model_type": "arima",
                    "framework": "statsmodels",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "ARIMA_Precip_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_PC_2025-08",
                    "model_name": "ARIMA_Precip_v1",
                    "items": [
                        {
                            "timestamp": "2025-08-05T12:00:00Z",
                            "prediction": 5.7
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_PC_2025-08"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "ARIMA_Precip_v1",
                    "metric_name": "R2",
                    "value": 0.89,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "ARIMA_Precip_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PC_VAL_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PC_VAL_2025-08"
                }
            }
        ],
        "outputs": [
                "model.name=ARIMA_Precip_v1; type=arima; framework=statsmodels; version=1.0; status=staged | pred.batch_name=VAL_PC_2025-08; pred.model=ARIMA_Precip_v1; rows=1; first_ts=2025-08-05T12:00:00Z; first_pred=5.7 | metric.model=ARIMA_Precip_v1; metric.name=R2; metric.value=0.89; split=validation | qc.figure_label=QC_PC_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_203",
        "instruction": "Handle the configuration of 'RandomForest_Wind_v5' and incorporate a validation record for September 2025. Final state: The model 'RandomForest_Wind_v5' (type 'random_forest', framework 'sklearn', version '5.0', status 'staged') should be inserted and visible; the validation batch 'VAL_WD_2025-09' contains one entry ('2025-09-18T15:00:00Z', 12.6) and must be retrievable; validation RMSE 1.2 should be stored and readable; QC PNG labeled 'QC_WD_VAL_2025-09' is linked and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "RandomForest_Wind_v5",
                    "model_type": "random_forest",
                    "framework": "sklearn",
                    "version": "5.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "RandomForest_Wind_v5"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_WD_2025-09",
                    "model_name": "RandomForest_Wind_v5",
                    "items": [
                        {
                            "timestamp": "2025-09-18T15:00:00Z",
                            "prediction": 12.6
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_WD_2025-09"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "RandomForest_Wind_v5",
                    "metric_name": "RMSE",
                    "value": 1.2,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "RandomForest_Wind_v5"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-09.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-09"
                }
            }
        ],
        "outputs": [
                "model.name=RandomForest_Wind_v5; type=random_forest; framework=sklearn; version=5.0; status=staged | pred.batch_name=VAL_WD_2025-09; pred.model=RandomForest_Wind_v5; rows=1; first_ts=2025-09-18T15:00:00Z; first_pred=12.6 | metric.model=RandomForest_Wind_v5; metric.name=RMSE; metric.value=1.2; split=validation | qc.figure_label=QC_WD_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-09.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_206",
        "instruction": "Coordinate the curation of feature set 'precip_extremes_v1' (version '1.0') with columns ['daily_rainfall_max','monthly_rainfall_mean','extreme_event_count'] and ensure its activation. Final state: The feature set should be retrievable; the feature file '/features/precip_extremes_v1.parquet' needs to be present and valid; the project config 'climate_features' must match 'precip_extremes_v1'; QC report 'QC_PRECIP_2025-08' should exist as a PDF.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "precip_extremes_v1",
                    "version": "1.0",
                    "columns": [
                        "daily_rainfall_max",
                        "monthly_rainfall_mean",
                        "extreme_event_count"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "precip_extremes_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/precip_extremes_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/precip_extremes_v1.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "climate_features": "precip_extremes_v1"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "climate_features"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_2025-08"
                }
            }
        ],
        "outputs": [
                "feature_set.name=precip_extremes_v1; version=1.0; columns=daily_rainfall_max|monthly_rainfall_mean|extreme_event_count | file.path=/features/precip_extremes_v1.parquet; file.mime=application/parquet | config.climate_features=precip_extremes_v1 | qc.figure_label=QC_PRECIP_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_211",
        "instruction": "Handle the quality control of a merged satellite rainfall dataset covering the years 2000\u20132020. End state: processed series 'rainfall_sat_qc_2000_2020' includes [('avg_rainfall', 114.6), ('max_rainfall_day', 312.0)] and is retrievable; a QC report (artifact_type 'pdf') exists with label 'QC_RAINFALL_SAT_2000_2020'; stakeholder output 'Rainfall QC 2000-2020' (audience 'external') references 'https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "rainfall_sat_qc_2000_2020",
                    "items": [
                        {
                            "timestamp": "avg_rainfall",
                            "value": 114.6
                        },
                        {
                            "timestamp": "max_rainfall_day",
                            "value": 312.0
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "rainfall_sat_qc_2000_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RAINFALL_SAT_2000_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RAINFALL_SAT_2000_2020",
                    "figure_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RAINFALL_SAT_2000_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall QC 2000-2020",
                    "audience": "external",
                    "artifact_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall QC 2000-2020"
                }
            }
        ],
        "outputs": [
                "series.name=rainfall_sat_qc_2000_2020; points=2; p1.ts=avg_rainfall; p1.value=114.6; p2.ts=max_rainfall_day; p2.value=312.0 | qc.figure_label=QC_RAINFALL_SAT_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf | stakeholder.output_label=Rainfall QC 2000-2020; audience=external; artifact_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_213",
        "instruction": "Coordinate the quality control for 25-year global CO\u2082 concentration records. End state: processed series 'co2_qc_1990_2015' has [('avg_co2_ppm', 402.5), ('max_co2_ppm', 419.1)] and is retrievable; a QC PDF report with label 'QC_CO2_1990_2015' is available; stakeholder output 'Global CO\u2082 QC 1990-2015' (audience 'external') links to 'https://storage.example.com/reports/QC_CO2_1990_2015.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "co2_qc_1990_2015",
                    "items": [
                        {
                            "timestamp": "avg_co2_ppm",
                            "value": 402.5
                        },
                        {
                            "timestamp": "max_co2_ppm",
                            "value": 419.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "co2_qc_1990_2015"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CO2_1990_2015"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CO2_1990_2015",
                    "figure_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CO2_1990_2015"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Global CO₂ QC 1990-2015",
                    "audience": "external",
                    "artifact_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Global CO₂ QC 1990-2015"
                }
            }
        ],
        "outputs": [
                "series.name=co2_qc_1990_2015; points=2; p1.ts=avg_co2_ppm; p1.value=402.5; p2.ts=max_co2_ppm; p2.value=419.1 | qc.figure_label=QC_CO2_1990_2015; qc.figure_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf | stakeholder.output_label=Global CO₂ QC 1990-2015; audience=external; artifact_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_214",
        "instruction": "Handle QC of river discharge measurements for the Amazon basin (1980\u20132010). Final state: processed series 'amazon_discharge_qc_1980_2010' includes [('avg_discharge', 85000.0), ('peak_discharge', 120000.0)] and is accessible; a QC figure marked 'QC_AMAZON_DISCHARGE_1980_2010' (pdf) is archived; stakeholder output 'Amazon River Discharge QC 1980-2010' (for audience 'internal') references 'https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "amazon_discharge_qc_1980_2010",
                    "items": [
                        {
                            "timestamp": "avg_discharge",
                            "value": 85000.0
                        },
                        {
                            "timestamp": "peak_discharge",
                            "value": 120000.0
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "amazon_discharge_qc_1980_2010"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_AMAZON_DISCHARGE_1980_2010"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_AMAZON_DISCHARGE_1980_2010",
                    "figure_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_AMAZON_DISCHARGE_1980_2010"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Amazon River Discharge QC 1980-2010",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Amazon River Discharge QC 1980-2010"
                }
            }
        ],
        "outputs": [
                "series.name=amazon_discharge_qc_1980_2010; points=2; p1.ts=avg_discharge; p1.value=85000.0; p2.ts=peak_discharge; p2.value=120000.0 | qc.figure_label=QC_AMAZON_DISCHARGE_1980_2010; qc.figure_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf | stakeholder.output_label=Amazon River Discharge QC 1980-2010; audience=internal; artifact_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_125",
        "instruction": "Coordinate the staging of 'ARIMA_Tide_v2' and document a May-2025 validation batch with QC. End state: model 'ARIMA_Tide_v2' (type 'arima', framework 'statsmodels', version '2.0', status 'staged') is documented and searchable; validation batch 'VAL_TIDE_2025-05' contains one entry ('2025-05-09T00:00:00Z', 1.45) and is accessible; validation MAPE 7.8 is preserved and viewable; QC PDF for label 'QC_TIDE_VAL_2025-05' is available and retrievable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "ARIMA_Tide_v2",
                    "model_type": "arima",
                    "framework": "statsmodels",
                    "version": "2.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "ARIMA_Tide_v2"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_TIDE_2025-05",
                    "model_name": "ARIMA_Tide_v2",
                    "items": [
                        {
                            "timestamp": "2025-05-09T00:00:00Z",
                            "prediction": 1.45
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_TIDE_2025-05"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "ARIMA_Tide_v2",
                    "metric_name": "MAPE",
                    "value": 7.8,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "ARIMA_Tide_v2"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_VAL_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_VAL_2025-05"
                }
            }
        ],
        "outputs": [
                "model.name=ARIMA_Tide_v2; type=arima; framework=statsmodels; version=2.0; status=staged | pred.batch_name=VAL_TIDE_2025-05; pred.model=ARIMA_Tide_v2; rows=1; first_ts=2025-05-09T00:00:00Z; first_pred=1.45 | metric.model=ARIMA_Tide_v2; metric.name=MAPE; metric.value=7.8; split=validation | qc.figure_label=QC_TIDE_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_124",
        "instruction": "Handle 'GRU_Temperature_v1' preparation and document a validation batch for June-2025 including QC. Final outcome: model 'GRU_Temperature_v1' (type 'gru', framework 'pytorch', version '1.0', status 'staged') is saved and searchable; validation batch 'VAL_TEMP_2025-06' contains one entry ('2025-06-18T12:00:00Z', 27.6) and is accessible; validation MAE 0.3 is documented; QC PNG for label 'QC_TEMP_VAL_2025-06' is present and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "GRU_Temperature_v1",
                    "model_type": "gru",
                    "framework": "pytorch",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "GRU_Temperature_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_TEMP_2025-06",
                    "model_name": "GRU_Temperature_v1",
                    "items": [
                        {
                            "timestamp": "2025-06-18T12:00:00Z",
                            "prediction": 27.6
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_TEMP_2025-06"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "GRU_Temperature_v1",
                    "metric_name": "MAE",
                    "value": 0.3,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "GRU_Temperature_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_VAL_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_VAL_2025-06"
                }
            }
        ],
        "outputs": [
                "model.name=GRU_Temperature_v1; type=gru; framework=pytorch; version=1.0; status=staged | pred.batch_name=VAL_TEMP_2025-06; pred.model=GRU_Temperature_v1; rows=1; first_ts=2025-06-18T12:00:00Z; first_pred=27.6 | metric.model=GRU_Temperature_v1; metric.name=MAE; metric.value=0.3; split=validation | qc.figure_label=QC_TEMP_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_123",
        "instruction": "Coordinate the staging of 'XGBoost_FloodRisk_v1' and document a July-2025 validation batch with QC. Final result: model 'XGBoost_FloodRisk_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is logged and accessible; validation batch 'VAL_FR_2025-07' includes one entry ('2025-07-20T00:00:00Z', 0.34) and is available; validation RMSE 0.05 is recorded and visible; QC PDF for label 'QC_FR_VAL_2025-07' is available and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "XGBoost_FloodRisk_v1",
                    "model_type": "xgboost",
                    "framework": "xgboost",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "XGBoost_FloodRisk_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_FR_2025-07",
                    "model_name": "XGBoost_FloodRisk_v1",
                    "items": [
                        {
                            "timestamp": "2025-07-20T00:00:00Z",
                            "prediction": 0.34
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_FR_2025-07"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "XGBoost_FloodRisk_v1",
                    "metric_name": "RMSE",
                    "value": 0.05,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "XGBoost_FloodRisk_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FR_VAL_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FR_VAL_2025-07"
                }
            }
        ],
        "outputs": [
                "model.name=XGBoost_FloodRisk_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | pred.batch_name=VAL_FR_2025-07; pred.model=XGBoost_FloodRisk_v1; rows=1; first_ts=2025-07-20T00:00:00Z; first_pred=0.34 | metric.model=XGBoost_FloodRisk_v1; metric.name=RMSE; metric.value=0.05; split=validation | qc.figure_label=QC_FR_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_122",
        "instruction": "Handle the staging of 'CNN_WaveHeight_v1' and record a validation batch for September 2025 with QC. End state: model 'CNN_WaveHeight_v1' (type 'cnn', framework 'tensorflow', version '1.0', status 'staged') is preserved and accessible; validation batch 'VAL_WH_2025-09' comprises one row ('2025-09-05T06:00:00Z', 1.72) and is available; validation MAE 0.12 is archived and viewable; QC PNG labeled 'QC_WH_VAL_2025-09' is preserved and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "CNN_WaveHeight_v1",
                    "model_type": "cnn",
                    "framework": "tensorflow",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "CNN_WaveHeight_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_WH_2025-09",
                    "model_name": "CNN_WaveHeight_v1",
                    "items": [
                        {
                            "timestamp": "2025-09-05T06:00:00Z",
                            "prediction": 1.72
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_WH_2025-09"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "CNN_WaveHeight_v1",
                    "metric_name": "MAE",
                    "value": 0.12,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "CNN_WaveHeight_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WH_VAL_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_WH_VAL_2025-09.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WH_VAL_2025-09"
                }
            }
        ],
        "outputs": [
                "model.name=CNN_WaveHeight_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | pred.batch_name=VAL_WH_2025-09; pred.model=CNN_WaveHeight_v1; rows=1; first_ts=2025-09-05T06:00:00Z; first_pred=1.72 | metric.model=CNN_WaveHeight_v1; metric.name=MAE; metric.value=0.12; split=validation | qc.figure_label=QC_WH_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WH_VAL_2025-09.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_121",
        "instruction": "Coordinate the staging of 'LSTM_Rainfall_v2' and document an August 2025 validation batch with QC. End state: model 'LSTM_Rainfall_v2' (type 'lstm', framework 'pytorch', version '2.0', status 'staged') is preserved and accessible; validation batch 'VAL_RF_2025-08' consists of one row ('2025-08-10T12:00:00Z', 22.5) and is available; validation RMSE 1.05 is documented and viewable; QC PDF labeled 'QC_RF_VAL_2025-08' is preserved and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "LSTM_Rainfall_v2",
                    "model_type": "lstm",
                    "framework": "pytorch",
                    "version": "2.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "LSTM_Rainfall_v2"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_RF_2025-08",
                    "model_name": "LSTM_Rainfall_v2",
                    "items": [
                        {
                            "timestamp": "2025-08-10T12:00:00Z",
                            "prediction": 22.5
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_RF_2025-08"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "LSTM_Rainfall_v2",
                    "metric_name": "RMSE",
                    "value": 1.05,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "LSTM_Rainfall_v2"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RF_VAL_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RF_VAL_2025-08"
                }
            }
        ],
        "outputs": [
                "model.name=LSTM_Rainfall_v2; type=lstm; framework=pytorch; version=2.0; status=staged | pred.batch_name=VAL_RF_2025-08; pred.model=LSTM_Rainfall_v2; rows=1; first_ts=2025-08-10T12:00:00Z; first_pred=22.5 | metric.model=LSTM_Rainfall_v2; metric.name=RMSE; metric.value=1.05; split=validation | qc.figure_label=QC_RF_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_120",
        "instruction": "Handle the staging of 'CNN_FloodExtent_v1' and document a validation log for July-2025. End state: model 'CNN_FloodExtent_v1' (type 'cnn', framework 'tensorflow', version '1.0', status 'staged') becomes recorded and queryable; validation batch 'VAL_FE_2025-07' includes one entry ('2025-07-12T15:00:00Z', 0.88) and is retrievable; validation MAE 0.09 is stored and accessible; QC PNG for the label 'QC_FE_VAL_2025-07' is available and retrievable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "CNN_FloodExtent_v1",
                    "model_type": "cnn",
                    "framework": "tensorflow",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "CNN_FloodExtent_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_FE_2025-07",
                    "model_name": "CNN_FloodExtent_v1",
                    "items": [
                        {
                            "timestamp": "2025-07-12T15:00:00Z",
                            "prediction": 0.88
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_FE_2025-07"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "CNN_FloodExtent_v1",
                    "metric_name": "MAE",
                    "value": 0.09,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "CNN_FloodExtent_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FE_VAL_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_FE_VAL_2025-07.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FE_VAL_2025-07"
                }
            }
        ],
        "outputs": [
                "model.name=CNN_FloodExtent_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | pred.batch_name=VAL_FE_2025-07; pred.model=CNN_FloodExtent_v1; rows=1; first_ts=2025-07-12T15:00:00Z; first_pred=0.88 | metric.model=CNN_FloodExtent_v1; metric.name=MAE; metric.value=0.09; split=validation | qc.figure_label=QC_FE_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FE_VAL_2025-07.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_119",
        "instruction": "Coordinate the staging of 'GRU_Rainfall_v1' and document a validation entry for June-2025. End state: model 'GRU_Rainfall_v1' (type 'gru', framework 'pytorch', version '1.0', status 'staged') is stored and accessible; validation batch 'VAL_RF_2025-06' contains one entry ('2025-06-15T09:00:00Z', 15.3) and is available; validation RMSE 1.2 is captured and readable; QC PDF labeled 'QC_RF_VAL_2025-06' is saved and retrievable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "GRU_Rainfall_v1",
                    "model_type": "gru",
                    "framework": "pytorch",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "GRU_Rainfall_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_RF_2025-06",
                    "model_name": "GRU_Rainfall_v1",
                    "items": [
                        {
                            "timestamp": "2025-06-15T09:00:00Z",
                            "prediction": 15.3
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_RF_2025-06"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "GRU_Rainfall_v1",
                    "metric_name": "RMSE",
                    "value": 1.2,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "GRU_Rainfall_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RF_VAL_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RF_VAL_2025-06"
                }
            }
        ],
        "outputs": [
                "model.name=GRU_Rainfall_v1; type=gru; framework=pytorch; version=1.0; status=staged | pred.batch_name=VAL_RF_2025-06; pred.model=GRU_Rainfall_v1; rows=1; first_ts=2025-06-15T09:00:00Z; first_pred=15.3 | metric.model=GRU_Rainfall_v1; metric.name=RMSE; metric.value=1.2; split=validation | qc.figure_label=QC_RF_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_117",
        "instruction": "Handle the onboarding of 'RF_Temperature_v3' and record a validation dataset from May 2025. Final state: model 'RF_Temperature_v3' (type 'random_forest', framework 'sklearn', version '3.1', status 'staged') is stored; validation batch 'VAL_TEMP_2025-05' includes one entry ('2025-05-05T00:00:00Z', 18.7) and is accessible; R\u00b2 score 0.91 is documented; a QC PDF report 'QC_TEMP_VAL_2025-05' is created and retained.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "RF_Temperature_v3",
                    "model_type": "random_forest",
                    "framework": "sklearn",
                    "version": "3.1",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "RF_Temperature_v3"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_TEMP_2025-05",
                    "model_name": "RF_Temperature_v3",
                    "items": [
                        {
                            "timestamp": "2025-05-05T00:00:00Z",
                            "prediction": 18.7
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_TEMP_2025-05"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "RF_Temperature_v3",
                    "metric_name": "R2",
                    "value": 0.91,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "RF_Temperature_v3"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_VAL_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_VAL_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_VAL_2025-05"
                }
            }
        ],
        "outputs": [
                "model.name=RF_Temperature_v3; type=random_forest; framework=sklearn; version=3.1; status=staged | pred.batch_name=VAL_TEMP_2025-05; pred.model=RF_Temperature_v3; rows=1; first_ts=2025-05-05T00:00:00Z; first_pred=18.7 | metric.model=RF_Temperature_v3; metric.name=R2; metric.value=0.91; split=validation | qc.figure_label=QC_TEMP_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_115",
        "instruction": "Coordinate the setup of 'Prophet_TideCycle_v1' and input a validation record for May 2025. Final state: model 'Prophet_TideCycle_v1' (type 'prophet', framework 'prophet', version '1.0', status 'staged') is inserted and available; validation batch 'VAL_TC_2025-05' contains one row ('2025-05-20T06:00:00Z', 2.44) and can be retrieved; validation MAPE 4.5 is logged and viewable; QC PDF labeled 'QC_TC_VAL_2025-05' is linked and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "Prophet_TideCycle_v1",
                    "model_type": "prophet",
                    "framework": "prophet",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "Prophet_TideCycle_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_TC_2025-05",
                    "model_name": "Prophet_TideCycle_v1",
                    "items": [
                        {
                            "timestamp": "2025-05-20T06:00:00Z",
                            "prediction": 2.44
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_TC_2025-05"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "Prophet_TideCycle_v1",
                    "metric_name": "MAPE",
                    "value": 4.5,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "Prophet_TideCycle_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TC_VAL_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TC_VAL_2025-05"
                }
            }
        ],
        "outputs": [
                "model.name=Prophet_TideCycle_v1; type=prophet; framework=prophet; version=1.0; status=staged | pred.batch_name=VAL_TC_2025-05; pred.model=Prophet_TideCycle_v1; rows=1; first_ts=2025-05-20T06:00:00Z; first_pred=2.44 | metric.model=Prophet_TideCycle_v1; metric.name=MAPE; metric.value=4.5; split=validation | qc.figure_label=QC_TC_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_114",
        "instruction": "Configure 'XGB_WindDamage_v1' and acquire a validation dataset for February-2025. Final state: model 'XGB_WindDamage_v1' (type 'xgboost', framework 'xgboost', version '1.6', status 'staged') is preserved; validation batch 'VAL_WD_2025-02' contains one entry ('2025-02-14T18:00:00Z', 12.8) and can be queried; validation MAE 1.7 is recorded and accessible; QC PDF is present for label 'QC_WD_VAL_2025-02' and is accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "XGB_WindDamage_v1",
                    "model_type": "xgboost",
                    "framework": "xgboost",
                    "version": "1.6",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "XGB_WindDamage_v1"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_WD_2025-02",
                    "model_name": "XGB_WindDamage_v1",
                    "items": [
                        {
                            "timestamp": "2025-02-14T18:00:00Z",
                            "prediction": 12.8
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_WD_2025-02"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "XGB_WindDamage_v1",
                    "metric_name": "MAE",
                    "value": 1.7,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "XGB_WindDamage_v1"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-02",
                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WD_VAL_2025-02"
                }
            }
        ],
        "outputs": [
                "model.name=XGB_WindDamage_v1; type=xgboost; framework=xgboost; version=1.6; status=staged | pred.batch_name=VAL_WD_2025-02; pred.model=XGB_WindDamage_v1; rows=1; first_ts=2025-02-14T18:00:00Z; first_pred=12.8 | metric.model=XGB_WindDamage_v1; metric.name=MAE; metric.value=1.7; split=validation | qc.figure_label=QC_WD_VAL_2025-02; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_113",
        "instruction": "Ensure 'LSTM_FloodRisk_v2' is registered and document an April-2025 validation run. Completion state: model 'LSTM_FloodRisk_v2' (type 'lstm', framework 'tensorflow', version '2.0', status 'staged') is retained and can be queried; validation batch 'VAL_FR_2025-04' includes one record ('2025-04-05T12:00:00Z', 0.76) and is accessible; validation RMSE 0.32 is cataloged and available; QC PNG is available for label 'QC_FR_VAL_2025-04' and is retrievable.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "LSTM_FloodRisk_v2",
                    "model_type": "lstm",
                    "framework": "tensorflow",
                    "version": "2.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "LSTM_FloodRisk_v2"
                },
            },
            {
                "name": "InsertPredictionBatch",
                "arguments": {
                    "batch_name": "VAL_FR_2025-04",
                    "model_name": "LSTM_FloodRisk_v2",
                    "items": [
                        {
                            "timestamp": "2025-04-05T12:00:00Z",
                            "prediction": 0.76
                        }
                    ]
                },
            },
            {
                "name": "GetPredictions",
                "arguments": {
                    "batch_name": "VAL_FR_2025-04"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "LSTM_FloodRisk_v2",
                    "metric_name": "RMSE",
                    "value": 0.32,
                    "dataset_split": "validation"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "LSTM_FloodRisk_v2"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FR_VAL_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-04.png",
                    "artifact_type": "png"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FR_VAL_2025-04"
                }
            }
        ],
        "outputs": [
                "model.name=LSTM_FloodRisk_v2; type=lstm; framework=tensorflow; version=2.0; status=staged | pred.batch_name=VAL_FR_2025-04; pred.model=LSTM_FloodRisk_v2; rows=1; first_ts=2025-04-05T12:00:00Z; first_pred=0.76 | metric.model=LSTM_FloodRisk_v2; metric.name=RMSE; metric.value=0.32; split=validation | qc.figure_label=QC_FR_VAL_2025-04; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-04.png"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_112",
        "instruction": "Handle the December-2024 salinity anomaly dataset, record QC validation, and dispatch the internal report. End state: processed series 'sal_anom_2024-12' contains four points, QC artifact 'QC_SAL_ANOM_2024-12.pdf' is stored, and stakeholder output titled 'Salinity Anomaly Dec 2024' for audience 'internal' references the PDF.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2024-12",
                    "items": [
                        {
                            "timestamp": "2024-12-03T00:00:00Z",
                            "value": 0.12
                        },
                        {
                            "timestamp": "2024-12-10T00:00:00Z",
                            "value": -0.04
                        },
                        {
                            "timestamp": "2024-12-18T00:00:00Z",
                            "value": 0.05
                        },
                        {
                            "timestamp": "2024-12-27T00:00:00Z",
                            "value": 0.09
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2024-12"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2024-12"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2024-12",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2024-12"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Dec 2024",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Dec 2024"
                }
            }
        ],
        "outputs": [
                "series.name=sal_anom_2024-12; points=4; p1.ts=2024-12-03T00:00:00Z; p1.value=0.12; p2.ts=2024-12-10T00:00:00Z; p2.value=-0.04; p3.ts=2024-12-18T00:00:00Z; p3.value=0.05; p4.ts=2024-12-27T00:00:00Z; p4.value=0.09 | qc.figure_label=QC_SAL_ANOM_2024-12; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf | stakeholder.output_label=Salinity Anomaly Dec 2024; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_111",
        "instruction": "Coordinate the generation of a January-2025 tidal harmonic series, attach QC results, and release an external summary. End state: harmonic series 'tidal_harm_2025-01' comprises three points, QC artifact 'QC_TIDAL_HARM_2025-01.pdf' is stored, and stakeholder output titled 'Tidal Harmonics Jan 2025' for audience 'external' references the PDF.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tidal_harm_2025-01",
                    "items": [
                        {
                            "timestamp": "2025-01-05T00:00:00Z",
                            "value": 1.21
                        },
                        {
                            "timestamp": "2025-01-15T00:00:00Z",
                            "value": 1.15
                        },
                        {
                            "timestamp": "2025-01-25T00:00:00Z",
                            "value": 1.18
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tidal_harm_2025-01"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_HARM_2025-01"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_HARM_2025-01",
                    "figure_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDAL_HARM_2025-01"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Tidal Harmonics Jan 2025",
                    "audience": "external",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Tidal Harmonics Jan 2025"
                }
            }
        ],
        "outputs": [
                "series.name=tidal_harm_2025-01; points=3; p1.ts=2025-01-05T00:00:00Z; p1.value=1.21; p2.ts=2025-01-15T00:00:00Z; p2.value=1.15; p3.ts=2025-01-25T00:00:00Z; p3.value=1.18 | qc.figure_label=QC_TIDAL_HARM_2025-01; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf | stakeholder.output_label=Tidal Harmonics Jan 2025; audience=external; artifact_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_110",
        "instruction": "Handle the computation of a February-2025 surge residual series, ensure it is archived, and distribute the QC output. End state: residual series 'surge_resid_2025-02' has four points, QC artifact 'QC_SURGE_RESID_2025-02.pdf' is stored, and an internal stakeholder summary labeled 'Feb 2025 Surge Residual' references the PDF.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "surge_resid_2025-02",
                    "items": [
                        {
                            "timestamp": "2025-02-02T00:00:00Z",
                            "value": -0.11
                        },
                        {
                            "timestamp": "2025-02-10T00:00:00Z",
                            "value": 0.07
                        },
                        {
                            "timestamp": "2025-02-18T00:00:00Z",
                            "value": 0.02
                        },
                        {
                            "timestamp": "2025-02-26T00:00:00Z",
                            "value": -0.05
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "surge_resid_2025-02"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RESID_2025-02"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RESID_2025-02",
                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SURGE_RESID_2025-02"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Feb 2025 Surge Residual",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Feb 2025 Surge Residual"
                }
            }
        ],
        "outputs": [
                "series.name=surge_resid_2025-02; points=4; p1.ts=2025-02-02T00:00:00Z; p1.value=-0.11; p2.ts=2025-02-10T00:00:00Z; p2.value=0.07; p3.ts=2025-02-18T00:00:00Z; p3.value=0.02; p4.ts=2025-02-26T00:00:00Z; p4.value=-0.05 | qc.figure_label=QC_SURGE_RESID_2025-02; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf | stakeholder.output_label=Feb 2025 Surge Residual; audience=internal; artifact_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_109",
        "instruction": "Coordinate the publication of June-2025 salinity index results with QC. End state: processed series 'sal_index_2025-06' holds points [('2025-06-04T00:00:00Z', 33.1), ('2025-06-16T00:00:00Z', 34.2), ('2025-06-29T00:00:00Z', 32.8)] and a QC report with label 'QC_SAL_INDEX_2025-06' is available.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_index_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-04T00:00:00Z",
                            "value": 33.1
                        },
                        {
                            "timestamp": "2025-06-16T00:00:00Z",
                            "value": 34.2
                        },
                        {
                            "timestamp": "2025-06-29T00:00:00Z",
                            "value": 32.8
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_index_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_INDEX_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_INDEX_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_INDEX_2025-06"
                }
            }
        ],
        "outputs": [
                "series.name=sal_index_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=33.1; p2.ts=2025-06-16T00:00:00Z; p2.value=34.2; p3.ts=2025-06-29T00:00:00Z; p3.value=32.8 | qc.figure_label=QC_SAL_INDEX_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_108",
        "instruction": "Handle the creation of a May-2025 rainfall deviation series and confirm that QC is generated. Objective: the processed series 'rain_dev_2025-05' includes [('2025-05-03T00:00:00Z', -5.1), ('2025-05-12T00:00:00Z', 2.4), ('2025-05-25T00:00:00Z', -1.7)]; ensure a QC figure is available under the label 'QC_RAIN_DEV_2025-05' with its stored path.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "rain_dev_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-03T00:00:00Z",
                            "value": -5.1
                        },
                        {
                            "timestamp": "2025-05-12T00:00:00Z",
                            "value": 2.4
                        },
                        {
                            "timestamp": "2025-05-25T00:00:00Z",
                            "value": -1.7
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "rain_dev_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_DEV_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_DEV_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_DEV_2025-05"
                }
            }
        ],
        "outputs": [
                "series.name=rain_dev_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=-5.1; p2.ts=2025-05-12T00:00:00Z; p2.value=2.4; p3.ts=2025-05-25T00:00:00Z; p3.value=-1.7 | qc.figure_label=QC_RAIN_DEV_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_107",
        "instruction": "Coordinate the publication of the April-2025 temperature anomaly series with QC validation. Final objective: the processed series 'temp_anom_2025-04' contains three data points [('2025-04-05T00:00:00Z', 1.2), ('2025-04-15T00:00:00Z', -0.3), ('2025-04-27T00:00:00Z', 0.6)] and remains readable; a corresponding QC PDF is available for the label 'QC_TEMP_ANOM_2025-04' stored as an artifact_type 'pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-05T00:00:00Z",
                            "value": 1.2
                        },
                        {
                            "timestamp": "2025-04-15T00:00:00Z",
                            "value": -0.3
                        },
                        {
                            "timestamp": "2025-04-27T00:00:00Z",
                            "value": 0.6
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04"
                }
            }
        ],
        "outputs": [
                "series.name=temp_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=1.2; p2.ts=2025-04-15T00:00:00Z; p2.value=-0.3; p3.ts=2025-04-27T00:00:00Z; p3.value=0.6 | qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_106",
        "instruction": "Handle the creation of a June-2025 salinity anomaly dataset inclusive of a QC check. End state: the processed series 'sal_anom_2025-06' contains two points [('2025-06-12T00:00:00Z', 0.5), ('2025-06-22T00:00:00Z', -0.1)] and is accessible; QC record 'QC_SAL_ANOM_2025-06' is available as PDF and retrievable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-12T00:00:00Z",
                            "value": 0.5
                        },
                        {
                            "timestamp": "2025-06-22T00:00:00Z",
                            "value": -0.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-06"
                }
            }
        ],
        "outputs": [
                "series.name=sal_anom_2025-06; points=2; p1.ts=2025-06-12T00:00:00Z; p1.value=0.5; p2.ts=2025-06-22T00:00:00Z; p2.value=-0.1 | qc.figure_label=QC_SAL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_105",
        "instruction": "Coordinate the generation of a May-2025 rainfall anomaly report with QC validation. End state: the processed series 'rain_anom_2025-05' contains three points [('2025-05-05T00:00:00Z', 12.0), ('2025-05-15T00:00:00Z', -3.2), ('2025-05-25T00:00:00Z', 4.7)] and can be retrieved; a QC artifact with label 'QC_RAIN_ANOM_2025-05' is saved as PDF and accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "rain_anom_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-05T00:00:00Z",
                            "value": 12.0
                        },
                        {
                            "timestamp": "2025-05-15T00:00:00Z",
                            "value": -3.2
                        },
                        {
                            "timestamp": "2025-05-25T00:00:00Z",
                            "value": 4.7
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "rain_anom_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_ANOM_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_ANOM_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RAIN_ANOM_2025-05"
                }
            }
        ],
        "outputs": [
                "series.name=rain_anom_2025-05; points=3; p1.ts=2025-05-05T00:00:00Z; p1.value=12.0; p2.ts=2025-05-15T00:00:00Z; p2.value=-3.2; p3.ts=2025-05-25T00:00:00Z; p3.value=4.7 | qc.figure_label=QC_RAIN_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_104",
        "instruction": "Publish the April-2025 temperature anomaly dataset with QC verification. Desired result: processed series 'temp_anom_2025-04' contains two points [('2025-04-10T00:00:00Z', 1.1), ('2025-04-25T00:00:00Z', -0.3)] and is accessible; a QC PDF is available for the label 'QC_TEMP_ANOM_2025-04' with the artifact stored and accessible; stakeholder output 'Temp Anomaly Apr 2025' (audience 'internal') is prepared.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-10T00:00:00Z",
                            "value": 1.1
                        },
                        {
                            "timestamp": "2025-04-25T00:00:00Z",
                            "value": -0.3
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-04"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Temp Anomaly Apr 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Temp Anomaly Apr 2025"
                }
            }
        ],
        "outputs": [
                "series.name=temp_anom_2025-04; points=2; p1.ts=2025-04-10T00:00:00Z; p1.value=1.1; p2.ts=2025-04-25T00:00:00Z; p2.value=-0.3 | qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf | stakeholder.output_label=Temp Anomaly Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_103",
        "instruction": "Handle the publication of the June-2025 precipitation anomaly series and ensure the QC figure is stored. Expected result: processed series 'precip_anom_2025-06' includes three points [('2025-06-01T00:00:00Z', -5.0), ('2025-06-15T00:00:00Z', 3.2), ('2025-06-29T00:00:00Z', -1.1)] and is retrievable; a QC artifact 'QC_PRECIP_ANOM_2025-06' (pdf) is present and accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_anom_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-01T00:00:00Z",
                            "value": -5.0
                        },
                        {
                            "timestamp": "2025-06-15T00:00:00Z",
                            "value": 3.2
                        },
                        {
                            "timestamp": "2025-06-29T00:00:00Z",
                            "value": -1.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "precip_anom_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_PRECIP_ANOM_2025-06"
                }
            }
        ],
        "outputs": [
                "series.name=precip_anom_2025-06; points=3; p1.ts=2025-06-01T00:00:00Z; p1.value=-5.0; p2.ts=2025-06-15T00:00:00Z; p2.value=3.2; p3.ts=2025-06-29T00:00:00Z; p3.value=-1.1 | qc.figure_label=QC_PRECIP_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_102",
        "instruction": "Handle the recording of February-2025 river-flow anomalies and ensure QC. End state: processed series 'flow_anom_2025-02' has three points [('2025-02-03T00:00:00Z', 120), ('2025-02-14T00:00:00Z', 110), ('2025-02-25T00:00:00Z', 130)] and is readable; QC figure with label 'QC_FLOW_ANOM_2025-02' exists and is retrievable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "flow_anom_2025-02",
                    "items": [
                        {
                            "timestamp": "2025-02-03T00:00:00Z",
                            "value": 120
                        },
                        {
                            "timestamp": "2025-02-14T00:00:00Z",
                            "value": 110
                        },
                        {
                            "timestamp": "2025-02-25T00:00:00Z",
                            "value": 130
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "flow_anom_2025-02"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOW_ANOM_2025-02"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOW_ANOM_2025-02",
                    "figure_path": "https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_FLOW_ANOM_2025-02"
                }
            }
        ],
        "outputs": [
                "series.name=flow_anom_2025-02; points=3; p1.ts=2025-02-03T00:00:00Z; p1.value=120; p2.ts=2025-02-14T00:00:00Z; p2.value=110; p3.ts=2025-02-25T00:00:00Z; p3.value=130 | qc.figure_label=QC_FLOW_ANOM_2025-02; qc.figure_path=https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_101",
        "instruction": "Coordinate the publication of an April-2025 sea-surface temperature anomaly series with a QC summary. End state: processed series 'sst_anom_2025-04' has three points [('2025-04-05T00:00:00Z', 0.5), ('2025-04-15T00:00:00Z', -0.1), ('2025-04-27T00:00:00Z', 0.3)] and is readable; a QC PDF exists for label 'QC_SST_ANOM_2025-04' with artifact_type 'pdf' and is retrievable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sst_anom_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-05T00:00:00Z",
                            "value": 0.5
                        },
                        {
                            "timestamp": "2025-04-15T00:00:00Z",
                            "value": -0.1
                        },
                        {
                            "timestamp": "2025-04-27T00:00:00Z",
                            "value": 0.3
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sst_anom_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SST_ANOM_2025-04"
                }
            }
        ],
        "outputs": [
                "series.name=sst_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=0.5; p2.ts=2025-04-15T00:00:00Z; p2.value=-0.1; p3.ts=2025-04-27T00:00:00Z; p3.value=0.3 | qc.figure_label=QC_SST_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SST_ANOM_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_82",
        "instruction": "Handle the publication of a November\u20112025 salinity anomaly series with QC. End state: processed series 'salinity_anom_2025-11' contains three points [('2025-11-01T00:00:00Z', 0.10), ('2025-11-11T00:00:00Z', -0.04), ('2025-11-21T00:00:00Z', 0.06)] and remains readable; a QC PDF for label 'QC_SAL_ANOM_2025-11' should be available with the figure record stored (artifact_type 'pdf') and readable; stakeholder output 'Salinity Anomaly Nov 2025' (audience 'internal') must reference 'https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf' and be accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "salinity_anom_2025-11",
                    "items": [
                        {
                            "timestamp": "2025-11-01T00:00:00Z",
                            "value": 0.1
                        },
                        {
                            "timestamp": "2025-11-11T00:00:00Z",
                            "value": -0.04
                        },
                        {
                            "timestamp": "2025-11-21T00:00:00Z",
                            "value": 0.06
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "salinity_anom_2025-11"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-11"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-11",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-11"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Nov 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Nov 2025"
                }
            }
        ],
        "outputs": [
                "series.name=salinity_anom_2025-11; points=3; p1.ts=2025-11-01T00:00:00Z; p1.value=0.10; p2.ts=2025-11-11T00:00:00Z; p2.value=-0.04; p3.ts=2025-11-21T00:00:00Z; p3.value=0.06 | qc.figure_label=QC_SAL_ANOM_2025-11; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf | stakeholder.output_label=Salinity Anomaly Nov 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_81",
        "instruction": "Oversee the publication of an October\u20112025 tide anomaly series with QC. End state: processed series 'tide_anom_2025-10' includes three points [('2025-10-03T00:00:00Z', 0.12), ('2025-10-13T00:00:00Z', -0.05), ('2025-10-23T00:00:00Z', 0.08)] and is readable; ensure a QC PDF for label 'QC_TIDE_ANOM_2025-10' is available with the figure record stored (artifact_type 'pdf') and readable; stakeholder output 'Tide Anomaly Oct 2025' (audience 'internal') must reference 'https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf' and be accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_anom_2025-10",
                    "items": [
                        {
                            "timestamp": "2025-10-03T00:00:00Z",
                            "value": 0.12
                        },
                        {
                            "timestamp": "2025-10-13T00:00:00Z",
                            "value": -0.05
                        },
                        {
                            "timestamp": "2025-10-23T00:00:00Z",
                            "value": 0.08
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "tide_anom_2025-10"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_ANOM_2025-10"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_ANOM_2025-10",
                    "figure_path": "https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TIDE_ANOM_2025-10"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Tide Anomaly Oct 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Tide Anomaly Oct 2025"
                }
            }
        ],
        "outputs": [
                "series.name=tide_anom_2025-10; points=3; p1.ts=2025-10-03T00:00:00Z; p1.value=0.12; p2.ts=2025-10-13T00:00:00Z; p2.value=-0.05; p3.ts=2025-10-23T00:00:00Z; p3.value=0.08 | qc.figure_label=QC_TIDE_ANOM_2025-10; qc.figure_path=https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf | stakeholder.output_label=Tide Anomaly Oct 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_80",
        "instruction": "Handle the publication of a September\u20112025 water\u2011level anomaly series with QC. Final state: the series 'wl_anom_2025-09' has been processed with three data points [('2025-09-05T00:00:00Z', 0.06), ('2025-09-15T00:00:00Z', -0.04), ('2025-09-25T00:00:00Z', 0.05)] and remains accessible; a PDF for QC is available for the label 'QC_WL_ANOM_2025-09', including a figure record stored as an artifact of type 'pdf' and is accessible; the stakeholder deliverable 'WL Anomaly Sep 2025' for the 'internal' audience links to 'https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "wl_anom_2025-09",
                    "items": [
                        {
                            "timestamp": "2025-09-05T00:00:00Z",
                            "value": 0.06
                        },
                        {
                            "timestamp": "2025-09-15T00:00:00Z",
                            "value": -0.04
                        },
                        {
                            "timestamp": "2025-09-25T00:00:00Z",
                            "value": 0.05
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "wl_anom_2025-09"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WL_ANOM_2025-09"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WL_ANOM_2025-09",
                    "figure_path": "https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WL_ANOM_2025-09"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "WL Anomaly Sep 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "WL Anomaly Sep 2025"
                }
            }
        ],
        "outputs": [
                "series.name=wl_anom_2025-09; points=3; p1.ts=2025-09-05T00:00:00Z; p1.value=0.06; p2.ts=2025-09-15T00:00:00Z; p2.value=-0.04; p3.ts=2025-09-25T00:00:00Z; p3.value=0.05 | qc.figure_label=QC_WL_ANOM_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf | stakeholder.output_label=WL Anomaly Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_75",
        "instruction": "Coordinate the publication of an April-2025 salinity anomaly series with QC. Final state: the series 'sal_anom_2025-04' has been processed with three data points [('2025-04-05T00:00:00Z', 0.12), ('2025-04-15T00:00:00Z', -0.03), ('2025-04-25T00:00:00Z', 0.07)] and remains accessible; a PDF for QC is available for the label 'QC_SAL_ANOM_2025-04', including a figure record stored as an artifact of type 'pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-05T00:00:00Z",
                            "value": 0.12
                        },
                        {
                            "timestamp": "2025-04-15T00:00:00Z",
                            "value": -0.03
                        },
                        {
                            "timestamp": "2025-04-25T00:00:00Z",
                            "value": 0.07
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "sal_anom_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-04"
                }
            }
        ],
        "outputs": [
                "series.name=sal_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=0.12; p2.ts=2025-04-15T00:00:00Z; p2.value=-0.03; p3.ts=2025-04-25T00:00:00Z; p3.value=0.07 | qc.figure_label=QC_SAL_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_76",
        "instruction": "Handle the publishing of a May-2025 water-temperature anomaly series ensuring QC is included. Final outcome: the series referred to as 'temp_anom_2025-05' is processed with three data points [('2025-05-03T00:00:00Z', -0.15), ('2025-05-12T00:00:00Z', 0.02), ('2025-05-27T00:00:00Z', 0.09)], and it is accessible; a QC PDF with the label 'QC_TEMP_ANOM_2025-05' is also available and readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-03T00:00:00Z",
                            "value": -0.15
                        },
                        {
                            "timestamp": "2025-05-12T00:00:00Z",
                            "value": 0.02
                        },
                        {
                            "timestamp": "2025-05-27T00:00:00Z",
                            "value": 0.09
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "temp_anom_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_TEMP_ANOM_2025-05"
                }
            }
        ],
        "outputs": [
                "series.name=temp_anom_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=-0.15; p2.ts=2025-05-12T00:00:00Z; p2.value=0.02; p3.ts=2025-05-27T00:00:00Z; p3.value=0.09 | qc.figure_label=QC_TEMP_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_77",
        "instruction": "Coordinate the publishing of a June-2025 current-speed anomaly series, making sure to include QC. The eventual state: the series named 'cur_anom_2025-06' is processed with three points [('2025-06-04T00:00:00Z', 0.22), ('2025-06-16T00:00:00Z', -0.05), ('2025-06-24T00:00:00Z', 0.11)], and is accessible; a QC PDF labeled 'QC_CUR_ANOM_2025-06' exists and is readable.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "cur_anom_2025-06",
                    "items": [
                        {
                            "timestamp": "2025-06-04T00:00:00Z",
                            "value": 0.22
                        },
                        {
                            "timestamp": "2025-06-16T00:00:00Z",
                            "value": -0.05
                        },
                        {
                            "timestamp": "2025-06-24T00:00:00Z",
                            "value": 0.11
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "cur_anom_2025-06"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CUR_ANOM_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CUR_ANOM_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_CUR_ANOM_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CUR_ANOM_2025-06"
                }
            }
        ],
        "outputs": [
                "series.name=cur_anom_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=0.22; p2.ts=2025-06-16T00:00:00Z; p2.value=-0.05; p3.ts=2025-06-24T00:00:00Z; p3.value=0.11 | qc.figure_label=QC_CUR_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_CUR_ANOM_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_78",
        "instruction": "Handle the publication of a July-2025 wave-height anomaly series ensuring QC is applied. End state: the processed series 'wave_anom_2025-07' contains three data points [('2025-07-07T00:00:00Z', 0.35), ('2025-07-18T00:00:00Z', -0.06), ('2025-07-29T00:00:00Z', 0.21)] and is accessible; a QC PDF is available for the label 'QC_WAVE_ANOM_2025-07' and can be accessed.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "wave_anom_2025-07",
                    "items": [
                        {
                            "timestamp": "2025-07-07T00:00:00Z",
                            "value": 0.35
                        },
                        {
                            "timestamp": "2025-07-18T00:00:00Z",
                            "value": -0.06
                        },
                        {
                            "timestamp": "2025-07-29T00:00:00Z",
                            "value": 0.21
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "wave_anom_2025-07"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOM_2025-07"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOM_2025-07",
                    "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_ANOM_2025-07"
                }
            }
        ],
        "outputs": [
                "series.name=wave_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=0.35; p2.ts=2025-07-18T00:00:00Z; p2.value=-0.06; p3.ts=2025-07-29T00:00:00Z; p3.value=0.21 | qc.figure_label=QC_WAVE_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_79",
        "instruction": "Coordinate the publication of an August-2025 dissolved-oxygen anomaly series with the QC ensured. End state: the processed series 'do_anom_2025-08' includes three data points [('2025-08-02T00:00:00Z', 0.18), ('2025-08-14T00:00:00Z', -0.07), ('2025-08-27T00:00:00Z', 0.10)] and is accessible; a QC PDF is in place for the label 'QC_DO_ANOM_2025-08' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "do_anom_2025-08",
                    "items": [
                        {
                            "timestamp": "2025-08-02T00:00:00Z",
                            "value": 0.18
                        },
                        {
                            "timestamp": "2025-08-14T00:00:00Z",
                            "value": -0.07
                        },
                        {
                            "timestamp": "2025-08-27T00:00:00Z",
                            "value": 0.1
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "do_anom_2025-08"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_DO_ANOM_2025-08"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_DO_ANOM_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_DO_ANOM_2025-08"
                }
            }
        ],
        "outputs": [
                "series.name=do_anom_2025-08; points=3; p1.ts=2025-08-02T00:00:00Z; p1.value=0.18; p2.ts=2025-08-14T00:00:00Z; p2.value=-0.07; p3.ts=2025-08-27T00:00:00Z; p3.value=0.10 | qc.figure_label=QC_DO_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_71",
        "instruction": "Handle the registration of 'XGBoost_Rainfall_v1' version 1.0 along with test artifacts. End state: the model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is successfully recorded and accessible; the model_config 'default' includes max_depth 5, n_estimators 150, learning_rate 0.05 and is accessible; test AUC 0.94 is documented and accessible; artifact '/models/XGBoost_Rainfall_v1_v1.0.json' is present and accessible.",
        "actions": [
            {
                "name": "InsertModel",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "model_type": "xgboost",
                    "framework": "xgboost",
                    "version": "1.0",
                    "status": "staged"
                },
            },
            {
                "name": "GetModelDetails",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1"
                },
            },
            {
                "name": "UpsertModelConfig",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "config_name": "default",
                    "params": {
                        "max_depth": 5,
                        "n_estimators": 150,
                        "learning_rate": 0.05
                    }
                },
            },
            {
                "name": "GetModelConfig",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "config_name": "default"
                },
            },
            {
                "name": "InsertMetrics",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1",
                    "metric_name": "AUC",
                    "value": 0.94,
                    "dataset_split": "test"
                },
            },
            {
                "name": "GetMetrics",
                "arguments": {
                    "model_name": "XGBoost_Rainfall_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/models/XGBoost_Rainfall_v1_v1.0.json",
                    "mime_type": "application/json"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/models/XGBoost_Rainfall_v1_v1.0.json"
                }
            }
        ],
        "outputs": [
                "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | config.model=XGBoost_Rainfall_v1; config.name=default; params.max_depth=5; params.n_estimators=150; params.learning_rate=0.05 | metric.model=XGBoost_Rainfall_v1; metric.name=AUC; metric.value=0.94; split=test | file.path=/models/XGBoost_Rainfall_v1_v1.0.json; file.mime=application/json"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_56",
        "instruction": "Coordinate the curation of feature set 'coastal_flood_features_v1' (version '1.0') including columns ['water_level_max','wave_height_mean','precipitation_total'] and mark it as active. End state: the feature set is accessible; feature file '/features/coastal_flood_features_v1.parquet' is present and accessible; project config 'active_feature_set' is set to 'coastal_flood_features_v1'; QC PDF 'QC_COASTAL_FEATURES_2025-06' is available and accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "coastal_flood_features_v1",
                    "version": "1.0",
                    "columns": [
                        "water_level_max",
                        "wave_height_mean",
                        "precipitation_total"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "coastal_flood_features_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/coastal_flood_features_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/coastal_flood_features_v1.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "coastal_flood_features_v1"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_FEATURES_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_FEATURES_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_COASTAL_FEATURES_2025-06"
                }
            }
        ],
        "outputs": [
                "feature_set.name=coastal_flood_features_v1; version=1.0; columns=water_level_max|wave_height_mean|precipitation_total | file.path=/features/coastal_flood_features_v1.parquet; file.mime=application/parquet | config.active_feature_set=coastal_flood_features_v1 | qc.figure_label=QC_COASTAL_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_50",
        "instruction": "Handle the creation of a feature set 'storm_features_v2' (version '2.0') with the columns ['surge_height', 'wind_speed', 'precipitation'] and ensure its recording. End state: the feature set is accessible; the feature file '/features/storm_features_v2.parquet' is available and can be read; the project config 'active_feature_set' is updated to 'storm_features_v2'; the QC PDF titled 'QC_STORM_FEATURES_2025-06' is present and accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "storm_features_v2",
                    "version": "2.0",
                    "columns": [
                        "surge_height",
                        "wind_speed",
                        "precipitation"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "storm_features_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/storm_features_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/storm_features_v2.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "storm_features_v2"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_FEATURES_2025-06"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_FEATURES_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_FEATURES_2025-06"
                }
            }
        ],
        "outputs": [
                "feature_set.name=storm_features_v2; version=2.0; columns=surge_height|wind_speed|precipitation | file.path=/features/storm_features_v2.parquet; file.mime=application/parquet | config.active_feature_set=storm_features_v2 | qc.figure_label=QC_STORM_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_51",
        "instruction": "Coordinate the curation of the feature set 'harbor_arrival_metrics_v2' version 2.0 and proceed to activate it. End state: the feature_set 'harbor_arrival_metrics_v2' with the columns ['arrival_count','dwell_time_mean','dwell_time_median'] is recorded; the feature file '/features/harbor_arrival_metrics_v2.parquet' is present and readable; the project configuration 'active_feature_set' is set to 'harbor_arrival_metrics_v2'; a QC PDF labeled 'QC_HARBOR_ARRIVAL_2025-03' is available and readable.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "harbor_arrival_metrics_v2",
                    "version": "2.0",
                    "columns": [
                        "arrival_count",
                        "dwell_time_mean",
                        "dwell_time_median"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "harbor_arrival_metrics_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/harbor_arrival_metrics_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/harbor_arrival_metrics_v2.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "harbor_arrival_metrics_v2"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_ARRIVAL_2025-03"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_ARRIVAL_2025-03",
                    "figure_path": "https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_ARRIVAL_2025-03"
                }
            }
        ],
        "outputs": [
                "feature_set.name=harbor_arrival_metrics_v2; version=2.0; columns=arrival_count|dwell_time_mean|dwell_time_median | file.path=/features/harbor_arrival_metrics_v2.parquet; file.mime=application/parquet | config.active_feature_set=harbor_arrival_metrics_v2 | qc.figure_label=QC_HARBOR_ARRIVAL_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_36",
        "instruction": "Coordinate the creation of a processed time series for harbor ice thickness 'ice_thickness_2025-05'. Final status: series 'ice_thickness_2025-05' comprises three data points [('2025-05-01T00:00:00Z', 0.25), ('2025-05-08T00:00:00Z', 0.30), ('2025-05-15T00:00:00Z', 0.28)] and is accessible for reading; QC figure 'QC_ICE_THICKNESS_2025-05' is generated (artifact_type 'pdf') and readable; the stakeholder document 'Harbor Ice Thickness May 2025' (audience 'internal') includes a link to 'https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf'.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "ice_thickness_2025-05",
                    "items": [
                        {
                            "timestamp": "2025-05-01T00:00:00Z",
                            "value": 0.25
                        },
                        {
                            "timestamp": "2025-05-08T00:00:00Z",
                            "value": 0.3
                        },
                        {
                            "timestamp": "2025-05-15T00:00:00Z",
                            "value": 0.28
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "ice_thickness_2025-05"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_ICE_THICKNESS_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_ICE_THICKNESS_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_ICE_THICKNESS_2025-05"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Harbor Ice Thickness May 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Harbor Ice Thickness May 2025"
                }
            }
        ],
        "outputs": [
                "series.name=ice_thickness_2025-05; points=3; p1.value=0.25; p2.value=0.30; p3.value=0.28 | qc.figure_label=QC_ICE_THICKNESS_2025-05; qc.figure_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf | stakeholder.output_label=Harbor Ice Thickness May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_37",
        "instruction": "Handle the curation of a feature set 'storm_surge_v2' for May 2025 and ensure it is activated within the project configuration. Final outcome: feature_set 'storm_surge_v2' (version '2.0') with columns ['max_surge','mean_surge'] is documented and readable; ensure that the feature file '/features/storm_surge_v2.parquet' exists and is accessible; the project configuration 'active_feature_set' is set to 'storm_surge_v2'; QC figure 'QC_STORM_SURGE_2025-05' has been created (artifact_type 'pdf') and is available for reading.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "storm_surge_v2",
                    "version": "2.0",
                    "columns": [
                        "max_surge",
                        "mean_surge"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "storm_surge_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/storm_surge_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/storm_surge_v2.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "storm_surge_v2"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_SURGE_2025-05"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_SURGE_2025-05",
                    "figure_path": "https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_STORM_SURGE_2025-05"
                }
            }
        ],
        "outputs": [
                "feature_set.name=storm_surge_v2; version=2.0; columns=max_surge|mean_surge | file.path=/features/storm_surge_v2.parquet; file.mime=application/parquet | config.active_feature_set=storm_surge_v2 | qc.figure_label=QC_STORM_SURGE_2025-05; qc.figure_path=https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_3",
        "instruction": "Handle the publication of a March\u20112025 rainfall-runoff anomaly series. End state: the processed series 'rainfall_runoff_anom_2025-03' includes three points [('2025-03-05T00:00:00Z', 12.4), ('2025-03-12T00:00:00Z', 9.8), ('2025-03-19T00:00:00Z', 15.2)] and is accessible; a QC PDF with label 'QC_RR_ANOM_2025-03' is created, with a figure record stored (artifact_type 'pdf') and accessible; the stakeholder output 'Rainfall-Runoff Anomaly Mar 2025' (audience 'internal') has a reference to 'https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "rainfall_runoff_anom_2025-03",
                    "items": [
                        {
                            "timestamp": "2025-03-05T00:00:00Z",
                            "value": 12.4
                        },
                        {
                            "timestamp": "2025-03-12T00:00:00Z",
                            "value": 9.8
                        },
                        {
                            "timestamp": "2025-03-19T00:00:00Z",
                            "value": 15.2
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "rainfall_runoff_anom_2025-03"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_RR_ANOM_2025-03"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_RR_ANOM_2025-03",
                    "figure_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_RR_ANOM_2025-03"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall-Runoff Anomaly Mar 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Rainfall-Runoff Anomaly Mar 2025"
                }
            }
        ],
        "outputs": [
                "series.name=rainfall_runoff_anom_2025-03; points=3; p1.ts=2025-03-05T00:00:00Z; p1.value=12.4; p2.ts=2025-03-12T00:00:00Z; p2.value=9.8; p3.ts=2025-03-19T00:00:00Z; p3.value=15.2 | qc.figure_label=QC_RR_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf | stakeholder.output_label=Rainfall-Runoff Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_5",
        "instruction": "Coordinate a QC review of a 30-year NOAA tide gauge dataset. End state: the processed series 'noaa_tide_qc_1990_2020' provides summary points [('mean_sea_level', 2.34), ('max_tide', 3.78)] and is accessible; a QC PDF labeled 'QC_NOAA_TIDE_1990_2020' is generated and stored (artifact_type 'pdf'); the stakeholder output 'NOAA Tide QC 1990-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_tide_qc_1990_2020",
                    "items": [
                        {
                            "timestamp": "mean_sea_level",
                            "value": 2.34
                        },
                        {
                            "timestamp": "max_tide",
                            "value": 3.78
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "noaa_tide_qc_1990_2020"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_TIDE_1990_2020"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_TIDE_1990_2020",
                    "figure_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_NOAA_TIDE_1990_2020"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Tide QC 1990-2020",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "NOAA Tide QC 1990-2020"
                }
            }
        ],
        "outputs": [
                "series.name=noaa_tide_qc_1990_2020; points=2; p1.ts=mean_sea_level; p1.value=2.34; p2.ts=max_tide; p2.value=3.78 | qc.figure_label=QC_NOAA_TIDE_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf | stakeholder.output_label=NOAA Tide QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_30",
        "instruction": "Handle the publication of a March\u20112025 salinity anomaly series. Final state: processed series 'salinity_anom_2025-03' contains three points [('2025-03-07T00:00:00Z', 0.07), ('2025-03-14T00:00:00Z', -0.02), ('2025-03-21T00:00:00Z', 0.04)] and is accessible; a QC PDF is available for the label 'QC_SAL_ANOM_2025-03' with figure record kept (artifact_type 'pdf') and is accessible; stakeholder output 'Salinity Anomaly Mar 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "salinity_anom_2025-03",
                    "items": [
                        {
                            "timestamp": "2025-03-07T00:00:00Z",
                            "value": 0.07
                        },
                        {
                            "timestamp": "2025-03-14T00:00:00Z",
                            "value": -0.02
                        },
                        {
                            "timestamp": "2025-03-21T00:00:00Z",
                            "value": 0.04
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "salinity_anom_2025-03"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-03"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-03",
                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_SAL_ANOM_2025-03"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Mar 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Salinity Anomaly Mar 2025"
                }
            }
        ],
        "outputs": [
                "series.name=salinity_anom_2025-03; points=3; p1.ts=2025-03-07T00:00:00Z; p1.value=0.07; p2.ts=2025-03-14T00:00:00Z; p2.value=-0.02; p3.ts=2025-03-21T00:00:00Z; p3.value=0.04 | qc.figure_label=QC_SAL_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf | stakeholder.output_label=Salinity Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_31",
        "instruction": "Coordinate the curation of the feature set 'harbor_ops_v2' and activate it with QC. Final state: feature_set 'harbor_ops_v2' (version '2.0') featuring columns ['arrival_count','dwell_time_median','departure_count'] is documented and accessible; feature file '/features/harbor_ops_v2.parquet' is present and accessible; project config 'active_feature_set' is set to 'harbor_ops_v2' and is accessible; a QC PDF is available for label 'QC_HARBOR_OPS_2025-03' with figure record kept (artifact_type 'pdf') and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "harbor_ops_v2",
                    "version": "2.0",
                    "columns": [
                        "arrival_count",
                        "dwell_time_median",
                        "departure_count"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "harbor_ops_v2"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/harbor_ops_v2.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/harbor_ops_v2.parquet"
                },
            },
            {
                "name": "UpdateProjectConfig",
                "arguments": {
                    "updates": {
                        "active_feature_set": "harbor_ops_v2"
                    }
                },
            },
            {
                "name": "GetProjectConfig",
                "arguments": {
                    "key": "active_feature_set"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_OPS_2025-03"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_OPS_2025-03",
                    "figure_path": "https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_HARBOR_OPS_2025-03"
                }
            }
        ],
        "outputs": [
                "feature_set.name=harbor_ops_v2; version=2.0; columns=arrival_count|dwell_time_median|departure_count | file.path=/features/harbor_ops_v2.parquet; file.mime=application/parquet | config.active_feature_set=harbor_ops_v2 | qc.figure_label=QC_HARBOR_OPS_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_32",
        "instruction": "Handle the publication of an April 2025 wave height series for Puget Sound. Desired outcome: processed series 'wave_height_2025-04' includes three points [('2025-04-05T00:00:00Z', 1.2), ('2025-04-12T00:00:00Z', 0.8), ('2025-04-19T00:00:00Z', 1.5)] and remains accessible; a quality control PDF for label 'QC_WAVE_HEIGHT_2025-04' is created, stored as a figure (artifact_type 'pdf') and accessible; internal audience output 'Wave Height Apr 2025' references 'https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertProcessedTimeseries",
                "arguments": {
                    "series_name": "wave_height_2025-04",
                    "items": [
                        {
                            "timestamp": "2025-04-05T00:00:00Z",
                            "value": 1.2
                        },
                        {
                            "timestamp": "2025-04-12T00:00:00Z",
                            "value": 0.8
                        },
                        {
                            "timestamp": "2025-04-19T00:00:00Z",
                            "value": 1.5
                        }
                    ]
                },
            },
            {
                "name": "GetProcessedTimeseries",
                "arguments": {
                    "series_name": "wave_height_2025-04"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_HEIGHT_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_HEIGHT_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_WAVE_HEIGHT_2025-04"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Wave Height Apr 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Wave Height Apr 2025"
                }
            }
        ],
        "outputs": [
                "series.name=wave_height_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=1.2; p2.ts=2025-04-12T00:00:00Z; p2.value=0.8; p3.ts=2025-04-19T00:00:00Z; p3.value=1.5 | qc.figure_label=QC_WAVE_HEIGHT_2025-04; qc.figure_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf | stakeholder.output_label=Wave Height Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"
        ]
    }
    ,
    {
        "annotator": R,
        "user_id": "ds_v3_34",
        "instruction": "Coordinate the creation of a logistic regression climate risk assessment dataset 'climate_risk_v1' for 2025-04. Expected outcome: dataset 'climate_risk_v1' (version '1.0') containing columns ['temperature','rainfall','flood_risk'] is documented and open for access; feature file '/features/climate_risk_v1.parquet' is present and accessible; a quality control PDF with label 'QC_CLIMATE_RISK_2025-04' is prepared, stored as a figure (artifact_type 'pdf') and accessible; internal audience output 'Climate Risk Apr 2025' references 'https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf' and is accessible.",
        "actions": [
            {
                "name": "InsertFeatureSet",
                "arguments": {
                    "feature_set_name": "climate_risk_v1",
                    "version": "1.0",
                    "columns": [
                        "temperature",
                        "rainfall",
                        "flood_risk"
                    ]
                },
            },
            {
                "name": "GetFeatureSetDetails",
                "arguments": {
                    "feature_set_name": "climate_risk_v1"
                },
            },
            {
                "name": "InsertFile",
                "arguments": {
                    "path": "/features/climate_risk_v1.parquet",
                    "mime_type": "application/parquet"
                },
            },
            {
                "name": "GetFile",
                "arguments": {
                    "path": "/features/climate_risk_v1.parquet"
                },
            },
            {
                "name": "ExportQcFigure",
                "arguments": {
                    "figure_label": "QC_CLIMATE_RISK_2025-04"
                },
            },
            {
                "name": "InsertQcFigure",
                "arguments": {
                    "figure_label": "QC_CLIMATE_RISK_2025-04",
                    "figure_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf",
                    "artifact_type": "pdf"
                },
            },
            {
                "name": "GetQcFigure",
                "arguments": {
                    "figure_label": "QC_CLIMATE_RISK_2025-04"
                },
            },
            {
                "name": "InsertStakeholderOutput",
                "arguments": {
                    "output_label": "Climate Risk Apr 2025",
                    "audience": "internal",
                    "artifact_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"
                },
            },
            {
                "name": "GetStakeholderOutput",
                "arguments": {
                    "output_label": "Climate Risk Apr 2025"
                }
            }
        ],
        "outputs": [
                "feature_set.name=climate_risk_v1; version=1.0; columns=temperature|rainfall|flood_risk | file.path=/features/climate_risk_v1.parquet; file.mime=application/parquet | qc.figure_label=QC_CLIMATE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf | stakeholder.output_label=Climate Risk Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"
        ]
    }
]
