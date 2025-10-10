from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="v5",
        user_id="ds_ops_001",
        instruction=(
            "You Deliver April-2025 temperature anomaly record with QC validation. "
            "End state: series 'temp_anom_2025-04' has three values; "
            "[('2025-04-05T00:00:00Z', 1.2), ('2025-04-15T00:00:00Z', -0.3), ('2025-04-27T00:00:00Z', 0.6)] "
            "QC report 'QC_TEMP_ANOM_2025-04' (pdf) is created."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-15T00:00:00Z", "value": -0.3},
                {"timestamp": "2025-04-27T00:00:00Z", "value": 0.6}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),

            Action(name="append_audit_event", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "temp_anom_2025-04",
                                                                  "qc_label": "QC_TEMP_ANOM_2025-04"}}),
            Action(name="read_audit_events", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[
            "series.name=temp_anom_2025-04; points=3; p1.value=1.2; p2.value=-0.3; p3.value=0.6 | "
            "qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_002",
        instruction=(
            "You Produce June-2025 salinity anomaly with QC. "
            "End state: series 'sal_anom_2025-06' has two entries; "
            "[('2025-06-12T00:00:00Z', 0.5), ('2025-06-22T00:00:00Z', -0.1)] and is available; "
            "QC record 'QC_SAL_ANOM_2025-06' (pdf) is stored and retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "sal_anom_2025-06", "items": [
                {"timestamp": "2025-06-12T00:00:00Z", "value": 0.5},
                {"timestamp": "2025-06-22T00:00:00Z", "value": -0.1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "sal_anom_2025-06"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),

            Action(name="append_audit_event", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "sal_anom_2025-06",
                                                                  "qc_label": "QC_SAL_ANOM_2025-06"}}),
            Action(name="read_audit_events", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[
            "series.name=sal_anom_2025-06; points=2; p1.value=0.5; p2.value=-0.1 | "
            "qc.figure_label=QC_SAL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_003",
        instruction=(
            "You Assemble May-2025 rainfall anomaly dataset with QC. "
            "End state: series 'rain_anom_2025-05' holds three values; "
            "[('2025-05-05T00:00:00Z', 12.0), ('2025-05-15T00:00:00Z', -3.2), ('2025-05-25T00:00:00Z', 4.7)] and is retrievable; "
            "QC artifact 'QC_RAIN_ANOM_2025-05' (pdf) is available."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "rain_anom_2025-05", "items": [
                {"timestamp": "2025-05-05T00:00:00Z", "value": 12.0},
                {"timestamp": "2025-05-15T00:00:00Z", "value": -3.2},
                {"timestamp": "2025-05-25T00:00:00Z", "value": 4.7}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "rain_anom_2025-05"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),

            Action(name="append_audit_event", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "rain_anom_2025-05",
                                                                  "qc_label": "QC_RAIN_ANOM_2025-05"}}),
            Action(name="read_audit_events", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[
            "series.name=rain_anom_2025-05; points=3; p1.value=12.0; p2.value=-3.2; p3.value=4.7 | "
            "qc.figure_label=QC_RAIN_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_004",
        instruction=(
            "You onboard the LSTM flood model (v2.0) with its config and a validation score. "
            "End state: model 'LSTM_Flood_v2' (type=rnn, framework=tensorflow, version=2.0, status=staged) is stored and readable; "
            "profile 'seq_default' records hidden_units=128, dropout=0.3, layers=3; "
            "validation Accuracy=0.902 is logged."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "LSTM_Flood_v2", "model_type": "rnn", "framework": "tensorflow",
                           "version": "2.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="upsert_model_profile",
                   kwargs={"model_name": "LSTM_Flood_v2", "config_name": "seq_default",
                           "params": {"hidden_units": 128, "dropout": 0.3, "layers": 3}}),
            Action(name="read_model_profiles", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "LSTM_Flood_v2", "metric_name": "Accuracy",
                           "value": 0.902, "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "LSTM_Flood_v2"}),
        ],
        outputs=[

            "model.name=LSTM_Flood_v2; type=rnn; framework=tensorflow; version=2.0; status=staged | "
            "config.model=LSTM_Flood_v2; config.name=seq_default; params.hidden_units=128; params.dropout=0.3; params.layers=3 | "
            "metric.model=LSTM_Flood_v2; metric.name=Accuracy; metric.value=0.902; split=validation"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_005",
        instruction=(
            "You register the Transformer climate model (v3.1) with its configuration and a validation loss. "
            "End state: model 'Transformer_Climate_v3' (type=transformer, framework=pytorch, version=3.1, status=staged) is stored and readable; "
            "profile 'attention_default' records heads=8, d_model=256, layers=6; "
            "validation Loss=0.145 is logged."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "Transformer_Climate_v3", "model_type": "transformer", "framework": "pytorch",
                           "version": "3.1", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="upsert_model_profile",
                   kwargs={"model_name": "Transformer_Climate_v3", "config_name": "attention_default",
                           "params": {"heads": 8, "d_model": 256, "layers": 6}}),
            Action(name="read_model_profiles", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "Transformer_Climate_v3", "metric_name": "Loss",
                           "value": 0.145, "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "Transformer_Climate_v3"}),
        ],
        outputs=[
            "model.name=Transformer_Climate_v3; type=transformer; framework=pytorch; version=3.1; status=staged | "
            "config.model=Transformer_Climate_v3; config.name=attention_default; params.heads=8; params.d_model=256; params.layers=6 | "
            "metric.model=Transformer_Climate_v3; metric.name=Loss; metric.value=0.145; split=validation"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_006",
        instruction=(
            "You configure a January-2026 backfill cutoff, run a lightweight readiness probe series, and archive QC for ops. End state: "
            "project settings show backfill_cutoff '2026-01-10T08:00:00Z'; "
            "probe series 'backfill_probe_2026-01' has 1 timestamps and is readable; "
            "audit event 'BACKFILL_READY' with message 'Early January backfill cutoff configured successfully.' exists; "
            "QC report 'QC_CONFIG_BACKFILL_2026-01' (pdf) is stored and referenced by an internal ops artifact."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"backfill_cutoff": "2026-01-10T08:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "backfill_cutoff"}),
            Action(name="write_processed_series", kwargs={"series_name": "backfill_probe_2026-01", "items": [
                {"timestamp": "2026-01-10T08:00:00Z", "value": 1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "backfill_probe_2026-01"}),
            Action(name="append_audit_event", kwargs={
                "event_type": "BACKFILL_READY",
                "message": "Early January backfill cutoff configured successfully."
            }),
            Action(name="read_audit_events", kwargs={"event_type": "BACKFILL_READY"}),
            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_CONFIG_BACKFILL_2026-01",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
            Action(name="record_stakeholder_artifact", kwargs={
                "output_label": "Backfill Cutoff Jan 2026",
                "audience": "internal_ops",
                "artifact_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf"
            }),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Backfill Cutoff Jan 2026"}),
        ],
        outputs=[
            "config.backfill_cutoff=2026-01-10T08:00:00Z | "
            "series.name=backfill_probe_2026-01; points=2; p1.ts=2026-01-10T08:00:00Z; p1.value=1 | "
            "audit.event_type=BACKFILL_READY; audit.message=Early January backfill cutoff configured successfully. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2026-01; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf | "
            "stakeholder.output_label=Backfill Cutoff Jan 2026; audience=internal_ops"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_007",
        instruction=(
            "You register 'GradientBoosting_Wind_v3' and log an October-2025 validation batch with QC. End state: "
            "model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is stored; "
            "validation lot 'VAL_WD_2025-10' includes 1 entries; "
            "validation MAE 0.95 is logged; "
            "QC report 'QC_WD_VAL_2025-10' (png) is recorded and readable."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "model_type": "gradient_boosting",
                           "framework": "sklearn", "version": "3.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_WD_2025-10", "model_name": "GradientBoosting_Wind_v3", "items": [
                       {"timestamp": "2025-10-10T12:00:00Z", "prediction": 15.3}
                   ]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_WD_2025-10"}),
            Action(name="log_model_metric",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "metric_name": "MAE", "value": 0.95,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-10"}),
        ],
        outputs=[
            "model.name=GradientBoosting_Wind_v3; type=gradient_boosting; framework=sklearn; version=3.0; status=staged | "
            "lot.batch_name=VAL_WD_2025-10; rows=1; first_ts=2025-10-10T12:00:00Z; first_pred=15.3 | "
            "metric.model=GradientBoosting_Wind_v3; metric.name=MAE; metric.value=0.95; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-10.png"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_008",
        instruction=(
            "You register 'GradientBoosting_Wind_v3' and log an October-2025 validation batch with QC. End state: "
            "model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is stored; "
            "validation lot 'VAL_WD_2025-10' includes 2 entries; "
            "validation MAE 0.95 is logged; "
            "QC report 'QC_WD_VAL_2025-10' (png) is recorded and readable."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "model_type": "gradient_boosting",
                           "framework": "sklearn", "version": "3.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_WD_2025-10", "model_name": "GradientBoosting_Wind_v3", "items": [
                       {"timestamp": "2025-10-10T12:00:00Z", "prediction": 15.3}
                   ]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_WD_2025-10"}),
            Action(name="log_model_metric",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "metric_name": "MAE", "value": 0.95,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-10"}),
        ],
        outputs=[
            "model.name=GradientBoosting_Wind_v3; type=gradient_boosting; framework=sklearn; version=3.0; status=staged | "
            "lot.batch_name=VAL_WD_2025-10; rows=1; first_ts=2025-10-10T12:00:00Z; first_pred=15.3 | "
            "metric.model=GradientBoosting_Wind_v3; metric.name=MAE; metric.value=0.95; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-10.png"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_009",
        instruction=(
            "You onboard 'XGBoost_Rainfall_v1' and log a July-2025 validation set. End state: "
            "model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is registered and readable; "
            "validation lot 'VAL_RAIN_2025-07' has one entry ('2025-07-15T00:00:00Z', 124.3) and is retrievable; "
            "R²=0.93 is recorded for the validation split and viewable; "
            "QC report 'QC_RAIN_VAL_2025-07' (pdf) is stored and retrievable."
        ),
        actions=[
            # Model artifact (write → verify)
            Action(name="store_model_artifact",
                   kwargs={"model_name": "XGBoost_Rainfall_v1", "model_type": "xgboost",
                           "framework": "xgboost", "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            # Predictions (write → verify)
            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_RAIN_2025-07", "model_name": "XGBoost_Rainfall_v1", "items": [
                       {"timestamp": "2025-07-15T00:00:00Z", "prediction": 124.3}
                   ]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_RAIN_2025-07"}),

            # Metric (write → verify)
            Action(name="log_model_metric",
                   kwargs={"model_name": "XGBoost_Rainfall_v1", "metric_name": "R2", "value": 0.93,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            # QC report (write → verify)
            Action(name="record_qc_report",
                   kwargs={"figure_label": "QC_RAIN_VAL_2025-07",
                           "figure_path": "https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf",
                           "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RAIN_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "pred.batch_name=VAL_RAIN_2025-07; rows=1; first_ts=2025-07-15T00:00:00Z; first_pred=124.3 | "
            "metric.model=XGBoost_Rainfall_v1; metric.name=R2; metric.value=0.93; split=validation | "
            "qc.figure_label=QC_RAIN_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_010",
        instruction=(
            "You register 'storm_features_v2' (v2.0), set it as active, and capture QC plus an activation audit. End state: "
            "feature bundle is retrievable; file '/features/storm_features_v2.parquet' exists and can be fetched; "
            "project setting 'active_feature_set' equals 'storm_features_v2'; "
            "QC PDF 'QC_STORM_FEATURES_2025-06' is recorded and readable; "
            "audit event 'FEATURE_SET_ACTIVATED' with message 'storm_features_v2 set active.' is present."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={
                "feature_set_name": "storm_features_v2",
                "version": "2.0",
                "columns": ["surge_height", "wind_speed", "precipitation"]
            }),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "storm_features_v2"}),

            Action(name="register_file_entry", kwargs={
                "path": "/features/storm_features_v2.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/storm_features_v2.parquet"}),

            Action(name="patch_project_settings", kwargs={"updates": {"active_feature_set": "storm_features_v2"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_STORM_FEATURES_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"}),
            Action(name="append_audit_event", kwargs={
                "event_type": "FEATURE_SET_ACTIVATED",
                "message": "storm_features_v2 set active."
            }),
            Action(name="read_audit_events", kwargs={"event_type": "FEATURE_SET_ACTIVATED"}),
        ],
        outputs=[
            "feature_set.name=storm_features_v2; version=2.0; columns=surge_height|wind_speed|precipitation | "
            "file.path=/features/storm_features_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=storm_features_v2 | "
            "qc.figure_label=QC_STORM_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf | "
            "audit.event_type=FEATURE_SET_ACTIVATED; audit.message=storm_features_v2 set active."
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_011",
        instruction=(
            "You finalize 'harbor_arrival_metrics_v2' (v2.0) and set it live in configuration. End state: "
            "feature_set 'harbor_arrival_metrics_v2' with fields ['arrival_count','dwell_time_mean','dwell_time_median'] is recorded and retrievable; "
            "file '/features/harbor_arrival_metrics_v2.parquet' exists and is retrievable; "
            "project setting 'active_feature_set' equals 'harbor_arrival_metrics_v2'; "
            "QC PDF with label 'QC_HARBOR_ARRIVAL_2025-03' exists and is retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={
                "feature_set_name": "harbor_arrival_metrics_v2",
                "version": "2.0",
                "columns": ["arrival_count", "dwell_time_mean", "dwell_time_median"]
            }),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "harbor_arrival_metrics_v2"}),

            Action(name="register_file_entry", kwargs={
                "path": "/features/harbor_arrival_metrics_v2.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/harbor_arrival_metrics_v2.parquet"}),

            Action(name="patch_project_settings",
                   kwargs={"updates": {"active_feature_set": "harbor_arrival_metrics_v2"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_HARBOR_ARRIVAL_2025-03",
                "figure_path": "https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
        ],
        outputs=[
            "feature_set.name=harbor_arrival_metrics_v2; version=2.0; columns=arrival_count|dwell_time_mean|dwell_time_median | "
            "file.path=/features/harbor_arrival_metrics_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=harbor_arrival_metrics_v2 | "
            "qc.figure_label=QC_HARBOR_ARRIVAL_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_012",
        instruction=(
            "You generate a harbor ice-thickness series for May-2025 with QC and a deliverable. End state: "
            "series 'ice_thickness_2025-05' has three points "
            "[('2025-05-01T00:00:00Z', 0.25), ('2025-05-08T00:00:00Z', 0.30), ('2025-05-15T00:00:00Z', 0.28)] and is retrievable; "
            "QC figure 'QC_ICE_THICKNESS_2025-05' exists (artifact_type 'pdf') and is retrievable; "
            "stakeholder output 'Harbor Ice Thickness May 2025' (audience 'internal') references "
            "'https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf' and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "ice_thickness_2025-05", "items": [
                {"timestamp": "2025-05-01T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-05-08T00:00:00Z", "value": 0.30},
                {"timestamp": "2025-05-15T00:00:00Z", "value": 0.28}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "ice_thickness_2025-05"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_ICE_THICKNESS_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),

            Action(name="record_stakeholder_artifact", kwargs={
                "output_label": "Harbor Ice Thickness May 2025",
                "audience": "internal",
                "artifact_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
            }),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Harbor Ice Thickness May 2025"}),
        ],
        outputs=[
            "series.name=ice_thickness_2025-05; points=3; p1.value=0.25; p2.value=0.30; p3.value=0.28 | "
            "qc.figure_label=QC_ICE_THICKNESS_2025-05; qc.figure_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf | "
            "stakeholder.output_label=Harbor Ice Thickness May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_013",
        instruction=(
            "You finalize a May-2025 storm-surge feature bundle and switch it on in config. End state: "
            "feature_set 'storm_surge_v2' (version '2.0') with fields ['max_surge','mean_surge'] is stored and retrievable; "
            "file '/features/storm_surge_v2.parquet' exists and is retrievable; "
            "project setting 'active_feature_set' equals 'storm_surge_v2'; "
            "QC figure 'QC_STORM_SURGE_2025-05' exists (artifact_type 'pdf') and is retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "storm_surge_v2", "version": "2.0",
                                                           "columns": ["max_surge", "mean_surge"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "storm_surge_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/storm_surge_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/storm_surge_v2.parquet"}),

            Action(name="patch_project_settings", kwargs={"updates": {"active_feature_set": "storm_surge_v2"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_STORM_SURGE_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
        ],
        outputs=[
            "feature_set.name=storm_surge_v2; version=2.0; columns=max_surge|mean_surge | "
            "file.path=/features/storm_surge_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=storm_surge_v2 | "
            "qc.figure_label=QC_STORM_SURGE_2025-05; qc.figure_path=https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_014",
        instruction=(
            "You release a March-2025 rainfall-runoff anomaly series with a QC record and deliverable. End state: "
            "processed series 'rainfall_runoff_anom_2025-03' holds three points "
            "[('2025-03-05T00:00:00Z', 12.4), ('2025-03-12T00:00:00Z', 9.8), ('2025-03-19T00:00:00Z', 15.2)] and is retrievable; "
            "a QC PDF exists for label 'QC_RR_ANOM_2025-03' and is retrievable; "
            "stakeholder output 'Rainfall-Runoff Anomaly Mar 2025' (audience 'internal') references "
            "'https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf' and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "rainfall_runoff_anom_2025-03", "items": [
                {"timestamp": "2025-03-05T00:00:00Z", "value": 12.4},
                {"timestamp": "2025-03-12T00:00:00Z", "value": 9.8},
                {"timestamp": "2025-03-19T00:00:00Z", "value": 15.2}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "rainfall_runoff_anom_2025-03"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_RR_ANOM_2025-03",
                "figure_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),

            Action(name="record_stakeholder_artifact", kwargs={
                "output_label": "Rainfall-Runoff Anomaly Mar 2025",
                "audience": "internal",
                "artifact_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
            }),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Rainfall-Runoff Anomaly Mar 2025"}),
        ],
        outputs=[
            "series.name=rainfall_runoff_anom_2025-03; points=3; p1.ts=2025-03-05T00:00:00Z; p1.value=12.4; "
            "p2.ts=2025-03-12T00:00:00Z; p2.value=9.8; p3.ts=2025-03-19T00:00:00Z; p3.value=15.2 | "
            "qc.figure_label=QC_RR_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf | "
            "stakeholder.output_label=Rainfall-Runoff Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_015",
        instruction=(
            "You Stage 'CNN_FloodExtent_v1' with a July-2025 validation entry. "
            "End state: model 'CNN_FloodExtent_v1' (type=cnn, framework=tensorflow, version=1.0, status=staged) is persisted and retrievable; "
            "validation batch 'VAL_FE_2025-07' contains one row ('2025-07-12T15:00:00Z', 0.88); "
            "validation MAE=0.09 is logged; QC artifact 'QC_FE_VAL_2025-07' (png) is stored and accessible."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "CNN_FloodExtent_v1", "model_type": "cnn", "framework": "tensorflow",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_FE_2025-07", "model_name": "CNN_FloodExtent_v1",
                           "items": [{"timestamp": "2025-07-12T15:00:00Z", "prediction": 0.88}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_FE_2025-07"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "CNN_FloodExtent_v1", "metric_name": "MAE", "value": 0.09,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_FE_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_FE_VAL_2025-07.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FE_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=CNN_FloodExtent_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | "
            "pred.batch_name=VAL_FE_2025-07; rows=1; first_ts=2025-07-12T15:00:00Z; first_pred=0.88 | "
            "metric.model=CNN_FloodExtent_v1; metric.name=MAE; metric.value=0.09; split=validation | "
            "qc.figure_label=QC_FE_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FE_VAL_2025-07.png"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_016",
        instruction=(
            "You Stage 'GRU_Rainfall_v1' with June-2025 validation details. "
            "End state: model 'GRU_Rainfall_v1' (type=gru, framework=pytorch, version=1.0, status=staged) is available; "
            "batch 'VAL_RF_2025-06' includes one entry ('2025-06-15T09:00:00Z', 15.3); "
            "validation RMSE=1.2 is logged; QC artifact 'QC_RF_VAL_2025-06' (pdf) is recorded and retrievable."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "GRU_Rainfall_v1", "model_type": "gru", "framework": "pytorch",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="write_prediction_lot", kwargs={"batch_name": "VAL_RF_2025-06", "model_name": "GRU_Rainfall_v1",
                                                        "items": [{"timestamp": "2025-06-15T09:00:00Z",
                                                                   "prediction": 15.3}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_RF_2025-06"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "GRU_Rainfall_v1", "metric_name": "RMSE", "value": 1.2,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_RF_VAL_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RF_VAL_2025-06"}),
        ],
        outputs=[
            "model.name=GRU_Rainfall_v1; type=gru; framework=pytorch; version=1.0; status=staged | "
            "pred.batch_name=VAL_RF_2025-06; rows=1; first_ts=2025-06-15T09:00:00Z; first_pred=15.3 | "
            "metric.model=GRU_Rainfall_v1; metric.name=RMSE; metric.value=1.2; split=validation | "
            "qc.figure_label=QC_RF_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_017",
        instruction=(
            "You have to register 'RF_Temperature_v3' and capture a May-2025 validation run. "
            "Final state: model 'RF_Temperature_v3' (type 'random_forest', framework 'sklearn', version '3.1', status 'staged') is stored; "
            "validation lot 'VAL_TEMP_2025-05' includes one record ('2025-05-05T00:00:00Z', 18.7) and can be read; "
            "R² value 0.91 is logged under validation split; "
            "QC report 'QC_TEMP_VAL_2025-05' is saved as pdf and retrievable."
        ),
        actions=[
            Action(name="store_model_artifact", kwargs={
                "model_name": "RF_Temperature_v3",
                "model_type": "random_forest",
                "framework": "sklearn",
                "version": "3.1",
                "status": "staged"
            }),
            Action(name="fetch_model_record", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="write_prediction_lot", kwargs={
                "batch_name": "VAL_TEMP_2025-05",
                "model_name": "RF_Temperature_v3",
                "items": [{"timestamp": "2025-05-05T00:00:00Z", "prediction": 18.7}]
            }),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_TEMP_2025-05"}),

            Action(name="log_model_metric", kwargs={
                "model_name": "RF_Temperature_v3",
                "metric_name": "R2",
                "value": 0.91,
                "dataset_split": "validation"
            }),
            Action(name="read_model_metrics", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_TEMP_VAL_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TEMP_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=RF_Temperature_v3; type=random_forest; framework=sklearn; version=3.1; status=staged | "
            "pred.batch_name=VAL_TEMP_2025-05; rows=1; first_ts=2025-05-05T00:00:00Z; first_pred=18.7 | "
            "metric.model=RF_Temperature_v3; metric.name=R2; metric.value=0.91; split=validation | "
            "qc.figure_label=QC_TEMP_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_018",
        instruction=(
            "You Configure 'Prophet_TideCycle_v1' with May-2025 validation details. "
            "End state: model 'Prophet_TideCycle_v1' (type=prophet, framework=prophet, version=1.0, status=staged) is inserted; "
            "batch 'VAL_TC_2025-05' has one row ('2025-05-20T06:00:00Z', 2.44); "
            "MAPE=4.5 is logged; QC file 'QC_TC_VAL_2025-05' (pdf) exists."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "Prophet_TideCycle_v1", "model_type": "prophet", "framework": "prophet",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_TC_2025-05", "model_name": "Prophet_TideCycle_v1",
                           "items": [{"timestamp": "2025-05-20T06:00:00Z", "prediction": 2.44}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_TC_2025-05"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "Prophet_TideCycle_v1", "metric_name": "MAPE", "value": 4.5,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_TC_VAL_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TC_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=Prophet_TideCycle_v1; type=prophet; framework=prophet; version=1.0; status=staged | "
            "pred.batch_name=VAL_TC_2025-05; rows=1; first_ts=2025-05-20T06:00:00Z; first_pred=2.44 | "
            "metric.model=Prophet_TideCycle_v1; metric.name=MAPE; metric.value=4.5; split=validation | "
            "qc.figure_label=QC_TC_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_019",
        instruction=(
            "You Deploy 'XGB_WindDamage_v1' with February-2025 validation results. "
            "End state: model 'XGB_WindDamage_v1' (type=xgboost, framework=xgboost, version=1.6, status=staged) is registered; "
            "batch 'VAL_WD_2025-02' includes one row ('2025-02-14T18:00:00Z', 12.8); "
            "validation MAE=1.7 is stored; QC document 'QC_WD_VAL_2025-02' (pdf) exists and is retrievable."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "XGB_WindDamage_v1", "model_type": "xgboost", "framework": "xgboost",
                           "version": "1.6", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_WD_2025-02", "model_name": "XGB_WindDamage_v1",
                           "items": [{"timestamp": "2025-02-14T18:00:00Z", "prediction": 12.8}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_WD_2025-02"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "XGB_WindDamage_v1", "metric_name": "MAE", "value": 1.7,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-02"}),
        ],
        outputs=[
            "model.name=XGB_WindDamage_v1; type=xgboost; framework=xgboost; version=1.6; status=staged | "
            "pred.batch_name=VAL_WD_2025-02; rows=1; first_ts=2025-02-14T18:00:00Z; first_pred=12.8 | "
            "metric.model=XGB_WindDamage_v1; metric.name=MAE; metric.value=1.7; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-02; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_020",
        instruction=(
            "You Register 'LSTM_FloodRisk_v2' with April-2025 validation entry. "
            "End state: model 'LSTM_FloodRisk_v2' (type=lstm, framework=tensorflow, version=2.0, status=staged) is accessible; "
            "validation batch 'VAL_FR_2025-04' contains one row ('2025-04-05T12:00:00Z', 0.76); "
            "validation RMSE=0.32 is logged; QC artifact 'QC_FR_VAL_2025-04' (png) is stored."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "LSTM_FloodRisk_v2", "model_type": "lstm", "framework": "tensorflow",
                           "version": "2.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_FR_2025-04", "model_name": "LSTM_FloodRisk_v2",
                           "items": [{"timestamp": "2025-04-05T12:00:00Z", "prediction": 0.76}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_FR_2025-04"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "LSTM_FloodRisk_v2", "metric_name": "RMSE", "value": 0.32,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_FR_VAL_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-04.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FR_VAL_2025-04"}),
        ],
        outputs=[
            "model.name=LSTM_FloodRisk_v2; type=lstm; framework=tensorflow; version=2.0; status=staged | "
            "pred.batch_name=VAL_FR_2025-04; rows=1; first_ts=2025-04-05T12:00:00Z; first_pred=0.76 | "
            "metric.model=LSTM_FloodRisk_v2; metric.name=RMSE; metric.value=0.32; split=validation | "
            "qc.figure_label=QC_FR_VAL_2025-04; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-04.png"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_021",
        instruction=(
            "You Process December-2024 salinity anomalies with QC and internal report. "
            "End state: series 'sal_anom_2024-12' has four values; QC file 'QC_SAL_ANOM_2024-12' (pdf) exists; "
            "stakeholder output 'Salinity Anomaly Dec 2024' (audience=internal) references the QC artifact."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "sal_anom_2024-12", "items": [
                {"timestamp": "2024-12-03T00:00:00Z", "value": 0.12},
                {"timestamp": "2024-12-10T00:00:00Z", "value": -0.04},
                {"timestamp": "2024-12-18T00:00:00Z", "value": 0.05},
                {"timestamp": "2024-12-27T00:00:00Z", "value": 0.09}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "sal_anom_2024-12"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2024-12",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Salinity Anomaly Dec 2024", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Salinity Anomaly Dec 2024"}),
        ],
        outputs=[
            "series.name=sal_anom_2024-12; points=4; p1.ts=2024-12-03T00:00:00Z; p1.value=0.12; p2.ts=2024-12-10T00:00:00Z; p2.value=-0.04; p3.ts=2024-12-18T00:00:00Z; p3.value=0.05; p4.ts=2024-12-27T00:00:00Z; p4.value=0.09 | "
            "qc.figure_label=QC_SAL_ANOM_2024-12; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf | "
            "stakeholder.output_label=Salinity Anomaly Dec 2024; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_022",
        instruction=(
            "You produce the tidal harmonics dataset for January 2025, confirm QC output, and release a public-facing summary. "
            "End state: processed series 'tidal_harm_2025-01' contains three entries, QC report 'QC_TIDAL_HARM_2025-01.pdf' is archived, "
            "and a stakeholder artifact titled 'Tidal Harmonics Jan 2025' for audience 'external' links to the QC document."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "tidal_harm_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 1.21},
                {"timestamp": "2025-01-15T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-01-25T00:00:00Z", "value": 1.18}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "tidal_harm_2025-01"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_TIDAL_HARM_2025-01",
                "figure_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),

            Action(name="record_stakeholder_artifact", kwargs={
                "output_label": "Tidal Harmonics Jan 2025",
                "audience": "external",
                "artifact_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
            }),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Tidal Harmonics Jan 2025"}),
        ],
        outputs=[
            "series.name=tidal_harm_2025-01; points=3; "
            "p1.ts=2025-01-05T00:00:00Z; p1.value=1.21; "
            "p2.ts=2025-01-15T00:00:00Z; p2.value=1.15; "
            "p3.ts=2025-01-25T00:00:00Z; p3.value=1.18 | "
            "qc.figure_label=QC_TIDAL_HARM_2025-01; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf | "
            "stakeholder.output_label=Tidal Harmonics Jan 2025; audience=external; artifact_path=https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_023",
        instruction=(
            "You have to Compute February-2025 surge residuals series, archive it, and distribute the QC output."
            "End state: series 'surge_resid_2025-02' has four values; QC artifact 'QC_SURGE_RESID_2025-02' (pdf) exists; "
            "stakeholder output 'Feb 2025 Surge Residual' references the PDF."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "surge_resid_2025-02", "items": [
                {"timestamp": "2025-02-02T00:00:00Z", "value": -0.11},
                {"timestamp": "2025-02-10T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-02-18T00:00:00Z", "value": 0.02},
                {"timestamp": "2025-02-26T00:00:00Z", "value": -0.05}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "surge_resid_2025-02"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SURGE_RESID_2025-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Feb 2025 Surge Residual", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Feb 2025 Surge Residual"}),
        ],
        outputs=[
            "series.name=surge_resid_2025-02; points=4; p1.value=-0.11; p2.value=0.07; p3.value=0.02; p4.value=-0.05 | "
            "qc.figure_label=QC_SURGE_RESID_2025-02; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf | "
            "stakeholder.output_label=Feb 2025 Surge Residual; audience=internal; artifact_path=https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_024",
        instruction=(
            "You have to Publish June-2025 salinity index dataset with QC. "
            "End state: time series 'sal_index_2025-06' holds three entries; "
            "[('2025-06-04T00:00:00Z', 33.1), ('2025-06-16T00:00:00Z', 34.2), ('2025-06-29T00:00:00Z', 32.8)] "
            "QC report 'QC_SAL_INDEX_2025-06' (pdf) is stored and readable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "sal_index_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 33.1},
                {"timestamp": "2025-06-16T00:00:00Z", "value": 34.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": 32.8}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "sal_index_2025-06"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SAL_INDEX_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
        ],
        outputs=[
            "series.name=sal_index_2025-06; points=3; p1.value=33.1; p2.value=34.2; p3.value=32.8 | "
            "qc.figure_label=QC_SAL_INDEX_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_025",
        instruction=(
            "You Assemble rainfall deviation set for May-2025 with QC check. "
            "End state: series 'rain_dev_2025-05' contains three values; "
            "[('2025-05-03T00:00:00Z', -5.1), ('2025-05-12T00:00:00Z', 2.4), ('2025-05-25T00:00:00Z', -1.7)]; "
            "QC artifact 'QC_RAIN_DEV_2025-05' is present (pdf)."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "rain_dev_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": -5.1},
                {"timestamp": "2025-05-12T00:00:00Z", "value": 2.4},
                {"timestamp": "2025-05-25T00:00:00Z", "value": -1.7}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "rain_dev_2025-05"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_RAIN_DEV_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
        ],
        outputs=[
            "series.name=rain_dev_2025-05; points=3; p1.value=-5.1; p2.value=2.4; p3.value=-1.7 | "
            "qc.figure_label=QC_RAIN_DEV_2025-05; qc.figure_path=https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_026",
        instruction=(
            "You validate a 30-year NOAA tide gauge archive. End state: "
            "processed series 'noaa_tide_qc_1990_2020' contains summary values [('mean_sea_level', 2.34), ('max_tide', 3.78)] and can be retrieved; "
            "a QC PDF with label 'QC_NOAA_TIDE_1990_2020' is stored (artifact_type 'pdf') and retrievable; "
            "stakeholder artifact 'NOAA Tide QC 1990-2020' (audience 'internal') points to 'https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf' and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_tide_qc_1990_2020", "items": [
                {"timestamp": "mean_sea_level", "value": 2.34},
                {"timestamp": "max_tide", "value": 3.78}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_tide_qc_1990_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA Tide QC 1990-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA Tide QC 1990-2020"}),
        ],
        outputs=[
            "series.name=noaa_tide_qc_1990_2020; points=2; p1.ts=mean_sea_level; p1.value=2.34; p2.ts=max_tide; p2.value=3.78 | "
            "qc.figure_label=QC_NOAA_TIDE_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf | "
            "stakeholder.output_label=NOAA Tide QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_027",
        instruction=(
            "You release a March-2025 salinity anomaly dataset. End state: "
            "processed series 'salinity_anom_2025-03' holds three entries [('2025-03-07T00:00:00Z', 0.07), ('2025-03-14T00:00:00Z', -0.02), ('2025-03-21T00:00:00Z', 0.04)] and is retrievable; "
            "a QC PDF for label 'QC_SAL_ANOM_2025-03' is logged (artifact_type 'pdf') and retrievable; "
            "stakeholder artifact 'Salinity Anomaly Mar 2025' (audience 'internal') points to 'https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf' and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "salinity_anom_2025-03", "items": [
                {"timestamp": "2025-03-07T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-03-14T00:00:00Z", "value": -0.02},
                {"timestamp": "2025-03-21T00:00:00Z", "value": 0.04}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "salinity_anom_2025-03"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Salinity Anomaly Mar 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Salinity Anomaly Mar 2025"}),
        ],
        outputs=[
            "series.name=salinity_anom_2025-03; points=3; p1.ts=2025-03-07T00:00:00Z; p1.value=0.07; p2.ts=2025-03-14T00:00:00Z; p2.value=-0.02; p3.ts=2025-03-21T00:00:00Z; p3.value=0.04 | "
            "qc.figure_label=QC_SAL_ANOM_2025-03; qc.figure_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf | "
            "stakeholder.output_label=Salinity Anomaly Mar 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_028",
        instruction=(
            "You maintain the feature bundle 'harbor_ops_v2' and designate it active with QC. End state: "
            "feature_set 'harbor_ops_v2' (version '2.0') with fields ['arrival_count','dwell_time_median','departure_count'] is stored and retrievable; "
            "file '/features/harbor_ops_v2.parquet' is present and retrievable; "
            "project setting 'active_feature_set' equals 'harbor_ops_v2' and is retrievable; "
            "QC PDF for label 'QC_HARBOR_OPS_2025-03' is recorded (artifact_type 'pdf') and retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "harbor_ops_v2", "version": "2.0",
                                                           "columns": ["arrival_count", "dwell_time_median",
                                                                       "departure_count"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "harbor_ops_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/harbor_ops_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/harbor_ops_v2.parquet"}),

            Action(name="patch_project_settings", kwargs={"updates": {"active_feature_set": "harbor_ops_v2"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
        ],
        outputs=[
            "feature_set.name=harbor_ops_v2; version=2.0; columns=arrival_count|dwell_time_median|departure_count | "
            "file.path=/features/harbor_ops_v2.parquet; file.mime=application/parquet | "
            "config.active_feature_set=harbor_ops_v2 | "
            "qc.figure_label=QC_HARBOR_OPS_2025-03; qc.figure_path=https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_029",
        instruction=(
            "You Release April-2025 temperature anomaly dataset with QC and internal report. "
            "End state: series 'temp_anom_2025-04' has two entries; "
            "[('2025-04-10T00:00:00Z', 1.1), ('2025-04-25T00:00:00Z', -0.3)] and is readable; "
            "QC file 'QC_TEMP_ANOM_2025-04' exists (pdf); "
            "stakeholder output 'Temp Anomaly Apr 2025' (audience=internal) is linked."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-10T00:00:00Z", "value": 1.1},
                {"timestamp": "2025-04-25T00:00:00Z", "value": -0.3}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Temp Anomaly Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Temp Anomaly Apr 2025"}),
        ],
        outputs=[
            "series.name=temp_anom_2025-04; points=2; p1.value=1.1; p2.value=-0.3 | "
            "qc.figure_label=QC_TEMP_ANOM_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf | "
            "stakeholder.output_label=Temp Anomaly Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_030",
        instruction=(
            "You generate the June 2025 precipitation anomaly dataset, verify QC, and archive results. "
            "End state: processed series 'precip_anom_2025-06' holds three values "
            "[('2025-06-01T00:00:00Z', -5.0), ('2025-06-15T00:00:00Z', 3.2), ('2025-06-29T00:00:00Z', -1.1)] "
            "and can be retrieved; QC record 'QC_PRECIP_ANOM_2025-06' (pdf) is created and available."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "precip_anom_2025-06", "items": [
                {"timestamp": "2025-06-01T00:00:00Z", "value": -5.0},
                {"timestamp": "2025-06-15T00:00:00Z", "value": 3.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": -1.1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "precip_anom_2025-06"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_PRECIP_ANOM_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=precip_anom_2025-06; points=3; "
            "p1.ts=2025-06-01T00:00:00Z; p1.value=-5.0; "
            "p2.ts=2025-06-15T00:00:00Z; p2.value=3.2; "
            "p3.ts=2025-06-29T00:00:00Z; p3.value=-1.1 | "
            "qc.figure_label=QC_PRECIP_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_031",
        instruction=(
            "You capture February 2025 river flow anomaly data, verify QC output, and store results. "
            "End state: processed series 'flow_anom_2025-02' includes three records "
            "[('2025-02-03T00:00:00Z', 120), ('2025-02-14T00:00:00Z', 110), ('2025-02-25T00:00:00Z', 130)] "
            "and is retrievable; a QC report with label 'QC_FLOW_ANOM_2025-02' (pdf) is generated and accessible."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "flow_anom_2025-02", "items": [
                {"timestamp": "2025-02-03T00:00:00Z", "value": 120},
                {"timestamp": "2025-02-14T00:00:00Z", "value": 110},
                {"timestamp": "2025-02-25T00:00:00Z", "value": 130}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "flow_anom_2025-02"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_FLOW_ANOM_2025-02",
                "figure_path": "https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
        ],
        outputs=[
            "series.name=flow_anom_2025-02; points=3; "
            "p1.ts=2025-02-03T00:00:00Z; p1.value=120; "
            "p2.ts=2025-02-14T00:00:00Z; p2.value=110; "
            "p3.ts=2025-02-25T00:00:00Z; p3.value=130 | "
            "qc.figure_label=QC_FLOW_ANOM_2025-02; qc.figure_path=https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_032",
        instruction=(
            "You Prepare feature collection 'precip_extremes_v1' (version '1.0') with columns "
            "['daily_rainfall_max','monthly_rainfall_mean','extreme_event_count'] and mark it active. Final state: "
            "feature set is queryable; the file '/features/precip_extremes_v1.parquet' exists and is valid; "
            "project option 'climate_features' is set to 'precip_extremes_v1'; QC summary 'QC_PRECIP_2025-08' is registered as a PDF."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "precip_extremes_v1", "version": "1.0",
                                                           "columns": ["daily_rainfall_max", "monthly_rainfall_mean",
                                                                       "extreme_event_count"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "precip_extremes_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/precip_extremes_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/precip_extremes_v1.parquet"}),

            Action(name="patch_project_settings", kwargs={"updates": {"climate_features": "precip_extremes_v1"}}),
            Action(name="read_project_settings", kwargs={}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-08"}),
        ],
        outputs=[
            "feature_set.name=precip_extremes_v1; version=1.0; columns=daily_rainfall_max|monthly_rainfall_mean|extreme_event_count | "
            "file.path=/features/precip_extremes_v1.parquet; file.mime=application/parquet | "
            "config.climate_features=precip_extremes_v1 | "
            "qc.figure_label=QC_PRECIP_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-08.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_033",
        instruction=(
            "You Run QC for the merged satellite rainfall dataset spanning 2000–2020. Final state: "
            "time series 'rainfall_sat_qc_2000_2020' holds [('avg_rainfall',114.6),('max_rainfall_day',312.0)] and is accessible; "
            "QC record 'QC_RAINFALL_SAT_2000_2020' is a stored PDF; "
            "stakeholder output 'Rainfall QC 2000-2020' (audience external) links to 'https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf'."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "rainfall_sat_qc_2000_2020", "items": [
                {"timestamp": "avg_rainfall", "value": 114.6},
                {"timestamp": "max_rainfall_day", "value": 312.0}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "rainfall_sat_qc_2000_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Rainfall QC 2000-2020", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Rainfall QC 2000-2020"}),
        ],
        outputs=[
            "series.name=rainfall_sat_qc_2000_2020; points=2; p1.ts=avg_rainfall; p1.value=114.6; p2.ts=max_rainfall_day; p2.value=312.0 | "
            "qc.figure_label=QC_RAINFALL_SAT_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf | "
            "stakeholder.output_label=Rainfall QC 2000-2020; audience=external; artifact_path=https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_034",
        instruction=(
            "You Validate 25 years of atmospheric CO₂ records. Final state: "
            "series 'co2_qc_1990_2015' has [('avg_co2_ppm',402.5),('max_co2_ppm',419.1)] retrievable; "
            "QC PDF 'QC_CO2_1990_2015' exists; "
            "stakeholder product 'Global CO₂ QC 1990-2015' (external) links to 'https://storage.example.com/reports/QC_CO2_1990_2015.pdf'."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "co2_qc_1990_2015", "items": [
                {"timestamp": "avg_co2_ppm", "value": 402.5},
                {"timestamp": "max_co2_ppm", "value": 419.1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "co2_qc_1990_2015"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CO2_1990_2015"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CO2_1990_2015",
                                                    "figure_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CO2_1990_2015"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Global CO₂ QC 1990-2015", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Global CO₂ QC 1990-2015"}),
        ],
        outputs=[
            "series.name=co2_qc_1990_2015; points=2; p1.ts=avg_co2_ppm; p1.value=402.5; p2.ts=max_co2_ppm; p2.value=419.1 | "
            "qc.figure_label=QC_CO2_1990_2015; qc.figure_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf | "
            "stakeholder.output_label=Global CO₂ QC 1990-2015; audience=external; artifact_path=https://storage.example.com/reports/QC_CO2_1990_2015.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_035",
        instruction=(
            "You Check river flow data for the Amazon (1980–2010). Final state: "
            "series 'amazon_discharge_qc_1980_2010' contains [('avg_discharge',85000.0),('peak_discharge',120000.0)] retrievable; "
            "QC record 'QC_AMAZON_DISCHARGE_1980_2010' (pdf) is stored; "
            "stakeholder output 'Amazon River Discharge QC 1980-2010' (internal) points to 'https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf'."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "amazon_discharge_qc_1980_2010", "items": [
                {"timestamp": "avg_discharge", "value": 85000.0},
                {"timestamp": "peak_discharge", "value": 120000.0}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "amazon_discharge_qc_1980_2010"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010",
                                                    "figure_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Amazon River Discharge QC 1980-2010", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Amazon River Discharge QC 1980-2010"}),
        ],
        outputs=[
            "series.name=amazon_discharge_qc_1980_2010; points=2; p1.ts=avg_discharge; p1.value=85000.0; p2.ts=peak_discharge; p2.value=120000.0 | "
            "qc.figure_label=QC_AMAZON_DISCHARGE_1980_2010; qc.figure_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf | "
            "stakeholder.output_label=Amazon River Discharge QC 1980-2010; audience=internal; artifact_path=https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_036",
        instruction=(
            "You Register 'ARIMA_Tide_v2' and validate on May 2025 batch with QC. "
            "Final state: model 'ARIMA_Tide_v2' (type arima, framework statsmodels, version 2.0, status staged) is stored and retrievable; "
            "validation lot 'VAL_TIDE_2025-05' has one entry ('2025-05-09T00:00:00Z', 1.45); "
            "MAPE 7.8 is logged; "
            "QC report 'QC_TIDE_VAL_2025-05' exists as PDF."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "ARIMA_Tide_v2", "model_type": "arima", "framework": "statsmodels",
                           "version": "2.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="write_prediction_lot", kwargs={"batch_name": "VAL_TIDE_2025-05", "model_name": "ARIMA_Tide_v2",
                                                        "items": [{"timestamp": "2025-05-09T00:00:00Z",
                                                                   "prediction": 1.45}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_TIDE_2025-05"}),

            Action(name="log_model_metric", kwargs={"model_name": "ARIMA_Tide_v2", "metric_name": "MAPE", "value": 7.8,
                                                    "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDE_VAL_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDE_VAL_2025-05"}),
        ],
        outputs=[
            "model.name=ARIMA_Tide_v2; type=arima; framework=statsmodels; version=2.0; status=staged | "
            "pred.batch_name=VAL_TIDE_2025-05; pred.model=ARIMA_Tide_v2; rows=1; first_ts=2025-05-09T00:00:00Z; first_pred=1.45 | "
            "metric.model=ARIMA_Tide_v2; metric.name=MAPE; metric.value=7.8; split=validation | "
            "qc.figure_label=QC_TIDE_VAL_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_037",
        instruction=(
            "You Onboard 'GRU_Temperature_v1' with June 2025 validation and QC. "
            "Model 'GRU_Temperature_v1' (type gru, framework pytorch, version 1.0, status staged) is stored; "
            "batch 'VAL_TEMP_2025-06' has one record ('2025-06-18T12:00:00Z', 27.6); "
            "MAE 0.3 is logged; "
            "QC image 'QC_TEMP_VAL_2025-06' exists as PNG."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "GRU_Temperature_v1", "model_type": "gru", "framework": "pytorch",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_TEMP_2025-06", "model_name": "GRU_Temperature_v1",
                           "items": [{"timestamp": "2025-06-18T12:00:00Z", "prediction": 27.6}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_TEMP_2025-06"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "GRU_Temperature_v1", "metric_name": "MAE", "value": 0.3,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_TEMP_VAL_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TEMP_VAL_2025-06"}),
        ],
        outputs=[
            "model.name=GRU_Temperature_v1; type=gru; framework=pytorch; version=1.0; status=staged | "
            "pred.batch_name=VAL_TEMP_2025-06; pred.model=GRU_Temperature_v1; rows=1; first_ts=2025-06-18T12:00:00Z; first_pred=27.6 | "
            "metric.model=GRU_Temperature_v1; metric.name=MAE; metric.value=0.3; split=validation | "
            "qc.figure_label=QC_TEMP_VAL_2025-06; qc.figure_path=https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_038",
        instruction=(
            "You Stage 'XGBoost_FloodRisk_v1' with July 2025 validation data. "
            "Model 'XGBoost_FloodRisk_v1' is stored (type xgboost, framework xgboost, version 1.0, status staged); "
            "lot 'VAL_FR_2025-07' has entry ('2025-07-20T00:00:00Z', 0.34); "
            "RMSE 0.05 logged; "
            "QC PDF 'QC_FR_VAL_2025-07' exists."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "XGBoost_FloodRisk_v1", "model_type": "xgboost", "framework": "xgboost",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_FR_2025-07", "model_name": "XGBoost_FloodRisk_v1",
                           "items": [{"timestamp": "2025-07-20T00:00:00Z", "prediction": 0.34}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_FR_2025-07"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "XGBoost_FloodRisk_v1", "metric_name": "RMSE", "value": 0.05,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_FR_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FR_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=XGBoost_FloodRisk_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "pred.batch_name=VAL_FR_2025-07; pred.model=XGBoost_FloodRisk_v1; rows=1; first_ts=2025-07-20T00:00:00Z; first_pred=0.34 | "
            "metric.model=XGBoost_FloodRisk_v1; metric.name=RMSE; metric.value=0.05; split=validation | "
            "qc.figure_label=QC_FR_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_039",
        instruction=(
            "You Validate 'CNN_WaveHeight_v1' with Sept 2025 batch and QC. "
            "Final state: model stored (cnn, tensorflow, v1.0, staged); "
            "lot 'VAL_WH_2025-09' has entry ('2025-09-05T06:00:00Z', 1.72); "
            "MAE 0.12 logged; "
            "QC PNG 'QC_WH_VAL_2025-09' available."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "CNN_WaveHeight_v1", "model_type": "cnn", "framework": "tensorflow",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_WH_2025-09", "model_name": "CNN_WaveHeight_v1",
                           "items": [{"timestamp": "2025-09-05T06:00:00Z", "prediction": 1.72}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_WH_2025-09"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "CNN_WaveHeight_v1", "metric_name": "MAE", "value": 0.12,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_WH_VAL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_WH_VAL_2025-09.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WH_VAL_2025-09"}),
        ],
        outputs=[
            "model.name=CNN_WaveHeight_v1; type=cnn; framework=tensorflow; version=1.0; status=staged | "
            "pred.batch_name=VAL_WH_2025-09; pred.model=CNN_WaveHeight_v1; rows=1; first_ts=2025-09-05T06:00:00Z; first_pred=1.72 | "
            "metric.model=CNN_WaveHeight_v1; metric.name=MAE; metric.value=0.12; split=validation | "
            "qc.figure_label=QC_WH_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WH_VAL_2025-09.png"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_040",
        instruction=(
            "You Stage 'LSTM_Rainfall_v2' with Aug 2025 validation lot + QC. "
            "Model stored (lstm, pytorch, v2.0, staged); "
            "lot 'VAL_RF_2025-08' includes one entry ('2025-08-10T12:00:00Z', 22.5); "
            "RMSE 1.05 logged; "
            "QC PDF 'QC_RF_VAL_2025-08' exists."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "LSTM_Rainfall_v2", "model_type": "lstm", "framework": "pytorch",
                           "version": "2.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_RF_2025-08", "model_name": "LSTM_Rainfall_v2",
                           "items": [{"timestamp": "2025-08-10T12:00:00Z", "prediction": 22.5}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_RF_2025-08"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "LSTM_Rainfall_v2", "metric_name": "RMSE", "value": 1.05,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_RF_VAL_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RF_VAL_2025-08"}),
        ],
        outputs=[
            "model.name=LSTM_Rainfall_v2; type=lstm; framework=pytorch; version=2.0; status=staged | "
            "pred.batch_name=VAL_RF_2025-08; pred.model=LSTM_Rainfall_v2; rows=1; first_ts=2025-08-10T12:00:00Z; first_pred=22.5 | "
            "metric.model=LSTM_Rainfall_v2; metric.name=RMSE; metric.value=1.05; split=validation | "
            "qc.figure_label=QC_RF_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_041",
        instruction=(
            "You have to Summarize April-2025 sales ETL and notify finance. Final state: "
            "ETL job 'sales_rollup_2025-04' (task monthly_sales_aggregation) status finished, rows_processed=420; "
            "QC 'QC_SALES_2025-04' exists as PDF; "
            "audit event 'SALES_QC_DONE' with message; 'April sales aggregation complete.'"
            "email sent to finance-team@example.com with subject 'QC_SALES_2025-04', body 'Sales aggregation QC attached.' and attachment URL is sent."
        ),
        actions=[
            Action(name="log_etl_execution",
                   kwargs={"run_name": "sales_rollup_2025-04", "task": "monthly_sales_aggregation",
                           "status": "finished", "rows_processed": 420}),
            Action(name="fetch_etl_execution", kwargs={"run_name": "sales_rollup_2025-04"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SALES_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SALES_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_SALES_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SALES_2025-04"}),

            Action(name="append_audit_event",
                   kwargs={"event_type": "SALES_QC_DONE", "message": "April sales aggregation complete."}),
            Action(name="read_audit_events", kwargs={"event_type": "SALES_QC_DONE"}),

            Action(name="dispatch_results_mail",
                   kwargs={"to_address": "finance-team@example.com", "subject": "QC_SALES_2025-04",
                           "body_text": "Sales aggregation QC attached.",
                           "attachment": "https://storage.example.com/reports/QC_SALES_2025-04.pdf"}),
        ],
        outputs=[
            "etl.run_name=sales_rollup_2025-04; etl.task=monthly_sales_aggregation; etl.status=finished; etl.rows_processed=420 | "
            "qc.figure_label=QC_SALES_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SALES_2025-04.pdf | "
            "audit.event_type=SALES_QC_DONE; audit.message=April sales aggregation complete. | "
            "email.to=finance-team@example.com; email.subject=QC_SALES_2025-04; email.attachment=https://storage.example.com/reports/QC_SALES_2025-04.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_042",
        instruction=(
            "You Compile Jan-2025 precipitation totals and share externally. "
            "Series 'precip_total_2025-01' has 3 values; "
            "[('2025-01-05T00:00:00Z', 14.2), ('2025-01-18T00:00:00Z', 9.7), ('2025-01-30T00:00:00Z', 12.5)] and is retrievable; "
            "QC report 'QC_PRECIP_2025-01' exists; "
            "stakeholder report 'Jan 2025 Precipitation Summary' audience external."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "precip_total_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 14.2},
                {"timestamp": "2025-01-18T00:00:00Z", "value": 9.7},
                {"timestamp": "2025-01-30T00:00:00Z", "value": 12.5}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "precip_total_2025-01"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-01"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-01",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PRECIP_2025-01"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Jan 2025 Precipitation Summary", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Jan 2025 Precipitation Summary"}),
        ],
        outputs=[
            "series.name=precip_total_2025-01; points=3; p1.ts=2025-01-05T00:00:00Z; p1.value=14.2; p2.ts=2025-01-18T00:00:00Z; p2.value=9.7; p3.ts=2025-01-30T00:00:00Z; p3.value=12.5 | "
            "qc.figure_label=QC_PRECIP_2025-01; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf | "
            "stakeholder.output_label=Jan 2025 Precipitation Summary; audience=external; artifact_path=https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_043",
        instruction=(
            "You Prepare April-2025 tidal maxima, validate QC, and release a municipal summary. "
            "Result: series 'tide_max_2025-04' has 3 values [('2025-04-02T00:00:00Z',3.12),('2025-04-15T00:00:00Z',3.44),('2025-04-29T00:00:00Z',3.21)] retrievable; "
            "QC report 'QC_TIDE_MAX_2025-04' exists as PDF; "
            "stakeholder summary 'April 2025 Tide Max Report' (audience municipal) links to QC doc."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "tide_max_2025-04", "items": [
                {"timestamp": "2025-04-02T00:00:00Z", "value": 3.12},
                {"timestamp": "2025-04-15T00:00:00Z", "value": 3.44},
                {"timestamp": "2025-04-29T00:00:00Z", "value": 3.21}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "tide_max_2025-04"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDE_MAX_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "April 2025 Tide Max Report", "audience": "municipal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "April 2025 Tide Max Report"}),
        ],
        outputs=[
            "series.name=tide_max_2025-04; points=3; p1.ts=2025-04-02T00:00:00Z; p1.value=3.12; p2.ts=2025-04-15T00:00:00Z; p2.value=3.44; p3.ts=2025-04-29T00:00:00Z; p3.value=3.21 | "
            "qc.figure_label=QC_TIDE_MAX_2025-04; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf | "
            "stakeholder.output_label=April 2025 Tide Max Report; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_044",
        instruction=(
            "You QC coastal wind dataset (1995–2015) and create internal summary. "
            "Result: processed set 'wind_qc_1995_2015' holds [('avg_wind',12.4),('max_wind_day',68.0)] retrievable; "
            "QC file 'QC_WIND_1995_2015' exists as PDF; "
            "stakeholder report 'Wind QC 1995-2015' (audience internal) references QC doc."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "wind_qc_1995_2015", "items": [
                {"timestamp": "avg_wind", "value": 12.4},
                {"timestamp": "max_wind_day", "value": 68.0}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "wind_qc_1995_2015"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WIND_1995_2015"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WIND_1995_2015",
                                                    "figure_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WIND_1995_2015"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Wind QC 1995-2015", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Wind QC 1995-2015"}),
        ],
        outputs=[
            "series.name=wind_qc_1995_2015; points=2; p1.ts=avg_wind; p1.value=12.4; p2.ts=max_wind_day; p2.value=68.0 | "
            "qc.figure_label=QC_WIND_1995_2015; qc.figure_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf | "
            "stakeholder.output_label=Wind QC 1995-2015; audience=internal; artifact_path=https://storage.example.com/reports/QC_WIND_1995_2015.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_045",
        instruction=(
            "You Configure and validate 'LSTM_StormSurge_v3' with July-2025 data. "
            "Result: model 'LSTM_StormSurge_v3' (type lstm, framework tensorflow, version 3.0, status staged) is saved and queryable; "
            "validation batch 'VAL_SS_2025-07' contains one row ('2025-07-15T03:00:00Z', 1.92); "
            "validation MAE=0.15 logged; "
            "QC record 'QC_SS_VAL_2025-07' stored as CSV."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "LSTM_StormSurge_v3", "model_type": "lstm", "framework": "tensorflow",
                           "version": "3.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_SS_2025-07", "model_name": "LSTM_StormSurge_v3",
                           "items": [{"timestamp": "2025-07-15T03:00:00Z", "prediction": 1.92}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_SS_2025-07"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "LSTM_StormSurge_v3", "metric_name": "MAE", "value": 0.15,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_SS_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_SS_VAL_2025-07.csv",
                                                    "artifact_type": "csv"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SS_VAL_2025-07"}),
        ],
        outputs=[
            "model.name=LSTM_StormSurge_v3; type=lstm; framework=tensorflow; version=3.0; status=staged | "
            "pred.batch_name=VAL_SS_2025-07; pred.model=LSTM_StormSurge_v3; rows=1; first_ts=2025-07-15T03:00:00Z; first_pred=1.92 | "
            "metric.model=LSTM_StormSurge_v3; metric.name=MAE; metric.value=0.15; split=validation | "
            "qc.figure_label=QC_SS_VAL_2025-07; qc.figure_path=https://storage.example.com/reports/QC_SS_VAL_2025-07.csv"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_046",
        instruction=(
            "You Set up 'ARIMA_Precip_v1' and log August-2025 validation. "
            "Result: model 'ARIMA_Precip_v1' (type arima, framework statsmodels, version 1.0, status staged) is recorded; "
            "validation batch 'VAL_PC_2025-08' contains ('2025-08-05T12:00:00Z', 5.7); "
            "R²=0.89 captured; "
            "QC file 'QC_PC_VAL_2025-08' saved as PDF."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "ARIMA_Precip_v1", "model_type": "arima", "framework": "statsmodels",
                           "version": "1.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="write_prediction_lot", kwargs={"batch_name": "VAL_PC_2025-08", "model_name": "ARIMA_Precip_v1",
                                                        "items": [
                                                            {"timestamp": "2025-08-05T12:00:00Z", "prediction": 5.7}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_PC_2025-08"}),

            Action(name="log_model_metric", kwargs={"model_name": "ARIMA_Precip_v1", "metric_name": "R2", "value": 0.89,
                                                    "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_PC_VAL_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PC_VAL_2025-08"}),
        ],
        outputs=[
            "model.name=ARIMA_Precip_v1; type=arima; framework=statsmodels; version=1.0; status=staged | "
            "pred.batch_name=VAL_PC_2025-08; pred.model=ARIMA_Precip_v1; rows=1; first_ts=2025-08-05T12:00:00Z; first_pred=5.7 | "
            "metric.model=ARIMA_Precip_v1; metric.name=R2; metric.value=0.89; split=validation | "
            "qc.figure_label=QC_PC_VAL_2025-08; qc.figure_path=https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_047",
        instruction=(
            "You Register 'RandomForest_Wind_v5' and log September-2025 validation. "
            "Result: model 'RandomForest_Wind_v5' (type random_forest, framework sklearn, version 5.0, status staged) is stored; "
            "validation batch 'VAL_WD_2025-09' includes ('2025-09-18T15:00:00Z', 12.6); "
            "RMSE=1.2 saved; "
            "QC PNG 'QC_WD_VAL_2025-09' recorded and retrievable."
        ),
        actions=[
            Action(name="store_model_artifact",
                   kwargs={"model_name": "RandomForest_Wind_v5", "model_type": "random_forest", "framework": "sklearn",
                           "version": "5.0", "status": "staged"}),
            Action(name="fetch_model_record", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="write_prediction_lot",
                   kwargs={"batch_name": "VAL_WD_2025-09", "model_name": "RandomForest_Wind_v5",
                           "items": [{"timestamp": "2025-09-18T15:00:00Z", "prediction": 12.6}]}),
            Action(name="read_prediction_lots", kwargs={"batch_name": "VAL_WD_2025-09"}),

            Action(name="log_model_metric",
                   kwargs={"model_name": "RandomForest_Wind_v5", "metric_name": "RMSE", "value": 1.2,
                           "dataset_split": "validation"}),
            Action(name="read_model_metrics", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="record_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-09.png",
                                                    "artifact_type": "png"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WD_VAL_2025-09"}),
        ],
        outputs=[
            "model.name=RandomForest_Wind_v5; type=random_forest; framework=sklearn; version=5.0; status=staged | "
            "pred.batch_name=VAL_WD_2025-09; pred.model=RandomForest_Wind_v5; rows=1; first_ts=2025-09-18T15:00:00Z; first_pred=12.6 | "
            "metric.model=RandomForest_Wind_v5; metric.name=RMSE; metric.value=1.2; split=validation | "
            "qc.figure_label=QC_WD_VAL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_WD_VAL_2025-09.png"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_048",
        instruction=(
            "You Validate a 25-year NOAA coastal wind record. "
            "Final state: processed set 'noaa_wind_qc_1995_2020' holds [('mean_wind_speed', 12.4), ('max_wind_speed', 29.8)]; "
            "QC report 'QC_NOAA_WIND_1995_2020' (pdf) is archived; "
            "stakeholder deliverable 'NOAA Wind QC 1995-2020' for internal use points to the QC file."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_wind_qc_1995_2020", "items": [
                {"timestamp": "mean_wind_speed", "value": 12.4},
                {"timestamp": "max_wind_speed", "value": 29.8}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_wind_qc_1995_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA Wind QC 1995-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA Wind QC 1995-2020"}),
        ],
        outputs=[
            "series.name=noaa_wind_qc_1995_2020; points=2; p1.ts=mean_wind_speed; p1.value=12.4; p2.ts=max_wind_speed; p2.value=29.8 | "
            "qc.figure_label=QC_NOAA_WIND_1995_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf | "
            "stakeholder.output_label=NOAA Wind QC 1995-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_049",
        instruction=(
            "You Quality-check a 20-year NOAA river discharge record. "
            "End result: processed series 'noaa_river_qc_2000_2020' captures [('mean_discharge', 350.6), ('max_discharge', 1120.3)]; "
            "QC artifact 'QC_NOAA_RIVER_2000_2020' is registered as pdf; "
            "stakeholder note 'NOAA River QC 2000-2020' (internal) links to the stored file."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_river_qc_2000_2020", "items": [
                {"timestamp": "mean_discharge", "value": 350.6},
                {"timestamp": "max_discharge", "value": 1120.3}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_river_qc_2000_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA River QC 2000-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA River QC 2000-2020"}),
        ],
        outputs=[
            "series.name=noaa_river_qc_2000_2020; points=2; p1.ts=mean_discharge; p1.value=350.6; p2.ts=max_discharge; p2.value=1120.3 | "
            "qc.figure_label=QC_NOAA_RIVER_2000_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf | "
            "stakeholder.output_label=NOAA River QC 2000-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_050",
        instruction=(
            "You Perform QC on a 15-year NOAA rainfall dataset. "
            "Target state: 'noaa_precip_qc_2005_2020' includes [('mean_precip', 102.7), ('max_precip_day', 210.5)]; "
            "QC report 'QC_NOAA_PRECIP_2005_2020' saved as pdf; "
            "summary 'NOAA Precip QC 2005-2020' (internal) published with link to the file."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_precip_qc_2005_2020", "items": [
                {"timestamp": "mean_precip", "value": 102.7},
                {"timestamp": "max_precip_day", "value": 210.5}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_precip_qc_2005_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA Precip QC 2005-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA Precip QC 2005-2020"}),
        ],
        outputs=[
            "series.name=noaa_precip_qc_2005_2020; points=2; p1.ts=mean_precip; p1.value=102.7; p2.ts=max_precip_day; p2.value=210.5 | "
            "qc.figure_label=QC_NOAA_PRECIP_2005_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf | "
            "stakeholder.output_label=NOAA Precip QC 2005-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_051",
        instruction=(
            "You Check and register a decade NOAA salinity dataset. "
            "Final outcome: 'noaa_salinity_qc_2010_2020' has [('mean_salinity', 35.1), ('max_salinity', 36.7)]; "
            "QC doc 'QC_NOAA_SALINITY_2010_2020' stored as pdf; "
            "stakeholder record 'NOAA Salinity QC 2010-2020' (internal) links to the report."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_salinity_qc_2010_2020", "items": [
                {"timestamp": "mean_salinity", "value": 35.1},
                {"timestamp": "max_salinity", "value": 36.7}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_salinity_qc_2010_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA Salinity QC 2010-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA Salinity QC 2010-2020"}),
        ],
        outputs=[
            "series.name=noaa_salinity_qc_2010_2020; points=2; p1.ts=mean_salinity; p1.value=35.1; p2.ts=max_salinity; p2.value=36.7 | "
            "qc.figure_label=QC_NOAA_SALINITY_2010_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf | "
            "stakeholder.output_label=NOAA Salinity QC 2010-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_052",
        instruction=(
            "You Audit a 12-year NOAA sea surface temperature series. "
            "Final state: 'noaa_sst_qc_2008_2020' reports [('mean_sst', 18.5), ('max_sst', 29.2)]; "
            "QC label 'QC_NOAA_SST_2008_2020' (pdf) stored; "
            "stakeholder entry 'NOAA SST QC 2008-2020' (internal) published with reference."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_sst_qc_2008_2020", "items": [
                {"timestamp": "mean_sst", "value": 18.5},
                {"timestamp": "max_sst", "value": 29.2}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_sst_qc_2008_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_SST_2008_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA SST QC 2008-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA SST QC 2008-2020"}),
        ],
        outputs=[
            "series.name=noaa_sst_qc_2008_2020; points=2; p1.ts=mean_sst; p1.value=18.5; p2.ts=max_sst; p2.value=29.2 | "
            "qc.figure_label=QC_NOAA_SST_2008_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf | "
            "stakeholder.output_label=NOAA SST QC 2008-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_053",
        instruction=(
            "You prepare a logistic-regression wildfire risk dataset 'wildfire_risk_v1' for 2025-06. Final state: "
            "feature set 'wildfire_risk_v1' (version '1.0') with columns ['temperature','humidity','fire_risk'] is registered and readable; "
            "feature file '/features/wildfire_risk_v1.parquet' exists and can be retrieved; "
            "a QC PDF is available for label 'QC_WILDFIRE_RISK_2025-06' with the figure recorded (artifact_type 'pdf') and readable; "
            "stakeholder output 'Wildfire Risk Jun 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "wildfire_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "humidity", "fire_risk"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "wildfire_risk_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/wildfire_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/wildfire_risk_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Wildfire Risk Jun 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Wildfire Risk Jun 2025"}),
        ],
        outputs=[
            "feature_set.name=wildfire_risk_v1; version=1.0; columns=temperature|humidity|fire_risk | "
            "file.path=/features/wildfire_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_WILDFIRE_RISK_2025-06; qc.figure_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf | "
            "stakeholder.output_label=Wildfire Risk Jun 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_054",
        instruction=(
            "You publish the flood prediction dataset 'flood_forecast_v2' for 2025-05. Final state: "
            "feature set 'flood_forecast_v2' (version '2.0') with columns ['rainfall','river_level','flood_probability'] is registered and readable; "
            "feature file '/features/flood_forecast_v2.parquet' exists and can be retrieved; "
            "a QC PDF for 'QC_FLOOD_FORECAST_2025-05' is rendered and stored (artifact_type 'pdf'); "
            "stakeholder output 'Flood Forecast May 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "flood_forecast_v2", "version": "2.0",
                                                           "columns": ["rainfall", "river_level",
                                                                       "flood_probability"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "flood_forecast_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/flood_forecast_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/flood_forecast_v2.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Flood Forecast May 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Flood Forecast May 2025"}),
        ],
        outputs=[
            "feature_set.name=flood_forecast_v2; version=2.0; columns=rainfall|river_level|flood_probability | "
            "file.path=/features/flood_forecast_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_FLOOD_FORECAST_2025-05; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf | "
            "stakeholder.output_label=Flood Forecast May 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_055",
        instruction=(
            "You curate the air quality prediction dataset 'air_quality_index_v3' for 2025-07. Final state: "
            "feature set 'air_quality_index_v3' (version '3.0') with columns ['PM2_5','PM10','AQI'] is registered and readable; "
            "feature file '/features/air_quality_index_v3.parquet' exists and can be retrieved; "
            "a QC PDF for 'QC_AIR_QUALITY_2025-07' is rendered and recorded (artifact_type 'pdf'); "
            "stakeholder output 'Air Quality Jul 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "air_quality_index_v3", "version": "3.0",
                                                           "columns": ["PM2_5", "PM10", "AQI"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "air_quality_index_v3"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/air_quality_index_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/air_quality_index_v3.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Air Quality Jul 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Air Quality Jul 2025"}),
        ],
        outputs=[
            "feature_set.name=air_quality_index_v3; version=3.0; columns=PM2_5|PM10|AQI | "
            "file.path=/features/air_quality_index_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_AIR_QUALITY_2025-07; qc.figure_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf | "
            "stakeholder.output_label=Air Quality Jul 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_056",
        instruction=(
            "You publish the coastal erosion prediction dataset 'coastal_erosion_v2' for 2025-08. Final state: "
            "feature set 'coastal_erosion_v2' (version '2.0') with columns ['wave_height','shoreline_change','erosion_risk'] is registered and readable; "
            "feature file '/features/coastal_erosion_v2.parquet' exists and can be retrieved; "
            "a QC PDF for 'QC_COASTAL_EROSION_2025-08' is rendered and recorded (artifact_type 'pdf'); "
            "stakeholder output 'Coastal Erosion Aug 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "coastal_erosion_v2", "version": "2.0",
                                                           "columns": ["wave_height", "shoreline_change",
                                                                       "erosion_risk"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "coastal_erosion_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/coastal_erosion_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/coastal_erosion_v2.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Coastal Erosion Aug 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Coastal Erosion Aug 2025"}),
        ],
        outputs=[
            "feature_set.name=coastal_erosion_v2; version=2.0; columns=wave_height|shoreline_change|erosion_risk | "
            "file.path=/features/coastal_erosion_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_COASTAL_EROSION_2025-08; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf | "
            "stakeholder.output_label=Coastal Erosion Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_057",
        instruction=(
            "You create a September-2025 sea-surface temperature anomaly dataset with QC. Final state: "
            "processed series 'sst_anom_2025-09' contains three entries [('2025-09-03T00:00:00Z', 0.25), ('2025-09-15T00:00:00Z', -0.12), ('2025-09-28T00:00:00Z', 0.08)] and is retrievable; "
            "a QC PDF under label 'QC_SST_ANOM_2025-09' is recorded and accessible."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "sst_anom_2025-09", "items": [
                {"timestamp": "2025-09-03T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-09-15T00:00:00Z", "value": -0.12},
                {"timestamp": "2025-09-28T00:00:00Z", "value": 0.08}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "sst_anom_2025-09"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SST_ANOM_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
        ],
        outputs=[
            "series.name=sst_anom_2025-09; points=3; p1.ts=2025-09-03T00:00:00Z; p1.value=0.25; p2.ts=2025-09-15T00:00:00Z; p2.value=-0.12; p3.ts=2025-09-28T00:00:00Z; p3.value=0.08 | "
            "qc.figure_label=QC_SST_ANOM_2025-09; qc.figure_path=https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_058",
        instruction=(
            "You generate an October-2025 chlorophyll anomaly dataset with QC. Final state: "
            "processed series 'chl_anom_2025-10' includes [('2025-10-01T00:00:00Z', 1.15), ('2025-10-12T00:00:00Z', -0.95), ('2025-10-25T00:00:00Z', 0.60)] and is retrievable; "
            "QC file 'QC_CHL_ANOM_2025-10' is registered as pdf and accessible."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "chl_anom_2025-10", "items": [
                {"timestamp": "2025-10-01T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-10-12T00:00:00Z", "value": -0.95},
                {"timestamp": "2025-10-25T00:00:00Z", "value": 0.60}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "chl_anom_2025-10"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CHL_ANOM_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
        ],
        outputs=[
            "series.name=chl_anom_2025-10; points=3; p1.ts=2025-10-01T00:00:00Z; p1.value=1.15; p2.ts=2025-10-12T00:00:00Z; p2.value=-0.95; p3.ts=2025-10-25T00:00:00Z; p3.value=0.60 | "
            "qc.figure_label=QC_CHL_ANOM_2025-10; qc.figure_path=https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_059",
        instruction=(
            "You log a November-2025 nitrate anomaly dataset with QC. Final state: "
            "processed series 'no3_anom_2025-11' contains [('2025-11-05T00:00:00Z', 0.55), ('2025-11-16T00:00:00Z', -0.40), ('2025-11-29T00:00:00Z', 0.22)] and is retrievable; "
            "QC report 'QC_NO3_ANOM_2025-11' is stored as pdf and accessible."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "no3_anom_2025-11", "items": [
                {"timestamp": "2025-11-05T00:00:00Z", "value": 0.55},
                {"timestamp": "2025-11-16T00:00:00Z", "value": -0.40},
                {"timestamp": "2025-11-29T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "no3_anom_2025-11"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NO3_ANOM_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
        ],
        outputs=[
            "series.name=no3_anom_2025-11; points=3; p1.ts=2025-11-05T00:00:00Z; p1.value=0.55; p2.ts=2025-11-16T00:00:00Z; p2.value=-0.40; p3.ts=2025-11-29T00:00:00Z; p3.value=0.22 | "
            "qc.figure_label=QC_NO3_ANOM_2025-11; qc.figure_path=https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_060",
        instruction=(
            "You register feature bundle 'port_departure_metrics_v1' version 1.1 and mark it active. Final state: "
            "feature bundle 'port_departure_metrics_v1' has columns ['departure_count','avg_wait_time','max_wait_time'] and is retrievable; "
            "feature file '/features/port_departure_metrics_v1.parquet' exists and can be read; "
            "project settings show 'active_feature_set' = 'port_departure_metrics_v1'; "
            "QC report 'QC_PORT_DEPARTURE_2025-03' is stored as pdf and accessible."
        ),
        actions=[
            Action(name="register_feature_bundle",
                   kwargs={"feature_set_name": "port_departure_metrics_v1", "version": "1.1",
                           "columns": ["departure_count", "avg_wait_time", "max_wait_time"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "port_departure_metrics_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/port_departure_metrics_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/port_departure_metrics_v1.parquet"}),

            Action(name="patch_project_settings",
                   kwargs={"updates": {"active_feature_set": "port_departure_metrics_v1"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
        ],
        outputs=[
            "feature_set.name=port_departure_metrics_v1; version=1.1; columns=departure_count|avg_wait_time|max_wait_time | "
            "file.path=/features/port_departure_metrics_v1.parquet; file.mime=application/parquet | "
            "config.active_feature_set=port_departure_metrics_v1 | "
            "qc.figure_label=QC_PORT_DEPARTURE_2025-03; qc.figure_path=https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_061",
        instruction=(
            "You distribute an April-2025 Puget Sound wave height dataset. End state: "
            "processed series 'wave_height_2025-04' holds three points [('2025-04-05T00:00:00Z', 1.2), ('2025-04-12T00:00:00Z', 0.8), ('2025-04-19T00:00:00Z', 1.5)] and is retrievable; "
            "a QC PDF labeled 'QC_WAVE_HEIGHT_2025-04' is stored (artifact_type 'pdf') and retrievable; "
            "stakeholder artifact 'Wave Height Apr 2025' (audience 'internal') points to 'https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf' and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "wave_height_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-12T00:00:00Z", "value": 0.8},
                {"timestamp": "2025-04-19T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "wave_height_2025-04"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Wave Height Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Wave Height Apr 2025"}),
        ],
        outputs=[
            "series.name=wave_height_2025-04; points=3; p1.ts=2025-04-05T00:00:00Z; p1.value=1.2; p2.ts=2025-04-12T00:00:00Z; p2.value=0.8; p3.ts=2025-04-19T00:00:00Z; p3.value=1.5 | "
            "qc.figure_label=QC_WAVE_HEIGHT_2025-04; qc.figure_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf | "
            "stakeholder.output_label=Wave Height Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_062",
        instruction=(
            "You assemble a logistic regression climate risk feature set 'climate_risk_v1' for Apr-2025. End state: "
            "feature_set 'climate_risk_v1' (version '1.0') with fields ['temperature','rainfall','flood_risk'] is stored and retrievable; "
            "file '/features/climate_risk_v1.parquet' is present and retrievable; "
            "QC PDF with label 'QC_CLIMATE_RISK_2025-04' is recorded (artifact_type 'pdf') and retrievable; "
            "stakeholder artifact 'Climate Risk Apr 2025' (audience 'internal') points to 'https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf' and is retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "climate_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "rainfall", "flood_risk"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "climate_risk_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/climate_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/climate_risk_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Climate Risk Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Climate Risk Apr 2025"}),
        ],
        outputs=[
            "feature_set.name=climate_risk_v1; version=1.0; columns=temperature|rainfall|flood_risk | "
            "file.path=/features/climate_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_CLIMATE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf | "
            "stakeholder.output_label=Climate Risk Apr 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_063",
        instruction=(
            "You validate surge-risk feature QC for April-2025. End state: "
            "feature bundle 'surge_risk_v2' (version 2.1) with columns ['risk_index','exceedance_prob'] is registered and readable; "
            "feature file '/features/surge_risk_v2.parquet' exists and is retrievable; "
            "QC report 'QC_SURGE_RISK_2025-04' is stored as pdf and accessible; "
            "stakeholder artifact 'Surge Risk QC Apr 2025' (audience regulators) is published with link to the pdf."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "surge_risk_v2", "version": "2.1",
                                                           "columns": ["risk_index", "exceedance_prob"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "surge_risk_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/surge_risk_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/surge_risk_v2.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SURGE_RISK_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Surge Risk QC Apr 2025", "audience": "regulators",
                           "artifact_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Surge Risk QC Apr 2025"}),
        ],
        outputs=[
            "feature_set.name=surge_risk_v2; version=2.1; columns=risk_index|exceedance_prob | "
            "file.path=/features/surge_risk_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SURGE_RISK_2025-04; qc.figure_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf | "
            "stakeholder.output_label=Surge Risk QC Apr 2025; audience=regulators; artifact_path=https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_064",
        instruction=(
            "You complete wave anomaly QC for May-2025. End state: "
            "feature bundle 'wave_anomaly_v1' (version 1.3) with columns ['hmean','hmax','stddev'] is registered and retrievable; "
            "feature file '/features/wave_anomaly_v1.parquet' exists and can be read; "
            "QC report 'QC_WAVE_ANOMALY_2025-05' is archived as pdf; "
            "stakeholder artifact 'Wave Anomaly QC May 2025' (audience science_team) points to the pdf and is retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "wave_anomaly_v1", "version": "1.3",
                                                           "columns": ["hmean", "hmax", "stddev"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "wave_anomaly_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/wave_anomaly_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/wave_anomaly_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Wave Anomaly QC May 2025", "audience": "science_team",
                           "artifact_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Wave Anomaly QC May 2025"}),
        ],
        outputs=[
            "feature_set.name=wave_anomaly_v1; version=1.3; columns=hmean|hmax|stddev | "
            "file.path=/features/wave_anomaly_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_WAVE_ANOMALY_2025-05; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf | "
            "stakeholder.output_label=Wave Anomaly QC May 2025; audience=science_team; artifact_path=https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_065",
        instruction=(
            "You validate rainfall intensity QC for June-2025. End state: "
            "feature bundle 'rain_intensity_v3' (version 3.0) with columns ['avg_rate','peak_rate','duration'] is stored and retrievable; "
            "feature file '/features/rain_intensity_v3.parquet' exists and can be accessed; "
            "QC report 'QC_RAIN_INTENSITY_2025-06' is archived as pdf; "
            "stakeholder artifact 'Rainfall Intensity QC Jun 2025' (audience external_partners) points to the pdf and is accessible."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "rain_intensity_v3", "version": "3.0",
                                                           "columns": ["avg_rate", "peak_rate", "duration"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "rain_intensity_v3"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/rain_intensity_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/rain_intensity_v3.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Rainfall Intensity QC Jun 2025", "audience": "external_partners",
                           "artifact_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Rainfall Intensity QC Jun 2025"}),
        ],
        outputs=[
            "feature_set.name=rain_intensity_v3; version=3.0; columns=avg_rate|peak_rate|duration | "
            "file.path=/features/rain_intensity_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_RAIN_INTENSITY_2025-06; qc.figure_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf | "
            "stakeholder.output_label=Rainfall Intensity QC Jun 2025; audience=external_partners; artifact_path=https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_066",
        instruction=(
            "You configure the April-2025 retrain window and confirm it. End state: "
            "project settings hold retrain_window_start=2025-04-01T00:00:00Z and retrain_window_end=2025-04-30T23:59:59Z; "
            "audit log entry 'MODEL_RETRAIN_WINDOW_SET' with message 'April retrain window applied.' is recorded and readable; "
            "QC report 'QC_CONFIG_RETRAIN_2025-04' is stored as pdf and retrievable; "
            "an additional audit check verifies the same event."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {
                "retrain_window_start": "2025-04-01T00:00:00Z",
                "retrain_window_end": "2025-04-30T23:59:59Z"
            }}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_start"}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_end"}),

            Action(name="append_audit_event", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "April retrain window applied."
            }),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-04",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-04-01T00:00:00Z; config.retrain_window_end=2025-04-30T23:59:59Z | "
            "audit.event_type=MODEL_RETRAIN_WINDOW_SET; audit.message=April retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-04; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_067",
        instruction=(
            "You set a February-2026 validation checkpoint and confirm readiness. End state: "
            "project settings include validation_checkpoint '2026-02-14T14:00:00Z' and are readable; "
            "audit event 'VALIDATION_CHECKPOINT_SET' with message 'Validation checkpoint created for mid-February.' exists and is readable; "
            "QC report 'QC_CONFIG_VALIDATION_2026-02' is stored as pdf and retrievable."
        ),
        actions=[
            Action(name="patch_project_settings",
                   kwargs={"updates": {"validation_checkpoint": "2026-02-14T14:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "validation_checkpoint"}),

            Action(name="append_audit_event", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET",
                                                      "message": "Validation checkpoint created for mid-February."}),
            Action(name="read_audit_events", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
        ],
        outputs=[
            "config.validation_checkpoint=2026-02-14T14:00:00Z | "
            "audit.event_type=VALIDATION_CHECKPOINT_SET; audit.message=Validation checkpoint created for mid-February. | "
            "qc.figure_label=QC_CONFIG_VALIDATION_2026-02; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_068",
        instruction=(
            "You publish the May-2025 precipitation anomaly series and attach QC. End state: "
            "processed series 'precip_anom_2025-05' has three points "
            "[('2025-05-02T00:00:00Z', -12.5), ('2025-05-18T00:00:00Z', 8.3), ('2025-05-29T00:00:00Z', 3.1)] and is readable; "
            "QC PDF labeled 'QC_PRECIP_ANOM_2025-05' is stored and readable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "precip_anom_2025-05", "items": [
                {"timestamp": "2025-05-02T00:00:00Z", "value": -12.5},
                {"timestamp": "2025-05-18T00:00:00Z", "value": 8.3},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 3.1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "precip_anom_2025-05"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
        ],
        outputs=[
            "series.name=precip_anom_2025-05; points=3; p1.ts=2025-05-02T00:00:00Z; p1.value=-12.5; p2.ts=2025-05-18T00:00:00Z; p2.value=8.3; p3.ts=2025-05-29T00:00:00Z; p3.value=3.1 | "
            "qc.figure_label=QC_PRECIP_ANOM_2025-05; qc.figure_path=https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_069",
        instruction=(
            "You publish the June-2025 sea-level anomaly series with QC validation. End state: "
            "processed series 'sea_lvl_anom_2025-06' has three points "
            "[('2025-06-04T00:00:00Z', 0.12), ('2025-06-14T00:00:00Z', -0.05), ('2025-06-25T00:00:00Z', 0.22)] and is readable; "
            "QC PDF labeled 'QC_SEA_LVL_ANOM_2025-06' is stored and readable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "sea_lvl_anom_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 0.12},
                {"timestamp": "2025-06-14T00:00:00Z", "value": -0.05},
                {"timestamp": "2025-06-25T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "sea_lvl_anom_2025-06"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
        ],
        outputs=[
            "series.name=sea_lvl_anom_2025-06; points=3; p1.ts=2025-06-04T00:00:00Z; p1.value=0.12; p2.ts=2025-06-14T00:00:00Z; p2.value=-0.05; p3.ts=2025-06-25T00:00:00Z; p3.value=0.22 | "
            "qc.figure_label=QC_SEA_LVL_ANOM_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_070",
        instruction=(
            "You publish the July-2025 wind-speed anomaly series and attach QC. End state: "
            "processed series 'windspd_anom_2025-07' has three points "
            "[('2025-07-07T00:00:00Z', 2.5), ('2025-07-16T00:00:00Z', -1.8), ('2025-07-28T00:00:00Z', 0.9)] and is readable; "
            "QC PDF labeled 'QC_WINDSPD_ANOM_2025-07' is stored and readable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "windspd_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 2.5},
                {"timestamp": "2025-07-16T00:00:00Z", "value": -1.8},
                {"timestamp": "2025-07-28T00:00:00Z", "value": 0.9}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "windspd_anom_2025-07"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
        ],
        outputs=[
            "series.name=windspd_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=2.5; p2.ts=2025-07-16T00:00:00Z; p2.value=-1.8; p3.ts=2025-07-28T00:00:00Z; p3.value=0.9 | "
            "qc.figure_label=QC_WINDSPD_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_071",
        instruction=(
            "You publish the August-2025 humidity anomaly series with QC validation. End state: "
            "processed series 'humid_anom_2025-08' has three points "
            "[('2025-08-03T00:00:00Z', 4.0), ('2025-08-14T00:00:00Z', -2.7), ('2025-08-26T00:00:00Z', 1.5)] and is readable; "
            "QC PDF labeled 'QC_HUMID_ANOM_2025-08' is stored and readable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "humid_anom_2025-08", "items": [
                {"timestamp": "2025-08-03T00:00:00Z", "value": 4.0},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -2.7},
                {"timestamp": "2025-08-26T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "humid_anom_2025-08"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
        ],
        outputs=[
            "series.name=humid_anom_2025-08; points=3; p1.ts=2025-08-03T00:00:00Z; p1.value=4.0; p2.ts=2025-08-14T00:00:00Z; p2.value=-2.7; p3.ts=2025-08-26T00:00:00Z; p3.value=1.5 | "
            "qc.figure_label=QC_HUMID_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_072",
        instruction=(
            "You release a July-2025 wave-height anomaly series with QC evidence. End state: "
            "processed series 'wave_anom_2025-07' contains three points "
            "[('2025-07-07T00:00:00Z', 0.35), ('2025-07-18T00:00:00Z', -0.06), ('2025-07-29T00:00:00Z', 0.21)] and is retrievable; "
            "a QC PDF for label 'QC_WAVE_ANOM_2025-07' exists and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "wave_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-07-18T00:00:00Z", "value": -0.06},
                {"timestamp": "2025-07-29T00:00:00Z", "value": 0.21}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "wave_anom_2025-07"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_WAVE_ANOM_2025-07",
                "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
        ],
        outputs=[
            "series.name=wave_anom_2025-07; points=3; p1.ts=2025-07-07T00:00:00Z; p1.value=0.35; "
            "p2.ts=2025-07-18T00:00:00Z; p2.value=-0.06; p3.ts=2025-07-29T00:00:00Z; p3.value=0.21 | "
            "qc.figure_label=QC_WAVE_ANOM_2025-07; qc.figure_path=https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_073",
        instruction=(
            "You publish an August-2025 dissolved-oxygen anomaly series and attach QC. End state: "
            "processed series 'do_anom_2025-08' holds three entries "
            "[('2025-08-02T00:00:00Z', 0.18), ('2025-08-14T00:00:00Z', -0.07), ('2025-08-27T00:00:00Z', 0.10)] and is retrievable; "
            "a QC PDF for label 'QC_DO_ANOM_2025-08' exists and is retrievable."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "do_anom_2025-08", "items": [
                {"timestamp": "2025-08-02T00:00:00Z", "value": 0.18},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -0.07},
                {"timestamp": "2025-08-27T00:00:00Z", "value": 0.10}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "do_anom_2025-08"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_DO_ANOM_2025-08",
                "figure_path": "https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
        ],
        outputs=[
            "series.name=do_anom_2025-08; points=3; p1.ts=2025-08-02T00:00:00Z; p1.value=0.18; "
            "p2.ts=2025-08-14T00:00:00Z; p2.value=-0.07; p3.ts=2025-08-27T00:00:00Z; p3.value=0.10 | "
            "qc.figure_label=QC_DO_ANOM_2025-08; qc.figure_path=https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_074",
        instruction=(
            "You onboard 'XGBoost_Rainfall_v1' (v1.0) with its configuration, test score, and artifact. "
            "End state: model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is stored; "
            "profile 'default' has max_depth=5, n_estimators=150, learning_rate=0.05; "
            "test AUC=0.94 is logged; "
            "artifact '/models/XGBoost_Rainfall_v1_v1.0.json' is recorded and retrievable."
        ),
        actions=[
            Action(name="store_model_artifact", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "model_type": "xgboost",
                "framework": "xgboost",
                "version": "1.0",
                "status": "staged"
            }),
            Action(name="fetch_model_record", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="upsert_model_profile", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "profile_name": "default",
                "params": {"max_depth": 5, "n_estimators": 150, "learning_rate": 0.05}
            }),
            Action(name="read_model_profiles", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="log_model_metric", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "metric_name": "AUC",
                "value": 0.94,
                "dataset_split": "test"
            }),
            Action(name="read_model_metrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="register_file_entry", kwargs={
                "path": "/models/XGBoost_Rainfall_v1_v1.0.json",
                "mime_type": "application/json"
            }),
            Action(name="retrieve_file_entry", kwargs={"path": "/models/XGBoost_Rainfall_v1_v1.0.json"}),
        ],
        outputs=[
            "model.name=XGBoost_Rainfall_v1; type=xgboost; framework=xgboost; version=1.0; status=staged | "
            "profile.model=XGBoost_Rainfall_v1; profile.name=default; params.max_depth=5; params.n_estimators=150; params.learning_rate=0.05 | "
            "metric.model=XGBoost_Rainfall_v1; metric.name=AUC; metric.value=0.94; split=test | "
            "file.path=/models/XGBoost_Rainfall_v1_v1.0.json; file.mime=application/json"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_075",
        instruction=(
            "You register a coastal flood dataset 'flood_risk_v5' for October-2025. End state: "
            "feature bundle 'flood_risk_v5' (version '5.0') with columns ['flood_probability','storm_surge_height','risk_index'] is saved and retrievable; "
            "file '/features/flood_risk_v5.parquet' exists and is readable; "
            "QC PDF 'QC_FLOOD_RISK_2025-10' is generated; "
            "stakeholder artifact 'Flood Risk Oct 2025' (audience 'internal') links to the same pdf."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "flood_risk_v5", "version": "5.0",
                                                           "columns": ["flood_probability", "storm_surge_height",
                                                                       "risk_index"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "flood_risk_v5"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/flood_risk_v5.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/flood_risk_v5.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Flood Risk Oct 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Flood Risk Oct 2025"}),
        ],
        outputs=[
            "feature_bundle.name=flood_risk_v5; version=5.0; columns=flood_probability|storm_surge_height|risk_index | "
            "file.path=/features/flood_risk_v5.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_FLOOD_RISK_2025-10; qc.figure_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf | "
            "stakeholder.output_label=Flood Risk Oct 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_076",
        instruction=(
            "You prepare a tidal variation dataset 'tidal_variation_v3' for November-2025. End state: "
            "bundle 'tidal_variation_v3' (version '3.0') with fields ['high_tide','low_tide','tidal_range'] is stored and accessible; "
            "file '/features/tidal_variation_v3.parquet' exists and is retrievable; "
            "QC report 'QC_TIDAL_VARIATION_2025-11' is archived; "
            "stakeholder output 'Tidal Variation Nov 2025' (audience 'internal') links to the report."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "tidal_variation_v3", "version": "3.0",
                                                           "columns": ["high_tide", "low_tide", "tidal_range"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "tidal_variation_v3"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/tidal_variation_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/tidal_variation_v3.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Tidal Variation Nov 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Tidal Variation Nov 2025"}),
        ],
        outputs=[
            "feature_bundle.name=tidal_variation_v3; version=3.0; columns=high_tide|low_tide|tidal_range | "
            "file.path=/features/tidal_variation_v3.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_TIDAL_VARIATION_2025-11; qc.figure_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf | "
            "stakeholder.output_label=Tidal Variation Nov 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_077",
        instruction=(
            "You validate a 40-year NOAA precipitation archive. End state: "
            "processed series 'noaa_precip_qc_1980_2020' has points [('annual_avg', 1023.4), ('max_annual', 1820.1), ('min_annual', 540.2)] and is accessible; "
            "QC document 'QC_NOAA_PRECIP_1980_2020' is stored; "
            "stakeholder note 'NOAA Precipitation QC 1980-2020' (audience 'internal') links to the pdf."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "noaa_precip_qc_1980_2020", "items": [
                {"timestamp": "annual_avg", "value": 1023.4},
                {"timestamp": "max_annual", "value": 1820.1},
                {"timestamp": "min_annual", "value": 540.2}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "noaa_precip_qc_1980_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "NOAA Precipitation QC 1980-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "NOAA Precipitation QC 1980-2020"}),
        ],
        outputs=[
            "series.name=noaa_precip_qc_1980_2020; points=3; p1.ts=annual_avg; p1.value=1023.4; p2.ts=max_annual; p2.value=1820.1; p3.ts=min_annual; p3.value=540.2 | "
            "qc.figure_label=QC_NOAA_PRECIP_1980_2020; qc.figure_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf | "
            "stakeholder.output_label=NOAA Precipitation QC 1980-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_078",
        instruction=(
            "You QC a 20-year USGS groundwater record. End state: "
            "processed series 'usgs_groundwater_qc_2005_2025' has summary [('mean_level', 15.7), ('lowest_level', 3.4), ('highest_level', 28.1)] and is retrievable; "
            "QC file 'QC_USGS_GW_2005_2025' exists as pdf; "
            "stakeholder record 'USGS Groundwater QC 2005-2025' (audience 'internal') links to it."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "usgs_groundwater_qc_2005_2025", "items": [
                {"timestamp": "mean_level", "value": 15.7},
                {"timestamp": "lowest_level", "value": 3.4},
                {"timestamp": "highest_level", "value": 28.1}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "usgs_groundwater_qc_2005_2025"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_USGS_GW_2005_2025",
                                                    "figure_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "USGS Groundwater QC 2005-2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "USGS Groundwater QC 2005-2025"}),
        ],
        outputs=[
            "series.name=usgs_groundwater_qc_2005_2025; points=3; p1.ts=mean_level; p1.value=15.7; p2.ts=lowest_level; p2.value=3.4; p3.ts=highest_level; p3.value=28.1 | "
            "qc.figure_label=QC_USGS_GW_2005_2025; qc.figure_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf | "
            "stakeholder.output_label=USGS Groundwater QC 2005-2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_079",
        instruction=(
            "You QC a Landsat surface temperature dataset covering 1990–2020. End state: "
            "processed series 'landsat_surf_temp_qc_1990_2020' holds [('avg_temp', 22.3), ('max_temp_day', 38.7), ('min_temp_day', -4.2)] and is readable; "
            "QC artifact 'QC_LANDSAT_TEMP_1990_2020' is archived; "
            "stakeholder record 'Landsat Surface Temp QC 1990–2020' (audience 'internal') links to report."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020", "items": [
                {"timestamp": "avg_temp", "value": 22.3},
                {"timestamp": "max_temp_day", "value": 38.7},
                {"timestamp": "min_temp_day", "value": -4.2}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Landsat Surface Temp QC 1990-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Landsat Surface Temp QC 1990-2020"}),
        ],
        outputs=[
            "series.name=landsat_surf_temp_qc_1990_2020; points=3; p1.ts=avg_temp; p1.value=22.3; p2.ts=max_temp_day; p2.value=38.7; p3.ts=min_temp_day; p3.value=-4.2 | "
            "qc.figure_label=QC_LANDSAT_TEMP_1990_2020; qc.figure_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf | "
            "stakeholder.output_label=Landsat Surface Temp QC 1990-2020; audience=internal; artifact_path=https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_080",
        instruction=(
            "You QC a TRMM rainfall archive spanning 1998–2018. End state: "
            "processed series 'trmm_rainfall_qc_1998_2018' holds [('annual_avg', 105.7), ('max_daily_rain', 289.5), ('min_daily_rain', 0.0)] and is retrievable; "
            "QC report 'QC_TRMM_RAINFALL_1998_2018' exists as pdf; "
            "stakeholder note 'TRMM Rainfall QC 1998-2018' (audience 'external') links to stored pdf."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "trmm_rainfall_qc_1998_2018", "items": [
                {"timestamp": "annual_avg", "value": 105.7},
                {"timestamp": "max_daily_rain", "value": 289.5},
                {"timestamp": "min_daily_rain", "value": 0.0}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "trmm_rainfall_qc_1998_2018"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018",
                                                    "figure_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "TRMM Rainfall QC 1998-2018", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "TRMM Rainfall QC 1998-2018"}),
        ],
        outputs=[
            "series.name=trmm_rainfall_qc_1998_2018; points=3; p1.ts=annual_avg; p1.value=105.7; p2.ts=max_daily_rain; p2.value=289.5; p3.ts=min_daily_rain; p3.value=0.0 | "
            "qc.figure_label=QC_TRMM_RAINFALL_1998_2018; qc.figure_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf | "
            "stakeholder.output_label=TRMM Rainfall QC 1998-2018; audience=external; artifact_path=https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_081",
        instruction=(
            "You prepare a drought risk dataset 'drought_risk_v1' for September-2025. End state: "
            "bundle 'drought_risk_v1' (version '1.0') with fields ['soil_moisture','temperature','drought_index'] is stored and queryable; "
            "file '/features/drought_risk_v1.parquet' is present and retrievable; "
            "QC record 'QC_DROUGHT_RISK_2025-09' is archived as pdf; "
            "stakeholder artifact 'Drought Risk Sep 2025' (audience 'internal') points to 'https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf'."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "drought_risk_v1", "version": "1.0",
                                                           "columns": ["soil_moisture", "temperature",
                                                                       "drought_index"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "drought_risk_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/drought_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/drought_risk_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Drought Risk Sep 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Drought Risk Sep 2025"}),
        ],
        outputs=[
            "feature_bundle.name=drought_risk_v1; version=1.0; columns=soil_moisture|temperature|drought_index | "
            "file.path=/features/drought_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_DROUGHT_RISK_2025-09; qc.figure_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf | "
            "stakeholder.output_label=Drought Risk Sep 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_082",
        instruction=(
            "You complete sea surface temperature feature QC for June-2025. End state: "
            "bundle 'sst_features_v2' (version '2.1') with fields ['sst_mean','sst_max','sst_std'] is registered and accessible; "
            "file '/features/sst_features_v2.parquet' exists and is retrievable; "
            "QC record 'QC_SST_FEATURES_2025-06' is stored; "
            "stakeholder artifact 'SST QC June 2025' (audience 'oceanography_team') points to 'https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf'."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "sst_features_v2", "version": "2.1",
                                                           "columns": ["sst_mean", "sst_max", "sst_std"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "sst_features_v2"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/sst_features_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/sst_features_v2.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SST_FEATURES_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "SST QC June 2025", "audience": "oceanography_team",
                           "artifact_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "SST QC June 2025"}),
        ],
        outputs=[
            "feature_bundle.name=sst_features_v2; version=2.1; columns=sst_mean|sst_max|sst_std | "
            "file.path=/features/sst_features_v2.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SST_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf | "
            "stakeholder.output_label=SST QC June 2025; audience=oceanography_team; artifact_path=https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_083",
        instruction=(
            "You finalize ocean current feature QC for July-2025. End state: "
            "bundle 'ocean_current_v1' (version '1.5') with fields ['current_speed','current_dir','std_dev'] is saved and readable; "
            "file '/features/ocean_current_v1.parquet' exists and is retrievable; "
            "QC artifact 'QC_OCEAN_CURRENT_2025-07' is stored; "
            "stakeholder artifact 'Ocean Current QC July 2025' (audience 'marine_team') links to 'https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf'."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "ocean_current_v1", "version": "1.5",
                                                           "columns": ["current_speed", "current_dir", "std_dev"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "ocean_current_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/ocean_current_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/ocean_current_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Ocean Current QC July 2025", "audience": "marine_team",
                           "artifact_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Ocean Current QC July 2025"}),
        ],
        outputs=[
            "feature_bundle.name=ocean_current_v1; version=1.5; columns=current_speed|current_dir|std_dev | "
            "file.path=/features/ocean_current_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_OCEAN_CURRENT_2025-07; qc.figure_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf | "
            "stakeholder.output_label=Ocean Current QC July 2025; audience=marine_team; artifact_path=https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_084",
        instruction=(
            "You finalize ocean salinity feature QC for August-2025. End state: "
            "bundle 'salinity_index_v1' (version '1.2') with fields ['salinity_mean','salinity_max','salinity_std'] is registered and accessible; "
            "file '/features/salinity_index_v1.parquet' is available and retrievable; "
            "QC record 'QC_SALINITY_INDEX_2025-08' is archived; "
            "stakeholder artifact 'Salinity Index QC Aug 2025' (audience 'research_team') references 'https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf'."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "salinity_index_v1", "version": "1.2",
                                                           "columns": ["salinity_mean", "salinity_max",
                                                                       "salinity_std"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "salinity_index_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/salinity_index_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/salinity_index_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Salinity Index QC Aug 2025", "audience": "research_team",
                           "artifact_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Salinity Index QC Aug 2025"}),
        ],
        outputs=[
            "feature_bundle.name=salinity_index_v1; version=1.2; columns=salinity_mean|salinity_max|salinity_std | "
            "file.path=/features/salinity_index_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_SALINITY_INDEX_2025-08; qc.figure_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf | "
            "stakeholder.output_label=Salinity Index QC Aug 2025; audience=research_team; artifact_path=https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_085",
        instruction=(
            "You assemble feature set 'coastal_flood_features_v1' (v1.0) with required columns['water_level_max','wave_height_mean','precipitation_total'] and make it active. End state: "
            "feature set is retrievable; feature file '/features/coastal_flood_features_v1.parquet' exists and is retrievable; "
            "project setting 'active_feature_set' equals 'coastal_flood_features_v1'; "
            "QC PDF 'QC_COASTAL_FEATURES_2025-06' exists and is retrievable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={
                "feature_set_name": "coastal_flood_features_v1",
                "version": "1.0",
                "columns": ["water_level_max", "wave_height_mean", "precipitation_total"]
            }),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "coastal_flood_features_v1"}),

            Action(name="register_file_entry", kwargs={
                "path": "/features/coastal_flood_features_v1.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/coastal_flood_features_v1.parquet"}),

            Action(name="patch_project_settings",
                   kwargs={"updates": {"active_feature_set": "coastal_flood_features_v1"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_COASTAL_FEATURES_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"}),
        ],
        outputs=[
            "feature_set.name=coastal_flood_features_v1; version=1.0; columns=water_level_max|wave_height_mean|precipitation_total | "
            "file.path=/features/coastal_flood_features_v1.parquet; file.mime=application/parquet | "
            "config.active_feature_set=coastal_flood_features_v1 | "
            "qc.figure_label=QC_COASTAL_FEATURES_2025-06; qc.figure_path=https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_086",
        instruction=(
            "You configure a May-2025 model retrain window and verify it. End state: "
            "project settings contain retrain_window_start '2025-05-01T00:00:00Z' and retrain_window_end '2025-05-31T23:59:59Z'; "
            "audit entry 'MODEL_RETRAIN_WINDOW_SET' with message 'May retrain window applied.' is confirmed twice; "
            "QC report 'QC_CONFIG_RETRAIN_2025-05' is saved as pdf and validated."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {
                "retrain_window_start": "2025-05-01T00:00:00Z",
                "retrain_window_end": "2025-05-31T23:59:59Z"
            }}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_start"}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_end"}),

            Action(name="append_audit_event", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "May retrain window applied."
            }),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-05-01T00:00:00Z; config.retrain_window_end=2025-05-31T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=May retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_087",
        instruction=(
            "You configure a June-2025 retrain window and validate it. End state: "
            "settings show retrain_window_start '2025-06-01T00:00:00Z' and retrain_window_end '2025-06-30T23:59:59Z'; "
            "audit event 'MODEL_RETRAIN_WINDOW_SET' with message 'June retrain window applied.' is logged and checked twice; "
            "QC report 'QC_CONFIG_RETRAIN_2025-06' is generated and available as pdf."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {
                "retrain_window_start": "2025-06-01T00:00:00Z",
                "retrain_window_end": "2025-06-30T23:59:59Z"
            }}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_start"}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_end"}),

            Action(name="append_audit_event", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "June retrain window applied."
            }),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
            Action(name="record_qc_report", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-06-01T00:00:00Z; config.retrain_window_end=2025-06-30T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=June retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-06; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_088",
        instruction=(
            "You assemble a heatwave risk dataset 'heatwave_risk_v1' for 2025-08. End state: "
            "dataset 'heatwave_risk_v1' (version '1.0') with columns ['temperature','humidity','heat_risk'] is stored and retrievable; "
            "feature file '/features/heatwave_risk_v1.parquet' exists and is readable; "
            "a QC PDF exists for label 'QC_HEATWAVE_RISK_2025-08' with artifact_type 'pdf' and is accessible; "
            "stakeholder output 'Heatwave Risk Aug 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "heatwave_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "humidity", "heat_risk"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "heatwave_risk_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/heatwave_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/heatwave_risk_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Heatwave Risk Aug 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Heatwave Risk Aug 2025"}),
        ],
        outputs=[
            "feature_set.name=heatwave_risk_v1; version=1.0; columns=temperature|humidity|heat_risk | "
            "file.path=/features/heatwave_risk_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_HEATWAVE_RISK_2025-08; qc.figure_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf | "
            "stakeholder.output_label=Heatwave Risk Aug 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_089",
        instruction=(
            "You define a December-2025 backfill cutoff and verify readiness. End state: "
            "project config has backfill_cutoff '2025-12-22T20:00:00Z' and is retrievable; "
            "audit log event 'BACKFILL_CUTOFF_APPLIED' with message 'Backfill cutoff applied for end-of-year runs.' exists and is readable; "
            "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-12' with artifact_type 'pdf' and is accessible."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"backfill_cutoff": "2025-12-22T20:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "backfill_cutoff"}),

            Action(name="append_audit_event", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED",
                                                      "message": "Backfill cutoff applied for end-of-year runs."}),
            Action(name="read_audit_events", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-12-22T20:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_APPLIED; log.message=Backfill cutoff applied for end-of-year runs. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-12; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf"
        ],
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_090",
        instruction=(
            "You define a September-2025 backfill cutoff and ensure readiness. End state: "
            "project config has backfill_cutoff '2025-09-15T16:00:00Z' and is readable; "
            "audit log event 'BACKFILL_CUTOFF_CONFIRMED' with message 'September backfill cutoff completed successfully.' exists and is retrievable; "
            "a QC PDF exists for label 'QC_CONFIG_BACKFILL_2025-09' with artifact_type 'pdf' and is accessible."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"backfill_cutoff": "2025-09-15T16:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "backfill_cutoff"}),

            Action(name="append_audit_event", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED",
                                                      "message": "September backfill cutoff completed successfully."}),
            Action(name="read_audit_events", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-09-15T16:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_CONFIRMED; log.message=September backfill cutoff completed successfully. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-09; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_091",
        instruction=(
            "You publish feature set 'cargo_throughput_summary_v3' version 3.0 and mark it active. End state: "
            "feature_set 'cargo_throughput_summary_v3' with columns ['total_cargo','avg_loading_time','avg_unloading_time'] is recorded; "
            "feature file '/features/cargo_throughput_summary_v3.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'cargo_throughput_summary_v3'; "
            "a QC PDF exists for label 'QC_CARGO_THROUGHPUT_2025-03' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle",
                   kwargs={"feature_set_name": "cargo_throughput_summary_v3", "version": "3.0",
                           "columns": ["total_cargo", "avg_loading_time", "avg_unloading_time"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "cargo_throughput_summary_v3"}),

            Action(name="register_file_entry", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet",
                                                       "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet"}),

            Action(name="patch_project_settings",
                   kwargs={"updates": {"active_feature_set": "cargo_throughput_summary_v3"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_CARGO_THROUGHPUT_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
        ],
        outputs=[
            "feature_set.name=cargo_throughput_summary_v3; version=3.0; columns=total_cargo|avg_loading_time|avg_unloading_time | "
            "file.path=/features/cargo_throughput_summary_v3.parquet; file.mime=application/parquet | "
            "config.active_feature_set=cargo_throughput_summary_v3 | "
            "qc.figure_label=QC_CARGO_THROUGHPUT_2025-03; qc.figure_path=https://storage.example.com/reports/QC_CARGO_THROUGHPUT_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_092",
        instruction=(
            "You curate feature set 'port_utilization_stats_v4' version 4.2 and activate it. End state: "
            "feature_set 'port_utilization_stats_v4' with columns ['berth_occupancy','avg_turnaround_time','peak_traffic_hour'] is recorded; "
            "feature file '/features/port_utilization_stats_v4.parquet' exists and is readable; "
            "project config 'active_feature_set' equals 'port_utilization_stats_v4'; "
            "a QC PDF exists for label 'QC_PORT_UTILIZATION_2025-03' and is readable."
        ),
        actions=[
            Action(name="register_feature_bundle",
                   kwargs={"feature_set_name": "port_utilization_stats_v4", "version": "4.2",
                           "columns": ["berth_occupancy", "avg_turnaround_time", "peak_traffic_hour"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "port_utilization_stats_v4"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/port_utilization_stats_v4.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/port_utilization_stats_v4.parquet"}),

            Action(name="patch_project_settings",
                   kwargs={"updates": {"active_feature_set": "port_utilization_stats_v4"}}),
            Action(name="read_project_settings", kwargs={"key": "active_feature_set"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_PORT_UTILIZATION_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
        ],
        outputs=[
            "feature_set.name=port_utilization_stats_v4; version=4.2; columns=berth_occupancy|avg_turnaround_time|peak_traffic_hour | "
            "file.path=/features/port_utilization_stats_v4.parquet; file.mime=application/parquet | "
            "config.active_feature_set=port_utilization_stats_v4 | "
            "qc.figure_label=QC_PORT_UTILIZATION_2025-03; qc.figure_path=https://storage.example.com/reports/QC_PORT_UTILIZATION_2025-03.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_093",
        instruction=(
            "You configure a July-2025 ingestion deadline and confirm system readiness. End state: "
            "project settings include ingestion_deadline='2025-07-15T12:00:00Z' and are retrievable; "
            "audit log event 'INGESTION_DEADLINE_SET' with message 'Deadline established for mid-July ingestion.' is present; "
            "a QC report labeled 'QC_CONFIG_INGESTION_2025-07' (pdf) is registered and accessible."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"ingestion_deadline": "2025-07-15T12:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "ingestion_deadline"}),

            Action(name="append_audit_event", kwargs={"event_type": "INGESTION_DEADLINE_SET",
                                                      "message": "Deadline established for mid-July ingestion."}),
            Action(name="read_audit_events", kwargs={"event_type": "INGESTION_DEADLINE_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_INGESTION_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
        ],
        outputs=[
            "config.ingestion_deadline=2025-07-15T12:00:00Z | "
            "log.event_type=INGESTION_DEADLINE_SET; log.message=Deadline established for mid-July ingestion. | "
            "qc.figure_label=QC_CONFIG_INGESTION_2025-07; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_INGESTION_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_094",
        instruction=(
            "You set a November-2025 backfill cutoff and verify readiness. End state: "
            "project settings include backfill_cutoff='2025-11-20T18:00:00Z' and are retrievable; "
            "audit log entry 'BACKFILL_CUTOFF_SET' with message 'Backfill cutoff applied for late November runs.' is present; "
            "a QC report with label 'QC_CONFIG_BACKFILL_2025-11' (pdf) is stored and accessible."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"backfill_cutoff": "2025-11-20T18:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "backfill_cutoff"}),

            Action(name="append_audit_event", kwargs={"event_type": "BACKFILL_CUTOFF_SET",
                                                      "message": "Backfill cutoff applied for late November runs."}),
            Action(name="read_audit_events", kwargs={"event_type": "BACKFILL_CUTOFF_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-11-20T18:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_SET; log.message=Backfill cutoff applied for late November runs. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-11; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-11.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_095",
        instruction=(
            "You configure a July-2025 model retrain window and confirm readiness. End state: "
            "project settings include retrain_window_start='2025-07-01T00:00:00Z' and retrain_window_end='2025-07-31T23:59:59Z'; "
            "audit log entry 'MODEL_RETRAIN_WINDOW_SET' with message 'July retrain window applied.' exists; "
            "a QC report with label 'QC_CONFIG_RETRAIN_2025-07' (pdf) is recorded and retrievable."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"retrain_window_start": "2025-07-01T00:00:00Z",
                                                                      "retrain_window_end": "2025-07-31T23:59:59Z"}}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_start"}),
            Action(name="read_project_settings", kwargs={"key": "retrain_window_end"}),

            Action(name="append_audit_event",
                   kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "July retrain window applied."}),
            Action(name="read_audit_events", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
        ],
        outputs=[
            "config.retrain_window_start=2025-07-01T00:00:00Z; config.retrain_window_end=2025-07-31T23:59:59Z | "
            "log.event_type=MODEL_RETRAIN_WINDOW_SET; log.message=July retrain window applied. | "
            "qc.figure_label=QC_CONFIG_RETRAIN_2025-07; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_096",
        instruction=(
            "You prepare an urban flood dataset 'urban_flood_v1' for July-2025. End state: "
            "feature bundle 'urban_flood_v1' (version '1.0') with columns ['rainfall','drainage_capacity','flood_risk'] is registered; "
            "file '/features/urban_flood_v1.parquet' exists and is accessible; "
            "QC report labeled 'QC_URBAN_FLOOD_2025-07' (pdf) is available; "
            "stakeholder output 'Urban Flood Jul 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf'."
        ),
        actions=[
            Action(name="register_feature_bundle", kwargs={"feature_set_name": "urban_flood_v1", "version": "1.0",
                                                           "columns": ["rainfall", "drainage_capacity", "flood_risk"]}),
            Action(name="read_feature_bundle", kwargs={"feature_set_name": "urban_flood_v1"}),

            Action(name="register_file_entry",
                   kwargs={"path": "/features/urban_flood_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="retrieve_file_entry", kwargs={"path": "/features/urban_flood_v1.parquet"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "Urban Flood Jul 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "Urban Flood Jul 2025"}),
        ],
        outputs=[
            "feature_set.name=urban_flood_v1; version=1.0; columns=rainfall|drainage_capacity|flood_risk | "
            "file.path=/features/urban_flood_v1.parquet; file.mime=application/parquet | "
            "qc.figure_label=QC_URBAN_FLOOD_2025-07; qc.figure_path=https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf | "
            "stakeholder.output_label=Urban Flood Jul 2025; audience=internal; artifact_path=https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_097",
        instruction=(
            "You define an October-2025 backfill cutoff and validate system state. End state: "
            "project settings include backfill_cutoff='2025-10-18T17:00:00Z'; "
            "audit log entry 'BACKFILL_CUTOFF_CONFIRMED' with message 'October backfill cutoff finalized.' exists; "
            "QC report 'QC_CONFIG_BACKFILL_2025-10' (pdf) is stored and accessible."
        ),
        actions=[
            Action(name="patch_project_settings", kwargs={"updates": {"backfill_cutoff": "2025-10-18T17:00:00Z"}}),
            Action(name="read_project_settings", kwargs={"key": "backfill_cutoff"}),

            Action(name="append_audit_event",
                   kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED", "message": "October backfill cutoff finalized."}),
            Action(name="read_audit_events", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
        ],
        outputs=[
            "config.backfill_cutoff=2025-10-18T17:00:00Z | "
            "log.event_type=BACKFILL_CUTOFF_CONFIRMED; log.message=October backfill cutoff finalized. | "
            "qc.figure_label=QC_CONFIG_BACKFILL_2025-10; qc.figure_path=https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-10.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_098",
        instruction=(
            "You assemble tidal range observations for July-2025, verify QC, and circulate a local authority note. "
            "End state: processed series 'tide_range_2025-07' records three values "
            "[('2025-07-05T00:00:00Z', 2.67), ('2025-07-18T00:00:00Z', 3.02), ('2025-07-31T00:00:00Z', 2.88)] and can be retrieved; "
            "a QC document 'QC_TIDE_RANGE_2025-07' (pdf) is generated and accessible; "
            "a stakeholder deliverable 'July 2025 Tidal Range Brief' (audience 'municipal') points to that QC file."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "tide_range_2025-07", "items": [
                {"timestamp": "2025-07-05T00:00:00Z", "value": 2.67},
                {"timestamp": "2025-07-18T00:00:00Z", "value": 3.02},
                {"timestamp": "2025-07-31T00:00:00Z", "value": 2.88}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "tide_range_2025-07"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "July 2025 Tidal Range Brief", "audience": "municipal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "July 2025 Tidal Range Brief"}),
        ],
        outputs=[
            "series.name=tide_range_2025-07; points=3; p1.ts=2025-07-05T00:00:00Z; p1.value=2.67; "
            "p2.ts=2025-07-18T00:00:00Z; p2.value=3.02; p3.ts=2025-07-31T00:00:00Z; p3.value=2.88 | "
            "qc.figure_label=QC_TIDE_RANGE_2025-07; qc.figure_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf | "
            "stakeholder.output_label=July 2025 Tidal Range Brief; audience=municipal; artifact_path=https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_099",
        instruction=(
            "You generate mean tidal levels for August-2025, check QC, and provide a summary for state agencies. "
            "End state: processed series 'tide_mean_2025-08' holds three records "
            "[('2025-08-04T00:00:00Z', 1.87), ('2025-08-17T00:00:00Z', 2.01), ('2025-08-30T00:00:00Z', 1.95)] and is available; "
            "QC output 'QC_TIDE_MEAN_2025-08' (pdf) is saved; "
            "a stakeholder note 'August 2025 Mean Tide Brief' (audience 'state') references the QC document."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "tide_mean_2025-08", "items": [
                {"timestamp": "2025-08-04T00:00:00Z", "value": 1.87},
                {"timestamp": "2025-08-17T00:00:00Z", "value": 2.01},
                {"timestamp": "2025-08-30T00:00:00Z", "value": 1.95}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "tide_mean_2025-08"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "August 2025 Mean Tide Brief", "audience": "state",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "August 2025 Mean Tide Brief"}),
        ],
        outputs=[
            "series.name=tide_mean_2025-08; points=3; p1.ts=2025-08-04T00:00:00Z; p1.value=1.87; "
            "p2.ts=2025-08-17T00:00:00Z; p2.value=2.01; p3.ts=2025-08-30T00:00:00Z; p3.value=1.95 | "
            "qc.figure_label=QC_TIDE_MEAN_2025-08; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf | "
            "stakeholder.output_label=August 2025 Mean Tide Brief; audience=state; artifact_path=https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"
        ],
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_100",
        instruction=(
            "You prepare tidal minimum readings for May-2025, validate QC, and draft a report for coastal teams. "
            "End state: processed series 'tide_min_2025-05' contains three entries "
            "[('2025-05-03T00:00:00Z', 0.42), ('2025-05-16T00:00:00Z', 0.35), ('2025-05-29T00:00:00Z', 0.50)] retrievable from storage; "
            "QC record 'QC_TIDE_MIN_2025-05' (pdf) is archived; "
            "a stakeholder artifact 'May 2025 Tide Min Summary' (audience 'coastal') points to the QC file."
        ),
        actions=[
            Action(name="write_processed_series", kwargs={"series_name": "tide_min_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": 0.42},
                {"timestamp": "2025-05-16T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 0.50}
            ]}),
            Action(name="read_processed_series", kwargs={"series_name": "tide_min_2025-05"}),

            Action(name="render_qc_report", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),
            Action(name="record_qc_report", kwargs={"figure_label": "QC_TIDE_MIN_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="read_qc_report", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),

            Action(name="record_stakeholder_artifact",
                   kwargs={"output_label": "May 2025 Tide Min Summary", "audience": "coastal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"}),
            Action(name="read_stakeholder_artifact", kwargs={"output_label": "May 2025 Tide Min Summary"}),
        ],
        outputs=[
            "series.name=tide_min_2025-05; points=3; p1.ts=2025-05-03T00:00:00Z; p1.value=0.42; "
            "p2.ts=2025-05-16T00:00:00Z; p2.value=0.35; p3.ts=2025-05-29T00:00:00Z; p3.value=0.50 | "
            "qc.figure_label=QC_TIDE_MIN_2025-05; qc.figure_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf | "
            "stakeholder.output_label=May 2025 Tide Min Summary; audience=coastal; artifact_path=https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"
        ],
    )
]
