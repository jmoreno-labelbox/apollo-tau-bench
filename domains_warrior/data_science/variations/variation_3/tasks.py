from domains.dto import Action, Task

TASKS = [
   # Task(
   #      annotator="R",
   #      user_id="ds_v3_1000",
   #      instruction=(
   #          "You define an October-2025 backfill cutoff and validate configuration. End state: "
   #          "project config has backfill_cutoff '2025-10-18T17:00:00Z' and is retrievable; "
   #          "terminal log event 'BACKFILL_CUTOFF_CONFIRMED' with message 'October backfill cutoff finalized.' exists and is readable; "
   #          "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-10' with artifact_type 'pdf' and is accessible."
   #      ),
   #      actions=[
   #          Action(name="update_project_config", kwargs={"updates": {"backfill_cutoff": "2025-10-18T17:00:00Z"}}),
   #          Action(name="get_project_config", kwargs={"key": "backfill_cutoff"}),
   #
   #          Action(name="record_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED", "message": "October backfill cutoff finalized."}),
   #          Action(name="list_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),
   #
   #          Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
   #          Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10", "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-10.pdf", "artifact_type": "pdf"}),
   #          Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
   #      ],
   #      outputs=[
   #          "config.backfill_cutoff=2025-10-18T17:00:00Z | "
   #          "log.event_type=BACKFILL_CUTOFF_CONFIRMED; log.message=October backfill cutoff finalized. | "
   #          "qc.figure_label=QC_CONFIG_BACKFILL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-10.pdf"
   #      ],
   #  ),

    Task(
        annotator="R",
        user_id="ds_v3_1001",
        instruction=(
            "You define a December-2025 backfill cutoff and verify readiness. End state: "
            "project config has backfill_cutoff '2025-12-22T20:00:00Z' and is retrievable; "
            "terminal log event 'BACKFILL_CUTOFF_APPLIED' with message 'Backfill cutoff applied for end-of-year runs.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-12' with artifact_type 'pdf' and is accessible."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"backfill_cutoff": "2025-12-22T20:00:00Z"}}),
            Action(name="get_project_config", kwargs={"key": "backfill_cutoff"}),

            Action(name="record_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED", "message": "Backfill cutoff applied for end-of-year runs."}),
            Action(name="list_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12", "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-12-22T20:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_APPLIED; log.message=Backfill cutoff applied for end-of-year runs. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-12; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1002",
        instruction=(
            "You define a September-2025 backfill cutoff and ensure readiness. End state: "
            "project config has backfill_cutoff '2025-09-15T16:00:00Z' and is readable; "
            "terminal log event 'BACKFILL_CUTOFF_CONFIRMED' with message 'September backfill cutoff completed successfully.' exists and is retrievable; "
            "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-09' with artifact_type 'pdf' and is accessible."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"backfill_cutoff": "2025-09-15T16:00:00Z"}}),
            Action(name="get_project_config", kwargs={"key": "backfill_cutoff"}),

            Action(name="record_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED", "message": "September backfill cutoff completed successfully."}),
            Action(name="list_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09", "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-09-15T16:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_CONFIRMED; log.message=September backfill cutoff completed successfully. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf"
        ],
    ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_1003",
    #     instruction=(
    #         "You create an urban flood risk dataset 'urban_flood_v1' for 2025‑07. End state: "
    #         "dataset 'urban_flood_v1' (version '1.0') with columns ['rainfall','drainage_capacity','flood_risk'] is recorded and retrievable; "
    #         "feature file '/features/urban_flood_v1.parquet' exists and is readable; "
    #         "a QC PDF exists for label 'QC_URBAN_FLOOD_2025-07' with artifact_type 'pdf' and is accessible; "
    #         "stakeholder output 'Urban Flood Jul 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf' and is readable."
    #     ),
    #     actions=[
    #         Action(name="insert_feature_set", kwargs={"feature_set_name": "urban_flood_v1", "version": "1.0", "columns": ["rainfall","drainage_capacity","flood_risk"]}),
    #         Action(name="get_feature_set_details", kwargs={"feature_set_name": "urban_flood_v1"}),
    #
    #         Action(name="insert_file", kwargs={"path": "/features/urban_flood_v1.parquet", "mime_type": "application/parquet"}),
    #         Action(name="get_file", kwargs={"path": "/features/urban_flood_v1.parquet"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07", "figure_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),
    #
    #         Action(name="insert_stakeholder_output", kwargs={"output_label": "Urban Flood Jul 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf"}),
    #         Action(name="get_stakeholder_output", kwargs={"output_label": "Urban Flood Jul 2025"}),
    #     ],
    #     outputs=[
    #         "feature_set.name=urban_flood_v1; version=1.0; columns=rainfall|drainage_capacity|flood_risk | "
    #         "file.path=/features/urban_flood_v1.parquet; file.mime=application/parquet | "
    #         "qc.figure_label=QC_URBAN_FLOOD_2025-07; qc.figure_path=https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf | "
    #         "stakeholder.output_label=Urban Flood Jul 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf"
    #     ],
    # ),

        Task(
            annotator="R",
            user_id="ds_v3_1004",
            instruction=(
                "You create a heatwave risk dataset 'heatwave_risk_v1' for 2025‑08. End state: "
                "dataset 'heatwave_risk_v1' (version '1.0') with columns ['temperature','humidity','heat_risk'] is stored and retrievable; "
                "feature file '/features/heatwave_risk_v1.parquet' exists and is readable; "
                "a QC PDF exists for label 'QC_HEATWAVE_RISK_2025-08' with artifact_type 'pdf' and is accessible; "
                "stakeholder output 'Heatwave Risk Aug 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf' and is readable."
            ),
            actions=[
                Action(name="insert_feature_set", kwargs={"feature_set_name": "heatwave_risk_v1", "version": "1.0", "columns": ["temperature","humidity","heat_risk"]}),
                Action(name="get_feature_set_details", kwargs={"feature_set_name": "heatwave_risk_v1"}),

                Action(name="insert_file", kwargs={"path": "/features/heatwave_risk_v1.parquet", "mime_type": "application/parquet"}),
                Action(name="get_file", kwargs={"path": "/features/heatwave_risk_v1.parquet"}),

                Action(name="export_qc_figure", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),
                Action(name="insert_qc_figure", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08", "figure_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf", "artifact_type": "pdf"}),
                Action(name="get_qc_figure", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),

                Action(name="insert_stakeholder_output", kwargs={"output_label": "Heatwave Risk Aug 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"}),
                Action(name="get_stakeholder_output", kwargs={"output_label": "Heatwave Risk Aug 2025"}),
            ],
            outputs=[
                "feature_set.name=heatwave_risk_v1; version=1.0; columns=temperature|humidity|heat_risk | "
                "file.path=/features/heatwave_risk_v1.parquet; file.mime=application/parquet | "
                "qc.figure_label=QC_HEATWAVE_RISK_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf | "
                "stakeholder.output_label=Heatwave Risk Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"
            ],
        ),

    Task(
        annotator="R",
        user_id="ds_v3_1005",
        instruction=(
            "You create a drought risk dataset 'drought_risk_v1' for 2025‑09. End state: "
            "dataset 'drought_risk_v1' (version '1.0') with columns ['soil_moisture','temperature','drought_index'] is stored and readable; "
            "feature file '/features/drought_risk_v1.parquet' exists and is accessible; "
            "a QC PDF exists for label 'QC_DROUGHT_RISK_2025-09' with artifact_type 'pdf'; "
            "stakeholder output 'Drought Risk Sep 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf' and is retrievable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "drought_risk_v1", "version": "1.0", "columns": ["soil_moisture","temperature","drought_index"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "drought_risk_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/drought_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/drought_risk_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09", "figure_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Drought Risk Sep 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Drought Risk Sep 2025"}),
        ],
        outputs=[
            "feature_set.name=drought_risk_v1; version=1.0; columns=soil_moisture|temperature|drought_index | "
            "file.path=/features/drought_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_DROUGHT_RISK_2025-09; qc.figure_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf | "
            "stakeholder.output_label=Drought Risk Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1006",
        instruction=(
            "You finalize sea surface temperature feature QC for June-2025. End state: "
            "feature_set 'sst_features_v2' (version '2.1') with columns ['sst_mean','sst_max','sst_std'] is recorded and readable; "
            "feature file '/features/sst_features_v2.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_SST_FEATURES_2025-06' with artifact_type 'pdf' and is readable; "
            "stakeholder output 'SST QC June 2025' (audience 'oceanography_team') references 'https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "sst_features_v2", "version": "2.1", "columns": ["sst_mean","sst_max","sst_std"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "sst_features_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/sst_features_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/sst_features_v2.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SST_FEATURES_2025-06", "figure_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "SST QC June 2025", "audience": "oceanography_team", "artifact_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "SST QC June 2025"}),
        ],
        outputs=[
            "feature_set.name=sst_features_v2; version=2.1; columns=sst_mean|sst_max|sst_std | "
            "file.path=/features/sst_features_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SST_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf | "
            "stakeholder.output_label=SST QC June 2025; audience=oceanography_team; artifact_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1007",
        instruction=(
            "You finalize ocean current feature QC for July-2025. End state: "
            "feature_set 'ocean_current_v1' (version '1.5') with columns ['current_speed','current_dir','std_dev'] is stored and readable; "
            "feature file '/features/ocean_current_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_OCEAN_CURRENT_2025-07' with artifact_type 'pdf' and accessible; "
            "stakeholder output 'Ocean Current QC July 2025' (audience 'marine_team') references 'https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "ocean_current_v1", "version": "1.5", "columns": ["current_speed","current_dir","std_dev"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "ocean_current_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/ocean_current_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/ocean_current_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07", "figure_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Ocean Current QC July 2025", "audience": "marine_team", "artifact_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Ocean Current QC July 2025"}),
        ],
        outputs=[
            "feature_set.name=ocean_current_v1; version=1.5; columns=current_speed|current_dir|std_dev | "
            "file.path=/features/ocean_current_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_OCEAN_CURRENT_2025-07; qc.figure_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf | "
            "stakeholder.output_label=Ocean Current QC July 2025; audience=marine_team; artifact_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1008",
        instruction=(
            "You finalize ocean salinity feature QC for August-2025. End state: "
            "feature_set 'salinity_index_v1' (version '1.2') with columns ['salinity_mean','salinity_max','salinity_std'] is recorded and readable; "
            "feature file '/features/salinity_index_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_SALINITY_INDEX_2025-08' with artifact_type 'pdf' and accessible; "
            "stakeholder output 'Salinity Index QC Aug 2025' (audience 'research_team') references 'https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "salinity_index_v1", "version": "1.2", "columns": ["salinity_mean","salinity_max","salinity_std"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "salinity_index_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/salinity_index_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/salinity_index_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08", "figure_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Salinity Index QC Aug 2025", "audience": "research_team", "artifact_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Salinity Index QC Aug 2025"}),
        ],
        outputs=[
            "feature_set.name=salinity_index_v1; version=1.2; columns=salinity_mean|salinity_max|salinity_std | "
            "file.path=/features/salinity_index_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SALINITY_INDEX_2025-08; qc.figure_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf | "
            "stakeholder.output_label=Salinity Index QC Aug 2025; audience=research_team; artifact_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1010",
        instruction=(
            "You onboard 'XGBoost_Rainfall_v1' and log a July-2025 validation dataset. "
            "End state: model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is persisted; "
            "validation batch 'VAL_RAIN_2025-07' contains one entry ('2025-07-15T00:00:00Z', 124.3) and is accessible; "
            "R² score 0.93 is registered; "
            "a QC PDF report 'QC_RAIN_VAL_2025-07' is generated and stored."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "XGBoost_Rainfall_v1", "model_type": "xgboost", "framework": "xgboost", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_RAIN_2025-07", "model_name": "XGBoost_Rainfall_v1", "items": [
                {"timestamp": "2025-07-15T00:00:00Z", "prediction": 124.3}
            ]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_RAIN_2025-07"}),

            Action(name="insert_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1", "metric_name": "R2", "value": 0.93, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RAIN_VAL_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RAIN_VAL_2025-07", "figure_path": "https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RAIN_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "pred.batch_name=VAL_RAIN_2025-07; pred.model=XGBoost_Rainfall_v1; rows=1; first_ts=2025-07-15T00:00:00Z; first_pred=124.3 | "
            "metric.model=XGBoost_Rainfall_v1; metric.name=R2; metric.value=0.93; split=validation | "
            "qc.figure_label=QC_RAIN_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1012",
        instruction=(
            "You configure a May-2025 model retrain window and validate it. End state: "
            "project config has retrain_window_start '2025-05-01T00:00:00Z' and retrain_window_end '2025-05-31T23:59:59Z' and is readable; "
            "terminal log event 'MODEL_RETRAIN_WINDOW_SET' with message 'May retrain window applied.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_RETRAIN_2025-05' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"retrain_window_start": "2025-05-01T00:00:00Z", "retrain_window_end": "2025-05-31T23:59:59Z"}}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_start"}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_end"}),

            Action(name="record_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "May retrain window applied."}),
            Action(name="list_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05", "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-05-01T00:00:00Z; config.retrain_window_end=2025-05-31T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=May retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_1013",
        instruction=(
            "You configure a June-2025 model retrain window and validate it. End state: "
            "project config has retrain_window_start '2025-06-01T00:00:00Z' and retrain_window_end '2025-06-30T23:59:59Z' and is readable; "
            "terminal log event 'MODEL_RETRAIN_WINDOW_SET' with message 'June retrain window applied.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_RETRAIN_2025-06' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"retrain_window_start": "2025-06-01T00:00:00Z", "retrain_window_end": "2025-06-30T23:59:59Z"}}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_start"}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_end"}),

            Action(name="record_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "June retrain window applied."}),
            Action(name="list_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06", "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-06-01T00:00:00Z; config.retrain_window_end=2025-06-30T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=June retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-06; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf"
        ],
    ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_1014",
    #     instruction=(
    #         "You configure a July-2025 model retrain window and validate it. End state: "
    #         "project config has retrain_window_start '2025-07-01T00:00:00Z' and retrain_window_end '2025-07-31T23:59:59Z' and is readable; "
    #         "terminal log event 'MODEL_RETRAIN_WINDOW_SET' with message 'July retrain window applied.' exists and is readable; "
    #         "a QC PDF exists for label 'QC_CONFIG_RETRAIN_2025-07' with figure record stored (artifact_type 'pdf') and readable."
    #     ),
    #     actions=[
    #         Action(name="update_project_config", kwargs={"updates": {"retrain_window_start": "2025-07-01T00:00:00Z", "retrain_window_end": "2025-07-31T23:59:59Z"}}),
    #         Action(name="get_project_config", kwargs={"key": "retrain_window_start"}),
    #         Action(name="get_project_config", kwargs={"key": "retrain_window_end"}),
    #
    #         Action(name="record_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "July retrain window applied."}),
    #         Action(name="list_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07", "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-07.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
    #     ],
    #     outputs=[
    #         "config.retrain_window_start=2025-07-01T00:00:00Z; config.retrain_window_end=2025-07-31T23:59:59Z | "
    #         "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=July retrain window applied. | "
    #         "qc.figure_label=QC_CONFIG_RETRAIN_2025-07; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-07.pdf"
    #     ],
    # ),

    Task(
        annotator="R",
        user_id="ds_v3_901",
        instruction=(
            "You should define a January-2026 backfill cutoff, ensure system readiness, and archive QC. "
            "End state: project config has backfill_cutoff '2026-01-10T08:00:00Z'; terminal log 'BACKFILL_READY' with message "
            "'Early January backfill cutoff configured successfully.' is present; QC PDF 'QC_CONFIG_BACKFILL_2026-01.pdf' is stored."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"backfill_cutoff": "2026-01-10T08:00:00Z"}}),
            Action(name="get_project_config", kwargs={"key": "backfill_cutoff"}),

            Action(name="record_terminal_log", kwargs={"event_type": "BACKFILL_READY", "message": "Early January backfill cutoff configured successfully."}),
            Action(name="list_terminal_log", kwargs={"event_type": "BACKFILL_READY"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01", "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
        ],
        outputs=[
            "config.backfill_cutoff=2026-01-10T08:00:00Z | "
            "log.event_type=BACKFILL_READY; log.message=Early January backfill cutoff configured successfully. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2026-01; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_903",
        instruction=(
            "You configure 'GradientBoosting_Wind_v3' and add an October-2025 validation record. "
            "End state: model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is inserted and visible; "
            "validation batch 'VAL_WD_2025-10' has two rows [('2025-10-10T12:00:00Z', 15.3), ('2025-10-22T12:00:00Z', 14.8)] and is retrievable; "
            "validation MAE 0.95 is stored and readable; "
            "QC PNG with label 'QC_WD_VAL_2025-10' is linked and accessible."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "GradientBoosting_Wind_v3", "model_type": "gradient_boosting", "framework": "sklearn", "version": "3.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "GradientBoosting_Wind_v3"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_WD_2025-10", "model_name": "GradientBoosting_Wind_v3", "items": [
                {"timestamp": "2025-10-10T12:00:00Z", "prediction": 15.3},
                {"timestamp": "2025-10-22T12:00:00Z", "prediction": 14.8}
            ]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_WD_2025-10"}),

            Action(name="insert_metrics", kwargs={"model_name": "GradientBoosting_Wind_v3", "metric_name": "MAE", "value": 0.95, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "GradientBoosting_Wind_v3"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-10", "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-10"}),
        ],
        outputs=[
            "model.name=GradientBoosting_Wind_v3; type=gradient_boosting; framework=sklearn; version=3.0; status=staged | "
            "pred.batch_name=VAL_WD_2025-10; pred.model=GradientBoosting_Wind_v3; rows=2; first_ts=2025-10-10T12:00:00Z; first_pred=15.3 | "
            "metric.model=GradientBoosting_Wind_v3; metric.name=MAE; metric.value=0.95; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-10.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_906",
        instruction=(
            "You publish a sediment transport feature set 'sediment_transport_v3' for 2025‑09. End state: "
            "feature set 'sediment_transport_v3' (version '3.0') with columns ['sediment_flux','current_speed','deposition_rate'] is recorded and readable; "
            "feature file '/features/sediment_transport_v3.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_SEDIMENT_TRANSPORT_2025-09' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Sediment Transport Sep 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "sediment_transport_v3", "version": "3.0", "columns": ["sediment_flux","current_speed","deposition_rate"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "sediment_transport_v3"}),

            Action(name="insert_file", kwargs={"path": "/features/sediment_transport_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/sediment_transport_v3.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SEDIMENT_TRANSPORT_2025-09"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SEDIMENT_TRANSPORT_2025-09", "figure_path": "https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SEDIMENT_TRANSPORT_2025-09"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Sediment Transport Sep 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Sediment Transport Sep 2025"}),
        ],
        outputs=[
            "feature_set.name=sediment_transport_v3; version=3.0; columns=sediment_flux|current_speed|deposition_rate | "
            "file.path=/features/sediment_transport_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SEDIMENT_TRANSPORT_2025-09; qc.figure_path=https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf | "
            "stakeholder.output_label=Sediment Transport Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SEDIMENT_TRANSPORT_2025-09.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_907",
        instruction=(
            "You publish a coastal flood risk dataset 'flood_risk_v5' for 2025‑10. End state: "
            "dataset 'flood_risk_v5' (version '5.0') with columns ['flood_probability','storm_surge_height','risk_index'] is recorded and readable; "
            "feature file '/features/flood_risk_v5.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_FLOOD_RISK_2025-10' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Flood Risk Oct 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "flood_risk_v5", "version": "5.0", "columns": ["flood_probability","storm_surge_height","risk_index"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "flood_risk_v5"}),

            Action(name="insert_file", kwargs={"path": "/features/flood_risk_v5.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/flood_risk_v5.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10", "figure_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Flood Risk Oct 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Flood Risk Oct 2025"}),
        ],
        outputs=[
            "feature_set.name=flood_risk_v5; version=5.0; columns=flood_probability|storm_surge_height|risk_index | "
            "file.path=/features/flood_risk_v5.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_FLOOD_RISK_2025-10; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf | "
            "stakeholder.output_label=Flood Risk Oct 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_908",
        instruction=(
            "You publish a tidal variation dataset 'tidal_variation_v3' for 2025‑11. End state: "
            "dataset 'tidal_variation_v3' (version '3.0') with columns ['high_tide','low_tide','tidal_range'] is recorded and readable; "
            "feature file '/features/tidal_variation_v3.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_TIDAL_VARIATION_2025-11' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Tidal Variation Nov 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "tidal_variation_v3", "version": "3.0", "columns": ["high_tide","low_tide","tidal_range"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "tidal_variation_v3"}),

            Action(name="insert_file", kwargs={"path": "/features/tidal_variation_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/tidal_variation_v3.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11", "figure_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Tidal Variation Nov 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Tidal Variation Nov 2025"}),
        ],
        outputs=[
            "feature_set.name=tidal_variation_v3; version=3.0; columns=high_tide|low_tide|tidal_range | "
            "file.path=/features/tidal_variation_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_TIDAL_VARIATION_2025-11; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf | "
            "stakeholder.output_label=Tidal Variation Nov 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_910",
        instruction=(
            "You QC a 40-year NOAA precipitation dataset. End state: "
            "processed series 'noaa_precip_qc_1980_2020' has summary points [('annual_avg', 1023.4), ('max_annual', 1820.1), ('min_annual', 540.2)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_PRECIP_1980_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA Precipitation QC 1980-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_precip_qc_1980_2020", "items": [
                {"timestamp": "annual_avg", "value": 1023.4},
                {"timestamp": "max_annual", "value": 1820.1},
                {"timestamp": "min_annual", "value": 540.2}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_precip_qc_1980_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA Precipitation QC 1980-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA Precipitation QC 1980-2020"}),
        ],
        outputs=[
            "series.name=noaa_precip_qc_1980_2020; points=3; p1.ts=annual_avg; p1.value=1023.4; p2.ts=max_annual; p2.value=1820.1; p3.ts=min_annual; p3.value=540.2 | "
            "qc.figure_label=QC_NOAA_PRECIP_1980_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf | "
            "stakeholder.output_label=NOAA Precipitation QC 1980-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_911",
        instruction=(
            "You QC a 20-year USGS groundwater level dataset. End state: "
            "processed series 'usgs_groundwater_qc_2005_2025' has summary points [('mean_level', 15.7), ('lowest_level', 3.4), ('highest_level', 28.1)] and is readable; "
            "a QC PDF exists for label 'QC_USGS_GW_2005_2025' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'USGS Groundwater QC 2005-2025' (audience 'internal') references 'https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "usgs_groundwater_qc_2005_2025", "items": [
                {"timestamp": "mean_level", "value": 15.7},
                {"timestamp": "lowest_level", "value": 3.4},
                {"timestamp": "highest_level", "value": 28.1}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "usgs_groundwater_qc_2005_2025"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_USGS_GW_2005_2025", "figure_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "USGS Groundwater QC 2005-2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "USGS Groundwater QC 2005-2025"}),
        ],
        outputs=[
            "series.name=usgs_groundwater_qc_2005_2025; points=3; p1.ts=mean_level; p1.value=15.7; p2.ts=lowest_level; p2.value=3.4; p3.ts=highest_level; p3.value=28.1 | "
            "qc.figure_label=QC_USGS_GW_2005_2025; qc.figure_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf | "
            "stakeholder.output_label=USGS Groundwater QC 2005-2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_913",
        instruction=(
            "You QC a Landsat-derived surface temperature dataset for 1990–2020. End state: "
            "processed series 'landsat_surf_temp_qc_1990_2020' includes [('avg_temp', 22.3), ('max_temp_day', 38.7), ('min_temp_day', -4.2)] and is retrievable; "
            "a QC report (artifact_type 'pdf') exists with label 'QC_LANDSAT_TEMP_1990_2020'; "
            "stakeholder output 'Landsat Surface Temp QC 1990-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020", "items": [
                {"timestamp": "avg_temp", "value": 22.3},
                {"timestamp": "max_temp_day", "value": 38.7},
                {"timestamp": "min_temp_day", "value": -4.2}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020", "figure_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Landsat Surface Temp QC 1990-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Landsat Surface Temp QC 1990-2020"}),
        ],
        outputs=[
            "series.name=landsat_surf_temp_qc_1990_2020; points=3; p1.ts=avg_temp; p1.value=22.3; p2.ts=max_temp_day; p2.value=38.7; p3.ts=min_temp_day; p3.value=-4.2 | "
            "qc.figure_label=QC_LANDSAT_TEMP_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf | "
            "stakeholder.output_label=Landsat Surface Temp QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_914",
        instruction=(
            "You QC a TRMM satellite rainfall dataset covering 1998–2018. End state: "
            "processed series 'trmm_rainfall_qc_1998_2018' includes [('annual_avg', 105.7), ('max_daily_rain', 289.5), ('min_daily_rain', 0.0)] and is retrievable; "
            "a QC report (artifact_type 'pdf') exists with label 'QC_TRMM_RAINFALL_1998_2018'; "
            "stakeholder output 'TRMM Rainfall QC 1998-2018' (audience 'external') references 'https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "trmm_rainfall_qc_1998_2018", "items": [
                {"timestamp": "annual_avg", "value": 105.7},
                {"timestamp": "max_daily_rain", "value": 289.5},
                {"timestamp": "min_daily_rain", "value": 0.0}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "trmm_rainfall_qc_1998_2018"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018", "figure_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "TRMM Rainfall QC 1998-2018", "audience": "external", "artifact_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "TRMM Rainfall QC 1998-2018"}),
        ],
        outputs=[
            "series.name=trmm_rainfall_qc_1998_2018; points=3; p1.ts=annual_avg; p1.value=105.7; p2.ts=max_daily_rain; p2.value=289.5; p3.ts=min_daily_rain; p3.value=0.0 | "
            "qc.figure_label=QC_TRMM_RAINFALL_1998_2018; qc.figure_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf | "
            "stakeholder.output_label=TRMM Rainfall QC 1998-2018; audience=external; artifact_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"
        ],
    ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_802",
    #     instruction=(
    #         "You define a November-2025 backfill cutoff and confirm readiness. End state: "
    #         "project config has backfill_cutoff '2025-11-20T18:00:00Z' and is readable; "
    #         "terminal log event 'BACKFILL_CUTOFF_SET' with message 'Backfill cutoff applied for late November runs.' exists and is readable; "
    #         "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-11' with figure record stored (artifact_type 'pdf') and readable."
    #     ),
    #     actions=[
    #         Action(name="update_project_config", kwargs={"updates": {"backfill_cutoff": "2025-11-20T18:00:00Z"}}),
    #         Action(name="get_project_config", kwargs={"key": "backfill_cutoff"}),
    #
    #         Action(name="record_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_SET", "message": "Backfill cutoff applied for late November runs."}),
    #         Action(name="list_terminal_log", kwargs={"event_type": "BACKFILL_CUTOFF_SET"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11", "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-11.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
    #     ],
    #     outputs=[
    #         "config.backfill_cutoff=2025-11-20T18:00:00Z | "
    #         "log.event_type=BACKFILL_CUTOFF_SET; log.message=Backfill cutoff applied for late November runs. | "
    #         "qc.figure_label=QC_CONFIG_BACKFILL_2025-11; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-11.pdf"
    #     ],
    # ),

    Task(
        annotator="R",
        user_id="ds_v3_805",
        instruction=(
            "You configure a February-2026 validation checkpoint and validate readiness. End state: "
            "project config has validation_checkpoint '2026-02-14T14:00:00Z' and is readable; "
            "terminal log event 'VALIDATION_CHECKPOINT_SET' with message 'Validation checkpoint created for mid-February.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_VALIDATION_2026-02' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"validation_checkpoint": "2026-02-14T14:00:00Z"}}),
            Action(name="get_project_config", kwargs={"key": "validation_checkpoint"}),

            Action(name="record_terminal_log", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET", "message": "Validation checkpoint created for mid-February."}),
            Action(name="list_terminal_log", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02", "figure_path": "https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
        ],
        outputs=[
            "config.validation_checkpoint=2026-02-14T14:00:00Z | "
            "log.event_type=VALIDATION_CHECKPOINT_SET; log.message=Validation checkpoint created for mid-February. | "
            "qc.figure_label=QC_CONFIG_VALIDATION_2026-02; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_701",
        instruction=(
            "You should publish the May-2025 precipitation anomaly series with QC validation. "
            "End state: processed series 'precip_anom_2025-05' has three points "
            "[('2025-05-02T00:00:00Z', -12.5), ('2025-05-18T00:00:00Z', 8.3), ('2025-05-29T00:00:00Z', 3.1)] "
            "and is readable; a QC PDF exists for label 'QC_PRECIP_ANOM_2025-05' and is stored in artifact_type 'pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "precip_anom_2025-05", "items": [
                {"timestamp": "2025-05-02T00:00:00Z", "value": -12.5},
                {"timestamp": "2025-05-18T00:00:00Z", "value": 8.3},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 3.1}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "precip_anom_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05", "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
        ],
        outputs=[
            "series.name=precip_anom_2025-05; points=3; p1.ts=2025-05-02T00:00:00Z; p1.value=-12.5; p2.ts=2025-05-18T00:00:00Z; p2.value=8.3; p3.ts=2025-05-29T00:00:00Z; p3.value=3.1 | "
            "qc.figure_label=QC_PRECIP_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf"
        ],
    ),

        Task(
        annotator="R",
        user_id="ds_v3_702",
        instruction=(
            "You should publish the June-2025 sea-level anomaly series with QC validation. "
            "End state: processed series 'sea_lvl_anom_2025-06' has three points "
            "[('2025-06-04T00:00:00Z', 0.12), ('2025-06-14T00:00:00Z', -0.05), ('2025-06-25T00:00:00Z', 0.22)] "
            "and is readable; a QC PDF exists for label 'QC_SEA_LVL_ANOM_2025-06' and is stored in artifact_type 'pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sea_lvl_anom_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 0.12},
                {"timestamp": "2025-06-14T00:00:00Z", "value": -0.05},
                {"timestamp": "2025-06-25T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sea_lvl_anom_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06", "figure_path": "https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=sea_lvl_anom_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=0.12; p2.ts=2025-06-14T00:00:00Z; p2.value=-0.05; p3.ts=2025-06-25T00:00:00Z; p3.value=0.22 | "
            "qc.figure_label=QC_SEA_LVL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_703",
        instruction=(
            "You should publish the July-2025 wind-speed anomaly series with QC validation. "
            "End state: processed series 'windspd_anom_2025-07' has three points "
            "[('2025-07-07T00:00:00Z', 2.5), ('2025-07-16T00:00:00Z', -1.8), ('2025-07-28T00:00:00Z', 0.9)] "
            "and is readable; a QC PDF exists for label 'QC_WINDSPD_ANOM_2025-07' and is stored in artifact_type 'pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "windspd_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 2.5},
                {"timestamp": "2025-07-16T00:00:00Z", "value": -1.8},
                {"timestamp": "2025-07-28T00:00:00Z", "value": 0.9}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "windspd_anom_2025-07"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07", "figure_path": "https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
        ],
        outputs=[
            "series.name=windspd_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=2.5; p2.ts=2025-07-16T00:00:00Z; p2.value=-1.8; p3.ts=2025-07-28T00:00:00Z; p3.value=0.9 | "
            "qc.figure_label=QC_WINDSPD_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_704",
        instruction=(
            "You should publish the August-2025 humidity anomaly series with QC validation. "
            "End state: processed series 'humid_anom_2025-08' has three points "
            "[('2025-08-03T00:00:00Z', 4.0), ('2025-08-14T00:00:00Z', -2.7), ('2025-08-26T00:00:00Z', 1.5)] "
            "and is readable; a QC PDF exists for label 'QC_HUMID_ANOM_2025-08' and is stored in artifact_type 'pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "humid_anom_2025-08", "items": [
                {"timestamp": "2025-08-03T00:00:00Z", "value": 4.0},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -2.7},
                {"timestamp": "2025-08-26T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "humid_anom_2025-08"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08", "figure_path": "https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
        ],
        outputs=[
            "series.name=humid_anom_2025-08; points=3; p1.ts=2025-08-03T00:00:00Z; p1.value=4.0; p2.ts=2025-08-14T00:00:00Z; p2.value=-2.7; p3.ts=2025-08-26T00:00:00Z; p3.value=1.5 | "
            "qc.figure_label=QC_HUMID_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_705",
        instruction=(
            "You should register 'LSTM_Flood_v2' with validation metrics and model config. End state: "
            "model 'LSTM_Flood_v2' (type 'rnn', framework 'tensorflow', version '2.0', status 'staged') is recorded and readable; "
            "model_config 'seq_default' has hidden_units 128, dropout 0.3, and layers 3 and is readable; "
            "validation Accuracy 0.902 is stored and readable; "
            "artifact '/models/LSTM_Flood_v2_v2.0.h5' exists and is readable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "LSTM_Flood_v2", "model_type": "rnn", "framework": "tensorflow", "version": "2.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="upsert_model_config", kwargs={"model_name": "LSTM_Flood_v2", "config_name": "seq_default", "params": {"hidden_units": 128, "dropout": 0.3, "layers": 3}}),
            Action(name="get_model_config", kwargs={"model_name": "LSTM_Flood_v2", "config_name": "seq_default"}),

            Action(name="insert_metrics", kwargs={"model_name": "LSTM_Flood_v2", "metric_name": "Accuracy", "value": 0.902, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="insert_file", kwargs={"path": "/models/LSTM_Flood_v2_v2.0.h5", "mime_type": "application/octet-stream"}),
            Action(name="get_file", kwargs={"path": "/models/LSTM_Flood_v2_v2.0.h5"}),
        ],
        outputs=[
            "model.name=LSTM_Flood_v2; type=rnn; framework=tensorflow; version=2.0; status=staged | "
            "config.model=LSTM_Flood_v2; config.name=seq_default; params.hidden_units=128; params.dropout=0.3; params.layers=3 | "
            "metric.model=LSTM_Flood_v2; metric.name=Accuracy; metric.value=0.902; split=validation | "
            "file.path=/models/LSTM_Flood_v2_v2.0.h5; file.mime=application/octet-stream"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_706",
        instruction=(
            "You should register 'Transformer_Climate_v3' with artifacts and metrics. End state: "
            "model 'Transformer_Climate_v3' (type 'transformer', framework 'pytorch', version '3.1', status 'staged') is recorded and readable; "
            "model_config 'attention_default' has heads 8, d_model 256, and layers 6 and is readable; "
            "validation Loss 0.145 is stored and readable; "
            "artifact '/models/Transformer_Climate_v3_v3.1.pt' exists and is readable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "Transformer_Climate_v3", "model_type": "transformer", "framework": "pytorch", "version": "3.1", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="upsert_model_config", kwargs={"model_name": "Transformer_Climate_v3", "config_name": "attention_default", "params": {"heads": 8, "d_model": 256, "layers": 6}}),
            Action(name="get_model_config", kwargs={"model_name": "Transformer_Climate_v3", "config_name": "attention_default"}),

            Action(name="insert_metrics", kwargs={"model_name": "Transformer_Climate_v3", "metric_name": "Loss", "value": 0.145, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="insert_file", kwargs={"path": "/models/Transformer_Climate_v3_v3.1.pt", "mime_type": "application/octet-stream"}),
            Action(name="get_file", kwargs={"path": "/models/Transformer_Climate_v3_v3.1.pt"}),
        ],
        outputs=[
            "model.name=Transformer_Climate_v3; type=transformer; framework=pytorch; version=3.1; status=staged | "
            "config.model=Transformer_Climate_v3; config.name=attention_default; params.heads=8; params.d_model=256; params.layers=6 | "
            "metric.model=Transformer_Climate_v3; metric.name=Loss; metric.value=0.145; split=validation | "
            "file.path=/models/Transformer_Climate_v3_v3.1.pt; file.mime=application/octet-stream"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_708",
        instruction=(
            "You register surge-risk feature QC for April-2025. End state: "
            "feature_set 'surge_risk_v2' (version '2.1') with columns ['risk_index','exceedance_prob'] is recorded and readable; "
            "feature file '/features/surge_risk_v2.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_SURGE_RISK_2025-04' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Surge Risk QC Apr 2025' (audience 'regulators') references 'https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "surge_risk_v2", "version": "2.1", "columns": ["risk_index","exceedance_prob"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "surge_risk_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/surge_risk_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/surge_risk_v2.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SURGE_RISK_2025-04", "figure_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Surge Risk QC Apr 2025", "audience": "regulators", "artifact_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Surge Risk QC Apr 2025"}),
        ],
        outputs=[
            "feature_set.name=surge_risk_v2; version=2.1; columns=risk_index|exceedance_prob | "
            "file.path=/features/surge_risk_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SURGE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf | "
            "stakeholder.output_label=Surge Risk QC Apr 2025; audience=regulators; artifact_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_709",
        instruction=(
            "You finalize wave-height anomaly feature QC for May-2025. End state: "
            "feature_set 'wave_anomaly_v1' (version '1.3') with columns ['hmean','hmax','stddev'] is recorded and readable; "
            "feature file '/features/wave_anomaly_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_WAVE_ANOMALY_2025-05' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Wave Anomaly QC May 2025' (audience 'science_team') references 'https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "wave_anomaly_v1", "version": "1.3", "columns": ["hmean","hmax","stddev"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "wave_anomaly_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/wave_anomaly_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/wave_anomaly_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05", "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Wave Anomaly QC May 2025", "audience": "science_team", "artifact_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Wave Anomaly QC May 2025"}),
        ],
        outputs=[
            "feature_set.name=wave_anomaly_v1; version=1.3; columns=hmean|hmax|stddev | "
            "file.path=/features/wave_anomaly_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_WAVE_ANOMALY_2025-05; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf | "
            "stakeholder.output_label=Wave Anomaly QC May 2025; audience=science_team; artifact_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_710",
        instruction=(
            "You validate rainfall-intensity feature QC for June-2025. End state: "
            "feature_set 'rain_intensity_v3' (version '3.0') with columns ['avg_rate','peak_rate','duration'] is recorded and readable; "
            "feature file '/features/rain_intensity_v3.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_RAIN_INTENSITY_2025-06' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Rainfall Intensity QC Jun 2025' (audience 'external_partners') references 'https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "rain_intensity_v3", "version": "3.0", "columns": ["avg_rate","peak_rate","duration"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "rain_intensity_v3"}),

            Action(name="insert_file", kwargs={"path": "/features/rain_intensity_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/rain_intensity_v3.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06", "figure_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Rainfall Intensity QC Jun 2025", "audience": "external_partners", "artifact_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Rainfall Intensity QC Jun 2025"}),
        ],
        outputs=[
            "feature_set.name=rain_intensity_v3; version=3.0; columns=avg_rate|peak_rate|duration | "
            "file.path=/features/rain_intensity_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_RAIN_INTENSITY_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf | "
            "stakeholder.output_label=Rainfall Intensity QC Jun 2025; audience=external_partners; artifact_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_714",
        instruction=(
            "You configure an April-2025 model retrain window and validate it. End state: "
            "project config has retrain_window_start '2025-04-01T00:00:00Z' and retrain_window_end '2025-04-30T23:59:59Z' and is readable; "
            "terminal log event 'MODEL_RETRAIN_WINDOW_SET' with message 'April retrain window applied.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_RETRAIN_2025-04' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="update_project_config", kwargs={"updates": {"retrain_window_start": "2025-04-01T00:00:00Z", "retrain_window_end": "2025-04-30T23:59:59Z"}}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_start"}),
            Action(name="get_project_config", kwargs={"key": "retrain_window_end"}),

            Action(name="record_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "April retrain window applied."}),
            Action(name="list_terminal_log", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04", "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-04-01T00:00:00Z; config.retrain_window_end=2025-04-30T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=April retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf"
        ],
    ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_716",
    #     instruction=(
    #         "You set a July-2025 ingestion deadline and validate readiness. End state: "
    #         "project config has ingestion_deadline '2025-07-15T12:00:00Z' and is readable; "
    #         "terminal log event 'INGESTION_DEADLINE_SET' with message 'Deadline established for mid-July ingestion.' exists and is readable; "
    #         "a QC PDF exists for label 'QC_CONFIG_INGESTION_2025-07' with figure record stored (artifact_type 'pdf') and readable."
    #     ),
    #     actions=[
    #         Action(name="update_project_config", kwargs={"updates": {"ingestion_deadline": "2025-07-15T12:00:00Z"}}),
    #         Action(name="get_project_config", kwargs={"key": "ingestion_deadline"}),
    #
    #         Action(name="record_terminal_log", kwargs={"event_type": "INGESTION_DEADLINE_SET", "message": "Deadline established for mid-July ingestion."}),
    #         Action(name="list_terminal_log", kwargs={"event_type": "INGESTION_DEADLINE_SET"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07", "figure_path": "https://storage.example.com/reports/QC_CONFIG_INGESTION_2025-07.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
    #     ],
    #     outputs=[
    #         "config.ingestion_deadline=2025-07-15T12:00:00Z | "
    #         "log.event_type=INGESTION_DEADLINE_SET; log.message=Deadline established for mid-July ingestion. | "
    #         "qc.figure_label=QC_CONFIG_INGESTION_2025-07; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_INGESTION_2025-07.pdf"
    #     ],
    # ),
  Task(
        annotator="R",
        user_id="ds_v3_600",
        instruction=(
            "You publish a September-2025 sea-surface temperature anomaly series with QC. End state: "
            "processed series 'sst_anom_2025-09' has three points [('2025-09-03T00:00:00Z', 0.25), ('2025-09-15T00:00:00Z', -0.12), ('2025-09-28T00:00:00Z', 0.08)] and is readable; "
            "a QC PDF exists for label 'QC_SST_ANOM_2025-09' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sst_anom_2025-09", "items": [
                {"timestamp": "2025-09-03T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-09-15T00:00:00Z", "value": -0.12},
                {"timestamp": "2025-09-28T00:00:00Z", "value": 0.08}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sst_anom_2025-09"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-09", "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
        ],
        outputs=[
            "series.name=sst_anom_2025-09; points=3; p1.ts=2025-09-03T00:00:00Z; p1.value=0.25; p2.ts=2025-09-15T00:00:00Z; p2.value=-0.12; p3.ts=2025-09-28T00:00:00Z; p3.value=0.08 | "
            "qc.figure_label=QC_SST_ANOM_2025-09; qc.figure_path=https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_601",
        instruction=(
            "You publish an October-2025 chlorophyll anomaly series with QC. End state: "
            "processed series 'chl_anom_2025-10' has three points [('2025-10-01T00:00:00Z', 1.15), ('2025-10-12T00:00:00Z', -0.95), ('2025-10-25T00:00:00Z', 0.60)] and is readable; "
            "a QC PDF exists for label 'QC_CHL_ANOM_2025-10' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "chl_anom_2025-10", "items": [
                {"timestamp": "2025-10-01T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-10-12T00:00:00Z", "value": -0.95},
                {"timestamp": "2025-10-25T00:00:00Z", "value": 0.60}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "chl_anom_2025-10"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CHL_ANOM_2025-10", "figure_path": "https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
        ],
        outputs=[
            "series.name=chl_anom_2025-10; points=3; p1.ts=2025-10-01T00:00:00Z; p1.value=1.15; p2.ts=2025-10-12T00:00:00Z; p2.value=-0.95; p3.ts=2025-10-25T00:00:00Z; p3.value=0.60 | "
            "qc.figure_label=QC_CHL_ANOM_2025-10; qc.figure_path=https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_602",
        instruction=(
            "You publish a November-2025 nitrate concentration anomaly series with QC. End state: "
            "processed series 'no3_anom_2025-11' has three points [('2025-11-05T00:00:00Z', 0.55), ('2025-11-16T00:00:00Z', -0.40), ('2025-11-29T00:00:00Z', 0.22)] and is readable; "
            "a QC PDF exists for label 'QC_NO3_ANOM_2025-11' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "no3_anom_2025-11", "items": [
                {"timestamp": "2025-11-05T00:00:00Z", "value": 0.55},
                {"timestamp": "2025-11-16T00:00:00Z", "value": -0.40},
                {"timestamp": "2025-11-29T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "no3_anom_2025-11"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NO3_ANOM_2025-11", "figure_path": "https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
        ],
        outputs=[
            "series.name=no3_anom_2025-11; points=3; p1.ts=2025-11-05T00:00:00Z; p1.value=0.55; p2.ts=2025-11-16T00:00:00Z; p2.value=-0.40; p3.ts=2025-11-29T00:00:00Z; p3.value=0.22 | "
            "qc.figure_label=QC_NO3_ANOM_2025-11; qc.figure_path=https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_603",
        instruction=(
            "You curate feature set 'port_departure_metrics_v1' version 1.1 and activate it. End state: "
            "feature_set 'port_departure_metrics_v1' with columns ['departure_count','avg_wait_time','max_wait_time'] is recorded; "
            "feature file '/features/port_departure_metrics_v1.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'port_departure_metrics_v1'; "
            "a QC PDF exists for label 'QC_PORT_DEPARTURE_2025-03' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "port_departure_metrics_v1", "version": "1.1", "columns": ["departure_count","avg_wait_time","max_wait_time"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "port_departure_metrics_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/port_departure_metrics_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/port_departure_metrics_v1.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "port_departure_metrics_v1"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03", "figure_path": "https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
        ],
        outputs=[
            "feature_set.name=port_departure_metrics_v1; version=1.1; columns=departure_count|avg_wait_time|max_wait_time | "
            "file.path=/features/port_departure_metrics_v1.parquet; file.mime=application/parquet | "
            "config.active_feature_set=port_departure_metrics_v1 | "
            "qc.figure_label=QC_PORT_DEPARTURE_2025-03; qc.figure_path=https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf"
        ],
    ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_604",
    #     instruction=(
    #         "You publish feature set 'cargo_throughput_summary_v3' version 3.0 and mark it active. End state: "
    #         "feature_set 'cargo_throughput_summary_v3' with columns ['total_cargo','avg_loading_time','avg_unloading_time'] is recorded; "
    #         "feature file '/features/cargo_throughput_summary_v3.parquet' exists and is readable; "
    #         "project config 'active_feature_set' equals 'cargo_throughput_summary_v3'; "
    #         "a QC PDF exists for label 'QC_CARGO_THROUGHPUT_2025-03' and is readable."
    #     ),
    #     actions=[
    #         Action(name="insert_feature_set", kwargs={"feature_set_name": "cargo_throughput_summary_v3", "version": "3.0", "columns": ["total_cargo","avg_loading_time","avg_unloading_time"]}),
    #         Action(name="get_feature_set_details", kwargs={"feature_set_name": "cargo_throughput_summary_v3"}),
    #
    #         Action(name="insert_file", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet", "mime_type": "application/parquet"}),
    #         Action(name="get_file", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet"}),
    #
    #         Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "cargo_throughput_summary_v3"}}),
    #         Action(name="get_project_config", kwargs={"key": "active_feature_set"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03", "figure_path": "https://storage.example.com/reports/QC_CARGO_THROUGHPUT_2025-03.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
    #     ],
    #     outputs=[
    #         "feature_set.name=cargo_throughput_summary_v3; version=3.0; columns=total_cargo|avg_loading_time|avg_unloading_time | "
    #         "file.path=/features/cargo_throughput_summary_v3.parquet; file.mime=application/parquet | "
    #         "config.active_feature_set=cargo_throughput_summary_v3 | "
    #         "qc.figure_label=QC_CARGO_THROUGHPUT_2025-03; qc.figure_path=https://storage.example.com/reports/QC_CARGO_THROUGHPUT_2025-03.pdf"
    #     ],
    # ),

    # Task(
    #     annotator="R",
    #     user_id="ds_v3_605",
    #     instruction=(
    #         "You curate feature set 'port_utilization_stats_v4' version 4.2 and activate it. End state: "
    #         "feature_set 'port_utilization_stats_v4' with columns ['berth_occupancy','avg_turnaround_time','peak_traffic_hour'] is recorded; "
    #         "feature file '/features/port_utilization_stats_v4.parquet' exists and is readable; "
    #         "project config 'active_feature_set' equals 'port_utilization_stats_v4'; "
    #         "a QC PDF exists for label 'QC_PORT_UTILIZATION_2025-03' and is readable."
    #     ),
    #     actions=[
    #         Action(name="insert_feature_set", kwargs={"feature_set_name": "port_utilization_stats_v4", "version": "4.2", "columns": ["berth_occupancy","avg_turnaround_time","peak_traffic_hour"]}),
    #         Action(name="get_feature_set_details", kwargs={"feature_set_name": "port_utilization_stats_v4"}),
    #
    #         Action(name="insert_file", kwargs={"path": "/features/port_utilization_stats_v4.parquet", "mime_type": "application/parquet"}),
    #         Action(name="get_file", kwargs={"path": "/features/port_utilization_stats_v4.parquet"}),
    #
    #         Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "port_utilization_stats_v4"}}),
    #         Action(name="get_project_config", kwargs={"key": "active_feature_set"}),
    #
    #         Action(name="export_qc_figure", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
    #         Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03", "figure_path": "https://storage.example.com/reports/QC_PORT_UTILIZATION_2025-03.pdf", "artifact_type": "pdf"}),
    #         Action(name="get_qc_figure", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
    #     ],
    #     outputs=[
    #         "feature_set.name=port_utilization_stats_v4; version=4.2; columns=berth_occupancy|avg_turnaround_time|peak_traffic_hour | "
    #         "file.path=/features/port_utilization_stats_v4.parquet; file.mime=application/parquet | "
    #         "config.active_feature_set=port_utilization_stats_v4 | "
    #         "qc.figure_label=QC_PORT_UTILIZATION_2025-03; qc.figure_path=https://storage.example.com/reports/QC_PORT_UTILIZATION_2025-03.pdf"
    #     ],
    # ),

    Task(
        annotator="R",
        user_id="ds_v3_606",
        instruction=(
            "You create a logistic regression wildfire risk dataset 'wildfire_risk_v1' for 2025‑06. End state: "
            "dataset 'wildfire_risk_v1' (version '1.0') with columns ['temperature','humidity','fire_risk'] is recorded and readable; "
            "feature file '/features/wildfire_risk_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_WILDFIRE_RISK_2025-06' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Wildfire Risk Jun 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "wildfire_risk_v1", "version": "1.0", "columns": ["temperature","humidity","fire_risk"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "wildfire_risk_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/wildfire_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/wildfire_risk_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06", "figure_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Wildfire Risk Jun 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Wildfire Risk Jun 2025"}),
        ],
        outputs=[
            "feature_set.name=wildfire_risk_v1; version=1.0; columns=temperature|humidity|fire_risk | "
            "file.path=/features/wildfire_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_WILDFIRE_RISK_2025-06; qc.figure_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf | "
            "stakeholder.output_label=Wildfire Risk Jun 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_607",
        instruction=(
            "You publish a flood prediction dataset 'flood_forecast_v2' for 2025‑05. End state: "
            "dataset 'flood_forecast_v2' (version '2.0') with columns ['rainfall','river_level','flood_probability'] is recorded and readable; "
            "feature file '/features/flood_forecast_v2.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_FLOOD_FORECAST_2025-05' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Flood Forecast May 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "flood_forecast_v2", "version": "2.0", "columns": ["rainfall","river_level","flood_probability"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "flood_forecast_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/flood_forecast_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/flood_forecast_v2.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05", "figure_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Flood Forecast May 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Flood Forecast May 2025"}),
        ],
        outputs=[
            "feature_set.name=flood_forecast_v2; version=2.0; columns=rainfall|river_level|flood_probability | "
            "file.path=/features/flood_forecast_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_FLOOD_FORECAST_2025-05; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf | "
            "stakeholder.output_label=Flood Forecast May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_608",
        instruction=(
            "You curate air quality prediction dataset 'air_quality_index_v3' for 2025‑07. End state: "
            "dataset 'air_quality_index_v3' (version '3.0') with columns ['PM2_5','PM10','AQI'] is recorded and readable; "
            "feature file '/features/air_quality_index_v3.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_AIR_QUALITY_2025-07' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Air Quality Jul 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "air_quality_index_v3", "version": "3.0", "columns": ["PM2_5","PM10","AQI"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "air_quality_index_v3"}),

            Action(name="insert_file", kwargs={"path": "/features/air_quality_index_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/air_quality_index_v3.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07", "figure_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Air Quality Jul 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Air Quality Jul 2025"}),
        ],
        outputs=[
            "feature_set.name=air_quality_index_v3; version=3.0; columns=PM2_5|PM10|AQI | "
            "file.path=/features/air_quality_index_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_AIR_QUALITY_2025-07; qc.figure_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf | "
            "stakeholder.output_label=Air Quality Jul 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_609",
        instruction=(
            "You publish a coastal erosion prediction dataset 'coastal_erosion_v2' for 2025‑08. End state: "
            "dataset 'coastal_erosion_v2' (version '2.0') with columns ['wave_height','shoreline_change','erosion_risk'] is recorded and readable; "
            "feature file '/features/coastal_erosion_v2.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_COASTAL_EROSION_2025-08' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'Coastal Erosion Aug 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "coastal_erosion_v2", "version": "2.0", "columns": ["wave_height","shoreline_change","erosion_risk"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "coastal_erosion_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/coastal_erosion_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/coastal_erosion_v2.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08", "figure_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Coastal Erosion Aug 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Coastal Erosion Aug 2025"}),
        ],
        outputs=[
            "feature_set.name=coastal_erosion_v2; version=2.0; columns=wave_height|shoreline_change|erosion_risk | "
            "file.path=/features/coastal_erosion_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_COASTAL_EROSION_2025-08; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf | "
            "stakeholder.output_label=Coastal Erosion Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_610",
        instruction=(
            "You prepare May-2025 tidal minima, verify QC, and publish a summary for coastal authorities. "
            "End state: processed series 'tide_min_2025-05' stores three points "
            "[('2025-05-03T00:00:00Z', 0.45), ('2025-05-17T00:00:00Z', 0.32), ('2025-05-30T00:00:00Z', 0.50)] and is retrievable; "
            "a QC figure 'QC_TIDE_MIN_2025-05' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'May 2025 Tide Min Report' (audience 'coastal') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_min_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": 0.45},
                {"timestamp": "2025-05-17T00:00:00Z", "value": 0.32},
                {"timestamp": "2025-05-30T00:00:00Z", "value": 0.50}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_min_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05", "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "May 2025 Tide Min Report", "audience": "coastal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "May 2025 Tide Min Report"}),
        ],
        outputs=[
            "series.name=tide_min_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=0.45; "
            "p2.ts=2025-05-17T00:00:00Z; p2.value=0.32; p3.ts=2025-05-30T00:00:00Z; p3.value=0.50 | "
            "qc.figure_label=QC_TIDE_MIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf | "
            "stakeholder.output_label=May 2025 Tide Min Report; audience=coastal; artifact_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_611",
        instruction=(
            "You process June-2025 high tide series, validate QC, and release an executive briefing. "
            "End state: processed series 'tide_high_2025-06' stores three points "
            "[('2025-06-01T00:00:00Z', 3.55), ('2025-06-14T00:00:00Z', 3.78), ('2025-06-28T00:00:00Z', 3.61)] and is retrievable; "
            "a QC figure 'QC_TIDE_HIGH_2025-06' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'June 2025 Tide High Report' (audience 'executive') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_high_2025-06", "items": [
                {"timestamp": "2025-06-01T00:00:00Z", "value": 3.55},
                {"timestamp": "2025-06-14T00:00:00Z", "value": 3.78},
                {"timestamp": "2025-06-28T00:00:00Z", "value": 3.61}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_high_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06", "figure_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "June 2025 Tide High Report", "audience": "executive", "artifact_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "June 2025 Tide High Report"}),
        ],
        outputs=[
            "series.name=tide_high_2025-06; points=3; p1.ts=2025-06-01T00:00:00Z; p1.value=3.55; "
            "p2.ts=2025-06-14T00:00:00Z; p2.value=3.78; p3.ts=2025-06-28T00:00:00Z; p3.value=3.61 | "
            "qc.figure_label=QC_TIDE_HIGH_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf | "
            "stakeholder.output_label=June 2025 Tide High Report; audience=executive; artifact_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_612",
        instruction=(
            "You compile July-2025 tidal range data, confirm QC, and distribute a municipal briefing. "
            "End state: processed series 'tide_range_2025-07' stores three points "
            "[('2025-07-05T00:00:00Z', 2.67), ('2025-07-18T00:00:00Z', 3.02), ('2025-07-31T00:00:00Z', 2.88)] and is retrievable; "
            "a QC figure 'QC_TIDE_RANGE_2025-07' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'July 2025 Tide Range Report' (audience 'municipal') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_range_2025-07", "items": [
                {"timestamp": "2025-07-05T00:00:00Z", "value": 2.67},
                {"timestamp": "2025-07-18T00:00:00Z", "value": 3.02},
                {"timestamp": "2025-07-31T00:00:00Z", "value": 2.88}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_range_2025-07"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07", "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "July 2025 Tide Range Report", "audience": "municipal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "July 2025 Tide Range Report"}),
        ],
        outputs=[
            "series.name=tide_range_2025-07; points=3; p1.ts=2025-07-05T00:00:00Z; p1.value=2.67; "
            "p2.ts=2025-07-18T00:00:00Z; p2.value=3.02; p3.ts=2025-07-31T00:00:00Z; p3.value=2.88 | "
            "qc.figure_label=QC_TIDE_RANGE_2025-07; qc.figure_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf | "
            "stakeholder.output_label=July 2025 Tide Range Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_613",
        instruction=(
            "You generate August-2025 mean tide series, validate QC, and distribute a briefing for state agencies. "
            "End state: processed series 'tide_mean_2025-08' stores three points "
            "[('2025-08-04T00:00:00Z', 1.87), ('2025-08-17T00:00:00Z', 2.01), ('2025-08-30T00:00:00Z', 1.95)] and is retrievable; "
            "a QC figure 'QC_TIDE_MEAN_2025-08' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'August 2025 Mean Tide Report' (audience 'state') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_mean_2025-08", "items": [
                {"timestamp": "2025-08-04T00:00:00Z", "value": 1.87},
                {"timestamp": "2025-08-17T00:00:00Z", "value": 2.01},
                {"timestamp": "2025-08-30T00:00:00Z", "value": 1.95}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_mean_2025-08"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08", "figure_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "August 2025 Mean Tide Report", "audience": "state", "artifact_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "August 2025 Mean Tide Report"}),
        ],
        outputs=[
            "series.name=tide_mean_2025-08; points=3; p1.ts=2025-08-04T00:00:00Z; p1.value=1.87; "
            "p2.ts=2025-08-17T00:00:00Z; p2.value=2.01; p3.ts=2025-08-30T00:00:00Z; p3.value=1.95 | "
            "qc.figure_label=QC_TIDE_MEAN_2025-08; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf | "
            "stakeholder.output_label=August 2025 Mean Tide Report; audience=state; artifact_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_614",
        instruction=(
            "You prepare May-2025 tidal minima, validate QC, and issue a briefing for coastal management. "
            "End state: processed series 'tide_min_2025-05' stores three points "
            "[('2025-05-03T00:00:00Z', 0.42), ('2025-05-16T00:00:00Z', 0.35), ('2025-05-29T00:00:00Z', 0.50)] and is retrievable; "
            "a QC figure 'QC_TIDE_MIN_2025-05' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'May 2025 Tide Min Report' (audience 'coastal') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_min_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": 0.42},
                {"timestamp": "2025-05-16T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 0.50}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_min_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05", "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "May 2025 Tide Min Report", "audience": "coastal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "May 2025 Tide Min Report"}),
        ],
        outputs=[
            "series.name=tide_min_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=0.42; "
            "p2.ts=2025-05-16T00:00:00Z; p2.value=0.35; p3.ts=2025-05-29T00:00:00Z; p3.value=0.50 | "
            "qc.figure_label=QC_TIDE_MIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf | "
            "stakeholder.output_label=May 2025 Tide Min Report; audience=coastal; artifact_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_615",
        instruction=(
            "You prepare June-2025 high tide series, perform QC validation, and release an executive briefing. "
            "End state: processed series 'tide_high_2025-06' stores three points "
            "[('2025-06-02T00:00:00Z', 3.55), ('2025-06-15T00:00:00Z', 3.78), ('2025-06-28T00:00:00Z', 3.60)] and is retrievable; "
            "a QC figure 'QC_TIDE_HIGH_2025-06' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'June 2025 Tide High Report' (audience 'executive') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_high_2025-06", "items": [
                {"timestamp": "2025-06-02T00:00:00Z", "value": 3.55},
                {"timestamp": "2025-06-15T00:00:00Z", "value": 3.78},
                {"timestamp": "2025-06-28T00:00:00Z", "value": 3.60}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_high_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06", "figure_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_HIGH_2025-06"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "June 2025 Tide High Report", "audience": "executive", "artifact_path": "https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "June 2025 Tide High Report"}),
        ],
        outputs=[
            "series.name=tide_high_2025-06; points=3; p1.ts=2025-06-02T00:00:00Z; p1.value=3.55; "
            "p2.ts=2025-06-15T00:00:00Z; p2.value=3.78; p3.ts=2025-06-28T00:00:00Z; p3.value=3.60 | "
            "qc.figure_label=QC_TIDE_HIGH_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf | "
            "stakeholder.output_label=June 2025 Tide High Report; audience=executive; artifact_path=https://storage.example.com/reports/QC_TIDE_HIGH_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_616",
        instruction=(
            "You generate July-2025 tidal range series, validate QC, and issue a municipal briefing. "
            "End state: processed series 'tide_range_2025-07' stores three points "
            "[('2025-07-04T00:00:00Z', 2.65), ('2025-07-17T00:00:00Z', 3.01), ('2025-07-30T00:00:00Z', 2.87)] and is retrievable; "
            "a QC figure 'QC_TIDE_RANGE_2025-07' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'July 2025 Tide Range Report' (audience 'municipal') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_range_2025-07", "items": [
                {"timestamp": "2025-07-04T00:00:00Z", "value": 2.65},
                {"timestamp": "2025-07-17T00:00:00Z", "value": 3.01},
                {"timestamp": "2025-07-30T00:00:00Z", "value": 2.87}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_range_2025-07"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07", "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "July 2025 Tide Range Report", "audience": "municipal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "July 2025 Tide Range Report"}),
        ],
        outputs=[
            "series.name=tide_range_2025-07; points=3; p1.ts=2025-07-04T00:00:00Z; p1.value=2.65; "
            "p2.ts=2025-07-17T00:00:00Z; p2.value=3.01; p3.ts=2025-07-30T00:00:00Z; p3.value=2.87 | "
            "qc.figure_label=QC_TIDE_RANGE_2025-07; qc.figure_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf | "
            "stakeholder.output_label=July 2025 Tide Range Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_514",
        instruction=(
            "You QC a 25-year NOAA coastal wind dataset. End state: "
            "processed series 'noaa_wind_qc_1995_2020' has summary points [('mean_wind_speed', 12.4), ('max_wind_speed', 29.8)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_WIND_1995_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA Wind QC 1995-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_wind_qc_1995_2020", "items": [
                {"timestamp": "mean_wind_speed", "value": 12.4},
                {"timestamp": "max_wind_speed", "value": 29.8}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_wind_qc_1995_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA Wind QC 1995-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA Wind QC 1995-2020"}),
        ],
        outputs=[
            "series.name=noaa_wind_qc_1995_2020; points=2; p1.ts=mean_wind_speed; p1.value=12.4; p2.ts=max_wind_speed; p2.value=29.8 | "
            "qc.figure_label=QC_NOAA_WIND_1995_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf | "
            "stakeholder.output_label=NOAA Wind QC 1995-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_515",
        instruction=(
            "You QC a 20-year NOAA river discharge dataset. End state: "
            "processed series 'noaa_river_qc_2000_2020' has summary points [('mean_discharge', 350.6), ('max_discharge', 1120.3)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_RIVER_2000_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA River QC 2000-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_river_qc_2000_2020", "items": [
                {"timestamp": "mean_discharge", "value": 350.6},
                {"timestamp": "max_discharge", "value": 1120.3}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_river_qc_2000_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA River QC 2000-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA River QC 2000-2020"}),
        ],
        outputs=[
            "series.name=noaa_river_qc_2000_2020; points=2; p1.ts=mean_discharge; p1.value=350.6; p2.ts=max_discharge; p2.value=1120.3 | "
            "qc.figure_label=QC_NOAA_RIVER_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf | "
            "stakeholder.output_label=NOAA River QC 2000-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_516",
        instruction=(
            "You QC a 15-year NOAA precipitation dataset. End state: "
            "processed series 'noaa_precip_qc_2005_2020' has summary points [('mean_precip', 102.7), ('max_precip_day', 210.5)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_PRECIP_2005_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA Precip QC 2005-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_precip_qc_2005_2020", "items": [
                {"timestamp": "mean_precip", "value": 102.7},
                {"timestamp": "max_precip_day", "value": 210.5}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_precip_qc_2005_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA Precip QC 2005-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA Precip QC 2005-2020"}),
        ],
        outputs=[
            "series.name=noaa_precip_qc_2005_2020; points=2; p1.ts=mean_precip; p1.value=102.7; p2.ts=max_precip_day; p2.value=210.5 | "
            "qc.figure_label=QC_NOAA_PRECIP_2005_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf | "
            "stakeholder.output_label=NOAA Precip QC 2005-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_517",
        instruction=(
            "You QC a 10-year NOAA salinity dataset. End state: "
            "processed series 'noaa_salinity_qc_2010_2020' has summary points [('mean_salinity', 35.1), ('max_salinity', 36.7)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_SALINITY_2010_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA Salinity QC 2010-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_salinity_qc_2010_2020", "items": [
                {"timestamp": "mean_salinity", "value": 35.1},
                {"timestamp": "max_salinity", "value": 36.7}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_salinity_qc_2010_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA Salinity QC 2010-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA Salinity QC 2010-2020"}),
        ],
        outputs=[
            "series.name=noaa_salinity_qc_2010_2020; points=2; p1.ts=mean_salinity; p1.value=35.1; p2.ts=max_salinity; p2.value=36.7 | "
            "qc.figure_label=QC_NOAA_SALINITY_2010_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf | "
            "stakeholder.output_label=NOAA Salinity QC 2010-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_518",
        instruction=(
            "You QC a 12-year NOAA sea surface temperature dataset. End state: "
            "processed series 'noaa_sst_qc_2008_2020' has summary points [('mean_sst', 18.5), ('max_sst', 29.2)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_SST_2008_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA SST QC 2008-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_sst_qc_2008_2020", "items": [
                {"timestamp": "mean_sst", "value": 18.5},
                {"timestamp": "max_sst", "value": 29.2}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_sst_qc_2008_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_SST_2008_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA SST QC 2008-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA SST QC 2008-2020"}),
        ],
        outputs=[
            "series.name=noaa_sst_qc_2008_2020; points=2; p1.ts=mean_sst; p1.value=18.5; p2.ts=max_sst; p2.value=29.2 | "
            "qc.figure_label=QC_NOAA_SST_2008_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf | "
            "stakeholder.output_label=NOAA SST QC 2008-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_411",
        instruction=(
            "You summarize a April‑2025 sales ETL run and notify the finance team. End state: "
            "ETL run 'sales_rollup_2025-04' (task 'monthly_sales_aggregation') status 'completed' rows_processed 420 is recorded and readable; "
            "a QC PDF exists for label 'QC_SALES_2025-04' and is stored; "
            "terminal log event 'SALES_QC_DONE' with message 'April sales aggregation complete.' exists and is readable; "
            "email to 'finance-team@example.com' with subject 'QC_SALES_2025-04', body 'Sales aggregation QC attached.' and attachment URL is sent."
        ),
        actions=[
            Action(name="register_etl_run", kwargs={"run_name": "sales_rollup_2025-04", "task": "monthly_sales_aggregation", "status": "completed", "rows_processed": 420}),
            Action(name="get_etl_run_details", kwargs={"run_name": "sales_rollup_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SALES_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SALES_2025-04", "figure_path": "https://storage.example.com/reports/QC_SALES_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SALES_2025-04"}),

            Action(name="record_terminal_log", kwargs={"event_type": "SALES_QC_DONE", "message": "April sales aggregation complete."}),
            Action(name="list_terminal_log", kwargs={"event_type": "SALES_QC_DONE"}),

            Action(name="send_results_email", kwargs={"to_address": "finance-team@example.com", "subject": "QC_SALES_2025-04", "body_text": "Sales aggregation QC attached.", "attachment": "https://storage.example.com/reports/QC_SALES_2025-04.pdf"}),
        ],
        outputs=[
            "etl.run_name=sales_rollup_2025-04; etl.task=monthly_sales_aggregation; etl.status=completed; etl.rows_processed=420 | "
            "qc.figure_label=QC_SALES_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SALES_2025-04.pdf | "
            "log.event_type=SALES_QC_DONE; log.message=April sales aggregation complete. | "
            "email.to=finance-team@example.com; email.subject=QC_SALES_2025-04; email.attachment=https://storage.example.com/reports/QC_SALES_2025-04.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_300",
        instruction=(
            "You compile January-2025 precipitation totals with QC review and distribute a summary for external partners. "
            "End state: processed series 'precip_total_2025-01' has three points "
            "[('2025-01-05T00:00:00Z', 14.2), ('2025-01-18T00:00:00Z', 9.7), ('2025-01-30T00:00:00Z', 12.5)] and is retrievable; "
            "a QC report PDF labeled 'QC_PRECIP_2025-01' is stored and readable; "
            "stakeholder output 'Jan 2025 Precipitation Summary' (audience 'external') references the QC report."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "precip_total_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 14.2},
                {"timestamp": "2025-01-18T00:00:00Z", "value": 9.7},
                {"timestamp": "2025-01-30T00:00:00Z", "value": 12.5}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "precip_total_2025-01"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_PRECIP_2025-01"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PRECIP_2025-01", "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PRECIP_2025-01"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Jan 2025 Precipitation Summary", "audience": "external", "artifact_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Jan 2025 Precipitation Summary"}),
        ],
        outputs=[
            "series.name=precip_total_2025-01; points=3; p1.ts=2025-01-05T00:00:00Z; p1.value=14.2; "
            "p2.ts=2025-01-18T00:00:00Z; p2.value=9.7; p3.ts=2025-01-30T00:00:00Z; p3.value=12.5 | "
            "qc.figure_label=QC_PRECIP_2025-01; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf | "
            "stakeholder.output_label=Jan 2025 Precipitation Summary; audience=external; artifact_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_302",
        instruction=(
            "You prepare April-2025 tidal height maxima, verify QC, and release a concise update for municipal stakeholders. "
            "End state: processed series 'tide_max_2025-04' stores three points "
            "[('2025-04-02T00:00:00Z', 3.12), ('2025-04-15T00:00:00Z', 3.44), ('2025-04-29T00:00:00Z', 3.21)] and is retrievable; "
            "a QC figure 'QC_TIDE_MAX_2025-04' (artifact_type 'pdf') is stored and accessible; "
            "stakeholder output 'April 2025 Tide Max Report' (audience 'municipal') is linked to the QC document."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_max_2025-04", "items": [
                {"timestamp": "2025-04-02T00:00:00Z", "value": 3.12},
                {"timestamp": "2025-04-15T00:00:00Z", "value": 3.44},
                {"timestamp": "2025-04-29T00:00:00Z", "value": 3.21}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_max_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_MAX_2025-04", "figure_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "April 2025 Tide Max Report", "audience": "municipal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "April 2025 Tide Max Report"}),
        ],
        outputs=[
            "series.name=tide_max_2025-04; points=3; p1.ts=2025-04-02T00:00:00Z; p1.value=3.12; "
            "p2.ts=2025-04-15T00:00:00Z; p2.value=3.44; p3.ts=2025-04-29T00:00:00Z; p3.value=3.21 | "
            "qc.figure_label=QC_TIDE_MAX_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf | "
            "stakeholder.output_label=April 2025 Tide Max Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_305",
        instruction=(
            "You QC a merged coastal wind speed dataset covering 1995–2015. End state: "
            "processed series 'wind_qc_1995_2015' includes [('avg_wind', 12.4), ('max_wind_day', 68.0)] and is retrievable; "
            "a QC report (artifact_type 'pdf') exists with label 'QC_WIND_1995_2015'; "
            "stakeholder output 'Wind QC 1995-2015' (audience 'internal') references 'https://storage.example.com/reports/QC_WIND_1995_2015.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "wind_qc_1995_2015", "items": [
                {"timestamp": "avg_wind", "value": 12.4},
                {"timestamp": "max_wind_day", "value": 68.0}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "wind_qc_1995_2015"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WIND_1995_2015"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WIND_1995_2015", "figure_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WIND_1995_2015"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Wind QC 1995-2015", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Wind QC 1995-2015"}),
        ],
        outputs=[
            "series.name=wind_qc_1995_2015; points=2; p1.ts=avg_wind; p1.value=12.4; p2.ts=max_wind_day; p2.value=68.0 | "
            "qc.figure_label=QC_WIND_1995_2015; qc.figure_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf | "
            "stakeholder.output_label=Wind QC 1995-2015; audience=internal; artifact_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_201",
        instruction=(
            "You configure 'LSTM_StormSurge_v3' and add a July-2025 validation record. "
            "End state: model 'LSTM_StormSurge_v3' (type 'lstm', framework 'tensorflow', version '3.0', status 'staged') is inserted and visible; "
            "validation batch 'VAL_SS_2025-07' has one row ('2025-07-15T03:00:00Z', 1.92) and is retrievable; "
            "validation MAE 0.15 is stored and readable; "
            "QC CSV with label 'QC_SS_VAL_2025-07' is linked and accessible."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "LSTM_StormSurge_v3", "model_type": "lstm", "framework": "tensorflow", "version": "3.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_SS_2025-07", "model_name": "LSTM_StormSurge_v3", "items": [{"timestamp": "2025-07-15T03:00:00Z", "prediction": 1.92}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_SS_2025-07"}),

            Action(name="insert_metrics", kwargs={"model_name": "LSTM_StormSurge_v3", "metric_name": "MAE", "value": 0.15, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SS_VAL_2025-07", "figure_path": "https://storage.example.com/reports/QC_SS_VAL_2025-07.csv", "artifact_type": "csv"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SS_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=LSTM_StormSurge_v3; type=lstm; framework=tensorflow; version=3.0; status=staged | "
            "pred.batch_name=VAL_SS_2025-07; pred.model=LSTM_StormSurge_v3; rows=1; first_ts=2025-07-15T03:00:00Z; first_pred=1.92 | "
            "metric.model=LSTM_StormSurge_v3; metric.name=MAE; metric.value=0.15; split=validation | "
            "qc.figure_label=QC_SS_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_SS_VAL_2025-07.csv"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_202",
        instruction=(
            "You configure 'ARIMA_Precip_v1' and add an August-2025 validation record. "
            "End state: model 'ARIMA_Precip_v1' (type 'arima', framework 'statsmodels', version '1.0', status 'staged') is inserted and visible; "
            "validation batch 'VAL_PC_2025-08' has one row ('2025-08-05T12:00:00Z', 5.7) and is retrievable; "
            "validation R² 0.89 is stored and readable; "
            "QC PDF with label 'QC_PC_VAL_2025-08' is linked and accessible."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "ARIMA_Precip_v1", "model_type": "arima", "framework": "statsmodels", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_PC_2025-08", "model_name": "ARIMA_Precip_v1", "items": [{"timestamp": "2025-08-05T12:00:00Z", "prediction": 5.7}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_PC_2025-08"}),

            Action(name="insert_metrics", kwargs={"model_name": "ARIMA_Precip_v1", "metric_name": "R2", "value": 0.89, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PC_VAL_2025-08", "figure_path": "https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PC_VAL_2025-08"}),
        ],
        outputs=[
            "model.name=ARIMA_Precip_v1; type=arima; framework=statsmodels; version=1.0; status=staged | "
            "pred.batch_name=VAL_PC_2025-08; pred.model=ARIMA_Precip_v1; rows=1; first_ts=2025-08-05T12:00:00Z; first_pred=5.7 | "
            "metric.model=ARIMA_Precip_v1; metric.name=R2; metric.value=0.89; split=validation | "
            "qc.figure_label=QC_PC_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_203",
        instruction=(
            "You configure 'RandomForest_Wind_v5' and add a September-2025 validation record. "
            "End state: model 'RandomForest_Wind_v5' (type 'random_forest', framework 'sklearn', version '5.0', status 'staged') is inserted and visible; "
            "validation batch 'VAL_WD_2025-09' has one row ('2025-09-18T15:00:00Z', 12.6) and is retrievable; "
            "validation RMSE 1.2 is stored and readable; "
            "QC PNG with label 'QC_WD_VAL_2025-09' is linked and accessible."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "RandomForest_Wind_v5", "model_type": "random_forest", "framework": "sklearn", "version": "5.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_WD_2025-09", "model_name": "RandomForest_Wind_v5", "items": [{"timestamp": "2025-09-18T15:00:00Z", "prediction": 12.6}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_WD_2025-09"}),

            Action(name="insert_metrics", kwargs={"model_name": "RandomForest_Wind_v5", "metric_name": "RMSE", "value": 1.2, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-09", "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-09.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-09"}),
        ],
        outputs=[
            "model.name=RandomForest_Wind_v5; type=random_forest; framework=sklearn; version=5.0; status=staged | "
            "pred.batch_name=VAL_WD_2025-09; pred.model=RandomForest_Wind_v5; rows=1; first_ts=2025-09-18T15:00:00Z; first_pred=12.6 | "
            "metric.model=RandomForest_Wind_v5; metric.name=RMSE; metric.value=1.2; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-09.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_206",
        instruction=(
            "You curate feature set 'precip_extremes_v1' (version '1.0') with columns "
            "['daily_rainfall_max','monthly_rainfall_mean','extreme_event_count'] and activate it. End state: "
            "feature set is retrievable; feature file '/features/precip_extremes_v1.parquet' is present and valid; "
            "project config 'climate_features' equals 'precip_extremes_v1'; QC report 'QC_PRECIP_2025-08' exists as a PDF."
        ),
        actions=[
            Action(
                name="insert_feature_set",
                kwargs={
                    "feature_set_name": "precip_extremes_v1",
                    "version": "1.0",
                    "columns": ["daily_rainfall_max","monthly_rainfall_mean","extreme_event_count"]
                }
            ),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "precip_extremes_v1"}),

            Action(
                name="insert_file",
                kwargs={"path": "/features/precip_extremes_v1.parquet", "mime_type": "application/parquet"}
            ),
            Action(name="get_file", kwargs={"path": "/features/precip_extremes_v1.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"climate_features": "precip_extremes_v1"}}),
            Action(name="get_project_config", kwargs={"key": "climate_features"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_PRECIP_2025-08"}),
            Action(
                name="insert_qc_figure",
                kwargs={
                    "figure_label": "QC_PRECIP_2025-08",
                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-08.pdf",
                    "artifact_type": "pdf"
                }
            ),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PRECIP_2025-08"})
        ],
        outputs=[
            "feature_set.name=precip_extremes_v1; version=1.0; columns=daily_rainfall_max|monthly_rainfall_mean|extreme_event_count | "
            "file.path=/features/precip_extremes_v1.parquet; file.mime=application/parquet | "
            "config.climate_features=precip_extremes_v1 | "
            "qc.figure_label=QC_PRECIP_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-08.pdf"
        ]
    ),

    Task(
        annotator="R",
        user_id="ds_v3_211",
        instruction=(
            "You QC a merged satellite rainfall dataset covering 2000–2020. End state: "
            "processed series 'rainfall_sat_qc_2000_2020' includes [('avg_rainfall', 114.6), ('max_rainfall_day', 312.0)] and is retrievable; "
            "a QC report (artifact_type 'pdf') exists with label 'QC_RAINFALL_SAT_2000_2020'; "
            "stakeholder output 'Rainfall QC 2000-2020' (audience 'external') references 'https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "rainfall_sat_qc_2000_2020", "items": [
                {"timestamp": "avg_rainfall", "value": 114.6},
                {"timestamp": "max_rainfall_day", "value": 312.0}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "rainfall_sat_qc_2000_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020", "figure_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Rainfall QC 2000-2020", "audience": "external", "artifact_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Rainfall QC 2000-2020"}),
        ],
        outputs=[
            "series.name=rainfall_sat_qc_2000_2020; points=2; p1.ts=avg_rainfall; p1.value=114.6; p2.ts=max_rainfall_day; p2.value=312.0 | "
            "qc.figure_label=QC_RAINFALL_SAT_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf | "
            "stakeholder.output_label=Rainfall QC 2000-2020; audience=external; artifact_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_213",
        instruction=(
            "You QC 25-year global CO₂ concentration records. End state: "
            "processed series 'co2_qc_1990_2015' has [('avg_co2_ppm', 402.5), ('max_co2_ppm', 419.1)] and is retrievable; "
            "a QC PDF report with label 'QC_CO2_1990_2015' is available; "
            "stakeholder output 'Global CO₂ QC 1990-2015' (audience 'external') links to 'https://storage.example.com/reports/QC_CO2_1990_2015.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "co2_qc_1990_2015", "items": [
                {"timestamp": "avg_co2_ppm", "value": 402.5},
                {"timestamp": "max_co2_ppm", "value": 419.1}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "co2_qc_1990_2015"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CO2_1990_2015"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CO2_1990_2015", "figure_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CO2_1990_2015"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Global CO₂ QC 1990-2015", "audience": "external", "artifact_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Global CO₂ QC 1990-2015"}),
        ],
        outputs=[
            "series.name=co2_qc_1990_2015; points=2; p1.ts=avg_co2_ppm; p1.value=402.5; p2.ts=max_co2_ppm; p2.value=419.1 | "
            "qc.figure_label=QC_CO2_1990_2015; qc.figure_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf | "
            "stakeholder.output_label=Global CO₂ QC 1990-2015; audience=external; artifact_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_214",
        instruction=(
            "You QC river discharge measurements for the Amazon basin (1980–2010). End state: "
            "processed series 'amazon_discharge_qc_1980_2010' contains [('avg_discharge', 85000.0), ('peak_discharge', 120000.0)] and is retrievable; "
            "a QC figure labeled 'QC_AMAZON_DISCHARGE_1980_2010' (pdf) is stored; "
            "stakeholder output 'Amazon River Discharge QC 1980-2010' (audience 'internal') points to 'https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "amazon_discharge_qc_1980_2010", "items": [
                {"timestamp": "avg_discharge", "value": 85000.0},
                {"timestamp": "peak_discharge", "value": 120000.0}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "amazon_discharge_qc_1980_2010"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010", "figure_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Amazon River Discharge QC 1980-2010", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Amazon River Discharge QC 1980-2010"}),
        ],
        outputs=[
            "series.name=amazon_discharge_qc_1980_2010; points=2; p1.ts=avg_discharge; p1.value=85000.0; p2.ts=peak_discharge; p2.value=120000.0 | "
            "qc.figure_label=QC_AMAZON_DISCHARGE_1980_2010; qc.figure_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf | "
            "stakeholder.output_label=Amazon River Discharge QC 1980-2010; audience=internal; artifact_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"
        ],
    ),
     Task(
        annotator="R",
        user_id="ds_v3_125",
        instruction=(
            "You stage 'ARIMA_Tide_v2' and log a May-2025 validation batch with QC. "
            "End state: model 'ARIMA_Tide_v2' (type 'arima', framework 'statsmodels', version '2.0', status 'staged') is recorded and queryable; "
            "validation batch 'VAL_TIDE_2025-05' has one row ('2025-05-09T00:00:00Z', 1.45) and is retrievable; "
            "validation MAPE 7.8 is stored and readable; "
            "QC PDF exists for label 'QC_TIDE_VAL_2025-05' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "ARIMA_Tide_v2", "model_type": "arima", "framework": "statsmodels", "version": "2.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_TIDE_2025-05", "model_name": "ARIMA_Tide_v2", "items": [{"timestamp": "2025-05-09T00:00:00Z", "prediction": 1.45}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_TIDE_2025-05"}),

            Action(name="insert_metrics", kwargs={"model_name": "ARIMA_Tide_v2", "metric_name": "MAPE", "value": 7.8, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_VAL_2025-05", "figure_path": "https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=ARIMA_Tide_v2; type=arima; framework=statsmodels; version=2.0; status=staged | "
            "pred.batch_name=VAL_TIDE_2025-05; pred.model=ARIMA_Tide_v2; rows=1; first_ts=2025-05-09T00:00:00Z; first_pred=1.45 | "
            "metric.model=ARIMA_Tide_v2; metric.name=MAPE; metric.value=7.8; split=validation | "
            "qc.figure_label=QC_TIDE_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_124",
        instruction=(
            "You stage 'GRU_Temperature_v1' and log a June-2025 validation batch with QC. "
            "End state: model 'GRU_Temperature_v1' (type 'gru', framework 'pytorch', version '1.0', status 'staged') is stored and queryable; "
            "validation batch 'VAL_TEMP_2025-06' has one row ('2025-06-18T12:00:00Z', 27.6) and is retrievable; "
            "validation MAE 0.3 is recorded; "
            "QC PNG exists for label 'QC_TEMP_VAL_2025-06' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "GRU_Temperature_v1", "model_type": "gru", "framework": "pytorch", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_TEMP_2025-06", "model_name": "GRU_Temperature_v1", "items": [{"timestamp": "2025-06-18T12:00:00Z", "prediction": 27.6}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_TEMP_2025-06"}),

            Action(name="insert_metrics", kwargs={"model_name": "GRU_Temperature_v1", "metric_name": "MAE", "value": 0.3, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TEMP_VAL_2025-06", "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TEMP_VAL_2025-06"}),
        ],
        outputs=[
            "model.name=GRU_Temperature_v1; type=gru; framework=pytorch; version=1.0; status=staged | "
            "pred.batch_name=VAL_TEMP_2025-06; pred.model=GRU_Temperature_v1; rows=1; first_ts=2025-06-18T12:00:00Z; first_pred=27.6 | "
            "metric.model=GRU_Temperature_v1; metric.name=MAE; metric.value=0.3; split=validation | "
            "qc.figure_label=QC_TEMP_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_123",
        instruction=(
            "You stage 'XGBoost_FloodRisk_v1' and log a July-2025 validation batch with QC. "
            "End state: model 'XGBoost_FloodRisk_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is recorded and queryable; "
            "validation batch 'VAL_FR_2025-07' has one row ('2025-07-20T00:00:00Z', 0.34) and is retrievable; "
            "validation RMSE 0.05 is stored and readable; "
            "QC PDF exists for label 'QC_FR_VAL_2025-07' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "XGBoost_FloodRisk_v1", "model_type": "xgboost", "framework": "xgboost", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_FR_2025-07", "model_name": "XGBoost_FloodRisk_v1", "items": [{"timestamp": "2025-07-20T00:00:00Z", "prediction": 0.34}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_FR_2025-07"}),

            Action(name="insert_metrics", kwargs={"model_name": "XGBoost_FloodRisk_v1", "metric_name": "RMSE", "value": 0.05, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FR_VAL_2025-07", "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FR_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=XGBoost_FloodRisk_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "pred.batch_name=VAL_FR_2025-07; pred.model=XGBoost_FloodRisk_v1; rows=1; first_ts=2025-07-20T00:00:00Z; first_pred=0.34 | "
            "metric.model=XGBoost_FloodRisk_v1; metric.name=RMSE; metric.value=0.05; split=validation | "
            "qc.figure_label=QC_FR_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_122",
        instruction=(
            "You stage 'CNN_WaveHeight_v1' and log a September-2025 validation batch with QC. "
            "End state: model 'CNN_WaveHeight_v1' (type 'cnn', framework 'tensorflow', version '1.0', status 'staged') is stored and queryable; "
            "validation batch 'VAL_WH_2025-09' has one row ('2025-09-05T06:00:00Z', 1.72) and is retrievable; "
            "validation MAE 0.12 is stored and readable; "
            "QC PNG with label 'QC_WH_VAL_2025-09' is stored and retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "CNN_WaveHeight_v1", "model_type": "cnn", "framework": "tensorflow", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_WH_2025-09", "model_name": "CNN_WaveHeight_v1", "items": [{"timestamp": "2025-09-05T06:00:00Z", "prediction": 1.72}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_WH_2025-09"}),

            Action(name="insert_metrics", kwargs={"model_name": "CNN_WaveHeight_v1", "metric_name": "MAE", "value": 0.12, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WH_VAL_2025-09", "figure_path": "https://storage.example.com/reports/QC_WH_VAL_2025-09.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WH_VAL_2025-09"}),
        ],
        outputs=[
            "model.name=CNN_WaveHeight_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | "
            "pred.batch_name=VAL_WH_2025-09; pred.model=CNN_WaveHeight_v1; rows=1; first_ts=2025-09-05T06:00:00Z; first_pred=1.72 | "
            "metric.model=CNN_WaveHeight_v1; metric.name=MAE; metric.value=0.12; split=validation | "
            "qc.figure_label=QC_WH_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WH_VAL_2025-09.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_121",
        instruction=(
            "You stage 'LSTM_Rainfall_v2' and log an August-2025 validation batch with QC. "
            "End state: model 'LSTM_Rainfall_v2' (type 'lstm', framework 'pytorch', version '2.0', status 'staged') is stored and queryable; "
            "validation batch 'VAL_RF_2025-08' has one row ('2025-08-10T12:00:00Z', 22.5) and is retrievable; "
            "validation RMSE 1.05 is recorded and readable; "
            "QC PDF with label 'QC_RF_VAL_2025-08' is stored and retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "LSTM_Rainfall_v2", "model_type": "lstm", "framework": "pytorch", "version": "2.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_RF_2025-08", "model_name": "LSTM_Rainfall_v2", "items": [{"timestamp": "2025-08-10T12:00:00Z", "prediction": 22.5}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_RF_2025-08"}),

            Action(name="insert_metrics", kwargs={"model_name": "LSTM_Rainfall_v2", "metric_name": "RMSE", "value": 1.05, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RF_VAL_2025-08", "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RF_VAL_2025-08"}),
        ],
        outputs=[
            "model.name=LSTM_Rainfall_v2; type=lstm; framework=pytorch; version=2.0; status=staged | "
            "pred.batch_name=VAL_RF_2025-08; pred.model=LSTM_Rainfall_v2; rows=1; first_ts=2025-08-10T12:00:00Z; first_pred=22.5 | "
            "metric.model=LSTM_Rainfall_v2; metric.name=RMSE; metric.value=1.05; split=validation | "
            "qc.figure_label=QC_RF_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_120",
        instruction=(
            "You stage 'CNN_FloodExtent_v1' and log a July-2025 validation record. "
            "End state: model 'CNN_FloodExtent_v1' (type 'cnn', framework 'tensorflow', version '1.0', status 'staged') is recorded and queryable; "
            "validation batch 'VAL_FE_2025-07' has one row ('2025-07-12T15:00:00Z', 0.88) and is retrievable; "
            "validation MAE 0.09 is stored and readable; "
            "QC PNG exists for label 'QC_FE_VAL_2025-07' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "CNN_FloodExtent_v1", "model_type": "cnn", "framework": "tensorflow", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_FE_2025-07", "model_name": "CNN_FloodExtent_v1", "items": [{"timestamp": "2025-07-12T15:00:00Z", "prediction": 0.88}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_FE_2025-07"}),

            Action(name="insert_metrics", kwargs={"model_name": "CNN_FloodExtent_v1", "metric_name": "MAE", "value": 0.09, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FE_VAL_2025-07", "figure_path": "https://storage.example.com/reports/QC_FE_VAL_2025-07.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FE_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=CNN_FloodExtent_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | "
            "pred.batch_name=VAL_FE_2025-07; pred.model=CNN_FloodExtent_v1; rows=1; first_ts=2025-07-12T15:00:00Z; first_pred=0.88 | "
            "metric.model=CNN_FloodExtent_v1; metric.name=MAE; metric.value=0.09; split=validation | "
            "qc.figure_label=QC_FE_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FE_VAL_2025-07.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_119",
        instruction=(
            "You stage 'GRU_Rainfall_v1' and log a June-2025 validation record. "
            "End state: model 'GRU_Rainfall_v1' (type 'gru', framework 'pytorch', version '1.0', status 'staged') is stored and queryable; "
            "validation batch 'VAL_RF_2025-06' has one row ('2025-06-15T09:00:00Z', 15.3) and is retrievable; "
            "validation RMSE 1.2 is recorded and readable; "
            "QC PDF with label 'QC_RF_VAL_2025-06' is stored and retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "GRU_Rainfall_v1", "model_type": "gru", "framework": "pytorch", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_RF_2025-06", "model_name": "GRU_Rainfall_v1", "items": [{"timestamp": "2025-06-15T09:00:00Z", "prediction": 15.3}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_RF_2025-06"}),

            Action(name="insert_metrics", kwargs={"model_name": "GRU_Rainfall_v1", "metric_name": "RMSE", "value": 1.2, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RF_VAL_2025-06", "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RF_VAL_2025-06"}),
        ],
        outputs=[
            "model.name=GRU_Rainfall_v1; type=gru; framework=pytorch; version=1.0; status=staged | "
            "pred.batch_name=VAL_RF_2025-06; pred.model=GRU_Rainfall_v1; rows=1; first_ts=2025-06-15T09:00:00Z; first_pred=15.3 | "
            "metric.model=GRU_Rainfall_v1; metric.name=RMSE; metric.value=1.2; split=validation | "
            "qc.figure_label=QC_RF_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_117",
        instruction=(
            "You onboard 'RF_Temperature_v3' and log a May-2025 validation dataset. "
            "End state: model 'RF_Temperature_v3' (type 'random_forest', framework 'sklearn', version '3.1', status 'staged') is persisted; "
            "validation batch 'VAL_TEMP_2025-05' contains one entry ('2025-05-05T00:00:00Z', 18.7) and is accessible; "
            "R² score 0.91 is registered; "
            "a QC PDF report 'QC_TEMP_VAL_2025-05' is generated and stored."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "RF_Temperature_v3", "model_type": "random_forest", "framework": "sklearn", "version": "3.1", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_TEMP_2025-05", "model_name": "RF_Temperature_v3", "items": [{"timestamp": "2025-05-05T00:00:00Z", "prediction": 18.7}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_TEMP_2025-05"}),

            Action(name="insert_metrics", kwargs={"model_name": "RF_Temperature_v3", "metric_name": "R2", "value": 0.91, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TEMP_VAL_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TEMP_VAL_2025-05", "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TEMP_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=RF_Temperature_v3; type=random_forest; framework=sklearn; version=3.1; status=staged | "
            "pred.batch_name=VAL_TEMP_2025-05; pred.model=RF_Temperature_v3; rows=1; first_ts=2025-05-05T00:00:00Z; first_pred=18.7 | "
            "metric.model=RF_Temperature_v3; metric.name=R2; metric.value=0.91; split=validation | "
            "qc.figure_label=QC_TEMP_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_115",
        instruction=(
            "You configure 'Prophet_TideCycle_v1' and add a May-2025 validation record. "
            "End state: model 'Prophet_TideCycle_v1' (type 'prophet', framework 'prophet', version '1.0', status 'staged') is inserted and visible; "
            "validation batch 'VAL_TC_2025-05' has one row ('2025-05-20T06:00:00Z', 2.44) and is retrievable; "
            "validation MAPE 4.5 is stored and readable; "
            "QC PDF with label 'QC_TC_VAL_2025-05' is linked and accessible."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "Prophet_TideCycle_v1", "model_type": "prophet", "framework": "prophet", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_TC_2025-05", "model_name": "Prophet_TideCycle_v1", "items": [{"timestamp": "2025-05-20T06:00:00Z", "prediction": 2.44}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_TC_2025-05"}),

            Action(name="insert_metrics", kwargs={"model_name": "Prophet_TideCycle_v1", "metric_name": "MAPE", "value": 4.5, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TC_VAL_2025-05", "figure_path": "https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TC_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=Prophet_TideCycle_v1; type=prophet; framework=prophet; version=1.0; status=staged | "
            "pred.batch_name=VAL_TC_2025-05; pred.model=Prophet_TideCycle_v1; rows=1; first_ts=2025-05-20T06:00:00Z; first_pred=2.44 | "
            "metric.model=Prophet_TideCycle_v1; metric.name=MAPE; metric.value=4.5; split=validation | "
            "qc.figure_label=QC_TC_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_114",
        instruction=(
            "You set up 'XGB_WindDamage_v1' and capture a February-2025 validation dataset. "
            "End state: model 'XGB_WindDamage_v1' (type 'xgboost', framework 'xgboost', version '1.6', status 'staged') is saved; "
            "validation batch 'VAL_WD_2025-02' has one row ('2025-02-14T18:00:00Z', 12.8) and is queryable; "
            "validation MAE 1.7 is stored and retrievable; "
            "QC PDF exists for label 'QC_WD_VAL_2025-02' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "XGB_WindDamage_v1", "model_type": "xgboost", "framework": "xgboost", "version": "1.6", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_WD_2025-02", "model_name": "XGB_WindDamage_v1", "items": [{"timestamp": "2025-02-14T18:00:00Z", "prediction": 12.8}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_WD_2025-02"}),

            Action(name="insert_metrics", kwargs={"model_name": "XGB_WindDamage_v1", "metric_name": "MAE", "value": 1.7, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-02", "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WD_VAL_2025-02"}),
        ],
        outputs=[
            "model.name=XGB_WindDamage_v1; type=xgboost; framework=xgboost; version=1.6; status=staged | "
            "pred.batch_name=VAL_WD_2025-02; pred.model=XGB_WindDamage_v1; rows=1; first_ts=2025-02-14T18:00:00Z; first_pred=12.8 | "
            "metric.model=XGB_WindDamage_v1; metric.name=MAE; metric.value=1.7; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-02; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_113",
        instruction=(
            "You register 'LSTM_FloodRisk_v2' and log an April-2025 validation run. "
            "End state: model 'LSTM_FloodRisk_v2' (type 'lstm', framework 'tensorflow', version '2.0', status 'staged') "
            "is stored and queryable; validation batch 'VAL_FR_2025-04' has one row ('2025-04-05T12:00:00Z', 0.76) and is retrievable; "
            "validation RMSE 0.32 is logged and accessible; "
            "QC PNG exists for label 'QC_FR_VAL_2025-04' and is retrievable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "LSTM_FloodRisk_v2", "model_type": "lstm", "framework": "tensorflow", "version": "2.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="insert_prediction_batch", kwargs={"batch_name": "VAL_FR_2025-04", "model_name": "LSTM_FloodRisk_v2", "items": [{"timestamp": "2025-04-05T12:00:00Z", "prediction": 0.76}]}),
            Action(name="get_predictions", kwargs={"batch_name": "VAL_FR_2025-04"}),

            Action(name="insert_metrics", kwargs={"model_name": "LSTM_FloodRisk_v2", "metric_name": "RMSE", "value": 0.32, "dataset_split": "validation"}),
            Action(name="get_metrics", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FR_VAL_2025-04", "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-04.png", "artifact_type": "png"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FR_VAL_2025-04"}),
        ],
        outputs=[
            "model.name=LSTM_FloodRisk_v2; type=lstm; framework=tensorflow; version=2.0; status=staged | "
            "pred.batch_name=VAL_FR_2025-04; pred.model=LSTM_FloodRisk_v2; rows=1; first_ts=2025-04-05T12:00:00Z; first_pred=0.76 | "
            "metric.model=LSTM_FloodRisk_v2; metric.name=RMSE; metric.value=0.32; split=validation | "
            "qc.figure_label=QC_FR_VAL_2025-04; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-04.png"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_112",
        instruction=(
            "You should process the December-2024 salinity anomaly dataset, record QC validation, and send the internal report. "
            "End state: processed series 'sal_anom_2024-12' has four points, QC artifact 'QC_SAL_ANOM_2024-12.pdf' is stored, "
            "and stakeholder output labeled 'Salinity Anomaly Dec 2024' for audience 'internal' references the PDF."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sal_anom_2024-12", "items": [
                {"timestamp": "2024-12-03T00:00:00Z", "value": 0.12},
                {"timestamp": "2024-12-10T00:00:00Z", "value": -0.04},
                {"timestamp": "2024-12-18T00:00:00Z", "value": 0.05},
                {"timestamp": "2024-12-27T00:00:00Z", "value": 0.09}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sal_anom_2024-12"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2024-12", "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Dec 2024", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Dec 2024"}),
        ],
        outputs=[
            "series.name=sal_anom_2024-12; points=4; p1.ts=2024-12-03T00:00:00Z; p1.value=0.12; p2.ts=2024-12-10T00:00:00Z; p2.value=-0.04; p3.ts=2024-12-18T00:00:00Z; p3.value=0.05; p4.ts=2024-12-27T00:00:00Z; p4.value=0.09 | "
            "qc.figure_label=QC_SAL_ANOM_2024-12; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf | "
            "stakeholder.output_label=Salinity Anomaly Dec 2024; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_111",
        instruction=(
            "You need to generate a January-2025 tidal harmonic series, attach QC results, and publish an external summary. "
            "End state: harmonic series 'tidal_harm_2025-01' has three points, QC artifact 'QC_TIDAL_HARM_2025-01.pdf' is stored, "
            "and stakeholder output labeled 'Tidal Harmonics Jan 2025' for audience 'external' references the PDF."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tidal_harm_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 1.21},
                {"timestamp": "2025-01-15T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-01-25T00:00:00Z", "value": 1.18}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tidal_harm_2025-01"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01", "figure_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Tidal Harmonics Jan 2025", "audience": "external", "artifact_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Tidal Harmonics Jan 2025"}),
        ],
        outputs=[
            "series.name=tidal_harm_2025-01; points=3; p1.ts=2025-01-05T00:00:00Z; p1.value=1.21; p2.ts=2025-01-15T00:00:00Z; p2.value=1.15; p3.ts=2025-01-25T00:00:00Z; p3.value=1.18 | "
            "qc.figure_label=QC_TIDAL_HARM_2025-01; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf | "
            "stakeholder.output_label=Tidal Harmonics Jan 2025; audience=external; artifact_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_110",
        instruction=(
            "You should compute a February-2025 surge residual series, archive it, and distribute the QC output. "
            "End state: residual series 'surge_resid_2025-02' has four points, QC artifact 'QC_SURGE_RESID_2025-02.pdf' is stored, "
            "and an internal stakeholder summary labeled 'Feb 2025 Surge Residual' references the PDF."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "surge_resid_2025-02", "items": [
                {"timestamp": "2025-02-02T00:00:00Z", "value": -0.11},
                {"timestamp": "2025-02-10T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-02-18T00:00:00Z", "value": 0.02},
                {"timestamp": "2025-02-26T00:00:00Z", "value": -0.05}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "surge_resid_2025-02"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SURGE_RESID_2025-02", "figure_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Feb 2025 Surge Residual", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Feb 2025 Surge Residual"}),
        ],
        outputs=[
            "series.name=surge_resid_2025-02; points=4; p1.ts=2025-02-02T00:00:00Z; p1.value=-0.11; p2.ts=2025-02-10T00:00:00Z; p2.value=0.07; p3.ts=2025-02-18T00:00:00Z; p3.value=0.02; p4.ts=2025-02-26T00:00:00Z; p4.value=-0.05 | "
            "qc.figure_label=QC_SURGE_RESID_2025-02; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf | "
            "stakeholder.output_label=Feb 2025 Surge Residual; audience=internal; artifact_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_109",
        instruction=(
            "You should publish June-2025 salinity index results with QC. "
            "End state: processed series 'sal_index_2025-06' holds points "
            "[('2025-06-04T00:00:00Z', 33.1), ('2025-06-16T00:00:00Z', 34.2), ('2025-06-29T00:00:00Z', 32.8)] "
            "and a QC report with label 'QC_SAL_INDEX_2025-06' is available."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sal_index_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 33.1},
                {"timestamp": "2025-06-16T00:00:00Z", "value": 34.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": 32.8}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sal_index_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_INDEX_2025-06", "figure_path": "https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
        ],
        outputs=[
            "series.name=sal_index_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=33.1; p2.ts=2025-06-16T00:00:00Z; p2.value=34.2; p3.ts=2025-06-29T00:00:00Z; p3.value=32.8 | "
            "qc.figure_label=QC_SAL_INDEX_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_108",
        instruction=(
            "You need to create a May-2025 rainfall deviation series and ensure QC is generated. "
            "End state: processed series 'rain_dev_2025-05' contains "
            "[('2025-05-03T00:00:00Z', -5.1), ('2025-05-12T00:00:00Z', 2.4), ('2025-05-25T00:00:00Z', -1.7)]; "
            "a QC figure is available under label 'QC_RAIN_DEV_2025-05' with stored path."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "rain_dev_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": -5.1},
                {"timestamp": "2025-05-12T00:00:00Z", "value": 2.4},
                {"timestamp": "2025-05-25T00:00:00Z", "value": -1.7}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "rain_dev_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RAIN_DEV_2025-05", "figure_path": "https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
        ],
        outputs=[
            "series.name=rain_dev_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=-5.1; p2.ts=2025-05-12T00:00:00Z; p2.value=2.4; p3.ts=2025-05-25T00:00:00Z; p3.value=-1.7 | "
            "qc.figure_label=QC_RAIN_DEV_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_107",
        instruction=(
            "You should publish the April-2025 temperature anomaly series with QC validation. "
            "End state: processed series 'temp_anom_2025-04' has three points "
            "[('2025-04-05T00:00:00Z', 1.2), ('2025-04-15T00:00:00Z', -0.3), ('2025-04-27T00:00:00Z', 0.6)] "
            "and is readable; a QC PDF exists for label 'QC_TEMP_ANOM_2025-04' and is stored in artifact_type 'pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-15T00:00:00Z", "value": -0.3},
                {"timestamp": "2025-04-27T00:00:00Z", "value": 0.6}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04", "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
        ],
        outputs=[
            "series.name=temp_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=1.2; p2.ts=2025-04-15T00:00:00Z; p2.value=-0.3; p3.ts=2025-04-27T00:00:00Z; p3.value=0.6 | "
            "qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_106",
        instruction=(
            "You should create a June-2025 salinity anomaly dataset with a QC check. "
            "End state: processed series 'sal_anom_2025-06' has two points "
            "[('2025-06-12T00:00:00Z', 0.5), ('2025-06-22T00:00:00Z', -0.1)] and is available; "
            "QC record 'QC_SAL_ANOM_2025-06' exists as PDF and is retrievable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sal_anom_2025-06", "items": [
                {"timestamp": "2025-06-12T00:00:00Z", "value": 0.5},
                {"timestamp": "2025-06-22T00:00:00Z", "value": -0.1}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sal_anom_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-06", "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=sal_anom_2025-06; points=2; p1.ts=2025-06-12T00:00:00Z; p1.value=0.5; p2.ts=2025-06-22T00:00:00Z; p2.value=-0.1 | "
            "qc.figure_label=QC_SAL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_105",
        instruction=(
            "You should generate a May-2025 rainfall anomaly report with QC validation. "
            "End state: processed series 'rain_anom_2025-05' has three points "
            "[('2025-05-05T00:00:00Z', 12.0), ('2025-05-15T00:00:00Z', -3.2), ('2025-05-25T00:00:00Z', 4.7)] and is retrievable; "
            "a QC artifact with label 'QC_RAIN_ANOM_2025-05' is stored as PDF and readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "rain_anom_2025-05", "items": [
                {"timestamp": "2025-05-05T00:00:00Z", "value": 12.0},
                {"timestamp": "2025-05-15T00:00:00Z", "value": -3.2},
                {"timestamp": "2025-05-25T00:00:00Z", "value": 4.7}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "rain_anom_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05", "figure_path": "https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),
        ],
        outputs=[
            "series.name=rain_anom_2025-05; points=3; p1.ts=2025-05-05T00:00:00Z; p1.value=12.0; p2.ts=2025-05-15T00:00:00Z; p2.value=-3.2; p3.ts=2025-05-25T00:00:00Z; p3.value=4.7 | "
            "qc.figure_label=QC_RAIN_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_104",
        instruction=(
            "You should publish the April-2025 temperature anomaly dataset with QC verification. "
            "End state: processed series 'temp_anom_2025-04' has two points "
            "[('2025-04-10T00:00:00Z', 1.1), ('2025-04-25T00:00:00Z', -0.3)] and is readable; "
            "a QC PDF exists for label 'QC_TEMP_ANOM_2025-04' with artifact stored and accessible; "
            "stakeholder output 'Temp Anomaly Apr 2025' (audience 'internal') is created."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-10T00:00:00Z", "value": 1.1},
                {"timestamp": "2025-04-25T00:00:00Z", "value": -0.3}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04", "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Temp Anomaly Apr 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Temp Anomaly Apr 2025"}),
        ],
        outputs=[
            "series.name=temp_anom_2025-04; points=2; p1.ts=2025-04-10T00:00:00Z; p1.value=1.1; p2.ts=2025-04-25T00:00:00Z; p2.value=-0.3 | "
            "qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf | "
            "stakeholder.output_label=Temp Anomaly Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_103",
        instruction=(
            "You publish June-2025 precipitation anomaly series and store QC figure. "
            "End state: processed series 'precip_anom_2025-06' has three points "
            "[('2025-06-01T00:00:00Z', -5.0), ('2025-06-15T00:00:00Z', 3.2), ('2025-06-29T00:00:00Z', -1.1)] "
            "and is retrievable; QC artifact 'QC_PRECIP_ANOM_2025-06' (pdf) exists and is retrievable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "precip_anom_2025-06", "items": [
                {"timestamp": "2025-06-01T00:00:00Z", "value": -5.0},
                {"timestamp": "2025-06-15T00:00:00Z", "value": 3.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": -1.1}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "precip_anom_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06", "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=precip_anom_2025-06; points=3; p1.ts=2025-06-01T00:00:00Z; p1.value=-5.0; "
            "p2.ts=2025-06-15T00:00:00Z; p2.value=3.2; p3.ts=2025-06-29T00:00:00Z; p3.value=-1.1 | "
            "qc.figure_label=QC_PRECIP_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_102",
        instruction=(
            "You record February-2025 river-flow anomalies and QC. "
            "End state: processed series 'flow_anom_2025-02' has three points "
            "[('2025-02-03T00:00:00Z', 120), ('2025-02-14T00:00:00Z', 110), ('2025-02-25T00:00:00Z', 130)] "
            "and is readable; QC figure with label 'QC_FLOW_ANOM_2025-02' exists and is retrievable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "flow_anom_2025-02", "items": [
                {"timestamp": "2025-02-03T00:00:00Z", "value": 120},
                {"timestamp": "2025-02-14T00:00:00Z", "value": 110},
                {"timestamp": "2025-02-25T00:00:00Z", "value": 130}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "flow_anom_2025-02"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02", "figure_path": "https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
        ],
        outputs=[
            "series.name=flow_anom_2025-02; points=3; p1.ts=2025-02-03T00:00:00Z; p1.value=120; "
            "p2.ts=2025-02-14T00:00:00Z; p2.value=110; p3.ts=2025-02-25T00:00:00Z; p3.value=130 | "
            "qc.figure_label=QC_FLOW_ANOM_2025-02; qc.figure_path=https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_101",
        instruction=(
            "You publish an April-2025 sea-surface temperature anomaly series with QC summary. "
            "End state: processed series 'sst_anom_2025-04' has three points "
            "[('2025-04-05T00:00:00Z', 0.5), ('2025-04-15T00:00:00Z', -0.1), ('2025-04-27T00:00:00Z', 0.3)] "
            "and is readable; a QC PDF exists for label 'QC_SST_ANOM_2025-04' with artifact_type 'pdf' and is retrievable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sst_anom_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 0.5},
                {"timestamp": "2025-04-15T00:00:00Z", "value": -0.1},
                {"timestamp": "2025-04-27T00:00:00Z", "value": 0.3}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sst_anom_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-04", "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SST_ANOM_2025-04"}),
        ],
        outputs=[
            "series.name=sst_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=0.5; "
            "p2.ts=2025-04-15T00:00:00Z; p2.value=-0.1; p3.ts=2025-04-27T00:00:00Z; p3.value=0.3 | "
            "qc.figure_label=QC_SST_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SST_ANOM_2025-04.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_82",
        instruction=(
            "You publish a November‑2025 salinity anomaly series with QC. End state: "
            "processed series 'salinity_anom_2025-11' has three points [('2025-11-01T00:00:00Z', 0.10), ('2025-11-11T00:00:00Z', -0.04), ('2025-11-21T00:00:00Z', 0.06)] and is readable; "
            "a QC PDF exists for label 'QC_SAL_ANOM_2025-11' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Salinity Anomaly Nov 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "salinity_anom_2025-11", "items": [
                {"timestamp": "2025-11-01T00:00:00Z", "value": 0.10},
                {"timestamp": "2025-11-11T00:00:00Z", "value": -0.04},
                {"timestamp": "2025-11-21T00:00:00Z", "value": 0.06}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "salinity_anom_2025-11"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-11"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-11", "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-11"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Nov 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Nov 2025"}),
        ],
        outputs=[
            "series.name=salinity_anom_2025-11; points=3; p1.ts=2025-11-01T00:00:00Z; p1.value=0.10; p2.ts=2025-11-11T00:00:00Z; p2.value=-0.04; p3.ts=2025-11-21T00:00:00Z; p3.value=0.06 | "
            "qc.figure_label=QC_SAL_ANOM_2025-11; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf | "
            "stakeholder.output_label=Salinity Anomaly Nov 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-11.pdf"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_81",
        instruction=(
            "You publish an October‑2025 tide anomaly series with QC. End state: "
            "processed series 'tide_anom_2025-10' has three points [('2025-10-03T00:00:00Z', 0.12), ('2025-10-13T00:00:00Z', -0.05), ('2025-10-23T00:00:00Z', 0.08)] and is readable; "
            "a QC PDF exists for label 'QC_TIDE_ANOM_2025-10' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Tide Anomaly Oct 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "tide_anom_2025-10", "items": [
                {"timestamp": "2025-10-03T00:00:00Z", "value": 0.12},
                {"timestamp": "2025-10-13T00:00:00Z", "value": -0.05},
                {"timestamp": "2025-10-23T00:00:00Z", "value": 0.08}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "tide_anom_2025-10"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TIDE_ANOM_2025-10"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TIDE_ANOM_2025-10", "figure_path": "https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TIDE_ANOM_2025-10"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Tide Anomaly Oct 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Tide Anomaly Oct 2025"}),
        ],
        outputs=[
            "series.name=tide_anom_2025-10; points=3; p1.ts=2025-10-03T00:00:00Z; p1.value=0.12; p2.ts=2025-10-13T00:00:00Z; p2.value=-0.05; p3.ts=2025-10-23T00:00:00Z; p3.value=0.08 | "
            "qc.figure_label=QC_TIDE_ANOM_2025-10; qc.figure_path=https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf | "
            "stakeholder.output_label=Tide Anomaly Oct 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TIDE_ANOM_2025-10.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_80",
        instruction=(
            "You publish a September‑2025 water‑level anomaly series with QC. End state: "
            "processed series 'wl_anom_2025-09' has three points [('2025-09-05T00:00:00Z', 0.06), ('2025-09-15T00:00:00Z', -0.04), ('2025-09-25T00:00:00Z', 0.05)] and is readable; "
            "a QC PDF exists for label 'QC_WL_ANOM_2025-09' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'WL Anomaly Sep 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "wl_anom_2025-09", "items": [
                {"timestamp": "2025-09-05T00:00:00Z", "value": 0.06},
                {"timestamp": "2025-09-15T00:00:00Z", "value": -0.04},
                {"timestamp": "2025-09-25T00:00:00Z", "value": 0.05}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "wl_anom_2025-09"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WL_ANOM_2025-09"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WL_ANOM_2025-09", "figure_path": "https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WL_ANOM_2025-09"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "WL Anomaly Sep 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "WL Anomaly Sep 2025"}),
        ],
        outputs=[
            "series.name=wl_anom_2025-09; points=3; p1.ts=2025-09-05T00:00:00Z; p1.value=0.06; p2.ts=2025-09-15T00:00:00Z; p2.value=-0.04; p3.ts=2025-09-25T00:00:00Z; p3.value=0.05 | "
            "qc.figure_label=QC_WL_ANOM_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf | "
            "stakeholder.output_label=WL Anomaly Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WL_ANOM_2025-09.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_75",
        instruction=(
            "You publish an April-2025 salinity anomaly series with QC. End state: "
            "processed series 'sal_anom_2025-04' has three points [('2025-04-05T00:00:00Z', 0.12), ('2025-04-15T00:00:00Z', -0.03), ('2025-04-25T00:00:00Z', 0.07)] and is readable; "
            "a QC PDF exists for label 'QC_SAL_ANOM_2025-04' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "sal_anom_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 0.12},
                {"timestamp": "2025-04-15T00:00:00Z", "value": -0.03},
                {"timestamp": "2025-04-25T00:00:00Z", "value": 0.07}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "sal_anom_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-04", "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-04"}),
        ],
        outputs=[
            "series.name=sal_anom_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=0.12; p2.ts=2025-04-15T00:00:00Z; p2.value=-0.03; p3.ts=2025-04-25T00:00:00Z; p3.value=0.07 | "
            "qc.figure_label=QC_SAL_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-04.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_76",
        instruction=(
            "You publish a May-2025 water-temperature anomaly series with QC. End state: "
            "processed series 'temp_anom_2025-05' has three points [('2025-05-03T00:00:00Z', -0.15), ('2025-05-12T00:00:00Z', 0.02), ('2025-05-27T00:00:00Z', 0.09)] and is readable; "
            "a QC PDF exists for label 'QC_TEMP_ANOM_2025-05' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "temp_anom_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": -0.15},
                {"timestamp": "2025-05-12T00:00:00Z", "value": 0.02},
                {"timestamp": "2025-05-27T00:00:00Z", "value": 0.09}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "temp_anom_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-05", "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_TEMP_ANOM_2025-05"}),
        ],
        outputs=[
            "series.name=temp_anom_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=-0.15; p2.ts=2025-05-12T00:00:00Z; p2.value=0.02; p3.ts=2025-05-27T00:00:00Z; p3.value=0.09 | "
            "qc.figure_label=QC_TEMP_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_77",
        instruction=(
            "You publish a June-2025 current-speed anomaly series with QC. End state: "
            "processed series 'cur_anom_2025-06' has three points [('2025-06-04T00:00:00Z', 0.22), ('2025-06-16T00:00:00Z', -0.05), ('2025-06-24T00:00:00Z', 0.11)] and is readable; "
            "a QC PDF exists for label 'QC_CUR_ANOM_2025-06' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "cur_anom_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 0.22},
                {"timestamp": "2025-06-16T00:00:00Z", "value": -0.05},
                {"timestamp": "2025-06-24T00:00:00Z", "value": 0.11}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "cur_anom_2025-06"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CUR_ANOM_2025-06"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CUR_ANOM_2025-06", "figure_path": "https://storage.example.com/reports/QC_CUR_ANOM_2025-06.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CUR_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=cur_anom_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=0.22; p2.ts=2025-06-16T00:00:00Z; p2.value=-0.05; p3.ts=2025-06-24T00:00:00Z; p3.value=0.11 | "
            "qc.figure_label=QC_CUR_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_CUR_ANOM_2025-06.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_78",
        instruction=(
            "You publish a July-2025 wave-height anomaly series with QC. End state: "
            "processed series 'wave_anom_2025-07' has three points [('2025-07-07T00:00:00Z', 0.35), ('2025-07-18T00:00:00Z', -0.06), ('2025-07-29T00:00:00Z', 0.21)] and is readable; "
            "a QC PDF exists for label 'QC_WAVE_ANOM_2025-07' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "wave_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-07-18T00:00:00Z", "value": -0.06},
                {"timestamp": "2025-07-29T00:00:00Z", "value": 0.21}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "wave_anom_2025-07"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07", "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
        ],
        outputs=[
            "series.name=wave_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=0.35; p2.ts=2025-07-18T00:00:00Z; p2.value=-0.06; p3.ts=2025-07-29T00:00:00Z; p3.value=0.21 | "
            "qc.figure_label=QC_WAVE_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_79",
        instruction=(
            "You publish an August-2025 dissolved-oxygen anomaly series with QC. End state: "
            "processed series 'do_anom_2025-08' has three points [('2025-08-02T00:00:00Z', 0.18), ('2025-08-14T00:00:00Z', -0.07), ('2025-08-27T00:00:00Z', 0.10)] and is readable; "
            "a QC PDF exists for label 'QC_DO_ANOM_2025-08' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "do_anom_2025-08", "items": [
                {"timestamp": "2025-08-02T00:00:00Z", "value": 0.18},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -0.07},
                {"timestamp": "2025-08-27T00:00:00Z", "value": 0.10}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "do_anom_2025-08"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_DO_ANOM_2025-08", "figure_path": "https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
        ],
        outputs=[
            "series.name=do_anom_2025-08; points=3; p1.ts=2025-08-02T00:00:00Z; p1.value=0.18; p2.ts=2025-08-14T00:00:00Z; p2.value=-0.07; p3.ts=2025-08-27T00:00:00Z; p3.value=0.10 | "
            "qc.figure_label=QC_DO_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_71",
        instruction=(
            "You register 'XGBoost_Rainfall_v1' v1.0 with test artifacts. End state: "
            "model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is recorded and readable; "
            "model_config 'default' has max_depth 5, n_estimators 150, learning_rate 0.05 and is readable; "
            "test AUC 0.94 is stored and readable; "
            "artifact '/models/XGBoost_Rainfall_v1_v1.0.json' exists and is readable."
        ),
        actions=[
            Action(name="insert_model", kwargs={"model_name": "XGBoost_Rainfall_v1", "model_type": "xgboost", "framework": "xgboost", "version": "1.0", "status": "staged"}),
            Action(name="get_model_details", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="upsert_model_config", kwargs={"model_name": "XGBoost_Rainfall_v1", "config_name": "default", "params": {"max_depth": 5, "n_estimators": 150, "learning_rate": 0.05}}),
            Action(name="get_model_config", kwargs={"model_name": "XGBoost_Rainfall_v1", "config_name": "default"}),

            Action(name="insert_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1", "metric_name": "AUC", "value": 0.94, "dataset_split": "test"}),
            Action(name="get_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="insert_file", kwargs={"path": "/models/XGBoost_Rainfall_v1_v1.0.json", "mime_type": "application/json"}),
            Action(name="get_file", kwargs={"path": "/models/XGBoost_Rainfall_v1_v1.0.json"}),
        ],
        outputs=[
            "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "config.model=XGBoost_Rainfall_v1; config.name=default; params.max_depth=5; params.n_estimators=150; params.learning_rate=0.05 | "
            "metric.model=XGBoost_Rainfall_v1; metric.name=AUC; metric.value=0.94; split=test | "
            "file.path=/models/XGBoost_Rainfall_v1_v1.0.json; file.mime=application/json"
        ],
    ),


    Task(
        annotator="R",
        user_id="ds_v3_56",
        instruction=(
            "You curate feature set 'coastal_flood_features_v1' (version '1.0') with columns "
            "['water_level_max','wave_height_mean','precipitation_total'] and set it active. End state: "
            "feature set is readable; feature file '/features/coastal_flood_features_v1.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'coastal_flood_features_v1'; QC PDF 'QC_COASTAL_FEATURES_2025-06' exists and is readable."
        ),
        actions=[
            Action(
                name="insert_feature_set",
                kwargs={
                    "feature_set_name": "coastal_flood_features_v1",
                    "version": "1.0",
                    "columns": ["water_level_max","wave_height_mean","precipitation_total"]
                }
            ),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "coastal_flood_features_v1"}),

            Action(
                name="insert_file",
                kwargs={"path": "/features/coastal_flood_features_v1.parquet", "mime_type": "application/parquet"}
            ),
            Action(name="get_file", kwargs={"path": "/features/coastal_flood_features_v1.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "coastal_flood_features_v1"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"}),
            Action(
                name="insert_qc_figure",
                kwargs={
                    "figure_label": "QC_COASTAL_FEATURES_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf",
                    "artifact_type": "pdf"
                }
            ),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"})
        ],
        outputs=[
            "feature_set.name=coastal_flood_features_v1; version=1.0; columns=water_level_max|wave_height_mean|precipitation_total | "
            "file.path=/features/coastal_flood_features_v1.parquet; file.mime=application/parquet | "
            "config.active_feature_set=coastal_flood_features_v1 | "
            "qc.figure_label=QC_COASTAL_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf"
        ]
    ),


    Task(
        annotator="R",
        user_id="ds_v3_50",
        instruction=(
            "You create a feature set 'storm_features_v2' (version '2.0') with columns ['surge_height', 'wind_speed', 'precipitation'] "
            "and record it. End state: feature set is readable; feature file '/features/storm_features_v2.parquet' exists and is readable; "
            "project config 'active_feature_set' is updated to 'storm_features_v2'; QC PDF labeled 'QC_STORM_FEATURES_2025-06' exists and is readable."
        ),
        actions=[
            Action(
                name="insert_feature_set",
                kwargs={
                    "feature_set_name": "storm_features_v2",
                    "version": "2.0",
                    "columns": ["surge_height", "wind_speed", "precipitation"]
                }
            ),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "storm_features_v2"}),

            Action(
                name="insert_file",
                kwargs={"path": "/features/storm_features_v2.parquet", "mime_type": "application/parquet"}
            ),
            Action(name="get_file", kwargs={"path": "/features/storm_features_v2.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "storm_features_v2"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"}),
            Action(
                name="insert_qc_figure",
                kwargs={
                    "figure_label": "QC_STORM_FEATURES_2025-06",
                    "figure_path": "https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf",
                    "artifact_type": "pdf"
                }
            ),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"})
        ],
        outputs=[
            "feature_set.name=storm_features_v2; version=2.0; columns=surge_height|wind_speed|precipitation | "
            "file.path=/features/storm_features_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=storm_features_v2 | "
            "qc.figure_label=QC_STORM_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf"
        ]
    ),


    Task(
        annotator="R",
        user_id="ds_v3_51",
        instruction=(
            "You curate feature set 'harbor_arrival_metrics_v2' version 2.0 and activate it. End state: "
            "feature_set 'harbor_arrival_metrics_v2' with columns ['arrival_count','dwell_time_mean','dwell_time_median'] is recorded; "
            "feature file '/features/harbor_arrival_metrics_v2.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'harbor_arrival_metrics_v2'; "
            "a QC PDF exists for label 'QC_HARBOR_ARRIVAL_2025-03' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "harbor_arrival_metrics_v2", "version": "2.0", "columns": ["arrival_count","dwell_time_mean","dwell_time_median"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "harbor_arrival_metrics_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/harbor_arrival_metrics_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/harbor_arrival_metrics_v2.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "harbor_arrival_metrics_v2"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03", "figure_path": "https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
        ],
        outputs=[
            "feature_set.name=harbor_arrival_metrics_v2; version=2.0; columns=arrival_count|dwell_time_mean|dwell_time_median | "
            "file.path=/features/harbor_arrival_metrics_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=harbor_arrival_metrics_v2 | "
            "qc.figure_label=QC_HARBOR_ARRIVAL_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf"
        ],
    ),
    Task(
        annotator="R",
        user_id="ds_v3_36",
        instruction=(
            "You generate a processed time series for harbor ice thickness 'ice_thickness_2025-05'. End state: "
            "series 'ice_thickness_2025-05' has three points [('2025-05-01T00:00:00Z', 0.25), ('2025-05-08T00:00:00Z', 0.30), ('2025-05-15T00:00:00Z', 0.28)] and is readable; "
            "QC figure 'QC_ICE_THICKNESS_2025-05' exists (artifact_type 'pdf') and is readable; "
            "stakeholder output 'Harbor Ice Thickness May 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf'."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "ice_thickness_2025-05", "items": [
                {"timestamp": "2025-05-01T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-05-08T00:00:00Z", "value": 0.30},
                {"timestamp": "2025-05-15T00:00:00Z", "value": 0.28}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "ice_thickness_2025-05"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05", "figure_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Harbor Ice Thickness May 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Harbor Ice Thickness May 2025"}),
        ],
        outputs=[
            "series.name=ice_thickness_2025-05; points=3; p1.value=0.25; p2.value=0.30; p3.value=0.28 | "
            "qc.figure_label=QC_ICE_THICKNESS_2025-05; qc.figure_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf | "
            "stakeholder.output_label=Harbor Ice Thickness May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_37",
        instruction=(
            "You curate a feature set 'storm_surge_v2' for May 2025 and activate it in project configuration. End state: "
            "feature_set 'storm_surge_v2' (version '2.0') with columns ['max_surge','mean_surge'] is recorded and readable; "
            "feature file '/features/storm_surge_v2.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'storm_surge_v2'; "
            "QC figure 'QC_STORM_SURGE_2025-05' exists (artifact_type 'pdf') and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "storm_surge_v2", "version": "2.0", "columns": ["max_surge","mean_surge"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "storm_surge_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/storm_surge_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/storm_surge_v2.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "storm_surge_v2"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_STORM_SURGE_2025-05", "figure_path": "https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
        ],
        outputs=[
            "feature_set.name=storm_surge_v2; version=2.0; columns=max_surge|mean_surge | "
            "file.path=/features/storm_surge_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=storm_surge_v2 | "
            "qc.figure_label=QC_STORM_SURGE_2025-05; qc.figure_path=https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_3",
        instruction=(
            "You publish a March‑2025 rainfall-runoff anomaly series. End state: "
            "processed series 'rainfall_runoff_anom_2025-03' has three points [('2025-03-05T00:00:00Z', 12.4), ('2025-03-12T00:00:00Z', 9.8), ('2025-03-19T00:00:00Z', 15.2)] and is readable; "
            "a QC PDF exists for label 'QC_RR_ANOM_2025-03' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Rainfall-Runoff Anomaly Mar 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "rainfall_runoff_anom_2025-03", "items": [
                {"timestamp": "2025-03-05T00:00:00Z", "value": 12.4},
                {"timestamp": "2025-03-12T00:00:00Z", "value": 9.8},
                {"timestamp": "2025-03-19T00:00:00Z", "value": 15.2}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "rainfall_runoff_anom_2025-03"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_RR_ANOM_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),

            Action(name="insert_stakeholder_output",
                   kwargs={"output_label": "Rainfall-Runoff Anomaly Mar 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Rainfall-Runoff Anomaly Mar 2025"}),
        ],
        outputs=[
            "series.name=rainfall_runoff_anom_2025-03; points=3; p1.ts=2025-03-05T00:00:00Z; p1.value=12.4; "
            "p2.ts=2025-03-12T00:00:00Z; p2.value=9.8; p3.ts=2025-03-19T00:00:00Z; p3.value=15.2 | "
            "qc.figure_label=QC_RR_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf | "
            "stakeholder.output_label=Rainfall-Runoff Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_5",
        instruction=(
            "You QC a 30-year NOAA tide gauge dataset. End state: "
            "processed series 'noaa_tide_qc_1990_2020' has summary points [('mean_sea_level', 2.34), ('max_tide', 3.78)] and is readable; "
            "a QC PDF exists for label 'QC_NOAA_TIDE_1990_2020' and is stored (artifact_type 'pdf'); "
            "stakeholder output 'NOAA Tide QC 1990-2020' (audience 'internal') references 'https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "noaa_tide_qc_1990_2020", "items": [
                {"timestamp": "mean_sea_level", "value": 2.34},
                {"timestamp": "max_tide", "value": 3.78}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "noaa_tide_qc_1990_2020"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020", "figure_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "NOAA Tide QC 1990-2020", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "NOAA Tide QC 1990-2020"}),
        ],
        outputs=[
            "series.name=noaa_tide_qc_1990_2020; points=2; p1.ts=mean_sea_level; p1.value=2.34; p2.ts=max_tide; p2.value=3.78 | "
            "qc.figure_label=QC_NOAA_TIDE_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf | "
            "stakeholder.output_label=NOAA Tide QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_30",
        instruction=(
            "You publish a March‑2025 salinity anomaly series. End state: "
            "processed series 'salinity_anom_2025-03' has three points [('2025-03-07T00:00:00Z', 0.07), ('2025-03-14T00:00:00Z', -0.02), ('2025-03-21T00:00:00Z', 0.04)] and is readable; "
            "a QC PDF exists for label 'QC_SAL_ANOM_2025-03' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Salinity Anomaly Mar 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "salinity_anom_2025-03", "items": [
                {"timestamp": "2025-03-07T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-03-14T00:00:00Z", "value": -0.02},
                {"timestamp": "2025-03-21T00:00:00Z", "value": 0.04}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "salinity_anom_2025-03"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-03", "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Mar 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Salinity Anomaly Mar 2025"}),
        ],
        outputs=[
            "series.name=salinity_anom_2025-03; points=3; p1.ts=2025-03-07T00:00:00Z; p1.value=0.07; p2.ts=2025-03-14T00:00:00Z; p2.value=-0.02; p3.ts=2025-03-21T00:00:00Z; p3.value=0.04 | "
            "qc.figure_label=QC_SAL_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf | "
            "stakeholder.output_label=Salinity Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_31",
        instruction=(
            "You curate the feature set 'harbor_ops_v2' and set it active with QC. End state: "
            "feature_set 'harbor_ops_v2' (version '2.0') with columns ['arrival_count','dwell_time_median','departure_count'] is recorded and readable; "
            "feature file '/features/harbor_ops_v2.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'harbor_ops_v2' and is readable; "
            "a QC PDF exists for label 'QC_HARBOR_OPS_2025-03' with figure record stored (artifact_type 'pdf') and readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "harbor_ops_v2", "version": "2.0", "columns": ["arrival_count","dwell_time_median","departure_count"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "harbor_ops_v2"}),

            Action(name="insert_file", kwargs={"path": "/features/harbor_ops_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/harbor_ops_v2.parquet"}),

            Action(name="update_project_config", kwargs={"updates": {"active_feature_set": "harbor_ops_v2"}}),
            Action(name="get_project_config", kwargs={"key": "active_feature_set"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03", "figure_path": "https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
        ],
        outputs=[
            "feature_set.name=harbor_ops_v2; version=2.0; columns=arrival_count|dwell_time_median|departure_count | "
            "file.path=/features/harbor_ops_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=harbor_ops_v2 | "
            "qc.figure_label=QC_HARBOR_OPS_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_32",
        instruction=(
            "You publish a April‑2025 wave height series for Puget Sound. End state: "
            "processed series 'wave_height_2025-04' has three points [('2025-04-05T00:00:00Z', 1.2), ('2025-04-12T00:00:00Z', 0.8), ('2025-04-19T00:00:00Z', 1.5)] and is readable; "
            "a QC PDF exists for label 'QC_WAVE_HEIGHT_2025-04' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Wave Height Apr 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_processed_timeseries", kwargs={"series_name": "wave_height_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-12T00:00:00Z", "value": 0.8},
                {"timestamp": "2025-04-19T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="get_processed_timeseries", kwargs={"series_name": "wave_height_2025-04"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04", "figure_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Wave Height Apr 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Wave Height Apr 2025"}),
        ],
        outputs=[
            "series.name=wave_height_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=1.2; p2.ts=2025-04-12T00:00:00Z; p2.value=0.8; p3.ts=2025-04-19T00:00:00Z; p3.value=1.5 | "
            "qc.figure_label=QC_WAVE_HEIGHT_2025-04; qc.figure_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf | "
            "stakeholder.output_label=Wave Height Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"
        ],
    ),

    Task(
        annotator="R",
        user_id="ds_v3_34",
        instruction=(
            "You create a logistic regression climate risk assessment dataset 'climate_risk_v1' for 2025‑04. End state: "
            "dataset 'climate_risk_v1' (version '1.0') with columns ['temperature','rainfall','flood_risk'] is recorded and readable; "
            "feature file '/features/climate_risk_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_CLIMATE_RISK_2025-04' with figure record stored (artifact_type 'pdf') and readable; "
            "stakeholder output 'Climate Risk Apr 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf' and is readable."
        ),
        actions=[
            Action(name="insert_feature_set", kwargs={"feature_set_name": "climate_risk_v1", "version": "1.0", "columns": ["temperature","rainfall","flood_risk"]}),
            Action(name="get_feature_set_details", kwargs={"feature_set_name": "climate_risk_v1"}),

            Action(name="insert_file", kwargs={"path": "/features/climate_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="get_file", kwargs={"path": "/features/climate_risk_v1.parquet"}),

            Action(name="export_qc_figure", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),
            Action(name="insert_qc_figure", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04", "figure_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf", "artifact_type": "pdf"}),
            Action(name="get_qc_figure", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),

            Action(name="insert_stakeholder_output", kwargs={"output_label": "Climate Risk Apr 2025", "audience": "internal", "artifact_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"}),
            Action(name="get_stakeholder_output", kwargs={"output_label": "Climate Risk Apr 2025"}),
        ],
        outputs=[
            "feature_set.name=climate_risk_v1; version=1.0; columns=temperature|rainfall|flood_risk | "
            "file.path=/features/climate_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_CLIMATE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf | "
            "stakeholder.output_label=Climate Risk Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"
        ],
    )
]
